# **Fine-tuning Phi-3 cu Lora**

Fine-tuning modelului de limbaj Phi-3 Mini de la Microsoft folosind [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) pe un set de date personalizat pentru instrucțiuni de chat.

LORA va ajuta la îmbunătățirea înțelegerii conversaționale și generării răspunsurilor.

## Ghid pas cu pas pentru fine-tuning-ul Phi-3 Mini:

**Importuri și Configurare**

Instalarea loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Începe prin a importa bibliotecile necesare precum datasets, transformers, peft, trl și torch.  
Configurează logging-ul pentru a urmări procesul de antrenament.

Poți alege să adaptezi unele straturi înlocuindu-le cu echivalente implementate în loralib. Momentan suportăm doar nn.Linear, nn.Embedding și nn.Conv2d. De asemenea, suportăm MergedLinear pentru cazurile în care un singur nn.Linear reprezintă mai multe straturi, cum ar fi în unele implementări ale proiecției qkv din atenție (vezi Notițe suplimentare pentru detalii).

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

import loralib as lora

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

Înainte de a începe bucla de antrenament, marchează doar parametrii LoRA ca fiind antrenabili.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

La salvarea unui checkpoint, generează un state_dict care să conțină doar parametrii LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

La încărcarea unui checkpoint folosind load_state_dict, asigură-te că setezi strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Acum antrenamentul poate continua în mod obișnuit.

**Hiperparametri**

Definește două dicționare: training_config și peft_config. training_config include hiperparametrii pentru antrenament, cum ar fi rata de învățare, dimensiunea batch-ului și setările de logging.

peft_config specifică parametrii legați de LoRA, precum rank, dropout și tipul sarcinii.

**Încărcarea Modelului și Tokenizer-ului**

Specifică calea către modelul Phi-3 pre-antrenat (de exemplu, "microsoft/Phi-3-mini-4k-instruct"). Configurează setările modelului, inclusiv utilizarea cache-ului, tipul de date (bfloat16 pentru precizie mixtă) și implementarea atenției.

**Antrenament**

Fine-tunează modelul Phi-3 folosind setul de date personalizat pentru instrucțiuni de chat. Folosește setările LoRA din peft_config pentru o adaptare eficientă. Monitorizează progresul antrenamentului folosind strategia de logging specificată.  
Evaluare și Salvare: Evaluează modelul fine-tuned.  
Salvează checkpoint-uri în timpul antrenamentului pentru utilizare ulterioară.

**Exemple**  
- [Află mai multe cu acest notebook exemplu](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Exemplu de script Python pentru FineTuning](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [Exemplu de Fine Tuning pe Hugging Face Hub cu LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Exemplu Model Card Hugging Face - Fine Tuning cu LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [Exemplu de Fine Tuning pe Hugging Face Hub cu QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Declinare a responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.