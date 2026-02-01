# **Inference Phi-3 σε Android**

Ας δούμε πώς μπορείτε να κάνετε inference με το Phi-3-mini σε συσκευές Android. Το Phi-3-mini είναι μια νέα σειρά μοντέλων από τη Microsoft που επιτρέπει την ανάπτυξη Μεγάλων Γλωσσικών Μοντέλων (LLMs) σε edge συσκευές και συσκευές IoT.

## Semantic Kernel και Inference

Το [Semantic Kernel](https://github.com/microsoft/semantic-kernel) είναι ένα πλαίσιο εφαρμογών που σας επιτρέπει να δημιουργείτε εφαρμογές συμβατές με το Azure OpenAI Service, τα μοντέλα OpenAI, και ακόμη και τοπικά μοντέλα. Αν είστε νέοι στο Semantic Kernel, σας προτείνουμε να δείτε το [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Πρόσβαση στο Phi-3-mini μέσω Semantic Kernel

Μπορείτε να το συνδυάσετε με το Hugging Face Connector στο Semantic Kernel. Ανατρέξτε σε αυτό το [Παράδειγμα Κώδικα](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Κατά προεπιλογή, αντιστοιχεί στο model ID στο Hugging Face. Ωστόσο, μπορείτε επίσης να συνδεθείτε σε έναν τοπικά κατασκευασμένο server μοντέλου Phi-3-mini.

### Κλήση Ποσοτικοποιημένων Μοντέλων με Ollama ή LlamaEdge

Πολλοί χρήστες προτιμούν να χρησιμοποιούν ποσοτικοποιημένα μοντέλα για να τρέχουν μοντέλα τοπικά. Το [Ollama](https://ollama.com/) και το [LlamaEdge](https://llamaedge.com) επιτρέπουν σε μεμονωμένους χρήστες να καλούν διάφορα ποσοτικοποιημένα μοντέλα:

#### Ollama

Μπορείτε να τρέξετε απευθείας `ollama run Phi-3` ή να το ρυθμίσετε εκτός σύνδεσης δημιουργώντας ένα `Modelfile` με τη διαδρομή προς το αρχείο `.gguf` σας.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Παράδειγμα Κώδικα](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Αν θέλετε να χρησιμοποιήσετε αρχεία `.gguf` ταυτόχρονα στο cloud και σε edge συσκευές, το LlamaEdge είναι μια εξαιρετική επιλογή. Μπορείτε να ανατρέξετε σε αυτό το [παράδειγμα κώδικα](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) για να ξεκινήσετε.

### Εγκατάσταση και Εκτέλεση σε Android Τηλέφωνα

1. **Κατεβάστε την εφαρμογή MLC Chat** (δωρεάν) για Android τηλέφωνα.  
2. Κατεβάστε το αρχείο APK (148MB) και εγκαταστήστε το στη συσκευή σας.  
3. Εκκινήστε την εφαρμογή MLC Chat. Θα δείτε μια λίστα με μοντέλα AI, συμπεριλαμβανομένου του Phi-3-mini.

Συνοψίζοντας, το Phi-3-mini ανοίγει συναρπαστικές δυνατότητες για γεννητική AI σε edge συσκευές, και μπορείτε να ξεκινήσετε να εξερευνάτε τις δυνατότητές του σε Android.

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.