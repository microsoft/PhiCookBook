<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-03-27T08:24:55+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingAppleMLXQuantifyingPhi.md",
  "language_code": "de"
}
-->
# **Quantisieren von Phi-3.5 mit dem Apple MLX Framework**

MLX ist ein Array-Framework für maschinelles Lernen auf Apple Silicon, entwickelt von der Apple Machine Learning Research.

MLX wurde von Forschern im Bereich maschinelles Lernen für andere Forscher entwickelt. Das Framework ist darauf ausgelegt, benutzerfreundlich zu sein, dabei aber dennoch effizient für das Training und die Bereitstellung von Modellen. Auch das Design des Frameworks ist konzeptionell einfach gehalten. Ziel ist es, Forschern die Möglichkeit zu geben, MLX leicht zu erweitern und zu verbessern, um schnell neue Ideen zu erforschen.

LLMs können auf Apple Silicon-Geräten mithilfe von MLX beschleunigt werden, und Modelle können lokal sehr bequem ausgeführt werden.

Das Apple MLX Framework unterstützt jetzt die Quantisierungsumwandlung von Phi-3.5-Instruct (**Apple MLX Framework Support**), Phi-3.5-Vision (**MLX-VLM Framework Support**) und Phi-3.5-MoE (**Apple MLX Framework Support**). Probieren wir es aus:

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

### **🤖 Beispiele für Phi-3.5 mit Apple MLX**

| Labs    | Einführung | Gehe zu |
| -------- | ------- | ------- |
| 🚀 Lab-Einführung Phi-3.5 Instruct  | Erfahren Sie, wie Sie Phi-3.5 Instruct mit dem Apple MLX Framework nutzen können | [Gehe zu](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb) |
| 🚀 Lab-Einführung Phi-3.5 Vision (Bild) | Erfahren Sie, wie Sie Phi-3.5 Vision nutzen können, um Bilder mit dem Apple MLX Framework zu analysieren | [Gehe zu](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb) |
| 🚀 Lab-Einführung Phi-3.5 Vision (MoE) | Erfahren Sie, wie Sie Phi-3.5 MoE mit dem Apple MLX Framework nutzen können | [Gehe zu](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb) |

## **Ressourcen**

1. Erfahren Sie mehr über das Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub-Repository [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub-Repository [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.