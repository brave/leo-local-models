# tools/

## `generate_passage_embeddings_model_info.py`

Generates the `model-info.pb` in a model dir — the metadata file the browser
reads out of the component. It is the same `optimization_guide.proto.ModelInfo`
message Chrome's own model packages ship, so the model version, the embedder
metadata and the companion file names travel with the model instead of being
hard-coded in the browser binary.

```sh
pip install -r tools/requirements.txt
# regenerate
./tools/generate_passage_embeddings_model_info.py embeddinggemma-300m/litert
# is the checked in .pb current?
./tools/generate_passage_embeddings_model_info.py --check \
    embeddinggemma-300m/litert
```

The values to encode live in `model-info.json` next to the model, so the binary
is the output of a reviewable text file; only the companion file names are read
off the model dir. **Bump `version` whenever the model changes** — the browser
stores it alongside every embedding, and a change is what makes it re-embed
history instead of comparing vectors from two different models. Update
`input_window_size` and `output_size` with it, since they describe the model's
tensors.

Any model dir laid out the way optimization guide expects will do, but the
metadata it writes is passage-embeddings specific: it targets
`OPTIMIZATION_TARGET_PASSAGE_EMBEDDER` and fills a
`PassageEmbeddingsModelMetadata`. A different optimization target needs its own
generator next to this one.

## `proto/`, `proto_gen/`

`proto/` vendors the three Chromium `.proto` files the message is built from,
and `proto_gen/` holds the Python bindings compiled from them, so generating
the metadata only needs the protobuf runtime.

Refresh both when upstream changes those messages — nothing else requires it,
and a refresh usually leaves `model-info.pb` byte for byte identical:

```sh
./tools/regenerate_protos.sh <path to a chromium src/ checkout>
# did the refresh change the bytes?
./tools/generate_passage_embeddings_model_info.py --check \
    embeddinggemma-300m/litert
```

The script copies the protos verbatim, records the checkout's version in
`proto/CHROMIUM_VERSION`, and recompiles the bindings with the `protoc` that
`grpcio-tools` bundles. Check in `proto/`, `proto/CHROMIUM_VERSION` and
`proto_gen/` together.
