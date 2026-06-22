# leo-local-models

Keep track of the local models that Leo uses in brave-core.

## Resources

### Page content refine (Deprecated)
- [Currently use Text Embedder model](https://www.kaggle.com/models/google/universal-sentence-encoder-qa-ondevice/tfLite/universal-sentence-encoder-qa-ondevice/)
- [Text Embedder Model compatibility](https://www.tensorflow.org/lite/inference_with_metadata/task_library/text_embedder)

### EmbeddingGemma

- We use `config.json` and `tokenizer.json` from [Google](https://huggingface.co/google/embeddinggemma-300m/tree/main)
- Quantized model file is from [Unsloth AI](https://huggingface.co/unsloth/embeddinggemma-300m-GGUF/tree/main)
- 2_Dense and 3_Dense files are from [Google](https://huggingface.co/google/embeddinggemma-300m-qat-q4_0-unquantized/tree/main)

### Nemotron Speech Streaming (int4 ONNX, English only)

- Original model is [nvidia/nemotron-speech-streaming-en-0.6b](https://huggingface.co/nvidia/nemotron-speech-streaming-en-0.6b)
- `encoder.onnx`, `encoder.onnx.data`, `decoder_joint.onnx` and `decoder_joint.onnx.data` are the int4 ONNX export from [altunenes/parakeet-rs](https://huggingface.co/altunenes/parakeet-rs/tree/main/nemotron-speech-streaming-en-0.6b), re-saved so the weights live in `*.onnx.data` sidecars following [Converting and Saving an ONNX Model to External Data](https://onnx.ai/onnx/repo-docs/ExternalData.html#converting-and-saving-an-onnx-model-to-external-data)
- `filterbank.bin` is from [danielbodart/nemotron-speech-600m-onnx](https://huggingface.co/danielbodart/nemotron-speech-600m-onnx/blob/main/shared/filterbank.bin)
- `tokens.txt` is from [danielbodart/nemotron-speech-600m-onnx](https://huggingface.co/danielbodart/nemotron-speech-600m-onnx/blob/main/shared/tokens.txt)
