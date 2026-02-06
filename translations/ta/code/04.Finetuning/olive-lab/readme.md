# ஆய்வகம். சாதனத்தில் உள்ளே AI மாதிரிகளை மேம்படுத்தவும்

## அறிமுகம் 

> [!IMPORTANT]
> இந்த ஆய்வகத்திற்கு **Nvidia A10 அல்லது A100 GPU** மற்றும் அதற்கான டிரைவர்கள் மற்றும் CUDA கருவி தொகுப்பு (பதிப்பு 12+) நிறுவல் தேவை.

> [!NOTE]
> இது **35 நிமிட** ஆய்வகம், இது OLIVE பயன்படுத்தி சாதனத்தில் உள்ளே மாதிரிகளை மேம்படுத்துவதற்கான முக்கிய கருத்துகளை கையால் அறிமுகம் செய்யும்.

## கற்றல் நோக்கங்கள்

இந்த ஆய்வகத்தின் முடிவில், நீங்கள் OLIVE பயன்படுத்தி கீழ்கண்டவற்றை செய்ய முடியும்:

- AWQ அளவீட்டு முறையைப் பயன்படுத்தி AI மாதிரியை அளவீடு செய்யவும்.
- குறிப்பிட்ட பணிக்காக AI மாதிரியை நன்றாகத் தகுதிகரிக்கவும்.
- ONNX Runtime-ல் திறமையான சாதனத்தில் உள்ளே inference செய்ய LoRA adapters (நன்றாகத் தகுதிகரிக்கப்பட்ட மாதிரி) உருவாக்கவும்.

### Olive என்றால் என்ன

Olive (*O*NNX *live*) என்பது ONNX runtime +++https://onnxruntime.ai+++ க்கான மாதிரிகளை தரம் மற்றும் செயல்திறனுடன் அனுப்புவதற்கு உதவும் CLI உடன் கூடிய மாதிரி மேம்பாட்டு கருவி தொகுப்பு.

![Olive Flow](../../../../../code/04.Finetuning/olive-lab/images/olive-flow.png)

Olive-க்கு உள்ளீடு பொதுவாக PyTorch அல்லது Hugging Face மாதிரியாக இருக்கும், மற்றும் வெளியீடு சாதனத்தில் (deployment target) இயக்கப்படும் மேம்படுத்தப்பட்ட ONNX மாதிரியாக இருக்கும். Olive மாதிரியை deployment target இன் AI accelerator (NPU, GPU, CPU) க்காக hardware vendor (Qualcomm, AMD, Nvidia, Intel போன்ற) வழங்கியதைப் பயன்படுத்தி மேம்படுத்தும்.

Olive ஒரு *workflow* ஐ செயல்படுத்துகிறது, இது *passes* எனப்படும் தனிப்பட்ட மாதிரி மேம்பாட்டு பணிகளின் ஒழுங்கமைக்கப்பட்ட வரிசையாகும் - உதாரணமாக: மாதிரி சுருக்கம், graph capture, அளவீடு, graph optimization. ஒவ்வொரு pass க்கும் சிறந்த அளவீடுகளை (accuracy மற்றும் latency போன்றவை) அடைய தகுதிகரிக்கக்கூடிய அளவீட்டு அளவுருக்கள் உள்ளன. Olive ஒரு தேடல் algorithm ஐப் பயன்படுத்தி ஒவ்வொரு pass ஐ தனித்தனியாக அல்லது passes க்கான தொகுப்பை auto-tune செய்யும் தேடல் உத்தியைப் பயன்படுத்துகிறது.

#### Olive இன் நன்மைகள்

- graph optimization, compression மற்றும் quantization க்கான பல்வேறு முறைகளை முயற்சித்து தோல்வியடையும் கையால் முயற்சிக்கும் சிரமத்தையும் நேரத்தையும் குறைக்கவும். உங்கள் தரம் மற்றும் செயல்திறன் கட்டுப்பாடுகளை வரையறுக்கவும், Olive உங்களுக்கு சிறந்த மாதிரியை தானாகவே கண்டறிய அனுமதிக்கவும்.
- **40+ உள்ளமைக்கப்பட்ட மாதிரி மேம்பாட்டு கூறுகள்** அளவீடு, சுருக்கம், graph optimization மற்றும் finetuning இல் முன்னணி தொழில்நுட்பங்களை உள்ளடக்கியவை.
- **எளிதான CLI** பொதுவான மாதிரி மேம்பாட்டு பணிகளுக்கு. உதாரணமாக, olive quantize, olive auto-opt, olive finetune.
- மாதிரி தொகுப்பு மற்றும் deployment உள்ளமைக்கப்பட்டுள்ளது.
- **Multi LoRA serving** க்கான மாதிரிகளை உருவாக்க ஆதரவு.
- YAML/JSON ஐப் பயன்படுத்தி workflows ஐ உருவாக்கி மாதிரி மேம்பாட்டு மற்றும் deployment பணிகளை ஒருங்கிணைக்கவும்.
- **Hugging Face** மற்றும் **Azure AI** ஒருங்கிணைப்பு.
- **செலவுகளைச் சேமிக்க** உள்ளமைக்கப்பட்ட **caching** முறை.

