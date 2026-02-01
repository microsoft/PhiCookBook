## **Πώς να χρησιμοποιήσετε το Model Builder για την ποσοτικοποίηση του Phi-3.5**

Το Model Builder υποστηρίζει πλέον την ποσοτικοποίηση μοντέλων ONNX για τα Phi-3.5 Instruct και Phi-3.5-Vision.

### **Phi-3.5-Instruct**

**Μετατροπή ποσοτικοποιημένης INT4 με επιτάχυνση CPU**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Μετατροπή ποσοτικοποιημένης INT4 με επιτάχυνση CUDA**

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

5. Μεταβείτε στο τερματικό

    Μετατροπή υποστήριξης ONNX με FP32

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Σημείωση:**

1. Το Model Builder υποστηρίζει προς το παρόν τη μετατροπή των Phi-3.5-Instruct και Phi-3.5-Vision, αλλά όχι του Phi-3.5-MoE.

2. Για να χρησιμοποιήσετε το ποσοτικοποιημένο μοντέλο ONNX, μπορείτε να το κάνετε μέσω του Generative AI extensions για onnxruntime SDK.

3. Πρέπει να λάβουμε υπόψη πιο υπεύθυνη χρήση της τεχνητής νοημοσύνης, γι’ αυτό μετά τη μετατροπή ποσοτικοποίησης του μοντέλου, συνιστάται να γίνουν πιο αποτελεσματικοί έλεγχοι αποτελεσμάτων.

4. Με την ποσοτικοποίηση του μοντέλου CPU INT4, μπορούμε να το αναπτύξουμε σε Edge Devices, που προσφέρουν καλύτερα σενάρια εφαρμογής, γι’ αυτό και ολοκληρώσαμε το Phi-3.5-Instruct γύρω από το INT4.

## **Πόροι**

1. Μάθετε περισσότερα για το Generative AI extensions για onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Αποθετήριο GitHub του Generative AI extensions για onnxruntime [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.