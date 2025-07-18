<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-07-17T10:33:44+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "hi"
}
-->
## C# का उपयोग करके Phi लैब्स में आपका स्वागत है

यहाँ कुछ लैब्स का चयन है जो दिखाते हैं कि कैसे Phi मॉडल के विभिन्न शक्तिशाली संस्करणों को .NET वातावरण में एकीकृत किया जा सकता है।

## आवश्यकताएँ

नमूना चलाने से पहले, सुनिश्चित करें कि आपके पास निम्नलिखित इंस्टॉल हैं:

**.NET 9:** सुनिश्चित करें कि आपके कंप्यूटर पर [नवीनतम .NET संस्करण](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) इंस्टॉल है।

**(वैकल्पिक) Visual Studio या Visual Studio Code:** आपको ऐसा IDE या कोड एडिटर चाहिए जो .NET प्रोजेक्ट्स चला सके। [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) या [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) की सलाह दी जाती है।

**git का उपयोग करते हुए** Hugging Face से उपलब्ध Phi-3, Phi3.5 या Phi-4 संस्करणों में से किसी एक को स्थानीय रूप से क्लोन करें: [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c)।

**Phi-4 ONNX मॉडल्स** को अपनी स्थानीय मशीन पर डाउनलोड करें:

### मॉडल्स को स्टोर करने के लिए फोल्डर पर जाएं

```bash
cd c:\phi\models
```

### lfs के लिए सपोर्ट जोड़ें

```bash
git lfs install 
```

### Phi-4 मिनी इंस्ट्रक्ट मॉडल और Phi-4 मल्टी मोडल मॉडल क्लोन और डाउनलोड करें

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Phi-3 ONNX मॉडल्स** को अपनी स्थानीय मशीन पर डाउनलोड करें:

### Phi-3 मिनी 4K इंस्ट्रक्ट मॉडल और Phi-3 विज़न 128K मॉडल क्लोन और डाउनलोड करें

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**महत्वपूर्ण:** वर्तमान डेमो मॉडल के ONNX संस्करणों का उपयोग करने के लिए डिज़ाइन किए गए हैं। पिछले चरण निम्नलिखित मॉडल क्लोन करते हैं।

## लैब्स के बारे में

मुख्य समाधान में कई नमूना लैब्स हैं जो C# का उपयोग करके Phi मॉडल की क्षमताओं को प्रदर्शित करते हैं।

| प्रोजेक्ट | मॉडल | विवरण |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 या Phi-3.5 | नमूना कंसोल चैट जो उपयोगकर्ता को प्रश्न पूछने की अनुमति देता है। प्रोजेक्ट `Microsoft.ML.OnnxRuntime` लाइब्रेरीज़ का उपयोग करके स्थानीय ONNX Phi-3 मॉडल लोड करता है। |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 या Phi-3.5 | नमूना कंसोल चैट जो उपयोगकर्ता को प्रश्न पूछने की अनुमति देता है। प्रोजेक्ट `Microsoft.Semantic.Kernel` लाइब्रेरीज़ का उपयोग करके स्थानीय ONNX Phi-3 मॉडल लोड करता है। |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 या Phi-3.5 | यह एक नमूना प्रोजेक्ट है जो स्थानीय phi3 विज़न मॉडल का उपयोग करके छवियों का विश्लेषण करता है। प्रोजेक्ट `Microsoft.ML.OnnxRuntime` लाइब्रेरीज़ का उपयोग करके स्थानीय ONNX Phi-3 विज़न मॉडल लोड करता है। |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 या Phi-3.5 | यह एक नमूना प्रोजेक्ट है जो स्थानीय phi3 विज़न मॉडल का उपयोग करके छवियों का विश्लेषण करता है। प्रोजेक्ट `Microsoft.ML.OnnxRuntime` लाइब्रेरीज़ का उपयोग करके स्थानीय ONNX Phi-3 विज़न मॉडल लोड करता है। प्रोजेक्ट उपयोगकर्ता के साथ इंटरैक्ट करने के लिए विभिन्न विकल्पों के साथ एक मेनू भी प्रस्तुत करता है। | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | नमूना कंसोल चैट जो उपयोगकर्ता को प्रश्न पूछने की अनुमति देता है। प्रोजेक्ट `Microsoft.ML.OnnxRuntime` लाइब्रेरीज़ का उपयोग करके स्थानीय ONNX Phi-4 मॉडल लोड करता है। |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | नमूना कंसोल चैट जो उपयोगकर्ता को प्रश्न पूछने की अनुमति देता है। प्रोजेक्ट `Semantic Kernel` लाइब्रेरीज़ का उपयोग करके स्थानीय ONNX Phi-4 मॉडल लोड करता है। |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | नमूना कंसोल चैट जो उपयोगकर्ता को प्रश्न पूछने की अनुमति देता है। प्रोजेक्ट `Microsoft.ML.OnnxRuntimeGenAI` लाइब्रेरीज़ का उपयोग करके स्थानीय ONNX Phi-4 मॉडल लोड करता है और `Microsoft.Extensions.AI` से `IChatClient` को लागू करता है। |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | नमूना कंसोल चैट जो उपयोगकर्ता को प्रश्न पूछने की अनुमति देता है। चैट में मेमोरी लागू है। |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | यह एक नमूना प्रोजेक्ट है जो स्थानीय Phi-4 मॉडल का उपयोग करके छवियों का विश्लेषण करता है और परिणाम कंसोल में दिखाता है। प्रोजेक्ट `Microsoft.ML.OnnxRuntime` लाइब्रेरीज़ का उपयोग करके स्थानीय Phi-4-`multimodal-instruct-onnx` मॉडल लोड करता है। |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | यह एक नमूना प्रोजेक्ट है जो स्थानीय Phi-4 मॉडल का उपयोग करके एक ऑडियो फ़ाइल का विश्लेषण करता है, फ़ाइल का ट्रांसक्रिप्ट बनाता है और परिणाम कंसोल में दिखाता है। प्रोजेक्ट `Microsoft.ML.OnnxRuntime` लाइब्रेरीज़ का उपयोग करके स्थानीय Phi-4-`multimodal-instruct-onnx` मॉडल लोड करता है। |

## प्रोजेक्ट्स कैसे चलाएं

प्रोजेक्ट्स चलाने के लिए, निम्न चरणों का पालन करें:

1. रिपॉजिटरी को अपनी स्थानीय मशीन पर क्लोन करें।

1. एक टर्मिनल खोलें और इच्छित प्रोजेक्ट पर जाएं। उदाहरण के लिए, चलाते हैं `LabsPhi4-Chat-01OnnxRuntime`।

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. कमांड के साथ प्रोजेक्ट चलाएं

    ```bash
    dotnet run
    ```

1. नमूना प्रोजेक्ट उपयोगकर्ता से इनपुट मांगता है और स्थानीय मॉडल का उपयोग करके जवाब देता है।

   चल रहा डेमो इस जैसा दिखता है:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।