#!/usr/bin/env python3
"""Generates model-info.pb for a LiteRT passage embeddings model.

Brave's passage embeddings controller reads this file out of the component, the
same way Chrome's own model packages ship a `model-info.pb` next to the model.
It carries the model version plus the embedder metadata, so those numbers travel
with the .tflite instead of being hard-coded in the browser binary.

Everything is addressed by the model dir, whose layout follows what
optimization guide expects: `model.tflite`, `model-info.pb`, and any companion
files the model needs. `model-info.json` sits alongside them holding the values
to encode, so the .pb is a reviewable text file's output rather than something
hand-assembled.

Regenerate after editing model-info.json, and check the two in together:

    ./tools/generate_passage_embeddings_model_info.py <model dir>

To confirm the checked in .pb is current (for CI or a pre-commit hook):

    ./tools/generate_passage_embeddings_model_info.py --check <model dir>

`version` MUST be bumped whenever the model changes: the browser stores it
alongside every embedding, and a change is what makes it re-embed history
instead of comparing vectors produced by two different models.
`input_window_size` and `output_size` describe the model's tensors, so they need
updating with it too.

Any such model dir will do, but the metadata written is passage-embeddings
specific -- the optimization target and the metadata message. Another
optimization target wants its own generator rather than a mode of this one.

The message is built with Chromium's own .proto definitions, vendored under
tools/proto/ and compiled to tools/proto_gen/ (see tools/README.md). Install the
runtime with `pip install -r tools/requirements.txt`.
"""

import argparse
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent / 'proto_gen'))

try:
    from components.optimization_guide.proto import models_pb2
    from components.optimization_guide.proto \
        import passage_embeddings_model_metadata_pb2 as metadata_pb2
except Exception as e:
    # Either the runtime is missing, or it is older than the bindings, which
    # protobuf refuses to load.
    sys.exit(f'error: {e}\n'
             f'       install the protobuf runtime with '
             f'`pip install -r tools/requirements.txt` (needs Python 3.10+)')

# ModelInfo.model_metadata is optimization_guide's own copy of Any rather than
# google.protobuf.Any, so the runtime's Pack() is unavailable and type_url has
# to be filled the way upstream's AnyWrapProto() does: this prefix plus the
# message's fully qualified name.
# components/optimization_guide/core/optimization_guide_proto_util.cc
TYPE_URL_PREFIX = 'type.googleapis.com/'

CONFIG_NAME = "model-info.json"

# Optimization guide resolves both of these by fixed name, and lists everything
# else the model needs in ModelInfo.additional_files as basenames relative to
# the model dir.
# GetBaseFileNameForModels(), GetBaseFileNameForModelInfo(),
# components/optimization_guide/core/delivery/model_util.cc
MODEL_NAME = "model.tflite"
OUTPUT_NAME = "model-info.pb"


def build_model_info(config, additional_files):
    metadata = metadata_pb2.PassageEmbeddingsModelMetadata(
        input_window_size=config['input_window_size'],
        output_size=config['output_size'],
        score_threshold=config['score_threshold'])

    model_info = models_pb2.ModelInfo(
        # Upstream rejects a model-info.pb without version and
        # optimization_target, so set it even though our component path does
        # not go through that downloader.
        # PredictionModelDownloadManager::ProcessUnzippedContents(),
        # components/optimization_guide/core/delivery/
        # prediction_model_download_manager.cc
        optimization_target=models_pb2.OPTIMIZATION_TARGET_PASSAGE_EMBEDDER,
        version=config['version'])
    model_info.model_metadata.type_url = \
        TYPE_URL_PREFIX + metadata.DESCRIPTOR.full_name
    model_info.model_metadata.value = metadata.SerializeToString()
    for name in additional_files:
        model_info.additional_files.add().file_path = name
    return model_info


# --- config ------------------------------------------------------------------

# Every value the .pb carries, other than the file names read off the model dir.
COUNTS = ('version', 'input_window_size', 'output_size')
KEYS = COUNTS + ('score_threshold',)


def load_config(path):
    if not path.is_file():
        sys.exit(f'error: no such config: {path}\n'
                 f'       expected a JSON file with the key(s) '
                 f'{sorted(KEYS)}')
    try:
        config = json.loads(path.read_text())
    except json.JSONDecodeError as e:
        sys.exit(f'error: {path} is not valid JSON: {e}')

    unknown = set(config) - set(KEYS)
    if unknown:
        sys.exit(f'error: {path} has unknown key(s): {sorted(unknown)}')
    missing = set(KEYS) - set(config)
    if missing:
        sys.exit(f'error: {path} is missing key(s): {sorted(missing)}')
    for key in COUNTS:
        if not isinstance(config[key], int) or config[key] < 1:
            sys.exit(f'error: {path}: "{key}" must be a positive integer')
    if not 0.0 <= config['score_threshold'] <= 1.0:
        sys.exit(f'error: {path}: "score_threshold" must be within [0.0, 1.0]')
    return config


def discover_additional_files(model):
    """Every other file the model dir ships, as basenames.

    Optimization guide resolves these relative to the model dir, and neither
    this tool's input nor its output is part of the model, so both are excluded.
    """
    generated = {model.name, CONFIG_NAME, OUTPUT_NAME}
    return sorted(entry.name for entry in model.parent.iterdir()
                  if entry.is_file() and entry.name not in generated
                  and not entry.name.startswith('.'))


# --- main --------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'model_dir', type=pathlib.Path,
        help=f'model dir holding {MODEL_NAME}, {CONFIG_NAME} and any '
             f'companion files; {OUTPUT_NAME} is written into it')
    parser.add_argument(
        '--check', action='store_true',
        help='verify the checked in .pb matches the config and the model dir '
             'instead of writing it; exits non-zero if it is stale')
    args = parser.parse_args()

    if not args.model_dir.is_dir():
        sys.exit(f'error: no such model dir: {args.model_dir}')
    model = args.model_dir / MODEL_NAME
    if not model.is_file():
        sys.exit(f'error: no {MODEL_NAME} in {args.model_dir}; optimization '
                 f'guide resolves the model by that fixed name')

    config_path = args.model_dir / CONFIG_NAME
    out_path = args.model_dir / OUTPUT_NAME

    config = load_config(config_path)
    additional_files = discover_additional_files(model)
    blob = build_model_info(config, additional_files).SerializeToString()

    if args.check:
        if not out_path.is_file():
            sys.exit(f'error: {out_path} is missing; run '
                     f'{pathlib.Path(sys.argv[0]).name} to generate it')
        if out_path.read_bytes() != blob:
            sys.exit(f'error: {out_path} is stale -- it does not match '
                     f'{config_path.name} and the files in {args.model_dir}; '
                     f'regenerate it with {pathlib.Path(sys.argv[0]).name}')
        print(f'{out_path} is up to date ('
              + ', '.join(f'{key} {config[key]}' for key in KEYS) + ')')
        return

    out_path.write_bytes(blob)
    print(f'config            {config_path.name}')
    for key in KEYS:
        print(f'  {key:<17} {config[key]}')
    print(f'model             {model.name}')
    print(f'  additional      {", ".join(additional_files) or "(none)"}')
    print(f'wrote             {out_path.name} ({len(blob)} bytes)')


if __name__ == '__main__':
    main()
