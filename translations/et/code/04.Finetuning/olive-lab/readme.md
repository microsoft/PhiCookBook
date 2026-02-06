# Labor. Tehisintellekti mudelite optimeerimine seadmesiseseks järeldamiseks

## Sissejuhatus

> [!IMPORTANT]
> Selle labori jaoks on vajalik **Nvidia A10 või A100 GPU** koos vastavate draiverite ja CUDA tööriistakomplektiga (versioon 12+).

> [!NOTE]
> See on **35-minutiline** labor, mis annab teile praktilise ülevaate mudelite optimeerimise põhikontseptsioonidest seadmesiseseks järeldamiseks, kasutades OLIVE-t.

## Õpieesmärgid

Selle labori lõpuks oskate kasutada OLIVE-t, et:

- Kvantiseerida tehisintellekti mudelit, kasutades AWQ kvantiseerimismeetodit.
- Peenhäälestada tehisintellekti mudelit konkreetse ülesande jaoks.
- Luua LoRA adaptereid (peenhäälestatud mudel) tõhusaks seadmesiseseks järeldamiseks ONNX Runtime'i abil.

### Mis on Olive

Olive (*O*NNX *live*) on mudelite optimeerimise tööriistakomplekt koos kaasneva CLI-ga, mis võimaldab teil tarnida mudeleid ONNX Runtime'i jaoks +++https://onnxruntime.ai+++ kvaliteedi ja jõudlusega.

![Olive Flow](../../../../../code/04.Finetuning/olive-lab/images/olive-flow.png)

Olive'i sisendiks on tavaliselt PyTorch või Hugging Face mudel ning väljundiks on optimeeritud ONNX mudel, mida käitatakse seadmes (juurutamise sihtmärk), kus töötab ONNX Runtime. Olive optimeerib mudeli juurutamise sihtmärgi AI kiirendi (NPU, GPU, CPU) jaoks, mille on pakkunud riistvaratootja, näiteks Qualcomm, AMD, Nvidia või Intel.

Olive täidab *töövoogu*, mis on üksikute mudelite optimeerimise ülesannete järjestatud jada, mida nimetatakse *passideks* - näited passidest hõlmavad mudeli tihendamist, graafiku jäädvustamist, kvantiseerimist, graafiku optimeerimist. Igal passil on parameetrite komplekt, mida saab häälestada parimate mõõdikute, näiteks täpsuse ja latentsuse, saavutamiseks, mida hindab vastav hindaja. Olive kasutab otsingustrateegiat, mis kasutab otsingualgoritmi iga passi ükshaaval või passide komplekti automaatseks häälestamiseks.

#### Olive'i eelised

- **Vähendab pettumust ja aega**, mis kulub erinevate graafiku optimeerimise, tihendamise ja kvantiseerimise tehnikate katse-eksituse meetodil katsetamisele. Määrake oma kvaliteedi- ja jõudlusnõuded ning las Olive leiab automaatselt teie jaoks parima mudeli.
- **40+ sisseehitatud mudelite optimeerimise komponente**, mis hõlmavad tipptasemel tehnikaid kvantiseerimises, tihendamises, graafiku optimeerimises ja peenhäälestamises.
- **Lihtsasti kasutatav CLI** tavaliste mudelite optimeerimise ülesannete jaoks. Näiteks olive quantize, olive auto-opt, olive finetune.
- Mudelite pakkimine ja juurutamine on sisseehitatud.
- Toetab mudelite loomist **Multi LoRA teenindamiseks**.
- Töövoogude koostamine YAML/JSON abil mudelite optimeerimise ja juurutamise ülesannete korraldamiseks.
- **Hugging Face** ja **Azure AI** integratsioon.
- Sisseehitatud **vahemälu** mehhanism **kulude kokkuhoiuks**.

## Labori juhised
> [!NOTE]
> Palun veenduge, et olete seadistanud oma Azure AI Hubi ja projekti ning seadistanud oma A100 arvutusressursi vastavalt 1. laborile.

### Samm 0: Ühendage oma Azure AI Compute'iga

Ühendate Azure AI arvutiga, kasutades **VS Code'i** kaugühenduse funktsiooni.

1. Avage oma **VS Code'i** töölauarakendus:
1. Avage **käsupalett** kasutades **Shift+Ctrl+P**.
1. Otsige käsupaletis **AzureML - remote: Connect to compute instance in New Window**.
1. Järgige ekraanil kuvatavaid juhiseid, et ühenduda arvutiga. See hõlmab teie Azure'i tellimuse, ressursigrupi, projekti ja arvuti nime valimist, mille te 1. laboris seadistasite.
1. Kui olete oma Azure ML Compute'i sõlmega ühendatud, kuvatakse see **Visual Code'i vasakus allnurgas** `><Azure ML: Compute Name`.

### Samm 1: Kloonige see repo

VS Code'is saate avada uue terminali, vajutades **Ctrl+J**, ja kloonida selle repo:

Terminalis peaksite nägema järgmist viipa:

