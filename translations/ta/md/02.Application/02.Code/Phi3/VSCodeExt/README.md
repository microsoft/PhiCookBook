# **Visual Studio Code GitHub Copilot Chat-ஐ Microsoft Phi-3 குடும்பத்துடன் உருவாக்குங்கள்**

GitHub Copilot Chat-இல் workspace agent-ஐ பயன்படுத்தியுள்ளீர்களா? உங்கள் குழுவின் code agent-ஐ உருவாக்க விரும்புகிறீர்களா? இந்த கையேடு திறந்த மூல மாடலை இணைத்து ஒரு நிறுவன மட்ட code business agent-ஐ உருவாக்க உதவுகிறது.

## **அடித்தளம்**

### **Microsoft Phi-3-ஐ ஏன் தேர்வு செய்ய வேண்டும்**

Phi-3 என்பது ஒரு குடும்பத் தொடர், இதில் phi-3-mini, phi-3-small, மற்றும் phi-3-medium ஆகியவை உள்ளன, இது உரை உருவாக்கம், உரையாடல் முடிவு, மற்றும் code உருவாக்கத்திற்கான மாறுபட்ட பயிற்சி அளவுகளை அடிப்படையாகக் கொண்டது. Vision அடிப்படையில் phi-3-vision என்ற மாடலும் உள்ளது. இது நிறுவனங்கள் அல்லது குழுக்களுக்கு offline generative AI தீர்வுகளை உருவாக்க ஏற்றது.

