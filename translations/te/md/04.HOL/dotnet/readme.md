## C# ఉపయోగించి Phi ల్యాబ్స్‌కు స్వాగతం

.NET పరిసరాలలో వివిధ శక్తివంతమైన Phi మోడళ్లను ఏలా సమీకరించాలో చూపిస్తూ ల్యాబ్స్‌ యొక్క ఒక ఎంపిక అందుబాటులో ఉంది.

## అవసరమైన సముచితాలు

సాంపిల్ ను నడిపించే ముందు, మీ యంత్రంలో క్రింది వాటిని ఇన్‌స్టాల్ చేసుకున్నారా అని నిర్ధారించండి:

**.NET 9:** మీ యంత్రంపై [.NET యొక్క తాజా సంస్కరణ](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) ఇన్‌స్టాల్ చేయబడిందనుకోండి.

**(ఐచ్చికం) Visual Studio లేదా Visual Studio Code:** మీరు .NET ప్రాజెక్టులను నడిపే సామర్థ్యం ఉన్న IDE లేదా కోడ్ ఎడిటర్ అవసరం. [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) లేదా [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) ని సూచిస్తాము.

**git ఉపయోగించడం:** మీ స్థానిక యంత్రంలో [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c) నుండి అందుబాటులో ఉన్న Phi-3, Phi3.5 లేదా Phi-4 వెర్షన్లలో ఒకదాన్ని క్లోన్ చేయండి.

**Phi-4 ONNX మోడళ్లను మీ స్థానిక యంత్రానికి డౌన్లోడ్ చేయండి:**

### మోడళ్లను నిల్వ చేయడానికి ఫోల్డర్‌కు వెళ్లండి

```bash
cd c:\phi\models
```

### lfs కు మద్దతు జోడించండి

```bash
git lfs install 
```

### Phi-4 mini instruct మోడల్ మరియు Phi-4 multi modal మోడల్‌ను క్లోన్ చేసి డౌన్లోడ్ చేయండి

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Phi-3 ONNX మోడళ్లను** మీ స్థానిక యంత్రానికి డౌన్లోడ్ చేయండి:

### Phi-3 mini 4K instruct మోడల్ మరియు Phi-3 vision 128K మోడల్‌ను క్లోన్ చేసి డౌన్లోడ్ చేయండి

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**గమనిక:** ప్రస్తుత డెమోలు మోడల్ యొక్క ONNX వెర్షన్లను ఉపయోగించేలా రూపొందించబడ్డాయి. పై దశలు క్రింది మోడళ్లను క్లోన్ చేస్తాయి.

## ల్యాబ్స్ గురించి

ప్రధాన సొల్యూషన్‌లో C# ఉపయోగించి Phi మోడళ్ల సామర్థ్యాలను చూపించే అనేక శాంపిల్ ల్యాబ్స్ ఉన్నాయి.

