<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-10-11T11:39:09+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "ta"
}
-->
## Phi லேப்களுக்கு C# பயன்படுத்தி வரவேற்கிறோம்

.NET சூழலில் பல்வேறு Phi மாடல்களின் சக்திவாய்ந்த பதிப்புகளை ஒருங்கிணைப்பது எப்படி என்பதை காட்டும் சில லேப்கள் உள்ளன.

## முன் தேவைகள்

மாதிரியை இயக்குவதற்கு முன், கீழே உள்ளவை நிறுவப்பட்டுள்ளதா என்பதை உறுதிப்படுத்தவும்:

**.NET 9:** உங்கள் கணினியில் [சமீபத்திய .NET பதிப்பு](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) நிறுவப்பட்டுள்ளதா என்பதை உறுதிப்படுத்தவும்.

**(விருப்பம்) Visual Studio அல்லது Visual Studio Code:** .NET திட்டங்களை இயக்கக்கூடிய IDE அல்லது குறியீட்டு திருத்தி தேவைப்படும். [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) அல்லது [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) பரிந்துரைக்கப்படுகிறது.

**git பயன்படுத்தி** [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c) இல் உள்ள Phi-3, Phi3.5 அல்லது Phi-4 பதிப்புகளை உள்ளூர் கணினியில் கிளோன் செய்யவும்.

**Phi-4 ONNX மாடல்களை** உங்கள் உள்ளூர் கணினியில் பதிவிறக்கவும்:

### மாடல்களை சேமிக்க வேண்டிய கோப்பகத்திற்கு செல்லவும்

```bash
cd c:\phi\models
```

### lfs ஆதரவைச் சேர்க்கவும்

```bash
git lfs install 
```

### Phi-4 mini instruct மாடல் மற்றும் Phi-4 multi modal மாடலை கிளோன் செய்து பதிவிறக்கவும்

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Phi-3 ONNX மாடல்களை** உங்கள் உள்ளூர் கணினியில் பதிவிறக்கவும்:

### Phi-3 mini 4K instruct மாடல் மற்றும் Phi-3 vision 128K மாடலை கிளோன் செய்து பதிவிறக்கவும்

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**முக்கியம்:** தற்போதைய டெமோக்கள் ONNX பதிப்புகளைப் பயன்படுத்த வடிவமைக்கப்பட்டுள்ளன. மேலே உள்ள படிகள் பின்வரும் மாடல்களை கிளோன் செய்கின்றன.

## லேப்கள் பற்றி

முதன்மை தீர்வில் C# பயன்படுத்தி Phi மாடல்களின் திறன்களை விளக்கும் பல மாதிரி லேப்கள் உள்ளன.

