<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-05-07T14:31:34+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "ur"
}
-->
# **اینڈرائیڈ میں Inference Phi-3**

چلیے دیکھتے ہیں کہ آپ Android ڈیوائسز پر Phi-3-mini کے ساتھ inference کیسے کر سکتے ہیں۔ Phi-3-mini مائیکروسافٹ کی نئی ماڈلز کی سیریز ہے جو edge ڈیوائسز اور IoT ڈیوائسز پر Large Language Models (LLMs) کو deploy کرنے کی سہولت دیتی ہے۔

## Semantic Kernel اور Inference

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) ایک application framework ہے جو آپ کو Azure OpenAI Service، OpenAI ماڈلز، اور یہاں تک کہ local ماڈلز کے ساتھ compatible applications بنانے دیتا ہے۔ اگر آپ Semantic Kernel میں نئے ہیں، تو ہم آپ کو [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) دیکھنے کی تجویز دیتے ہیں۔

### Semantic Kernel کے ذریعے Phi-3-mini تک رسائی

آپ اسے Semantic Kernel میں Hugging Face Connector کے ساتھ ملا سکتے ہیں۔ اس [Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo) کا حوالہ لیں۔

By default، یہ Hugging Face پر ماڈل ID کے مطابق ہوتا ہے۔ تاہم، آپ locally built Phi-3-mini ماڈل سرور سے بھی connect کر سکتے ہیں۔

### Ollama یا LlamaEdge کے ساتھ Quantized Models کو کال کرنا

بہت سے صارفین locally ماڈلز چلانے کے لیے quantized models استعمال کرنا پسند کرتے ہیں۔ [Ollama](https://ollama.com/) اور [LlamaEdge](https://llamaedge.com) انفرادی صارفین کو مختلف quantized models کال کرنے کی اجازت دیتے ہیں:

#### Ollama

آپ `ollama run Phi-3` کو براہ راست چلا سکتے ہیں یا اسے offline configure کرنے کے لیے اپنے `.gguf` فائل کے راستے کے ساتھ ایک `Modelfile` بنا سکتے ہیں۔

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

اگر آپ چاہتے ہیں کہ `.gguf` فائلیں بیک وقت cloud اور edge ڈیوائسز پر استعمال ہوں، تو LlamaEdge ایک بہترین انتخاب ہے۔ شروع کرنے کے لیے اس [sample code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) کا حوالہ لیں۔

### اینڈرائیڈ فونز پر انسٹال اور چلائیں

1. **MLC Chat ایپ ڈاؤن لوڈ کریں** (مفت) اینڈرائیڈ فونز کے لیے۔
2. APK فائل (148MB) ڈاؤن لوڈ کریں اور اپنے ڈیوائس پر انسٹال کریں۔
3. MLC Chat ایپ لانچ کریں۔ آپ کو AI ماڈلز کی فہرست نظر آئے گی، جس میں Phi-3-mini بھی شامل ہے۔

خلاصہ یہ کہ، Phi-3-mini edge ڈیوائسز پر generative AI کے لیے دلچسپ امکانات کھولتا ہے، اور آپ اس کی صلاحیتوں کو اینڈرائیڈ پر آزمانا شروع کر سکتے ہیں۔

**ڈس کلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار تراجم میں غلطیاں یا کمی بیشی ہو سکتی ہے۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ تجویز کیا جاتا ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تعبیر کی ذمہ داری ہم پر عائد نہیں ہوتی۔