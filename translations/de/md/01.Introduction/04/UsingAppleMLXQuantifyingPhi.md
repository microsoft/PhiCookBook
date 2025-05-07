<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-05-07T10:46:45+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "de"
}
-->
# **Quantisierung von Phi-3.5 mit dem Apple MLX Framework**

MLX ist ein Array-Framework für maschinelles Lernen auf Apple Silicon, entwickelt von den Apple Machine Learning Forschern.

MLX wurde von Forschern für Forscher im Bereich maschinelles Lernen entworfen. Das Framework soll benutzerfreundlich sein, gleichzeitig aber effizient beim Trainieren und Bereitstellen von Modellen. Auch das Design des Frameworks selbst ist konzeptionell einfach gehalten. Wir möchten es Forschern erleichtern, MLX zu erweitern und zu verbessern, um neue Ideen schnell ausprobieren zu können.

LLMs können auf Apple Silicon Geräten mit MLX beschleunigt werden, und Modelle lassen sich sehr bequem lokal ausführen.

Das Apple MLX Framework unterstützt jetzt die Quantisierungskonvertierung von Phi-3.5-Instruct (**Apple MLX Framework support**), Phi-3.5-Vision (**MLX-VLM Framework support**) und Phi-3.5-MoE (**Apple MLX Framework support**). Probieren wir es aus:

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

| Labs    | Einführung | Los |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Erfahre, wie man Phi-3.5 Instruct mit dem Apple MLX Framework verwendet   |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | Lerne, wie man Phi-3.5 Vision zur Bildanalyse mit dem Apple MLX Framework einsetzt     |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Erfahre, wie man Phi-3.5 MoE mit dem Apple MLX Framework verwendet  |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Ressourcen**

1. Erfahre mehr über das Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub Repo [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub Repo [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir auf Genauigkeit achten, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.