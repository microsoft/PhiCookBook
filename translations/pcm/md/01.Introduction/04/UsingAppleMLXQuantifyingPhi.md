<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-12-22T01:41:26+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "pcm"
}
-->
# **How to quantize Phi-3.5 wit Apple MLX Framework**

MLX na array framework for machine learning research for Apple silicon, na Apple machine learning research bring am.

MLX dem design am for machine learning researchers make machine learning researchers fit use am. Di framework suppose dey user-friendly, but still efficient to train and deploy models. Di design of di framework sef simple for mind. We wan make am easy for researchers to extend and improve MLX so dem fit quickly explore new ideas.

You fit accelerate LLMs on Apple Silicon devices with MLX, and models fit run locally very conveniently.

Now Apple MLX Framework dey support quantization conversion of Phi-3.5-Instruct(**Apple MLX Framework dey support**), Phi-3.5-Vision(**MLX-VLM Framework dey support**) support**), and Phi-3.5-MoE(**Apple MLX Framework dey support**). Make we try am next:

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



### **🤖 Sample dem for Phi-3.5 wit Apple MLX**

| Labs    | Intro | Open |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Learn how to use Phi-3.5 Instruct wit Apple MLX framework   |  [Open](../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | Learn how to use Phi-3.5 Vision take analyze image wit Apple MLX framework     |  [Open](../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Learn how to use Phi-3.5 MoE wit Apple MLX framework  |  [Open](../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |


## **Resource dem**

1. Find out about Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub Repo [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub Repo [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dis document na AI translate use Co-op Translator (https://github.com/Azure/co-op-translator). Even though we dey try make am accurate, abeg note say automated translation fit get mistakes or inaccuracies. The original document inside im original language na im get final authority. If na critical or important information, e better make professional human translator do am. We no go responsible for any misunderstanding or misinterpretation wey fit come from using this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->