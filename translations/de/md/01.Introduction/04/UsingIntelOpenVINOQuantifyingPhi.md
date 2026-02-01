# **Quantisierung von Phi-3.5 mit Intel OpenVINO**

Intel ist der traditionellste CPU-Hersteller mit vielen Anwendern. Mit dem Aufstieg von Machine Learning und Deep Learning ist Intel auch in den Wettbewerb um AI-Beschleunigung eingestiegen. Für die Modellausführung nutzt Intel nicht nur GPUs und CPUs, sondern auch NPUs.

Wir möchten die Phi-3.x-Familie am Endgerät einsetzen und hoffen, damit zum wichtigsten Bestandteil von AI-PCs und Copilot-PCs zu werden. Das Laden des Modells am Endgerät hängt von der Zusammenarbeit verschiedener Hardware-Hersteller ab. Dieses Kapitel konzentriert sich hauptsächlich auf das Anwendungsszenario von Intel OpenVINO als quantifiziertes Modell.

## **Was ist OpenVINO**

OpenVINO ist ein Open-Source-Toolkit zur Optimierung und Bereitstellung von Deep-Learning-Modellen vom Cloud- bis zum Edge-Bereich. Es beschleunigt die Deep-Learning-Inferenz in verschiedenen Anwendungsfällen wie generativer KI, Video, Audio und Sprache mit Modellen aus beliebten Frameworks wie PyTorch, TensorFlow, ONNX und mehr. Modelle können konvertiert und optimiert sowie auf einer Mischung aus Intel®-Hardware und Umgebungen bereitgestellt werden – lokal, auf Geräten, im Browser oder in der Cloud.

Mit OpenVINO können Sie nun schnell GenAI-Modelle auf Intel-Hardware quantisieren und die Modellreferenz beschleunigen.

OpenVINO unterstützt jetzt die Quantisierungsumwandlung von Phi-3.5-Vision und Phi-3.5 Instruct.

### **Umgebung einrichten**

Bitte stellen Sie sicher, dass die folgenden Abhängigkeiten installiert sind, dies ist requirement.txt

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Quantisierung von Phi-3.5-Instruct mit OpenVINO**

Bitte führen Sie dieses Skript im Terminal aus

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Quantisierung von Phi-3.5-Vision mit OpenVINO**

Bitte führen Sie dieses Skript in Python oder Jupyter Lab aus

```python

import requests
from pathlib import Path
from ov_phi3_vision import convert_phi3_model
import nncf

if not Path("ov_phi3_vision.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/notebooks/phi-3-vision/ov_phi3_vision.py")
    open("ov_phi3_vision.py", "w").write(r.text)


if not Path("gradio_helper.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/notebooks/phi-3-vision/gradio_helper.py")
    open("gradio_helper.py", "w").write(r.text)

if not Path("notebook_utils.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/utils/notebook_utils.py")
    open("notebook_utils.py", "w").write(r.text)



model_id = "microsoft/Phi-3.5-vision-instruct"
out_dir = Path("../model/phi-3.5-vision-128k-instruct-ov")
compression_configuration = {
    "mode": nncf.CompressWeightsMode.INT4_SYM,
    "group_size": 64,
    "ratio": 0.6,
}
if not out_dir.exists():
    convert_phi3_model(model_id, out_dir, compression_configuration)

```

### **🤖 Beispiele für Phi-3.5 mit Intel OpenVINO**

| Labs    | Einführung | Los geht’s |
| -------- | ------- |  ------- |
| 🚀 Lab-Einführung Phi-3.5 Instruct  | Lernen Sie, wie Sie Phi-3.5 Instruct in Ihrem AI-PC verwenden    |  [Los geht’s](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Einführung Phi-3.5 Vision (Bild) | Lernen Sie, wie Sie Phi-3.5 Vision zur Bildanalyse in Ihrem AI-PC einsetzen      |  [Los geht’s](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Einführung Phi-3.5 Vision (Video)   | Lernen Sie, wie Sie Phi-3.5 Vision zur Videoanalyse in Ihrem AI-PC einsetzen    |  [Los geht’s](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Ressourcen**

1. Mehr erfahren über Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub Repo [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.