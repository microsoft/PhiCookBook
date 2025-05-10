<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-05-09T04:43:10+00:00",
  "source_file": "code/04.Finetuning/olive-lab/readme.md",
  "language_code": "sr"
}
-->
# Lab. Optimizujte AI modele za inferencu na uređaju

## Uvod

> [!IMPORTANT]  
> Ovaj laboratorijski rad zahteva **Nvidia A10 ili A100 GPU** sa odgovarajućim drajverima i instaliranim CUDA toolkit-om (verzija 12+).

> [!NOTE]  
> Ovo je **35-minutni** laboratorijski rad koji će vam pružiti praktičan uvod u osnovne koncepte optimizacije modela za inferencu na uređaju koristeći OLIVE.

## Ciljevi učenja

Na kraju ovog laboratorijskog rada bićete u mogućnosti da koristite OLIVE za:

- Kvantizaciju AI modela koristeći AWQ metodu kvantizacije.  
- Fino podešavanje AI modela za specifičan zadatak.  
- Generisanje LoRA adaptera (fino podešenog modela) za efikasnu inferencu na uređaju koristeći ONNX Runtime.

### Šta je Olive

Olive (*O*NNX *live*) je alat za optimizaciju modela sa pratećim CLI interfejsom koji vam omogućava da isporučujete modele za ONNX runtime +++https://onnxruntime.ai+++ sa kvalitetom i performansama.

![Olive Flow](../../../../../translated_images/olive-flow.e4682fa65f77777f49e884482fa8dd83eadcb90904fcb41a54093af85c330060.sr.png)

Ulaz u Olive je obično PyTorch ili Hugging Face model, a izlaz je optimizovani ONNX model koji se izvršava na uređaju (ciljnoj platformi) koji koristi ONNX runtime. Olive optimizuje model za AI akcelerator ciljne platforme (NPU, GPU, CPU) koji obezbeđuje proizvođač hardvera kao što su Qualcomm, AMD, Nvidia ili Intel.

Olive izvršava *workflow*, što je uređeni niz pojedinačnih zadataka optimizacije modela nazvanih *passes* – primeri takvih koraka su: kompresija modela, hvatanje grafa, kvantizacija, optimizacija grafa. Svaki korak ima skup parametara koje možete podesiti da biste postigli najbolje metrike, kao što su tačnost i latencija, koje ocenjuje odgovarajući evaluator. Olive koristi strategiju pretrage koja primenjuje algoritam pretrage za automatsko podešavanje svakog koraka pojedinačno ili grupe koraka zajedno.

#### Prednosti Olive

- **Smanjuje frustraciju i vreme** ručnog eksperimentisanja metodom pokušaja i greške sa različitim tehnikama optimizacije grafa, kompresije i kvantizacije. Definišite svoje zahteve za kvalitet i performanse i dozvolite Olive-u da automatski pronađe najbolji model za vas.  
- **Više od 40 ugrađenih komponenti za optimizaciju modela** koje pokrivaju najsavremenije tehnike u kvantizaciji, kompresiji, optimizaciji grafa i fino podešavanje.  
- **Jednostavan CLI** za uobičajene zadatke optimizacije modela. Na primer, olive quantize, olive auto-opt, olive finetune.  
- Ugrađeno pakovanje i implementacija modela.  
- Podrška za generisanje modela za **Multi LoRA servisiranje**.  
- Kreiranje workflow-a korišćenjem YAML/JSON za orkestraciju zadataka optimizacije i implementacije modela.  
- Integracija sa **Hugging Face** i **Azure AI**.  
- Ugrađeni mehanizam za **keširanje** radi **uštede troškova**.

## Uputstva za laboratorijski rad

> [!NOTE]  
> Proverite da li ste postavili svoj Azure AI Hub i projekat i konfigurisali A100 računarski resurs prema Lab 1.

### Korak 0: Povežite se na Azure AI Compute

Povezaćete se na Azure AI računarski resurs koristeći udaljenu funkciju u **VS Code-u**.

1. Otvorite **VS Code** desktop aplikaciju:  
1. Otvorite **command palette** pomoću **Shift+Ctrl+P**  
1. U command palette-u potražite **AzureML - remote: Connect to compute instance in New Window**.  
1. Pratite uputstva na ekranu da se povežete na Compute. Ovo uključuje izbor vaše Azure pretplate, Resource Group, projekta i imena računara koji ste postavili u Lab 1.  
1. Kada se povežete na Azure ML Compute čvor, to će biti prikazano u **donjem levom uglu Visual Code-a** `><Azure ML: Compute Name`

