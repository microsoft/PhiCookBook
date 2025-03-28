<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3bb9f5c926673593287eddc3741226cb",
  "translation_date": "2025-03-27T08:43:19+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingORTGenAIQuantifyingPhi.md",
  "language_code": "de"
}
-->
# **Quantisierung der Phi-Familie mit Generative AI Extensions für onnxruntime**

## **Was sind Generative AI Extensions für onnxruntime**

Diese Erweiterungen helfen Ihnen, generative KI mit ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)) auszuführen. Sie bieten die generative KI-Schleife für ONNX-Modelle, einschließlich Inferenz mit ONNX Runtime, Verarbeitung von Logits, Suche und Sampling sowie Verwaltung des KV-Caches. Entwickler können entweder die hochrangige Methode `generate()` aufrufen oder jede Iteration des Modells in einer Schleife ausführen, wobei ein Token nach dem anderen generiert wird. Dabei können die Generierungsparameter innerhalb der Schleife optional aktualisiert werden. Es werden Greedy-/Beam-Suche und TopP-, TopK-Sampling unterstützt, um Token-Sequenzen zu generieren, sowie integrierte Logits-Verarbeitung wie Wiederholungsstrafen. Eigene Bewertungsmethoden können ebenfalls einfach hinzugefügt werden.

Auf Anwendungsebene können Sie Generative AI Extensions für onnxruntime verwenden, um Anwendungen mit C++/C#/Python zu erstellen. Auf Modellebene können Sie damit feingetunte Modelle zusammenführen und damit verbundene quantitative Bereitstellungsarbeiten durchführen.

## **Quantisierung von Phi-3.5 mit Generative AI Extensions für onnxruntime**

### **Unterstützte Modelle**

Generative AI Extensions für onnxruntime unterstützen die Quantisierungsumwandlung von Microsoft Phi, Google Gemma, Mistral und Meta LLaMA.

### **Model Builder in Generative AI Extensions für onnxruntime**

Der Model Builder beschleunigt die Erstellung optimierter und quantisierter ONNX-Modelle, die mit der ONNX Runtime `generate()` API ausgeführt werden, erheblich.

Mit dem Model Builder können Sie das Modell auf INT4, INT8, FP16, FP32 quantisieren und verschiedene Hardware-Beschleunigungsmethoden wie CPU, CUDA, DirectML, Mobile usw. kombinieren.

Um den Model Builder zu verwenden, müssen Sie Folgendes installieren:

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Nach der Installation können Sie das Model Builder-Skript vom Terminal aus ausführen, um die Modellformat- und Quantisierungsumwandlung durchzuführen.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Verstehen Sie die relevanten Parameter:

1. **model_name** Dies ist das Modell auf Hugging Face, wie z. B. `microsoft/Phi-3.5-mini-instruct`, `microsoft/Phi-3.5-vision-instruct` usw. Es kann auch der Pfad sein, in dem Sie das Modell speichern.

2. **path_to_output_folder** Speicherpfad für die quantisierte Umwandlung.

3. **execution_provider** Unterstützung für verschiedene Hardwarebeschleunigungen, wie z. B. CPU, CUDA, DirectML.

4. **cache_dir_to_save_hf_files** Wir laden das Modell von Hugging Face herunter und cachen es lokal.

***Hinweis:***  

## **Wie man den Model Builder verwendet, um Phi-3.5 zu quantisieren**

Der Model Builder unterstützt jetzt die ONNX-Modellquantisierung für Phi-3.5 Instruct und Phi-3.5-Vision.

### **Phi-3.5-Instruct**

**CPU-beschleunigte Umwandlung in quantisiertes INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA-beschleunigte Umwandlung in quantisiertes INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Umgebung im Terminal einrichten:

```bash

mkdir models

cd models 

```

2. Laden Sie `microsoft/Phi-3.5-vision-instruct` in den Ordner `models` herunter:  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Bitte laden Sie diese Dateien in Ihren Ordner `Phi-3.5-vision-instruct` herunter:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Laden Sie diese Datei in den Ordner `models` herunter:  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Öffnen Sie das Terminal:

    Umwandlung in ONNX mit FP32 durchführen:

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Hinweis:**

1. Der Model Builder unterstützt derzeit die Umwandlung von Phi-3.5-Instruct und Phi-3.5-Vision, jedoch nicht Phi-3.5-MoE.

2. Um das quantisierte Modell von ONNX zu verwenden, können Sie dies über das Generative AI Extensions für onnxruntime SDK tun.

3. Wir müssen verantwortungsvollere KI in Betracht ziehen. Daher wird empfohlen, nach der Modellquantisierungsumwandlung effektivere Ergebnistests durchzuführen.

4. Durch die Quantisierung des CPU-INT4-Modells können wir es auf Edge-Geräten bereitstellen, was bessere Anwendungsszenarien bietet. Daher haben wir Phi-3.5-Instruct auf INT4 optimiert.

## **Ressourcen**

1. Erfahren Sie mehr über Generative AI Extensions für onnxruntime: [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. GitHub-Repository der Generative AI Extensions für onnxruntime: [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung resultieren.