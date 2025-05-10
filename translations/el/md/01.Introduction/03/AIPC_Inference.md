<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e08ce816e23ad813244a09ca34ebb8ac",
  "translation_date": "2025-05-09T10:16:53+00:00",
  "source_file": "md/01.Introduction/03/AIPC_Inference.md",
  "language_code": "el"
}
-->
# **Inference Phi-3 σε AI PC**

Με την πρόοδο της γενετικής τεχνητής νοημοσύνης και τη βελτίωση των δυνατοτήτων υλικού στις edge συσκευές, όλο και περισσότερα μοντέλα γενετικής AI μπορούν πλέον να ενσωματωθούν στις συσκευές Bring Your Own Device (BYOD) των χρηστών. Τα AI PC ανήκουν σε αυτά τα μοντέλα. Από το 2024, η Intel, η AMD και η Qualcomm συνεργάζονται με κατασκευαστές PC για να παρουσιάσουν AI PC που διευκολύνουν την ανάπτυξη τοπικών μοντέλων γενετικής AI μέσω τροποποιήσεων υλικού. Σε αυτή τη συζήτηση, θα επικεντρωθούμε στα Intel AI PC και θα εξερευνήσουμε πώς να αναπτύξουμε το Phi-3 σε ένα Intel AI PC.

### Τι είναι το NPU

Ένα NPU (Neural Processing Unit) είναι ένας αφιερωμένος επεξεργαστής ή μονάδα επεξεργασίας σε ένα μεγαλύτερο SoC, σχεδιασμένος ειδικά για την επιτάχυνση λειτουργιών νευρωνικών δικτύων και εργασιών AI. Σε αντίθεση με τους γενικής χρήσης CPUs και GPUs, τα NPUs είναι βελτιστοποιημένα για παράλληλο υπολογισμό βασισμένο σε δεδομένα, καθιστώντας τα εξαιρετικά αποδοτικά στην επεξεργασία μεγάλου όγκου πολυμεσικών δεδομένων όπως βίντεο και εικόνες, καθώς και στην επεξεργασία δεδομένων για νευρωνικά δίκτυα. Είναι ιδιαίτερα ικανά στην αντιμετώπιση εργασιών σχετικών με AI, όπως αναγνώριση φωνής, θόλωση φόντου σε βιντεοκλήσεις και διαδικασίες επεξεργασίας φωτογραφιών ή βίντεο όπως ανίχνευση αντικειμένων.

## NPU vs GPU

Ενώ πολλές εργασίες AI και μηχανικής μάθησης τρέχουν σε GPUs, υπάρχει μια σημαντική διαφορά μεταξύ GPUs και NPUs.  
Οι GPUs είναι γνωστές για τις δυνατότητες παράλληλου υπολογισμού τους, αλλά δεν είναι όλες οι GPUs το ίδιο αποδοτικές πέρα από την επεξεργασία γραφικών. Τα NPUs, από την άλλη, έχουν σχεδιαστεί ειδικά για πολύπλοκους υπολογισμούς που εμπλέκονται στις λειτουργίες νευρωνικών δικτύων, καθιστώντας τα ιδιαίτερα αποτελεσματικά για εργασίες AI.

Συνοψίζοντας, τα NPUs είναι οι «μαθηματικοί» που επιταχύνουν τους AI υπολογισμούς και παίζουν βασικό ρόλο στην αναδυόμενη εποχή των AI PC!

***Αυτό το παράδειγμα βασίζεται στον πιο πρόσφατο Intel Core Ultra Processor της Intel***

## **1. Χρήση NPU για εκτέλεση του μοντέλου Phi-3**

Η συσκευή Intel® NPU είναι ένας επιταχυντής AI inference ενσωματωμένος σε Intel client CPUs, ξεκινώντας από τη γενιά Intel® Core™ Ultra (παλαιότερα γνωστή ως Meteor Lake). Επιτρέπει την ενεργειακά αποδοτική εκτέλεση εργασιών τεχνητών νευρωνικών δικτύων.

