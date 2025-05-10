<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-05-09T22:41:40+00:00",
  "source_file": "md/03.FineTuning/olive-lab/readme.md",
  "language_code": "sr"
}
-->
# Lab. Optimizacija AI modela za inferencu na uređaju

## Uvod

> [!IMPORTANT]
> Ovaj laboratorijski zadatak zahteva **Nvidia A10 ili A100 GPU** sa pripadajućim drajverima i instaliranim CUDA alatom (verzija 12+).

> [!NOTE]
> Ovo je **35-minutni** laboratorijski zadatak koji će vam pružiti praktičan uvod u osnovne koncepte optimizacije modela za inferencu na uređaju koristeći OLIVE.

## Ciljevi učenja

Na kraju ovog laboratorijskog zadatka bićete u stanju da koristite OLIVE za:

- Kvantizaciju AI modela koristeći AWQ metodu kvantizacije.
- Fino podešavanje AI modela za specifičan zadatak.
- Generisanje LoRA adaptera (fino podešen model) za efikasnu inferencu na uređaju koristeći ONNX Runtime.

### Šta je Olive

Olive (*O*NNX *live*) je alat za optimizaciju modela sa pripadajućim CLI koji vam omogućava da isporučite modele za ONNX runtime +++https://onnxruntime.ai+++ sa kvalitetom i performansama.

![Olive Flow](../../../../../translated_images/olive-flow.9e6a284c256068568eb569a242b22dd2e7ec6e73f292d98272398739537ef513.sr.png)

Ulaz u Olive je obično PyTorch ili Hugging Face model, a izlaz je optimizovani ONNX model koji se izvršava na uređaju (ciljni uređaj za deployment) koji koristi ONNX runtime. Olive optimizuje model za AI akcelerator ciljnog uređaja (NPU, GPU, CPU) koji obezbeđuje proizvođač hardvera kao što su Qualcomm, AMD, Nvidia ili Intel.

Olive izvršava *workflow*, što je uređeni niz pojedinačnih zadataka optimizacije modela nazvanih *passes* - primeri takvih koraka su: kompresija modela, hvatanje grafa, kvantizacija, optimizacija grafa. Svaki korak ima skup parametara koje je moguće podesiti da bi se postigli najbolji rezultati, na primer preciznost i latencija, koji se ocenjuju pomoću odgovarajućeg evaluatora. Olive koristi strategiju pretraživanja koja primenjuje algoritam pretraživanja za automatsko podešavanje svakog koraka pojedinačno ili grupe koraka zajedno.

#### Prednosti Olive

- **Smanjuje frustraciju i vreme** povezano sa manuelnim eksperimentisanjem metodama optimizacije grafa, kompresije i kvantizacije. Definišite svoje zahteve za kvalitet i performanse i dozvolite Olive-u da automatski pronađe najbolji model za vas.
- **Više od 40 ugrađenih komponenti za optimizaciju modela** koje pokrivaju najsavremenije tehnike kvantizacije, kompresije, optimizacije grafa i fino podešavanje.
- **Jednostavan CLI** za uobičajene zadatke optimizacije modela. Na primer, olive quantize, olive auto-opt, olive finetune.
- Ugrađeno pakovanje i deployment modela.
- Podrška za generisanje modela za **Multi LoRA servisiranje**.
- Kreiranje workflow-a koristeći YAML/JSON za orkestraciju zadataka optimizacije i deploymenta modela.
- Integracija sa **Hugging Face** i **Azure AI**.
- Ugrađeni **mehanizam keširanja** za **uštede troškova**.

## Uputstva za laboratoriju

> [!NOTE]
> Proverite da li ste konfigurisali vaš Azure AI Hub i projekat i podesili A100 računar kao što je opisano u Lab 1.

### Korak 0: Povezivanje sa Azure AI računarom

Povezaćete se sa Azure AI računarom koristeći udaljenu funkciju u **VS Code-u**.

1. Otvorite vašu **VS Code** desktop aplikaciju:
1. Otvorite **command palette** pritiskom na **Shift+Ctrl+P**
1. U command palette-u potražite **AzureML - remote: Connect to compute instance in New Window**.
1. Pratite uputstva na ekranu da se povežete sa računarom. Ovo uključuje izbor vaše Azure pretplate, Resource Group, projekta i imena računara koje ste podesili u Lab 1.
1. Kada ste povezani sa vašim Azure ML Compute nodom, to će biti prikazano u **donjem levom uglu Visual Code-a** `><Azure ML: Compute Name`

