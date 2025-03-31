<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-03-27T07:48:04+00:00",
  "source_file": "md\\01.Introduction\\03\\MLX_Inference.md",
  "language_code": "de"
}
-->
# **Inference Phi-3 mit dem Apple MLX Framework**

## **Was ist das MLX Framework**

MLX ist ein Array-Framework für maschinelles Lernen auf Apple Silicon, entwickelt von der Apple Machine Learning Forschung.

MLX wurde von Forschern für maschinelles Lernen für andere Forscher konzipiert. Das Framework soll benutzerfreundlich sein und gleichzeitig eine effiziente Möglichkeit bieten, Modelle zu trainieren und einzusetzen. Das Design des Frameworks ist bewusst einfach gehalten, um Forschern die Erweiterung und Verbesserung von MLX zu erleichtern, mit dem Ziel, neue Ideen schnell zu erforschen.

LLMs können auf Apple-Silicon-Geräten durch MLX beschleunigt werden, und Modelle können sehr bequem lokal ausgeführt werden.

## **Phi-3-mini mit MLX inferieren**

### **1. Einrichtung Ihrer MLX-Umgebung**

1. Python 3.11.x  
2. Installation der MLX-Bibliothek  

```bash

pip install mlx-lm

```

### **2. Phi-3-mini im Terminal mit MLX ausführen**

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Das Ergebnis (mein System: Apple M1 Max, 64GB) ist:

![Terminal](../../../../../translated_images/01.0d0f100b646a4e4c4f1cd36c1a05727cd27f1e696ed642c06cf6e2c9bbf425a4.de.png)

### **3. Phi-3-mini mit MLX im Terminal quantisieren**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Hinweis:*** Das Modell kann über mlx_lm.convert quantisiert werden, wobei die Standardquantisierung INT4 ist. Dieses Beispiel quantisiert Phi-3-mini auf INT4.

Das Modell wird durch mlx_lm.convert quantisiert, wobei die Standardquantisierung INT4 ist. Dieses Beispiel zeigt die Quantisierung von Phi-3-mini in INT4. Nach der Quantisierung wird das Modell im Standardverzeichnis ./mlx_model gespeichert.

Wir können das mit MLX quantisierte Modell im Terminal testen:

```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Das Ergebnis ist:

![INT4](../../../../../translated_images/02.04e0be1f18a90a58ad47e0c9d9084ac94d0f1a8c02fa707d04dd2dfc7e9117c6.de.png)

### **4. Phi-3-mini mit MLX in Jupyter Notebook ausführen**

![Notebook](../../../../../translated_images/03.0cf0092fe143357656bb5a7bc6427c41d8528d772d38a82d0b2693e2a3eeb16e.de.png)

***Hinweis:*** Bitte lesen Sie dieses Beispiel [klicken Sie auf diesen Link](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)

## **Ressourcen**

1. Mehr über das Apple MLX Framework erfahren: [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub-Repo: [https://github.com/ml-explore](https://github.com/ml-explore)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir haften nicht für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.