<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3bb9f5c926673593287eddc3741226cb",
  "translation_date": "2025-07-16T22:14:25+00:00",
  "source_file": "md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md",
  "language_code": "de"
}
-->
## **Wie man Model Builder zur Quantisierung von Phi-3.5 verwendet**

Model Builder unterstützt jetzt die Quantisierung von ONNX-Modellen für Phi-3.5 Instruct und Phi-3.5-Vision.

### **Phi-3.5-Instruct**

**CPU-beschleunigte Konvertierung in quantisiertes INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA-beschleunigte Konvertierung in quantisiertes INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Umgebung im Terminal einrichten

```bash

mkdir models

cd models 

```

2. Lade microsoft/Phi-3.5-vision-instruct im Models-Ordner herunter  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Bitte lade diese Dateien in deinen Phi-3.5-vision-instruct-Ordner herunter

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Lade diese Datei in den Models-Ordner herunter  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Öffne das Terminal

    Konvertiere ONNX-Unterstützung mit FP32

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Hinweis:**

1. Model Builder unterstützt derzeit die Konvertierung von Phi-3.5-Instruct und Phi-3.5-Vision, jedoch nicht Phi-3.5-MoE.

2. Um das quantisierte ONNX-Modell zu verwenden, kannst du es über das Generative AI extensions for onnxruntime SDK nutzen.

3. Da wir verantwortungsbewusste KI berücksichtigen müssen, wird empfohlen, nach der Quantisierung des Modells umfassendere Tests der Ergebnisse durchzuführen.

4. Durch die Quantisierung des CPU INT4-Modells können wir es auf Edge-Geräten bereitstellen, was bessere Anwendungsszenarien ermöglicht. Daher haben wir Phi-3.5-Instruct rund um INT4 abgeschlossen.

## **Ressourcen**

1. Erfahre mehr über Generative AI extensions for onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime GitHub-Repo [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.