<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-05-09T04:42:34+00:00",
  "source_file": "code/04.Finetuning/olive-lab/readme.md",
  "language_code": "ro"
}
-->
# Lab. Optimizarea modelelor AI pentru inferență pe dispozitiv

## Introducere

> [!IMPORTANT]
> Acest laborator necesită un **GPU Nvidia A10 sau A100** cu driverele aferente și toolkit-ul CUDA (versiunea 12+) instalate.

> [!NOTE]
> Acesta este un laborator de **35 de minute** care îți oferă o introducere practică în conceptele de bază pentru optimizarea modelelor pentru inferență pe dispozitiv folosind OLIVE.

## Obiective de învățare

La finalul acestui laborator vei putea să folosești OLIVE pentru a:

- Quantiza un model AI folosind metoda de cuantizare AWQ.
- Ajusta fin un model AI pentru o sarcină specifică.
- Genera adaptoare LoRA (model ajustat fin) pentru inferență eficientă pe dispozitiv folosind ONNX Runtime.

### Ce este Olive

Olive (*O*NNX *live*) este un toolkit de optimizare a modelelor cu CLI asociat care îți permite să livrezi modele pentru ONNX runtime +++https://onnxruntime.ai+++ cu calitate și performanță.

![Olive Flow](../../../../../translated_images/olive-flow.e4682fa65f77777f49e884482fa8dd83eadcb90904fcb41a54093af85c330060.ro.png)

Input-ul pentru Olive este de obicei un model PyTorch sau Hugging Face, iar output-ul este un model ONNX optimizat care este executat pe un dispozitiv (ținta de implementare) ce rulează ONNX runtime. Olive va optimiza modelul pentru acceleratorul AI al țintei de implementare (NPU, GPU, CPU) furnizat de un producător hardware precum Qualcomm, AMD, Nvidia sau Intel.

Olive execută un *workflow*, care este o succesiune ordonată de sarcini individuale de optimizare a modelului numite *passes* - exemple de passes includ: compresia modelului, capturarea grafului, cuantizarea, optimizarea grafului. Fiecare pass are un set de parametri care pot fi ajustați pentru a obține cele mai bune metrici, cum ar fi acuratețea și latența, evaluate de evaluatorul respectiv. Olive folosește o strategie de căutare care utilizează un algoritm pentru a regla automat fiecare pass pe rând sau un set de passes împreună.

#### Beneficiile Olive

- **Reducerea frustrării și a timpului** petrecut în experimentări manuale de tip trial-and-error cu diferite tehnici pentru optimizarea grafului, compresie și cuantizare. Definește-ți constrângerile de calitate și performanță și lasă Olive să găsească automat cel mai bun model pentru tine.
- **Peste 40 de componente integrate de optimizare a modelelor** care acoperă tehnici de ultimă oră în cuantizare, compresie, optimizarea grafului și ajustare fină.
- **CLI ușor de folosit** pentru sarcini comune de optimizare a modelelor. De exemplu, olive quantize, olive auto-opt, olive finetune.
- Ambalare și implementare a modelelor integrate.
- Suportă generarea de modele pentru **Multi LoRA serving**.
- Construiește fluxuri de lucru folosind YAML/JSON pentru a orchestra sarcinile de optimizare și implementare a modelelor.
- Integrare cu **Hugging Face** și **Azure AI**.
- Mecanism integrat de **caching** pentru a **reduce costurile**.

## Instrucțiuni laborator
> [!NOTE]
> Asigură-te că ai provisionat Azure AI Hub și proiectul tău și ai configurat compute-ul A100 conform laboratorului 1.

### Pasul 0: Conectează-te la Azure AI Compute

Te vei conecta la compute-ul Azure AI folosind funcția remote din **VS Code.**

1. Deschide aplicația desktop **VS Code**:
2. Deschide **command palette** folosind **Shift+Ctrl+P**
3. În command palette caută **AzureML - remote: Connect to compute instance in New Window**.
4. Urmează instrucțiunile de pe ecran pentru a te conecta la Compute. Va trebui să selectezi Azure Subscription, Resource Group, Proiectul și numele Compute-ului configurat în laboratorul 1.
5. Odată conectat la nodul Azure ML Compute, acesta va fi afișat în **colțul din stânga jos al Visual Code** `><Azure ML: Compute Name`

### Pasul 1: Clonează acest repo

În VS Code, poți deschide un terminal nou cu **Ctrl+J** și clona acest repo:

În terminal ar trebui să vezi promptul

```
azureuser@computername:~/cloudfiles/code$ 
```
Clonează soluția

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### Pasul 2: Deschide folderul în VS Code

Pentru a deschide VS Code în folderul relevant execută următoarea comandă în terminal, care va deschide o fereastră nouă:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

Alternativ, poți deschide folderul selectând **File** > **Open Folder**.

### Pasul 3: Dependențe

Deschide un terminal în VS Code pe instanța ta Azure AI Compute (sfat: **Ctrl+J**) și execută următoarele comenzi pentru a instala dependențele:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> Instalarea tuturor dependențelor va dura aproximativ 5 minute.