## ஆய்வக வழிமுறைகள்
> [!NOTE]
> Lab 1 இன் படி உங்கள் Azure AI Hub மற்றும் Project ஐ provision செய்து உங்கள் A100 கணினியை அமைத்துள்ளீர்கள் என்பதை உறுதிப்படுத்தவும்.

### படி 0: உங்கள் Azure AI Compute ஐ இணைக்கவும்

நீங்கள் **VS Code** இல் உள்ள remote feature ஐப் பயன்படுத்தி Azure AI compute ஐ இணைப்பீர்கள்.

1. உங்கள் **VS Code** desktop application ஐ திறக்கவும்:
1. **Shift+Ctrl+P** ஐப் பயன்படுத்தி **command palette** ஐ திறக்கவும்.
1. command palette இல் **AzureML - remote: Connect to compute instance in New Window** ஐத் தேடவும்.
1. Compute ஐ இணைக்க on-screen வழிமுறைகளைப் பின்பற்றவும். இது Lab 1 இல் நீங்கள் அமைத்த Azure Subscription, Resource Group, Project மற்றும் Compute name ஐத் தேர்ந்தெடுப்பதை உள்ளடக்கியது.
1. உங்கள் Azure ML Compute node ஐ இணைத்த பிறகு, இது **Visual Code இன் இடது கீழ் பகுதியில்** `><Azure ML: Compute Name` எனக் காட்டப்படும்.

### படி 1: இந்த repo ஐ clone செய்யவும்

VS Code இல், **Ctrl+J** ஐப் பயன்படுத்தி புதிய terminal ஐ திறக்கவும் மற்றும் இந்த repo ஐ clone செய்யவும்:

Terminal இல் நீங்கள் prompt ஐப் பார்க்க வேண்டும்

```
azureuser@computername:~/cloudfiles/code$ 
```
Solution ஐ clone செய்யவும் 

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### படி 2: VS Code இல் Folder ஐ திறக்கவும்

VS Code ஐ தொடர்புடைய folder இல் திறக்க, terminal இல் கீழ்கண்ட கட்டளையைச் செயல்படுத்தவும், இது புதிய window ஐத் திறக்கும்:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

மாற்றாக, **File** > **Open Folder** ஐத் தேர்ந்தெடுத்து folder ஐத் திறக்கலாம்.

### படி 3: Dependencies

Azure AI Compute Instance இல் VS Code இல் terminal window ஐ திறக்கவும் (tip: **Ctrl+J**) மற்றும் dependencies ஐ நிறுவ கீழ்கண்ட கட்டளைகளைச் செயல்படுத்தவும்:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> dependencies ஐ நிறுவ ~5 நிமிடங்கள் ஆகும்.

இந்த ஆய்வகத்தில், நீங்கள் Azure AI Model catalog க்கு மாதிரிகளை பதிவிறக்கம் செய்து பதிவேற்றுவீர்கள். Model catalog ஐ அணுக, Azure இல் login செய்ய வேண்டும்:

```bash
az login
```

> [!NOTE]
> login செய்யும் போது உங்கள் subscription ஐத் தேர்ந்தெடுக்கக் கேட்கப்படும். இந்த ஆய்வகத்திற்கான subscription ஐ அமைத்துள்ளீர்கள் என்பதை உறுதிப்படுத்தவும்.

### படி 4: Olive கட்டளைகளைச் செயல்படுத்தவும் 

Azure AI Compute Instance இல் VS Code இல் terminal window ஐ திறக்கவும் (tip: **Ctrl+J**) மற்றும் `olive-ai` conda environment செயல்படுத்தப்பட்டுள்ளதா என்பதை உறுதிப்படுத்தவும்:

```bash
conda activate olive-ai
```

அடுத்து, command line இல் கீழ்கண்ட Olive கட்டளைகளைச் செயல்படுத்தவும்.

1. **தரவை ஆய்வு செய்யவும்:** இந்த எடுத்துக்காட்டில், நீங்கள் Phi-3.5-Mini மாதிரியை நன்றாகத் தகுதிகரிக்கப் போகிறீர்கள், இது பயண தொடர்பான கேள்விகளுக்கு பதிலளிக்க சிறப்பு பெற்றது. Dataset இன் முதல் சில பதிவுகளை JSON lines format இல் காட்டும் code கீழே உள்ளது:
   
    ```bash
    head data/data_sample_travel.jsonl
    ```
