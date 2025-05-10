<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c1559c5af6caccf6f623fd43a6b3a9a3",
  "translation_date": "2025-05-09T20:35:21+00:00",
  "source_file": "md/03.FineTuning/FineTuning_AIFoundry.md",
  "language_code": "tl"
}
-->
# Fine-tuning Phi-3 gamit ang Azure AI Foundry

Tuklasin natin kung paano i-fine-tune ang Microsoft Phi-3 Mini language model gamit ang Azure AI Foundry. Ang fine-tuning ay nagbibigay-daan upang iakma ang Phi-3 Mini sa mga partikular na gawain, kaya mas nagiging malakas at angkop ito sa konteksto.

## Mga Dapat Isaalang-alang

- **Kakayahan:** Alin sa mga modelo ang pwedeng i-fine tune? Ano ang mga kaya ng base model kapag na-fine tune?
- **Gastos:** Ano ang modelo ng pagpepresyo para sa fine tuning?
- **Customizability:** Gaano kalawak ang pwedeng baguhin sa base model – at sa anong paraan?
- **Kaginhawaan:** Paano ba talaga nangyayari ang fine tuning – kailangan ba ng custom na code? Kailangan ba ng sariling compute?
- **Kaligtasan:** Kilala na may mga panganib sa kaligtasan ang mga fine-tuned models – may mga proteksyon ba laban sa hindi inaasahang pinsala?

![AIFoundry Models](../../../../translated_images/AIFoundryModels.4440430c9f07dbd6c625971422e7b9a5b9cb91fa046e447ba9ea41457860532f.tl.png)

## Paghahanda para sa fine-tuning

### Mga Kinakailangan

> [!NOTE]
> Para sa Phi-3 family models, ang pay-as-you-go na fine-tune offering ay available lamang sa mga hubs na ginawa sa **East US 2** na rehiyon.

- Isang Azure subscription. Kung wala ka pang Azure subscription, gumawa ng [paid Azure account](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) para makapagsimula.

