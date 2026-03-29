# Fine-tuning Phi-3 gamit ang Microsoft Foundry

Tuklasin natin kung paano i-fine-tune ang Phi-3 Mini na language model ng Microsoft gamit ang Microsoft Foundry. Ang fine-tuning ay nagpapahintulot sa iyo na i-adapt ang Phi-3 Mini sa mga partikular na gawain, ginagawang mas makapangyarihan at mas may kamalayan sa konteksto.

## Mga Pagsasaalang-alang

- **Kakayahan:** Aling mga modelo ang maaaring i-fine tune? Ano ang maaaring gawin ng base na modelo kapag na-fine tune?
- **Gastos:** Ano ang modelo ng pagpepresyo para sa fine tuning
- **Pag-customize:** Gaano kalaki ang maaaring baguhin sa base na modelo – at sa anong mga paraan?
- **Kaginhawaan:** Paano ba talaga nangyayari ang fine tuning – kailangan ba akong magsulat ng custom code? Kailangan ko ba magdala ng sariling compute?
- **Kaligtasan:** Kilala ang mga fine tuned na modelo na may mga panganib sa kaligtasan – may mga guardrails ba na nakalagay para protektahan laban sa hindi inaasahang pinsala?

![AIFoundry Models](../../../../translated_images/tl/AIFoundryModels.0e1b16f7d0b09b73.webp)

## Paghahanda para sa fine-tuning

### Mga Kinakailangan

> [!NOTE]
> Para sa mga Phi-3 family na modelo, ang pay-as-you-go na modelo ng fine-tune ay available lamang sa mga hub na nilikha sa **East US 2** na mga rehiyon.

- Isang Azure subscription. Kung wala ka pang Azure subscription, gumawa ng [paid Azure account](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) upang makapagsimula.

