<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b94610e2f6fe648e01fa23626f0dd03",
  "translation_date": "2025-07-17T08:00:11+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLX.md",
  "language_code": "el"
}
-->
# **Fine-tuning του Phi-3 με το Apple MLX Framework**

Μπορούμε να ολοκληρώσουμε το Fine-tuning σε συνδυασμό με το Lora μέσω της γραμμής εντολών του Apple MLX framework. (Αν θέλετε να μάθετε περισσότερα για τη λειτουργία του MLX Framework, παρακαλώ διαβάστε το [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md)


## **1. Προετοιμασία δεδομένων**

Από προεπιλογή, το MLX Framework απαιτεί το jsonl format για train, test και eval, και συνδυάζεται με το Lora για να ολοκληρώσει τις εργασίες fine-tuning.


### ***Note:***

1. μορφή δεδομένων jsonl ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Το παράδειγμά μας χρησιμοποιεί τα [δεδομένα του TruthfulQA](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), αλλά η ποσότητα των δεδομένων είναι σχετικά περιορισμένη, οπότε τα αποτελέσματα του fine-tuning δεν είναι απαραίτητα τα καλύτερα. Συνιστάται οι χρήστες να χρησιμοποιήσουν καλύτερα δεδομένα βασισμένα στα δικά τους σενάρια για να ολοκληρώσουν τη διαδικασία.

3. Η μορφή των δεδομένων είναι συνδυασμένη με το πρότυπο του Phi-3

Παρακαλώ κατεβάστε τα δεδομένα από αυτόν τον [σύνδεσμο](../../../../code/04.Finetuning/mlx), βεβαιωθείτε ότι περιλαμβάνονται όλα τα .jsonl στον φάκελο ***data***


## **2. Fine-tuning στο τερματικό σας**

Παρακαλώ εκτελέστε αυτή την εντολή στο τερματικό


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Note:***

1. Πρόκειται για LoRA fine-tuning, το MLX framework δεν έχει δημοσιεύσει QLoRA

2. Μπορείτε να ρυθμίσετε το config.yaml για να αλλάξετε ορισμένες παραμέτρους, όπως


```yaml


# The path to the local model directory or Hugging Face repo.
model: "microsoft/Phi-3-mini-4k-instruct"
# Whether or not to train (boolean)
train: true

# Directory with {train, valid, test}.jsonl files
data: "data"

# The PRNG seed
seed: 0

# Number of layers to fine-tune
lora_layers: 32

# Minibatch size.
batch_size: 1

# Iterations to train for.
iters: 1000

# Number of validation batches, -1 uses the entire validation set.
val_batches: 25

# Adam learning rate.
learning_rate: 1e-6

# Number of training steps between loss reporting.
steps_per_report: 10

# Number of training steps between validations.
steps_per_eval: 200

# Load path to resume training with the given adapter weights.
resume_adapter_file: null

# Save/load path for the trained adapter weights.
adapter_path: "adapters"

# Save the model every N iterations.
save_every: 1000

# Evaluate on the test set after training
test: false

# Number of test set batches, -1 uses the entire test set.
test_batches: 100

# Maximum sequence length.
max_seq_length: 2048

# Use gradient checkpointing to reduce memory use.
grad_checkpoint: true

# LoRA parameters can only be specified in a config file
lora_parameters:
  # The layer keys to apply LoRA to.
  # These will be applied for the last lora_layers
  keys: ["o_proj","qkv_proj"]
  rank: 64
  scale: 1
  dropout: 0.1


```

Παρακαλώ εκτελέστε αυτή την εντολή στο τερματικό


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Εκτέλεση Fine-tuning adapter για δοκιμή**

Μπορείτε να τρέξετε τον fine-tuning adapter στο τερματικό, όπως αυτό


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

και να τρέξετε το αρχικό μοντέλο για να συγκρίνετε τα αποτελέσματα


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Μπορείτε να δοκιμάσετε να συγκρίνετε τα αποτελέσματα του Fine-tuning με το αρχικό μοντέλο


## **4. Συγχώνευση adapters για δημιουργία νέων μοντέλων**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Εκτέλεση ποσοτικοποιημένων μοντέλων fine-tuning με χρήση ollama**

Πριν τη χρήση, παρακαλώ ρυθμίστε το περιβάλλον σας για llama.cpp


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Note:*** 

1. Τώρα υποστηρίζεται η μετατροπή ποσοτικοποίησης για fp32, fp16 και INT 8

2. Το συγχωνευμένο μοντέλο δεν περιλαμβάνει tokenizer.model, παρακαλώ κατεβάστε το από https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

ορίστε ένα [Ollma Model](https://ollama.com/)


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

εκτελέστε την εντολή στο τερματικό


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Συγχαρητήρια! Κατακτήσατε το fine-tuning με το MLX Framework

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που προσπαθούμε για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.