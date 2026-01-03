<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "82af197df38d25346a98f1f0e84d1698",
  "translation_date": "2025-07-16T20:21:33+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference.md",
  "language_code": "el"
}
-->
# **Inference Phi-3 σε iOS**

Το Phi-3-mini είναι μια νέα σειρά μοντέλων από τη Microsoft που επιτρέπει την ανάπτυξη Μεγάλων Γλωσσικών Μοντέλων (LLMs) σε edge συσκευές και συσκευές IoT. Το Phi-3-mini είναι διαθέσιμο για iOS, Android και Edge Device deployments, επιτρέποντας την ανάπτυξη γεννητικής τεχνητής νοημοσύνης σε περιβάλλοντα BYOD. Το παρακάτω παράδειγμα δείχνει πώς να αναπτύξετε το Phi-3-mini σε iOS.

## **1. Προετοιμασία**

- **a.** macOS 14+
- **b.** Xcode 15+
- **c.** iOS SDK 17.x (iPhone 14 A16 ή νεότερο)
- **d.** Εγκατάσταση Python 3.10+ (συνιστάται Conda)
- **e.** Εγκατάσταση της βιβλιοθήκης Python: `python-flatbuffers`
- **f.** Εγκατάσταση CMake

### Semantic Kernel και Inference

Το Semantic Kernel είναι ένα πλαίσιο εφαρμογών που σας επιτρέπει να δημιουργείτε εφαρμογές συμβατές με το Azure OpenAI Service, μοντέλα OpenAI, αλλά και τοπικά μοντέλα. Η πρόσβαση σε τοπικές υπηρεσίες μέσω του Semantic Kernel διευκολύνει την ενσωμάτωση με τον αυτο-φιλοξενούμενο server μοντέλου Phi-3-mini.

### Κλήση Ποσοτικοποιημένων Μοντέλων με Ollama ή LlamaEdge

