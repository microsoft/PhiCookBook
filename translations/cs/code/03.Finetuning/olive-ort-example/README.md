# Doladění Phi3 pomocí Olive

V tomto příkladu použijete Olive k:

1. Doladění LoRA adaptéru pro klasifikaci frází do kategorií Smutek, Radost, Strach, Překvapení.
1. Sloučení vah adaptéru do základního modelu.
1. Optimalizaci a kvantizaci modelu do formátu `int4`.

Ukážeme vám také, jak provést inferenci doladěného modelu pomocí ONNX Runtime (ORT) Generate API.

> **⚠️ Pro doladění je potřeba mít k dispozici vhodnou GPU - například A10, V100, A100.**

## 💾 Instalace

Vytvořte nové Python virtuální prostředí (například pomocí `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Dále nainstalujte Olive a závislosti pro doladění:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Doladění Phi3 pomocí Olive
[Konfigurační soubor Olive](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) obsahuje *workflow* se následujícími *kroky*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Ve zkratce tento workflow:

1. Doladí Phi3 (po dobu 150 kroků, což můžete upravit) pomocí dat z [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Sloučí váhy LoRA adaptéru do základního modelu. Výsledkem bude jeden modelový artefakt ve formátu ONNX.
1. Model Builder optimalizuje model pro ONNX runtime *a* kvantizuje model do `int4`.

Pro spuštění workflow použijte:

```bash
olive run --config phrase-classification.json
```

Po dokončení Olive je váš optimalizovaný a kvantizovaný `int4` doladěný model Phi3 dostupný v: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrace doladěného Phi3 do vaší aplikace

Pro spuštění aplikace:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Odpověď by měla být jednoslovná klasifikace fráze (Smutek/Radost/Strach/Překvapení).

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.