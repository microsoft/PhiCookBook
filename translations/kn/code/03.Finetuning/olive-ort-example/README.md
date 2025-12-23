<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-12-21T16:52:31+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "kn"
}
-->
# Olive ಬಳಸಿ Phi3 ಅನ್ನು ಸೂಕ್ಷ್ಮ-ಸಂಯೋಜನೆ (Fine-tune) ಮಾಡುವುದು

In this example you'll use Olive to:

1. Fine-tune a LoRA adapter to classify phrases into Sad, Joy, Fear, Surprise.
1. Merge the adapter weights into the base model.
1. Optimize and Quantize the model into `int4`.

We'll also show you how to inference the fine-tuned model using the ONNX Runtime (ORT) Generate API.

> **⚠️ ಸೂಕ್ಷ್ಮ-ಸಂಯೋಜನೆಗಾಗಿ, ನಿಮ್ಮ ಬಳಿ ಸೂಕ್ತ GPU ಲಭ್ಯವಿರಬೇಕು - ಉದಾಹರಣೆಗೆ, A10, V100, A100.**

## 💾 ಸ್ಥಾಪನೆ

Create a new Python virtual environment (for example, using `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Next, install the Olive and the dependencies for a fine-tuning workflow:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Olive ಬಳಸಿ Phi3 ಅನ್ನು ಸೂಕ್ಷ್ಮ-ಸಂಯೋಜನೆ (Fine-tune) ಮಾಡಿ
The [Olive configuration file](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) contains a *workflow* with the following *passes*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

At a high-level, this workflow will:

1. [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json) ಡೇಟಾ ಬಳಸಿ Phi3 ಅನ್ನು ಸೂಕ್ಷ್ಮ-ಸಂಯೋಜನೆ ಮಾಡುವುದು (150 ಹೆಜ್ಜೆಗಳಿಗಾಗಿ, ನೀವು ಇದನ್ನು ಬದಲಾಯಿಸಬಹುದು).
1. LoRA ಅಡಾಪ್ಟರ್ ತೂಕಗಳನ್ನು ಬೇಸ್ ಮಾದರಿಯಲ್ಲಿ ವಿಲೀನಗೊಳಿಸುವುದು. ಇದರಿಂದ ನಿಮಗೆ ONNX ಫಾರ್ಮ್ಯಾಟ್‌ನಲ್ಲಿ ಒಂದೇ ಮಾದರಿ ಆರ್ಟಿಫ್ಯಾಕ್ ಸಿಗುತ್ತದೆ.
1. Model Builder ONNX runtime ಗೆ ಪ್ರಯುಕ್ತವಾಗುವಂತೆ ಮಾದರಿಯನ್ನು ಆಪ್ಟಿಮೈಸ್ ಮಾಡುತ್ತದೆ *ಮತ್ತು* ಮಾದರಿಯನ್ನು `int4` ಗೆ ಕ್ವಾಂಟೈಜ್ ಮಾಡುತ್ತದೆ.

To execute the workflow, run:

```bash
olive run --config phrase-classification.json
```

When Olive has completed, you're optimized `int4` fine-tuned Phi3 model is available in: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 ಸೂಕ್ಷ್ಮ-ಸಂಯೋಜಿತ Phi3 ಅನ್ನು ನಿಮ್ಮ ಅಪ್ಲಿಕೇಶನ್‌ಗೆ ಒಗ್ಗೂಡಿಸುವುದು

To run the app:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

This response should be a single word classification of the phrase (Sad/Joy/Fear/Surprise).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ನಿರಾಕರಣೆ:
ಈ ದಸ್ತಾವೇಜನ್ನು AI ಅನುವಾದಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವದಿಸಲಾಗಿದೆ. ನಾವು ಶುದ್ಧತೆಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ ಸಹ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರುವ ಸಂಭವನೀಯತೆ ಇದೆ ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿ ಇರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆನ್ನಿಸಿ ಪರಿಗಣಿಸಬೇಕು. ಗಂಭೀರ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ಅಸಮoju? (ಅಸಮಂಜಸ್ಯತೆಗಳು) ಅಥವಾ ತಪ್ಪು ಅರ್ಥಗರ್ಭಿತಕ್ಕಾಗಿ ನಾವು ಜವಾಬ್ದಾರಿಯಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->