```
azureuser@computername:~/cloudfiles/code$ 
```
Klooni lahendus

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### Samm 2: Avage kaust VS Code'is

Kausta avamiseks VS Code'is täitke terminalis järgmine käsk, mis avab uue akna:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

Teise võimalusena saate kausta avada, valides **File** > **Open Folder**.

### Samm 3: Sõltuvused

Avage terminaliaken VS Code'is oma Azure AI Compute'i instantsis (vihje: **Ctrl+J**) ja täitke järgmised käsud, et installida sõltuvused:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> Kõigi sõltuvuste installimine võtab aega ~5 minutit.

Selles laboris laadite alla ja üles mudeleid Azure AI mudelikataloogi. Selleks, et saaksite mudelikataloogile juurde pääseda, peate Azure'i sisse logima, kasutades:

```bash
az login
```

> [!NOTE]
> Sisselogimisel palutakse teil valida oma tellimus. Veenduge, et määrate tellimuse sellele, mis on selle labori jaoks ette nähtud.

### Samm 4: Käivitage Olive'i käsud

Avage terminaliaken VS Code'is oma Azure AI Compute'i instantsis (vihje: **Ctrl+J**) ja veenduge, et `olive-ai` conda keskkond on aktiveeritud:

```bash
conda activate olive-ai
```

Seejärel täitke järgmised Olive'i käsud käsureal.

1. **Andmete kontrollimine:** Selles näites peenhäälestate Phi-3.5-Mini mudelit, et see spetsialiseeruks reisidega seotud küsimustele vastamisele. Allolev kood kuvab andmekogumi esimesed kirjed, mis on JSON-ridade formaadis:

    ```bash
    head data/data_sample_travel.jsonl
    ```
1. **Mudeli kvantiseerimine:** Enne mudeli treenimist kvantiseerige see järgmise käsuga, mis kasutab tehnikat nimega Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++. AWQ kvantiseerib mudeli kaalu, võttes arvesse järeldamise ajal toodetud aktiveerimisi. See tähendab, et kvantiseerimisprotsess arvestab aktiveerimiste tegelikku andmejaotust, mis viib mudeli täpsuse parema säilimiseni võrreldes traditsiooniliste kaalu kvantiseerimismeetoditega.

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```
    
    AWQ kvantiseerimine võtab aega **~8 minutit**, mis **vähendab mudeli suurust ~7,5 GB-lt ~2,5 GB-le**.

    Selles laboris näitame, kuidas sisestada mudeleid Hugging Face'ist (näiteks: `microsoft/Phi-3.5-mini-instruct`). Kuid Olive võimaldab teil sisestada mudeleid ka Azure AI kataloogist, uuendades `model_name_or_path` argumenti Azure AI vara ID-ks (näiteks: `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`).

1. **Mudeli treenimine:** Järgmisena peenhäälestab `olive finetune` käsk kvantiseeritud mudeli. Mudeli kvantiseerimine *enne* peenhäälestamist annab parema täpsuse, kuna peenhäälestamise protsess taastab osa kvantiseerimisest tingitud kaost.

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
    
    Peenhäälestamine (100 sammu) võtab aega **~6 minutit**.

1. **Optimeerimine:** Kui mudel on treenitud, optimeerite mudeli Olive'i `auto-opt` käsu abil, mis jäädvustab ONNX graafiku ja viib automaatselt läbi mitmeid optimeerimisi, et parandada mudeli jõudlust CPU jaoks, tihendades mudelit ja tehes liitmisi. Tuleb märkida, et saate optimeerida ka teiste seadmete, näiteks NPU või GPU jaoks, lihtsalt uuendades `--device` ja `--provider` argumente - kuid selle labori eesmärgil kasutame CPU-d.

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
    
    Optimeerimine võtab aega **~5 minutit**.

### Samm 5: Mudeli järeldamise kiirtest

Mudeli järeldamise testimiseks looge oma kausta Python-fail nimega **app.py** ja kopeerige-kleepige järgmine kood:

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

Käivitage kood, kasutades:

```bash
python app.py
```

### Samm 6: Mudeli üleslaadimine Azure AI-sse

Mudeli üleslaadimine Azure AI mudelikataloogi muudab mudeli jagatavaks teie arendustiimi teiste liikmetega ja haldab ka mudeli versioonikontrolli. Mudeli üleslaadimiseks käivitage järgmine käsk:

> [!NOTE]
> Uuendage `{}` kohatäited oma ressursigrupi ja Azure AI projekti nimega.

Oma ressursigrupi `"resourceGroup"` ja Azure AI projekti nime leidmiseks käivitage järgmine käsk:

```
az ml workspace show
```

Või minge +++ai.azure.com+++ ja valige **management center** **project** **overview**.

Uuendage `{}` kohatäited oma ressursigrupi ja Azure AI projekti nimega.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```

Seejärel saate oma üleslaaditud mudelit vaadata ja juurutada aadressil https://ml.azure.com/model/list

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.