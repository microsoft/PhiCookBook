# Laboratorija. Optimizuokite AI modelius įrenginio inferencijai

## Įvadas

> [!IMPORTANT]
> Šiai laboratorijai reikalinga **Nvidia A10 arba A100 GPU** su įdiegtais atitinkamais tvarkyklėmis ir CUDA įrankių rinkiniu (12+ versija).

> [!NOTE]
> Tai yra **35 minučių** laboratorija, kuri suteiks praktinį įvadą į pagrindines modelių optimizavimo koncepcijas naudojant OLIVE.

## Mokymosi tikslai

Baigę šią laboratoriją, galėsite naudoti OLIVE, kad:

- Kvantizuotumėte AI modelį naudodami AWQ kvantizavimo metodą.
- Patobulintumėte AI modelį konkrečiai užduočiai.
- Sukurtumėte LoRA adapterius (patobulintą modelį) efektyviai įrenginio inferencijai naudojant ONNX Runtime.

### Kas yra Olive

Olive (*O*NNX *live*) yra modelių optimizavimo įrankių rinkinys su pridedamu CLI, kuris leidžia paruošti modelius ONNX Runtime +++https://onnxruntime.ai+++ su aukšta kokybe ir našumu.

![Olive Flow](../../../../../code/03.Finetuning/olive-lab/images/olive-flow.png)

Olive įvestis paprastai yra PyTorch arba Hugging Face modelis, o išvestis – optimizuotas ONNX modelis, vykdomas įrenginyje (diegimo taikinys), kuriame veikia ONNX Runtime. Olive optimizuoja modelį pagal diegimo taikinio AI akceleratorių (NPU, GPU, CPU), kurį teikia tokie techninės įrangos tiekėjai kaip Qualcomm, AMD, Nvidia ar Intel.

Olive vykdo *darbo eigą*, kuri yra tvarkinga atskirų modelio optimizavimo užduočių seka, vadinama *perėjimais* – pavyzdžiui, modelio suspaudimas, grafiko užfiksavimas, kvantizavimas, grafiko optimizavimas. Kiekvienas perėjimas turi parametrų rinkinį, kurį galima reguliuoti siekiant geriausių metrikų, pavyzdžiui, tikslumo ir vėlinimo, kuriuos vertina atitinkamas vertintojas. Olive naudoja paieškos strategiją, kuri taiko paieškos algoritmą automatiškai reguliuoti kiekvieną perėjimą atskirai arba perėjimų rinkinį kartu.

#### Olive privalumai

- **Sumažinkite nusivylimą ir laiką**, skiriamą bandymams ir klaidoms, eksperimentuojant su įvairiomis grafiko optimizavimo, suspaudimo ir kvantizavimo technikomis. Apibrėžkite savo kokybės ir našumo apribojimus, o Olive automatiškai suras geriausią modelį už jus.
- **40+ įmontuotų modelių optimizavimo komponentų**, apimančių pažangiausias kvantizavimo, suspaudimo, grafiko optimizavimo ir patobulinimo technikas.
- **Paprastas CLI** dažnoms modelių optimizavimo užduotims. Pavyzdžiui, olive quantize, olive auto-opt, olive finetune.
- Modelių paketavimas ir diegimas įmontuotas.
- Palaiko modelių generavimą **Multi LoRA aptarnavimui**.
- Darbo eigų konstravimas naudojant YAML/JSON, kad būtų galima organizuoti modelių optimizavimo ir diegimo užduotis.
- **Hugging Face** ir **Azure AI** integracija.
- Įmontuotas **kešavimo** mechanizmas, leidžiantis **sutaupyti išlaidas**.

## Laboratorijos instrukcijos
> [!NOTE]
> Įsitikinkite, kad paruošėte savo Azure AI Hub ir projektą bei nustatėte savo A100 kompiuterį pagal 1 laboratoriją.

### 0 žingsnis: Prisijunkite prie Azure AI Compute

Prisijungsite prie Azure AI Compute naudodami nuotolinę funkciją **VS Code.**

1. Atidarykite savo **VS Code** darbalaukio programą:
1. Atidarykite **komandų paletę** naudodami **Shift+Ctrl+P**.
1. Komandų paletėje ieškokite **AzureML - remote: Connect to compute instance in New Window**.
1. Vykdykite ekrane pateiktas instrukcijas, kad prisijungtumėte prie Compute. Tai apims jūsų Azure prenumeratos, išteklių grupės, projekto ir Compute pavadinimo pasirinkimą, kurį nustatėte 1 laboratorijoje.
1. Kai prisijungsite prie savo Azure ML Compute mazgo, tai bus rodoma **apatiniame kairiajame Visual Code kampe** `><Azure ML: Compute Name`.

### 1 žingsnis: Klonuokite šį repo

VS Code galite atidaryti naują terminalą naudodami **Ctrl+J** ir klonuoti šį repo:

Terminale turėtumėte matyti raginimą

```
azureuser@computername:~/cloudfiles/code$ 
```
Klonuokite sprendimą

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### 2 žingsnis: Atidarykite aplanką VS Code

