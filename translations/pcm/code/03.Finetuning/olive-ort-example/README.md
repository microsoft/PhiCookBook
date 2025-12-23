<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-12-21T16:49:02+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "pcm"
}
-->
# Fine-tune Phi3 using Olive

For dis example you go use Olive to:

1. Fine-tune one LoRA adapter to classify phrases into Sad, Joy, Fear, Surprise.
1. Merge di adapter weights into di base model.
1. Optimize and quantize di model into `int4`.

> **⚠️ For fine-tuning, you go need GPU wey fit handle am - for example, an A10, V100, A100.**

## 💾 Install

Create new Python virtual environment (for example, you fit use `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Next, install Olive and di dependencies wey you need for a fine-tuning workflow:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Fine-tune Phi3 using Olive
Di [Olive configuration file](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) contains a *workflow* with the following *passes*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

For high-level, dis workflow go:

1. Fine-tune Phi3 (for 150 steps, wey you fit change) using the [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json) data.
1. Merge di LoRA adapter weights into di base model. Dis go give you one single model artifact for ONNX format.
1. Model Builder go optimize di model for di ONNX runtime *and* go quantize di model into `int4`.

To run di workflow, run:

```bash
olive run --config phrase-classification.json
```

When Olive don complete, your optimized `int4` fine-tuned Phi3 model go dey available for: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrate fine-tuned Phi3 into your application 

To run di app:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Di response suppose be one single word wey classify di phrase (Sad/Joy/Fear/Surprise).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dis document don translate wit AI translation service [Co-op Translator] (https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg sabi say automated translation fit get mistakes or wrong parts. The original document for im original language na the main authoritative source. If na important matter, make you use professional human translator. We no dey liable for any misunderstanding or wrong interpretation wey fit result from this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->