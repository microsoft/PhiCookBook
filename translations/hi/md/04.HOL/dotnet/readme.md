<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-05-08T05:02:15+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "hi"
}
-->
﻿## C# का उपयोग करते हुए Phi लैब्स में आपका स्वागत है

यहाँ Phi मॉडल के विभिन्न शक्तिशाली संस्करणों को .NET वातावरण में एकीकृत करने के तरीके को दिखाने वाले लैब्स का एक चयन है।

## आवश्यकताएँ

नमूना चलाने से पहले, सुनिश्चित करें कि आपके पास निम्नलिखित इंस्टॉल हैं:

**.NET 9:** सुनिश्चित करें कि आपके कंप्यूटर पर [लेटेस्ट .NET संस्करण](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) इंस्टॉल है।

**(वैकल्पिक) Visual Studio या Visual Studio Code:** आपको एक ऐसा IDE या कोड एडिटर चाहिए जो .NET प्रोजेक्ट्स चला सके। [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) या [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) की सलाह दी जाती है।

**git का उपयोग करते हुए** [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c) से Phi-3, Phi3.5 या Phi-4 के उपलब्ध संस्करणों में से किसी एक को लोकली क्लोन करें।

**Phi-4 ONNX मॉडल अपने लोकल मशीन पर डाउनलोड करें:**

### मॉडल्स को स्टोर करने के लिए फ़ोल्डर में जाएँ

```bash
cd c:\phi\models
```

### lfs के लिए सपोर्ट जोड़ें

```bash
git lfs install 
```

### Phi-4 मिनी इंस्ट्रक्ट मॉडल और Phi-4 मल्टी मोडल मॉडल को क्लोन और डाउनलोड करें

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Phi-3 ONNX मॉडल अपने लोकल मशीन पर डाउनलोड करें:**

### Phi-3 मिनी 4K इंस्ट्रक्ट मॉडल और Phi-3 विज़न 128K मॉडल को क्लोन और डाउनलोड करें

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**महत्वपूर्ण:** वर्तमान डेमो मॉडल के ONNX संस्करणों का उपयोग करने के लिए डिज़ाइन किए गए हैं। ऊपर दिए गए चरण निम्नलिखित मॉडलों को क्लोन करते हैं।

## लैब्स के बारे में

मुख्य सॉल्यूशन में कई सैंपल लैब्स हैं जो C# का उपयोग करते हुए Phi मॉडलों की क्षमताओं को दर्शाते हैं।

| प्रोजेक्ट | मॉडल | विवरण |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 या Phi-3.5 | एक सैंपल कंसोल चैट जो उपयोगकर्ता को सवाल पूछने की अनुमति देता है। यह प्रोजेक्ट लोकल ONNX Phi-3 मॉडल को `Microsoft.ML.OnnxRuntime` libraries. |
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

1. Open a terminal and navigate to the desired project. In example, let's run `LabsPhi4-Chat-01OnnxRuntime` का उपयोग करके लोड करता है।

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. प्रोजेक्ट को इस कमांड से चलाएँ

    ```bash
    dotnet run
    ```

1. सैंपल प्रोजेक्ट उपयोगकर्ता से इनपुट मांगता है और लोकल मॉडल का उपयोग करके जवाब देता है।

   चल रहा डेमो इस जैसा दिखता है:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान रखें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।