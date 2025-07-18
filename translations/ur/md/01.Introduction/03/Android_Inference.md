<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-07-16T20:11:13+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "ur"
}
-->
# **اینڈرائیڈ میں Inference Phi-3**

آئیے دیکھتے ہیں کہ آپ اینڈرائیڈ ڈیوائسز پر Phi-3-mini کے ساتھ inference کیسے کر سکتے ہیں۔ Phi-3-mini مائیکروسافٹ کی نئی ماڈلز کی سیریز ہے جو ایج ڈیوائسز اور IoT ڈیوائسز پر Large Language Models (LLMs) کی تعیناتی کو ممکن بناتی ہے۔

## Semantic Kernel اور Inference

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) ایک ایپلیکیشن فریم ورک ہے جو آپ کو Azure OpenAI Service، OpenAI ماڈلز، اور یہاں تک کہ لوکل ماڈلز کے ساتھ مطابقت رکھنے والی ایپلیکیشنز بنانے کی اجازت دیتا ہے۔ اگر آپ Semantic Kernel میں نئے ہیں، تو ہم آپ کو [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) دیکھنے کی تجویز دیتے ہیں۔

### Semantic Kernel کے ذریعے Phi-3-mini تک رسائی

آپ اسے Semantic Kernel میں Hugging Face Connector کے ساتھ ملا سکتے ہیں۔ اس [نمونہ کوڈ](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo) کا حوالہ دیں۔

ڈیفالٹ کے طور پر، یہ Hugging Face پر ماڈل ID کے مطابق ہوتا ہے۔ تاہم، آپ لوکل طور پر بنائے گئے Phi-3-mini ماڈل سرور سے بھی کنیکٹ کر سکتے ہیں۔

### Ollama یا LlamaEdge کے ساتھ Quantized ماڈلز کو کال کرنا

بہت سے صارفین ماڈلز کو لوکل چلانے کے لیے quantized ماڈلز استعمال کرنا پسند کرتے ہیں۔ [Ollama](https://ollama.com/) اور [LlamaEdge](https://llamaedge.com) انفرادی صارفین کو مختلف quantized ماڈلز کال کرنے کی اجازت دیتے ہیں:

#### Ollama

آپ براہ راست `ollama run Phi-3` چلا سکتے ہیں یا `.gguf` فائل کے راستے کے ساتھ `Modelfile` بنا کر اسے آف لائن ترتیب دے سکتے ہیں۔

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[نمونہ کوڈ](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

اگر آپ بادل اور ایج ڈیوائسز پر بیک وقت `.gguf` فائلیں استعمال کرنا چاہتے ہیں، تو LlamaEdge ایک بہترین انتخاب ہے۔ شروع کرنے کے لیے اس [نمونہ کوڈ](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) کا حوالہ دیں۔

### اینڈرائیڈ فونز پر انسٹال اور چلائیں

1. **MLC Chat ایپ ڈاؤن لوڈ کریں** (مفت) اینڈرائیڈ فونز کے لیے۔
2. APK فائل (148MB) ڈاؤن لوڈ کریں اور اپنے ڈیوائس پر انسٹال کریں۔
3. MLC Chat ایپ لانچ کریں۔ آپ کو AI ماڈلز کی فہرست نظر آئے گی، جس میں Phi-3-mini بھی شامل ہے۔

خلاصہ یہ کہ، Phi-3-mini ایج ڈیوائسز پر generative AI کے لیے دلچسپ امکانات کھولتا ہے، اور آپ اینڈرائیڈ پر اس کی صلاحیتوں کو دریافت کرنا شروع کر سکتے ہیں۔

**دستخطی دستبرداری**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