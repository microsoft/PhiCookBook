<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c2bc0950f44919ac75a88c1a871680c2",
  "translation_date": "2025-10-11T11:41:28+00:00",
  "source_file": "md/03.FineTuning/Finetuning_VSCodeaitoolkit.md",
  "language_code": "et"
}
-->
## Tere tulemast AI Toolkit'i VS Code'i jaoks

[AI Toolkit VS Code'i jaoks](https://github.com/microsoft/vscode-ai-toolkit/tree/main) ühendab erinevaid mudeleid Azure AI Studio kataloogist ja teistest kataloogidest, nagu Hugging Face. Tööriistakomplekt lihtsustab generatiivsete AI tööriistade ja mudelitega AI rakenduste arendamise tavapäraseid ülesandeid:
- Alustage mudelite avastamise ja mänguväljakuga.
- Mudelite peenhäälestamine ja järeldamine kohalike arvutusressursside abil.
- Kaugpeenhäälestamine ja järeldamine Azure'i ressursside abil.

[Paigalda AI Toolkit VS Code'i jaoks](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

![AIToolkit FineTuning](../../../../imgs/03/intro/Aitoolkit.png)

**[Privaatne eelvaade]** Ühe klõpsuga Azure Container Apps'i ettevalmistamine mudelite peenhäälestamiseks ja järeldamiseks pilves.

Nüüd alustame teie AI rakenduse arendamist:

- [Tere tulemast AI Toolkit'i VS Code'i jaoks](../../../../md/03.FineTuning)
- [Kohalik arendus](../../../../md/03.FineTuning)
  - [Ettevalmistused](../../../../md/03.FineTuning)
  - [Conda aktiveerimine](../../../../md/03.FineTuning)
  - [Ainult baasmudeli peenhäälestamine](../../../../md/03.FineTuning)
  - [Mudeli peenhäälestamine ja järeldamine](../../../../md/03.FineTuning)
  - [Mudeli peenhäälestamine](../../../../md/03.FineTuning)
  - [Microsoft Olive](../../../../md/03.FineTuning)
  - [Peenhäälestamise näited ja ressursid](../../../../md/03.FineTuning)
- [**\[Privaatne eelvaade\]** Kaugarendus](../../../../md/03.FineTuning)
  - [Eeltingimused](../../../../md/03.FineTuning)
  - [Kaugarendusprojekti seadistamine](../../../../md/03.FineTuning)
  - [Azure'i ressursside ettevalmistamine](../../../../md/03.FineTuning)
  - [\[Valikuline\] Huggingface'i tokeni lisamine Azure Container App'i salajasse](../../../../md/03.FineTuning)
  - [Peenhäälestamise käivitamine](../../../../md/03.FineTuning)
  - [Järeldamise lõpp-punkti ettevalmistamine](../../../../md/03.FineTuning)
  - [Järeldamise lõpp-punkti juurutamine](../../../../md/03.FineTuning)
  - [Täiustatud kasutamine](../../../../md/03.FineTuning)

## Kohalik arendus
### Ettevalmistused

1. Veenduge, et NVIDIA draiver on hostis installitud.
2. Käivitage `huggingface-cli login`, kui kasutate HF-i andmekogumite kasutamiseks.
3. `Olive` võtmesätete selgitused, mis muudavad mälukasutust.

### Conda aktiveerimine
Kuna kasutame WSL-i keskkonda ja see on jagatud, peate Conda keskkonna käsitsi aktiveerima. Pärast seda sammu saate käivitada peenhäälestamise või järeldamise.

```bash
conda activate [conda-env-name] 
```

### Ainult baasmudeli peenhäälestamine
Kui soovite lihtsalt baasmudelit proovida ilma peenhäälestamiseta, saate pärast Conda aktiveerimist käivitada järgmise käsu.

```bash
cd inference

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://0.0.0.0:7860) in a browser after gradio initiates the connections.
python gradio_chat.py --baseonly
```

### Mudeli peenhäälestamine ja järeldamine

Kui tööruum on avatud arenduskonteineris, avage terminal (vaikimisi tee on projekti juur) ja käivitage allolev käsk, et peenhäälestada LLM valitud andmekogumil.

```bash
python finetuning/invoke_olive.py 
```

Kontrollpunktid ja lõplik mudel salvestatakse kausta `models`.

Seejärel käivitage peenhäälestatud mudeliga järeldamine vestluste kaudu `konsoolis`, `veebibrauseris` või `prompt flow's`.

```bash
cd inference

# Console interface.
python console_chat.py

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://127.0.0.1:7860) in a browser after gradio initiates the connections.
python gradio_chat.py
```

`Prompt flow` kasutamiseks VS Code'is vaadake palun seda [Kiirstarti juhendit](https://microsoft.github.io/promptflow/how-to-guides/quick-start.html).

### Mudeli peenhäälestamine

Järgmiseks laadige alla järgmine mudel, sõltuvalt GPU olemasolust teie seadmes.

Kohaliku peenhäälestamise sessiooni alustamiseks QLoRA abil valige mudel, mida soovite meie kataloogist peenhäälestada.
| Platvorm(id) | GPU saadaval | Mudeli nimi | Suurus (GB) |
|---------|---------|--------|--------|
| Windows | Jah | Phi-3-mini-4k-**directml**-int4-awq-block-128-onnx | 2.13GB |
| Linux | Jah | Phi-3-mini-4k-**cuda**-int4-onnx | 2.30GB |
| Windows<br>Linux | Ei | Phi-3-mini-4k-**cpu**-int4-rtn-block-32-acc-level-4-onnx | 2.72GB |

**_Märkus_** Azure'i kontot ei ole vaja mudelite allalaadimiseks.

Phi3-mini (int4) mudel on umbes 2GB-3GB suurune. Sõltuvalt teie võrgu kiirusest võib allalaadimine võtta paar minutit.

Alustage projekti nime ja asukoha valimisega.
Seejärel valige mudel mudelikataloogist. Teile kuvatakse projekti malli allalaadimise teade. Seejärel saate klõpsata "Configure Project", et kohandada erinevaid seadeid.

### Microsoft Olive 

Me kasutame [Olive](https://microsoft.github.io/Olive/why-olive.html), et käivitada QLoRA peenhäälestamine PyTorch mudelil meie kataloogist. Kõik seaded on vaikimisi optimeeritud, et peenhäälestamise protsess kohapeal mälukasutust optimeerides käivitada, kuid neid saab kohandada vastavalt teie vajadustele.

### Peenhäälestamise näited ja ressursid

- [Peenhäälestamise alustamise juhend](https://learn.microsoft.com/windows/ai/toolkit/toolkit-fine-tune)
- [Peenhäälestamine HuggingFace'i andmekogumiga](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-hf-dataset.md)
- [Peenhäälestamine lihtsa andmekogumiga](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-simple-dataset.md)

## **[Privaatne eelvaade]** Kaugarendus

### Eeltingimused

1. Mudeli peenhäälestamiseks teie kaug Azure Container App keskkonnas veenduge, et teie tellimusel on piisav GPU maht. Esitage [toetuspilet](https://azure.microsoft.com/support/create-ticket/), et taotleda vajalikku mahtu teie rakenduse jaoks. [Lisateave GPU mahu kohta](https://learn.microsoft.com/azure/container-apps/workload-profiles-overview)
2. Kui kasutate HuggingFace'i privaatset andmekogumit, veenduge, et teil on [HuggingFace'i konto](https://huggingface.co/?WT.mc_id=aiml-137032-kinfeylo) ja [genereerige juurdepääsutoken](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=aiml-137032-kinfeylo)
3. Lubage AI Toolkit'i jaoks VS Code'is kaugpeenhäälestamise ja järeldamise funktsioonilipp:
   1. Avage VS Code'i seaded, valides *File -> Preferences -> Settings*.
   2. Navigeerige *Extensions* ja valige *AI Toolkit*.
   3. Valige *"Enable Remote Fine-tuning And Inference"* valik.
   4. Laadige VS Code uuesti, et muudatus jõustuks.

- [Kaugpeenhäälestamine](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/remote-finetuning.md)

### Kaugarendusprojekti seadistamine
1. Käivitage käsupalett `AI Toolkit: Focus on Resource View`.
2. Navigeerige *Model Fine-tuning*, et pääseda mudelikataloogi. Määrake oma projektile nimi ja valige selle asukoht oma masinas. Seejärel vajutage *"Configure Project"* nuppu.
3. Projekti konfiguratsioon:
    1. Vältige *"Fine-tune locally"* valiku lubamist.
    2. Olive'i konfiguratsiooniseaded kuvatakse eelmääratud vaikeseadetega. Kohandage ja täitke need konfiguratsioonid vastavalt vajadusele.
    3. Jätkake *Generate Project*. See etapp kasutab WSL-i ja hõlmab uue Conda keskkonna seadistamist, valmistudes tulevasteks uuendusteks, mis hõlmavad arenduskonteinereid.
4. Klõpsake *"Relaunch Window In Workspace"*, et avada oma kaugarendusprojekt.

> **Märkus:** Projekt töötab praegu kas kohapeal või kaugkeskkonnas AI Toolkit'i jaoks VS Code'is. Kui valite projekti loomisel *"Fine-tune locally"*, töötab see ainult WSL-is ilma kaugkeskkonna arendusvõimalusteta. Kui te ei luba *"Fine-tune locally"*, on projekt piiratud kaug Azure Container App keskkonnaga.

### Azure'i ressursside ettevalmistamine
Alustamiseks peate ette valmistama Azure'i ressursi kaugpeenhäälestamiseks. Tehke seda, käivitades käsupaletist `AI Toolkit: Provision Azure Container Apps job for fine-tuning`.

Jälgige ettevalmistamise edenemist väljundkanalis kuvatud lingi kaudu.

### [Valikuline] Huggingface'i tokeni lisamine Azure Container App'i salajasse
Kui kasutate HuggingFace'i privaatset andmekogumit, seadke oma HuggingFace'i token keskkonnamuutujana, et vältida vajadust HuggingFace'i hubis käsitsi sisse logida.
Seda saate teha käsuga `AI Toolkit: Add Azure Container Apps Job secret for fine-tuning`. Selle käsuga saate määrata salajase nimeks [`HF_TOKEN`](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables#hftoken) ja kasutada oma HuggingFace'i tokenit salajase väärtusena.

### Peenhäälestamise käivitamine
Kaugpeenhäälestamise töö käivitamiseks käivitage käsk `AI Toolkit: Run fine-tuning`.

Süsteemi ja konsooliloge saate vaadata Azure'i portaalis, kasutades väljundpaneelil kuvatud linki (rohkem samme leiate [Vaata ja päringuloge Azure'is](https://aka.ms/ai-toolkit/remote-provision#view-and-query-logs-on-azure)). Või saate konsooliloge otse VSCode'i väljundpaneelil vaadata, käivitades käsu `AI Toolkit: Show the running fine-tuning job streaming logs`. 
> **Märkus:** Töö võib olla järjekorras ressursside puudumise tõttu. Kui logi ei kuvata, käivitage käsk `AI Toolkit: Show the running fine-tuning job streaming logs`, oodake mõnda aega ja käivitage käsk uuesti, et voogesituslogiga uuesti ühendust luua.

Selle protsessi käigus kasutatakse QLoRA-d peenhäälestamiseks ja luuakse LoRA adapterid, mida mudel kasutab järeldamise ajal.
Peenhäälestamise tulemused salvestatakse Azure Files'i.

### Järeldamise lõpp-punkti ettevalmistamine
Pärast adapterite treenimist kaugkeskkonnas kasutage mudeliga suhtlemiseks lihtsat Gradio rakendust.
Sarnaselt peenhäälestamise protsessile peate kaugjäreldamiseks Azure'i ressursid seadistama, käivitades käsupaletist `AI Toolkit: Provision Azure Container Apps for inference`.

Vaikimisi peaks tellimus ja ressursigrupp järeldamiseks vastama peenhäälestamiseks kasutatutele. Järeldamine kasutab sama Azure Container App keskkonda ja pääseb juurde mudelile ja mudeli adapterile, mis salvestati Azure Files'i, mis genereeriti peenhäälestamise etapis.

### Järeldamise lõpp-punkti juurutamine
Kui soovite järeldamiskoodi muuta või järeldamismudelit uuesti laadida, käivitage käsk `AI Toolkit: Deploy for inference`. See sünkroonib teie viimase koodi Azure Container App'iga ja taaskäivitab replika.  

Kui juurutamine on edukalt lõpule viidud, saate järeldamise API-le juurde pääseda, klõpsates VSCode'i teates kuvatud "*Go to Inference Endpoint*" nuppu. Või leiate veebirakenduse API lõpp-punkti `ACA_APP_ENDPOINT` alt failis `./infra/inference.config.json` ja väljundpaneelil. Nüüd olete valmis mudelit selle lõpp-punkti kaudu hindama.

### Täiustatud kasutamine
Lisateabe saamiseks AI Toolkit'i kaugarenduse kohta vaadake dokumentatsiooni [Mudelite peenhäälestamine kaugkeskkonnas](https://aka.ms/ai-toolkit/remote-provision) ja [Järeldamine peenhäälestatud mudeliga](https://aka.ms/ai-toolkit/remote-inference).

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.