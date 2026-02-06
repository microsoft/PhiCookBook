# Fine-tune Phi3 wit Olive

For dis example you go use Olive to:

1. Fine-tune LoRA adapter make e fit classify phrases into Sad, Joy, Fear, Surprise.
1. Merge di adapter weights into di base model.
1. Optimize and Quantize di model into `int4`.

We go still show you how to run inference on di fine-tuned model using di ONNX Runtime (ORT) Generate API.

> **⚠️ For fine-tuning, you go need a correct GPU wey dey available - for example, an A10, V100, A100.**

## 💾 Install

Create new Python virtual environment (for example, using `conda`):

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
Di [Olive configuration file](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) get one *workflow* wey get di following *passes*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

At a high-level, dis workflow go:

1. Fine-tune Phi3 (for 150 steps, wey you fit change) using di [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json) data.
1. Merge the LoRA adapter weights into the base model. Dis go give you one single model artifact for di ONNX format.
1. Model Builder go optimize di model for di ONNX runtime *and* quantize di model into `int4`.

To run di workflow, run:

```bash
olive run --config phrase-classification.json
```

When Olive don finish, your optimized `int4` fine-tuned Phi3 model go dey for: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrate di fine-tuned Phi3 inside your application 

To run di app:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

This response suppose be one single word wey classify the phrase (Sad/Joy/Fear/Surprise).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Make una sabi:
Dis document dem translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg note say automated translations fit get mistakes or incorrect parts. The original document wey dey im own language na the correct/official source. If na important information, e better make professional human translator check am. We no go responsible for any misunderstanding or wrong interpretation wey fit result from using this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->