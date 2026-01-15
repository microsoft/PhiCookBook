<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-07-17T02:54:49+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "cs"
}
-->
# **Použití Microsoft Phi-3.5 tflite pro vytvoření Android aplikace**

Toto je ukázka pro Android využívající modely Microsoft Phi-3.5 tflite.

## **📚 Znalosti**

Android LLM Inference API umožňuje spouštět velké jazykové modely (LLM) zcela přímo na zařízení v Android aplikacích, které můžete využít pro širokou škálu úkolů, jako je generování textu, získávání informací v přirozeném jazyce nebo shrnování dokumentů. Tento nástroj nabízí vestavěnou podporu pro více textových velkých jazykových modelů, takže můžete do svých Android aplikací integrovat nejnovější generativní AI modely běžící přímo na zařízení.

Google AI Edge Torch je python knihovna, která podporuje převod PyTorch modelů do formátu .tflite, který lze následně spustit pomocí TensorFlow Lite a MediaPipe. To umožňuje vytvářet aplikace pro Android, iOS a IoT, které modely spouští kompletně na zařízení. AI Edge Torch nabízí širokou podporu CPU, s počáteční podporou GPU a NPU. AI Edge Torch se snaží úzce integrovat s PyTorch, staví na torch.export() a poskytuje dobrou podporu Core ATen operátorů.

## **🪬 Návod**

### **🔥 Převod Microsoft Phi-3.5 na podporu tflite**

0. Tento příklad je určen pro Android 14+

1. Nainstalujte Python 3.10.12

***Doporučení:*** použijte conda pro vytvoření Python prostředí

2. Ubuntu 20.04 / 22.04 (zaměřte se na [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Doporučení:*** použijte Azure Linux VM nebo cloudové VM třetích stran pro vytvoření prostředí

3. Otevřete Linux bash a nainstalujte Python knihovny

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Stáhněte Microsoft-3.5-Instruct z Hugging face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Převod Microsoft Phi-3.5 na tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Převod Microsoft Phi-3.5 na Android Mediapipe Bundle**

nejprve nainstalujte mediapipe

```bash

pip install mediapipe

```

spusťte tento kód ve [svém notebooku](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

```python

import mediapipe as mp
from mediapipe.tasks.python.genai import bundler

config = bundler.BundleConfig(
    tflite_model='Your Phi-3.5 tflite model path',
    tokenizer_model='Your Phi-3.5 tokenizer model path',
    start_token='start_token',
    stop_tokens=[STOP_TOKENS],
    output_filename='Your Phi-3.5 task model path',
    enable_bytes_to_unicode_mapping=True or Flase,
)
bundler.create_bundle(config)

```

### **🔥 Použití adb push pro přenos modelu na cestu v Android zařízení**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Spuštění vašeho Android kódu**

![demo](../../../../../../translated_images/cs/demo.06d5a4246f057d1b.webp)

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.