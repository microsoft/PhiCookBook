<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-10-11T11:35:34+00:00",
  "source_file": "code/03.Finetuning/olive-lab/readme.md",
  "language_code": "ta"
}
-->
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
- ONNX Runtime-ல் திறமையான சாதன முடிவெடுப்புக்காக LoRA அடாப்டர்களை (நன்றாகத் தகுதிகரிக்கப்பட்ட மாதிரி) உருவாக்கவும்.

### Olive என்றால் என்ன

Olive (*O*NNX *live*) என்பது ONNX runtime +++https://onnxruntime.ai+++ க்கான மாதிரிகளை தரம் மற்றும் செயல்திறனுடன் அனுப்புவதற்கான CLI உடன் கூடிய மாதிரி மேம்பாட்டு கருவி தொகுப்பு ஆகும்.

![Olive Flow](../../../../../code/03.Finetuning/olive-lab/images/olive-flow.png)

Olive-க்கு உள்ளீடு பொதுவாக PyTorch அல்லது Hugging Face மாதிரியாக இருக்கும், மற்றும் வெளியீடு சாதனத்தில் (விநியோக இலக்கு) செயல்படுத்தப்படும் மேம்படுத்தப்பட்ட ONNX மாதிரியாக இருக்கும், இது ONNX runtime இயக்குகிறது. Olive மாதிரியை வினியோக இலக்கின் AI வேகப்படுத்தி (NPU, GPU, CPU) க்காக மேம்படுத்தும், இது Qualcomm, AMD, Nvidia அல்லது Intel போன்ற ஹார்ட்வேர்விநியோகஸ்தரால் வழங்கப்படுகிறது.

Olive ஒரு *workflow* ஐ செயல்படுத்துகிறது, இது *passes* எனப்படும் தனிப்பட்ட மாதிரி மேம்பாட்டு பணிகளின் ஒழுங்கமைக்கப்பட்ட வரிசையாகும் - உதாரணமாக: மாதிரி சுருக்கம், கிராப் பிடிப்பு, அளவீடு, கிராப் மேம்பாடு. ஒவ்வொரு pass க்கும் சிறந்த அளவீடுகளை (உதாரணமாக துல்லியம் மற்றும் தாமதம்) அடைய தகுதிகரிக்கக்கூடிய அளவீட்டு கருவியால் மதிப்பீடு செய்யப்படும் அளவீட்டு அளவீடுகள் உள்ளன. Olive ஒவ்வொரு pass ஐ தனித்தனியாக அல்லது passes குழுவாக தானாகத் தகுதிகரிக்க ஒரு தேடல் ஆல்காரிதத்தைப் பயன்படுத்தும் தேடல் உத்தியைப் பயன்படுத்துகிறது.

#### Olive-ன் நன்மைகள்

- கிராப் மேம்பாடு, சுருக்கம் மற்றும் அளவீட்டத்திற்கான பல்வேறு உத்திகளை கையாண்டு முயற்சி மற்றும் தவறுகளின் **மனக்கசப்பு மற்றும் நேரத்தை குறைக்கவும்**. உங்கள் தரம் மற்றும் செயல்திறன் கட்டுப்பாடுகளை வரையறுக்கவும், Olive உங்களுக்கு சிறந்த மாதிரியை தானாகக் கண்டறிய அனுமதிக்கவும்.
- **40+ உள்ளமைக்கப்பட்ட மாதிரி மேம்பாட்டு கூறுகள்** அளவீடு, சுருக்கம், கிராப் மேம்பாடு மற்றும் நன்றாகத் தகுதிகரிப்பில் முன்னணி உத்திகளை உள்ளடக்கியவை.
- பொதுவான மாதிரி மேம்பாட்டு பணிகளுக்கான **எளிதான CLI**. உதாரணமாக, olive quantize, olive auto-opt, olive finetune.
- மாதிரி தொகுப்பு மற்றும் விநியோகம் உள்ளமைக்கப்பட்டுள்ளது.
- **Multi LoRA சேவை** க்கான மாதிரிகளை உருவாக்க ஆதரவு.
- மாதிரி மேம்பாட்டு மற்றும் விநியோக பணிகளை ஒருங்கிணைக்க YAML/JSON ஐப் பயன்படுத்தி workflows உருவாக்கவும்.
- **Hugging Face** மற்றும் **Azure AI** ஒருங்கிணைப்பு.
- **செலவுகளைச் சேமிக்க** **கேஷிங்** முறை உள்ளமைக்கப்பட்டுள்ளது.

