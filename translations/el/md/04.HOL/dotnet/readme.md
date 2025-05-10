<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-05-09T22:43:48+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "el"
}
-->
﻿## Καλώς ήρθατε στα εργαστήρια Phi με χρήση C#

Υπάρχει μια συλλογή εργαστηρίων που παρουσιάζουν πώς να ενσωματώσετε τις ισχυρές διαφορετικές εκδόσεις των μοντέλων Phi σε ένα περιβάλλον .NET.

## Προαπαιτούμενα

Πριν εκτελέσετε το δείγμα, βεβαιωθείτε ότι έχετε εγκαταστήσει τα εξής:

**.NET 9:** Βεβαιωθείτε ότι έχετε εγκαταστήσει την [τελευταία έκδοση του .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) στον υπολογιστή σας.

**(Προαιρετικά) Visual Studio ή Visual Studio Code:** Θα χρειαστείτε ένα IDE ή έναν επεξεργαστή κώδικα που να μπορεί να τρέξει .NET έργα. Συνιστώνται το [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) ή το [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo).

**Χρησιμοποιώντας git** κάντε κλωνοποίηση τοπικά μιας από τις διαθέσιμες εκδόσεις Phi-3, Phi3.5 ή Phi-4 από το [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**Κατεβάστε τα μοντέλα Phi-4 ONNX** στον τοπικό σας υπολογιστή:

### μεταβείτε στον φάκελο όπου θα αποθηκεύσετε τα μοντέλα

```bash
cd c:\phi\models
```

### προσθέστε υποστήριξη για lfs

```bash
git lfs install 
```

### κλωνοποιήστε και κατεβάστε το μοντέλο Phi-4 mini instruct και το πολυτροπικό μοντέλο Phi-4

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

**Σημαντικό:** Τα τρέχοντα demos έχουν σχεδιαστεί για να χρησιμοποιούν τις ONNX εκδόσεις των μοντέλων. Τα προηγούμενα βήματα κλωνοποιούν τα εξής μοντέλα.

## Σχετικά με τα Εργαστήρια

Η κύρια λύση περιλαμβάνει αρκετά δείγματα εργαστηρίων που παρουσιάζουν τις δυνατότητες των μοντέλων Phi με χρήση C#.

| Project | Model | Περιγραφή |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 ή Phi-3.5 | Δείγμα κονσόλας συνομιλίας που επιτρέπει στον χρήστη να κάνει ερωτήσεις. Το έργο φορτώνει ένα τοπικό ONNX μοντέλο Phi-3 χρησιμοποιώντας το `Microsoft.ML.OnnxRuntime` libraries. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 or Phi-3.5 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-3 model using the `Microsoft.Semantic.Kernel` libraries. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 or Phi-3.5 | This is a sample project that uses a local phi3 vision model to analyze images. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 or Phi-3.5 | This is a sample project that uses a local phi3 vision model to analyze images.. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. The project also presents a menu with different options to interacti with the user. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Semantic Kernel` libraries. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntimeGenAI` libraries and implements the `IChatClient` from `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Sample console chat that allows the user to ask questions. The chat implements memory. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | This is a sample project that uses a local Phi-4 model to analyze images showing the result in the console. The project load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 |This is a sample project that uses a local Phi-4 model to analyze an audio file, generate the transcript of the file and show the result in the console. The project load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |

## How to Run the Projects

To run the projects, follow these steps:

1. Clone the repository to your local machine.

1. Open a terminal and navigate to the desired project. In example, let's run `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Εκτελέστε το έργο με την εντολή

    ```bash
    dotnet run
    ```

1. Το δείγμα έργο ζητά είσοδο από τον χρήστη και απαντά χρησιμοποιώντας το τοπικό μοντέλο.

   Το τρέχον demo είναι παρόμοιο με το εξής:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να λάβετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η επίσημη πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.