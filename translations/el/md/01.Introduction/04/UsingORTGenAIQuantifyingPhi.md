<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3bb9f5c926673593287eddc3741226cb",
  "translation_date": "2025-05-09T14:31:09+00:00",
  "source_file": "md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md",
  "language_code": "el"
}
-->
## **Πώς να χρησιμοποιήσετε το Model Builder για την κβαντοποίηση του Phi-3.5**

Το Model Builder υποστηρίζει τώρα την κβαντοποίηση μοντέλων ONNX για τα Phi-3.5 Instruct και Phi-3.5-Vision

### **Phi-3.5-Instruct**

**Επιτάχυνση με CPU για κβαντοποίηση INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Επιτάχυνση με CUDA για κβαντοποίηση INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Ορίστε το περιβάλλον στο τερματικό

```bash

mkdir models

cd models 

```

2. Κατεβάστε το microsoft/Phi-3.5-vision-instruct στον φάκελο models  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Παρακαλώ κατεβάστε αυτά τα αρχεία στον φάκελο Phi-3.5-vision-instruct σας

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Κατεβάστε αυτό το αρχείο στον φάκελο models  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Πηγαίνετε στο τερματικό

   Μετατρέψτε το ONNX με υποστήριξη FP32

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Note：**

1. Το Model Builder υποστηρίζει προς το παρόν τη μετατροπή των Phi-3.5-Instruct και Phi-3.5-Vision, όχι όμως το Phi-3.5-MoE

2. Για να χρησιμοποιήσετε το κβαντισμένο μοντέλο ONNX, μπορείτε να το κάνετε μέσω του Generative AI extensions for onnxruntime SDK

3. Πρέπει να λάβουμε υπόψη πιο υπεύθυνη χρήση της AI, γι’ αυτό μετά την κβαντοποίηση του μοντέλου συνιστάται να γίνουν πιο αποτελεσματικοί έλεγχοι των αποτελεσμάτων

4. Με την κβαντοποίηση του μοντέλου CPU INT4, μπορούμε να το αναπτύξουμε σε Edge Device, κάτι που προσφέρει καλύτερα σενάρια εφαρμογής, έτσι ολοκληρώσαμε το Phi-3.5-Instruct γύρω από το INT 4

## **Πόροι**

1. Μάθετε περισσότερα για το Generative AI extensions for onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Αποθετήριο GitHub του Generative AI extensions for onnxruntime [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που προσπαθούμε για ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.