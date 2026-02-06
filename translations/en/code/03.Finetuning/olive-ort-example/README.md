# Fine-tune Phi3 using Olive

In this example, you'll use Olive to:

1. Fine-tune a LoRA adapter to classify phrases into Sad, Joy, Fear, Surprise.  
1. Merge the adapter weights into the base model.  
1. Optimize and Quantize the model into `int4`.  

We'll also show you how to run inference on the fine-tuned model using the ONNX Runtime (ORT) Generate API.

> **⚠️ For Fine-tuning, you'll need to have a suitable GPU available - for example, an A10, V100, A100.**

## 💾 Install

Create a new Python virtual environment (for example, using `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Next, install Olive and the dependencies for a fine-tuning workflow:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Fine-tune Phi3 using Olive
The [Olive configuration file](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) contains a *workflow* with the following *passes*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

At a high level, this workflow will:

1. Fine-tune Phi3 (for 150 steps, which you can adjust) using the [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json) data.  
1. Merge the LoRA adapter weights into the base model. This will produce a single model artifact in the ONNX format.  
1. Model Builder will optimize the model for the ONNX runtime *and* quantize the model into `int4`.  

To run the workflow, execute:

```bash
olive run --config phrase-classification.json
```

When Olive finishes, your optimized `int4` fine-tuned Phi3 model will be available at: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrate fine-tuned Phi3 into your application

To run the app:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

The response will be a single-word classification of the phrase (Sad/Joy/Fear/Surprise).

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.