## ஆய்வக வழிமுறைகள்
> [!NOTE]
> உங்கள் Azure AI Hub மற்றும் Project ஐ வழங்கி, Lab 1 இல் அமைத்த A100 கணினியை அமைத்துள்ளீர்கள் என்பதை உறுதிப்படுத்தவும்.

### படி 0: உங்கள் Azure AI கணினியுடன் இணைக்கவும்

**VS Code** இல் உள்ள தொலைதூர அம்சத்தைப் பயன்படுத்தி Azure AI கணினியுடன் நீங்கள் இணைக்க வேண்டும்.

1. உங்கள் **VS Code** டெஸ்க்டாப் பயன்பாட்டைத் திறக்கவும்:
1. **Shift+Ctrl+P** பயன்படுத்தி **command palette** ஐத் திறக்கவும்.
1. command palette இல் **AzureML - remote: Connect to compute instance in New Window** ஐத் தேடவும்.
1. Azure Subscription, Resource Group, Project மற்றும் Lab 1 இல் அமைத்த Compute name ஐத் தேர்ந்தெடுப்பது போன்ற திரையில் உள்ள வழிமுறைகளைப் பின்பற்றவும்.
1. உங்கள் Azure ML Compute node உடன் நீங்கள் இணைக்கப்பட்டவுடன், இது **Visual Code இன் இடது கீழ் பகுதியில்** `><Azure ML: Compute Name` எனக் காட்டப்படும்.

### படி 1: இந்த repo ஐ clone செய்யவும்

VS Code இல், **Ctrl+J** பயன்படுத்தி புதிய terminal ஐத் திறக்கவும் மற்றும் இந்த repo ஐ clone செய்யவும்:

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

இந்த ஆய்வகத்தில், நீங்கள் Azure AI Model catalog க்கு மாதிரிகளை பதிவிறக்கவும் பதிவேற்றவும் செய்ய வேண்டும். மாதிரி catalog ஐ அணுக, Azure இல் உள்நுழைய வேண்டும்:

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

1. **தரவை ஆய்வு செய்யவும்:** இந்த எடுத்துக்காட்டில், நீங்கள் Phi-3.5-Mini மாதிரியை நன்றாகத் தகுதிகரிக்கப் போகிறீர்கள், இது பயண தொடர்பான கேள்விகளுக்கு பதிலளிக்க நிபுணத்துவம் பெறும். JSON lines வடிவத்தில் உள்ள dataset இன் முதல் சில பதிவுகளை கீழே உள்ள குறியீடு காட்டுகிறது:
   
    ```bash
    head data/data_sample_travel.jsonl
    ```