இந்த இணைப்பை படிக்க பரிந்துரைக்கப்படுகிறது [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

GitHub Copilot Chat extension உங்களுக்கு ஒரு chat இடைமுகத்தை வழங்குகிறது, இது GitHub Copilot-இன் coding தொடர்பான கேள்விகளுக்கு பதிலளிக்க உதவுகிறது, documentation-ஐ தேடவோ அல்லது online forums-ஐ தேடவோ தேவையில்லை.

Copilot Chat syntax highlighting, indentation, மற்றும் formatting அம்சங்களை பயன்படுத்தி பதில்களை தெளிவாக வழங்குகிறது. பயனர் கேள்வியின் வகையைப் பொறுத்து, பதிலில் Copilot பயன்படுத்திய context-க்கு இணைப்புகள், source code files அல்லது documentation போன்றவை இருக்கலாம், அல்லது VS Code செயல்பாடுகளுக்கான அணுகல் பொத்தான்கள் இருக்கலாம்.

- Copilot Chat உங்கள் developer flow-இல் ஒருங்கிணைக்கப்படுகிறது மற்றும் உங்களுக்கு தேவையான இடத்தில் உதவுகிறது:

- Editor அல்லது terminal-இல் நேரடியாக inline chat conversation தொடங்குங்கள்

- Chat view-ஐ பயன்படுத்தி AI உதவியாளரை எப்போது வேண்டுமானாலும் அணுகுங்கள்

- Quick Chat-ஐ தொடங்கி ஒரு விரைவான கேள்வியை கேட்டு உங்கள் வேலையை தொடருங்கள்

GitHub Copilot Chat-ஐ பின்வரும் சூழல்களில் பயன்படுத்தலாம்:

- ஒரு பிரச்சினையை எவ்வாறு சிறப்பாக தீர்க்கலாம் என்பதை விளக்குதல்

- மற்றவரின் code-ஐ விளக்கி மேம்பாடுகளை பரிந்துரைத்தல்

- code திருத்தங்களை முன்மொழிதல்

- unit test cases உருவாக்குதல்

- code documentation உருவாக்குதல்

இந்த இணைப்பை படிக்க பரிந்துரைக்கப்படுகிறது [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)

### **Microsoft GitHub Copilot Chat @workspace**

Copilot Chat-இல் **@workspace**-ஐ குறிப்பிடுவது உங்கள் முழு codebase-ஐப் பற்றிய கேள்விகளை கேட்க அனுமதிக்கிறது. பயனர் கேள்வியின் அடிப்படையில், Copilot தொடர்புடைய கோப்புகள் மற்றும் சின்னங்களை புத்திசாலித்தனமாக பெறுகிறது, பின்னர் பதிலில் இணைப்புகள் மற்றும் code எடுத்துக்காட்டுகளாக குறிப்பிடுகிறது.

**@workspace** உங்கள் கேள்விக்கு பதிலளிக்க, VS Code-இல் codebase-ஐ developer-கள் தேடுவதற்கான மூலங்களைப் பயன்படுத்துகிறது:

- .gitignore கோப்பால் புறக்கணிக்கப்பட்ட கோப்புகளை தவிர workspace-இல் உள்ள அனைத்து கோப்புகளும்

- nested folder மற்றும் file names கொண்ட directory அமைப்பு

- workspace GitHub repository ஆக இருந்தால் மற்றும் code search மூலம் index செய்யப்பட்டால் GitHub-இன் code search index

- workspace-இல் உள்ள symbols மற்றும் definitions

- தற்போதைய தேர்ந்தெடுக்கப்பட்ட உரை அல்லது active editor-இல் காணப்படும் உரை

குறிப்பு: .gitignore புறக்கணிக்கப்படும், நீங்கள் ஒரு கோப்பை திறந்திருந்தால் அல்லது புறக்கணிக்கப்பட்ட கோப்பில் உள்ள உரையைத் தேர்ந்தெடுத்திருந்தால்.

இந்த இணைப்பை படிக்க பரிந்துரைக்கப்படுகிறது [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]

## **இந்த கையேடு பற்றி மேலும் அறிக**

GitHub Copilot நிறுவனங்களின் நிரலாக்க திறனை பெரிதும் மேம்படுத்தியுள்ளது, மேலும் ஒவ்வொரு நிறுவனமும் GitHub Copilot-இன் தொடர்புடைய செயல்பாடுகளை தனிப்பயனாக்க விரும்புகிறது. பல நிறுவனங்கள் தங்கள் சொந்த business scenarios மற்றும் திறந்த மூல மாடல்களை அடிப்படையாகக் கொண்டு GitHub Copilot போன்ற Extensions-ஐ தனிப்பயனாக்கியுள்ளன. நிறுவனங்களுக்கு, தனிப்பயனாக்கப்பட்ட Extensions-ஐ கட்டுப்படுத்துவது எளிதாக இருக்கும், ஆனால் இது பயனர் அனுபவத்தை பாதிக்கக்கூடும். GitHub Copilot பொதுவான சூழல்களை மற்றும் தொழில்முறைத் திறன்களை கையாளுவதில் வலுவாக உள்ளது. அனுபவம் ஒரே மாதிரியானதாக இருந்தால், நிறுவனத்தின் சொந்த Extension-ஐ தனிப்பயனாக்குவது சிறந்தது. GitHub Copilot Chat நிறுவனங்களுக்கு Chat அனுபவத்தில் விரிவாக்கம் செய்ய API-களை வழங்குகிறது. ஒரே மாதிரியான அனுபவத்தை பராமரித்து தனிப்பயனாக்கப்பட்ட செயல்பாடுகளை கொண்டிருப்பது சிறந்த பயனர் அனுபவமாக இருக்கும்.

இந்த கையேடு முக்கியமாக Phi-3 மாடலை உள்ளூர் NPU மற்றும் Azure hybrid-ஐ இணைத்து GitHub Copilot Chat ***@PHI3***-இல் ஒரு custom Agent-ஐ உருவாக்குகிறது, இது நிறுவன developer-க்களுக்கு code உருவாக்கம் ***(@PHI3 /gen)*** மற்றும் படங்களை அடிப்படையாகக் கொண்ட code உருவாக்கம் ***(@PHI3 /img)*** ஆகியவற்றை முடிக்க உதவுகிறது.

![PHI3](../../../../../../../imgs/02/vscodeext/cover.png)

### ***குறிப்பு:*** 

இந்த கையேடு தற்போது Intel CPU மற்றும் Apple Silicon-இன் AIPC-இல் செயல்படுத்தப்பட்டுள்ளது. Qualcomm NPU பதிப்பு தொடர்ந்து புதுப்பிக்கப்படும்.

## **கையேடு**

| பெயர் | விளக்கம் | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Installations(✅) | தொடர்புடைய சூழல்களை மற்றும் installation tools-ஐ அமைத்தல் | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Run Prompt flow with Phi-3-mini (✅) | AIPC / Apple Silicon-ஐ இணைத்து, உள்ளூர் NPU மூலம் Phi-3-mini-ஐ பயன்படுத்தி code உருவாக்கம் | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Deploy Phi-3-vision on Azure Machine Learning Service(✅) | Azure Machine Learning Service-இன் Model Catalog - Phi-3-vision image-ஐ deploy செய்து code உருவாக்கம் | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Create a @phi-3 agent in GitHub Copilot Chat(✅)  | GitHub Copilot Chat-இல் custom Phi-3 agent-ஐ உருவாக்கி code உருவாக்கம், graph generation code, RAG போன்றவற்றை முடிக்க | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Sample Code (✅)  | மாதிரி code-ஐ பதிவிறக்கவும் | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |

## **வளங்கள்**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. GitHub Copilot பற்றி மேலும் அறிக [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. GitHub Copilot Chat பற்றி மேலும் அறிக [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. GitHub Copilot Chat API பற்றி மேலும் அறிக [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Azure AI Foundry பற்றி மேலும் அறிக [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Azure AI Foundry-இன் Model Catalog பற்றி மேலும் அறிக [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியக்க மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாகக் கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.