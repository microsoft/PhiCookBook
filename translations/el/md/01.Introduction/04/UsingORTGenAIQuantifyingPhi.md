# **Κβαντοποίηση της οικογένειας Phi χρησιμοποιώντας επεκτάσεις Generative AI για onnxruntime**

## **Τι είναι οι επεκτάσεις Generative AI για onnxruntime**

Αυτές οι επεκτάσεις σας βοηθούν να εκτελείτε generative AI με το ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Παρέχουν τον βρόχο generative AI για μοντέλα ONNX, συμπεριλαμβανομένης της εκτέλεσης με ONNX Runtime, της επεξεργασίας των logits, της αναζήτησης και δειγματοληψίας, καθώς και της διαχείρισης της μνήμης KV cache. Οι προγραμματιστές μπορούν να καλέσουν μια υψηλού επιπέδου μέθοδο generate(), ή να εκτελέσουν κάθε επανάληψη του μοντέλου σε βρόχο, παράγοντας ένα token τη φορά και προαιρετικά ενημερώνοντας τις παραμέτρους γενιάς μέσα στον βρόχο. Υποστηρίζει αναζήτηση greedy/beam, δειγματοληψία TopP, TopK για τη δημιουργία ακολουθιών token και ενσωματωμένη επεξεργασία logits όπως ποινές επανάληψης. Μπορείτε επίσης εύκολα να προσθέσετε προσαρμοσμένη βαθμολόγηση.

Σε επίπεδο εφαρμογής, μπορείτε να χρησιμοποιήσετε τις επεκτάσεις Generative AI για onnxruntime για να κατασκευάσετε εφαρμογές με C++/ C# / Python. Σε επίπεδο μοντέλου, μπορείτε να το χρησιμοποιήσετε για να συγχωνεύσετε μοντέλα που έχουν βελτιωθεί και να κάνετε σχετική ποσοτική ανάπτυξη.


## **Κβαντοποίηση του Phi-3.5 με επεκτάσεις Generative AI για onnxruntime**

### **Υποστηριζόμενα Μοντέλα**

Οι επεκτάσεις Generative AI για onnxruntime υποστηρίζουν τη μετατροπή κβαντοποίησης των Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.


### **Κατασκευαστής Μοντέλων στις επεκτάσεις Generative AI για onnxruntime**

Ο κατασκευαστής μοντέλων επιταχύνει σημαντικά τη δημιουργία βελτιστοποιημένων και κβαντοποιημένων μοντέλων ONNX που εκτελούνται με το API generate() του ONNX Runtime.

Μέσω του Κατασκευαστή Μοντέλων, μπορείτε να κβαντοποιήσετε το μοντέλο σε INT4, INT8, FP16, FP32 και να συνδυάσετε διάφορες μεθόδους επιτάχυνσης υλικού όπως CPU, CUDA, DirectML, Mobile, κ.ά.

Για να χρησιμοποιήσετε τον Κατασκευαστή Μοντέλων χρειάζεται να εγκαταστήσετε

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Μετά την εγκατάσταση, μπορείτε να εκτελέσετε το σενάριο του Κατασκευαστή Μοντέλων από το τερματικό για να πραγματοποιήσετε μετατροπή μορφής μοντέλου και κβαντοποίησης.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Κατανοήστε τις σχετικές παραμέτρους

1. **model_name** Αυτό είναι το μοντέλο στο Hugging face, όπως microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct, κ.ά. Μπορεί επίσης να είναι η διαδρομή όπου αποθηκεύετε το μοντέλο

2. **path_to_output_folder** Διαδρομή αποθήκευσης της κβαντοποιημένης μετατροπής

3. **execution_provider** Υποστήριξη διαφορετικής επιτάχυνσης υλικού, όπως cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** Κατεβάζουμε το μοντέλο από το Hugging face και το αποθηκεύουμε προσωρινά τοπικά




***Σημείωση：*** <ul>Αν και οι επεκτάσεις Generative AI για onnxruntime είναι σε δοκιμαστική φάση, έχουν ενσωματωθεί στο Microsoft Olive, και μπορείτε επίσης να καλέσετε τις λειτουργίες του Model Builder των επεκτάσεων Generative AI για onnxruntime μέσω του Microsoft Olive.</ul>

## **Πώς να χρησιμοποιήσετε τον Κατασκευαστή Μοντέλων για την κβαντοποίηση του Phi-3.5**

Ο Κατασκευαστής Μοντέλων πλέον υποστηρίζει κβαντοποίηση μοντέλων ONNX για το Phi-3.5 Instruct και το Phi-3.5-Vision

### **Phi-3.5-Instruct**


**Επιτάχυνση μετατροπής κβαντοποιημένου INT 4 με CPU**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Επιτάχυνση μετατροπής κβαντοποιημένου INT 4 με CUDA**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Ρυθμίστε το περιβάλλον στο τερματικό

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


### **Σημείωση：**

1. Ο Κατασκευαστής Μοντέλων επί του παρόντος υποστηρίζει τη μετατροπή για το Phi-3.5-Instruct και το Phi-3.5-Vision, αλλά όχι το Phi-3.5-MoE

2. Για να χρησιμοποιήσετε το κβαντοποιημένο μοντέλο ONNX, μπορείτε να το χρησιμοποιήσετε μέσω του SDK των επεκτάσεων Generative AI για onnxruntime

3. Πρέπει να λάβουμε υπόψη πιο υπεύθυνη χρήση της AI, οπότε μετά τη μετατροπή κβαντοποίησης του μοντέλου, συνιστάται να πραγματοποιηθεί πιο αποτελεσματική δοκιμή αποτελεσμάτων

4. Με την κβαντοποίηση του μοντέλου CPU INT4, μπορούμε να το αναπτύξουμε σε Edge Device, που έχει καλύτερα σενάρια εφαρμογής, οπότε έχουμε ολοκληρώσει το Phi-3.5-Instruct γύρω από το INT 4


## **Πόροι**

1. Μάθετε περισσότερα για τις επεκτάσεις Generative AI για onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Αποθετήριο GitHub των επεκτάσεων Generative AI για onnxruntime [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->