<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-07-16T21:52:51+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "ur"
}
-->
# **Apple MLX Framework کے ذریعے Phi-3.5 کی Quantizing**

MLX ایک array فریم ورک ہے جو Apple silicon پر مشین لرننگ ریسرچ کے لیے بنایا گیا ہے، اور یہ Apple مشین لرننگ ریسرچ کی جانب سے پیش کیا گیا ہے۔

MLX مشین لرننگ ریسرچرز کے لیے، مشین لرننگ ریسرچرز نے ڈیزائن کیا ہے۔ یہ فریم ورک صارف دوست ہونے کے ساتھ ساتھ ماڈلز کو تربیت دینے اور تعینات کرنے میں مؤثر بھی ہے۔ فریم ورک کا ڈیزائن خود بھی تصوراتی طور پر سادہ ہے۔ ہمارا مقصد ہے کہ ریسرچرز کے لیے MLX کو بڑھانا اور بہتر بنانا آسان ہو تاکہ وہ جلدی سے نئے خیالات کو دریافت کر سکیں۔

Apple Silicon ڈیوائسز پر LLMs کو MLX کے ذریعے تیز کیا جا سکتا ہے، اور ماڈلز کو مقامی طور پر آسانی سے چلایا جا سکتا ہے۔

اب Apple MLX Framework Phi-3.5-Instruct (**Apple MLX Framework support**)، Phi-3.5-Vision (**MLX-VLM Framework support**)، اور Phi-3.5-MoE (**Apple MLX Framework support**) کی quantization conversion کو سپورٹ کرتا ہے۔ آئیے اگلے مرحلے میں اسے آزمائیں:

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

### **🤖 Apple MLX کے ساتھ Phi-3.5 کے لیے نمونے**

| Labs    | تعارف | جائیں |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | سیکھیں کہ Apple MLX فریم ورک کے ساتھ Phi-3.5 Instruct کو کیسے استعمال کیا جائے   |  [جائیں](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | سیکھیں کہ Apple MLX فریم ورک کے ساتھ Phi-3.5 Vision کو تصویر کے تجزیے کے لیے کیسے استعمال کیا جائے     |  [جائیں](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | سیکھیں کہ Apple MLX فریم ورک کے ساتھ Phi-3.5 MoE کو کیسے استعمال کیا جائے  |  [جائیں](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **وسائل**

1. Apple MLX Framework کے بارے میں جانیں [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub ریپوزیٹری [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub ریپوزیٹری [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**دستخطی دستبرداری**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