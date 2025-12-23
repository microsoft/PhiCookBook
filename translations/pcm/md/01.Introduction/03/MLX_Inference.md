<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-12-22T01:25:32+00:00",
  "source_file": "md/01.Introduction/03/MLX_Inference.md",
  "language_code": "pcm"
}
-->
# **Inferens Phi-3 wit Apple MLX Framework**

## **Wetin be MLX Framework**

MLX na array framework wey dem design for machine learning research on Apple silicon, e come from Apple machine learning research.

MLX dem design am by machine learning researchers for machine learning researchers. Di framework dey meant to be user-friendly, but e still make sense for training and deploying models. Di design of di framework self simple for brain. We wan make am easy for researchers to extend and improve MLX so dem fit quickly explore new ideas.

You fit accelerate LLMs for Apple Silicon devices through MLX, and models fit run locally very convenient.

## **How to use MLX do inferens Phi-3-mini**

### **1. Set up you MLX env**

1. Python 3.11.x
2. Install di MLX Library


```bash

pip install mlx-lm

```

### **2. Run Phi-3-mini in Terminal wit MLX**


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Di result (my env na Apple M1 Max,64GB) na

![Terminal](../../../../../translated_images/01.5cf57df8f7407cf9281c0237f4e69c3728b8817253aad0835d14108b07c83c88.pcm.png)

### **3. Quantizing Phi-3-mini wit MLX in Terminal**


```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Note：*** You fit quantize di model through mlx_lm.convert, an di default quantization na INT4. Dis example dey quantize Phi-3-mini to INT4

You fit quantize di model through mlx_lm.convert, an di default quantization na INT4. Dis example na to quantize Phi-3-mini into INT4. After quantization, e go store for di default directory ./mlx_model

We fit test di model wey dem quantize wit MLX from terminal


```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Di result na

![INT4](../../../../../translated_images/02.7b188681a8eadbc111aba8d8006e4b3671788947a99a46329261e169dd2ec29f.pcm.png)


### **4. Run Phi-3-mini wit MLX in Jupyter Notebook**


![Notebook](../../../../../translated_images/03.b9705a3a5aaa89f9eb0ca04c1a4565dfe4a5e8cc68604227d2eab149fef1d3c7.pcm.png)

***Note:*** Abeg read dis sample [click this link](../../../code/03.Inference/MLX/MLX_DEMO.ipynb)


## **Resources**

1. Learn about Apple MLX Framework [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub Repo [https://github.com/ml-explore](https://github.com/ml-explore)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dis document don translate by AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg note say automated translations fit get errors or inaccuracies. Di original document for im own language suppose be di authoritative source. For very important information, make una use professional human translation. We no dey liable for any misunderstanding or wrong interpretation wey fit come from di use of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->