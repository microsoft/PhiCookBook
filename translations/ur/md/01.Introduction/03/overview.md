Phi-3-mini کے سیاق و سباق میں، inference سے مراد ماڈل کو استعمال کرتے ہوئے ان پٹ ڈیٹا کی بنیاد پر پیش گوئیاں کرنا یا آؤٹ پٹ تیار کرنا ہے۔ آئیے میں آپ کو Phi-3-mini اور اس کی inference صلاحیتوں کے بارے میں مزید تفصیلات فراہم کرتا ہوں۔

Phi-3-mini، Microsoft کی جانب سے جاری کردہ Phi-3 سیریز کے ماڈلز کا حصہ ہے۔ یہ ماڈلز Small Language Models (SLMs) کے امکانات کو نئے سرے سے متعین کرنے کے لیے ڈیزائن کیے گئے ہیں۔

Phi-3-mini اور اس کی inference صلاحیتوں کے بارے میں چند اہم نکات درج ذیل ہیں:

## **Phi-3-mini کا جائزہ:**
- Phi-3-mini کے پاس 3.8 بلین پیرامیٹرز کی تعداد ہے۔
- یہ نہ صرف روایتی کمپیوٹنگ ڈیوائسز پر چل سکتا ہے بلکہ ایج ڈیوائسز جیسے موبائل اور IoT ڈیوائسز پر بھی کام کر سکتا ہے۔
- Phi-3-mini کی ریلیز افراد اور اداروں کو مختلف ہارڈویئر ڈیوائسز پر SLMs کو تعینات کرنے کی سہولت دیتی ہے، خاص طور پر محدود وسائل والے ماحول میں۔
- یہ مختلف ماڈل فارمیٹس کو کور کرتا ہے، جن میں روایتی PyTorch فارمیٹ، gguf فارمیٹ کا quantized ورژن، اور ONNX پر مبنی quantized ورژن شامل ہیں۔

## **Phi-3-mini تک رسائی:**
Phi-3-mini تک رسائی کے لیے، آپ Copilot ایپلیکیشن میں [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) استعمال کر سکتے ہیں۔ Semantic Kernel عام طور پر Azure OpenAI Service، Hugging Face پر موجود اوپن سورس ماڈلز، اور لوکل ماڈلز کے ساتھ مطابقت رکھتا ہے۔
آپ quantized ماڈلز کو کال کرنے کے لیے [Ollama](https://ollama.com) یا [LlamaEdge](https://llamaedge.com) بھی استعمال کر سکتے ہیں۔ Ollama انفرادی صارفین کو مختلف quantized ماڈلز کال کرنے کی اجازت دیتا ہے، جبکہ LlamaEdge GGUF ماڈلز کے لیے کراس-پلیٹ فارم دستیابی فراہم کرتا ہے۔

## **Quantized ماڈلز:**
بہت سے صارفین لوکل inference کے لیے quantized ماڈلز کو ترجیح دیتے ہیں۔ مثال کے طور پر، آپ Ollama کے ذریعے براہ راست Phi-3 کو چلا سکتے ہیں یا اسے Modelfile کے ذریعے آف لائن کنفیگر کر سکتے ہیں۔ Modelfile میں GGUF فائل کا راستہ اور پرامپٹ فارمیٹ مخصوص کیا جاتا ہے۔

## **Generative AI کے امکانات:**
Phi-3-mini جیسے SLMs کو ملا کر generative AI کے نئے امکانات کھلتے ہیں۔ inference صرف پہلا قدم ہے؛ یہ ماڈلز محدود وسائل، کم تاخیر، اور کم لاگت والے حالات میں مختلف کاموں کے لیے استعمال کیے جا سکتے ہیں۔

## **Phi-3-mini کے ساتھ Generative AI کو فعال کرنا: Inference اور Deployment کے لیے رہنما**
Semantic Kernel، Ollama/LlamaEdge، اور ONNX Runtime کو استعمال کرتے ہوئے Phi-3-mini ماڈلز تک رسائی اور inference کرنے کا طریقہ سیکھیں، اور مختلف ایپلیکیشن کے منظرناموں میں generative AI کے امکانات دریافت کریں۔

**خصوصیات**  
Phi-3-mini ماڈل میں inference:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)  

خلاصہ یہ کہ، Phi-3-mini ڈویلپرز کو مختلف ماڈل فارمیٹس کو دریافت کرنے اور مختلف ایپلیکیشن کے منظرناموں میں generative AI سے فائدہ اٹھانے کی اجازت دیتا ہے۔

**دستخطی دستبرداری**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