![Latency](../../../../../translated_images/aipcphitokenlatency.446d244d43a98a99f001e6eb55b421ab7ebc0b5d8f93fad8458da46cf263bfad.el.png)

![Latency770](../../../../../translated_images/aipcphitokenlatency770.862269853961e495131e9465fdb06c2c7b94395b83729dc498cfc077e02caade.el.png)

**Βιβλιοθήκη Επιτάχυνσης Intel NPU**

Η βιβλιοθήκη Intel NPU Acceleration Library [https://github.com/intel/intel-npu-acceleration-library](https://github.com/intel/intel-npu-acceleration-library) είναι μια Python βιβλιοθήκη σχεδιασμένη να αυξήσει την αποδοτικότητα των εφαρμογών σας αξιοποιώντας τη δύναμη του Intel Neural Processing Unit (NPU) για την εκτέλεση υψηλής ταχύτητας υπολογισμών σε συμβατό υλικό.

Παράδειγμα Phi-3-mini σε AI PC με επεξεργαστές Intel® Core™ Ultra.

![DemoPhiIntelAIPC](../../../../../imgs/01/03/AIPC/aipcphi3-mini.gif)

Εγκατάσταση της Python βιβλιοθήκης με pip

```bash

   pip install intel-npu-acceleration-library

```

***Note*** Το έργο είναι ακόμα υπό ανάπτυξη, αλλά το αναφορικό μοντέλο είναι ήδη πολύ ολοκληρωμένο.

### **Εκτέλεση Phi-3 με τη βιβλιοθήκη Intel NPU Acceleration**

Χρησιμοποιώντας την επιτάχυνση Intel NPU, αυτή η βιβλιοθήκη δεν επηρεάζει την παραδοσιακή διαδικασία κωδικοποίησης. Απλά χρειάζεται να χρησιμοποιήσετε αυτή τη βιβλιοθήκη για να ποσοτικοποιήσετε το αρχικό μοντέλο Phi-3, όπως FP16, INT8, INT4, όπως

```python
from transformers import AutoTokenizer, pipeline,TextStreamer
from intel_npu_acceleration_library import NPUModelForCausalLM, int4
from intel_npu_acceleration_library.compiler import CompilerConfig
import warnings

model_id = "microsoft/Phi-3-mini-4k-instruct"

compiler_conf = CompilerConfig(dtype=int4)
model = NPUModelForCausalLM.from_pretrained(
    model_id, use_cache=True, config=compiler_conf, attn_implementation="sdpa"
).eval()

tokenizer = AutoTokenizer.from_pretrained(model_id)

text_streamer = TextStreamer(tokenizer, skip_prompt=True)
```

Μετά την επιτυχή ποσοτικοποίηση, συνεχίστε την εκτέλεση καλώντας το NPU για να τρέξει το μοντέλο Phi-3.

```python
generation_args = {
   "max_new_tokens": 1024,
   "return_full_text": False,
   "temperature": 0.3,
   "do_sample": False,
   "streamer": text_streamer,
}

pipe = pipeline(
   "text-generation",
   model=model,
   tokenizer=tokenizer,
)

query = "<|system|>You are a helpful AI assistant.<|end|><|user|>Can you introduce yourself?<|end|><|assistant|>"

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    pipe(query, **generation_args)
```

Κατά την εκτέλεση του κώδικα, μπορούμε να παρακολουθήσουμε την κατάσταση λειτουργίας του NPU μέσω του Task Manager

![NPU](../../../../../translated_images/aipc_NPU.f047860f84f5bb5b183756f23b4b8506485e862ea34c6a53c58988707c23bc80.el.png)

***Samples*** : [AIPC_NPU_DEMO.ipynb](../../../../../code/03.Inference/AIPC/AIPC_NPU_DEMO.ipynb)

## **2. Χρήση DirectML + ONNX Runtime για εκτέλεση του μοντέλου Phi-3**

### **Τι είναι το DirectML**

Το [DirectML](https://github.com/microsoft/DirectML) είναι μια υψηλής απόδοσης, επιταχυνόμενη από υλικό βιβλιοθήκη DirectX 12 για μηχανική μάθηση. Το DirectML παρέχει επιτάχυνση GPU για κοινές εργασίες μηχανικής μάθησης σε ευρύ φάσμα υποστηριζόμενου υλικού και οδηγών, συμπεριλαμβανομένων όλων των GPUs που υποστηρίζουν DirectX 12 από κατασκευαστές όπως AMD, Intel, NVIDIA και Qualcomm.

Όταν χρησιμοποιείται ανεξάρτητα, το API του DirectML είναι μια χαμηλού επιπέδου βιβλιοθήκη DirectX 12 και είναι κατάλληλο για εφαρμογές υψηλής απόδοσης και χαμηλής καθυστέρησης όπως frameworks, παιχνίδια και άλλες εφαρμογές σε πραγματικό χρόνο. Η απρόσκοπτη διαλειτουργικότητα του DirectML με το Direct3D 12, καθώς και το χαμηλό overhead και η συμμόρφωση σε όλο το υλικό, καθιστούν το DirectML ιδανικό για επιτάχυνση μηχανικής μάθησης όταν απαιτείται υψηλή απόδοση και η αξιοπιστία και προβλεψιμότητα των αποτελεσμάτων σε διαφορετικό υλικό είναι κρίσιμες.

***Note*** : Το πιο πρόσφατο DirectML υποστηρίζει ήδη NPU (https://devblogs.microsoft.com/directx/introducing-neural-processor-unit-npu-support-in-directml-developer-preview/)

### DirectML και CUDA σε σχέση με τις δυνατότητες και την απόδοσή τους:

**DirectML** είναι μια βιβλιοθήκη μηχανικής μάθησης που ανέπτυξε η Microsoft. Έχει σχεδιαστεί για να επιταχύνει εργασίες μηχανικής μάθησης σε συσκευές Windows, όπως desktops, laptops και edge συσκευές.  
- Βασισμένο σε DX12: Το DirectML βασίζεται στο DirectX 12 (DX12), που προσφέρει ευρεία υποστήριξη υλικού σε GPUs, συμπεριλαμβανομένων NVIDIA και AMD.  
- Ευρύτερη Υποστήριξη: Αξιοποιώντας το DX12, το DirectML μπορεί να λειτουργήσει με οποιαδήποτε GPU που υποστηρίζει DX12, ακόμα και ενσωματωμένες GPUs.  
- Επεξεργασία Εικόνας: Το DirectML επεξεργάζεται εικόνες και άλλα δεδομένα χρησιμοποιώντας νευρωνικά δίκτυα, καθιστώντας το κατάλληλο για εργασίες όπως αναγνώριση εικόνας, ανίχνευση αντικειμένων κ.ά.  
- Εύκολη Ρύθμιση: Η ρύθμιση του DirectML είναι απλή και δεν απαιτεί συγκεκριμένα SDKs ή βιβλιοθήκες από κατασκευαστές GPU.  
- Απόδοση: Σε ορισμένες περιπτώσεις, το DirectML αποδίδει καλά και μπορεί να είναι πιο γρήγορο από το CUDA, ειδικά σε συγκεκριμένα φορτία εργασίας.  
- Περιορισμοί: Ωστόσο, υπάρχουν περιπτώσεις όπου το DirectML μπορεί να είναι πιο αργό, ιδιαίτερα για μεγάλου μεγέθους batch float16.

**CUDA** είναι η παράλληλη πλατφόρμα υπολογισμών και το προγραμματιστικό μοντέλο της NVIDIA. Επιτρέπει στους προγραμματιστές να αξιοποιήσουν τη δύναμη των GPUs της NVIDIA για γενικούς υπολογισμούς, συμπεριλαμβανομένης της μηχανικής μάθησης και επιστημονικών προσομοιώσεων.  
- Ειδικό για NVIDIA: Το CUDA είναι στενά ενσωματωμένο με τις GPUs της NVIDIA και έχει σχεδιαστεί ειδικά γι’ αυτές.  
- Υψηλή Βελτιστοποίηση: Παρέχει εξαιρετική απόδοση για εργασίες με επιτάχυνση GPU, ιδιαίτερα με GPUs της NVIDIA.  
- Ευρεία Χρήση: Πολλά frameworks και βιβλιοθήκες μηχανικής μάθησης (όπως TensorFlow και PyTorch) υποστηρίζουν CUDA.  
- Παραμετροποίηση: Οι προγραμματιστές μπορούν να ρυθμίσουν λεπτομερώς το CUDA για συγκεκριμένες εργασίες, οδηγώντας σε βέλτιστη απόδοση.  
- Περιορισμοί: Ωστόσο, η εξάρτηση του CUDA από το υλικό NVIDIA μπορεί να περιορίσει τη συμβατότητα με άλλες GPUs.

### Επιλογή μεταξύ DirectML και CUDA

Η επιλογή μεταξύ DirectML και CUDA εξαρτάται από τη συγκεκριμένη χρήση, τη διαθεσιμότητα υλικού και τις προτιμήσεις σας.  
Αν ψάχνετε για ευρύτερη συμβατότητα και εύκολη εγκατάσταση, το DirectML μπορεί να είναι καλή επιλογή. Αν όμως διαθέτετε NVIDIA GPUs και χρειάζεστε υψηλά βελτιστοποιημένη απόδοση, το CUDA παραμένει ισχυρή επιλογή. Συνολικά, και οι δύο έχουν τα πλεονεκτήματα και τα μειονεκτήματά τους, οπότε λάβετε υπόψη τις ανάγκες και το διαθέσιμο υλικό πριν αποφασίσετε.

### **Γενετική AI με ONNX Runtime**

Στην εποχή της AI, η φορητότητα των μοντέλων AI είναι πολύ σημαντική. Το ONNX Runtime επιτρέπει εύκολη ανάπτυξη εκπαιδευμένων μοντέλων σε διαφορετικές συσκευές. Οι προγραμματιστές δεν χρειάζεται να ανησυχούν για το πλαίσιο inference και χρησιμοποιούν ένα ενιαίο API για την ολοκλήρωση της inference διαδικασίας. Στην εποχή της γενετικής AI, το ONNX Runtime έχει επίσης πραγματοποιήσει βελτιστοποίηση κώδικα (https://onnxruntime.ai/docs/genai/). Μέσω του βελτιστοποιημένου ONNX Runtime, το ποσοτικοποιημένο γενετικό AI μοντέλο μπορεί να εκτελεστεί σε διάφορους τερματικούς σταθμούς. Με το Generative AI με ONNX Runtime, μπορείτε να κάνετε inference μοντέλου AI μέσω Python, C#, C / C++. Φυσικά, η ανάπτυξη σε iPhone μπορεί να εκμεταλλευτεί το API Generative AI με ONNX Runtime σε C++.

[Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx)

***Συγκρότηση της βιβλιοθήκης generative AI με ONNX Runtime***

```bash

winget install --id=Kitware.CMake  -e

git clone https://github.com/microsoft/onnxruntime.git

cd .\onnxruntime\

./build.bat --build_shared_lib --skip_tests --parallel --use_dml --config Release

cd ../

git clone https://github.com/microsoft/onnxruntime-genai.git

cd .\onnxruntime-genai\

mkdir ort

cd ort

mkdir include

mkdir lib

copy ..\onnxruntime\include\onnxruntime\core\providers\dml\dml_provider_factory.h ort\include

copy ..\onnxruntime\include\onnxruntime\core\session\onnxruntime_c_api.h ort\include

copy ..\onnxruntime\build\Windows\Release\Release\*.dll ort\lib

copy ..\onnxruntime\build\Windows\Release\Release\onnxruntime.lib ort\lib

python build.py --use_dml


```

**Εγκατάσταση βιβλιοθήκης**

```bash

pip install .\onnxruntime_genai_directml-0.3.0.dev0-cp310-cp310-win_amd64.whl

```

Αυτό είναι το αποτέλεσμα εκτέλεσης

![DML](../../../../../translated_images/aipc_DML.dd810ee1f3882323c131b39065ed0cf41bbe0aaa8d346a0d6d290c20f5c0bf75.el.png)

***Samples*** : [AIPC_DirectML_DEMO.ipynb](../../../../../code/03.Inference/AIPC/AIPC_DirectML_DEMO.ipynb)

## **3. Χρήση Intel OpenVino για εκτέλεση του μοντέλου Phi-3**

### **Τι είναι το OpenVINO**

Το [OpenVINO](https://github.com/openvinotoolkit/openvino) είναι ένα ανοιχτού κώδικα εργαλείο για τη βελτιστοποίηση και ανάπτυξη μοντέλων βαθιάς μάθησης. Παρέχει αυξημένη απόδοση για μοντέλα όρασης, ήχου και γλώσσας από δημοφιλή frameworks όπως TensorFlow, PyTorch και άλλα. Ξεκινήστε με το OpenVINO. Το OpenVINO μπορεί επίσης να χρησιμοποιηθεί σε συνδυασμό με CPU και GPU για να τρέξει το μοντέλο Phi3.

***Note***: Προς το παρόν, το OpenVINO δεν υποστηρίζει NPU.

### **Εγκατάσταση της βιβλιοθήκης OpenVINO**

```bash

 pip install git+https://github.com/huggingface/optimum-intel.git

 pip install git+https://github.com/openvinotoolkit/nncf.git

 pip install openvino-nightly

```

### **Εκτέλεση Phi-3 με OpenVINO**

Όπως και με το NPU, το OpenVINO ολοκληρώνει την κλήση των γενετικών AI μοντέλων τρέχοντας ποσοτικοποιημένα μοντέλα. Πρέπει πρώτα να ποσοτικοποιήσουμε το μοντέλο Phi-3 και να ολοκληρώσουμε την ποσοτικοποίηση μέσω της γραμμής εντολών με optimum-cli.

**INT4**

```bash

optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code ./openvinomodel/phi3/int4

```

**FP16**

```bash

optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format fp16 --trust-remote-code ./openvinomodel/phi3/fp16

```

Η μορφή μετά τη μετατροπή, όπως αυτή

![openvino_convert](../../../../../translated_images/aipc_OpenVINO_convert.bd70cf3d87e65a923d2d663f559a03d86227ab71071802355a6cfeaf80eb7042.el.png)

Φορτώνουμε διαδρομές μοντέλων (model_dir), σχετικές ρυθμίσεις (ov_config = {"PERFORMANCE_HINT": "LATENCY", "NUM_STREAMS": "1", "CACHE_DIR": ""}) και επιταχυνόμενες συσκευές υλικού (GPU.0) μέσω OVModelForCausalLM

```python

ov_model = OVModelForCausalLM.from_pretrained(
     model_dir,
     device='GPU.0',
     ov_config=ov_config,
     config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
     trust_remote_code=True,
)

```

Κατά την εκτέλεση του κώδικα, μπορούμε να παρακολουθήσουμε την κατάσταση λειτουργίας της GPU μέσω του Task Manager

![openvino_gpu](../../../../../translated_images/aipc_OpenVINO_GPU.142b31f25c5ffcf8802077629d11fbae275e53aeeb0752e0cdccf826feca6875.el.png)

***Samples*** : [AIPC_OpenVino_Demo.ipynb](../../../../../code/03.Inference/AIPC/AIPC_OpenVino_Demo.ipynb)

### ***Note*** : Οι τρεις παραπάνω μέθοδοι έχουν τα δικά τους πλεονεκτήματα, αλλά συνιστάται η χρήση επιτάχυνσης NPU για το inference σε AI PC.

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που προσπαθούμε για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται η επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.