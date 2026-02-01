# ஆய்வகம். சாதனத்தில் உள்ளே முடிவெடுப்பதற்கான AI மாதிரிகளை மேம்படுத்தவும்

## அறிமுகம் 

> [!IMPORTANT]
> இந்த ஆய்வகத்திற்கு **Nvidia A10 அல்லது A100 GPU** மற்றும் அதற்கான டிரைவர்கள் மற்றும் CUDA கருவி தொகுப்பு (பதிப்பு 12+) நிறுவப்பட்டிருக்க வேண்டும்.

> [!NOTE]
> இது **35 நிமிட** ஆய்வகம், இது OLIVE பயன்படுத்தி சாதனத்தில் உள்ளே முடிவெடுப்பதற்கான மாதிரிகளை மேம்படுத்துவதற்கான முக்கிய கருத்துக்களை கையாண்டு அறிமுகம் அளிக்கும்.

## கற்றல் நோக்கங்கள்

இந்த ஆய்வகத்தின் முடிவில், நீங்கள் OLIVE பயன்படுத்தி கீழ்கண்டவற்றை செய்ய முடியும்:

- AWQ அளவீட்டு முறையைப் பயன்படுத்தி AI மாதிரியை அளவீடு செய்யவும்.
- குறிப்பிட்ட பணிக்காக AI மாதிரியை நன்றாகத் தகுதிகரிக்கவும்.
- ONNX Runtime-ல் திறமையான சாதனத்தில் உள்ளே முடிவெடுப்பதற்கான LoRA அடாப்டர்களை (நன்றாகத் தகுதிகரிக்கப்பட்ட மாதிரி) உருவாக்கவும்.

### Olive என்றால் என்ன

Olive (*O*NNX *live*) என்பது ONNX runtime +++https://onnxruntime.ai+++ க்கான மாதிரிகளை தரம் மற்றும் செயல்திறனுடன் அனுப்புவதற்கான CLI உடன் கூடிய மாதிரி மேம்படுத்தல் கருவி தொகுப்பு ஆகும்.

![Olive Flow](../../../../../md/03.FineTuning/olive-lab/images/olive-flow.png)

Olive-க்கு உள்ளீடு பொதுவாக PyTorch அல்லது Hugging Face மாதிரியாக இருக்கும், மற்றும் வெளியீடு சாதனத்தில் (விநியோக இலக்கு) செயல்படுத்தப்படும் மேம்படுத்தப்பட்ட ONNX மாதிரியாக இருக்கும், இது ONNX runtime இயக்குகிறது. Olive மாதிரியை விநியோக இலக்கின் AI வேகப்படுத்தி (NPU, GPU, CPU) க்காக மேம்படுத்தும், இது Qualcomm, AMD, Nvidia அல்லது Intel போன்ற ஹார்ட்வேர்வெளியீட்டாளரால் வழங்கப்படுகிறது.

Olive ஒரு *workflow* ஐ செயல்படுத்துகிறது, இது *passes* எனப்படும் தனிப்பட்ட மாதிரி மேம்படுத்தல் பணிகளின் ஒழுங்கமைக்கப்பட்ட வரிசை - உதாரணமாக: மாதிரி சுருக்கம், கிராப் பிடிப்பு, அளவீடு, கிராப் மேம்படுத்தல். ஒவ்வொரு pass க்கும் சிறந்த அளவீடுகளை (உதாரணமாக துல்லியம் மற்றும் தாமதம்) அடைய தகுதிகரிக்கக்கூடிய அளவீட்டு கருவியால் மதிப்பீடு செய்யப்படும் அளவீட்டு அளவுருக்கள் உள்ளன. Olive ஒவ்வொரு pass ஐ தனித்தனியாக அல்லது passes குழுவாக தானாகத் தகுதிகரிக்க ஒரு தேடல் ஆல்கொரிதத்தைப் பயன்படுத்தும் தேடல் உத்தியைப் பயன்படுத்துகிறது.

#### Olive-ன் நன்மைகள்

