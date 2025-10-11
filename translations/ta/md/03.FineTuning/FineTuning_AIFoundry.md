<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c1559c5af6caccf6f623fd43a6b3a9a3",
  "translation_date": "2025-10-11T11:50:35+00:00",
  "source_file": "md/03.FineTuning/FineTuning_AIFoundry.md",
  "language_code": "ta"
}
-->
# Azure AI Foundry மூலம் Phi-3 மாடலை நன்றாக அமைத்தல்

Microsoft இன் Phi-3 Mini மொழி மாடலை Azure AI Foundry மூலம் நன்றாக அமைப்பது எப்படி என்பதை ஆராய்வோம். Fine-tuning மூலம் Phi-3 Mini மாடலை குறிப்பிட்ட பணிகளுக்கு ஏற்றவாறு மாற்றி, அதை மேலும் சக்திவாய்ந்ததாகவும் சூழலுக்கு பொருத்தமாகவும் மாற்றலாம்.

## கருத்துக்கள்

- **திறன்கள்:** எந்த மாடல்கள் fine-tuning செய்யக்கூடியவை? அடிப்படை மாடலை fine-tuning மூலம் என்ன செய்ய முடியும்?
- **செலவு:** fine-tuning கான விலை முறை என்ன?
- **தனிப்பயனாக்கம்:** அடிப்படை மாடலை எவ்வளவு மாற்ற முடியும் – மற்றும் எந்த வழிகளில்?
- **சௌகரியம்:** fine-tuning எப்படி நடக்கிறது – தனிப்பயன் குறியீடு எழுத வேண்டுமா? எனது கணினியை கொண்டு வர வேண்டுமா?
- **பாதுகாப்பு:** fine-tuned மாடல்கள் பாதுகாப்பு சிக்கல்களை கொண்டிருக்கலாம் – எதிர்பாராத பாதிப்புகளைத் தடுக்க எந்த பாதுகாப்பு வழிமுறைகள் உள்ளன?

![AIFoundry Models](../../../../imgs/03/AIFoundry/AIFoundryModels.png)

## Fine-tuning கான தயாரிப்பு

### முன் தேவைகள்

> [!NOTE]
> Phi-3 குடும்ப மாடல்களுக்கு, pay-as-you-go fine-tune சேவை **East US 2** பகுதிகளில் உருவாக்கப்பட்ட hubs-களுடன் மட்டுமே கிடைக்கிறது.

- Azure சந்தாதார கணக்கு. Azure சந்தாதார கணக்கு இல்லையெனில், [paid Azure account](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) உருவாக்கி தொடங்கவும்.

