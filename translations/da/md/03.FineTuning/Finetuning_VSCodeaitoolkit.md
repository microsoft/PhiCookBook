<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c2bc0950f44919ac75a88c1a871680c2",
  "translation_date": "2025-07-17T09:13:50+00:00",
  "source_file": "md/03.FineTuning/Finetuning_VSCodeaitoolkit.md",
  "language_code": "da"
}
-->
## Velkommen til AI Toolkit for VS Code

[AI Toolkit for VS Code](https://github.com/microsoft/vscode-ai-toolkit/tree/main) samler forskellige modeller fra Azure AI Studio Catalog og andre kataloger som Hugging Face. Toolkit’et forenkler de almindelige udviklingsopgaver til at bygge AI-apps med generative AI-værktøjer og modeller gennem:
- Kom godt i gang med modelopdagelse og playground.
- Model finjustering og inferens ved brug af lokale computerressourcer.
- Fjernfinjustering og inferens ved brug af Azure-ressourcer

[Installer AI Toolkit for VSCode](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

![AIToolkit FineTuning](../../../../translated_images/Aitoolkit.7157953df04812dc.da.png)


**[Private Preview]** Én-klik provisioning til Azure Container Apps for at køre model finjustering og inferens i skyen.

Lad os nu gå i gang med din AI-app udvikling:

- [Velkommen til AI Toolkit for VS Code](../../../../md/03.FineTuning)
- [Lokal udvikling](../../../../md/03.FineTuning)
  - [Forberedelser](../../../../md/03.FineTuning)
  - [Aktivér Conda](../../../../md/03.FineTuning)
  - [Kun finjustering af basismodellen](../../../../md/03.FineTuning)
  - [Model finjustering og inferens](../../../../md/03.FineTuning)
  - [Model finjustering](../../../../md/03.FineTuning)
  - [Microsoft Olive](../../../../md/03.FineTuning)
  - [Eksempler og ressourcer til finjustering](../../../../md/03.FineTuning)
- [**\[Private Preview\]** Fjernudvikling](../../../../md/03.FineTuning)
  - [Forudsætninger](../../../../md/03.FineTuning)
  - [Opsætning af et fjernudviklingsprojekt](../../../../md/03.FineTuning)
  - [Provision af Azure-ressourcer](../../../../md/03.FineTuning)
  - [\[Valgfrit\] Tilføj Huggingface-token til Azure Container App Secret](../../../../md/03.FineTuning)
  - [Kør finjustering](../../../../md/03.FineTuning)
  - [Provision af inferens-endpoint](../../../../md/03.FineTuning)
  - [Deploy inferens-endpoint](../../../../md/03.FineTuning)
  - [Avanceret brug](../../../../md/03.FineTuning)

## Lokal udvikling
### Forberedelser

1. Sørg for, at NVIDIA-driveren er installeret på værten.  
2. Kør `huggingface-cli login`, hvis du bruger HF til dataset-udnyttelse  
3. Forklaringer til `Olive` nøgleindstillinger for alt, der ændrer hukommelsesforbruget.

### Aktivér Conda
Da vi bruger WSL-miljøet, som deles, skal du manuelt aktivere conda-miljøet. Efter dette trin kan du køre finjustering eller inferens.

```bash
conda activate [conda-env-name] 
```

### Kun finjustering af basismodellen
Hvis du bare vil prøve basismodellen uden finjustering, kan du køre denne kommando efter aktivering af conda.

```bash
cd inference

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://0.0.0.0:7860) in a browser after gradio initiates the connections.
python gradio_chat.py --baseonly
```

### Model finjustering og inferens

Når arbejdsområdet er åbnet i en dev container, åbn en terminal (standardstien er projektets rodmappe), og kør derefter kommandoen nedenfor for at finjustere en LLM på det valgte datasæt.

```bash
python finetuning/invoke_olive.py 
```

Checkpoints og den endelige model gemmes i mappen `models`.

Kør derefter inferens med den finjusterede model via chats i en `console`, `webbrowser` eller `prompt flow`.

```bash
cd inference

# Console interface.
python console_chat.py

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://127.0.0.1:7860) in a browser after gradio initiates the connections.
python gradio_chat.py
```

For at bruge `prompt flow` i VS Code, se venligst denne [Quick Start](https://microsoft.github.io/promptflow/how-to-guides/quick-start.html).

### Model finjustering

Download herefter den model, der passer til, om der er en GPU tilgængelig på din enhed.

For at starte en lokal finjusteringssession med QLoRA, vælg en model, du vil finjustere, fra vores katalog.
| Platform(e) | GPU tilgængelig | Modelnavn | Størrelse (GB) |
|---------|---------|--------|--------|
| Windows | Ja | Phi-3-mini-4k-**directml**-int4-awq-block-128-onnx | 2.13GB |
| Linux | Ja | Phi-3-mini-4k-**cuda**-int4-onnx | 2.30GB |
| Windows<br>Linux | Nej | Phi-3-mini-4k-**cpu**-int4-rtn-block-32-acc-level-4-onnx | 2.72GB |

**_Bemærk_** Du behøver ikke en Azure-konto for at downloade modellerne

Phi3-mini (int4) modellen er cirka 2GB-3GB stor. Afhængigt af din netværkshastighed kan det tage et par minutter at downloade.

Start med at vælge et projektnavn og placering.  
Dernæst vælg en model fra modelkataloget. Du vil blive bedt om at downloade projektskabelonen. Du kan derefter klikke på "Configure Project" for at justere forskellige indstillinger.

### Microsoft Olive

Vi bruger [Olive](https://microsoft.github.io/Olive/why-olive.html) til at køre QLoRA finjustering på en PyTorch-model fra vores katalog. Alle indstillinger er forudindstillet med standardværdier for at optimere kørsel af finjusteringsprocessen lokalt med optimeret hukommelsesbrug, men de kan tilpasses til dit scenarie.

### Eksempler og ressourcer til finjustering

- [Guide til at komme i gang med finjustering](https://learn.microsoft.com/windows/ai/toolkit/toolkit-fine-tune)
- [Finjustering med et HuggingFace-datasæt](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-hf-dataset.md)
- [Finjustering med Simple DataSet](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-simple-dataset.md)

## **[Private Preview]** Fjernudvikling

### Forudsætninger

1. For at køre model finjustering i dit fjern-Azure Container App-miljø, skal du sikre, at dit abonnement har nok GPU-kapacitet. Indsend en [supportanmodning](https://azure.microsoft.com/support/create-ticket/) for at få den nødvendige kapacitet til din applikation. [Få mere info om GPU-kapacitet](https://learn.microsoft.com/azure/container-apps/workload-profiles-overview)  
2. Hvis du bruger private datasæt på HuggingFace, skal du have en [HuggingFace-konto](https://huggingface.co/?WT.mc_id=aiml-137032-kinfeylo) og [generere et adgangstoken](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=aiml-137032-kinfeylo)  
3. Aktiver Remote Fine-tuning og Inference feature-flag i AI Toolkit for VS Code  
   1. Åbn VS Code-indstillinger ved at vælge *File -> Preferences -> Settings*.  
   2. Gå til *Extensions* og vælg *AI Toolkit*.  
   3. Vælg *"Enable Remote Fine-tuning And Inference"* optionen.  
   4. Genstart VS Code for at aktivere ændringen.

- [Remote finjustering](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/remote-finetuning.md)

### Opsætning af et fjernudviklingsprojekt
1. Kør kommando-paletten `AI Toolkit: Focus on Resource View`.  
2. Naviger til *Model Fine-tuning* for at få adgang til modelkataloget. Giv dit projekt et navn og vælg dets placering på din maskine. Klik derefter på *"Configure Project"*.  
3. Projektkonfiguration  
    1. Undgå at aktivere *"Fine-tune locally"* optionen.  
    2. Olive-konfigurationsindstillingerne vises med forudindstillede standardværdier. Juster og udfyld disse konfigurationer efter behov.  
    3. Fortsæt til *Generate Project*. Dette trin bruger WSL og sætter et nyt Conda-miljø op, som forbereder til fremtidige opdateringer med Dev Containers.  
4. Klik på *"Relaunch Window In Workspace"* for at åbne dit fjernudviklingsprojekt.

> **Bemærk:** Projektet fungerer i øjeblikket enten lokalt eller fjernstyret inden for AI Toolkit for VS Code. Hvis du vælger *"Fine-tune locally"* under projektoprettelsen, vil det kun køre i WSL uden fjernudviklingsfunktioner. Hvis du derimod ikke aktiverer *"Fine-tune locally"*, vil projektet være begrænset til det fjernstyrede Azure Container App-miljø.

### Provision af Azure-ressourcer
For at komme i gang skal du provisionere Azure-ressourcen til fjernfinjustering. Det gør du ved at køre `AI Toolkit: Provision Azure Container Apps job for fine-tuning` fra kommando-paletten.

Følg fremskridtet for provisioneringen via linket, der vises i outputkanalen.

### [Valgfrit] Tilføj Huggingface-token til Azure Container App Secret
Hvis du bruger private HuggingFace-datasæt, kan du sætte dit HuggingFace-token som en miljøvariabel for at undgå manuel login på Hugging Face Hub.  
Det kan du gøre med kommandoen `AI Toolkit: Add Azure Container Apps Job secret for fine-tuning`. Med denne kommando kan du sætte hemmelighedsnavnet til [`HF_TOKEN`](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables#hftoken) og bruge dit Hugging Face-token som hemmelighedsværdi.

### Kør finjustering
For at starte det fjernstyrede finjusteringsjob, kør kommandoen `AI Toolkit: Run fine-tuning`.

For at se system- og konsollogs kan du besøge Azure-portalen via linket i outputpanelet (flere trin findes under [View and Query Logs on Azure](https://aka.ms/ai-toolkit/remote-provision#view-and-query-logs-on-azure)). Alternativt kan du se konsollogs direkte i VSCode’s outputpanel ved at køre kommandoen `AI Toolkit: Show the running fine-tuning job streaming logs`.  
> **Bemærk:** Jobbet kan være i kø på grund af utilstrækkelige ressourcer. Hvis loggen ikke vises, kør da `AI Toolkit: Show the running fine-tuning job streaming logs` kommandoen, vent lidt og kør den igen for at genoprette forbindelsen til streamingloggen.

Under processen vil QLoRA blive brugt til finjustering og oprette LoRA-adaptere til modellen, som bruges under inferens.  
Resultaterne af finjusteringen gemmes i Azure Files.

### Provision af inferens-endpoint
Når adapterne er trænet i det fjernstyrede miljø, kan du bruge en simpel Gradio-applikation til at interagere med modellen.  
Ligesom ved finjustering skal du opsætte Azure-ressourcer til fjerninferens ved at køre `AI Toolkit: Provision Azure Container Apps for inference` fra kommando-paletten.

Som standard bør abonnement og ressourcegruppe til inferens matche dem, der bruges til finjustering. Inferensen vil bruge det samme Azure Container App-miljø og få adgang til modellen og modeladapteren, som er gemt i Azure Files og blev genereret under finjusteringstrinnet.

### Deploy inferens-endpoint
Hvis du ønsker at ændre inferenskoden eller genindlæse inferensmodellen, skal du køre kommandoen `AI Toolkit: Deploy for inference`. Dette vil synkronisere din seneste kode med Azure Container App og genstarte replikaen.

Når deployment er gennemført med succes, kan du få adgang til inferens-API’en ved at klikke på knappen "*Go to Inference Endpoint*" i VSCode-notifikationen. Alternativt kan web-API-endpointet findes under `ACA_APP_ENDPOINT` i `./infra/inference.config.json` og i outputpanelet. Du er nu klar til at evaluere modellen via dette endpoint.

### Avanceret brug
For mere information om fjernudvikling med AI Toolkit, se dokumentationen om [Finjustering af modeller fjernstyret](https://aka.ms/ai-toolkit/remote-provision) og [Inferens med den finjusterede model](https://aka.ms/ai-toolkit/remote-inference).

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.