- கிராப் மேம்படுத்தல், சுருக்கம் மற்றும் அளவீட்டத்திற்கான பல்வேறு தொழில்நுட்பங்களை கையாண்டு முயற்சி மற்றும் தவறுகளின் கைகழுவலையும் நேரத்தையும் குறைக்கவும். உங்கள் தரம் மற்றும் செயல்திறன் கட்டுப்பாடுகளை வரையறுக்கவும், Olive உங்களுக்கு சிறந்த மாதிரியை தானாகக் கண்டறிய அனுமதிக்கவும்.
- **40+ உள்ளமைக்கப்பட்ட மாதிரி மேம்படுத்தல் கூறுகள்** அளவீடு, சுருக்கம், கிராப் மேம்படுத்தல் மற்றும் நன்றாகத் தகுதிகரிப்பில் முன்னணி தொழில்நுட்பங்களை உள்ளடக்கியவை.
- **எளிதான CLI** பொதுவான மாதிரி மேம்படுத்தல் பணிகளுக்கு. உதாரணமாக, olive quantize, olive auto-opt, olive finetune.
- மாதிரி தொகுப்பு மற்றும் விநியோகம் உள்ளமைக்கப்பட்டுள்ளது.
- **Multi LoRA சேவை** க்கான மாதிரிகளை உருவாக்க ஆதரவு.
- YAML/JSON ஐப் பயன்படுத்தி workflows ஐ கட்டமைத்து மாதிரி மேம்படுத்தல் மற்றும் விநியோகம் பணிகளை ஒருங்கிணைக்கவும்.
- **Hugging Face** மற்றும் **Azure AI** ஒருங்கிணைப்பு.
- **செலவுகளைச் சேமிக்க** உள்ளமைக்கப்பட்ட **கேஷிங்** முறை.

## ஆய்வக வழிமுறைகள்
> [!NOTE]
> Lab 1 இல் உங்கள் Azure AI Hub மற்றும் Project ஐ வழங்கி, உங்கள் A100 கணினியை அமைத்துள்ளீர்கள் என்பதை உறுதிப்படுத்தவும்.

### படி 0: உங்கள் Azure AI கணினியுடன் இணைக்கவும்

**VS Code** இல் உள்ள தொலை features ஐப் பயன்படுத்தி Azure AI கணினியுடன் இணைக்கவும்.

1. உங்கள் **VS Code** டெஸ்க்டாப் பயன்பாட்டைத் திறக்கவும்:
1. **Shift+Ctrl+P** ஐப் பயன்படுத்தி **command palette** ஐத் திறக்கவும்.
1. command palette இல் **AzureML - remote: Connect to compute instance in New Window** ஐத் தேடவும்.
1. உங்கள் Azure Subscription, Resource Group, Project மற்றும் Lab 1 இல் அமைத்த Compute name ஐத் தேர்ந்தெடுப்பது போன்ற திரையில் உள்ள வழிமுறைகளைப் பின்பற்றவும்.
1. உங்கள் Azure ML Compute node உடன் இணைக்கப்பட்டவுடன், இது **Visual Code** இன் **கீழ் இடது மூலையில்** `><Azure ML: Compute Name` எனக் காட்டப்படும்.

### படி 1: இந்த repo ஐ clone செய்யவும்

VS Code இல், **Ctrl+J** ஐப் பயன்படுத்தி புதிய terminal ஐத் திறந்து இந்த repo ஐ clone செய்யவும்:

Terminal இல் நீங்கள் prompt ஐப் பார்க்க வேண்டும்

```
azureuser@computername:~/cloudfiles/code$ 
```
Solution ஐ clone செய்யவும் 

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### படி 2: VS Code இல் கோப்புறையைத் திறக்கவும்

Terminal இல் கீழ்கண்ட கட்டளையைச் செயல்படுத்துவதன் மூலம் VS Code ஐ தொடர்புடைய கோப்புறையில் திறக்கவும், இது புதிய சாளரத்தைத் திறக்கும்:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

மாற்றாக, **File** > **Open Folder** ஐத் தேர்ந்தெடுத்து கோப்புறையைத் திறக்கலாம்.

### படி 3: Dependencies

Azure AI Compute Instance உள்ள VS Code இல் terminal window ஐத் திறக்கவும் (tip: **Ctrl+J**) மற்றும் dependencies ஐ நிறுவ கீழ்கண்ட கட்டளைகளைச் செயல்படுத்தவும்:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> dependencies அனைத்தையும் நிறுவ ~5 நிமிடங்கள் ஆகும்.

இந்த ஆய்வகத்தில், நீங்கள் Azure AI Model catalog க்கு மாதிரிகளை பதிவிறக்கவும் பதிவேற்றவும் செய்ய வேண்டும். Model catalog ஐ அணுக, Azure இல் உள்நுழைய வேண்டும்:

```bash
az login
```

