<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-09-12T15:02:39+00:00",
  "source_file": "code/04.Finetuning/olive-ort-example/README.md",
  "language_code": "lt"
}
-->
# Tobulinkite Phi3 naudodami Olive

Šiame pavyzdyje naudosite Olive, kad:

1. Tobulintumėte LoRA adapterį frazių klasifikavimui į kategorijas: Liūdesys, Džiaugsmas, Baimė, Nustebimas.
1. Sujungtumėte adapterio svorius su pagrindiniu modeliu.
1. Optimizuotumėte ir kvantizuotumėte modelį į `int4`.

Taip pat parodysime, kaip atlikti išvestį su patobulintu modeliu naudojant ONNX Runtime (ORT) Generate API.

> **⚠️ Tobulinimui reikės tinkamo GPU - pavyzdžiui, A10, V100, A100.**

## 💾 Įdiegimas

Sukurkite naują Python virtualią aplinką (pavyzdžiui, naudojant `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Tada įdiekite Olive ir priklausomybes, reikalingas tobulinimo procesui:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Tobulinkite Phi3 naudodami Olive
[Olive konfigūracijos failas](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) apima *darbo eigą* su šiais *veiksmais*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Aukšto lygio apžvalga, ką ši darbo eiga atliks:

1. Tobulins Phi3 (150 žingsnių, kuriuos galite pakeisti) naudojant [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json) duomenis.
1. Sujungs LoRA adapterio svorius su pagrindiniu modeliu. Tai sukurs vieną modelio artefaktą ONNX formatu.
1. Model Builder optimizuos modelį ONNX vykdymo aplinkai *ir* kvantizuos modelį į `int4`.

Norėdami vykdyti darbo eigą, paleiskite:

```bash
olive run --config phrase-classification.json
```

Kai Olive baigs, jūsų optimizuotas `int4` patobulintas Phi3 modelis bus pasiekiamas: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integruokite patobulintą Phi3 į savo programą 

Norėdami paleisti programą:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Atsakymas turėtų būti vieno žodžio frazės klasifikacija (Liūdesys/Džiaugsmas/Baimė/Nustebimas).

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.