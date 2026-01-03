<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-07-16T16:19:21+00:00",
  "source_file": "code/04.Finetuning/olive-lab/readme.md",
  "language_code": "hu"
}
-->
# Labor. AI modellek optimalizálása eszközön történő futtatáshoz

## Bevezetés

> [!IMPORTANT]
> Ehhez a laborhoz **Nvidia A10 vagy A100 GPU** szükséges a megfelelő driverekkel és a CUDA toolkit (12-es vagy újabb verzió) telepítésével.

> [!NOTE]
> Ez egy **35 perces** labor, amely gyakorlati bevezetést nyújt az OLIVE használatával történő eszközön futó modellek optimalizálásának alapfogalmaiba.

## Tanulási célok

A labor végére képes leszel az OLIVE segítségével:

- AI modell kvantálására az AWQ kvantálási módszerrel.
- AI modell finomhangolására egy adott feladathoz.
- LoRA adapterek (finomhangolt modell) generálására az ONNX Runtime hatékony eszközön futó inferenciájához.

### Mi az Olive

Az Olive (*O*NNX *live*) egy modelloptimalizáló eszközkészlet, amelyhez tartozik egy parancssori felület (CLI), és amely lehetővé teszi, hogy minőségi és teljesítménybeli szempontból optimalizált modelleket szállíts az ONNX runtime +++https://onnxruntime.ai+++ számára.

![Olive Flow](../../../../../translated_images/olive-flow.c4f76d9142c579b2.hu.png)

Az Olive bemenete általában egy PyTorch vagy Hugging Face modell, a kimenete pedig egy optimalizált ONNX modell, amelyet egy eszközön (telepítési célpont) futtatnak, amely az ONNX runtime-ot használja. Az Olive a telepítési célpont AI gyorsítójához (NPU, GPU, CPU) igazítja az optimalizálást, amelyet olyan hardvergyártók biztosítanak, mint a Qualcomm, AMD, Nvidia vagy Intel.

Az Olive egy *workflow*-t hajt végre, ami egy rendezett sorozata az egyes modelloptimalizálási feladatoknak, amelyeket *pass*-oknak nevezünk – például modell tömörítés, gráf rögzítés, kvantálás, gráf optimalizálás. Minden pass-hoz tartozik egy paraméterkészlet, amely finomhangolható a legjobb metrikák, például pontosság és késleltetés eléréséhez, amelyeket a megfelelő értékelő mér. Az Olive keresési stratégiát alkalmaz, amely egy kereső algoritmust használ arra, hogy automatikusan hangolja be a pass-okat egyenként vagy csoportosan.

#### Az Olive előnyei

- **Csökkenti a kézi próbálkozásokkal járó frusztrációt és időt** a gráf optimalizálás, tömörítés és kvantálás különböző technikáinak kipróbálásában. Határozd meg a minőségi és teljesítménybeli követelményeket, és az Olive automatikusan megtalálja a legjobb modellt.
- **40+ beépített modelloptimalizáló komponens**, amelyek a legmodernebb kvantálási, tömörítési, gráf optimalizálási és finomhangolási technikákat fedik le.
- **Könnyen használható CLI** a gyakori modelloptimalizálási feladatokhoz, például olive quantize, olive auto-opt, olive finetune.
- Beépített modellcsomagolás és telepítés.
- Támogatja a **Multi LoRA kiszolgálásra** alkalmas modellek generálását.
- YAML/JSON segítségével felépíthetők workflow-k a modelloptimalizálási és telepítési feladatok összehangolására.
- **Hugging Face** és **Azure AI** integráció.
- Beépített **gyorsítótárazási** mechanizmus a **költségek csökkentésére**.

## Labor utasítások

> [!NOTE]
> Kérjük, győződj meg róla, hogy az Azure AI Hub-ot és projektet létrehoztad, valamint az A100 számítási erőforrást beállítottad az 1. labor szerint.

### 0. lépés: Csatlakozás az Azure AI számítási erőforráshoz

Az Azure AI számítási erőforráshoz a **VS Code** távoli funkciójával csatlakozhatsz.

1. Nyisd meg a **VS Code** asztali alkalmazást:
1. Nyisd meg a **parancspalettát** a **Shift+Ctrl+P** billentyűkombinációval.
1. A parancspalettában keresd meg az **AzureML - remote: Connect to compute instance in New Window** parancsot.
1. Kövesd a képernyőn megjelenő utasításokat a számítási erőforráshoz való csatlakozáshoz. Ez magában foglalja az Azure előfizetés, erőforráscsoport, projekt és a 1. laborban beállított számítási erőforrás kiválasztását.
1. Ha csatlakoztál az Azure ML számítási csomóponthoz, az megjelenik a **Visual Studio Code bal alsó sarkában** `><Azure ML: Compute Name` formában.

### 1. lépés: A repó klónozása

A VS Code-ban nyiss egy új terminált a **Ctrl+J** billentyűkkel, és klónozd a repót:

A terminálban megjelenik a prompt