> [!NOTE]
> உள்நுழைவு நேரத்தில் உங்கள் subscription ஐத் தேர்ந்தெடுக்கக் கேட்கப்படும். இந்த ஆய்வகத்திற்காக வழங்கப்பட்ட subscription ஐ அமைத்துள்ளீர்கள் என்பதை உறுதிப்படுத்தவும்.

### படி 4: Olive கட்டளைகளைச் செயல்படுத்தவும் 

Azure AI Compute Instance உள்ள VS Code இல் terminal window ஐத் திறக்கவும் (tip: **Ctrl+J**) மற்றும் `olive-ai` conda சூழல் செயல்படுத்தப்பட்டுள்ளதா என்பதை உறுதிப்படுத்தவும்:

```bash
conda activate olive-ai
```

அடுத்து, command line இல் கீழ்கண்ட Olive கட்டளைகளைச் செயல்படுத்தவும்.

1. **தரவை ஆய்வு செய்யவும்:** இந்த எடுத்துக்காட்டில், நீங்கள் Phi-3.5-Mini மாதிரியை நன்றாகத் தகுதிகரிக்கப் போகிறீர்கள், இது பயண தொடர்பான கேள்விகளுக்கு பதிலளிக்க நிபுணத்துவம் பெறும். கீழே உள்ள குறியீடு JSON lines வடிவத்தில் உள்ள தரவுத்தொகுப்பின் முதல் சில பதிவுகளை காட்டுகிறது:
   
    ```bash
    head data/data_sample_travel.jsonl
    ```
1. **மாதிரியை அளவீடு செய்யவும்:** மாதிரியைப் பயிற்றுவிப்பதற்கு முன், நீங்கள் Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++ எனப்படும் தொழில்நுட்பத்தைப் பயன்படுத்தி கீழ்கண்ட கட்டளையைப் பயன்படுத்தி அளவீடு செய்ய வேண்டும். AWQ என்பது மாதிரியின் எடைகளை முடிவெடுப்பு செய்யும் போது உருவாகும் செயல்பாடுகளைப் பொருத்தமாகக் கருதுவதன் மூலம் அளவீடு செய்கிறது. இது செயல்பாடுகளில் உள்ள தரவின் உண்மையான விநியோகத்தை கருத்தில் கொள்ளும் அளவீட்டு செயல்முறையை அர்த்தமாக்குகிறது, இது பாரம்பரிய எடை அளவீட்டு முறைகளுடன் ஒப்பிடும்போது மாதிரி துல்லியத்தைச் சிறப்பாகப் பாதுகாக்க உதவுகிறது.
    
    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```
    
    AWQ அளவீட்டை முடிக்க **~8 நிமிடங்கள்** ஆகும், இது **மாதிரி அளவை ~7.5GB இருந்து ~2.5GB வரை குறைக்கும்**.
   
   இந்த ஆய்வகத்தில், Hugging Face (உதாரணமாக: `microsoft/Phi-3.5-mini-instruct`) இலிருந்து மாதிரிகளை உள்ளிடுவது எப்படி என்பதை உங்களுக்குக் காட்டுகிறோம். இருப்பினும், Olive `model_name_or_path` argument ஐ Azure AI asset ID (உதாரணமாக: `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`) க்கு புதுப்பிப்பதன் மூலம் Azure AI catalog இலிருந்து மாதிரிகளை உள்ளிட அனுமதிக்கிறது.

1. **மாதிரியைப் பயிற்றுவிக்கவும்:** அடுத்ததாக, `olive finetune` கட்டளை அளவீடு செய்யப்பட்ட மாதிரியை நன்றாகத் தகுதிகரிக்கிறது. மாதிரியை *முன்* நன்றாகத் தகுதிகரிப்பதற்கு முன் அளவீடு செய்வது, பின்னர் அளவீடு செய்வதற்குப் பதிலாக, சிறந்த துல்லியத்தை வழங்குகிறது, ஏனெனில் அளவீட்டத்தால் ஏற்படும் சில இழப்புகளை நன்றாகத் தகுதிகரிப்பு செயல்முறை மீட்டெடுக்கிறது.
    
    ```bash
    olive finetune \
        --method lora \
        --model_name_or_path models/phi/awq \
        --data_files "data/data_sample_travel.jsonl" \
        --data_name "json" \
        --text_template "<|user|>\n{prompt}<|end|>\n<|assistant|>\n{response}<|end|>" \
        --max_steps 100 \
        --output_path ./models/phi/ft \
        --log_level 1
    ```
    
    Fine-tuning ஐ முடிக்க **~6 நிமிடங்கள்** ஆகும் (100 படிகள்).

1. **மேம்படுத்தவும்:** மாதிரி பயிற்றுவிக்கப்பட்ட பிறகு, Olive இன் `auto-opt` கட்டளையைப் பயன்படுத்தி மாதிரியை மேம்படுத்துங்கள், இது ONNX graph ஐப் பிடித்து CPU க்கான மாதிரி செயல்திறனை மேம்படுத்த பல மேம்படுத்தல்களை தானாகவே செய்யும். மாதிரியை சுருக்குதல் மற்றும் இணைப்புகளைச் செய்வதன் மூலம் இது செய்யப்படுகிறது. இது குறிப்பிடப்பட வேண்டும், நீங்கள் NPU அல்லது GPU போன்ற பிற சாதனங்களுக்காகவும் `--device` மற்றும் `--provider` arguments ஐ புதுப்பிப்பதன் மூலம் மேம்படுத்தலாம் - ஆனால் இந்த ஆய்வகத்தின் நோக்கங்களுக்காக CPU ஐப் பயன்படுத்துவோம்.

    ```bash
    olive auto-opt \
       --model_name_or_path models/phi/ft/model \
       --adapter_path models/phi/ft/adapter \
       --device cpu \
       --provider CPUExecutionProvider \
       --use_ort_genai \
       --output_path models/phi/onnx-ao \
       --log_level 1
    ```
    
    மேம்படுத்தலை முடிக்க **~5 நிமிடங்கள்** ஆகும்.

### படி 5: மாதிரி முடிவெடுப்பு விரைவான சோதனை

மாதிரியை முடிவெடுப்பதற்கான சோதனை செய்ய, உங்கள் கோப்புறையில் **app.py** எனும் Python கோப்பை உருவாக்கி, கீழே உள்ள குறியீட்டை copy-and-paste செய்யவும்:

```python
import onnxruntime_genai as og
import numpy as np

