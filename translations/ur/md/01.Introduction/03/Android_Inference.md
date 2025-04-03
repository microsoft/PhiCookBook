<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b909b4ac6465d33e81adb17df38deef3",
  "translation_date": "2025-04-03T06:49:00+00:00",
  "source_file": "md\\01.Introduction\\03\\Android_Inference.md",
  "language_code": "ur"
}
-->
# **اینفرینس Phi-3 اینڈرائیڈ پر**

آئیے دیکھتے ہیں کہ آپ اینڈرائیڈ ڈیوائسز پر Phi-3-mini کے ساتھ انفرینس کیسے کر سکتے ہیں۔ Phi-3-mini مائیکروسافٹ کی ایک نئی ماڈل سیریز ہے جو بڑے لینگویج ماڈلز (LLMs) کو ایج ڈیوائسز اور IoT ڈیوائسز پر ڈیپلائی کرنے کے قابل بناتی ہے۔

## سیمینٹک کرنل اور انفرینس

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) ایک ایپلیکیشن فریم ورک ہے جو آپ کو ایسی ایپلیکیشنز بنانے کی اجازت دیتا ہے جو Azure OpenAI Service، OpenAI ماڈلز، اور لوکل ماڈلز کے ساتھ مطابقت رکھتی ہوں۔ اگر آپ سیمینٹک کرنل کے بارے میں نئے ہیں، تو ہم تجویز کرتے ہیں کہ آپ [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) پر نظر ڈالیں۔

### سیمینٹک کرنل کے ذریعے Phi-3-mini تک رسائی حاصل کرنا

آپ اسے سیمینٹک کرنل میں Hugging Face Connector کے ساتھ ملا سکتے ہیں۔ اس [نمونہ کوڈ](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo) کا حوالہ دیں۔

ڈیفالٹ طور پر، یہ Hugging Face پر ماڈل ID سے مطابقت رکھتا ہے۔ تاہم، آپ لوکل طور پر بنائے گئے Phi-3-mini ماڈل سرور سے بھی کنیکٹ کر سکتے ہیں۔

### Ollama یا LlamaEdge کے ذریعے کوانٹائزڈ ماڈلز کو کال کرنا

بہت سے صارفین ماڈلز کو لوکل طور پر چلانے کے لیے کوانٹائزڈ ماڈلز استعمال کرنا پسند کرتے ہیں۔ [Ollama](https://ollama.com/) اور [LlamaEdge](https://llamaedge.com) انفرادی صارفین کو مختلف کوانٹائزڈ ماڈلز کو کال کرنے کی اجازت دیتے ہیں:

#### Ollama

آپ براہ راست `ollama run Phi-3` چلا سکتے ہیں یا اسے آف لائن کنفیگر کر سکتے ہیں `Modelfile` بنا کر، جس میں آپ کے `.gguf` فائل کا راستہ دیا گیا ہو۔

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[نمونہ کوڈ](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

اگر آپ `.gguf` فائلز کو بیک وقت کلاؤڈ اور ایج ڈیوائسز پر استعمال کرنا چاہتے ہیں، تو LlamaEdge ایک بہترین انتخاب ہے۔ شروع کرنے کے لیے آپ اس [نمونہ کوڈ](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) کا حوالہ دے سکتے ہیں۔

### اینڈرائیڈ فونز پر انسٹال کریں اور چلائیں

1. **MLC Chat ایپ ڈاؤنلوڈ کریں** (مفت) اینڈرائیڈ فونز کے لیے۔
2. APK فائل (148MB) ڈاؤنلوڈ کریں اور اسے اپنے ڈیوائس پر انسٹال کریں۔
3. MLC Chat ایپ لانچ کریں۔ آپ کو AI ماڈلز کی ایک فہرست نظر آئے گی، جن میں Phi-3-mini شامل ہے۔

خلاصہ یہ کہ Phi-3-mini ایج ڈیوائسز پر جنریٹو AI کے لیے دلچسپ امکانات پیش کرتا ہے، اور آپ اینڈرائیڈ پر اس کی صلاحیتوں کو دریافت کرنا شروع کر سکتے ہیں۔

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کی پوری کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا خامیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ورانہ انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