1. **மாதிரியை அளவீடு செய்யவும்:** மாதிரியைப் பயிற்றுவிப்பதற்கு முன், நீங்கள் Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++ எனப்படும் உத்தியைப் பயன்படுத்தி கீழ்கண்ட கட்டளையைப் பயன்படுத்தி அளவீடு செய்ய வேண்டும். AWQ மாதிரியின் எடைகளை inference போது உருவாகும் செயல்பாடுகளைப் பொருத்தமாகக் கருதுவதன் மூலம் அளவீடு செய்கிறது. இது செயல்பாடுகளில் உள்ள உண்மையான தரவுப் பகிர்வை கருத்தில் கொள்ளும் அளவீட்டு செயல்முறையை அர்த்தமாக்குகிறது, இது பாரம்பரிய எடை அளவீட்டு முறைகளுடன் ஒப்பிடும்போது மாதிரி துல்லியத்தைச் சிறப்பாகப் பாதுகாக்கிறது.
    
    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```
    
    AWQ அளவீட்டை முடிக்க **~8 நிமிடங்கள்** ஆகும், இது **மாதிரி அளவை ~7.5GB இருந்து ~2.5GB வரை குறைக்கும்**.
   
   இந்த ஆய்வகத்தில், Hugging Face (உதாரணமாக: `microsoft/Phi-3.5-mini-instruct`) இருந்து மாதிரிகளை உள்ளிடுவது எப்படி என்பதை உங்களுக்குக் காட்டுகிறோம். இருப்பினும், Azure AI catalog இருந்து மாதிரிகளை உள்ளிட Olive உங்களை அனுமதிக்கிறது, `model_name_or_path` argument ஐ Azure AI asset ID க்கு (உதாரணமாக: `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`) புதுப்பிப்பதன் மூலம்.

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
    
    Fine-tuning ஐ முடிக்க **~6 நிமிடங்கள்** ஆகும் (100 steps உடன்).

1. **மேம்படுத்தவும்:** மாதிரியைப் பயிற்றுவித்த பிறகு, Olive இன் `auto-opt` கட்டளையைப் பயன்படுத்தி மாதிரியை மேம்படுத்துங்கள், இது ONNX graph ஐப் பிடித்து, மாதிரி செயல்திறனை CPU க்காக மேம்படுத்த பல்வேறு மேம்பாடுகளை தானாகவே செய்யும். மாதிரியை சுருக்குதல் மற்றும் இணைப்புகளைச் செய்வதன் மூலம். இது குறிப்பிடப்பட வேண்டும், நீங்கள் NPU அல்லது GPU போன்ற பிற சாதனங்களுக்காகவும் `--device` மற்றும் `--provider` arguments ஐ புதுப்பிப்பதன் மூலம் மேம்படுத்தலாம் - ஆனால் இந்த ஆய்வகத்தின் நோக்கங்களுக்காக CPU ஐப் பயன்படுத்துவோம்.

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
    
    மேம்பாட்டை முடிக்க **~5 நிமிடங்கள்** ஆகும்.

### படி 5: மாதிரி முடிவெடுப்பு விரைவான சோதனை

மாதிரியை முடிவெடுப்பதற்கான சோதனை செய்ய, **app.py** எனும் Python கோப்பை உங்கள் கோப்புறையில் உருவாக்கி, கீழ்கண்ட குறியீட்டை copy-and-paste செய்யவும்:

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

குறியீட்டை செயல்படுத்த:

```bash
python app.py
```

### படி 6: Azure AI க்கு மாதிரியை பதிவேற்றவும்

மாதிரியை Azure AI மாதிரி repository க்கு பதிவேற்றுவது, உங்கள் மேம்பாட்டு குழுவின் பிற உறுப்பினர்களுடன் மாதிரியை பகிரக்கூடியதாக ஆக்குகிறது மற்றும் மாதிரியின் பதிப்பு கட்டுப்பாட்டையும் கையாளுகிறது. மாதிரியை பதிவேற்ற கீழ்கண்ட கட்டளையைச் செயல்படுத்தவும்:

> [!NOTE]
> `{}` placeholders ஐ உங்கள் resource group மற்றும் Azure AI Project Name உடன் புதுப்பிக்கவும்.

உங்கள் resource group `"resourceGroup"` மற்றும் Azure AI Project name ஐ கண்டறிய, கீழ்கண்ட கட்டளையைச் செயல்படுத்தவும் 

```
az ml workspace show
```

அல்லது +++ai.azure.com+++ க்கு சென்று **management center** **project** **overview** ஐத் தேர்ந்தெடுக்கவும்.

`{}` placeholders ஐ உங்கள் resource group மற்றும் Azure AI Project Name உடன் புதுப்பிக்கவும்.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```

பின்னர் உங்கள் பதிவேற்றப்பட்ட மாதிரியைப் பார்க்கவும் மற்றும் உங்கள் மாதிரியை https://ml.azure.com/model/list இல் deploy செய்யவும்.

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.