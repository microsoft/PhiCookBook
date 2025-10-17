<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a853c08e4ee25ef9b4bfcedd8990da",
  "translation_date": "2025-10-11T12:07:27+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "ta"
}
-->
# Azure AI Foundry-இல் Microsoft-இன் பொறுப்பான AI கொள்கைகளை மையமாகக் கொண்டு Fine-tuned Phi-3 / Phi-3.5 மாடலை மதிப்பீடு செய்யுங்கள்

இந்த முழுமையான (E2E) மாதிரி Microsoft Tech Community-இல் உள்ள "[Azure AI Foundry-இல் Fine-tuned Phi-3 / 3.5 மாடல்களை Microsoft-இன் பொறுப்பான AI-ஐ மையமாகக் கொண்டு மதிப்பீடு செய்யுங்கள்](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" என்ற வழிகாட்டுதலின் அடிப்படையில் உருவாக்கப்பட்டுள்ளது.

## **கண்ணோட்டம்**

### Azure AI Foundry-இல் Fine-tuned Phi-3 / Phi-3.5 மாடலின் பாதுகாப்பு மற்றும் செயல்திறனை எப்படி மதிப்பீடு செய்யலாம்?

ஒரு மாடலை Fine-tune செய்வது சில நேரங்களில் எதிர்பாராத அல்லது தேவையற்ற பதில்களை உருவாக்கலாம். மாடல் பாதுகாப்பாகவும் பயனுள்ளதாகவும் இருக்க வேண்டும் என்பதை உறுதிப்படுத்த, அதன் தீங்கு விளைவிக்கும் உள்ளடக்கத்தை உருவாக்கும் திறனை மற்றும் துல்லியமான, தொடர்புடைய மற்றும் தெளிவான பதில்களை உருவாக்கும் திறனை மதிப்பீடு செய்வது முக்கியம். இந்த பயிற்சியில், Azure AI Foundry-இல் Prompt flow-இன் மூலம் ஒருங்கிணைக்கப்பட்ட Fine-tuned Phi-3 / Phi-3.5 மாடலின் பாதுகாப்பு மற்றும் செயல்திறனை மதிப்பீடு செய்வது எப்படி என்பதை நீங்கள் கற்றுக்கொள்வீர்கள்.

Azure AI Foundry-இன் மதிப்பீட்டு செயல்முறை இங்கே உள்ளது.

![பயிற்சியின் கட்டமைப்பு.](../../../../../../imgs/02/Evaluation-AIFoundry/architecture.png)