| திட்டம் | மாடல் | விளக்கம் |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 அல்லது Phi-3.5 | பயனர் கேள்விகளை கேட்க அனுமதிக்கும் மாதிரி கன்சோல் உரையாடல். இந்த திட்டம் `Microsoft.ML.OnnxRuntime` நூலகங்களைப் பயன்படுத்தி உள்ளூர் ONNX Phi-3 மாடலை ஏற்றுகிறது. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 அல்லது Phi-3.5 | பயனர் கேள்விகளை கேட்க அனுமதிக்கும் மாதிரி கன்சோல் உரையாடல். இந்த திட்டம் `Microsoft.Semantic.Kernel` நூலகங்களைப் பயன்படுத்தி உள்ளூர் ONNX Phi-3 மாடலை ஏற்றுகிறது. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 அல்லது Phi-3.5 | இது ஒரு மாதிரி திட்டமாகும், இது உள்ளூர் phi3 vision மாடலைப் பயன்படுத்தி படங்களை பகுப்பாய்வு செய்கிறது. இந்த திட்டம் `Microsoft.ML.OnnxRuntime` நூலகங்களைப் பயன்படுத்தி உள்ளூர் ONNX Phi-3 Vision மாடலை ஏற்றுகிறது. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 அல்லது Phi-3.5 | இது ஒரு மாதிரி திட்டமாகும், இது உள்ளூர் phi3 vision மாடலைப் பயன்படுத்தி படங்களை பகுப்பாய்வு செய்கிறது. இந்த திட்டம் `Microsoft.ML.OnnxRuntime` நூலகங்களைப் பயன்படுத்தி உள்ளூர் ONNX Phi-3 Vision மாடலை ஏற்றுகிறது. இந்த திட்டம் பயனருடன் தொடர்பு கொள்ள பல்வேறு விருப்பங்களை கொண்ட ஒரு மெனுவையும் வழங்குகிறது. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | பயனர் கேள்விகளை கேட்க அனுமதிக்கும் மாதிரி கன்சோல் உரையாடல். இந்த திட்டம் `Microsoft.ML.OnnxRuntime` நூலகங்களைப் பயன்படுத்தி உள்ளூர் ONNX Phi-4 மாடலை ஏற்றுகிறது. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | பயனர் கேள்விகளை கேட்க அனுமதிக்கும் மாதிரி கன்சோல் உரையாடல். இந்த திட்டம் `Semantic Kernel` நூலகங்களைப் பயன்படுத்தி உள்ளூர் ONNX Phi-4 மாடலை ஏற்றுகிறது. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | பயனர் கேள்விகளை கேட்க அனுமதிக்கும் மாதிரி கன்சோல் உரையாடல். இந்த திட்டம் `Microsoft.ML.OnnxRuntimeGenAI` நூலகங்களைப் பயன்படுத்தி உள்ளூர் ONNX Phi-4 மாடலை ஏற்றுகிறது மற்றும் `Microsoft.Extensions.AI` இல் இருந்து `IChatClient` ஐ செயல்படுத்துகிறது. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | பயனர் கேள்விகளை கேட்க அனுமதிக்கும் மாதிரி கன்சோல் உரையாடல். இந்த உரையாடல் நினைவுகளை செயல்படுத்துகிறது. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | இது ஒரு மாதிரி திட்டமாகும், இது உள்ளூர் Phi-4 மாடலைப் பயன்படுத்தி படங்களை பகுப்பாய்வு செய்து முடிவுகளை கன்சோலில் காட்டுகிறது. இந்த திட்டம் `Microsoft.ML.OnnxRuntime` நூலகங்களைப் பயன்படுத்தி உள்ளூர் Phi-4-`multimodal-instruct-onnx` மாடலை ஏற்றுகிறது. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | இது ஒரு மாதிரி திட்டமாகும், இது உள்ளூர் Phi-4 மாடலைப் பயன்படுத்தி ஒரு ஆடியோ கோப்பை பகுப்பாய்வு செய்து, கோப்பின் உரையை உருவாக்கி முடிவுகளை கன்சோலில் காட்டுகிறது. இந்த திட்டம் `Microsoft.ML.OnnxRuntime` நூலகங்களைப் பயன்படுத்தி உள்ளூர் Phi-4-`multimodal-instruct-onnx` மாடலை ஏற்றுகிறது. |

## திட்டங்களை இயக்குவது எப்படி

திட்டங்களை இயக்க, கீழே உள்ள படிகளை பின்பற்றவும்:

1. ரெப்போசிடரியை உங்கள் உள்ளூர் கணினியில் கிளோன் செய்யவும்.

1. ஒரு டெர்மினலை திறந்து, தேவையான திட்டத்திற்குச் செல்லவும். உதாரணமாக, `LabsPhi4-Chat-01OnnxRuntime` ஐ இயக்குவோம்.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. திட்டத்தை கீழே உள்ள கட்டளையைப் பயன்படுத்தி இயக்கவும்

    ```bash
    dotnet run
    ```

1. மாதிரி திட்டம் பயனரின் உள்ளீட்டை கேட்டு, உள்ளூர் முறை மூலம் பதிலளிக்கிறது.

   இயக்கப்படும் டெமோ இதற்கு ஒத்ததாக இருக்கும்:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. எங்கள் தரத்தை உறுதிப்படுத்த முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.