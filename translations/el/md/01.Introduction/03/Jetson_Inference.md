<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be4101a30d98e95a71d42c276e8bcd37",
  "translation_date": "2025-05-09T11:37:37+00:00",
  "source_file": "md/01.Introduction/03/Jetson_Inference.md",
  "language_code": "el"
}
-->
# **Inference Phi-3 στο Nvidia Jetson**

Το Nvidia Jetson είναι μια σειρά ενσωματωμένων υπολογιστικών πλακετών από την Nvidia. Τα μοντέλα Jetson TK1, TX1 και TX2 διαθέτουν επεξεργαστή Tegra (ή SoC) από την Nvidia που ενσωματώνει μια κεντρική μονάδα επεξεργασίας (CPU) με αρχιτεκτονική ARM. Το Jetson είναι ένα σύστημα χαμηλής κατανάλωσης ενέργειας και έχει σχεδιαστεί για επιτάχυνση εφαρμογών μηχανικής μάθησης. Το Nvidia Jetson χρησιμοποιείται από επαγγελματίες προγραμματιστές για τη δημιουργία πρωτοποριακών προϊόντων AI σε όλους τους κλάδους, καθώς και από φοιτητές και ενθουσιώδεις για πρακτική μάθηση AI και υλοποίηση εντυπωσιακών έργων. Το SLM αναπτύσσεται σε edge συσκευές όπως το Jetson, επιτρέποντας καλύτερη εφαρμογή σε βιομηχανικά σενάρια γενετικής AI.

## Ανάπτυξη στο NVIDIA Jetson:
Οι προγραμματιστές που εργάζονται σε αυτόνομα ρομπότ και ενσωματωμένες συσκευές μπορούν να αξιοποιήσουν το Phi-3 Mini. Το σχετικά μικρό μέγεθος του Phi-3 το καθιστά ιδανικό για edge ανάπτυξη. Οι παράμετροι έχουν ρυθμιστεί προσεκτικά κατά την εκπαίδευση, εξασφαλίζοντας υψηλή ακρίβεια στις απαντήσεις.

### Βελτιστοποίηση TensorRT-LLM:
Η βιβλιοθήκη [TensorRT-LLM της NVIDIA](https://github.com/NVIDIA/TensorRT-LLM?WT.mc_id=aiml-138114-kinfeylo) βελτιστοποιεί την εκτέλεση μεγάλων γλωσσικών μοντέλων. Υποστηρίζει το μεγάλο παράθυρο συμφραζομένων του Phi-3 Mini, βελτιώνοντας τόσο την απόδοση όσο και την καθυστέρηση. Οι βελτιστοποιήσεις περιλαμβάνουν τεχνικές όπως LongRoPE, FP8 και inflight batching.

### Διαθεσιμότητα και Ανάπτυξη:
Οι προγραμματιστές μπορούν να εξερευνήσουν το Phi-3 Mini με το παράθυρο συμφραζομένων 128K στο [NVIDIA AI](https://www.nvidia.com/en-us/ai-data-science/generative-ai/). Πακετάρεται ως NVIDIA NIM, ένα microservice με τυποποιημένο API που μπορεί να αναπτυχθεί οπουδήποτε. Επιπλέον, οι [υλοποιήσεις TensorRT-LLM στο GitHub](https://github.com/NVIDIA/TensorRT-LLM).

## **1. Προετοιμασία**

a. Jetson Orin NX / Jetson NX

b. JetPack 5.1.2+

c. Cuda 11.8

d. Python 3.8+

## **2. Εκτέλεση του Phi-3 στο Jetson**

Μπορούμε να επιλέξουμε [Ollama](https://ollama.com) ή [LlamaEdge](https://llamaedge.com)

Αν θέλετε να χρησιμοποιήσετε gguf ταυτόχρονα σε cloud και edge συσκευές, το LlamaEdge μπορεί να θεωρηθεί ως WasmEdge (το WasmEdge είναι ένα ελαφρύ, υψηλής απόδοσης, κλιμακούμενο περιβάλλον εκτέλεσης WebAssembly κατάλληλο για cloud native, edge και αποκεντρωμένες εφαρμογές. Υποστηρίζει serverless εφαρμογές, ενσωματωμένες λειτουργίες, microservices, έξυπνα συμβόλαια και IoT συσκευές). Μπορείτε να αναπτύξετε το ποσοτικό μοντέλο gguf σε edge συσκευές και στο cloud μέσω του LlamaEdge.

![llamaedge](../../../../../translated_images/llamaedge.1356a35c809c5e9d89d8168db0c92161e87f5e2c34831f2fad800f00fc4e74dc.el.jpg)

Ακολουθούν τα βήματα χρήσης

1. Εγκαταστήστε και κατεβάστε τις σχετικές βιβλιοθήκες και αρχεία

```bash

curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | bash -s -- --plugin wasi_nn-ggml

curl -LO https://github.com/LlamaEdge/LlamaEdge/releases/latest/download/llama-api-server.wasm

curl -LO https://github.com/LlamaEdge/chatbot-ui/releases/latest/download/chatbot-ui.tar.gz

tar xzf chatbot-ui.tar.gz

```

**Σημείωση**: Τα αρχεία llama-api-server.wasm και chatbot-ui πρέπει να βρίσκονται στον ίδιο φάκελο

2. Εκτελέστε τα scripts στο τερματικό

```bash

wasmedge --dir .:. --nn-preload default:GGML:AUTO:{Your gguf path} llama-api-server.wasm -p phi-3-chat

```

Αυτό είναι το αποτέλεσμα εκτέλεσης

![llamaedgerun](../../../../../translated_images/llamaedgerun.66eb2acd7f14e814437879522158b9531ae7c955014d48d0708d0e4ce6ac94a6.el.png)

***Παραδειγματικός κώδικας*** [Phi-3 mini WASM Notebook Sample](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm)

Συνοψίζοντας, το Phi-3 Mini αποτελεί ένα σημαντικό βήμα προόδου στη γλωσσική μοντελοποίηση, συνδυάζοντας αποδοτικότητα, επίγνωση συμφραζομένων και τις βελτιστοποιήσεις της NVIDIA. Είτε κατασκευάζετε ρομπότ είτε edge εφαρμογές, το Phi-3 Mini είναι ένα ισχυρό εργαλείο που αξίζει να γνωρίζετε.

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που προσπαθούμε για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται η επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.