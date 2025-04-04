<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0e3a4453db505856d5d991285dd6001",
  "translation_date": "2025-04-04T19:14:21+00:00",
  "source_file": "md\\04.HOL\\dotnet\\readme.md",
  "language_code": "hi"
}
-->
## Phi लैब्स में आपका स्वागत है (C# का उपयोग करते हुए)

यह लैब्स का एक चयन है जो दिखाता है कि .NET वातावरण में शक्तिशाली Phi मॉडल के विभिन्न संस्करणों को कैसे एकीकृत किया जाए।

## आवश्यकताएँ

नमूना चलाने से पहले, सुनिश्चित करें कि आपके पास निम्नलिखित इंस्टॉल हैं:

**.NET 9:** सुनिश्चित करें कि आपके कंप्यूटर पर [नवीनतम .NET संस्करण](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) इंस्टॉल है।

**(वैकल्पिक) Visual Studio या Visual Studio Code:** आपको एक IDE या कोड एडिटर की आवश्यकता होगी जो .NET प्रोजेक्ट्स चलाने में सक्षम हो। [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) या [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) की अनुशंसा की जाती है।

**git का उपयोग करते हुए** [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c) से उपलब्ध Phi-3, Phi3.5 या Phi-4 संस्करणों में से एक को लोकल क्लोन करें।

**Phi-4 ONNX मॉडल्स को डाउनलोड करें** और अपने कंप्यूटर पर स्टोर करें:

### मॉडल्स स्टोर करने के लिए फ़ोल्डर पर जाएं

```bash
cd c:\phi\models
```

### lfs सपोर्ट जोड़ें

```bash
git lfs install 
```

### Phi-4 मिनी इंस्ट्रक्ट मॉडल और Phi-4 मल्टी मोडल मॉडल को क्लोन और डाउनलोड करें

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Phi-3 ONNX मॉडल्स को डाउनलोड करें** और अपने कंप्यूटर पर स्टोर करें:

### Phi-3 मिनी 4K इंस्ट्रक्ट मॉडल और Phi-3 विजन 128K मॉडल को क्लोन और डाउनलोड करें

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**महत्वपूर्ण:** वर्तमान डेमो ONNX संस्करणों का उपयोग करने के लिए डिज़ाइन किए गए हैं। पिछले चरणों में निम्नलिखित मॉडल क्लोन किए जाते हैं।

## लैब्स के बारे में

मुख्य समाधान में कई नमूना लैब्स शामिल हैं जो C# का उपयोग करके Phi मॉडल्स की क्षमताओं को प्रदर्शित करते हैं।

| प्रोजेक्ट | मॉडल | विवरण |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 या Phi-3.5 | एक नमूना कंसोल चैट जो उपयोगकर्ता को प्रश्न पूछने की अनुमति देता है। प्रोजेक्ट लोकल ONNX Phi-3 मॉडल को लोड करता है `Microsoft.ML.OnnxRuntime` libraries. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 or Phi-3.5 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-3 model using the `Microsoft.Semantic.Kernel` libraries. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 or Phi-3.5 | This is a sample project that uses a local phi3 vision model to analyze images. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 or Phi-3.5 | This is a sample project that uses a local phi3 vision model to analyze images.. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. The project also presents a menu with different options to interacti with the user. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Semantic Kernel` libraries. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntimeGenAI` libraries and implements the `IChatClient` from `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Sample console chat that allows the user to ask questions. The chat implements memory. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | This is a sample project that uses a local Phi-4 model to analyze images showing the result in the console. The project load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 |This is a sample project that uses a local Phi-4 model to analyze an audio file, generate the transcript of the file and show the result in the console. The project load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |

## How to Run the Projects

To run the projects, follow these steps:

1. Clone the repository to your local machine.

1. Open a terminal and navigate to the desired project. In example, let's run `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. प्रोजेक्ट को निम्नलिखित कमांड के साथ चलाएं:

    ```bash
    dotnet run
    ```

1. नमूना प्रोजेक्ट उपयोगकर्ता इनपुट पूछता है और लोकल मोड का उपयोग करते हुए जवाब देता है।

   चल रहे डेमो इस प्रकार दिखता है:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।