Norėdami atidaryti VS Code atitinkamame aplanke, terminale vykdykite šią komandą, kuri atidarys naują langą:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

Arba galite atidaryti aplanką pasirinkdami **File** > **Open Folder**.

### 3 žingsnis: Priklausomybės

Atidarykite terminalo langą VS Code savo Azure AI Compute mazge (patarimas: **Ctrl+J**) ir vykdykite šias komandas, kad įdiegtumėte priklausomybes:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> Priklausomybių diegimas užtruks ~5 minutes.

Šioje laboratorijoje atsisiųsite ir įkelsite modelius į Azure AI Model katalogą. Kad galėtumėte pasiekti modelių katalogą, turėsite prisijungti prie Azure naudodami:

```bash
az login
```

> [!NOTE]
> Prisijungimo metu būsite paprašyti pasirinkti savo prenumeratą. Įsitikinkite, kad pasirinkote prenumeratą, skirtą šiai laboratorijai.

### 4 žingsnis: Vykdykite Olive komandas

Atidarykite terminalo langą VS Code savo Azure AI Compute mazge (patarimas: **Ctrl+J**) ir įsitikinkite, kad aktyvuota `olive-ai` conda aplinka:

```bash
conda activate olive-ai
```

Toliau vykdykite šias Olive komandas komandinėje eilutėje.

1. **Patikrinkite duomenis:** Šiame pavyzdyje patobulinsite Phi-3.5-Mini modelį, kad jis būtų specializuotas atsakyti į kelionių klausimus. Žemiau pateiktas kodas parodo pirmuosius duomenų rinkinio įrašus, kurie yra JSON linijų formatu:

    ```bash
    head data/data_sample_travel.jsonl
    ```
1. **Kvantizuokite modelį:** Prieš treniruodami modelį, pirmiausia kvantizuokite jį naudodami šią komandą, kuri naudoja techniką, vadinamą Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++. AWQ kvantizuoja modelio svorius, atsižvelgdama į aktyvacijas, kurios susidaro inferencijos metu. Tai reiškia, kad kvantizavimo procesas atsižvelgia į faktinį duomenų pasiskirstymą aktyvacijose, todėl geriau išsaugomas modelio tikslumas, palyginti su tradiciniais svorių kvantizavimo metodais.

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```

    Kvantizavimas užtrunka **~8 minutes**, o modelio dydis sumažėja nuo ~7.5GB iki ~2.5GB.

    Šioje laboratorijoje parodome, kaip įvesti modelius iš Hugging Face (pavyzdžiui: `microsoft/Phi-3.5-mini-instruct`). Tačiau Olive taip pat leidžia įvesti modelius iš Azure AI katalogo, atnaujinant `model_name_or_path` argumentą į Azure AI turto ID (pavyzdžiui: `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`).

1. **Treniruokite modelį:** Toliau `olive finetune` komanda patobulina kvantizuotą modelį. Kvantizuoti modelį *prieš* patobulinimą, o ne po jo, suteikia geresnį tikslumą, nes patobulinimo procesas atkuria dalį kvantizavimo praradimo.

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

    Patobulinimas užtrunka **~6 minutes** (su 100 žingsnių).

1. **Optimizuokite:** Kai modelis yra patobulintas, dabar optimizuokite modelį naudodami Olive `auto-opt` komandą, kuri užfiksuos ONNX grafiką ir automatiškai atliks keletą optimizacijų, kad pagerintų modelio našumą CPU, suspaudžiant modelį ir atliekant susijungimus. Reikia pažymėti, kad taip pat galite optimizuoti kitus įrenginius, tokius kaip NPU ar GPU, tiesiog atnaujindami `--device` ir `--provider` argumentus – tačiau šios laboratorijos tikslams naudosime CPU.

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

    Optimizavimas užtrunka **~5 minutes**.

### 5 žingsnis: Greitas modelio inferencijos testas

Norėdami išbandyti modelio inferenciją, sukurkite Python failą savo aplanke, pavadintą **app.py**, ir nukopijuokite-įklijuokite šį kodą:

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

Vykdykite kodą naudodami:

```bash
python app.py
```

### 6 žingsnis: Įkelkite modelį į Azure AI

Modelio įkėlimas į Azure AI modelių saugyklą leidžia modelį dalintis su kitais jūsų kūrimo komandos nariais ir taip pat tvarko modelio versijų kontrolę. Norėdami įkelti modelį, vykdykite šią komandą:

> [!NOTE]
> Atnaujinkite `{}` vietos rezervavimo ženklus savo išteklių grupės ir Azure AI projekto pavadinimu.

Norėdami rasti savo išteklių grupę `"resourceGroup"` ir Azure AI projekto pavadinimą, vykdykite šią komandą:

```
az ml workspace show
```

Arba eikite į +++ai.azure.com+++ ir pasirinkite **management center** **project** **overview**.

Atnaujinkite `{}` vietos rezervavimo ženklus savo išteklių grupės ir Azure AI projekto pavadinimu.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```

Tada galite matyti savo įkeltą modelį ir jį diegti adresu https://ml.azure.com/model/list

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.