*படத்தின் மூலமாக: [உருவாக்கும் AI பயன்பாடுகளின் மதிப்பீடு](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Phi-3 / Phi-3.5 பற்றிய கூடுதல் தகவல்களை ஆராய்வதற்கும், மேலும் வளங்களைப் பெறுவதற்கும், [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723) ஐ பார்வையிடவும்.

### **முன்னோட்டம்**

- [Python](https://www.python.org/downloads)
- [Azure subscription](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Fine-tuned Phi-3 / Phi-3.5 மாடல்

### **உள்ளடக்க அட்டவணை**

1. [**காட்சி 1: Azure AI Foundry-இன் Prompt flow மதிப்பீட்டுக்கான அறிமுகம்**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [பாதுகாப்பு மதிப்பீட்டுக்கான அறிமுகம்](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [செயல்திறன் மதிப்பீட்டுக்கான அறிமுகம்](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**காட்சி 2: Azure AI Foundry-இல் Phi-3 / Phi-3.5 மாடலை மதிப்பீடு செய்வது**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [தொடங்குவதற்கு முன்](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Phi-3 / Phi-3.5 மாடலை மதிப்பீடு செய்ய Azure OpenAI-ஐ பிரயோகிக்கவும்](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Azure AI Foundry-இன் Prompt flow மதிப்பீட்டின் மூலம் Fine-tuned Phi-3 / Phi-3.5 மாடலை மதிப்பீடு செய்யுங்கள்](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [வாழ்த்துக்கள்!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **காட்சி 1: Azure AI Foundry-இன் Prompt flow மதிப்பீட்டுக்கான அறிமுகம்**

### **பாதுகாப்பு மதிப்பீட்டுக்கான அறிமுகம்**

உங்கள் AI மாடல் நெறிமுறைகளுக்கு ஏற்பவும் பாதுகாப்பாகவும் இருக்க வேண்டும் என்பதை உறுதிப்படுத்த Microsoft-இன் பொறுப்பான AI கொள்கைகளை எதிர்கொள்ள மதிப்பீடு செய்வது முக்கியம். Azure AI Foundry-இல், பாதுகாப்பு மதிப்பீடுகள் உங்கள் மாடலின் jailbreak தாக்குதல்களுக்கு எதிரான பாதிப்பையும், தீங்கு விளைவிக்கும் உள்ளடக்கத்தை உருவாக்கும் திறனையும் மதிப்பீடு செய்ய உதவுகின்றன, இது இந்த கொள்கைகளுடன் நேரடியாக இணைக்கப்பட்டுள்ளது.

![பாதுகாப்பு மதிப்பீடு.](../../../../../../imgs/02/Evaluation-AIFoundry/safety-evaluation.png)

*படத்தின் மூலமாக: [உருவாக்கும் AI பயன்பாடுகளின் மதிப்பீடு](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### **Microsoft-இன் பொறுப்பான AI கொள்கைகள்**

தொழில்நுட்ப நடவடிக்கைகளைத் தொடங்குவதற்கு முன், Microsoft-இன் பொறுப்பான AI கொள்கைகளைப் புரிந்துகொள்வது முக்கியம். இது AI அமைப்புகளை பொறுப்புடன் உருவாக்கவும், பிரயோகிக்கவும், இயக்கவும் வழிகாட்டும் ஒரு நெறிமுறை அமைப்பாகும். இந்த கொள்கைகள் AI அமைப்புகளை நியாயமான, வெளிப்படையான மற்றும் உள்ளடக்கிய முறையில் உருவாக்குவதற்கான வழிகாட்டுதலாக செயல்படுகின்றன. AI மாடல்களின் பாதுகாப்பை மதிப்பீடு செய்வதற்கான அடிப்படையாக இந்த கொள்கைகள் உள்ளன.

Microsoft-இன் பொறுப்பான AI கொள்கைகள்:

- **நியாயம் மற்றும் உள்ளடக்கம்**: AI அமைப்புகள் அனைவரையும் நியாயமாக நடத்த வேண்டும் மற்றும் ஒரே நிலைமையில் உள்ள குழுக்களை வேறுபடுத்தாமல் இருக்க வேண்டும். உதாரணமாக, மருத்துவ சிகிச்சை, கடன் விண்ணப்பங்கள் அல்லது வேலை வாய்ப்புகள் குறித்து AI அமைப்புகள் வழிகாட்டும்போது, ஒரே அறிகுறிகள், நிதி சூழ்நிலைகள் அல்லது தொழில்முறை தகுதிகள் உள்ள அனைவருக்கும் ஒரே பரிந்துரைகளை வழங்க வேண்டும்.

- **நம்பகத்தன்மை மற்றும் பாதுகாப்பு**: நம்பகத்தன்மையை உருவாக்க, AI அமைப்புகள் நம்பகமாகவும், பாதுகாப்பாகவும், தொடர்ந்து செயல்பட வேண்டும். இந்த அமைப்புகள் தங்கள் வடிவமைப்பின் அடிப்படையில் செயல்படவும், எதிர்பாராத சூழ்நிலைகளுக்கு பாதுகாப்பாக பதிலளிக்கவும், தீங்கு விளைவிக்கும் மாற்றங்களை எதிர்க்கவும் வேண்டும்.

- **வெளிப்படைத்தன்மை**: AI அமைப்புகள் மக்களின் வாழ்க்கையில் பெரிய தாக்கங்களை ஏற்படுத்தும் முடிவுகளைத் தகவமைக்க உதவும்போது, அந்த முடிவுகள் எவ்வாறு எடுக்கப்பட்டன என்பதை மக்கள் புரிந்துகொள்ள வேண்டும்.

- **தனியுரிமை மற்றும் பாதுகாப்பு**: AI பரவலாகப் பயன்படும் போது, தனியுரிமையைப் பாதுகாப்பதும், தனிப்பட்ட மற்றும் வணிகத் தகவல்களைப் பாதுகாப்பதும் முக்கியமாகவும் சிக்கலாகவும் மாறுகிறது.

- **பொறுப்புத்தன்மை**: AI அமைப்புகளை வடிவமைக்கும் மற்றும் பிரயோகிக்கும் நபர்கள், அவற்றின் செயல்பாடுகளுக்கு பொறுப்பாக இருக்க வேண்டும்.

![Fill hub.](../../../../../../imgs/02/Evaluation-AIFoundry/responsibleai2.png)

*படத்தின் மூலமாக: [பொறுப்பான AI என்றால் என்ன?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Microsoft-இன் பொறுப்பான AI கொள்கைகள் பற்றி மேலும் அறிய, [பொறுப்பான AI என்றால் என்ன?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723) ஐ பார்வையிடவும்.

#### **பாதுகாப்பு அளவுகோல்கள்**

இந்த பயிற்சியில், Azure AI Foundry-இன் பாதுகாப்பு அளவுகோல்களைப் பயன்படுத்தி Fine-tuned Phi-3 மாடலின் பாதுகாப்பை மதிப்பீடு செய்வீர்கள். இந்த அளவுகோல்கள் மாடல் தீங்கு விளைவிக்கும் உள்ளடக்கத்தை உருவாக்கும் திறனை மற்றும் jailbreak தாக்குதல்களுக்கு எதிரான பாதிப்பை மதிப்பீடு செய்ய உதவுகின்றன. பாதுகாப்பு அளவுகோல்கள்:

- **சுயதீங்கு தொடர்பான உள்ளடக்கம்**: மாடல் சுயதீங்கு தொடர்பான உள்ளடக்கத்தை உருவாக்கும்倾向ம் உள்ளதா என்பதை மதிப்பீடு செய்கிறது.
- **வெறுப்பான மற்றும் அநியாயமான உள்ளடக்கம்**: மாடல் வெறுப்பான அல்லது அநியாயமான உள்ளடக்கத்தை உருவாக்கும்倾向ம் உள்ளதா என்பதை மதிப்பீடு செய்கிறது.
- **வன்முறை உள்ளடக்கம்**: மாடல் வன்முறை உள்ளடக்கத்தை உருவாக்கும்倾向ம் உள்ளதா என்பதை மதிப்பீடு செய்கிறது.
- **காமத்தன்மை உள்ளடக்கம்**: மாடல் பொருத்தமற்ற காமத்தன்மை உள்ளடக்கத்தை உருவாக்கும்倾向ம் உள்ளதா என்பதை மதிப்பீடு செய்கிறது.

இந்த அம்சங்களை மதிப்பீடு செய்வது AI மாடல் தீங்கு விளைவிக்கும் அல்லது ஆபத்தான உள்ளடக்கத்தை உருவாக்காமல் இருப்பதை உறுதிப்படுத்துகிறது.

![பாதுகாப்பின் அடிப்படையில் மதிப்பீடு செய்யுங்கள்.](../../../../../../imgs/02/Evaluation-AIFoundry/evaluate-based-on-safety.png)

### **செயல்திறன் மதிப்பீட்டுக்கான அறிமுகம்**

உங்கள் AI மாடல் எதிர்பார்த்தபடி செயல்படுகிறதா என்பதை உறுதிப்படுத்த, செயல்திறன் அளவுகோல்களை எதிர்கொள்ள மதிப்பீடு செய்வது முக்கியம். Azure AI Foundry-இல், செயல்திறன் மதிப்பீடுகள் உங்கள் மாடல் துல்லியமான, தொடர்புடைய மற்றும் தெளிவான பதில்களை உருவாக்கும் திறனை மதிப்பீடு செய்ய உதவுகின்றன.

![செயல்திறன் மதிப்பீடு.](../../../../../../imgs/02/Evaluation-AIFoundry/performance-evaluation.png)

*படத்தின் மூலமாக: [உருவாக்கும் AI பயன்பாடுகளின் மதிப்பீடு](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### **செயல்திறன் அளவுகோல்கள்**

இந்த பயிற்சியில், Azure AI Foundry-இன் செயல்திறன் அளவுகோல்களைப் பயன்படுத்தி Fine-tuned Phi-3 / Phi-3.5 மாடலின் செயல்திறனை மதிப்பீடு செய்வீர்கள். இந்த அளவுகோல்கள் மாடல் துல்லியமான, தொடர்புடைய மற்றும் தெளிவான பதில்களை உருவாக்கும் திறனை மதிப்பீடு செய்ய உதவுகின்றன. செயல்திறன் அளவுகோல்கள்:

- **Groundedness**: உருவாக்கப்பட்ட பதில்கள் உள்ளீட்டு மூலத்திலிருந்து தகவலுடன் எவ்வளவு நன்கு பொருந்துகின்றன என்பதை மதிப்பீடு செய்கிறது.
- **Relevance**: கொடுக்கப்பட்ட கேள்விகளுக்கு உருவாக்கப்பட்ட பதில்களின் தொடர்பு பொருத்தத்தை மதிப்பீடு செய்கிறது.
- **Coherence**: உருவாக்கப்பட்ட உரை எவ்வளவு மென்மையாக ஓடுகிறது, இயற்கையாக படிக்கிறது மற்றும் மனித மொழியைப் போன்றது என்பதை மதிப்பீடு செய்கிறது.
- **Fluency**: உருவாக்கப்பட்ட உரையின் மொழி திறமையை மதிப்பீடு செய்கிறது.
- **GPT Similarity**: உருவாக்கப்பட்ட பதிலை தரவின் உண்மையுடன் ஒப்பிடுகிறது.
- **F1 Score**: உருவாக்கப்பட்ட பதில் மற்றும் மூல தரவின் இடையே பகிரப்பட்ட சொற்களின் விகிதத்தை கணக்கிடுகிறது.

இந்த அளவுகோல்கள் மாடல் துல்லியமான, தொடர்புடைய மற்றும் தெளிவான பதில்களை உருவாக்கும் திறனை மதிப்பீடு செய்ய உதவுகின்றன.

![செயல்திறனின் அடிப்படையில் மதிப்பீடு செய்யுங்கள்.](../../../../../../imgs/02/Evaluation-AIFoundry/evaluate-based-on-performance.png)

## **காட்சி 2: Azure AI Foundry-இல் Phi-3 / Phi-3.5 மாடலை மதிப்பீடு செய்வது**

### **தொடங்குவதற்கு முன்**

இந்த பயிற்சி முந்தைய வலைப்பதிவுகளின் தொடர்ச்சியாகும், "[Prompt Flow உடன் Custom Phi-3 மாடல்களை Fine-Tune மற்றும் ஒருங்கிணைக்கவும்: படிப்படியாக வழிகாட்டுதல்](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" மற்றும் "[Azure AI Foundry-இல் Prompt Flow உடன் Custom Phi-3 மாடல்களை Fine-Tune மற்றும் ஒருங்கிணைக்கவும்](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." இந்த பதிவுகளில், Azure AI Foundry-இல் Phi-3 / Phi-3.5 மாடலை Fine-tune செய்வதற்கும் Prompt flow உடன் ஒருங்கிணைப்பதற்கும் செயல்முறையை நாங்கள் விவரித்தோம்.

இந்த பயிற்சியில், Azure AI Foundry-இல் Fine-tuned Phi-3 / Phi-3.5 மாடலை மதிப்பீடு செய்ய Azure OpenAI மாடலை மதிப்பீட்டாளராக பிரயோகிக்கவும்.

இந்த பயிற்சியைத் தொடங்குவதற்கு முன், முந்தைய பயிற்சிகளில் விவரிக்கப்பட்ட முன்னோட்டங்களை நீங்கள் கொண்டிருக்க வேண்டும்:

1. Fine-tuned Phi-3 / Phi-3.5 மாடலை மதிப்பீடு செய்ய தயாரிக்கப்பட்ட தரவுத்தொகுப்பு.
1. Azure Machine Learning-இல் Fine-tune செய்யப்பட்ட மற்றும் பிரயோகிக்கப்பட்ட Phi-3 / Phi-3.5 மாடல்.
1. Azure AI Foundry-இல் Prompt flow உடன் ஒருங்கிணைக்கப்பட்ட Fine-tuned Phi-3 / Phi-3.5 மாடல்.

> [!NOTE]
> முந்தைய வலைப்பதிவுகளில் பதிவிறக்கம் செய்யப்பட்ட **ULTRACHAT_200k** தரவுத்தொகுப்பிலிருந்து data கோப்பில் உள்ள *test_data.jsonl* கோப்பை Fine-tuned Phi-3 / Phi-3.5 மாடலை மதிப்பீடு செய்ய தரவுத்தொகுப்பாக நீங்கள் பயன்படுத்துவீர்கள்.

#### **Prompt flow உடன் Custom Phi-3 / Phi-3.5 மாடலை Azure AI Foundry-இல் ஒருங்கிணைக்கவும் (Code first approach)**

> [!NOTE]
> "[Azure AI Foundry-இல் Prompt Flow உடன் Custom Phi-3 மாடல்களை Fine-Tune மற்றும் ஒருங்கிணைக்கவும்](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)" என்ற குறைந்த குறியீட்டு அணுகுமுறையை நீங்கள் பின்பற்றியிருந்தால், இந்த பயிற்சியை தவிர்த்து அடுத்த பயிற்சிக்கு செல்லலாம்.
> ஆனால், "[Prompt Flow உடன் Custom Phi-3 மாடல்களை Fine-Tune மற்றும் ஒருங்கிணைக்கவும்: படிப்படியாக வழிகாட்டுதல்](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" என்ற Code-first அணுகுமுறையை நீங்கள் பின்பற்றியிருந்தால், Prompt flow-க்கு உங்கள் மாடலை இணைக்கும் செயல்முறை sedikit வேறுபட்டது. இந்த செயல்முறையை இந்த பயிற்சியில் நீங்கள் கற்றுக்கொள்வீர்கள்.

Fine-tuned Phi-3 / Phi-3.5 மாடலை Azure AI Foundry-இல் Prompt flow-க்கு ஒருங்கிணைக்க நீங்கள் தொடர வேண்டும்.

#### **Azure AI Foundry Hub உருவாக்கவும்**

Hub உருவாக்குவதற்கு முன் Project உருவாக்க வேண்டும். Hub என்பது Resource Group போல செயல்படுகிறது, இது Azure AI Foundry-இல் பல Project-களை ஒழுங்குபடுத்தவும் நிர்வகிக்கவும் உதவுகிறது.

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)-இல் உள்நுழைக.

1. இடதுபுற தாவலில் **All hubs** ஐத் தேர்ந்தெடுக்கவும்.

1. வழிசெலுத்தல் மெனுவிலிருந்து **+ New hub** ஐத் தேர்ந்தெடுக்கவும்.

    ![Hub உருவாக்கவும்.](../../../../../../imgs/02/Evaluation-AIFoundry/create-hub.png)
1. பின்வரும் பணிகளைச் செய்யவும்:

    - **Hub name** உள்ளிடவும். இது தனித்துவமான மதிப்பாக இருக்க வேண்டும்.
    - உங்கள் Azure **Subscription** தேர்ந்தெடுக்கவும்.
    - பயன்படுத்த வேண்டிய **Resource group** தேர்ந்தெடுக்கவும் (தேவையெனில் புதியது உருவாக்கவும்).
    - நீங்கள் பயன்படுத்த விரும்பும் **Location** தேர்ந்தெடுக்கவும்.
    - **Connect Azure AI Services** தேர்ந்தெடுக்கவும் (தேவையெனில் புதியது உருவாக்கவும்).
    - **Connect Azure AI Search** தேர்ந்தெடுத்து **Skip connecting** செய்யவும்.

    ![Hub நிரப்பவும்.](../../../../../../imgs/02/Evaluation-AIFoundry/fill-hub.png)

1. **Next** தேர்ந்தெடுக்கவும்.

#### Azure AI Foundry Project உருவாக்கவும்

1. நீங்கள் உருவாக்கிய Hub-இல், இடது பக்கத்திலுள்ள தாவலில் **All projects** தேர்ந்தெடுக்கவும்.

1. வழிசெலுத்தல் மெனுவில் **+ New project** தேர்ந்தெடுக்கவும்.

    ![புதிய Project தேர்ந்தெடுக்கவும்.](../../../../../../imgs/03/AIFoundry/select-new-project.png)

1. **Project name** உள்ளிடவும். இது தனித்துவமான மதிப்பாக இருக்க வேண்டும்.

    ![Project உருவாக்கவும்.](../../../../../../imgs/03/AIFoundry/create-project.png)

1. **Create a project** தேர்ந்தெடுக்கவும்.

#### Fine-tuned Phi-3 / Phi-3.5 மாடலுக்கான தனிப்பயன் இணைப்பைச் சேர்க்கவும்

உங்கள் தனிப்பயன் Phi-3 / Phi-3.5 மாடலை Prompt flow-இன் மூலம் ஒருங்கிணைக்க, மாடலின் endpoint மற்றும் key-ஐ தனிப்பயன் இணைப்பில் சேமிக்க வேண்டும். இந்த அமைப்பு Prompt flow-இல் உங்கள் தனிப்பயன் Phi-3 / Phi-3.5 மாடலுக்கு அணுகலை உறுதிசெய்கிறது.

#### Fine-tuned Phi-3 / Phi-3.5 மாடலின் api key மற்றும் endpoint uri அமைக்கவும்

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) ஐ பார்வையிடவும்.

1. நீங்கள் உருவாக்கிய Azure Machine learning workspace-க்கு செல்லவும்.

1. இடது பக்கத்திலுள்ள தாவலில் **Endpoints** தேர்ந்தெடுக்கவும்.

    ![Endpoints தேர்ந்தெடுக்கவும்.](../../../../../../imgs/02/Evaluation-AIFoundry/select-endpoints.png)

1. நீங்கள் உருவாக்கிய endpoint-ஐ தேர்ந்தெடுக்கவும்.

    ![உருவாக்கிய endpoint-ஐ தேர்ந்தெடுக்கவும்.](../../../../../../imgs/02/Evaluation-AIFoundry/select-endpoint-created.png)

1. வழிசெலுத்தல் மெனுவில் **Consume** தேர்ந்தெடுக்கவும்.

1. உங்கள் **REST endpoint** மற்றும் **Primary key** ஐ நகலெடுக்கவும்.

    ![api key மற்றும் endpoint uri நகலெடுக்கவும்.](../../../../../../imgs/02/Evaluation-AIFoundry/copy-endpoint-key.png)

#### Custom Connection சேர்க்கவும்

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) ஐ பார்வையிடவும்.

1. நீங்கள் உருவாக்கிய Azure AI Foundry project-க்கு செல்லவும்.

1. நீங்கள் உருவாக்கிய Project-இல், இடது பக்கத்திலுள்ள தாவலில் **Settings** தேர்ந்தெடுக்கவும்.

1. **+ New connection** தேர்ந்தெடுக்கவும்.

    ![புதிய இணைப்பு தேர்ந்தெடுக்கவும்.](../../../../../../imgs/02/Evaluation-AIFoundry/select-new-connection.png)

1. வழிசெலுத்தல் மெனுவில் **Custom keys** தேர்ந்தெடுக்கவும்.

    ![Custom keys தேர்ந்தெடுக்கவும்.](../../../../../../imgs/02/Evaluation-AIFoundry/select-custom-keys.png)

1. பின்வரும் பணிகளைச் செய்யவும்:

    - **+ Add key value pairs** தேர்ந்தெடுக்கவும்.
    - Key name-க்கு **endpoint** என உள்ளிடவும் மற்றும் Azure ML Studio-இல் நீங்கள் நகலெடுத்த endpoint-ஐ value புலத்தில் ஒட்டவும்.
    - மீண்டும் **+ Add key value pairs** தேர்ந்தெடுக்கவும்.
    - Key name-க்கு **key** என உள்ளிடவும் மற்றும் Azure ML Studio-இல் நீங்கள் நகலெடுத்த key-ஐ value புலத்தில் ஒட்டவும்.
    - Keys சேர்த்த பிறகு, **is secret** தேர்ந்தெடுத்து key வெளிப்படாமல் இருக்கச் செய்யவும்.

    ![இணைப்பு சேர்க்கவும்.](../../../../../../imgs/02/Evaluation-AIFoundry/add-connection.png)

1. **Add connection** தேர்ந்தெடுக்கவும்.

#### Prompt flow உருவாக்கவும்

நீங்கள் Azure AI Foundry-இல் ஒரு custom connection சேர்த்துள்ளீர்கள். இப்போது, பின்வரும் படிகளைப் பயன்படுத்தி Prompt flow உருவாக்குவோம். பின்னர், Prompt flow-இல் fine-tuned மாடலைப் பயன்படுத்த இந்த custom connection-ஐ இணைப்போம்.

1. நீங்கள் உருவாக்கிய Azure AI Foundry project-க்கு செல்லவும்.

1. இடது பக்கத்திலுள்ள தாவலில் **Prompt flow** தேர்ந்தெடுக்கவும்.

1. வழிசெலுத்தல் மெனுவில் **+ Create** தேர்ந்தெடுக்கவும்.

    ![Promptflow தேர்ந்தெடுக்கவும்.](../../../../../../imgs/02/Evaluation-AIFoundry/select-promptflow.png)

1. வழிசெலுத்தல் மெனுவில் **Chat flow** தேர்ந்தெடுக்கவும்.

    ![Chat flow தேர்ந்தெடுக்கவும்.](../../../../../../imgs/02/Evaluation-AIFoundry/select-flow-type.png)

1. பயன்படுத்த **Folder name** உள்ளிடவும்.

    ![Chat flow தேர்ந்தெடுக்கவும்.](../../../../../../imgs/02/Evaluation-AIFoundry/enter-name.png)

1. **Create** தேர்ந்தெடுக்கவும்.

#### Prompt flow-ஐ உங்கள் custom Phi-3 / Phi-3.5 மாடலுடன் உரையாட அமைக்கவும்

Fine-tuned Phi-3 / Phi-3.5 மாடலை Prompt flow-இல் ஒருங்கிணைக்க வேண்டும். இருப்பினும், வழங்கப்பட்ட Prompt flow இதற்காக வடிவமைக்கப்படவில்லை. எனவே, custom மாடலை ஒருங்கிணைக்க Prompt flow-ஐ மறுவடிவமைக்க வேண்டும்.

1. Prompt flow-இல், பின்வரும் பணிகளைச் செய்யவும்:

    - **Raw file mode** தேர்ந்தெடுக்கவும்.
    - *flow.dag.yml* கோப்பில் உள்ள அனைத்து உள்ளடக்கங்களையும் நீக்கவும்.
    - *flow.dag.yml* கோப்பில் பின்வரும் குறியீட்டைச் சேர்க்கவும்.

        ```yml
        inputs:
          input_data:
            type: string
            default: "Who founded Microsoft?"

        outputs:
          answer:
            type: string
            reference: ${integrate_with_promptflow.output}

        nodes:
        - name: integrate_with_promptflow
          type: python
          source:
            type: code
            path: integrate_with_promptflow.py
          inputs:
            input_data: ${inputs.input_data}
        ```

    - **Save** தேர்ந்தெடுக்கவும்.

    ![Raw file mode தேர்ந்தெடுக்கவும்.](../../../../../../imgs/02/Evaluation-AIFoundry/select-raw-file-mode.png)

1. Prompt flow-இல் custom Phi-3 / Phi-3.5 மாடலைப் பயன்படுத்த *integrate_with_promptflow.py* கோப்பில் பின்வரும் குறியீட்டைச் சேர்க்கவும்.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    data = {
        "input_data": [input_data],
        "params": {
            "temperature": 0.7,
            "max_new_tokens": 128,
            "do_sample": True,
            "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # Log the full JSON response
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Prompt flow குறியீட்டை ஒட்டவும்.](../../../../../../imgs/02/Evaluation-AIFoundry/paste-promptflow-code.png)

> [!NOTE]
> Azure AI Foundry-இல் Prompt flow-ஐப் பயன்படுத்துவதற்கான விரிவான தகவலுக்கு, [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) ஐப் பார்க்கவும்.

1. **Chat input**, **Chat output** தேர்ந்தெடுத்து உங்கள் மாடலுடன் உரையாடலை இயக்கவும்.

    ![Input Output தேர்ந்தெடுக்கவும்.](../../../../../../imgs/02/Evaluation-AIFoundry/select-input-output.png)

1. இப்போது உங்கள் custom Phi-3 / Phi-3.5 மாடலுடன் உரையாட தயாராக உள்ளீர்கள். அடுத்த பயிற்சியில், Prompt flow-ஐ தொடங்குவது மற்றும் fine-tuned Phi-3 / Phi-3.5 மாடலுடன் உரையாட அதை பயன்படுத்துவது எப்படி என்பதை நீங்கள் கற்றுக்கொள்வீர்கள்.

> [!NOTE]
>
> மறுவடிவமைக்கப்பட்ட flow கீழே உள்ள படத்தைப் போன்றதாக இருக்க வேண்டும்:
>
> ![Flow எடுத்துக்காட்டு](../../../../../../imgs/02/Evaluation-AIFoundry/graph-example.png)
>

#### Prompt flow தொடங்கவும்

1. Prompt flow-ஐ தொடங்க **Start compute sessions** தேர்ந்தெடுக்கவும்.

    ![Compute session தொடங்கவும்.](../../../../../../imgs/02/Evaluation-AIFoundry/start-compute-session.png)

1. அளவுருக்களை புதுப்பிக்க **Validate and parse input** தேர்ந்தெடுக்கவும்.

    ![Input சரிபார்க்கவும்.](../../../../../../imgs/02/Evaluation-AIFoundry/validate-input.png)

1. நீங்கள் உருவாக்கிய custom connection-க்கு **connection**-இன் **Value** ஐ தேர்ந்தெடுக்கவும். உதாரணமாக, *connection*.

    ![Connection.](../../../../../../imgs/02/Evaluation-AIFoundry/select-connection.png)

#### உங்கள் custom Phi-3 / Phi-3.5 மாடலுடன் உரையாடவும்

1. **Chat** தேர்ந்தெடுக்கவும்.

    ![Chat தேர்ந்தெடுக்கவும்.](../../../../../../imgs/02/Evaluation-AIFoundry/select-chat.png)

1. இதோ ஒரு எடுத்துக்காட்டு: இப்போது உங்கள் custom Phi-3 / Phi-3.5 மாடலுடன் உரையாடலாம். Fine-tuning-க்கு பயன்படுத்திய தரவின் அடிப்படையில் கேள்விகள் கேட்க பரிந்துரைக்கப்படுகிறது.

    ![Prompt flow உடன் உரையாடவும்.](../../../../../../imgs/02/Evaluation-AIFoundry/chat-with-promptflow.png)

### Azure OpenAI-ஐ deploy செய்து Phi-3 / Phi-3.5 மாடலை மதிப்பீடு செய்யவும்

Azure AI Foundry-இல் Phi-3 / Phi-3.5 மாடலை மதிப்பீடு செய்ய, Azure OpenAI மாடலை deploy செய்ய வேண்டும். இந்த மாடல் Phi-3 / Phi-3.5 மாடலின் செயல்திறனை மதிப்பீடு செய்ய பயன்படுத்தப்படும்.

#### Azure OpenAI deploy செய்யவும்

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) இல் உள்நுழைக.

1. நீங்கள் உருவாக்கிய Azure AI Foundry project-க்கு செல்லவும்.

    ![Project தேர்ந்தெடுக்கவும்.](../../../../../../imgs/02/Evaluation-AIFoundry/select-project-created.png)

1. நீங்கள் உருவாக்கிய Project-இல், இடது பக்கத்திலுள்ள தாவலில் **Deployments** தேர்ந்தெடுக்கவும்.

1. வழிசெலுத்தல் மெனுவில் **+ Deploy model** தேர்ந்தெடுக்கவும்.

1. **Deploy base model** தேர்ந்தெடுக்கவும்.

    ![Deployments தேர்ந்தெடுக்கவும்.](../../../../../../imgs/02/Evaluation-AIFoundry/deploy-openai-model.png)

1. நீங்கள் பயன்படுத்த விரும்பும் Azure OpenAI மாடலை தேர்ந்தெடுக்கவும். உதாரணமாக, **gpt-4o**.

    ![Azure OpenAI மாடலை தேர்ந்தெடுக்கவும்.](../../../../../../imgs/02/Evaluation-AIFoundry/select-openai-model.png)

1. **Confirm** தேர்ந்தெடுக்கவும்.

### Azure AI Foundry-இன் Prompt flow மதிப்பீடு மூலம் fine-tuned Phi-3 / Phi-3.5 மாடலை மதிப்பீடு செய்யவும்

### புதிய மதிப்பீட்டை தொடங்கவும்

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) ஐ பார்வையிடவும்.

1. நீங்கள் உருவாக்கிய Azure AI Foundry project-க்கு செல்லவும்.

    ![Project தேர்ந்தெடுக்கவும்.](../../../../../../imgs/02/Evaluation-AIFoundry/select-project-created.png)

1. நீங்கள் உருவாக்கிய Project-இல், இடது பக்கத்திலுள்ள தாவலில் **Evaluation** தேர்ந்தெடுக்கவும்.

1. வழிசெலுத்தல் மெனுவில் **+ New evaluation** தேர்ந்தெடுக்கவும்.

    ![Evaluation தேர்ந்தெடுக்கவும்.](../../../../../../imgs/02/Evaluation-AIFoundry/select-evaluation.png)

1. **Prompt flow** மதிப்பீட்டை தேர்ந்தெடுக்கவும்.

    ![Prompt flow மதிப்பீட்டை தேர்ந்தெடுக்கவும்.](../../../../../../imgs/02/Evaluation-AIFoundry/promptflow-evaluation.png)

1. பின்வரும் பணிகளைச் செய்யவும்:

    - மதிப்பீட்டு பெயரை உள்ளிடவும். இது தனித்துவமான மதிப்பாக இருக்க வேண்டும்.
    - Task type-ஐ **Question and answer without context** என தேர்ந்தெடுக்கவும். ஏனெனில், இந்த பயிற்சியில் பயன்படுத்தப்படும் **UlTRACHAT_200k** dataset context-ஐ கொண்டிருக்கவில்லை.
    - நீங்கள் மதிப்பீடு செய்ய விரும்பும் Prompt flow-ஐ தேர்ந்தெடுக்கவும்.

    ![Prompt flow மதிப்பீட்டு அமைப்பு.](../../../../../../imgs/02/Evaluation-AIFoundry/evaluation-setting1.png)

1. **Next** தேர்ந்தெடுக்கவும்.

1. பின்வரும் பணிகளைச் செய்யவும்:

    - **Add your dataset** தேர்ந்தெடுத்து dataset-ஐ upload செய்யவும். உதாரணமாக, **ULTRACHAT_200k** dataset-ஐ download செய்யும்போது சேர்க்கப்படும் *test_data.json1* போன்ற test dataset கோப்பை upload செய்யலாம்.
    - உங்கள் dataset-க்கு பொருந்தும் **Dataset column**-ஐ தேர்ந்தெடுக்கவும். உதாரணமாக, **ULTRACHAT_200k** dataset-ஐ பயன்படுத்தினால், **${data.prompt}**-ஐ dataset column-ஆக தேர்ந்தெடுக்கவும்.

    ![Prompt flow மதிப்பீட்டு அமைப்பு.](../../../../../../imgs/02/Evaluation-AIFoundry/evaluation-setting2.png)

1. **Next** தேர்ந்தெடுக்கவும்.

1. செயல்திறன் மற்றும் தரமான அளவுகோள்களை அமைக்க பின்வரும் பணிகளைச் செய்யவும்:

    - நீங்கள் பயன்படுத்த விரும்பும் செயல்திறன் மற்றும் தரமான அளவுகோள்களை தேர்ந்தெடுக்கவும்.
    - மதிப்பீட்டுக்காக நீங்கள் உருவாக்கிய Azure OpenAI மாடலை தேர்ந்தெடுக்கவும். உதாரணமாக, **gpt-4o**-ஐ தேர்ந்தெடுக்கவும்.

    ![Prompt flow மதிப்பீட்டு அமைப்பு.](../../../../../../imgs/02/Evaluation-AIFoundry/evaluation-setting3-1.png)

1. அபாயம் மற்றும் பாதுகாப்பு அளவுகோள்களை அமைக்க பின்வரும் பணிகளைச் செய்யவும்:

    - நீங்கள் பயன்படுத்த விரும்பும் அபாயம் மற்றும் பாதுகாப்பு அளவுகோள்களை தேர்ந்தெடுக்கவும்.
    - நீங்கள் பயன்படுத்த விரும்பும் defect rate-ஐ கணக்கிட threshold-ஐ தேர்ந்தெடுக்கவும். உதாரணமாக, **Medium**-ஐ தேர்ந்தெடுக்கவும்.
    - **question**-க்கு **Data source**-ஐ **{$data.prompt}** என அமைக்கவும்.
    - **answer**-க்கு **Data source**-ஐ **{$run.outputs.answer}** என அமைக்கவும்.
    - **ground_truth**-க்கு **Data source**-ஐ **{$data.message}** என அமைக்கவும்.

    ![Prompt flow மதிப்பீட்டு அமைப்பு.](../../../../../../imgs/02/Evaluation-AIFoundry/evaluation-setting3-2.png)

1. **Next** தேர்ந்தெடுக்கவும்.

1. மதிப்பீட்டை தொடங்க **Submit** தேர்ந்தெடுக்கவும்.

1. மதிப்பீட்டை முடிக்க சில நேரம் ஆகும். **Evaluation** தாவலில் முன்னேற்றத்தை கண்காணிக்கலாம்.

### மதிப்பீட்டு முடிவுகளை மதிப்பாய்வு செய்யவும்

> [!NOTE]
> கீழே வழங்கப்பட்ட முடிவுகள் மதிப்பீட்டு செயல்முறையை விளக்குவதற்காக மட்டுமே. இந்த பயிற்சியில், சிறிய dataset-இல் fine-tuned செய்யப்பட்ட மாடலை பயன்படுத்தியுள்ளோம், இது குறைவான முடிவுகளை ஏற்படுத்தக்கூடும். dataset-இன் அளவு, தரம், மற்றும் பல்வகைமை, மற்றும் மாடலின் குறிப்பிட்ட அமைப்பின் அடிப்படையில் உண்மையான முடிவுகள் மிகவும் மாறுபடக்கூடும்.

மதிப்பீடு முடிந்தவுடன், செயல்திறன் மற்றும் பாதுகாப்பு அளவுகோள்களுக்கான முடிவுகளை மதிப்பாய்வு செய்யலாம்.

1. செயல்திறன் மற்றும் தரமான அளவுகோள்கள்:

    - மாடல் தெளிவான, சீரான, மற்றும் தொடர்புடைய பதில்களை உருவாக்குவதில் அதன் திறனை மதிப்பீடு செய்யவும்.

    ![மதிப்பீட்டு முடிவு.](../../../../../../imgs/02/Evaluation-AIFoundry/evaluation-result-gpu.png)

1. அபாயம் மற்றும் பாதுகாப்பு அளவுகோள்கள்:
    - மாடலின் வெளியீடுகள் பாதுகாப்பானவை மற்றும் பொறுப்பான AI கொள்கைகளுடன் ஒத்துப்போகின்றன என்பதை உறுதிப்படுத்தவும், எந்தவிதமான தீங்கு அல்லது அவமதிப்பு உள்ளடக்கத்தையும் தவிர்க்கவும்.

    ![மதிப்பீட்டு முடிவு.](../../../../../../imgs/02/Evaluation-AIFoundry/evaluation-result-gpu-2.png)

1. **விரிவான அளவீட்டு முடிவுகளை** பார்க்க கீழே ஸ்க்ரோல் செய்யலாம்.

    ![மதிப்பீட்டு முடிவு.](../../../../../../imgs/02/Evaluation-AIFoundry/detailed-metrics-result.png)

1. உங்கள் தனிப்பயன் Phi-3 / Phi-3.5 மாடலை செயல்திறன் மற்றும் பாதுகாப்பு அளவீடுகளுக்கு எதிராக மதிப்பீடு செய்வதன் மூலம், மாடல் பயனுள்ளதாக மட்டுமல்லாமல் பொறுப்பான AI நடைமுறைகளுடன் ஒத்துப்போகின்றது என்பதை உறுதிப்படுத்தலாம், இது உண்மையான உலக பயன்பாட்டுக்கு தயாராக உள்ளது.

## வாழ்த்துக்கள்!

### நீங்கள் இந்த பயிற்சியை முடித்துவிட்டீர்கள்

Azure AI Foundry-யில் Prompt flow உடன் ஒருங்கிணைக்கப்பட்ட Phi-3 மாடலை வெற்றிகரமாக மதிப்பீடு செய்துள்ளீர்கள். உங்கள் AI மாடல்கள் நல்ல செயல்திறனுடன் மட்டுமல்லாமல் Microsoft-இன் பொறுப்பான AI கொள்கைகளுடன் ஒத்துப்போகின்றன என்பதை உறுதிப்படுத்துவது ஒரு முக்கியமான படியாகும், இது நம்பகமான மற்றும் விசுவாசமான AI பயன்பாடுகளை உருவாக்க உதவுகிறது.

![கட்டமைப்பு.](../../../../../../imgs/02/Evaluation-AIFoundry/architecture.png)

## Azure வளங்களை சுத்தம் செய்யவும்

உங்கள் Azure கணக்கில் கூடுதல் கட்டணங்களை தவிர்க்க Azure வளங்களை சுத்தம் செய்யவும். Azure போர்டலுக்கு சென்று பின்வரும் வளங்களை நீக்கவும்:

- Azure Machine learning வளம்.
- Azure Machine learning மாடல் முடுக்கம்.
- Azure AI Foundry Project வளம்.
- Azure AI Foundry Prompt flow வளம்.

### அடுத்த படிகள்

#### ஆவணங்கள்

- [பொறுப்பான AI டாஷ்போர்டைப் பயன்படுத்தி AI அமைப்புகளை மதிப்பீடு செய்யவும்](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [உருவாக்க AI-க்கு மதிப்பீட்டு மற்றும் கண்காணிப்பு அளவீடுகள்](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Azure AI Foundry ஆவணங்கள்](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow ஆவணங்கள்](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### பயிற்சி உள்ளடக்கம்

- [Microsoft-இன் பொறுப்பான AI அணுகுமுறைக்கு அறிமுகம்](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Azure AI Foundry-க்கு அறிமுகம்](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### குறிப்புகள்

- [பொறுப்பான AI என்றால் என்ன?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [உங்கள் உருவாக்க AI பயன்பாடுகளை பாதுகாப்பான மற்றும் நம்பகமானதாக உருவாக்க உதவும் புதிய கருவிகளை Azure AI-யில் அறிவித்தல்](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [உருவாக்க AI பயன்பாடுகளின் மதிப்பீடு](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியக்க மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளுங்கள். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.