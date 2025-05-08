<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-05-07T14:50:19+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "ur"
}
-->
# **Apple MLX Framework کے ذریعے Phi-3.5 کی Quantizing**


MLX ایک array framework ہے جو Apple silicon پر machine learning تحقیق کے لیے بنایا گیا ہے، جسے Apple machine learning تحقیق نے پیش کیا ہے۔

MLX machine learning محققین کے لیے، machine learning محققین کے ذریعے ڈیزائن کیا گیا ہے۔ یہ framework صارف دوست ہونے کے ساتھ ساتھ ماڈلز کو تربیت دینے اور چلانے میں مؤثر بھی ہے۔ framework کا ڈیزائن خود بھی تصوراتی طور پر سادہ ہے۔ ہمارا مقصد ہے کہ محققین کے لیے MLX کو آسانی سے بڑھایا اور بہتر بنایا جائے تاکہ نئے خیالات کو جلدی دریافت کیا جا سکے۔

Apple Silicon ڈیوائسز پر MLX کے ذریعے LLMs کو تیز کیا جا سکتا ہے، اور ماڈلز کو مقامی طور پر آسانی سے چلایا جا سکتا ہے۔

اب Apple MLX Framework Phi-3.5-Instruct (**Apple MLX Framework support**)، Phi-3.5-Vision (**MLX-VLM Framework support**)، اور Phi-3.5-MoE (**Apple MLX Framework support**) کی quantization conversion کو سپورٹ کرتا ہے۔ آئیں اسے اگلے مرحلے میں آزمائیں:

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



### **🤖 Apple MLX کے ساتھ Phi-3.5 کے نمونے**

| Labs    | تعارف | جائیں |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Apple MLX framework کے ساتھ Phi-3.5 Instruct استعمال کرنا سیکھیں   |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | Apple MLX framework کے ساتھ تصویر کا تجزیہ کرنے کے لیے Phi-3.5 Vision استعمال کرنا سیکھیں     |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Apple MLX framework کے ساتھ Phi-3.5 MoE استعمال کرنا سیکھیں  |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |


## **وسائل**

1. Apple MLX Framework کے بارے میں جانیں [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub ریپوزیٹری [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub ریپوزیٹری [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**دسclaimer**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا بے دقتیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں مستند ذریعہ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