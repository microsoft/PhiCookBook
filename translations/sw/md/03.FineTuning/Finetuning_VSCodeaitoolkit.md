<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c2bc0950f44919ac75a88c1a871680c2",
  "translation_date": "2025-07-17T09:18:37+00:00",
  "source_file": "md/03.FineTuning/Finetuning_VSCodeaitoolkit.md",
  "language_code": "sw"
}
-->
## Karibu kwenye AI Toolkit kwa VS Code

[AI Toolkit kwa VS Code](https://github.com/microsoft/vscode-ai-toolkit/tree/main) huleta pamoja mifano mbalimbali kutoka Azure AI Studio Catalog na katalogi nyingine kama Hugging Face. Kitengo hiki hurahisisha kazi za kawaida za maendeleo kwa kujenga programu za AI kwa kutumia zana na mifano ya AI inayozalisha kupitia:
- Anza na ugunduzi wa modeli na uwanja wa majaribio.
- Urekebishaji wa modeli na utambuzi kwa kutumia rasilimali za kompyuta za ndani.
- Urekebishaji wa mbali na utambuzi kwa kutumia rasilimali za Azure

[Sakinisha AI Toolkit kwa VSCode](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

![AIToolkit FineTuning](../../../../translated_images/Aitoolkit.7157953df04812dc.sw.png)


**[Private Preview]** Utoaji kwa bonyeza moja kwa Azure Container Apps kuendesha urekebishaji wa modeli na utambuzi katika wingu.

Sasa tuanze na maendeleo ya programu yako ya AI:

- [Karibu kwenye AI Toolkit kwa VS Code](../../../../md/03.FineTuning)
- [Maendeleo ya Ndani](../../../../md/03.FineTuning)
  - [Maandalizi](../../../../md/03.FineTuning)
  - [Washa Conda](../../../../md/03.FineTuning)
  - [Urekebishaji wa modeli msingi tu](../../../../md/03.FineTuning)
  - [Urekebishaji wa modeli na utambuzi](../../../../md/03.FineTuning)
  - [Urekebishaji wa Modeli](../../../../md/03.FineTuning)
  - [Microsoft Olive](../../../../md/03.FineTuning)
  - [Mifano na Rasilimali za Urekebishaji](../../../../md/03.FineTuning)
- [**\[Private Preview\]** Maendeleo ya Mbali](../../../../md/03.FineTuning)
  - [Mahitaji ya awali](../../../../md/03.FineTuning)
  - [Kuweka Mradi wa Maendeleo ya Mbali](../../../../md/03.FineTuning)
  - [Toa Rasilimali za Azure](../../../../md/03.FineTuning)
  - [\[Hiari\] Ongeza Tokeni ya Huggingface kwenye Siri ya Azure Container App](../../../../md/03.FineTuning)
  - [Endesha Urekebishaji](../../../../md/03.FineTuning)
  - [Toa Kituo cha Utambuzi](../../../../md/03.FineTuning)
  - [Tangaza Kituo cha Utambuzi](../../../../md/03.FineTuning)
  - [Matumizi ya Juu](../../../../md/03.FineTuning)

## Maendeleo ya Ndani
### Maandalizi

1. Hakikisha dereva wa NVIDIA amesakinishwa kwenye mwenyeji.
2. Endesha `huggingface-cli login`, ikiwa unatumia HF kwa matumizi ya seti ya data
3. Maelezo ya mipangilio ya ufunguo wa `Olive` kwa chochote kinachobadilisha matumizi ya kumbukumbu.

### Washa Conda
Kwa kuwa tunatumia mazingira ya WSL na yanashirikiwa, unahitaji kuwasha mazingira ya conda kwa mkono. Baada ya hatua hii unaweza kuendesha urekebishaji au utambuzi.

```bash
conda activate [conda-env-name] 
```

### Urekebishaji wa modeli msingi tu
Ili kujaribu tu modeli msingi bila urekebishaji, unaweza kuendesha amri hii baada ya kuwasha conda.

```bash
cd inference

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://0.0.0.0:7860) in a browser after gradio initiates the connections.
python gradio_chat.py --baseonly
```

### Urekebishaji wa modeli na utambuzi

Mara tu nafasi ya kazi itakapo funguliwa katika kontena la maendeleo, fungua terminal (njia ya chaguo-msingi ni mzizi wa mradi), kisha endesha amri ifuatayo kurekebisha LLM kwenye seti ya data iliyochaguliwa.

```bash
python finetuning/invoke_olive.py 
```

Pointi za kuhifadhi na modeli ya mwisho zitawekwa kwenye folda ya `models`.

Ifuatayo endesha utambuzi kwa kutumia modeli iliyorekebishwa kupitia mazungumzo katika `console`, `kivinjari cha wavuti` au `prompt flow`.

```bash
cd inference

# Console interface.
python console_chat.py

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://127.0.0.1:7860) in a browser after gradio initiates the connections.
python gradio_chat.py
```

Ili kutumia `prompt flow` katika VS Code, tafadhali rejea [Mwongozo wa Kuanzisha Haraka](https://microsoft.github.io/promptflow/how-to-guides/quick-start.html).

### Urekebishaji wa Modeli

Ifuatayo, pakua modeli ifuatayo kulingana na upatikanaji wa GPU kwenye kifaa chako.

Ili kuanzisha kikao cha urekebishaji wa ndani kwa kutumia QLoRA, chagua modeli unayotaka kurekebisha kutoka kwenye katalogi yetu.
| Jukwaa | GPU inapatikana | Jina la modeli | Ukubwa (GB) |
|---------|---------|--------|--------|
| Windows | Ndiyo | Phi-3-mini-4k-**directml**-int4-awq-block-128-onnx | 2.13GB |
| Linux | Ndiyo | Phi-3-mini-4k-**cuda**-int4-onnx | 2.30GB |
| Windows<br>Linux | Hapana | Phi-3-mini-4k-**cpu**-int4-rtn-block-32-acc-level-4-onnx | 2.72GB |

**_Kumbuka_** Huna haja ya Akaunti ya Azure kupakua mifano

Modeli ya Phi3-mini (int4) ni takriban ukubwa wa 2GB-3GB. Kulingana na kasi ya mtandao wako, inaweza kuchukua dakika chache kupakua.

Anza kwa kuchagua jina la mradi na mahali pa kuhifadhi.
Ifuatayo, chagua modeli kutoka katalogi ya modeli. Utaombwa kupakua kiolezo cha mradi. Kisha unaweza kubofya "Configure Project" kurekebisha mipangilio mbalimbali.

### Microsoft Olive

Tunatumia [Olive](https://microsoft.github.io/Olive/why-olive.html) kuendesha urekebishaji wa QLoRA kwenye modeli ya PyTorch kutoka katalogi yetu. Mipangilio yote imewekwa awali kwa thamani za chaguo-msingi ili kuboresha mchakato wa urekebishaji wa ndani kwa matumizi bora ya kumbukumbu, lakini inaweza kubadilishwa kulingana na hali yako.

### Mifano na Rasilimali za Urekebishaji

- [Mwongozo wa Kuanzisha Urekebishaji](https://learn.microsoft.com/windows/ai/toolkit/toolkit-fine-tune)
- [Urekebishaji kwa kutumia Dataset ya HuggingFace](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-hf-dataset.md)
- [Urekebishaji kwa kutumia Dataset Rahisi](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-simple-dataset.md)

## **[Private Preview]** Maendeleo ya Mbali

### Mahitaji ya awali

1. Ili kuendesha urekebishaji wa modeli katika Mazingira yako ya Azure Container App ya mbali, hakikisha usajili wako una uwezo wa GPU wa kutosha. Tuma [tiketi ya msaada](https://azure.microsoft.com/support/create-ticket/) kuomba uwezo unaohitajika kwa programu yako. [Pata Taarifa Zaidi kuhusu uwezo wa GPU](https://learn.microsoft.com/azure/container-apps/workload-profiles-overview)
2. Ikiwa unatumia seti ya data binafsi kwenye HuggingFace, hakikisha una [akaunti ya HuggingFace](https://huggingface.co/?WT.mc_id=aiml-137032-kinfeylo) na [tengeneza tokeni ya upatikanaji](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=aiml-137032-kinfeylo)
3. Washa kipengele cha Remote Fine-tuning na Inference katika AI Toolkit kwa VS Code
   1. Fungua Mipangilio ya VS Code kwa kuchagua *File -> Preferences -> Settings*.
   2. Nenda kwenye *Extensions* na chagua *AI Toolkit*.
   3. Chagua chaguo la *"Enable Remote Fine-tuning And Inference"*.
   4. Reload VS Code ili mabadiliko yafanyike kazi.

- [Urekebishaji wa Mbali](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/remote-finetuning.md)

### Kuweka Mradi wa Maendeleo ya Mbali
1. Endesha amri ya palette `AI Toolkit: Focus on Resource View`.
2. Nenda kwenye *Model Fine-tuning* kufikia katalogi ya modeli. Weka jina la mradi wako na chagua mahali pa kuhifadhi kwenye mashine yako. Kisha, bonyeza kitufe cha *"Configure Project"*.
3. Mipangilio ya Mradi
    1. Epuka kuwasha chaguo la *"Fine-tune locally"*.
    2. Mipangilio ya Olive itaonekana ikiwa na thamani za awali zilizowekwa. Tafadhali rekebisha na jaza mipangilio hii kama inavyohitajika.
    3. Endelea na *Generate Project*. Hatua hii inatumia WSL na inahusisha kuanzisha mazingira mapya ya Conda, kujiandaa kwa masasisho yajayo yanayojumuisha Dev Containers.
4. Bonyeza *"Relaunch Window In Workspace"* kufungua mradi wako wa maendeleo ya mbali.

> **Kumbuka:** Mradi huu kwa sasa unafanya kazi ama ndani au kwa mbali ndani ya AI Toolkit kwa VS Code. Ikiwa utachagua *"Fine-tune locally"* wakati wa kuanzisha mradi, utaendesha tu ndani ya WSL bila uwezo wa maendeleo ya mbali. Kwa upande mwingine, ukiacha kuwasha *"Fine-tune locally"*, mradi utakuwa kwa mazingira ya mbali ya Azure Container App pekee.

### Toa Rasilimali za Azure
Ili kuanza, unahitaji kutoa Rasilimali za Azure kwa urekebishaji wa mbali. Fanya hivyo kwa kuendesha amri ya `AI Toolkit: Provision Azure Container Apps job for fine-tuning` kutoka kwenye amri ya palette.

Fuatilia maendeleo ya utoaji kupitia kiungo kinachoonyeshwa kwenye chaneli ya matokeo.

### [Hiari] Ongeza Tokeni ya Huggingface kwenye Siri ya Azure Container App
Ikiwa unatumia seti ya data binafsi ya HuggingFace, weka tokeni yako ya HuggingFace kama mabadiliko ya mazingira ili kuepuka hitaji la kuingia kwa mkono kwenye Hugging Face Hub.
Unaweza kufanya hivi kwa kutumia amri ya `AI Toolkit: Add Azure Container Apps Job secret for fine-tuning`. Kwa amri hii, unaweza kuweka jina la siri kama [`HF_TOKEN`](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables#hftoken) na tumia tokeni yako ya Hugging Face kama thamani ya siri.

### Endesha Urekebishaji
Ili kuanza kazi ya urekebishaji wa mbali, endesha amri ya `AI Toolkit: Run fine-tuning`.

Ili kuona kumbukumbu za mfumo na console, unaweza kutembelea portal ya Azure kwa kutumia kiungo kilicho kwenye paneli ya matokeo (hatua zaidi ziko kwenye [View and Query Logs on Azure](https://aka.ms/ai-toolkit/remote-provision#view-and-query-logs-on-azure)). Au, unaweza kuona kumbukumbu za console moja kwa moja kwenye paneli ya matokeo ya VSCode kwa kuendesha amri `AI Toolkit: Show the running fine-tuning job streaming logs`.
> **Kumbuka:** Kazi inaweza kuwekwa kwenye foleni kutokana na rasilimali zisizotosheleza. Ikiwa kumbukumbu haionekani, endesha amri `AI Toolkit: Show the running fine-tuning job streaming logs`, subiri kidogo kisha endesha tena amri hiyo kuunganishwa tena na kumbukumbu zinazoendelea.

Wakati wa mchakato huu, QLoRA itatumika kwa urekebishaji, na itaunda LoRA adapters kwa modeli kutumia wakati wa utambuzi.
Matokeo ya urekebishaji yatahifadhiwa katika Azure Files.

### Toa Kituo cha Utambuzi
Baada ya adapters kufunzwa katika mazingira ya mbali, tumia programu rahisi ya Gradio kuingiliana na modeli.
Kama ilivyo kwa mchakato wa urekebishaji, unahitaji kuweka Rasilimali za Azure kwa utambuzi wa mbali kwa kuendesha amri ya `AI Toolkit: Provision Azure Container Apps for inference` kutoka kwenye amri ya palette.

Kwa kawaida, usajili na kundi la rasilimali kwa utambuzi vinapaswa kufanana na vilivyotumika kwa urekebishaji. Utambuzi utatumia Mazingira yale yale ya Azure Container App na kufikia modeli na adapter ya modeli iliyohifadhiwa katika Azure Files, ambayo ilizalishwa wakati wa hatua ya urekebishaji.

### Tangaza Kituo cha Utambuzi
Ikiwa unataka kurekebisha msimbo wa utambuzi au kupakia tena modeli ya utambuzi, tafadhali endesha amri ya `AI Toolkit: Deploy for inference`. Hii italinganisha msimbo wako wa hivi karibuni na Azure Container App na kuanzisha tena nakala.

Mara baada ya utekelezaji kufanikiwa, unaweza kufikia API ya utambuzi kwa kubofya kitufe cha "*Go to Inference Endpoint*" kinachoonyeshwa kwenye taarifa ya VSCode. Au, kiungo cha API ya wavuti kinaweza kupatikana chini ya `ACA_APP_ENDPOINT` katika `./infra/inference.config.json` na kwenye paneli ya matokeo. Sasa uko tayari kutathmini modeli kwa kutumia kituo hiki.

### Matumizi ya Juu
Kwa maelezo zaidi kuhusu maendeleo ya mbali kwa AI Toolkit, rejea nyaraka za [Urekebishaji wa mifano kwa mbali](https://aka.ms/ai-toolkit/remote-provision) na [Utambuzi kwa modeli iliyorekebishwa](https://aka.ms/ai-toolkit/remote-inference).

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.