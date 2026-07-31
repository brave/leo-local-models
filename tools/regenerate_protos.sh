#!/usr/bin/env bash
# Refreshes the vendored optimization guide protos from a Chromium checkout and
# recompiles the Python bindings. Only needed when Chromium changes the messages
# in tools/proto/; the generators run off the checked in bindings.
#
#   ./tools/regenerate_protos.sh ~/Projects/brave-browser/src
#
# The checkout's version is recorded in proto/CHROMIUM_VERSION; check that in
# with the updated .proto files and the regenerated bindings.

set -euo pipefail

PROTOS=(
  components/optimization_guide/proto/models.proto
  components/optimization_guide/proto/common_types.proto
  components/optimization_guide/proto/passage_embeddings_model_metadata.proto
)

tools_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [[ $# -ne 1 ]]; then
  echo "usage: $(basename "$0") <path to a chromium src/ checkout>" >&2
  exit 1
fi
chromium_src="$1"

version_file="${chromium_src}/chrome/VERSION"
[[ -f "${version_file}" ]] ||
  { echo "error: not a chromium checkout: ${chromium_src}" >&2; exit 1; }
chromium_version="$(sed -n 's/^[A-Z]*=//p' "${version_file}" | paste -sd. -)"

# Staged, then swapped in at the end: protoc only ever writes, so the
# destinations have to be emptied to drop bindings for protos that went away,
# and doing that in place would leave a failed run with no usable bindings.
stage="$(mktemp -d "${tools_dir}/.regen.XXXXXX")"
trap 'rm -rf "${stage}"' EXIT

for proto in "${PROTOS[@]}"; do
  src="${chromium_src}/${proto}"
  [[ -f "${src}" ]] || { echo "error: no such proto: ${src}" >&2; exit 1; }
  mkdir -p "${stage}/proto/$(dirname "${proto}")"
  cp "${src}" "${stage}/proto/${proto}"
done
echo "${chromium_version}" > "${stage}/proto/CHROMIUM_VERSION"

mkdir -p "${stage}/proto_gen"
python3 -m grpc_tools.protoc \
  -I "${stage}/proto" \
  --python_out="${stage}/proto_gen" \
  --pyi_out="${stage}/proto_gen" \
  "${PROTOS[@]}"

rm -rf "${tools_dir}/proto" "${tools_dir}/proto_gen"
mv "${stage}/proto" "${stage}/proto_gen" "${tools_dir}/"

echo "regenerated from Chromium ${chromium_version}; check in proto/ and"
echo "proto_gen/, then re-run the generators with --check to see whether the"
echo "refreshed definitions changed any model-info.pb"