În acest laborator vei descărca și încărca modele în catalogul de modele Azure AI. Pentru a accesa catalogul de modele, trebuie să te autentifici în Azure folosind:

```bash
az login
```

> [!NOTE]
> La autentificare ți se va cere să selectezi abonamentul. Asigură-te că selectezi abonamentul furnizat pentru acest laborator.

### Pasul 4: Execută comenzile Olive

Deschide un terminal în VS Code pe instanța ta Azure AI Compute (sfat: **Ctrl+J**) și asigură-te că mediul `olive-ai` conda este activat:

```bash
conda activate olive-ai
```

Apoi, execută următoarele comenzi Olive în linia de comandă.

1. **Inspectează datele:** În acest exemplu vei ajusta fin modelul Phi-3.5-Mini pentru a fi specializat în răspunsuri la întrebări legate de călătorii. Codul de mai jos afișează primele înregistrări din setul de date, care sunt în format JSON lines:
   
    ```bash
    head data/data_sample_travel.jsonl
    ```
2. **Quantizează modelul:** Înainte de antrenarea modelului, îl cuantizezi cu comanda următoare care folosește o tehnică numită Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++. AWQ cuantizează greutățile modelului ținând cont de activările produse în timpul inferenței. Aceasta înseamnă că procesul de cuantizare ia în calcul distribuția reală a datelor în activări, ceea ce duce la o păstrare mai bună a acurateței modelului comparativ cu metodele tradiționale de cuantizare a greutăților.
    
    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```
    
    Procesul de cuantizare AWQ durează aproximativ **8 minute** și va **reduce dimensiunea modelului de la ~7.5GB la ~2.5GB**.
   
   În acest laborator îți arătăm cum să imporți modele din Hugging Face (de exemplu: `microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune` ajustează fin modelul cuantizat. Cuantizarea modelului *înainte* de ajustarea fină, în loc de după, oferă o acuratețe mai bună deoarece procesul de ajustare fină recuperează o parte din pierderea cauzată de cuantizare.
    
    ```bash
    olive finetune \
        --method lora \
        --model_name_or_path models/phi/awq \
        --data_files "data/data_sample_travel.jsonl" \
        --data_name "json" \
        --text_template "<|user|>\n{prompt}<|end|>\n<|assistant|>\n{response}<|end|>" \
        --max_steps 100 \
        --output_path ./models/phi/ft \
        --log_level 1
    ```
    
    Ajustarea fină (cu 100 de pași) durează aproximativ **6 minute**.

3. **Optimizează:** După ce modelul este antrenat, îl optimizezi folosind argumentele `auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider` ale Olive - însă pentru acest laborator vom folosi CPU.

    ```bash
    olive auto-opt \
       --model_name_or_path models/phi/ft/model \
       --adapter_path models/phi/ft/adapter \
       --device cpu \
       --provider CPUExecutionProvider \
       --use_ort_genai \
       --output_path models/phi/onnx-ao \
       --log_level 1
    ```
    
    Optimizarea durează aproximativ **5 minute**.

### Pasul 5: Test rapid de inferență al modelului

Pentru a testa inferența modelului, creează un fișier Python în folderul tău numit **app.py** și copiază următorul cod:

```python
import onnxruntime_genai as og
import numpy as np

print("loading model and adapters...", end="", flush=True)
model = og.Model("models/phi/onnx-ao/model")
adapters = og.Adapters(model)
adapters.load("models/phi/onnx-ao/model/adapter_weights.onnx_adapter", "travel")
print("DONE!")

tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

params = og.GeneratorParams(model)
params.set_search_options(max_length=100, past_present_share_buffer=False)
user_input = "what is the best thing to see in chicago"
params.input_ids = tokenizer.encode(f"<|user|>\n{user_input}<|end|>\n<|assistant|>\n")

generator = og.Generator(model, params)

generator.set_active_adapter(adapters, "travel")

print(f"{user_input}")

while not generator.is_done():
    generator.compute_logits()
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    print(tokenizer_stream.decode(new_token), end='', flush=True)

print("\n")
```

Execută codul folosind:

```bash
python app.py
```

### Pasul 6: Încarcă modelul în Azure AI

Încărcarea modelului în depozitul de modele Azure AI face modelul partajabil cu ceilalți membri ai echipei tale de dezvoltare și gestionează controlul versiunilor modelului. Pentru a încărca modelul, rulează următoarea comandă:

> [!NOTE]
> Actualizează valorile `{}` pentru `resourceGroup` și numele proiectului Azure AI, apoi rulează comanda

```
az ml workspace show
```

Sau accesează +++ai.azure.com+++ și selectează **management center** **project** **overview**

Actualizează valorile `{}` cu numele grupului tău de resurse și numele proiectului Azure AI.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```

Poți apoi să vezi modelul încărcat și să îl implementezi la https://ml.azure.com/model/list

**Declinare a responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să țineți cont că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea în urma utilizării acestei traduceri.