<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3139a6a82f357a9f90f1fe51c4caf65a",
  "translation_date": "2025-05-09T13:56:05+00:00",
  "source_file": "md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "el"
}
-->
# **Ποσοτικοποίηση του Phi-3.5 με χρήση του Intel OpenVINO**

Η Intel είναι ο πιο παραδοσιακός κατασκευαστής CPU με πολλούς χρήστες. Με την άνοδο της μηχανικής μάθησης και της βαθιάς μάθησης, η Intel έχει επίσης μπει στον ανταγωνισμό για επιτάχυνση της τεχνητής νοημοσύνης. Για την εκτέλεση μοντέλων, η Intel δεν χρησιμοποιεί μόνο GPUs και CPUs, αλλά και NPUs.

Ελπίζουμε να αναπτύξουμε την οικογένεια Phi-3.x στην πλευρά του τελικού χρήστη, με στόχο να γίνει το πιο σημαντικό κομμάτι του AI PC και του Copilot PC. Η φόρτωση του μοντέλου στην πλευρά του τελικού χρήστη εξαρτάται από τη συνεργασία διαφορετικών κατασκευαστών υλικού. Αυτό το κεφάλαιο εστιάζει κυρίως στο σενάριο εφαρμογής του Intel OpenVINO ως ποσοτικοποιημένο μοντέλο.


## **Τι είναι το OpenVINO**

Το OpenVINO είναι ένα ανοιχτού κώδικα εργαλείο για τη βελτιστοποίηση και ανάπτυξη μοντέλων βαθιάς μάθησης από το cloud μέχρι την άκρη (edge). Επιταχύνει την εκτέλεση βαθιάς μάθησης σε διάφορα σενάρια, όπως γενετική τεχνητή νοημοσύνη, βίντεο, ήχο και γλώσσα, με μοντέλα από δημοφιλή πλαίσια όπως PyTorch, TensorFlow, ONNX και άλλα. Μετατρέπει και βελτιστοποιεί μοντέλα, και τα αναπτύσσει σε συνδυασμό με υλικό και περιβάλλοντα της Intel®, είτε σε τοπικό επίπεδο, είτε στη συσκευή, είτε στο πρόγραμμα περιήγησης ή στο cloud.

Τώρα με το OpenVINO, μπορείτε γρήγορα να ποσοτικοποιήσετε το μοντέλο GenAI σε υλικό Intel και να επιταχύνετε την αναφορά του μοντέλου.

Το OpenVINO υποστηρίζει πλέον τη μετατροπή ποσοτικοποίησης για τα Phi-3.5-Vision και Phi-3.5 Instruct

### **Ρύθμιση Περιβάλλοντος**

Παρακαλώ βεβαιωθείτε ότι οι παρακάτω εξαρτήσεις περιβάλλοντος είναι εγκατεστημένες, αυτό είναι το requirement.txt

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Ποσοτικοποίηση του Phi-3.5-Instruct με OpenVINO**

Στο τερματικό, τρέξτε αυτό το script

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Ποσοτικοποίηση του Phi-3.5-Vision με OpenVINO**

Παρακαλώ τρέξτε αυτό το script σε Python ή Jupyter lab

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

### **🤖 Παραδείγματα για το Phi-3.5 με Intel OpenVINO**

| Labs    | Περιγραφή | Μετάβαση |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Μάθετε πώς να χρησιμοποιείτε το Phi-3.5 Instruct στο AI PC σας    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (εικόνα) | Μάθετε πώς να χρησιμοποιείτε το Phi-3.5 Vision για ανάλυση εικόνας στο AI PC σας      |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (βίντεο)   | Μάθετε πώς να χρησιμοποιείτε το Phi-3.5 Vision για ανάλυση βίντεο στο AI PC σας    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |



## **Πόροι**

1. Μάθετε περισσότερα για το Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub Repo [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που προσπαθούμε για ακρίβεια, παρακαλούμε να λάβετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.