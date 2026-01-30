# **Phi-3 kasutamine Azure AI Foundry platvormil**

Generatiivse tehisintellekti arendamisega loodame kasutada ühtset platvormi, et hallata erinevaid LLM- ja SLM-mudeleid, integreerida ettevõtte andmeid, teostada peenhäälestamist/RAG-operatsioone ning hinnata erinevate ettevõtete tegevusi pärast LLM- ja SLM-mudelite integreerimist. See võimaldab generatiivsel tehisintellektil paremini rakenduda nutikates lahendustes. [Azure AI Foundry](https://ai.azure.com) on ettevõtte tasemel generatiivse tehisintellekti rakendusplatvorm.

![aistudo](../../../../imgs/01/02/03/aifoundry_home.png)

Azure AI Foundry abil saate hinnata suurte keelemudelite (LLM) vastuseid ja korraldada prompt flow abil rakenduste komponente, et saavutada paremat jõudlust. Platvorm toetab mastaapsust, muutes kontseptsioonide tõestamise täisfunktsionaalseks tootmiseks lihtsaks. Pidev jälgimine ja täiustamine tagavad pikaajalise edu.

Phi-3 mudeli saab Azure AI Foundry platvormil kiiresti juurutada lihtsate sammude abil ning seejärel kasutada platvormi Phi-3 seotud Playground/Chat, peenhäälestamise, hindamise ja muude tööde teostamiseks.

## **1. Ettevalmistus**

Kui teie arvutisse on juba installitud [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo), on selle malli kasutamine sama lihtne kui käivitada vastav käsk uues kataloogis.

## Käsitsi loomine

Microsoft Azure AI Foundry projekti ja hubi loomine on suurepärane viis oma tehisintellekti töö korraldamiseks ja haldamiseks. Siin on samm-sammuline juhend alustamiseks:

### Projekti loomine Azure AI Foundry platvormil

1. **Minge Azure AI Foundry lehele**: Logige sisse Azure AI Foundry portaalis.
2. **Looge projekt**:
   - Kui olete projektis, valige lehe vasakust ülanurgast "Azure AI Foundry", et minna avalehele.
   - Valige "+ Create project".
   - Sisestage projekti nimi.
   - Kui teil on hub, valitakse see vaikimisi. Kui teil on juurdepääs mitmele hubile, saate valida rippmenüüst teise. Kui soovite luua uue hubi, valige "Create new hub" ja sisestage nimi.
   - Valige "Create".

### Hubi loomine Azure AI Foundry platvormil

1. **Minge Azure AI Foundry lehele**: Logige sisse oma Azure kontoga.
2. **Looge hub**:
   - Valige vasakmenüüst "Management center".
   - Valige "All resources", seejärel klõpsake "+ New project" kõrval olevat noolt ja valige "+ New hub".
   - "Create a new hub" dialoogis sisestage hubi nimi (nt contoso-hub) ja muutke teisi välju vastavalt soovile.
   - Valige "Next", vaadake teave üle ja seejärel valige "Create".

Täpsemate juhiste saamiseks vaadake ametlikku [Microsofti dokumentatsiooni](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

Pärast edukat loomist pääsete loodud stuudiole ligi aadressil [ai.azure.com](https://ai.azure.com/)

Ühel AI Foundry platvormil võib olla mitu projekti. Looge AI Foundry platvormil projekt ettevalmistuseks.

Looge Azure AI Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)

## **2. Phi mudeli juurutamine Azure AI Foundry platvormil**

Klõpsake projekti Explore valikut, et siseneda Model Catalog lehele ja valige Phi-3.

Valige Phi-3-mini-4k-instruct.

Klõpsake 'Deploy', et juurutada Phi-3-mini-4k-instruct mudel.

> [!NOTE]
>
> Juurutamisel saate valida arvutusvõimsuse.

## **3. Playground Chat Phi Azure AI Foundry platvormil**

Minge juurutamise lehele, valige Playground ja vestelge Azure AI Foundry Phi-3 mudeliga.

## **4. Mudeli juurutamine Azure AI Foundry platvormilt**

Mudeli juurutamiseks Azure Model Catalog kaudu järgige neid samme:

- Logige sisse Azure AI Foundry platvormil.
- Valige mudel, mida soovite juurutada, Azure AI Foundry mudelikataloogist.
- Mudeli Details lehel valige Deploy ja seejärel Serverless API koos Azure AI Content Safety-ga.
- Valige projekt, kuhu soovite mudeli juurutada. Serverless API kasutamiseks peab teie tööruum kuuluma East US 2 või Sweden Central piirkonda. Saate kohandada juurutamise nime.
- Juurutamise viisardis valige Pricing and terms, et tutvuda hinna ja kasutustingimustega.
- Valige Deploy. Oodake, kuni juurutamine on valmis ja teid suunatakse Deployments lehele.
- Valige Open in playground, et alustada mudeliga suhtlemist.
- Võite naasta Deployments lehele, valida juurutuse ja märkida üles siht-URL-i ja salajase võtme, mida saate kasutada juurutuse kutsumiseks ja tulemuste genereerimiseks.
- Juurutuse üksikasju, URL-i ja juurdepääsuvõtmeid leiate alati Build vahekaardilt, valides Components sektsioonist Deployments.

> [!NOTE]
> Pange tähele, et teie kontol peab olema Azure AI Developer rolli õigused Resource Groupis, et neid samme teostada.

## **5. Phi API kasutamine Azure AI Foundry platvormil**

Saate Postman GET kaudu ligi aadressile https://{Teie projekti nimi}.region.inference.ml.azure.com/swagger.json ja kombineerida selle Key-ga, et tutvuda pakutavate liidestega.

Saate väga mugavalt kätte päringuparameetrid ja vastuseparameetrid.

---

**Lahtiütlus**:  
See dokument on tõlgitud, kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algkeeles tuleks lugeda autoriteetseks allikaks. Olulise teabe puhul on soovitatav kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valede tõlgenduste eest.