- Isang [AI Foundry project](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- Ginagamit ang Azure role-based access controls (Azure RBAC) para magbigay ng access sa mga operasyon sa Microsoft Foundry. Upang maisagawa ang mga hakbang sa artikulong ito, ang iyong user account ay dapat na nakatalaga sa __Azure AI Developer role__ sa resource group.

### Pagrehistro ng provider ng subscription

Suriin na ang subscription ay nakarehistro sa `Microsoft.Network` resource provider.

1. Mag-sign in sa [Azure portal](https://portal.azure.com).
1. Piliin ang **Subscriptions** sa kaliwang menu.
1. Piliin ang subscription na nais mong gamitin.
1. Piliin ang **AI project settings** > **Resource providers** sa kaliwang menu.
1. Kumpirmahin na ang **Microsoft.Network** ay nasa listahan ng mga resource providers. Kung wala, idagdag ito.

### Paghahanda ng data

Ihanda ang iyong training at validation data upang i-finetune ang iyong modelo. Ang iyong mga training data at validation data sets ay binubuo ng mga halimbawa ng input at output para sa nais mong performance ng modelo.

Siguraduhin na lahat ng iyong training examples ay sumusunod sa inaasahang format para sa inference. Upang maging epektibo ang fine-tuning ng mga modelo, tiyakin ang isang balanseng at iba't ibang dataset.

Kasama rito ang pagpapanatili ng balanse ng data, pagsasama ng iba't ibang senaryo, at pana-panahong pag-refine ng training data upang tumugma sa mga inaasahan sa totoong mundo, na magreresulta sa mas tumpak at balanseng mga sagot mula sa modelo.

Iba't ibang uri ng modelo ang nangangailangan ng iba't ibang format ng training data.

### Chat Completion

Ang training at validation data na gagamitin mo **ay dapat** nakafomat bilang JSON Lines (JSONL) na dokumento. Para sa `Phi-3-mini-128k-instruct` ang fine-tuning dataset ay kailangang nasa conversational na format na ginagamit ng Chat completions API.

### Halimbawang format ng file

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

Ang suportadong uri ng file ay JSON Lines. Ang mga file ay ia-upload sa default datastore at gagawing available sa iyong proyekto.

## Fine-Tuning Phi-3 gamit ang Microsoft Foundry

Pinapayagan ka ng Microsoft Foundry na i-tailor ang malalaking language models gamit ang iyong personal na mga dataset sa pamamagitan ng proseso na tinatawag na fine-tuning. Nagbibigay ang fine-tuning ng malaking halaga sa pamamagitan ng pagpapahintulot ng customization at optimisasyon para sa mga partikular na gawain at aplikasyon. Nagreresulta ito sa mas magandang performance, mas matipid na gastusin, mas mababang latency, at mga output na naaangkop sa iyong pangangailangan.

![Finetune AI Foundry](../../../../translated_images/tl/AIFoundryfinetune.193aaddce48d553c.webp)

### Gumawa ng Bagong Proyekto

1. Mag-sign in sa [Microsoft Foundry](https://ai.azure.com).

1. Piliin ang **+New project** upang gumawa ng bagong proyekto sa Microsoft Foundry.

    ![FineTuneSelect](../../../../translated_images/tl/select-new-project.cd31c0404088d7a3.webp)

1. Gawin ang mga sumusunod:

    - Pangalan ng proyekto sa **Hub name**. Dapat ito ay natatanging halaga.
    - Piliin ang **Hub** na gagamitin (gumawa ng bago kung kinakailangan).

    ![FineTuneSelect](../../../../translated_images/tl/create-project.ca3b71298b90e420.webp)

1. Gawin ang mga sumusunod para gumawa ng bagong hub:

    - Ilagay ang **Hub name**. Dapat ito ay natatanging halaga.
    - Piliin ang iyong Azure **Subscription**.
    - Piliin ang **Resource group** na gagamitin (gumawa ng bago kung kinakailangan).
    - Piliin ang **Location** na nais mong gamitin.
    - Piliin ang **Connect Azure AI Services** na gagamitin (gumawa ng bago kung kinakailangan).
    - Piliin ang **Connect Azure AI Search** na **Skip connecting**.

    ![FineTuneSelect](../../../../translated_images/tl/create-hub.49e53d235e80779e.webp)

1. Piliin ang **Next**.
1. Piliin ang **Create a project**.

### Paghahanda ng Data

Bago ang fine-tuning, mangolekta o gumawa ng dataset na may kaugnayan sa iyong gawain, tulad ng mga chat instructions, question-answer pairs, o anumang kaugnay na text data. Linisin at i-preprocess ang data sa pamamagitan ng pagtanggal ng noise, pag-aayos ng mga kulang na halaga, at pag-tokenize ng teksto.

### Fine-tune ang mga Phi-3 model sa Microsoft Foundry

> [!NOTE]
> Ang fine-tuning ng Phi-3 models ay kasalukuyang suportado lamang sa mga proyekto na nasa East US 2.

1. Piliin ang **Model catalog** mula sa tab sa kaliwa.

1. I-type ang *phi-3* sa **search bar** at piliin ang phi-3 na model na nais mong gamitin.

    ![FineTuneSelect](../../../../translated_images/tl/select-model.60ef2d4a6a3cec57.webp)

1. Piliin ang **Fine-tune**.

    ![FineTuneSelect](../../../../translated_images/tl/select-finetune.a976213b543dd9d8.webp)

1. I-type ang **Pangalan ng Fine-tuned na modelo**.

    ![FineTuneSelect](../../../../translated_images/tl/finetune1.c2b39463f0d34148.webp)

1. Piliin ang **Next**.

1. Gawin ang mga sumusunod:

    - Piliin ang **uri ng gawain** bilang **Chat completion**.
    - Piliin ang **Training data** na nais mong gamitin. Maaari mo itong i-upload sa pamamagitan ng Microsoft Foundry data o mula sa iyong lokal na kapaligiran.

    ![FineTuneSelect](../../../../translated_images/tl/finetune2.43cb099b1a94442d.webp)

1. Piliin ang **Next**.

1. I-upload ang **Validation data** na nais mong gamitin, o maaari mong piliin ang **Automatic split of training data**.

    ![FineTuneSelect](../../../../translated_images/tl/finetune3.fd96121b67dcdd92.webp)

1. Piliin ang **Next**.

1. Gawin ang mga sumusunod:

    - Piliin ang **Batch size multiplier** na nais mong gamitin.
    - Piliin ang **Learning rate** na nais mong gamitin.
    - Piliin ang **Epochs** na nais mong gamitin.

    ![FineTuneSelect](../../../../translated_images/tl/finetune4.e18b80ffccb5834a.webp)

1. Piliin ang **Submit** upang simulan ang proseso ng fine-tuning.

    ![FineTuneSelect](../../../../translated_images/tl/select-submit.0a3802d581bac271.webp)


1. Kapag na-fine-tune na ang iyong modelo, ipapakita ang status bilang **Completed**, tulad ng ipinapakita sa larawan sa ibaba. Maaari mo nang i-deploy ang modelo at magamit ito sa iyong sariling aplikasyon, sa playground, o sa prompt flow. Para sa karagdagang impormasyon, tingnan ang [Paano mag-deploy ng Phi-3 family ng maliliit na language model gamit ang Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![FineTuneSelect](../../../../translated_images/tl/completed.4dc8d2357144cdef.webp)

> [!NOTE]
> Para sa mas detalyadong impormasyon tungkol sa fine-tuning ng Phi-3, bisitahin ang [Fine-tune Phi-3 models in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini).

## Paglilinis ng iyong mga fine-tuned na modelo

Maaari mong tanggalin ang isang fine-tuned na modelo mula sa listahan ng fine-tuning model sa [Microsoft Foundry](https://ai.azure.com) o mula sa pahina ng detalye ng modelo. Piliin ang fine-tuned na model na nais tanggalin mula sa Fine-tuning page, at pagkatapos ay piliin ang Delete button upang alisin ang fine-tuned na modelo.

> [!NOTE]
> Hindi mo maaaring tanggalin ang isang custom na modelo kung mayroon itong umiiral na deployment. Dapat mo munang tanggalin ang deployment ng iyong modelo bago mo matatanggal ang iyong custom na modelo.

## Gastos at mga quota

### Mga konsiderasyon sa gastos at quota para sa Phi-3 models na fine-tuned bilang serbisyo

Ang mga Phi models na fine-tuned bilang serbisyo ay inaalok ng Microsoft at integradong ginagamit sa Microsoft Foundry. Maaari mong makita ang pagpepresyo kapag [nag-deploy](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) o fine-tuning ng mga modelo sa ilalim ng Pricing and terms tab sa deployment wizard.

## Pag-filter ng nilalaman

Ang mga modelong dineploy bilang serbisyo na may pay-as-you-go ay pinoprotektahan ng Azure AI Content Safety. Kapag dineploy sa real-time na mga endpoint, maaari mong piliing i-opt out ang kakayahang ito. Sa enabled na Azure AI content safety, ang parehong prompt at completion ay dumadaan sa ensemble ng mga classification model na nilalayong matukoy at pigilan ang output ng nakakapinsalang content. Ang content filtering system ay nakaka-detect at kumikilos sa mga partikular na kategorya ng potensyal na nakakapinsalang content sa parehong input prompts at output completions. Matuto pa tungkol sa [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering).

**Fine-Tuning Configuration**

Hyperparameters: Tukuyin ang mga hyperparameters tulad ng learning rate, batch size, at bilang ng training epochs.

**Loss Function**

Pumili ng angkop na loss function para sa iyong gawain (hal., cross-entropy).

**Optimizer**

Pumili ng optimizer (hal., Adam) para sa gradient updates habang nagtetrain.

**Fine-Tuning Process**

- Load Pre-Trained Model: I-load ang Phi-3 Mini checkpoint.
- Add Custom Layers: Magdagdag ng mga task-specific na layer (hal., classification head para sa chat instructions).

**Sanayin ang Modelo**  
I-fine tune ang modelo gamit ang iyong inihandang dataset. I-monitor ang progreso ng training at i-adjust ang mga hyperparameters kung kinakailangan.

**Evaluation and Validation**

Validation Set: Hatiin ang data mo sa training at validation sets.

**Suriin ang Performance**

Gamitin ang mga metrics tulad ng accuracy, F1-score, o perplexity upang tasahin ang performance ng modelo.

## I-save ang Fine-Tuned na Modelo

**Checkpoint**  
I-save ang checkpoint ng fine-tuned na modelo para sa hinaharap na gamit.

## Deployment

- I-deploy bilang Web Service: I-deploy ang fine-tuned na modelo bilang web service sa Microsoft Foundry.
- Subukan ang Endpoint: Magpadala ng test queries sa na-deploy na endpoint upang beripikahin ang functionality nito.

## Mag-iterate at Mag-improve

Mag-iterate: Kung hindi kasiya-siya ang performance, mag-iterate sa pamamagitan ng pag-adjust ng hyperparameters, pagdagdag ng data, o pag-fine-tune ng karagdagang epochs.

## Mag-monitor at Mag-refine

Patuloy na i-monitor ang behavior ng modelo at mag-refine kung kinakailangan.

## Mag-customize at Mag-extend

Custom Tasks: Maaaring i-fine-tune ang Phi-3 Mini para sa iba’t ibang gawain maliban sa chat instructions. Tuklasin ang iba pang mga gamit!  
Experiment: Subukan ang iba't ibang arkitektura, kombinasyon ng layers, at mga teknik upang mapabuti ang performance.

> [!NOTE]
> Ang fine-tuning ay isang paulit-ulit na proseso. Mag-eksperimento, matuto, at i-adapt ang iyong modelo upang makamit ang pinakamahusay na resulta para sa iyong partikular na gawain!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di pagkakatugma. Ang orihinal na dokumento sa kanyang orihinal na wika ang dapat ituring na pangunahing sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang mga hindi pagkakaunawaan o maling interpretasyon na nagmumula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->