<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-05-09T13:42:27+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "pa"
}
-->
# **Apple MLX Framework ਨਾਲ Phi-3.5 ਨੂੰ Quantize ਕਰਨਾ**


MLX ਇੱਕ array framework ਹੈ ਜੋ Apple silicon ਉੱਤੇ machine learning research ਲਈ ਬਣਾਇਆ ਗਿਆ ਹੈ, ਜੋ Apple machine learning research ਵੱਲੋਂ ਲਿਆਂਦਾ ਗਿਆ ਹੈ।

MLX machine learning researchers ਵੱਲੋਂ machine learning researchers ਲਈ ਡਿਜ਼ਾਈਨ ਕੀਤਾ ਗਿਆ ਹੈ। ਇਹ framework user-friendly ਹੋਣ ਲਈ ਬਣਾਇਆ ਗਿਆ ਹੈ, ਪਰ ਫਿਰ ਵੀ ਮਾਡਲ ਨੂੰ train ਅਤੇ deploy ਕਰਨ ਵਿੱਚ efficient ਹੈ। framework ਦਾ design ਵੀ conceptually ਸਧਾਰਣ ਹੈ। ਸਾਡਾ ਮਕਸਦ ਹੈ ਕਿ researchers ਲਈ MLX ਨੂੰ ਅਸਾਨ ਬਣਾਇਆ ਜਾਵੇ ਤਾਂ ਜੋ ਉਹ ਨਵੇਂ ideas ਨੂੰ ਤੇਜ਼ੀ ਨਾਲ explore ਕਰ ਸਕਣ।

Apple Silicon devices 'ਤੇ MLX ਰਾਹੀਂ LLMs ਨੂੰ ਤੇਜ਼ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ, ਅਤੇ ਮਾਡਲ ਨੂੰ ਬਹੁਤ ਆਸਾਨੀ ਨਾਲ locally ਚਲਾਇਆ ਜਾ ਸਕਦਾ ਹੈ।

ਹੁਣ Apple MLX Framework Phi-3.5-Instruct(**Apple MLX Framework support**), Phi-3.5-Vision(**MLX-VLM Framework support**), ਅਤੇ Phi-3.5-MoE(**Apple MLX Framework support**) ਦੇ quantization conversion ਨੂੰ support ਕਰਦਾ ਹੈ। ਆਓ ਅਗਲੇ ਕਦਮ 'ਤੇ ਕੋਸ਼ਿਸ਼ ਕਰੀਏ:

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



### **🤖 Apple MLX ਨਾਲ Phi-3.5 ਲਈ Samples**

| Labs    | ਜਾਣੂ ਕਰਵਾਉਣਾ | ਜਾਓ |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | ਜਾਣੋ ਕਿ Apple MLX framework ਨਾਲ Phi-3.5 Instruct ਨੂੰ ਕਿਵੇਂ ਵਰਤਣਾ ਹੈ   |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | ਜਾਣੋ ਕਿ Apple MLX framework ਨਾਲ Phi-3.5 Vision ਦੀ ਵਰਤੋਂ ਕਰਕੇ image ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਿਵੇਂ ਕਰਨਾ ਹੈ     |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | ਜਾਣੋ ਕਿ Apple MLX framework ਨਾਲ Phi-3.5 MoE ਨੂੰ ਕਿਵੇਂ ਵਰਤਣਾ ਹੈ  |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |


## **Resources**

1. Apple MLX Framework ਬਾਰੇ ਜਾਣੋ [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub Rep [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub Repo [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।