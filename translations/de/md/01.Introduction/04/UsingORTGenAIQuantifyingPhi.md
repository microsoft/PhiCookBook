# **Quantisierung der Phi-Familie mit Generative AI-Erweiterungen für onnxruntime**

## **Was sind Generative AI-Erweiterungen für onnxruntime**

Diese Erweiterungen helfen Ihnen, generative KI mit ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)) auszuführen. Sie bieten die generative KI-Schleife für ONNX-Modelle, einschließlich Inferenz mit ONNX Runtime, Logits-Verarbeitung, Suche und Sampling sowie Verwaltung des KV-Caches. Entwickler können eine hochstufige generate()-Methode aufrufen oder jede Iteration des Modells in einer Schleife ausführen, wobei jeweils ein Token generiert und optional die Generierungsparameter innerhalb der Schleife aktualisiert werden. Es gibt Unterstützung für Greedy/Beam Search und TopP, TopK Sampling zur Generierung von Token-Sequenzen sowie eingebauten Logits-Verarbeitung wie Wiederholungsstrafe. Sie können auch problemlos benutzerdefinierte Bewertungen hinzufügen.

Auf Anwendungsebene können Sie Generative AI-Erweiterungen für onnxruntime verwenden, um Anwendungen mit C++/ C# / Python zu entwickeln. Auf Modellebene können Sie damit feinabgestimmte Modelle zusammenführen und verwandte quantitative Bereitstellungsarbeiten durchführen.


## **Quantisierung von Phi-3.5 mit Generative AI-Erweiterungen für onnxruntime**

### **Unterstützte Modelle**

Generative AI-Erweiterungen für onnxruntime unterstützen die Quantisierungskonvertierung von Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.


### **Model Builder in Generative AI-Erweiterungen für onnxruntime**

Der Model Builder beschleunigt das Erstellen von optimierten und quantisierten ONNX-Modellen, die mit der ONNX Runtime generate()-API ausgeführt werden.

Über den Model Builder können Sie das Modell auf INT4, INT8, FP16, FP32 quantisieren und verschiedene Hardwarebeschleunigungsmethoden wie CPU, CUDA, DirectML, Mobile usw. kombinieren.

Um den Model Builder zu verwenden, müssen Sie installieren

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Nach der Installation können Sie das Model Builder-Skript über das Terminal ausführen, um Modellformat- und Quantisierungskonvertierungen durchzuführen.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Verstehen Sie die relevanten Parameter

1. **model_name** Dies ist das Modell auf Hugging Face, z.B. microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct usw. Es kann auch der Pfad sein, wo Sie das Modell speichern

2. **path_to_output_folder** Speicherort der quantisierten Konvertierung

3. **execution_provider** Unterstützung verschiedener Hardwarebeschleunigungen, z.B. cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** Wir laden das Modell von Hugging Face herunter und speichern es lokal im Cache




***Hinweis:*** <ul>Obwohl Generative AI-Erweiterungen für onnxruntime sich in der Vorschau befinden, sind sie bereits in Microsoft Olive integriert, und Sie können auch Model Builder-Funktionen der Generative AI-Erweiterungen für onnxruntime über Microsoft Olive aufrufen.</ul>

## **Wie man den Model Builder verwendet, um Phi-3.5 zu quantisieren**

Der Model Builder unterstützt jetzt die ONNX-Modellquantisierung für Phi-3.5 Instruct und Phi-3.5-Vision

### **Phi-3.5-Instruct**


**CPU-beschleunigte Konvertierung zu quantisiertem INT4**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA-beschleunigte Konvertierung zu quantisiertem INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Setzen Sie die Umgebung im Terminal

```bash

mkdir models

cd models 

```

2. Download microsoft/Phi-3.5-vision-instruct im Modelle-Ordner
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Bitte laden Sie diese Dateien in Ihren Phi-3.5-vision-instruct-Ordner herunter

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. Laden Sie diese Datei in den Modelle-Ordner herunter
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Gehen Sie ins Terminal

    Konvertieren Sie ONNX mit FP32-Unterstützung


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **Hinweis:**

1. Der Model Builder unterstützt derzeit die Konvertierung von Phi-3.5-Instruct und Phi-3.5-Vision, aber nicht Phi-3.5-MoE

2. Um ONNXs quantisiertes Modell zu nutzen, können Sie es über das Generative AI-Erweiterungen für onnxruntime SDK verwenden

3. Wir müssen verantwortungsvollere KI berücksichtigen, daher wird nach der Modellquantisierung empfohlen, effektivere Ergebnistests durchzuführen

4. Durch die Quantisierung des CPU INT4-Modells können wir es auf Edge-Geräten einsetzen, was bessere Anwendungsszenarien ermöglicht, deshalb haben wir Phi-3.5-Instruct rund um INT4 abgeschlossen


## **Ressourcen**

1. Erfahren Sie mehr über Generative AI-Erweiterungen für onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI-Erweiterungen für onnxruntime GitHub-Repo [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->