1. **மாதிரியை அளவீடு செய்யவும்:** மாதிரியைப் பயிற்றுவிப்பதற்கு முன், Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++ எனப்படும் தொழில்நுட்பத்தைப் பயன்படுத்தி கீழ்கண்ட கட்டளையைப் பயன்படுத்தி அளவீடு செய்யவும். AWQ மாதிரியின் எடைகளை inference இல் உருவாக்கப்படும் activations ஐக் கருத்தில் கொண்டு அளவீடு செய்கிறது. இது activations இல் உள்ள தரவின் distribution ஐ கருத்தில் கொண்டு அளவீட்டு செயல்முறையைச் செய்கிறது, இது பாரம்பரிய எடை அளவீட்டு முறைகளுடன் ஒப்பிடும்போது மாதிரி துல்லியத்தைச் சிறப்பாகப் பாதுகாக்க உதவுகிறது.
    
    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```
    
    AWQ அளவீட்டை முடிக்க **~8 நிமிடங்கள்** ஆகும், இது **மாதிரி அளவை ~7.5GB இல் இருந்து ~2.5GB ஆக குறைக்கும்**.
   
   இந்த ஆய்வகத்தில், Hugging Face இல் இருந்து மாதிரிகளை உள்ளிடுவது எப்படி என்பதை உங்களுக்குக் காட்டுகிறோம் (உதாரணமாக: `microsoft/Phi-3.5-mini-instruct`). எனினும், Azure AI catalog இல் இருந்து மாதிரிகளை உள்ளிடவும் Olive உங்களை அனுமதிக்கிறது, `model_name_or_path` argument ஐ Azure AI asset ID க்கு (உதாரணமாக: `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`) update செய்வதன் மூலம்.

1. **மாதிரியைப் பயிற்றுவிக்கவும்:** அடுத்ததாக, `olive finetune` கட்டளை அளவீடு செய்யப்பட்ட மாதிரியை நன்றாகத் தகுதிகரிக்கிறது. மாதிரியை *முன்* fine-tuning செய்வது, fine-tuning செயல்முறை quantization இன் சில இழப்புகளை மீட்டெடுப்பதால், சிறந்த துல்லியத்தை வழங்குகிறது.
    
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

1. **மேம்படுத்தவும்:** மாதிரியைப் பயிற்றுவித்த பிறகு, Olive இன் `auto-opt` கட்டளையைப் பயன்படுத்தி மாதிரியை optimize செய்யுங்கள், இது ONNX graph ஐ capture செய்து CPU க்கான மாதிரி செயல்திறனை மேம்படுத்த compress மற்றும் fusions செய்யும் பல optimizations ஐ தானாகவே செய்கிறது. இது குறிப்பிடப்பட வேண்டும், நீங்கள் NPU அல்லது GPU போன்ற சாதனங்களுக்கு optimize செய்ய `--device` மற்றும் `--provider` arguments ஐ update செய்வதன் மூலம் செய்யலாம் - ஆனால் இந்த ஆய்வகத்திற்காக CPU ஐப் பயன்படுத்துவோம்.

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
    
    Optimization ஐ முடிக்க **~5 நிமிடங்கள்** ஆகும்.

### படி 5: மாதிரி inference விரைவான சோதனை

மாதிரியை inference செய்ய சோதிக்க, உங்கள் folder இல் **app.py** எனும் Python file ஐ உருவாக்கி, கீழ்கண்ட code ஐ copy-paste செய்யவும்:

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

Code ஐ செயல்படுத்த:

```bash
python app.py
```

### படி 6: Azure AI க்கு மாதிரியைப் பதிவேற்றவும்

மாதிரியை Azure AI model repository க்கு பதிவேற்றுவது, உங்கள் மேம்பாட்டு குழுவின் பிற உறுப்பினர்களுடன் மாதிரியைப் பகிரக்கூடியதாக மாற்றுகிறது மற்றும் மாதிரியின் version control ஐயும் கையாளுகிறது. மாதிரியைப் பதிவேற்ற கீழ்கண்ட கட்டளையைச் செயல்படுத்தவும்:

> [!NOTE]
> `{}` placeholders ஐ உங்கள் resource group மற்றும் Azure AI Project Name இன் பெயருடன் update செய்யவும்.

உங்கள் resource group `"resourceGroup"` மற்றும் Azure AI Project name ஐ கண்டறிய, கீழ்கண்ட கட்டளையைச் செயல்படுத்தவும் 

```
az ml workspace show
```

அல்லது +++ai.azure.com+++ க்கு சென்று **management center** **project** **overview** ஐத் தேர்ந்தெடுக்கவும்.

`{}` placeholders ஐ உங்கள் resource group மற்றும் Azure AI Project Name இன் பெயருடன் update செய்யவும்.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```

பின்னர் உங்கள் பதிவேற்றப்பட்ட மாதிரியைப் பார்க்கவும் மற்றும் https://ml.azure.com/model/list இல் உங்கள் மாதிரியை deploy செய்யவும்.

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.