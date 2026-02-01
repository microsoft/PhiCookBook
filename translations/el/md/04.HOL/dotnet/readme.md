## Καλώς ήρθατε στα εργαστήρια Phi με χρήση C#

Υπάρχει μια συλλογή εργαστηρίων που παρουσιάζει πώς να ενσωματώσετε τις ισχυρές διαφορετικές εκδόσεις των μοντέλων Phi σε περιβάλλον .NET.

## Προαπαιτούμενα

Πριν τρέξετε το δείγμα, βεβαιωθείτε ότι έχετε εγκαταστήσει τα εξής:

**.NET 9:** Βεβαιωθείτε ότι έχετε εγκαταστήσει την [τελευταία έκδοση του .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) στον υπολογιστή σας.

**(Προαιρετικά) Visual Studio ή Visual Studio Code:** Θα χρειαστείτε ένα IDE ή έναν επεξεργαστή κώδικα που να μπορεί να τρέξει έργα .NET. Συνιστώνται το [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) ή το [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo).

**Χρησιμοποιώντας git** κάντε κλωνοποίηση τοπικά μιας από τις διαθέσιμες εκδόσεις Phi-3, Phi3.5 ή Phi-4 από το [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**Κατεβάστε τα μοντέλα Phi-4 ONNX** στον τοπικό σας υπολογιστή:

### πλοηγηθείτε στον φάκελο όπου θα αποθηκευτούν τα μοντέλα

```bash
cd c:\phi\models
```

### προσθέστε υποστήριξη για lfs

```bash
git lfs install 
```

### κλωνοποιήστε και κατεβάστε το μοντέλο Phi-4 mini instruct και το μοντέλο Phi-4 multi modal

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Κατεβάστε τα μοντέλα Phi-3 ONNX** στον τοπικό σας υπολογιστή:

### κλωνοποιήστε και κατεβάστε το μοντέλο Phi-3 mini 4K instruct και το μοντέλο Phi-3 vision 128K

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Σημαντικό:** Τα τρέχοντα demos έχουν σχεδιαστεί για να χρησιμοποιούν τις ONNX εκδόσεις των μοντέλων. Τα προηγούμενα βήματα κλωνοποιούν τα παρακάτω μοντέλα.

## Σχετικά με τα Εργαστήρια

Η κύρια λύση περιλαμβάνει αρκετά δείγματα εργαστηρίων που παρουσιάζουν τις δυνατότητες των μοντέλων Phi με χρήση C#.

| Project | Model | Περιγραφή |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 ή Phi-3.5 | Δείγμα συνομιλίας κονσόλας που επιτρέπει στον χρήστη να κάνει ερωτήσεις. Το έργο φορτώνει τοπικά ένα ONNX μοντέλο Phi-3 χρησιμοποιώντας τις βιβλιοθήκες `Microsoft.ML.OnnxRuntime`. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 ή Phi-3.5 | Δείγμα συνομιλίας κονσόλας που επιτρέπει στον χρήστη να κάνει ερωτήσεις. Το έργο φορτώνει τοπικά ένα ONNX μοντέλο Phi-3 χρησιμοποιώντας τις βιβλιοθήκες `Microsoft.Semantic.Kernel`. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 ή Phi-3.5 | Πρόκειται για ένα δείγμα έργου που χρησιμοποιεί τοπικό μοντέλο phi3 vision για ανάλυση εικόνων. Το έργο φορτώνει τοπικά ένα ONNX μοντέλο Phi-3 Vision χρησιμοποιώντας τις βιβλιοθήκες `Microsoft.ML.OnnxRuntime`. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 ή Phi-3.5 | Πρόκειται για ένα δείγμα έργου που χρησιμοποιεί τοπικό μοντέλο phi3 vision για ανάλυση εικόνων. Το έργο φορτώνει τοπικά ένα ONNX μοντέλο Phi-3 Vision χρησιμοποιώντας τις βιβλιοθήκες `Microsoft.ML.OnnxRuntime`. Το έργο παρουσιάζει επίσης ένα μενού με διάφορες επιλογές για αλληλεπίδραση με τον χρήστη. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Δείγμα συνομιλίας κονσόλας που επιτρέπει στον χρήστη να κάνει ερωτήσεις. Το έργο φορτώνει τοπικά ένα ONNX μοντέλο Phi-4 χρησιμοποιώντας τις βιβλιοθήκες `Microsoft.ML.OnnxRuntime`. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Δείγμα συνομιλίας κονσόλας που επιτρέπει στον χρήστη να κάνει ερωτήσεις. Το έργο φορτώνει τοπικά ένα ONNX μοντέλο Phi-4 χρησιμοποιώντας τις βιβλιοθήκες `Semantic Kernel`. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Δείγμα συνομιλίας κονσόλας που επιτρέπει στον χρήστη να κάνει ερωτήσεις. Το έργο φορτώνει τοπικά ένα ONNX μοντέλο Phi-4 χρησιμοποιώντας τις βιβλιοθήκες `Microsoft.ML.OnnxRuntimeGenAI` και υλοποιεί το `IChatClient` από το `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Δείγμα συνομιλίας κονσόλας που επιτρέπει στον χρήστη να κάνει ερωτήσεις. Η συνομιλία υποστηρίζει μνήμη. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | Πρόκειται για ένα δείγμα έργου που χρησιμοποιεί τοπικό μοντέλο Phi-4 για ανάλυση εικόνων και εμφανίζει το αποτέλεσμα στην κονσόλα. Το έργο φορτώνει τοπικά το μοντέλο Phi-4-`multimodal-instruct-onnx` χρησιμοποιώντας τις βιβλιοθήκες `Microsoft.ML.OnnxRuntime`. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | Πρόκειται για ένα δείγμα έργου που χρησιμοποιεί τοπικό μοντέλο Phi-4 για ανάλυση αρχείου ήχου, δημιουργεί τη μεταγραφή του αρχείου και εμφανίζει το αποτέλεσμα στην κονσόλα. Το έργο φορτώνει τοπικά το μοντέλο Phi-4-`multimodal-instruct-onnx` χρησιμοποιώντας τις βιβλιοθήκες `Microsoft.ML.OnnxRuntime`. |

## Πώς να τρέξετε τα έργα

Για να τρέξετε τα έργα, ακολουθήστε τα παρακάτω βήματα:

1. Κλωνοποιήστε το αποθετήριο στον τοπικό σας υπολογιστή.

1. Ανοίξτε ένα τερματικό και πλοηγηθείτε στο επιθυμητό έργο. Για παράδειγμα, ας τρέξουμε το `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Τρέξτε το έργο με την εντολή

    ```bash
    dotnet run
    ```

1. Το δείγμα έργο ζητάει είσοδο από τον χρήστη και απαντά χρησιμοποιώντας το τοπικό μοντέλο.

   Το τρέχον demo είναι παρόμοιο με το παρακάτω:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.