- [AI Foundry project](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- Azure RBAC (Azure role-based access controls) மூலம் Azure AI Foundry இல் செயல்பாடுகளுக்கு அணுகலை வழங்கப்படுகிறது. இந்த கட்டுரையில் உள்ள படிகளைச் செய்ய, உங்கள் பயனர் கணக்கு __Azure AI Developer role__-க்கு ஒதுக்கப்பட்டிருக்க வேண்டும்.

### சந்தாதார வழங்குநர் பதிவு

`Microsoft.Network` resource provider-க்கு சந்தாதார பதிவு செய்யப்பட்டுள்ளதா என்பதை உறுதிப்படுத்தவும்.

1. [Azure portal](https://portal.azure.com) இல் உள்நுழைக.
1. இடது மெனுவில் **Subscriptions** தேர்ந்தெடுக்கவும்.
1. நீங்கள் பயன்படுத்த விரும்பும் subscription-ஐ தேர்ந்தெடுக்கவும்.
1. இடது மெனுவில் **AI project settings** > **Resource providers** தேர்ந்தெடுக்கவும்.
1. **Microsoft.Network** resource providers பட்டியலில் உள்ளதா என்பதை உறுதிப்படுத்தவும். இல்லையெனில் அதைச் சேர்க்கவும்.

### தரவுத் தயாரிப்பு

உங்கள் மாடலை fine-tune செய்ய உங்கள் பயிற்சி மற்றும் சரிபார்ப்பு தரவுகளைத் தயாரிக்கவும். உங்கள் பயிற்சி மற்றும் சரிபார்ப்பு தரவுகள் மாடல் செயல்பட வேண்டிய விதத்தை விளக்கும் உள்ளீடு மற்றும் வெளியீடு எடுத்துக்காட்டுகளை கொண்டிருக்க வேண்டும்.

உங்கள் பயிற்சி எடுத்துக்காட்டுகள் inference கான எதிர்பார்க்கப்படும் வடிவமைப்பை பின்பற்றுவதை உறுதிப்படுத்தவும். மாடல்களை திறம்பட fine-tune செய்ய, சமநிலை மற்றும் பலதரப்பட்ட dataset-ஐ உறுதிப்படுத்தவும்.

இது தரவின் சமநிலையை பராமரிப்பதையும், பல்வேறு சூழல்களை உள்ளடக்குவதையும், பயிற்சி தரவுகளை அவ்வப்போது நிஜ உலக எதிர்பார்ப்புகளுடன் ஒத்திசைக்கவும், இறுதியில் மேலும் துல்லியமான மற்றும் சமநிலையான மாடல் பதில்களை உருவாக்கவும் உதவுகிறது.

வகை மாடல்களுக்கு வேறுபட்ட பயிற்சி தரவின் வடிவமைப்பு தேவை.

### Chat Completion

நீங்கள் பயன்படுத்தும் பயிற்சி மற்றும் சரிபார்ப்பு தரவுகள் **JSON Lines (JSONL)** ஆவணமாக வடிவமைக்கப்பட்டிருக்க வேண்டும். `Phi-3-mini-128k-instruct` மாடலுக்கு fine-tuning dataset Chat completions API பயன்படுத்தும் உரையாடல் வடிவமைப்பில் இருக்க வேண்டும்.

### எடுத்துக்காட்டு கோப்பு வடிவமைப்பு

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

JSON Lines கோப்பு வகை ஆதரிக்கப்படுகிறது. கோப்புகள் இயல்புநிலை datastore-க்கு பதிவேற்றப்பட்டு உங்கள் திட்டத்தில் கிடைக்கப்படும்.

## Azure AI Foundry மூலம் Phi-3 மாடலை Fine-Tuning

Azure AI Foundry மூலம் பெரிய மொழி மாடல்களை உங்கள் தனிப்பட்ட dataset-களுக்கு fine-tuning செய்யலாம். Fine-tuning மூலம் குறிப்பிட்ட பணிகள் மற்றும் பயன்பாடுகளுக்கு தனிப்பயனாக்கம் மற்றும் மேம்படுத்தல் கிடைக்கிறது. இது செயல்திறன், செலவுக் குறைவு, latency குறைவு, மற்றும் தனிப்பயன் வெளியீடுகளை மேம்படுத்துகிறது.

![Finetune AI Foundry](../../../../imgs/03/AIFoundry/AIFoundryfinetune.png)

### புதிய திட்டம் உருவாக்குதல்

1. [Azure AI Foundry](https://ai.azure.com) இல் உள்நுழைக.

1. **+New project** தேர்ந்தெடுத்து புதிய திட்டத்தை உருவாக்கவும்.

    ![FineTuneSelect](../../../../imgs/03/AIFoundry/select-new-project.png)

1. பின்வரும் பணிகளைச் செய்யவும்:

    - திட்ட **Hub name**. இது தனித்துவமான மதிப்பாக இருக்க வேண்டும்.
    - பயன்படுத்த **Hub**-ஐ தேர்ந்தெடுக்கவும் (தேவைப்பட்டால் புதிய Hub உருவாக்கவும்).

    ![FineTuneSelect](../../../../imgs/03/AIFoundry/create-project.png)

1. புதிய Hub உருவாக்க பின்வரும் பணிகளைச் செய்யவும்:

    - **Hub name** உள்ளிடவும். இது தனித்துவமான மதிப்பாக இருக்க வேண்டும்.
    - உங்கள் Azure **Subscription**-ஐ தேர்ந்தெடுக்கவும்.
    - பயன்படுத்த **Resource group**-ஐ தேர்ந்தெடுக்கவும் (தேவைப்பட்டால் புதிய Resource group உருவாக்கவும்).
    - நீங்கள் பயன்படுத்த விரும்பும் **Location**-ஐ தேர்ந்தெடுக்கவும்.
    - **Connect Azure AI Services**-ஐ தேர்ந்தெடுக்கவும் (தேவைப்பட்டால் புதிய சேவை உருவாக்கவும்).
    - **Connect Azure AI Search**-ஐ **Skip connecting** தேர்ந்தெடுக்கவும்.

    ![FineTuneSelect](../../../../imgs/03/AIFoundry/create-hub.png)

1. **Next** தேர்ந்தெடுக்கவும்.
1. **Create a project** தேர்ந்தெடுக்கவும்.

### தரவுத் தயாரிப்பு

Fine-tuning செய்ய முன், உங்கள் பணிக்கு தொடர்புடைய dataset-ஐ சேகரிக்கவும் அல்லது உருவாக்கவும், உதாரணமாக chat instructions, கேள்வி-பதில் ஜோடிகள், அல்லது பிற தொடர்புடைய உரை தரவுகள். இந்த தரவுகளை சுத்தம் செய்து, சிக்கல்களை நீக்கி, குறைந்த மதிப்புகளை நிரப்பி, உரையை tokenizing செய்யவும்.

### Azure AI Foundry இல் Phi-3 மாடல்களை Fine-Tuning செய்யுதல்

> [!NOTE]
> Phi-3 மாடல்களின் fine-tuning தற்போது East US 2 பகுதியில் உள்ள திட்டங்களில் ஆதரிக்கப்படுகிறது.

1. இடது பக்கத்திலுள்ள **Model catalog**-ஐ தேர்ந்தெடுக்கவும்.

1. **search bar**-இல் *phi-3* என type செய்து, நீங்கள் fine-tune செய்ய விரும்பும் phi-3 மாடலை தேர்ந்தெடுக்கவும்.

    ![FineTuneSelect](../../../../imgs/03/AIFoundry/select-model.png)

1. **Fine-tune** தேர்ந்தெடுக்கவும்.

    ![FineTuneSelect](../../../../imgs/03/AIFoundry/select-finetune.png)

1. **Fine-tuned model name** உள்ளிடவும்.

    ![FineTuneSelect](../../../../imgs/03/AIFoundry/finetune1.png)

1. **Next** தேர்ந்தெடுக்கவும்.

1. பின்வரும் பணிகளைச் செய்யவும்:

    - **task type**-ஐ **Chat completion**-ஆக தேர்ந்தெடுக்கவும்.
    - நீங்கள் பயன்படுத்த விரும்பும் **Training data**-ஐ தேர்ந்தெடுக்கவும். Azure AI Foundry தரவின் மூலம் அல்லது உங்கள் உள்ளூர் சூழலிலிருந்து அதை பதிவேற்றலாம்.

    ![FineTuneSelect](../../../../imgs/03/AIFoundry/finetune2.png)

1. **Next** தேர்ந்தெடுக்கவும்.

1. நீங்கள் பயன்படுத்த விரும்பும் **Validation data**-ஐ பதிவேற்றவும் அல்லது **Automatic split of training data**-ஐ தேர்ந்தெடுக்கவும்.

    ![FineTuneSelect](../../../../imgs/03/AIFoundry/finetune3.png)

1. **Next** தேர்ந்தெடுக்கவும்.

1. பின்வரும் பணிகளைச் செய்யவும்:

    - நீங்கள் பயன்படுத்த விரும்பும் **Batch size multiplier**-ஐ தேர்ந்தெடுக்கவும்.
    - நீங்கள் பயன்படுத்த விரும்பும் **Learning rate**-ஐ தேர்ந்தெடுக்கவும்.
    - நீங்கள் பயன்படுத்த விரும்பும் **Epochs**-ஐ தேர்ந்தெடுக்கவும்.

    ![FineTuneSelect](../../../../imgs/03/AIFoundry/finetune4.png)

1. Fine-tuning செயல்முறையை தொடங்க **Submit** தேர்ந்தெடுக்கவும்.

    ![FineTuneSelect](../../../../imgs/03/AIFoundry/select-submit.png)

1. உங்கள் மாடல் fine-tuned ஆனவுடன், நிலை **Completed** எனக் காட்டப்படும். இப்போது நீங்கள் மாடலை deploy செய்து, உங்கள் சொந்த பயன்பாட்டில், playground-இல், அல்லது prompt flow-இல் பயன்படுத்தலாம். மேலும் தகவலுக்கு [Azure AI Foundry மூலம் Phi-3 குடும்ப சிறிய மொழி மாடல்களை deploy செய்வது எப்படி](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) பார்க்கவும்.

    ![FineTuneSelect](../../../../imgs/03/AIFoundry/completed.png)

> [!NOTE]
> Phi-3 மாடல்களை fine-tuning செய்ய மேலும் விரிவான தகவலுக்கு [Fine-tune Phi-3 models in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini) பார்க்கவும்.

## Fine-tuned மாடல்களை சுத்தம் செய்தல்

Fine-tuning மாடல் பட்டியலில் இருந்து [Azure AI Foundry](https://ai.azure.com) அல்லது மாடல் விவர பக்கம் மூலம் fine-tuned மாடலை நீக்கலாம். Fine-tuning பக்கத்தில் fine-tuned மாடலை தேர்ந்தெடுத்து, Delete பொத்தானை அழுத்தி மாடலை நீக்கவும்.

> [!NOTE]
> Deployment உள்ள custom மாடலை நீக்க முடியாது. முதலில் உங்கள் மாடல் deployment-ஐ நீக்க வேண்டும், பின்னர் உங்கள் custom மாடலை நீக்கலாம்.

## செலவு மற்றும் ஒதுக்கீடுகள்

### Phi-3 மாடல்களை fine-tuning சேவையாக செய்யும் செலவு மற்றும் ஒதுக்கீடு கருத்துக்கள்

Phi மாடல்கள் Microsoft மூலம் fine-tuning சேவையாக வழங்கப்பட்டு Azure AI Foundry உடன் ஒருங்கிணைக்கப்பட்டுள்ளன. [Deploying](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) அல்லது மாடல்களை fine-tuning செய்யும்போது, deployment wizard இல் Pricing and terms tab-இல் விலை விவரங்களை காணலாம்.

## உள்ளடக்க வடிகட்டி

Pay-as-you-go சேவையாக deploy செய்யப்பட்ட மாடல்கள் Azure AI Content Safety மூலம் பாதுகாக்கப்படுகின்றன. Real-time endpoints-க்கு deploy செய்யும்போது, இந்த திறனை opt-out செய்யலாம். Azure AI content safety செயல்படுத்தப்பட்டால், prompt மற்றும் completion இரண்டும் தீங்கு விளைவிக்கும் உள்ளடக்கத்தை கண்டறிந்து தடுக்க classification மாடல்களின் தொகுப்பின் மூலம் செல்கின்றன. உள்ளீடு prompt மற்றும் வெளியீடு completions இரண்டிலும் தீங்கு விளைவிக்கும் உள்ளடக்கத்தை கண்டறிந்து நடவடிக்கை எடுக்கும் content filtering system செயல்படுகிறது. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering) பற்றி மேலும் அறிக.

**Fine-Tuning Configuration**

Hyperparameters: Learning rate, batch size, மற்றும் training epochs போன்ற hyperparameters-ஐ வரையறுக்கவும்.

**Loss Function**

உங்கள் பணிக்கான loss function (e.g., cross-entropy) தேர்ந்தெடுக்கவும்.

**Optimizer**

Training போது gradient updates கான optimizer (e.g., Adam) தேர்ந்தெடுக்கவும்.

**Fine-Tuning Process**

- Pre-Trained Model Load: Phi-3 Mini checkpoint-ஐ load செய்யவும்.
- Custom Layers Add: Task-specific layers (e.g., chat instructions கான classification head) சேர்க்கவும்.

**Train the Model**
உங்கள் dataset-ஐ பயன்படுத்தி மாடலை fine-tune செய்யவும். Training முன்னேற்றத்தை கண்காணித்து, தேவையான hyperparameters-ஐ சரிசெய்யவும்.

**Evaluation and Validation**

Validation Set: உங்கள் தரவுகளை training மற்றும் validation sets-ஆக பிரிக்கவும்.

**Evaluate Performance**

Accuracy, F1-score, அல்லது perplexity போன்ற metrics-ஐ பயன்படுத்தி மாடல் செயல்திறனை மதிப்பீடு செய்யவும்.

## Fine-Tuned Model Save

**Checkpoint**
Fine-tuned மாடல் checkpoint-ஐ எதிர்கால பயன்பாட்டிற்காக சேமிக்கவும்.

## Deployment

- Web Service ஆக Deploy செய்யவும்: Azure AI Foundry இல் உங்கள் fine-tuned மாடலை web service ஆக deploy செய்யவும்.
- Endpoint Test செய்யவும்: Deploy செய்யப்பட்ட endpoint-க்கு test queries அனுப்பி அதன் செயல்பாட்டை உறுதிப்படுத்தவும்.

## Iterate and Improve

Iterate: செயல்திறன் திருப்திகரமாக இல்லையெனில், hyperparameters-ஐ சரிசெய்தல், கூடுதல் தரவுகளை சேர்த்தல், அல்லது கூடுதல் epochs கான fine-tuning மூலம் iterate செய்யவும்.

## Monitor and Refine

மாடலின் நடத்தை தொடர்ந்து கண்காணித்து, தேவையான மாற்றங்களைச் செய்யவும்.

## Customize and Extend

Custom Tasks: Chat instructions தவிர Phi-3 Mini மாடலை பல்வேறு பணிகளுக்கு fine-tune செய்யலாம். பிற பயன்பாடுகளை ஆராயவும்!
Experiment: செயல்திறனை மேம்படுத்த architecture, layer combinations, மற்றும் techniques-ஐ முயற்சிக்கவும்.

> [!NOTE]
> Fine-tuning என்பது ஒரு iteration செயல்முறை. முயற்சி செய்யவும், கற்றுக்கொள்ளவும், மற்றும் உங்கள் குறிப்பிட்ட பணிக்கான சிறந்த முடிவுகளை அடைய உங்கள் மாடலை மாற்றவும்!

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியக்க மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளுங்கள். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.