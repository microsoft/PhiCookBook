# **Phi-3 kasutamine Microsoft Foundry's**

Generatiivse tehisintellekti arendamisega loodame kasutada ühtset platvormi erinevate LLM-ide ja SLM-ide, ettevõtte andmete integreerimise, peenhäälestuse/RAG-operatsioonide ja integreeritud LLM-ide ning SLM-ide põhjal erinevate ettevõtete äriprotsesside hindamise juhtimiseks, et generatiivne tehisintellekt saaks nutikaid rakendusi paremini ellu viia. [Microsoft Foundry](https://ai.azure.com) on ettevõtte tasemel generatiivse AI rakendusplatvorm.

![aistudo](../../../../translated_images/et/aifoundry_home.f28a8127c96c7d93.webp)

Microsoft Foundry abil saate hinnata suure keelemudeli (LLM) vastuseid ja orkestreerida käsklusrakenduse komponente prompt flow abil parema jõudluse saavutamiseks. Platvorm soodustab skaleeritavust, võimaldades hõlpsasti muuta kontseptsioonide prototüüpe täieulatuslikeks tootearendusteks. Järjepidev jälgimine ja täiustamine toetavad pikaajalist edu.

Saame Phi-3 mudeli Microsoft Foundry’s kiiresti juurutada lihtsate sammude abil ning seejärel kasutada Microsoft Foundry’d Phi-3 PlayGround/Chat, peenhäälestuse, hindamise ja muude seotud tööde tegemiseks.

## **1. Valmistumine**

Kui sul on juba [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) installitud sinu masinas, on selle malliga alustamine sama lihtne kui selle käsu käivitamine uues kataloogis.

## Käsitsi loomine

Microsoft Foundry projektide ja keskustega organisatsiooni ja oma AI tööde haldamine on suurepärane viis. Siin on samm-sammult juhend alustamiseks:

### Projekti loomine Microsoft Foundry’s

1. **Mine Microsoft Foundry’sse**: Logi sisse Microsoft Foundry portaali.
2. **Loo projekt**:
   - Kui oled juba mõnes projektis, vali lehe vasakus ülanurgas "Microsoft Foundry", et minna avalehele.
   - Vali "+ Create project".
   - Sisesta projekti nimi.
   - Kui sul on olemas keskuse (hub) ligipääs, valitakse see vaikimisi. Kui sul on ligipääs mitmele keskele, saad rippmenüüst valida mõne teise. Kui soovid luua uue keskuse, vali "Create new hub" ja anna sellele nimi.
   - Vali "Create".

### Keskuse loomine Microsoft Foundry’s

1. **Mine Microsoft Foundry’sse**: Logi sisse Azure kontoga.
2. **Loo keskus**:
   - Vali vasakult menüüst Management center.
   - Vali "All resources", seejärel noolega allapoole nupp "+ New project" juures ja vali "+ New hub".
   - Dialoogis "Create a new hub" sisesta oma keskusele nimi (nt contoso-hub) ja vajadusel kohanda teisi välju.
   - Vali "Next", kontrolli infot ja vali "Create".

Detailsemate juhiste jaoks võid vaadata ametlikku [Microsofti dokumentatsiooni](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

Pärast edukat loomist saad loodud stuudiot kasutada aadressil [ai.azure.com](https://ai.azure.com/)

Ühel AI Foundry’l võib olla mitu projekti. Valmista ette AI Foundry’s projekt.

Loo Microsoft Foundry [QuickStarts’id](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)

## **2. Phi mudeli juurutamine Microsoft Foundry’s**

Vali projekti alt Explore valik, et siseneda Model Catalog’i ja vali Phi-3

Vali Phi-3-mini-4k-instruct

Vajuta "Deploy", et juurutada Phi-3-mini-4k-instruct mudel

> [!NOTE]
>
> Juurutamise ajal saad valida arvutusvõimsuse

## **3. Playground Chat Phi Microsoft Foundry’s**

Mine juurutatud mudeli lehele, vali Playground ning suhtle Microsoft Foundry Phi-3 mudeliga

## **4. Mudeli juurutamine Microsoft Foundry’st**

Azur Model Catalog’ist mudeli juurutamiseks järgi neid samme:

- Logi sisse Microsoft Foundry’sse.
- Vali Microsoft Foundry mudelikataloogist oma juurutatav mudel.
- Mudeli detailide lehel vali Deploy ja seejärel vali Serverless API koos Azure AI Content Safety’ga.
- Vali projekt, kuhu soovid mudeli juurutada. Serverless API kasutamiseks peab su töökeskkond asuma East US 2 või Sweden Central regiooni all. Juurutamisnime saad kohandada.
- Juurutamise viisardis vali hinnakujunduse ja tingimuste vaade, et tutvuda kasutustingimuste ja hinnakirjaga.
- Vali Deploy. Oota, kuni juurutus on valmis ning sind suunatakse Deployments lehele.
- Vali “Open in playground”, et alustada mudeliga suhtlemist.
- Võid tagasi tulla Deployments lehele, valida juurutuse ja märgata selle lõpp-punkti Target URL-i ning Secret Key’d, mida kasutada juurutuse kutsumiseks ja tekstide genereerimiseks.
- Lõpp-punkti detailid kui URL ja ligipääsu võtmed on alati leitavad vahekaardilt Build ja komponendi jaotisest Deployments.

> [!NOTE]
> Arvesta, et konto peab omama Azure AI Developer rolliõiguseid Ressursigrupil, et neid samme sooritada.

## **5. Phi API kasutamine Microsoft Foundry’s**

Saad kasutada https://{Sinu projekti nimi}.region.inference.ml.azure.com/swagger.json Postmani GET päringuga ja koos Key-ga uurida pakutavaid liideseid.

Päringuparameetrid ja vastusparameetrid on mugavalt kättesaadavad.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:
See dokument on tõlgitud tehisintellekti tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi me püüame täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta tõlgendamis- või mõistmisvigade eest, mis võivad sellest tõlkest tekkida.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->