### Korak 1: Klonirajte ovaj repozitorijum

U VS Code-u otvorite novi terminal pomoću **Ctrl+J** i klonirajte ovaj repozitorijum:

U terminalu ćete videti prompt

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

Alternativno, možete otvoriti folder tako što ćete izabrati **File** > **Open Folder**.

### Korak 3: Zavisanosti

Otvorite terminal u VS Code-u na vašem Azure AI Compute instanci (prečica: **Ctrl+J**) i izvršite sledeće komande da instalirate zavisnosti:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]  
> Instalacija svih zavisnosti traje oko 5 minuta.

U ovom laboratorijskom radu ćete preuzimati i otpremati modele u Azure AI katalog modela. Da biste pristupili katalogu modela, potrebno je da se prijavite na Azure koristeći:

```bash
az login
```

> [!NOTE]  
> Prilikom prijavljivanja bićete upitani da izaberete svoju pretplatu. Obavezno izaberite pretplatu dodeljenu za ovaj laboratorijski rad.

### Korak 4: Izvršite Olive komande

Otvorite terminal u VS Code-u na vašem Azure AI Compute instanci (prečica: **Ctrl+J**) i uverite se da je aktivno `olive-ai` conda okruženje:

```bash
conda activate olive-ai
```

Zatim izvršite sledeće Olive komande u komandnoj liniji.

1. **Pregledajte podatke:** U ovom primeru ćete fino podešavati Phi-3.5-Mini model kako bi bio specijalizovan za odgovaranje na pitanja vezana za putovanja. Sledeći kod prikazuje prvih nekoliko zapisa iz skupa podataka, koji su u JSON lines formatu:

    ```bash
    head data/data_sample_travel.jsonl
    ```  
1. **Kvantizujte model:** Pre treniranja modela prvo ga kvantizujete sledećom komandom koja koristi tehniku zvanu Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++. AWQ kvantizuje težine modela uzimajući u obzir aktivacije koje se javljaju tokom inferencije. To znači da proces kvantizacije uzima u obzir stvarnu distribuciju podataka u aktivacijama, što dovodi do bolje očuvanosti tačnosti modela u poređenju sa tradicionalnim metodama kvantizacije težina.

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```

    Završetak AWQ kvantizacije traje oko **8 minuta**, a model se smanjuje sa otprilike **7.5GB na 2.5GB**.

    U ovom laboratorijskom radu prikazujemo kako da učitate modele sa Hugging Face (na primer: `microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune` komanda fino podešava kvantizovani model. Kvantizacija modela *pre* fino podešavanja, umesto posle, daje bolju tačnost jer proces fino podešavanja delimično nadoknađuje gubitke nastale kvantizacijom.

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

1. **Optimizujte:** Nakon treniranja modela, sada ga optimizujete koristeći Olive komandu `auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider` – ali za potrebe ovog laboratorijskog rada koristićemo CPU.

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

Da biste testirali inferencu modela, kreirajte Python fajl u vašem folderu pod nazivom **app.py** i kopirajte sledeći kod:

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

Pokrenite kod pomoću:

```bash
python app.py
```

### Korak 6: Otpremite model na Azure AI

Otpremanje modela u Azure AI repozitorijum modela omogućava deljenje modela sa drugim članovima vašeg tima za razvoj i takođe upravlja verzionisanjem modela. Da biste otpremili model, pokrenite sledeću komandu:

> [!NOTE]  
> Ažurirajte `{}` sa vašim "resourceGroup" i imenom Azure AI projekta, zatim pokrenite sledeću komandu

```
az ml workspace show
```

Ili putem +++ai.azure.com+++ gde izaberete **management center** > **project** > **overview**

Zamenite `{}` sa imenom vaše resource grupe i imenom Azure AI projekta.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```  
Nakon toga možete videti otpremljeni model i implementirati ga na https://ml.azure.com/model/list

**Одрицање од одговорности**:  
Овај документ је преведен помоћу AI сервиса за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако настојимо да превод буде прецизан, молимо имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Изворни документ на његовом оригиналном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални превод од стране стручних људи. Нисмо одговорни за било какве неспоразуме или погрешне тумачења која произилазе из употребе овог превода.