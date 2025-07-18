<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-07-16T21:54:20+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "pa"
}
-->
# **Apple MLX Framework ਨਾਲ Phi-3.5 ਦੀ Quantizing**


MLX ਇੱਕ ਐਰੇ ਫਰੇਮਵਰਕ ਹੈ ਜੋ Apple ਸਿਲੀਕਾਨ 'ਤੇ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਖੋਜ ਲਈ ਬਣਾਇਆ ਗਿਆ ਹੈ, ਜੋ Apple ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਖੋਜ ਵੱਲੋਂ ਤੁਹਾਡੇ ਲਈ ਲਿਆਇਆ ਗਿਆ ਹੈ।

MLX ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਖੋਜਕਾਰਾਂ ਵੱਲੋਂ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਖੋਜਕਾਰਾਂ ਲਈ ਡਿਜ਼ਾਈਨ ਕੀਤਾ ਗਿਆ ਹੈ। ਇਹ ਫਰੇਮਵਰਕ ਵਰਤੋਂਕਾਰ-ਮਿੱਤਰ ਹੈ, ਪਰ ਫਿਰ ਵੀ ਮਾਡਲਾਂ ਨੂੰ ਟ੍ਰੇਨ ਅਤੇ ਡਿਪਲੋਇ ਕਰਨ ਲਈ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਹੈ। ਫਰੇਮਵਰਕ ਦੀ ਡਿਜ਼ਾਈਨ ਖੁਦ ਵੀ ਸਿਧੀ ਅਤੇ ਆਸਾਨ ਹੈ। ਅਸੀਂ ਚਾਹੁੰਦੇ ਹਾਂ ਕਿ ਖੋਜਕਾਰ MLX ਨੂੰ ਆਸਾਨੀ ਨਾਲ ਵਧਾ ਸਕਣ ਅਤੇ ਸੁਧਾਰ ਸਕਣ ਤਾਂ ਜੋ ਨਵੇਂ ਵਿਚਾਰਾਂ ਨੂੰ ਤੇਜ਼ੀ ਨਾਲ ਖੋਜਿਆ ਜਾ ਸਕੇ।

Apple ਸਿਲੀਕਾਨ ਡਿਵਾਈਸਾਂ 'ਤੇ MLX ਰਾਹੀਂ LLMs ਨੂੰ ਤੇਜ਼ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ, ਅਤੇ ਮਾਡਲਾਂ ਨੂੰ ਬਹੁਤ ਆਸਾਨੀ ਨਾਲ ਲੋਕਲ ਤੌਰ 'ਤੇ ਚਲਾਇਆ ਜਾ ਸਕਦਾ ਹੈ।

ਹੁਣ Apple MLX Framework Phi-3.5-Instruct(**Apple MLX Framework support**), Phi-3.5-Vision(**MLX-VLM Framework support**), ਅਤੇ Phi-3.5-MoE(**Apple MLX Framework support**) ਦੀ quantization conversion ਨੂੰ ਸਹਿਯੋਗ ਦਿੰਦਾ ਹੈ। ਆਓ ਅਗਲੇ ਕਦਮ ਵੱਲ ਵਧੀਏ:

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



### **🤖 Apple MLX ਨਾਲ Phi-3.5 ਲਈ ਨਮੂਨੇ**

| ਲੈਬਸ    | ਜਾਣੂ ਕਰਵਾਉਣਾ | ਜਾਓ |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Apple MLX ਫਰੇਮਵਰਕ ਨਾਲ Phi-3.5 Instruct ਨੂੰ ਵਰਤਣਾ ਸਿੱਖੋ   |  [ਜਾਓ](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (ਚਿੱਤਰ) | Apple MLX ਫਰੇਮਵਰਕ ਨਾਲ ਚਿੱਤਰ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਨ ਲਈ Phi-3.5 Vision ਨੂੰ ਵਰਤਣਾ ਸਿੱਖੋ     |  [ਜਾਓ](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Apple MLX ਫਰੇਮਵਰਕ ਨਾਲ Phi-3.5 MoE ਨੂੰ ਵਰਤਣਾ ਸਿੱਖੋ  |  [ਜਾਓ](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |


## **ਸੰਸਾਧਨ**

1. Apple MLX Framework ਬਾਰੇ ਜਾਣੋ [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub ਰਿਪੋ [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub ਰਿਪੋ [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।