### Korak 1: Klonirajte ovaj repozitorijum

U VS Code-u možete otvoriti novi terminal pritiskom na **Ctrl+J** i klonirati ovaj repozitorijum:

U terminalu bi trebalo da vidite prompt

```
azureuser@computername:~/cloudfiles/code$ 
```
Klonirajte rešenje

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### Korak 2: Otvorite folder u VS Code-u

Da biste otvorili VS Code u odgovarajućem folderu, izvršite sledeću komandu u terminalu, što će otvoriti novi prozor:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

Alternativno, možete otvoriti folder izborom **File** > **Open Folder**.

### Korak 3: Završni uslovi (Dependencies)

Otvorite terminal u VS Code-u na vašem Azure AI Compute Instance-u (prečica: **Ctrl+J**) i izvršite sledeće komande za instalaciju zavisnosti:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> Instalacija svih zavisnosti će trajati oko 5 minuta.

U ovom laboratorijskom zadatku ćete preuzimati i postavljati modele u Azure AI katalog modela. Da biste pristupili katalogu modela, potrebno je da se prijavite na Azure koristeći:

```bash
az login
```

> [!NOTE]
> Prilikom prijave bićete upitani da izaberete vašu pretplatu. Proverite da ste izabrali pretplatu koja je dodeljena za ovaj laboratorijski zadatak.

### Korak 4: Izvršavanje Olive komandi

Otvorite terminal u VS Code-u na vašem Azure AI Compute Instance-u (prečica: **Ctrl+J**) i proverite da li je `olive-ai` conda okruženje aktivirano:

```bash
conda activate olive-ai
```

Zatim izvršite sledeće Olive komande u komandnoj liniji.

1. **Pregled podataka:** U ovom primeru ćete fino podesiti Phi-3.5-Mini model da bude specijalizovan za odgovaranje na pitanja vezana za putovanja. Kod ispod prikazuje prvih nekoliko zapisa iz dataseta, koji su u JSON lines formatu:

    ```bash
    head data/data_sample_travel.jsonl
    ```

1. **Kvantizujte model:** Pre treniranja modela, prvo ga kvantizujete sledećom komandom koja koristi tehniku nazvanu Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++. AWQ kvantizuje težine modela uzimajući u obzir aktivacije koje se proizvode tokom inferencije. To znači da proces kvantizacije uzima u obzir stvarnu distribuciju podataka u aktivacijama, što vodi ka boljem očuvanju preciznosti modela u poređenju sa tradicionalnim metodama kvantizacije težina.

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```

    Završetak AWQ kvantizacije traje oko **8 minuta**, što će **smanjiti veličinu modela sa oko 7.5GB na oko 2.5GB**.

    U ovom laboratorijskom zadatku pokazujemo kako da unosite modele iz Hugging Face (na primer: `microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune` komanda fino podešava kvantizovani model. Kvantizacija modela *pre* fino podešavanja, umesto posle, daje bolju preciznost jer proces fino podešavanja kompenzuje deo gubitka usled kvantizacije.

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

    Fino podešavanje traje oko **6 minuta** (sa 100 koraka).

1. **Optimizacija:** Nakon treniranja modela, sada optimizujete model koristeći Olive komandu `auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider` - ali za potrebe ovog laboratorijskog zadatka koristićemo CPU.

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

    Optimizacija traje oko **5 minuta**.

### Korak 5: Brzi test inferencije modela

Da biste testirali inferencu modela, napravite Python fajl u vašem folderu pod imenom **app.py** i kopirajte sledeći kod:

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

Pokrenite kod koristeći:

```bash
python app.py
```

### Korak 6: Postavljanje modela na Azure AI

Postavljanje modela u Azure AI repozitorijum modela omogućava deljenje modela sa drugim članovima vašeg tima i takođe upravljanje verzijama modela. Da biste postavili model, pokrenite sledeću komandu:

> [!NOTE]
> Ažurirajte `{}` placeholders with the name of your resource group and Azure AI Project Name. 

To find your resource group `"resourceGroup"` i ime Azure AI projekta, zatim pokrenite sledeću komandu

```
az ml workspace show
```

Ili posetite +++ai.azure.com+++ i izaberite **management center** > **project** > **overview**

Zamenite `{}` placeholder-e imenom vaše resource grupe i imenom Azure AI projekta.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```

Model koji ste postavili možete videti i postaviti u produkciju na https://ml.azure.com/model/list

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо прецизности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални превод од стране људског преводиоца. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.