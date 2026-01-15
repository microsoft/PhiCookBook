<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c2bc0950f44919ac75a88c1a871680c2",
  "translation_date": "2025-07-17T09:14:28+00:00",
  "source_file": "md/03.FineTuning/Finetuning_VSCodeaitoolkit.md",
  "language_code": "no"
}
-->
## Velkommen til AI Toolkit for VS Code

[AI Toolkit for VS Code](https://github.com/microsoft/vscode-ai-toolkit/tree/main) samler ulike modeller fra Azure AI Studio Catalog og andre kataloger som Hugging Face. Toolkit-en forenkler vanlige utviklingsoppgaver for å bygge AI-apper med generative AI-verktøy og modeller gjennom:
- Kom i gang med modellutforskning og lekeplass.
- Modellfinjustering og inferens ved bruk av lokale datamaskinressurser.
- Fjernfinjustering og inferens ved bruk av Azure-ressurser

[Installer AI Toolkit for VSCode](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

![AIToolkit FineTuning](../../../../translated_images/no/Aitoolkit.7157953df04812dc.png)


**[Private Preview]** Én-klikk provisjonering for Azure Container Apps for å kjøre modellfinjustering og inferens i skyen.

La oss nå hoppe rett inn i utviklingen av din AI-app:

- [Velkommen til AI Toolkit for VS Code](../../../../md/03.FineTuning)
- [Lokal utvikling](../../../../md/03.FineTuning)
  - [Forberedelser](../../../../md/03.FineTuning)
  - [Aktiver Conda](../../../../md/03.FineTuning)
  - [Kun finjustering av basismodell](../../../../md/03.FineTuning)
  - [Modellfinjustering og inferens](../../../../md/03.FineTuning)
  - [Modellfinjustering](../../../../md/03.FineTuning)
  - [Microsoft Olive](../../../../md/03.FineTuning)
  - [Eksempler og ressurser for finjustering](../../../../md/03.FineTuning)
- [**\[Private Preview\]** Fjernutvikling](../../../../md/03.FineTuning)
  - [Forutsetninger](../../../../md/03.FineTuning)
  - [Sette opp et fjernutviklingsprosjekt](../../../../md/03.FineTuning)
  - [Provisionere Azure-ressurser](../../../../md/03.FineTuning)
  - [\[Valgfritt\] Legg til Huggingface-token i Azure Container App Secret](../../../../md/03.FineTuning)
  - [Kjør finjustering](../../../../md/03.FineTuning)
  - [Provisionere inferens-endepunkt](../../../../md/03.FineTuning)
  - [Distribuer inferens-endepunkt](../../../../md/03.FineTuning)
  - [Avansert bruk](../../../../md/03.FineTuning)

## Lokal utvikling
### Forberedelser

1. Sørg for at NVIDIA-driveren er installert på vertsmaskinen.  
2. Kjør `huggingface-cli login` hvis du bruker HF for datasettnyttelse  
3. Forklaringer på `Olive`-nøkkelinnstillinger for alt som påvirker minnebruk.

### Aktiver Conda
Siden vi bruker WSL-miljø og det deles, må du manuelt aktivere conda-miljøet. Etter dette kan du kjøre finjustering eller inferens.

```bash
conda activate [conda-env-name] 
```

### Kun finjustering av basismodell
For å bare prøve basismodellen uten finjustering kan du kjøre denne kommandoen etter å ha aktivert conda.

```bash
cd inference

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://0.0.0.0:7860) in a browser after gradio initiates the connections.
python gradio_chat.py --baseonly
```

### Modellfinjustering og inferens

Når arbeidsområdet er åpnet i en dev container, åpne et terminalvindu (standardbane er prosjektets rotmappe), og kjør deretter kommandoen under for å finjustere en LLM på det valgte datasettet.

```bash
python finetuning/invoke_olive.py 
```

Sjekkpunkter og endelig modell lagres i `models`-mappen.

Kjør deretter inferens med den finjusterte modellen via chat i en `konsoll`, `nettleser` eller `prompt flow`.

```bash
cd inference

# Console interface.
python console_chat.py

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://127.0.0.1:7860) in a browser after gradio initiates the connections.
python gradio_chat.py
```

For å bruke `prompt flow` i VS Code, se denne [Quick Start](https://microsoft.github.io/promptflow/how-to-guides/quick-start.html).

### Modellfinjustering

Last ned modellen nedenfor avhengig av om du har GPU tilgjengelig på enheten din.

For å starte en lokal finjusteringsøkt med QLoRA, velg en modell du ønsker å finjustere fra katalogen vår.
| Plattform(er) | GPU tilgjengelig | Modellnavn | Størrelse (GB) |
|---------|---------|--------|--------|
| Windows | Ja | Phi-3-mini-4k-**directml**-int4-awq-block-128-onnx | 2.13GB |
| Linux | Ja | Phi-3-mini-4k-**cuda**-int4-onnx | 2.30GB |
| Windows<br>Linux | Nei | Phi-3-mini-4k-**cpu**-int4-rtn-block-32-acc-level-4-onnx | 2.72GB |

**_Merk_** Du trenger ikke en Azure-konto for å laste ned modellene

Phi3-mini (int4)-modellen er omtrent 2GB-3GB stor. Avhengig av nettverkshastigheten kan nedlastingen ta noen minutter.

Start med å velge et prosjektnavn og plassering.  
Deretter velger du en modell fra modellkatalogen. Du vil bli bedt om å laste ned prosjektmalen. Klikk deretter på "Configure Project" for å justere ulike innstillinger.

### Microsoft Olive

Vi bruker [Olive](https://microsoft.github.io/Olive/why-olive.html) for å kjøre QLoRA finjustering på en PyTorch-modell fra katalogen vår. Alle innstillinger er forhåndsdefinert med standardverdier for å optimalisere kjøringen av finjusteringsprosessen lokalt med effektiv minnebruk, men de kan justeres etter ditt scenario.

### Eksempler og ressurser for finjustering

- [Kom i gang med finjustering](https://learn.microsoft.com/windows/ai/toolkit/toolkit-fine-tune)
- [Finjustering med et HuggingFace-datasett](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-hf-dataset.md)
- [Finjustering med Simple DataSet](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-simple-dataset.md)

## **[Private Preview]** Fjernutvikling

### Forutsetninger

1. For å kjøre modellfinjustering i ditt eksterne Azure Container App-miljø, sørg for at abonnementet ditt har nok GPU-kapasitet. Send inn en [supporthenvendelse](https://azure.microsoft.com/support/create-ticket/) for å be om nødvendig kapasitet for applikasjonen din. [Mer info om GPU-kapasitet](https://learn.microsoft.com/azure/container-apps/workload-profiles-overview)  
2. Hvis du bruker private datasett på HuggingFace, sørg for at du har en [HuggingFace-konto](https://huggingface.co/?WT.mc_id=aiml-137032-kinfeylo) og [generer et tilgangstoken](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=aiml-137032-kinfeylo)  
3. Aktiver funksjonsflagget for fjernfinjustering og inferens i AI Toolkit for VS Code  
   1. Åpne VS Code-innstillinger via *File -> Preferences -> Settings*.  
   2. Gå til *Extensions* og velg *AI Toolkit*.  
   3. Velg alternativet *"Enable Remote Fine-tuning And Inference"*.  
   4. Last inn VS Code på nytt for at endringen skal tre i kraft.

- [Fjernfinjustering](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/remote-finetuning.md)

### Sette opp et fjernutviklingsprosjekt
1. Kjør kommando-paletten `AI Toolkit: Focus on Resource View`.  
2. Naviger til *Model Fine-tuning* for å få tilgang til modellkatalogen. Gi prosjektet ditt et navn og velg plassering på maskinen din. Klikk deretter på *"Configure Project"*.  
3. Prosjektkonfigurasjon  
    1. Ikke aktiver *"Fine-tune locally"*.  
    2. Olive-konfigurasjonsinnstillingene vises med forhåndsdefinerte standardverdier. Juster og fyll ut disse etter behov.  
    3. Gå videre til *Generate Project*. Dette trinnet bruker WSL og setter opp et nytt Conda-miljø, som forbereder for fremtidige oppdateringer med Dev Containers.  
4. Klikk på *"Relaunch Window In Workspace"* for å åpne ditt fjernutviklingsprosjekt.

> **Merk:** Prosjektet fungerer for øyeblikket enten lokalt eller eksternt innen AI Toolkit for VS Code. Hvis du velger *"Fine-tune locally"* under prosjektopprettelsen, vil det kun fungere i WSL uten fjernutviklingsmuligheter. Hvis du ikke aktiverer *"Fine-tune locally"*, vil prosjektet være begrenset til det eksterne Azure Container App-miljøet.

### Provisionere Azure-ressurser
For å komme i gang må du provisionere Azure-ressursen for fjernfinjustering. Kjør `AI Toolkit: Provision Azure Container Apps job for fine-tuning` fra kommando-paletten.

Følg fremdriften for provisjoneringen via lenken som vises i output-kanalen.

### [Valgfritt] Legg til Huggingface-token i Azure Container App Secret
Hvis du bruker private HuggingFace-datasett, sett HuggingFace-tokenet ditt som en miljøvariabel for å unngå manuell innlogging på Hugging Face Hub.  
Dette kan du gjøre med kommandoen `AI Toolkit: Add Azure Container Apps Job secret for fine-tuning`. Med denne kommandoen kan du sette hemmelighetsnavnet til [`HF_TOKEN`](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables#hftoken) og bruke HuggingFace-tokenet ditt som hemmelighetsverdi.

### Kjør finjustering
For å starte den eksterne finjusteringsjobben, kjør kommandoen `AI Toolkit: Run fine-tuning`.

For å se system- og konsolllogger kan du besøke Azure-portalen via lenken i output-panelet (flere steg i [View and Query Logs on Azure](https://aka.ms/ai-toolkit/remote-provision#view-and-query-logs-on-azure)). Du kan også se konsolllogger direkte i VSCode output-panelet ved å kjøre kommandoen `AI Toolkit: Show the running fine-tuning job streaming logs`.  
> **Merk:** Jobben kan være i kø på grunn av utilstrekkelige ressurser. Hvis loggen ikke vises, kjør `AI Toolkit: Show the running fine-tuning job streaming logs` på nytt etter en stund for å koble til strømmen igjen.

Under denne prosessen brukes QLoRA for finjustering, og det opprettes LoRA-adaptere for modellen som brukes under inferens.  
Resultatene av finjusteringen lagres i Azure Files.

### Provisionere inferens-endepunkt
Etter at adapterne er trent i det eksterne miljøet, bruk en enkel Gradio-applikasjon for å samhandle med modellen.  
På samme måte som for finjustering må du sette opp Azure-ressurser for fjerninferens ved å kjøre `AI Toolkit: Provision Azure Container Apps for inference` fra kommando-paletten.

Som standard bør abonnement og ressursgruppe for inferens samsvare med de som brukes for finjustering. Inferensen vil bruke samme Azure Container App-miljø og få tilgang til modellen og modelladapteren som er lagret i Azure Files, og som ble generert under finjusteringssteget.

### Distribuer inferens-endepunkt
Hvis du ønsker å endre inferenskoden eller laste inn inferensmodellen på nytt, kjør kommandoen `AI Toolkit: Deploy for inference`. Dette synkroniserer din nyeste kode med Azure Container App og starter replikaen på nytt.

Når distribusjonen er fullført, kan du få tilgang til inferens-API-en ved å klikke på "*Go to Inference Endpoint*" knappen som vises i VSCode-varslingen. Alternativt finner du web-API-endepunktet under `ACA_APP_ENDPOINT` i `./infra/inference.config.json` og i output-panelet. Du er nå klar til å evaluere modellen ved hjelp av dette endepunktet.

### Avansert bruk
For mer informasjon om fjernutvikling med AI Toolkit, se dokumentasjonen for [Finjustering av modeller eksternt](https://aka.ms/ai-toolkit/remote-provision) og [Inferens med den finjusterte modellen](https://aka.ms/ai-toolkit/remote-inference).

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.