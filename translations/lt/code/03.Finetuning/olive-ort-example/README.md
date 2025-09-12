<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-09-12T15:00:19+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "lt"
}
-->
# Suasmenkite Phi3 naudodami Olive

Šiame pavyzdyje naudosite Olive, kad:

1. Suasmenintumėte LoRA adapterį frazių klasifikavimui į kategorijas: Liūdesys, Džiaugsmas, Baimė, Nustebimas.
1. Sujungtumėte adapterio svorius su baziniu modeliu.
1. Optimizuotumėte ir kvantizuotumėte modelį į `int4`.

Taip pat parodysime, kaip atlikti suasmeninto modelio inferenciją naudojant ONNX Runtime (ORT) Generate API.

> **⚠️ Suasmeninimui reikės tinkamo GPU - pavyzdžiui, A10, V100, A100.**

## 💾 Įdiegimas

Sukurkite naują Python virtualią aplinką (pavyzdžiui, naudojant `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Tada įdiekite Olive ir suasmeninimo darbo eigos priklausomybes:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Suasmeninkite Phi3 naudodami Olive
[Olive konfigūracijos failas](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) apima *darbo eigą* su šiais *etapais*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Aukšto lygio apžvalga, ką ši darbo eiga atliks:

1. Suasmenins Phi3 (150 žingsnių, kuriuos galite pakeisti) naudojant [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json) duomenis.
1. Sujungs LoRA adapterio svorius su baziniu modeliu. Tai sukurs vieną modelio artefaktą ONNX formatu.
1. Model Builder optimizuos modelį ONNX vykdymo aplinkai *ir* kvantizuos modelį į `int4`.

Norėdami vykdyti darbo eigą, paleiskite:

```bash
olive run --config phrase-classification.json
```

Kai Olive baigs, jūsų optimizuotas `int4` suasmenintas Phi3 modelis bus pasiekiamas: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integruokite suasmenintą Phi3 į savo programą 

Norėdami paleisti programą:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Atsakymas turėtų būti vieno žodžio frazės klasifikacija (Liūdesys/Džiaugsmas/Baimė/Nustebimas).

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus aiškinimus, atsiradusius dėl šio vertimo naudojimo.