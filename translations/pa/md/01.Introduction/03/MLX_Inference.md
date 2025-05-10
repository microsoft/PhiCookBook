<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-05-09T12:11:17+00:00",
  "source_file": "md/01.Introduction/03/MLX_Inference.md",
  "language_code": "pa"
}
-->
# **Inference Phi-3 Apple MLX Framework ਨਾਲ**

## **MLX Framework ਕੀ ਹੈ**

MLX Apple silicon ਉੱਤੇ machine learning ਰਿਸਰਚ ਲਈ ਇੱਕ array framework ਹੈ, ਜੋ Apple machine learning research ਵੱਲੋਂ ਲਿਆਇਆ ਗਿਆ ਹੈ।

MLX machine learning researchers ਲਈ machine learning researchers ਵੱਲੋਂ ਬਣਾਇਆ ਗਿਆ ਹੈ। ਇਹ framework user-friendly ਬਣਾਉਣ ਲਈ ਤਿਆਰ ਕੀਤਾ ਗਿਆ ਹੈ, ਪਰ ਫਿਰ ਵੀ ਮਾਡਲ ਟ੍ਰੇਨ ਅਤੇ ਡਿਪਲੋਇ ਕਰਨ ਲਈ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਹੈ। framework ਦੀ design ਖੁਦ ਵੀ ਸਿਧੀ ਅਤੇ ਆਸਾਨ ਹੈ। ਅਸੀਂ researchers ਲਈ ਇਹ ਸੌਖਾ ਬਣਾਉਣਾ ਚਾਹੁੰਦੇ ਹਾਂ ਤਾਂ ਜੋ ਉਹ MLX ਨੂੰ ਤੇਜ਼ੀ ਨਾਲ ਵਧਾ ਸਕਣ ਅਤੇ ਨਵੇਂ ਵਿਚਾਰਾਂ ਦੀ ਖੋਜ ਕਰ ਸਕਣ।

Apple Silicon devices ਉੱਤੇ MLX ਰਾਹੀਂ LLMs ਨੂੰ ਤੇਜ਼ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ, ਅਤੇ ਮਾਡਲ ਨੂੰ ਸਥਾਨਕ ਤੌਰ 'ਤੇ ਬਹੁਤ ਆਸਾਨੀ ਨਾਲ ਚਲਾਇਆ ਜਾ ਸਕਦਾ ਹੈ।

## **MLX ਨਾਲ Phi-3-mini ਨੂੰ inference ਕਰਨ ਲਈ**

### **1. ਆਪਣਾ MLX env ਸੈੱਟ ਕਰੋ**

1. Python 3.11.x
2. MLX Library ਇੰਸਟਾਲ ਕਰੋ


```bash

pip install mlx-lm

```

### **2. MLX ਨਾਲ Terminal ਵਿੱਚ Phi-3-mini ਚਲਾਉਣਾ**


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

ਨਤੀਜਾ (ਮੇਰਾ env Apple M1 Max,64GB ਹੈ) ਇਹ ਹੈ

![Terminal](../../../../../translated_images/01.0d0f100b646a4e4c4f1cd36c1a05727cd27f1e696ed642c06cf6e2c9bbf425a4.pa.png)

### **3. MLX ਨਾਲ Terminal ਵਿੱਚ Phi-3-mini ਨੂੰ Quantize ਕਰਨਾ**


```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Note：*** ਮਾਡਲ ਨੂੰ mlx_lm.convert ਰਾਹੀਂ quantize ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ, ਅਤੇ ਡਿਫਾਲਟ quantization INT4 ਹੈ। ਇਸ ਉਦਾਹਰਨ ਵਿੱਚ Phi-3-mini ਨੂੰ INT4 ਵਿੱਚ quantize ਕੀਤਾ ਗਿਆ ਹੈ।

ਮਾਡਲ ਨੂੰ mlx_lm.convert ਰਾਹੀਂ quantize ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ, ਅਤੇ ਡਿਫਾਲਟ quantization INT4 ਹੈ। ਇਸ ਉਦਾਹਰਨ ਵਿੱਚ Phi-3-mini ਨੂੰ INT4 ਵਿੱਚ quantize ਕੀਤਾ ਗਿਆ ਹੈ। Quantization ਤੋਂ ਬਾਅਦ, ਇਹ ਮਾਡਲ ਡਿਫਾਲਟ ਡਾਇਰੈਕਟਰੀ ./mlx_model ਵਿੱਚ ਸਟੋਰ ਕੀਤਾ ਜਾਵੇਗਾ।

ਅਸੀਂ terminal ਤੋਂ MLX ਨਾਲ quantize ਕੀਤਾ ਮਾਡਲ ਟੈਸਟ ਕਰ ਸਕਦੇ ਹਾਂ


```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

ਨਤੀਜਾ ਇਹ ਹੈ

![INT4](../../../../../translated_images/02.04e0be1f18a90a58ad47e0c9d9084ac94d0f1a8c02fa707d04dd2dfc7e9117c6.pa.png)


### **4. Jupyter Notebook ਵਿੱਚ MLX ਨਾਲ Phi-3-mini ਚਲਾਉਣਾ**


![Notebook](../../../../../translated_images/03.0cf0092fe143357656bb5a7bc6427c41d8528d772d38a82d0b2693e2a3eeb16e.pa.png)

***Note:*** ਕਿਰਪਾ ਕਰਕੇ ਇਹ sample ਪੜ੍ਹੋ [click this link](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)


## **ਸਰੋਤ**

1. Apple MLX Framework ਬਾਰੇ ਜਾਣੋ [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub Repo [https://github.com/ml-explore](https://github.com/ml-explore)

**ਅਸਵੀਕਾਰੋक्ति**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਹੀਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੇ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਹੀ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਭ੍ਰਮਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।