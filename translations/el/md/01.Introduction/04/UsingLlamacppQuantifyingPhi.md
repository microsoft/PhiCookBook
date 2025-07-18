<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-07-16T22:09:17+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "el"
}
-->
# **Ποσοτικοποίηση της οικογένειας Phi με χρήση του llama.cpp**

## **Τι είναι το llama.cpp**

Το llama.cpp είναι μια ανοιχτού κώδικα βιβλιοθήκη λογισμικού, κυρίως γραμμένη σε C++, που εκτελεί inference σε διάφορα Μεγάλα Γλωσσικά Μοντέλα (LLMs), όπως το Llama. Ο κύριος στόχος του είναι να προσφέρει κορυφαία απόδοση για το inference LLM σε ένα ευρύ φάσμα υλικού με ελάχιστη ρύθμιση. Επιπλέον, υπάρχουν διαθέσιμες Python bindings για αυτή τη βιβλιοθήκη, που παρέχουν ένα υψηλού επιπέδου API για συμπλήρωση κειμένου και έναν OpenAI συμβατό web server.

Ο βασικός σκοπός του llama.cpp είναι να επιτρέψει το inference LLM με ελάχιστη ρύθμιση και κορυφαία απόδοση σε ποικίλο υλικό - τοπικά και στο cloud.

- Απλή υλοποίηση σε C/C++ χωρίς εξαρτήσεις
- Το Apple silicon υποστηρίζεται πλήρως - βελτιστοποιημένο μέσω ARM NEON, Accelerate και Metal frameworks
- Υποστήριξη AVX, AVX2 και AVX512 για αρχιτεκτονικές x86
- Ποσοτικοποίηση ακεραίων 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit και 8-bit για ταχύτερο inference και μειωμένη χρήση μνήμης
- Προσαρμοσμένοι πυρήνες CUDA για εκτέλεση LLM σε NVIDIA GPUs (υποστήριξη για AMD GPUs μέσω HIP)
- Υποστήριξη backend Vulkan και SYCL
- Υβριδικό inference CPU+GPU για μερική επιτάχυνση μοντέλων μεγαλύτερων από τη συνολική χωρητικότητα VRAM

## **Ποσοτικοποίηση του Phi-3.5 με χρήση του llama.cpp**

Το μοντέλο Phi-3.5-Instruct μπορεί να ποσοτικοποιηθεί με το llama.cpp, αλλά τα Phi-3.5-Vision και Phi-3.5-MoE δεν υποστηρίζονται ακόμα. Η μορφή που μετατρέπει το llama.cpp είναι η gguf, η οποία είναι και η πιο διαδεδομένη μορφή ποσοτικοποίησης.

Υπάρχει μεγάλος αριθμός μοντέλων σε ποσοτικοποιημένη μορφή GGUF στο Hugging Face. Οι AI Foundry, Ollama και LlamaEdge βασίζονται στο llama.cpp, οπότε τα μοντέλα GGUF χρησιμοποιούνται συχνά.

### **Τι είναι το GGUF**

Το GGUF είναι μια δυαδική μορφή που έχει βελτιστοποιηθεί για γρήγορη φόρτωση και αποθήκευση μοντέλων, καθιστώντας το ιδιαίτερα αποδοτικό για σκοπούς inference. Το GGUF έχει σχεδιαστεί για χρήση με το GGML και άλλους εκτελεστές. Το GGUF αναπτύχθηκε από τον @ggerganov, ο οποίος είναι επίσης ο δημιουργός του llama.cpp, ενός δημοφιλούς πλαισίου inference LLM σε C/C++. Μοντέλα που αρχικά αναπτύχθηκαν σε πλαίσια όπως το PyTorch μπορούν να μετατραπούν σε μορφή GGUF για χρήση με αυτούς τους εκτελεστές.

### **ONNX vs GGUF**

Το ONNX είναι μια παραδοσιακή μορφή μηχανικής μάθησης/βαθιάς μάθησης, που υποστηρίζεται καλά σε διάφορα AI Frameworks και έχει καλές περιπτώσεις χρήσης σε edge συσκευές. Όσον αφορά το GGUF, βασίζεται στο llama.cpp και μπορεί να θεωρηθεί προϊόν της εποχής GenAI. Οι δύο μορφές έχουν παρόμοιες χρήσεις. Αν θέλετε καλύτερη απόδοση σε ενσωματωμένο υλικό και επίπεδα εφαρμογών, το ONNX μπορεί να είναι η επιλογή σας. Αν χρησιμοποιείτε το παράγωγο πλαίσιο και τεχνολογία του llama.cpp, τότε το GGUF μπορεί να είναι καλύτερο.

### **Ποσοτικοποίηση του Phi-3.5-Instruct με χρήση του llama.cpp**

**1. Ρύθμιση περιβάλλοντος**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Ποσοτικοποίηση**

Μετατροπή του Phi-3.5-Instruct σε FP16 GGUF με χρήση του llama.cpp


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Ποσοτικοποίηση του Phi-3.5 σε INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Δοκιμές**

Εγκατάσταση του llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Σημείωση*** 

Αν χρησιμοποιείτε Apple Silicon, παρακαλώ εγκαταστήστε το llama-cpp-python ως εξής


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Δοκιμές 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Πόροι**

1. Μάθετε περισσότερα για το llama.cpp [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)  
2. Μάθετε περισσότερα για το onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)  
3. Μάθετε περισσότερα για το GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.