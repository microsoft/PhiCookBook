<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-07-17T10:03:22+00:00",
  "source_file": "md/03.FineTuning/03.Inference/MLX_Inference.md",
  "language_code": "de"
}
-->
# **Inference Phi-3 mit dem Apple MLX Framework**

## **Was ist das MLX Framework**

MLX ist ein Array-Framework für maschinelles Lernen auf Apple Silicon, entwickelt von Apples Forschung im Bereich maschinelles Lernen.

MLX wurde von Forschern für Forscher im Bereich maschinelles Lernen entworfen. Das Framework soll benutzerfreundlich sein, dabei aber effizient beim Trainieren und Bereitstellen von Modellen. Das Design des Frameworks ist zudem konzeptionell einfach gehalten. Wir möchten es Forschern erleichtern, MLX zu erweitern und zu verbessern, um schnell neue Ideen ausprobieren zu können.

LLMs können auf Apple Silicon Geräten durch MLX beschleunigt werden, und Modelle lassen sich sehr bequem lokal ausführen.

## **Verwendung von MLX zur Inferenz von Phi-3-mini**

### **1. Einrichtung deiner MLX-Umgebung**

1. Python 3.11.x  
2. Installation der MLX-Bibliothek

```bash

pip install mlx-lm

```

### **2. Phi-3-mini im Terminal mit MLX ausführen**

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Das Ergebnis (meine Umgebung ist Apple M1 Max, 64GB) ist

![Terminal](../../../../../translated_images/01.5cf57df8f7407cf9.de.png)

### **3. Quantisierung von Phi-3-mini mit MLX im Terminal**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Hinweis:*** Das Modell kann über mlx_lm.convert quantisiert werden, die Standardquantisierung ist INT4. Dieses Beispiel quantisiert Phi-3-mini auf INT4.

Das Modell kann über mlx_lm.convert quantisiert werden, die Standardquantisierung ist INT4. In diesem Beispiel wird Phi-3-mini in INT4 quantisiert. Nach der Quantisierung wird es im Standardverzeichnis ./mlx_model gespeichert.

Wir können das mit MLX quantisierte Modell im Terminal testen

```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Das Ergebnis ist

![INT4](../../../../../translated_images/02.7b188681a8eadbc1.de.png)

### **4. Phi-3-mini mit MLX im Jupyter Notebook ausführen**

![Notebook](../../../../../translated_images/03.b9705a3a5aaa89f9.de.png)

***Hinweis:*** Bitte sieh dir dieses Beispiel an [klicke hier](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)

## **Ressourcen**

1. Mehr zum Apple MLX Framework erfahren [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub Repo [https://github.com/ml-explore](https://github.com/ml-explore)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir auf Genauigkeit achten, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.