print("loading model and adapters...", end="", flush=True)
model = og.Model("models/phi/onnx-ao/model")
adapters = og.Adapters(model)
adapters.load("models/phi/onnx-ao/model/adapter_weights.onnx_adapter", "travel")
print("DONE!")

tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

params = og.GeneratorParams(model)
params.set_search_options(max_length=100, past_present_share_buffer=False)
user_input = "what is the best thing to see in chicago"
params.input_ids = tokenizer.encode(f"<|user|>\n{user_input}<|end|>\n<|assistant|>\n")

generator = og.Generator(model, params)

generator.set_active_adapter(adapters, "travel")

print(f"{user_input}")

while not generator.is_done():
    generator.compute_logits()
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    print(tokenizer_stream.decode(new_token), end='', flush=True)

print("\n")
```

குறியீட்டைச் செயல்படுத்த:

```bash
python app.py
```

### படி 6: Azure AI க்கு மாதிரியைப் பதிவேற்றவும்

மாதிரியை Azure AI மாதிரி repository க்கு பதிவேற்றுவது, உங்கள் மேம்பாட்டு குழுவின் பிற உறுப்பினர்களுடன் மாதிரியைப் பகிரக்கூடியதாக ஆக்குகிறது மற்றும் மாதிரியின் பதிப்பு கட்டுப்பாட்டையும் கையாளுகிறது. மாதிரியைப் பதிவேற்ற கீழ்கண்ட கட்டளையைச் செயல்படுத்தவும்:

> [!NOTE]
> `{}` இடங்களை உங்கள் resource group மற்றும் Azure AI Project Name க்கு பெயரைப் புதுப்பிக்கவும்.

உங்கள் resource group `"resourceGroup"` மற்றும் Azure AI Project name ஐ கண்டறிய, கீழ்கண்ட கட்டளையைச் செயல்படுத்தவும் 

```
az ml workspace show
```

அல்லது +++ai.azure.com+++ க்கு சென்று **management center** **project** **overview** ஐத் தேர்ந்தெடுக்கவும்.

`{}` இடங்களை உங்கள் resource group மற்றும் Azure AI Project Name க்கு பெயரைப் புதுப்பிக்கவும்.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```
பின்னர் உங்கள் பதிவேற்றப்பட்ட மாதிரியைப் பார்க்கவும், உங்கள் மாதிரியை https://ml.azure.com/model/list இல் deploy செய்யவும்.

---

**அறிவிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் சொந்த மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்களுக்கும் அல்லது தவறான விளக்கங்களுக்கும் நாங்கள் பொறுப்பல்ல.