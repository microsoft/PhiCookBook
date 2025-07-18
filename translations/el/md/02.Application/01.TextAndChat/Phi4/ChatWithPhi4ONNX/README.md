<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c98217bb3eff6c24e97b104b21632fd0",
  "translation_date": "2025-07-17T03:17:30+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md",
  "language_code": "el"
}
-->
# **Συνομιλία με το Phi-4-mini ONNX**

***ONNX*** είναι ένα ανοιχτό πρότυπο σχεδιασμένο για την αναπαράσταση μοντέλων μηχανικής μάθησης. Το ONNX ορίζει ένα κοινό σύνολο τελεστών - τα δομικά στοιχεία των μοντέλων μηχανικής μάθησης και βαθιάς μάθησης - καθώς και ένα κοινό μορφότυπο αρχείου που επιτρέπει στους προγραμματιστές AI να χρησιμοποιούν μοντέλα με διάφορα πλαίσια, εργαλεία, χρόνους εκτέλεσης και μεταγλωττιστές.

Ελπίζουμε να αναπτύξουμε γενετικά μοντέλα AI σε συσκευές άκρου και να τα χρησιμοποιήσουμε σε περιβάλλοντα με περιορισμένη υπολογιστική ισχύ ή εκτός σύνδεσης. Τώρα μπορούμε να πετύχουμε αυτόν τον στόχο μετατρέποντας το μοντέλο με κβαντισμένο τρόπο. Μπορούμε να μετατρέψουμε το κβαντισμένο μοντέλο σε μορφή GGUF ή ONNX.

Το Microsoft Olive μπορεί να σας βοηθήσει να μετατρέψετε το SLM σε κβαντισμένη μορφή ONNX. Η μέθοδος για την επίτευξη της μετατροπής μοντέλου είναι πολύ απλή

**Εγκατάσταση του Microsoft Olive SDK**


```bash

pip install olive-ai

pip install transformers

```

**Μετατροπή CPU ONNX Support**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Σημείωση*** αυτό το παράδειγμα χρησιμοποιεί CPU


### **Εκτέλεση του μοντέλου Phi-4-mini ONNX με ONNX Runtime GenAI**

- **Εγκατάσταση ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **Κώδικας Python**

*Αυτή είναι η έκδοση ONNX Runtime GenAI 0.5.2*

```python

import onnxruntime_genai as og
import numpy as np
import os


model_folder = "Your Phi-4-mini-onnx-cpu-int4 location"


model = og.Model(model_folder)


tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()


search_options = {}
search_options['max_length'] = 2048
search_options['past_present_share_buffer'] = False


chat_template = "<|user|>\n{input}</s>\n<|assistant|>"


text = """Can you introduce yourself"""


prompt = f'{chat_template.format(input=text)}'


input_tokens = tokenizer.encode(prompt)


params = og.GeneratorParams(model)


params.set_search_options(**search_options)
params.input_ids = input_tokens


generator = og.Generator(model, params)


while not generator.is_done():
      generator.compute_logits()
      generator.generate_next_token()

      new_token = generator.get_next_tokens()[0]
      print(tokenizer_stream.decode(new_token), end='', flush=True)

```


*Αυτή είναι η έκδοση ONNX Runtime GenAI 0.6.0*

```python

import onnxruntime_genai as og
import numpy as np
import os
import time
import psutil

model_folder = "Your Phi-4-mini-onnx model path"

model = og.Model(model_folder)

tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

search_options = {}
search_options['max_length'] = 1024
search_options['past_present_share_buffer'] = False

chat_template = "<|user|>{input}<|assistant|>"

text = """can you introduce yourself"""

prompt = f'{chat_template.format(input=text)}'

input_tokens = tokenizer.encode(prompt)

params = og.GeneratorParams(model)

params.set_search_options(**search_options)

generator = og.Generator(model, params)

generator.append_tokens(input_tokens)

while not generator.is_done():
      generator.generate_next_token()

      new_token = generator.get_next_tokens()[0]
      token_text = tokenizer.decode(new_token)
      # print(tokenizer_stream.decode(new_token), end='', flush=True)
      if token_count == 0:
        first_token_time = time.time()
        first_response_latency = first_token_time - start_time
        print(f"firstly token delpay: {first_response_latency:.4f} s")

      print(token_text, end='', flush=True)
      token_count += 1

```

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.