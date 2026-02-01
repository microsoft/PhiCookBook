# Fine-tune ang Phi3 gamit ang Olive

Sa halimbawang ito, gagamitin mo ang Olive para:

1. I-fine-tune ang isang LoRA adapter upang iklasipika ang mga parirala bilang Sad, Joy, Fear, Surprise.
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

## 🧪 Fine-tune ang Phi3 gamit ang Olive
Ang [Olive configuration file](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) ay naglalaman ng *workflow* na may mga sumusunod na *passes*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Sa pangkalahatan, ang workflow na ito ay:

1. I-fine-tune ang Phi3 (sa loob ng 150 na hakbang, na maaari mong baguhin) gamit ang data mula sa [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Pagsamahin ang mga timbang ng LoRA adapter sa base model. Magkakaroon ka ng isang model artifact sa ONNX format.
1. I-o-optimize ng Model Builder ang modelo para sa ONNX runtime *at* i-quantize ang modelo sa `int4`.

Para patakbuhin ang workflow, gamitin ang:

```bash
olive run --config phrase-classification.json
```

Kapag natapos na ang Olive, ang optimized na `int4` fine-tuned na Phi3 model ay makikita sa: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Isama ang fine-tuned na Phi3 sa iyong aplikasyon

Para patakbuhin ang app:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Ang sagot ay dapat isang salita na klasipikasyon ng parirala (Sad/Joy/Fear/Surprise).

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.