Πολλοί χρήστες προτιμούν να χρησιμοποιούν ποσοτικοποιημένα μοντέλα για να τρέχουν μοντέλα τοπικά. Οι [Ollama](https://ollama.com) και [LlamaEdge](https://llamaedge.com) επιτρέπουν στους χρήστες να καλούν διάφορα ποσοτικοποιημένα μοντέλα:

#### **Ollama**

Μπορείτε να τρέξετε `ollama run phi3` απευθείας ή να το ρυθμίσετε offline. Δημιουργήστε ένα Modelfile με τη διαδρομή προς το αρχείο `gguf` σας. Παράδειγμα κώδικα για την εκτέλεση του ποσοτικοποιημένου μοντέλου Phi-3-mini:

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

#### **LlamaEdge**

Αν θέλετε να χρησιμοποιήσετε `gguf` ταυτόχρονα σε cloud και edge συσκευές, το LlamaEdge είναι μια εξαιρετική επιλογή.

## **2. Μεταγλώττιση ONNX Runtime για iOS**

```bash

git clone https://github.com/microsoft/onnxruntime.git

cd onnxruntime

./build.sh --build_shared_lib --ios --skip_tests --parallel --build_dir ./build_ios --ios --apple_sysroot iphoneos --osx_arch arm64 --apple_deploy_target 17.5 --cmake_generator Xcode --config Release

cd ../

```

### **Σημείωση**

- **a.** Πριν τη μεταγλώττιση, βεβαιωθείτε ότι το Xcode είναι σωστά ρυθμισμένο και ορίστε το ως τον ενεργό φάκελο ανάπτυξης στο τερματικό:

    ```bash
    sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer
    ```

- **b.** Το ONNX Runtime πρέπει να μεταγλωττιστεί για διαφορετικές πλατφόρμες. Για iOS, μπορείτε να μεταγλωττίσετε για `arm64` ή `x86_64`.

- **c.** Συνιστάται να χρησιμοποιήσετε το πιο πρόσφατο iOS SDK για τη μεταγλώττιση. Ωστόσο, μπορείτε να χρησιμοποιήσετε και παλαιότερη έκδοση αν χρειάζεστε συμβατότητα με προηγούμενα SDK.

## **3. Μεταγλώττιση Generative AI με ONNX Runtime για iOS**

> **Note:** Επειδή το Generative AI με ONNX Runtime βρίσκεται σε προεπισκόπηση, να είστε προετοιμασμένοι για πιθανές αλλαγές.

```bash

git clone https://github.com/microsoft/onnxruntime-genai
 
cd onnxruntime-genai
 
mkdir ort
 
cd ort
 
mkdir include
 
mkdir lib
 
cd ../
 
cp ../onnxruntime/include/onnxruntime/core/session/onnxruntime_c_api.h ort/include
 
cp ../onnxruntime/build_ios/Release/Release-iphoneos/libonnxruntime*.dylib* ort/lib
 
export OPENCV_SKIP_XCODEBUILD_FORCE_TRYCOMPILE_DEBUG=1
 
python3 build.py --parallel --build_dir ./build_ios --ios --ios_sysroot iphoneos --ios_arch arm64 --ios_deployment_target 17.5 --cmake_generator Xcode --cmake_extra_defines CMAKE_XCODE_ATTRIBUTE_CODE_SIGNING_ALLOWED=NO

```

## **4. Δημιουργία εφαρμογής App στο Xcode**

Επέλεξα το Objective-C ως μέθοδο ανάπτυξης της εφαρμογής, επειδή η χρήση του Generative AI με το ONNX Runtime C++ API είναι πιο συμβατή με Objective-C. Φυσικά, μπορείτε επίσης να ολοκληρώσετε τις σχετικές κλήσεις μέσω Swift bridging.

![xcode](../../../../../translated_images/xcode.8147789e6c25e3e2.el.png)

## **5. Αντιγραφή του ποσοτικοποιημένου μοντέλου ONNX INT4 στο project της εφαρμογής**

Πρέπει να εισάγουμε το μοντέλο ποσοτικοποίησης INT4 σε μορφή ONNX, το οποίο πρέπει πρώτα να κατεβάσετε.

![hf](../../../../../translated_images/hf.6b8504fd88ee48dd.el.png)

Μετά το κατέβασμα, πρέπει να το προσθέσετε στον φάκελο Resources του project στο Xcode.

![model](../../../../../translated_images/model.3b879b14e0be877d.el.png)

## **6. Προσθήκη του C++ API στα ViewControllers**

> **Σημείωση:**

- **a.** Προσθέστε τα αντίστοιχα αρχεία κεφαλίδας C++ στο project.

  ![Header File](../../../../../translated_images/head.64cad021ce70a333.el.png)

- **b.** Συμπεριλάβετε τη δυναμική βιβλιοθήκη `onnxruntime-genai` στο Xcode.

  ![Library](../../../../../translated_images/lib.a4209b9f21ddf344.el.png)

- **c.** Χρησιμοποιήστε τον κώδικα δειγμάτων C για δοκιμές. Μπορείτε επίσης να προσθέσετε επιπλέον λειτουργίες όπως ChatUI για περισσότερη λειτουργικότητα.

- **d.** Επειδή χρειάζεται να χρησιμοποιήσετε C++ στο project σας, μετονομάστε το `ViewController.m` σε `ViewController.mm` για να ενεργοποιήσετε την υποστήριξη Objective-C++.

```objc

    NSString *llmPath = [[NSBundle mainBundle] resourcePath];
    char const *modelPath = llmPath.cString;

    auto model =  OgaModel::Create(modelPath);

    auto tokenizer = OgaTokenizer::Create(*model);

    const char* prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>Can you introduce yourself?<|end|><|assistant|>";

    auto sequences = OgaSequences::Create();
    tokenizer->Encode(prompt, *sequences);

    auto params = OgaGeneratorParams::Create(*model);
    params->SetSearchOption("max_length", 100);
    params->SetInputSequences(*sequences);

    auto output_sequences = model->Generate(*params);
    const auto output_sequence_length = output_sequences->SequenceCount(0);
    const auto* output_sequence_data = output_sequences->SequenceData(0);
    auto out_string = tokenizer->Decode(output_sequence_data, output_sequence_length);
    
    auto tmp = out_string;

```

## **7. Εκτέλεση της Εφαρμογής**

Μόλις ολοκληρωθεί η ρύθμιση, μπορείτε να τρέξετε την εφαρμογή για να δείτε τα αποτελέσματα της εκτέλεσης του μοντέλου Phi-3-mini.

![Running Result](../../../../../translated_images/result.326a947a6a2b9c51.el.jpg)

Για περισσότερα παραδείγματα κώδικα και λεπτομερείς οδηγίες, επισκεφθείτε το [Phi-3 Mini Samples repository](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios).

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.