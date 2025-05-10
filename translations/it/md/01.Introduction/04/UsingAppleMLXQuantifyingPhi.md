<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-05-09T13:43:28+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "it"
}
-->
# **Quantizzare Phi-3.5 usando il framework Apple MLX**

MLX è un framework array per la ricerca nel machine learning su Apple silicon, sviluppato dal team di ricerca Apple machine learning.

MLX è progettato da ricercatori di machine learning per ricercatori di machine learning. Il framework è pensato per essere facile da usare, ma allo stesso tempo efficiente per l’addestramento e il deployment dei modelli. La struttura del framework è anche concettualmente semplice. L’obiettivo è rendere facile per i ricercatori estendere e migliorare MLX, permettendo di esplorare rapidamente nuove idee.

Gli LLM possono essere accelerati sui dispositivi Apple Silicon tramite MLX, e i modelli possono essere eseguiti localmente in modo molto comodo.

Ora il framework Apple MLX supporta la conversione di quantizzazione di Phi-3.5-Instruct (**supporto Apple MLX Framework**), Phi-3.5-Vision (**supporto MLX-VLM Framework**), e Phi-3.5-MoE (**supporto Apple MLX Framework**). Proviamolo subito:

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


### **🤖 Esempi per Phi-3.5 con Apple MLX**

| Labs    | Introduzione | Vai |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Scopri come usare Phi-3.5 Instruct con il framework Apple MLX   |  [Vai](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (immagine) | Impara a usare Phi-3.5 Vision per analizzare immagini con il framework Apple MLX     |  [Vai](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Scopri come usare Phi-3.5 MoE con il framework Apple MLX  |  [Vai](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |


## **Risorse**

1. Scopri il framework Apple MLX [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Repository GitHub Apple MLX [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. Repository GitHub MLX-VLM [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o inesattezze. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda la traduzione professionale umana. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall’uso di questa traduzione.