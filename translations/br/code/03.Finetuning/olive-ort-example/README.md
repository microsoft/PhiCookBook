<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-09T04:31:43+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "br"
}
-->
# Fine-tune Phi3 gamit ang Olive

Sa halimbawa na ito, gagamitin mo ang Olive para:

1. I-fine-tune ang LoRA adapter para i-classify ang mga parirala bilang Sad, Joy, Fear, Surprise.
1. Pagsamahin ang mga timbang ng adapter sa base model.
1. I-optimize at i-quantize ang modelo sa `int4`.

Ipapakita rin namin kung paano mag-inference gamit ang fine-tuned na modelo gamit ang ONNX Runtime (ORT) Generate API.

> **⚠️ Para sa Fine-tuning, kailangan mong magkaroon ng angkop na GPU - halimbawa, A10, V100, A100.**

## 💾 Install

Gumawa ng bagong Python virtual environment (halimbawa, gamit ang `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Sunod, i-install ang Olive at ang mga dependencies para sa fine-tuning workflow:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Fine-tune Phi3 gamit ang Olive
Ang [Olive configuration file](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) ay naglalaman ng *workflow* na may mga sumusunod na *passes*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Sa pangkalahatan, ang workflow na ito ay:

1. I-fine-tune ang Phi3 (sa loob ng 150 steps, na pwede mong baguhin) gamit ang data mula sa [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Pagsamahin ang mga timbang ng LoRA adapter sa base model. Magkakaroon ka ng isang model artifact sa ONNX format.
1. I-o-optimize ng Model Builder ang modelo para sa ONNX runtime *at* i-quantize ang modelo sa `int4`.

Para patakbuhin ang workflow, gamitin ang:

```bash
olive run --config phrase-classification.json
```

Kapag natapos na ang Olive, ang optimized na `int4` fine-tuned Phi3 model ay makikita sa: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Isama ang fine-tuned na Phi3 sa iyong application

Para patakbuhin ang app:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Ang sagot ay isang salita lamang na classification ng parirala (Sad/Joy/Fear/Surprise).

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.