| Project | Model | Description |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 or Phi-3.5 | శాంపిల్ కాన్సోల్ చాట్; వినియోగదారుడు ప్రశ్నలు అడగగలిగేలా ఉంటుంది. ప్రాజెక్ట్ స్థానిక ONNX Phi-3 మోడల్‌ను `Microsoft.ML.OnnxRuntime` లైబ్రరీలను ఉపయోగించి లోడ్ చేస్తుంది. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 or Phi-3.5 | శాంపిల్ కాన్సోల్ చాట్; వినియోగదారుడు ప్రశ్నలు అడగగలిగేలా ఉంటుంది. ప్రాజెక్ట్ స్థానిక ONNX Phi-3 మోడల్‌ను `Microsoft.Semantic.Kernel` లైబ్రరీలను ఉపయోగించి లోడ్ చేస్తుంది. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 or Phi-3.5 | ఇది స్థానిక phi3 విజన్ మోడల్‌ను చిత్రాలను విశ్లేషించడానికి ఉపయోగించే శాంపిల్ ప్రాజెక్ట్. ప్రాజెక్ట్ స్థానిక ONNX Phi-3 Vision మోడల్‌ను `Microsoft.ML.OnnxRuntime` లైబ్రరీలను ఉపయోగించి లోడ్ చేస్తుంది. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 or Phi-3.5 | ఇది స్థానిక phi3 విజన్ మోడల్‌ను చిత్రాలను విశ్లేషించడానికి ఉపయోగించే శాంపిల్ ప్రాజెక్ట్. ప్రాజెక్ట్ స్థానిక ONNX Phi-3 Vision మోడల్‌ను `Microsoft.ML.OnnxRuntime` లైబ్రరీలను ఉపయోగించి లోడ్ చేస్తుంది. ప్రాజెక్ట్ వినియోగదారితో ఇన్‌టరాక్ట్ చేయడానికి వివిధ ఎంపికలతో మెను‌ను కూడా ప్రదర్శిస్తుంది. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | శాంపిల్ కాన్సోల్ చాట్; వినియోగదారుడు ప్రశ్నలు అడగగలిగేలా ఉంటుంది. ప్రాజెక్ట్ స్థానిక ONNX Phi-4 మోడల్‌ను `Microsoft.ML.OnnxRuntime` లైబ్రరీలను ఉపయోగించి లోడ్ చేస్తుంది. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | శాంపిల్ కాన్సోల్ చాట్; వినియోగదారుడు ప్రశ్నలు అడగగలిగేలా ఉంటుంది. ప్రాజెక్ట్ స్థానిక ONNX Phi-4 మోడల్‌ను `Semantic Kernel` లైబ్రరీలను ఉపయోగించి లోడ్ చేస్తుంది. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | శాంపిల్ కాన్సోల్ చాట్; వినియోగదారుడు ప్రశ్నలు అడగగలిగేలా ఉంటుంది. ప్రాజెక్ట్ స్థానిక ONNX Phi-4 మోడల్‌ను `Microsoft.ML.OnnxRuntimeGenAI` లైబ్రరీలను ఉపయోగించి లోడ్ చేస్తుంది మరియు `Microsoft.Extensions.AI` నుండి `IChatClient` ను అమలు చేస్తుంది. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | శాంపిల్ కాన్సోల్ చాట్; వినియోగదారుడు ప్రశ్నలు అడగగలిగేలా ఉంటుంది. చాట్ మెమరీని అమలు చేస్తుంది. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | ఇది స్థానిక Phi-4 మోడల్‌ను ఉపయోగించి చిత్రాలను విశ్లేషించి కంసోల్‌లో ఫలితాన్ని చూపించే శాంపిల్ ప్రాజెక్ట్. ప్రాజెక్ట్ స్థానిక Phi-4-`multimodal-instruct-onnx` మోడల్‌ను `Microsoft.ML.OnnxRuntime` లైబ్రరీలను ఉపయోగించి లోడ్ చేస్తుంది. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | ఇది స్థానిక Phi-4 మోడల్‌ను ఉపయోగించి ఆడియో ఫైల్‌ను విశ్లేషించి ఆ ఫైల్ యొక్క ట్రాన్స్క్రిప్ట్ రూపొందించి ఫలితాన్ని కాన్సోల్‌లో చూపించే శాంపిల్ ప్రోజెక్ట్. ప్రాజెక్ట్ స్థానిక Phi-4-`multimodal-instruct-onnx` మోడల్‌ను `Microsoft.ML.OnnxRuntime` లైబ్రరీలను ఉపయోగించి లోడ్ చేస్తుంది. |

## ప్రాజెక్ట్‌లను ఎలా నడపాలి

ప్రాజెక్ట్‌లను నడిపేందుకు, ఈ దశలను అనుసరించండి:

1. రిపాజిటరీని మీ స్థానిక యంత్రానికి క్లోన్ చేయండి.

1. టెర్మినల్ ఓపెన్ చేసి కావలసిన ప్రాజెక్ట్ ఫోల్డర్‌కు నావిగేట్ చేయండి. ఉదాహరణకు, మేము `LabsPhi4-Chat-01OnnxRuntime` ను నడపుదాం.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. ప్రాజెక్ట్‌ను ఈ కమాండ్‌తో నడపండి

    ```bash
    dotnet run
    ```

1. శాంపిల్ ప్రాజెక్ట్ వినియోగదారుడి ఇన్‌పుట్‌ను అడిగి, లోకల్ మోడల్‌ను ఉపయోగించి ప్రతిస్పందిస్తుంది। 

   రన్ అవుతున్న డెమో ఈ క్రింది లాగే ఉంటుంది:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
స్పష్టీకరణ:
ఈ డాక్యుమెంట్‌ను AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాలలో తప్పులు లేదా పొరపాట్లు ఉండే అవకాశం ఉందని దయచేసి గమనించండి. మూల పత్రాన్ని దాని స్థానిక (మాతృ) భాషలోని వెర్షన్‌ను అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి వృత్తిపరమైన మానవ అనువాదం సిఫారసు చేయబడుతుంది. ఈ అనువాదం వాడకంవల్ల ఏర్పడే ఏవైనా అపార్థాలు లేదా తప్పుద్వేషాలకు మేము బాధ్యులు కాకపోవచ్చు.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->