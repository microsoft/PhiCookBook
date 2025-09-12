<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c2bc0950f44919ac75a88c1a871680c2",
  "translation_date": "2025-09-12T14:44:57+00:00",
  "source_file": "md/03.FineTuning/Finetuning_VSCodeaitoolkit.md",
  "language_code": "lt"
}
-->
## Sveiki atvykę į AI Toolkit for VS Code

[AI Toolkit for VS Code](https://github.com/microsoft/vscode-ai-toolkit/tree/main) sujungia įvairius modelius iš Azure AI Studio Catalog ir kitų katalogų, tokių kaip Hugging Face. Šis įrankių rinkinys supaprastina dažniausiai pasitaikančias kūrimo užduotis, susijusias su AI programų kūrimu naudojant generatyvinius AI įrankius ir modelius, per:
- Pradėkite nuo modelių atradimo ir žaidimų aikštelės.
- Modelių pritaikymas ir inferencija naudojant vietinius kompiuterinius resursus.
- Nuotolinis modelių pritaikymas ir inferencija naudojant Azure resursus.

[Įdiegti AI Toolkit for VSCode](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

![AIToolkit FineTuning](../../../../imgs/03/intro/Aitoolkit.png)

**[Privati peržiūra]** Vieno paspaudimo Azure Container Apps paruošimas modelių pritaikymui ir inferencijai debesyje.

Dabar pereikime prie jūsų AI programų kūrimo:

- [Sveiki atvykę į AI Toolkit for VS Code](../../../../md/03.FineTuning)
- [Vietinis kūrimas](../../../../md/03.FineTuning)
  - [Pasiruošimas](../../../../md/03.FineTuning)
  - [Aktyvuoti Conda](../../../../md/03.FineTuning)
  - [Tik bazinio modelio pritaikymas](../../../../md/03.FineTuning)
  - [Modelio pritaikymas ir inferencija](../../../../md/03.FineTuning)
  - [Modelio pritaikymas](../../../../md/03.FineTuning)
  - [Microsoft Olive](../../../../md/03.FineTuning)
  - [Pritaikymo pavyzdžiai ir ištekliai](../../../../md/03.FineTuning)
- [**\[Privati peržiūra\]** Nuotolinis kūrimas](../../../../md/03.FineTuning)
  - [Būtinos sąlygos](../../../../md/03.FineTuning)
  - [Nuotolinio kūrimo projekto nustatymas](../../../../md/03.FineTuning)
  - [Azure resursų paruošimas](../../../../md/03.FineTuning)
  - [\[Pasirinktinai\] Pridėti Huggingface tokeną prie Azure Container App slaptumo](../../../../md/03.FineTuning)
  - [Paleisti pritaikymą](../../../../md/03.FineTuning)
  - [Inferencijos taško paruošimas](../../../../md/03.FineTuning)
  - [Inferencijos taško diegimas](../../../../md/03.FineTuning)
  - [Išplėstinis naudojimas](../../../../md/03.FineTuning)

## Vietinis kūrimas
### Pasiruošimas

1. Įsitikinkite, kad NVIDIA tvarkyklė yra įdiegta jūsų kompiuteryje.
2. Paleiskite `huggingface-cli login`, jei naudojate HF duomenų rinkinių naudojimui.
3. `Olive` pagrindiniai nustatymai, paaiškinantys viską, kas keičia atminties naudojimą.

### Aktyvuoti Conda
Kadangi naudojame WSL aplinką, kuri yra bendra, jums reikia rankiniu būdu aktyvuoti conda aplinką. Po šio žingsnio galite paleisti pritaikymą arba inferenciją.

```bash
conda activate [conda-env-name] 
```

### Tik bazinio modelio pritaikymas
Jei norite išbandyti bazinį modelį be pritaikymo, galite paleisti šią komandą po conda aktyvavimo.

```bash
cd inference

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://0.0.0.0:7860) in a browser after gradio initiates the connections.
python gradio_chat.py --baseonly
```

### Modelio pritaikymas ir inferencija

Kai darbo aplinka atidaroma kūrimo konteineryje, atidarykite terminalą (numatytasis kelias yra projekto šaknis), tada paleiskite žemiau esančią komandą, kad pritaikytumėte LLM pasirinktame duomenų rinkinyje.

```bash
python finetuning/invoke_olive.py 
```

Kontroliniai taškai ir galutinis modelis bus išsaugoti aplanke `models`.

Tada paleiskite inferenciją su pritaikytu modeliu per pokalbius `konsolėje`, `interneto naršyklėje` arba `prompt flow`.

```bash
cd inference

# Console interface.
python console_chat.py

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://127.0.0.1:7860) in a browser after gradio initiates the connections.
python gradio_chat.py
```

Norėdami naudoti `prompt flow` VS Code, prašome peržiūrėti šį [Greito starto vadovą](https://microsoft.github.io/promptflow/how-to-guides/quick-start.html).

### Modelio pritaikymas

Toliau atsisiųskite šį modelį, priklausomai nuo GPU prieinamumo jūsų įrenginyje.

Norėdami pradėti vietinį pritaikymo seansą naudojant QLoRA, pasirinkite modelį, kurį norite pritaikyti iš mūsų katalogo.
| Platforma(-os) | GPU prieinamas | Modelio pavadinimas | Dydis (GB) |
|---------|---------|--------|--------|
| Windows | Taip | Phi-3-mini-4k-**directml**-int4-awq-block-128-onnx | 2.13GB |
| Linux | Taip | Phi-3-mini-4k-**cuda**-int4-onnx | 2.30GB |
| Windows<br>Linux | Ne | Phi-3-mini-4k-**cpu**-int4-rtn-block-32-acc-level-4-onnx | 2.72GB |

**_Pastaba_** Jums nereikia Azure paskyros, kad atsisiųstumėte modelius.

Phi3-mini (int4) modelis yra maždaug 2GB-3GB dydžio. Priklausomai nuo jūsų tinklo greičio, atsisiuntimas gali užtrukti kelias minutes.

Pradėkite pasirinkdami projekto pavadinimą ir vietą.
Tada pasirinkite modelį iš modelių katalogo. Jums bus pasiūlyta atsisiųsti projekto šabloną. Tada galite spustelėti "Konfigūruoti projektą", kad pritaikytumėte įvairius nustatymus.

### Microsoft Olive 

Mes naudojame [Olive](https://microsoft.github.io/Olive/why-olive.html), kad paleistume QLoRA pritaikymą PyTorch modelyje iš mūsų katalogo. Visi nustatymai yra iš anksto nustatyti su numatytomis reikšmėmis, kad optimizuotų pritaikymo procesą vietoje, naudojant optimizuotą atminties naudojimą, tačiau juos galima pritaikyti pagal jūsų scenarijų.

### Pritaikymo pavyzdžiai ir ištekliai

- [Pritaikymo pradžios vadovas](https://learn.microsoft.com/windows/ai/toolkit/toolkit-fine-tune)
- [Pritaikymas naudojant HuggingFace duomenų rinkinį](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-hf-dataset.md)
- [Pritaikymas naudojant paprastą duomenų rinkinį](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-simple-dataset.md)

## **[Privati peržiūra]** Nuotolinis kūrimas

### Būtinos sąlygos

1. Norėdami paleisti modelio pritaikymą nuotoliniame Azure Container App aplinkoje, įsitikinkite, kad jūsų prenumerata turi pakankamą GPU pajėgumą. Pateikite [pagalbos bilietą](https://azure.microsoft.com/support/create-ticket/), kad paprašytumėte reikiamo pajėgumo jūsų programai. [Daugiau informacijos apie GPU pajėgumą](https://learn.microsoft.com/azure/container-apps/workload-profiles-overview)
2. Jei naudojate privatų duomenų rinkinį HuggingFace, įsitikinkite, kad turite [HuggingFace paskyrą](https://huggingface.co/?WT.mc_id=aiml-137032-kinfeylo) ir [sukurkite prieigos tokeną](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=aiml-137032-kinfeylo)
3. Įgalinkite Nuotolinio pritaikymo ir inferencijos funkciją AI Toolkit for VS Code
   1. Atidarykite VS Code nustatymus pasirinkdami *File -> Preferences -> Settings*.
   2. Eikite į *Extensions* ir pasirinkite *AI Toolkit*.
   3. Pasirinkite *"Enable Remote Fine-tuning And Inference"* parinktį.
   4. Perkraukite VS Code, kad pakeitimai įsigaliotų.

- [Nuotolinis pritaikymas](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/remote-finetuning.md)

### Nuotolinio kūrimo projekto nustatymas
1. Paleiskite komandų paletę `AI Toolkit: Focus on Resource View`.
2. Eikite į *Model Fine-tuning*, kad pasiektumėte modelių katalogą. Priskirkite savo projektui pavadinimą ir pasirinkite jo vietą savo kompiuteryje. Tada spustelėkite *"Configure Project"* mygtuką.
3. Projekto konfigūracija
    1. Venkite įjungti *"Fine-tune locally"* parinktį.
    2. Olive konfigūracijos nustatymai bus rodomi su iš anksto nustatytomis numatytomis reikšmėmis. Prašome pritaikyti ir užpildyti šiuos nustatymus pagal poreikį.
    3. Pereikite prie *Generate Project*. Šiame etape naudojama WSL ir sukuriama nauja Conda aplinka, ruošiantis būsimoms naujovėms, įskaitant Dev Containers.
4. Spustelėkite *"Relaunch Window In Workspace"*, kad atidarytumėte savo nuotolinio kūrimo projektą.

> **Pastaba:** Projektas šiuo metu veikia arba vietoje, arba nuotoliniu būdu AI Toolkit for VS Code. Jei pasirinksite *"Fine-tune locally"* projekto kūrimo metu, jis veiks tik WSL aplinkoje be nuotolinio kūrimo galimybių. Kita vertus, jei neįjungsite *"Fine-tune locally"*, projektas bus apribotas nuotoline Azure Container App aplinka.

### Azure resursų paruošimas
Norėdami pradėti, jums reikia paruošti Azure resursus nuotoliniam pritaikymui. Tai atlikite paleisdami `AI Toolkit: Provision Azure Container Apps job for fine-tuning` iš komandų paletės.

Stebėkite paruošimo eigą per nuorodą, rodomą išvesties kanale.

### [Pasirinktinai] Pridėti Huggingface tokeną prie Azure Container App slaptumo
Jei naudojate privatų HuggingFace duomenų rinkinį, nustatykite savo HuggingFace tokeną kaip aplinkos kintamąjį, kad išvengtumėte rankinio prisijungimo prie Hugging Face Hub.
Tai galite padaryti naudodami komandą `AI Toolkit: Add Azure Container Apps Job secret for fine-tuning`. Naudodami šią komandą, galite nustatyti slaptumo pavadinimą kaip [`HF_TOKEN`](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables#hftoken) ir naudoti savo Hugging Face tokeną kaip slaptumo reikšmę.

### Paleisti pritaikymą
Norėdami pradėti nuotolinį pritaikymo darbą, paleiskite komandą `AI Toolkit: Run fine-tuning`.

Norėdami peržiūrėti sistemos ir konsolės žurnalus, galite apsilankyti Azure portale naudodami nuorodą išvesties skydelyje (daugiau žingsnių rasite [Peržiūrėti ir užklausų žurnalus Azure](https://aka.ms/ai-toolkit/remote-provision#view-and-query-logs-on-azure)). Arba galite peržiūrėti konsolės žurnalus tiesiogiai VSCode išvesties skydelyje, paleisdami komandą `AI Toolkit: Show the running fine-tuning job streaming logs`. 
> **Pastaba:** Darbas gali būti eilėje dėl nepakankamų resursų. Jei žurnalas nerodomas, paleiskite komandą `AI Toolkit: Show the running fine-tuning job streaming logs`, palaukite šiek tiek laiko ir tada paleiskite komandą dar kartą, kad vėl prisijungtumėte prie srautinio žurnalo.

Šio proceso metu QLoRA bus naudojamas pritaikymui ir sukurs LoRA adapterius, kuriuos modelis naudos inferencijos metu.
Pritaikymo rezultatai bus saugomi Azure Files.

### Inferencijos taško paruošimas
Po to, kai adapteriai yra apmokyti nuotolinėje aplinkoje, naudokite paprastą Gradio programą, kad sąveikautumėte su modeliu.
Panašiai kaip pritaikymo procesas, jums reikia nustatyti Azure resursus nuotolinei inferencijai, paleidžiant `AI Toolkit: Provision Azure Container Apps for inference` iš komandų paletės.

Pagal numatytuosius nustatymus prenumerata ir resursų grupė inferencijai turėtų sutapti su tais, kurie buvo naudojami pritaikymui. Inferencija naudos tą pačią Azure Container App aplinką ir pasieks modelį bei modelio adapterį, saugomą Azure Files, kurie buvo sukurti pritaikymo metu.

### Inferencijos taško diegimas
Jei norite peržiūrėti inferencijos kodą arba iš naujo įkelti inferencijos modelį, prašome paleisti komandą `AI Toolkit: Deploy for inference`. Tai sinchronizuos jūsų naujausią kodą su Azure Container App ir iš naujo paleis repliką.

Kai diegimas bus sėkmingai baigtas, galite pasiekti inferencijos API spustelėdami "*Go to Inference Endpoint*" mygtuką, rodomą VSCode pranešime. Arba interneto API taško adresą galite rasti `ACA_APP_ENDPOINT` faile `./infra/inference.config.json` ir išvesties skydelyje. Dabar galite įvertinti modelį naudodami šį tašką.

### Išplėstinis naudojimas
Daugiau informacijos apie nuotolinį kūrimą su AI Toolkit rasite dokumentacijoje [Nuotolinis modelių pritaikymas](https://aka.ms/ai-toolkit/remote-provision) ir [Inferencija su pritaikytu modeliu](https://aka.ms/ai-toolkit/remote-inference).

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.