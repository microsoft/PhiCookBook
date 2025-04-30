<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "340bd4c009524ef84102b78d06eea735",
  "translation_date": "2025-04-03T07:02:19+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingAppleMLXQuantifyingPhi.md",
  "language_code": "ur"
}
-->
# **ایپل MLX فریم ورک کے ذریعے Phi-3.5 کو کوانٹائز کرنا**

MLX ایک ایری فریم ورک ہے جو ایپل سلیکون پر مشین لرننگ ریسرچ کے لیے بنایا گیا ہے، اور یہ ایپل کی مشین لرننگ ریسرچ ٹیم کی پیشکش ہے۔

MLX خاص طور پر مشین لرننگ ریسرچرز کے لیے ڈیزائن کیا گیا ہے۔ یہ فریم ورک استعمال میں آسان ہونے کے ساتھ ساتھ ماڈلز کی تربیت اور تعیناتی کے لیے مؤثر بھی ہے۔ اس فریم ورک کا ڈیزائن تصوراتی طور پر بھی سادہ ہے۔ ہمارا مقصد ہے کہ ریسرچرز MLX کو آسانی سے بڑھا سکیں اور نئے خیالات کو جلدی سے آزما سکیں۔

LLMs کو ایپل سلیکون ڈیوائسز پر MLX کے ذریعے تیز تر بنایا جا سکتا ہے، اور ماڈلز کو مقامی طور پر بہت سہولت کے ساتھ چلایا جا سکتا ہے۔

اب ایپل MLX فریم ورک Phi-3.5-Instruct (**Apple MLX Framework support**)، Phi-3.5-Vision (**MLX-VLM Framework support**) اور Phi-3.5-MoE (**Apple MLX Framework support**) کی کوانٹائزیشن کنورژن کو سپورٹ کرتا ہے۔ آئیے اسے آزما کر دیکھتے ہیں:

### **Phi-3.5-Instruct**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-mini-instruct -q

```

### **Phi-3.5-Vision**

```bash

python -m mlxv_lm.convert --hf-path microsoft/Phi-3.5-vision-instruct -q

```

### **Phi-3.5-MoE**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-MoE-instruct  -q

```

### **🤖 ایپل MLX کے ساتھ Phi-3.5 کے نمونے**

| لیبز    | تعارف | جاؤ |
| -------- | ------- | ------- |
| 🚀 لیب-Phi-3.5 Instruct کا تعارف  | ایپل MLX فریم ورک کے ساتھ Phi-3.5 Instruct کو استعمال کرنے کا طریقہ سیکھیں  |  [جاؤ](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 لیب-Phi-3.5 Vision (تصویر) کا تعارف | ایپل MLX فریم ورک کے ساتھ تصویر کو تجزیہ کرنے کے لیے Phi-3.5 Vision کو استعمال کرنے کا طریقہ سیکھیں  |  [جاؤ](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 لیب-Phi-3.5 Vision (moE) کا تعارف   | ایپل MLX فریم ورک کے ساتھ Phi-3.5 MoE کو استعمال کرنے کا طریقہ سیکھیں  |  [جاؤ](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **وسائل**

1. ایپل MLX فریم ورک کے بارے میں جانیں [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. ایپل MLX GitHub ریپوزیٹری [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub ریپوزیٹری [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کی پوری کوشش کرتے ہیں، لیکن براہ کرم یہ بات ذہن میں رکھیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں معتبر ماخذ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ تجویز کیا جاتا ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والے کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