<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-07-16T16:28:52+00:00",
  "source_file": "code/04.Finetuning/olive-ort-example/README.md",
  "language_code": "sl"
}
-->
# Prilagodite Phi3 z uporabo Olive

V tem primeru boste z Olive:

1. Prilagodili LoRA adapter za razvrščanje fraz v kategorije Žalost, Veselje, Strah, Presenečenje.
1. Združili uteži adapterja v osnovni model.
1. Optimizirali in kvantizirali model v `int4`.

Prikazali vam bomo tudi, kako izvesti inferenco prilagojenega modela z uporabo ONNX Runtime (ORT) Generate API.

> **⚠️ Za prilagajanje potrebujete ustrezno GPU napravo - na primer A10, V100, A100.**

## 💾 Namestitev

Ustvarite novo Python virtualno okolje (na primer z `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Nato namestite Olive in odvisnosti za potek dela prilagajanja:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Prilagodite Phi3 z uporabo Olive
[Olive konfiguracijska datoteka](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) vsebuje *potek dela* z naslednjimi *koraki*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Na visoki ravni bo ta potek dela:

1. Prilagodil Phi3 (150 korakov, kar lahko spremenite) z uporabo podatkov iz [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Združil uteži LoRA adapterja v osnovni model. Tako boste dobili en sam model v ONNX formatu.
1. Model Builder bo optimiziral model za ONNX runtime *in* kvantiziral model v `int4`.

Za zagon poteka dela izvedite:

```bash
olive run --config phrase-classification.json
```

Ko Olive konča, je vaš optimiziran `int4` prilagojeni Phi3 model na voljo v: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Vključite prilagojeni Phi3 v vašo aplikacijo

Za zagon aplikacije:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Odgovor naj bo enotna besedna klasifikacija fraze (Žalost/Veselje/Strah/Presenečenje).

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.