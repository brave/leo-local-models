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
- `litert/embeddinggemma-300M_seq512_mixed-precision.tflite` and `litert/sentencepiece.model` are from [litert-community](https://huggingface.co/litert-community/embeddinggemma-300m/tree/main)

### Nemotron Speech Streaming (int4 ONNX, English only)

- Original model is [nvidia/nemotron-speech-streaming-en-0.6b](https://huggingface.co/nvidia/nemotron-speech-streaming-en-0.6b)
- The quantized model is derived from the original `.nemo` model using our own scripts at [brave-experiments/ASR_Evaluations](https://github.com/brave-experiments/ASR_Evaluations/tree/main/ASR_Quantizations):
  - `export_nemotron_cache_onnx.py` converts the `.nemo` model to ONNX, and also extracts `filterbank.bin` and `tokens.txt` from the `.nemo` model.
  - `quantize_encoder_int4_weight_only.py` quantizes the encoder to int4 weight-only format. The combined decoder and joint network (`decoder_joint.onnx`) is left unchanged since it is tiny in comparison.
- The encoder weights live in `*.onnx.data` sidecars following [Converting and Saving an ONNX Model to External Data](https://onnx.ai/onnx/repo-docs/ExternalData.html#converting-and-saving-an-onnx-model-to-external-data).
- Note that, even though it is named int4 quantization, it is actually mixed precision: only `MatMul` ops with a constant weight tensor as the right-hand input are quantized to int4. Most other weights, biases, normalization parameters, etc. are kept in their original precision. An `accuracy_level` of 4 is set, which means the `MatMulNBits` kernels are permitted to use internal INT8 activation computation at run-time.
