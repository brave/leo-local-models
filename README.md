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