- Isang [AI Foundry project](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- Ginagamit ang Azure role-based access controls (Azure RBAC) para bigyan ng access sa mga operasyon sa Azure AI Foundry. Para magawa ang mga hakbang sa artikulong ito, kailangang may __Azure AI Developer role__ ang iyong user account sa resource group.

### Pagrehistro ng subscription provider

Siguraduhing nakarehistro ang subscription sa `Microsoft.Network` resource provider.

1. Mag-sign in sa [Azure portal](https://portal.azure.com).
1. Piliin ang **Subscriptions** mula sa kaliwang menu.
1. Piliin ang subscription na gagamitin.
1. Piliin ang **AI project settings** > **Resource providers** mula sa kaliwang menu.
1. Tiyakin na nasa listahan ang **Microsoft.Network** bilang resource provider. Kung wala, idagdag ito.

### Paghahanda ng data

Ihanda ang iyong training at validation data para i-fine tune ang iyong modelo. Ang iyong training at validation datasets ay binubuo ng mga input at output na halimbawa kung paano mo gustong gumana ang modelo.

Siguraduhing sumusunod sa inaasahang format para sa inference ang lahat ng training examples. Para epektibong ma-fine tune ang mga modelo, tiyakin na balanse at iba-iba ang dataset.

Kasama dito ang pagpapanatili ng balanse ng data, pagsasama ng iba't ibang senaryo, at pana-panahong pag-aayos ng training data para tumugma sa totoong mundo, na nagreresulta sa mas tumpak at balanseng mga sagot mula sa modelo.

Iba-iba ang format ng training data depende sa uri ng modelo.

### Chat Completion

Ang training at validation data na gagamitin mo ay **dapat** naka-format bilang JSON Lines (JSONL) na dokumento. Para sa `Phi-3-mini-128k-instruct`, ang fine-tuning dataset ay dapat nakaayos sa conversational format na ginagamit ng Chat completions API.

### Halimbawa ng format ng file

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

Ang suportadong uri ng file ay JSON Lines. Ina-upload ang mga file sa default datastore at ginagawa itong available sa iyong proyekto.

## Fine-Tuning ng Phi-3 gamit ang Azure AI Foundry

Pinapayagan ka ng Azure AI Foundry na i-customize ang malalaking language models gamit ang iyong sariling dataset sa proseso na tinatawag na fine-tuning. Malaki ang naitutulong ng fine-tuning dahil nagbibigay ito ng kakayahang i-customize at i-optimize ang mga modelo para sa partikular na mga gawain at aplikasyon. Nagdudulot ito ng mas mahusay na performance, mas mababang gastos, mas mabilis na response, at mga output na naaayon sa pangangailangan.

![Finetune AI Foundry](../../../../translated_images/AIFoundryfinetune.69ddc22d1ab08167a7e53a911cd33c749d99fea4047801a836ceb6eec66c5719.tl.png)

### Gumawa ng Bagong Proyekto

1. Mag-sign in sa [Azure AI Foundry](https://ai.azure.com).

1. Piliin ang **+New project** para gumawa ng bagong proyekto sa Azure AI Foundry.

    ![FineTuneSelect](../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.tl.png)

1. Gawin ang mga sumusunod:

    - Pangalan ng Project **Hub name**. Dapat ito ay natatangi.
    - Piliin ang **Hub** na gagamitin (gumawa ng bago kung kinakailangan).

    ![FineTuneSelect](../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.tl.png)

1. Gawin ang mga sumusunod para gumawa ng bagong hub:

    - Ilagay ang **Hub name**. Dapat ito ay natatangi.
    - Piliin ang iyong Azure **Subscription**.
    - Piliin ang **Resource group** na gagamitin (gumawa ng bago kung kinakailangan).
    - Piliin ang **Location** na nais gamitin.
    - Piliin ang **Connect Azure AI Services** na gagamitin (gumawa ng bago kung kinakailangan).
    - Piliin ang **Connect Azure AI Search** at piliin ang **Skip connecting**.

    ![FineTuneSelect](../../../../translated_images/create-hub.b93d390a6d3eebd4c33eb7e4ea6ef41fd69c4d39f21339d4bda51af9ed70505f.tl.png)

1. Piliin ang **Next**.
1. Piliin ang **Create a project**.

### Paghahanda ng Data

Bago mag-fine-tune, mangalap o gumawa ng dataset na may kaugnayan sa iyong gawain, tulad ng chat instructions, question-answer pairs, o iba pang kaugnay na text data. Linisin at i-preprocess ang data sa pamamagitan ng pagtanggal ng ingay, pag-aayos ng mga kulang na datos, at pag-tokenize ng teksto.

### Fine-tune ang Phi-3 models sa Azure AI Foundry

> [!NOTE]
> Ang fine-tuning ng Phi-3 models ay suportado lamang sa mga proyekto na nasa East US 2.

1. Piliin ang **Model catalog** mula sa kaliwang tab.

1. I-type ang *phi-3* sa **search bar** at piliin ang phi-3 model na nais mong gamitin.

    ![FineTuneSelect](../../../../translated_images/select-model.02eef2cbb5b7e61a86526b05bd5ec9822fd6b2abae4e38fd5d9bdef541dfb967.tl.png)

1. Piliin ang **Fine-tune**.

    ![FineTuneSelect](../../../../translated_images/select-finetune.88cf562034f78baf0b7f41511fd4c45e1f068104238f1397661b9402ff9e2e09.tl.png)

1. Ilagay ang **Fine-tuned model name**.

    ![FineTuneSelect](../../../../translated_images/finetune1.8a20c66f797cc7ede7feb789a45c42713b7aeadfeb01dbc34446019db5c189d4.tl.png)

1. Piliin ang **Next**.

1. Gawin ang mga sumusunod:

    - Piliin ang **task type** bilang **Chat completion**.
    - Piliin ang **Training data** na gagamitin. Maaari mo itong i-upload sa Azure AI Foundry o mula sa iyong lokal na kapaligiran.

    ![FineTuneSelect](../../../../translated_images/finetune2.47df1aa177096dbaa01e4d64a06eb3f46a29718817fa706167af3ea01419a32f.tl.png)

1. Piliin ang **Next**.

1. I-upload ang **Validation data** na nais mong gamitin, o piliin ang **Automatic split of training data**.

    ![FineTuneSelect](../../../../translated_images/finetune3.e887e47240626c31f969532610c965594635c91cf3f94639fa60fb5d2bbd8f93.tl.png)

1. Piliin ang **Next**.

1. Gawin ang mga sumusunod:

    - Piliin ang **Batch size multiplier** na nais mong gamitin.
    - Piliin ang **Learning rate** na nais mong gamitin.
    - Piliin ang **Epochs** na nais mong gamitin.

    ![FineTuneSelect](../../../../translated_images/finetune4.9f47c2fad66fddd0f091b62a2fa6ac23260226ab841287805d843ebc83761801.tl.png)

1. Piliin ang **Submit** para simulan ang fine-tuning.

    ![FineTuneSelect](../../../../translated_images/select-submit.b5344fd77e49bfb6d4efe72e713f6a46f04323d871c118bbf59bf0217698dfee.tl.png)

1. Kapag na-fine-tune na ang iyong modelo, makikita ang status na **Completed**, tulad ng ipinapakita sa larawan sa ibaba. Maaari mo nang i-deploy ang modelo at gamitin ito sa iyong sariling aplikasyon, sa playground, o sa prompt flow. Para sa karagdagang impormasyon, tingnan ang [How to deploy Phi-3 family of small language models with Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![FineTuneSelect](../../../../translated_images/completed.f4be2c6e660d8ba908d1d23e2102925cc31e57cbcd60fb10e7ad3b7925f585c4.tl.png)

> [!NOTE]
> Para sa mas detalyadong impormasyon tungkol sa fine-tuning ng Phi-3, bisitahin ang [Fine-tune Phi-3 models in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini).

## Paglilinis ng iyong mga fine-tuned models

Maaari mong tanggalin ang isang fine-tuned model mula sa listahan ng fine-tuning models sa [Azure AI Foundry](https://ai.azure.com) o mula sa model details page. Piliin ang fine-tuned model na nais tanggalin sa Fine-tuning page, pagkatapos ay piliin ang Delete button para burahin ito.

> [!NOTE]
> Hindi mo maaaring tanggalin ang isang custom model kung mayroon pa itong existing deployment. Kailangan mo munang tanggalin ang deployment bago mo mabura ang custom model.

## Gastos at quota

### Mga konsiderasyon sa gastos at quota para sa Phi-3 models na fine-tuned bilang serbisyo

Ang Phi models na fine-tuned bilang serbisyo ay inaalok ng Microsoft at naka-integrate sa Azure AI Foundry para magamit. Makikita mo ang pagpepresyo kapag [nagde-deploy](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) o nagfa-fine-tune ng mga modelo sa ilalim ng Pricing and terms tab sa deployment wizard.

## Content filtering

Ang mga modelong dineploy bilang serbisyo na pay-as-you-go ay pinoprotektahan ng Azure AI Content Safety. Kapag dineploy sa real-time endpoints, maaari mong piliing huwag gamitin ang kakayahang ito. Sa naka-enable na Azure AI content safety, parehong ang prompt at completion ay dumadaan sa isang grupo ng classification models na naglalayong tuklasin at pigilan ang paglabas ng nakakasamang nilalaman. Ang sistema ng content filtering ay nakakakita at kumikilos laban sa mga partikular na kategorya ng posibleng mapanganib na nilalaman sa parehong input prompts at output completions. Alamin pa tungkol sa [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering).

**Fine-Tuning Configuration**

Mga hyperparameters: Tukuyin ang mga hyperparameters tulad ng learning rate, batch size, at bilang ng training epochs.

**Loss Function**

Pumili ng angkop na loss function para sa iyong gawain (halimbawa, cross-entropy).

**Optimizer**

Pumili ng optimizer (halimbawa, Adam) para sa gradient updates habang nagtetrain.

**Proseso ng Fine-Tuning**

- Load Pre-Trained Model: I-load ang Phi-3 Mini checkpoint.
- Add Custom Layers: Magdagdag ng mga layer na angkop sa gawain (halimbawa, classification head para sa chat instructions).

**I-train ang Modelo**  
I-fine tune ang modelo gamit ang inihandang dataset. Subaybayan ang progreso ng training at ayusin ang mga hyperparameters kung kinakailangan.

**Evaluation at Validation**

Validation Set: Hatiin ang data sa training at validation sets.

**Suriin ang Performance**

Gamitin ang mga metrics tulad ng accuracy, F1-score, o perplexity para masukat ang performance ng modelo.

## I-save ang Fine-Tuned Model

**Checkpoint**  
I-save ang fine-tuned model checkpoint para sa susunod na paggamit.

## Deployment

- I-deploy bilang Web Service: I-deploy ang fine-tuned model bilang web service sa Azure AI Foundry.
- Subukan ang Endpoint: Magpadala ng test queries sa deployed endpoint para tiyakin ang functionality nito.

## Ulitin at Pagbutihin

Ulitin: Kung hindi pa kasiya-siya ang performance, ulitin ang proseso sa pamamagitan ng pag-adjust ng hyperparameters, pagdagdag ng data, o pag-fine-tune ng mas maraming epochs.

## Subaybayan at Paunlarin

Patuloy na subaybayan ang kilos ng modelo at pagbutihin ito kung kinakailangan.

## I-customize at Palawakin

Custom Tasks: Maaaring i-fine tune ang Phi-3 Mini para sa iba pang mga gawain bukod sa chat instructions. Tuklasin ang iba pang mga gamit!  
Experiment: Subukan ang iba't ibang arkitektura, kombinasyon ng mga layer, at mga teknik para mapahusay ang performance.

> [!NOTE]
> Ang fine-tuning ay isang paulit-ulit na proseso. Mag-eksperimento, matuto, at iakma ang iyong modelo para makamit ang pinakamahusay na resulta para sa iyong partikular na gawain!

**Pagsasalin**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.