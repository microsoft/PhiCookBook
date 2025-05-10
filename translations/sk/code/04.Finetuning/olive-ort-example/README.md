<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-09T04:47:04+00:00",
  "source_file": "code/04.Finetuning/olive-ort-example/README.md",
  "language_code": "sk"
}
-->
# Doladte Phi3 pomocou Olive

V tomto príklade použijete Olive na:

1. Doladenie LoRA adaptéra na klasifikáciu fráz do kategórií Smútok, Radosť, Strach, Prekvapenie.  
1. Zlúčenie váh adaptéra do základného modelu.  
1. Optimalizáciu a kvantizáciu modelu do `int4`.

Ukážeme vám tiež, ako vykonať inferenciu doladeného modelu pomocou ONNX Runtime (ORT) Generate API.

> **⚠️ Na doladenie budete potrebovať vhodnú GPU – napríklad A10, V100, A100.**

## 💾 Inštalácia

Vytvorte nové Python virtuálne prostredie (napríklad pomocou `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Ďalej nainštalujte Olive a závislosti pre doladiaci workflow:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Doladenie Phi3 pomocou Olive  
[Olive konfiguračný súbor](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) obsahuje *workflow* so nasledovnými *krokmi*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

V skratke, tento workflow:

1. Doladí Phi3 (po dobu 150 krokov, čo môžete upraviť) pomocou dát z [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).  
1. Zlúči váhy LoRA adaptéra do základného modelu. Výsledkom bude jeden modelový artefakt vo formáte ONNX.  
1. Model Builder optimalizuje model pre ONNX runtime *a* kvantizuje model do `int4`.

Pre spustenie workflow použite:

```bash
olive run --config phrase-classification.json
```

Keď Olive dokončí, váš optimalizovaný a doladený model Phi3 v `int4` nájdete v: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrácia doladeného Phi3 do vašej aplikácie

Na spustenie aplikácie použite:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Odpoveďou by mala byť jednoslovná klasifikácia frázy (Smútok/Radosť/Strach/Prekvapenie).

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, majte prosím na pamäti, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne výklady vyplývajúce z použitia tohto prekladu.