# **اینڈروڈ میں انفرنس Phi-3**

آئیے دیکھتے ہیں کہ آپ اینڈروڈ ڈیوائسز پر Phi-3-mini کے ساتھ انفرنس کیسے کر سکتے ہیں۔ Phi-3-mini مائیکروسافٹ کی نئی سیریز ہے جو ایج ڈیوائسز اور آئی او ٹی ڈیوائسز پر بڑے زبان ماڈلز (LLMs) کی ڈیپلائمنٹ کی سہولت دیتی ہے۔

## سیمانٹک کرنل اور انفرنس

[سیمانٹک کرنل](https://github.com/microsoft/semantic-kernel) ایک ایپلیکیشن فریم ورک ہے جو آپ کو ایذور اوپن اے آئی سروس، اوپن اے آئی ماڈلز، اور مقامی ماڈلز کے ساتھ مطابقت رکھنے والی ایپلیکیشن بنانے دیتا ہے۔ اگر آپ سیمانٹک کرنل میں نئے ہیں، تو ہم آپ کو مشورہ دیتے ہیں کہ آپ [سیمانٹک کرنل کک بُک](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) دیکھیں۔

### سیمانٹک کرنل کے ذریعے Phi-3-mini تک رسائی کے لیے

آپ اسے سیمانٹک کرنل میں Hugging Face کنیکٹر کے ساتھ ملا سکتے ہیں۔ اس [نمونہ کوڈ](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo) کو ملاحظہ کریں۔

ڈیفالٹ کے طور پر، یہ Hugging Face پر ماڈل آئی ڈی سے منسلک ہوتا ہے۔ تاہم، آپ لوکل طور پر بنے ہوئے Phi-3-mini ماڈل سرور سے بھی کنیکٹ کر سکتے ہیں۔

### Ollama یا LlamaEdge کے ساتھ کوانٹائزڈ ماڈلز کال کرنا

بہت سے صارفین مقامی طور پر ماڈلز چلانے کے لیے کوانٹائزڈ ماڈلز استعمال کرنا پسند کرتے ہیں۔ [Ollama](https://ollama.com/) اور [LlamaEdge](https://llamaedge.com) انفرادی صارفین کو مختلف کوانٹائزڈ ماڈلز کال کرنے کی اجازت دیتے ہیں:

#### Ollama

آپ `ollama run Phi-3` کو براہ راست چلا سکتے ہیں یا اپنے `.gguf` فائل کی راہ کے ساتھ `Modelfile` بناتے ہوئے اسے آف لائن ترتیب دے سکتے ہیں۔

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[نمونہ کوڈ](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

اگر آپ چاہیں کہ `.gguf` فائلز بیک وقت کلاؤڈ اور ایج ڈیوائسز پر استعمال ہوں، تو LlamaEdge بہترین انتخاب ہے۔ شروع کرنے کے لیے اس [نمونہ کوڈ](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) کو ملاحظہ کریں۔

### اینڈروڈ فونز پر انسٹال اور چلائیں

1. **MLC Chat ایپ** (فری) اینڈروڈ فونز کے لیے ڈاؤنلوڈ کریں۔
2. APK فائل (148MB) ڈاؤنلوڈ کریں اور اپنے ڈیوائس پر انسٹال کریں۔
3. MLC Chat ایپ شروع کریں۔ آپ کو AI ماڈلز کی ایک فہرست نظر آئے گی، جس میں Phi-3-mini بھی شامل ہے۔

### LiteRT-LM کے ساتھ Phi-4-mini-reasoning چلائیں

[Phi-4-mini-reasoning](https://huggingface.co/litert-community/Phi-4-mini-reasoning) ایک کمیونٹی-تبویب شدہ int4 `.litertlm` بنڈل کے طور پر دستیاب ہے جو گوگل کے [LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) آن-ڈیوائس رن ٹائم کے لیے ہے۔ اینڈرائیڈ پر یہ CPU یا GPU پر [Google AI Edge Gallery](https://github.com/google-ai-edge/gallery) ایپ کے ذریعے چلتا ہے (ایپ کے اندر Hugging Face سے بنڈل امپورٹ کریں) یا LiteRT-LM Kotlin API کے ذریعے؛ یہی بنڈل iOS، macOS، Linux اور Windows پر بھی چلتا ہے۔ ماڈل کارڈ میں ناپے گئے سپیڈز اور رن کمانڈز دی گئی ہیں۔

خلاصہ یہ کہ، Phi-3-mini ایج ڈیوائسز پر جنریٹو AI کے لیے دلچسپ امکانات کھولتا ہے، اور آپ اینڈرائیڈ پر اس کی صلاحیتوں کو دریافت کرنا شروع کر سکتے ہیں۔

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->