```
azureuser@computername:~/cloudfiles/code$ 
```
A megoldás klónozása

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### 2. lépés: Mappa megnyitása a VS Code-ban

A releváns mappa megnyitásához futtasd a következő parancsot a terminálban, amely új ablakot nyit:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

Alternatívaként megnyithatod a mappát a **Fájl** > **Mappa megnyitása** menüpontból is.

### 3. lépés: Függőségek telepítése

Nyiss egy terminált a VS Code-ban az Azure AI számítási erőforráson (tipp: **Ctrl+J**), és futtasd a következő parancsokat a függőségek telepítéséhez:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> A függőségek telepítése körülbelül 5 percet vesz igénybe.

Ebben a laborban modelleket fogsz letölteni és feltölteni az Azure AI modell katalógusába. A katalógus eléréséhez jelentkezz be az Azure-ba a következő paranccsal:

```bash
az login
```

> [!NOTE]
> A bejelentkezéskor ki kell választanod az előfizetésedet. Győződj meg róla, hogy a laborhoz biztosított előfizetést választod.

### 4. lépés: Olive parancsok futtatása

Nyiss egy terminált a VS Code-ban az Azure AI számítási erőforráson (tipp: **Ctrl+J**), és győződj meg róla, hogy az `olive-ai` conda környezet aktív:

```bash
conda activate olive-ai
```

Ezután futtasd a következő Olive parancsokat a parancssorban.

1. **Adatok megtekintése:** Ebben a példában a Phi-3.5-Mini modellt finomhangolod, hogy utazással kapcsolatos kérdésekre specializálódjon. Az alábbi kód megjeleníti az adathalmaz első néhány rekordját, amelyek JSON lines formátumban vannak:

    ```bash
    head data/data_sample_travel.jsonl
    ```
1. **A modell kvantálása:** A modell betanítása előtt kvantáljuk az alábbi paranccsal, amely az Active Aware Quantization (AWQ) technikát használja +++https://arxiv.org/abs/2306.00978+++. Az AWQ a modell súlyait úgy kvantálja, hogy figyelembe veszi az inferencia során keletkező aktivációkat. Ez azt jelenti, hogy a kvantálási folyamat az aktivációk valós adateloszlását veszi alapul, ami jobb pontosságmegőrzést eredményez a hagyományos súlykvantálási módszerekhez képest.

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```

    Az AWQ kvantálás **~8 percet** vesz igénybe, és a modell méretét **~7,5 GB-ról ~2,5 GB-ra csökkenti**.

    Ebben a laborban bemutatjuk, hogyan lehet modelleket betölteni a Hugging Face-ről (például: `microsoft/Phi-3.5-mini-instruct`). Az Olive azonban lehetővé teszi modellek betöltését az Azure AI katalógusból is, ha a `model_name_or_path` argumentumot Azure AI asset ID-re állítod (például: `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`).

1. **A modell betanítása:** Ezután az `olive finetune` parancs finomhangolja a kvantált modellt. A modell kvantálása *finomhangolás előtt* jobb pontosságot eredményez, mivel a finomhangolás részben visszanyeri a kvantálás okozta pontosságvesztést.

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

    A finomhangolás (100 lépés) **~6 percet** vesz igénybe.

1. **Optimalizálás:** A betanított modellt az Olive `auto-opt` parancsával optimalizálod, amely rögzíti az ONNX gráfot, és automatikusan több optimalizálást végez a modell teljesítményének javítására CPU-n, például tömörítést és fúziókat. Megjegyzendő, hogy más eszközökre, például NPU-ra vagy GPU-ra is optimalizálhatsz, ha a `--device` és `--provider` argumentumokat módosítod – de ebben a laborban CPU-t használunk.

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

    Az optimalizálás **~5 percet** vesz igénybe.

### 5. lépés: Gyors teszt az inferenciához

A modell inferenciájának teszteléséhez hozz létre egy Python fájlt a mappádban **app.py** néven, és másold be a következő kódot:

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

A kód futtatásához használd a következő parancsot:

```bash
python app.py
```

### 6. lépés: Modell feltöltése az Azure AI-ba

A modell feltöltése az Azure AI modell tárába lehetővé teszi, hogy a modell megosztható legyen a fejlesztőcsapat többi tagjával, és kezeli a verziókövetést is. A modell feltöltéséhez futtasd a következő parancsot:

> [!NOTE]
> Cseréld ki a `{}` helyőrzőket az erőforráscsoportod és az Azure AI projekted nevére.

Az erőforráscsoport és az Azure AI projekt nevének lekérdezéséhez futtasd a következő parancsot:

```
az ml workspace show
```

Vagy látogass el a +++ai.azure.com+++ oldalra, és válaszd a **management center** > **project** > **overview** menüpontot.

Cseréld ki a `{}` helyőrzőket az erőforráscsoportod és az Azure AI projekted nevére.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```

Ezután megtekintheted a feltöltött modellt, és telepítheted azt a https://ml.azure.com/model/list címen.

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.