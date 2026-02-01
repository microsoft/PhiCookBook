## C# प्रयोग गरेर Phi ल्याबहरूमा स्वागत छ

यहाँ विभिन्न Phi मोडेलहरूको शक्तिशाली संस्करणहरूलाई .NET वातावरणमा कसरी एकीकृत गर्ने देखाउने केही ल्याबहरू छन्।

## पूर्वआवश्यकताहरू

नमूना चलाउनु अघि, तलका कुराहरू तपाईंको कम्प्युटरमा इन्स्टल भएको सुनिश्चित गर्नुहोस्:

**.NET 9:** तपाईंको मेसिनमा [सबैभन्दा नयाँ .NET संस्करण](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) इन्स्टल गरिएको छ कि छैन जाँच गर्नुहोस्।

**(वैकल्पिक) Visual Studio वा Visual Studio Code:** तपाईंलाई .NET प्रोजेक्टहरू चलाउन सक्ने IDE वा कोड सम्पादक चाहिन्छ। [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) वा [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) सिफारिस गरिन्छ।

**git प्रयोग गरेर** स्थानीय रूपमा Hugging Face बाट उपलब्ध Phi-3, Phi3.5 वा Phi-4 संस्करणहरू मध्ये कुनै एक क्लोन गर्नुहोस्: [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c)।

**Phi-4 ONNX मोडेलहरू** तपाईंको स्थानीय मेसिनमा डाउनलोड गर्नुहोस्:

### मोडेलहरू भण्डारण गर्न फोल्डरमा जानुहोस्

```bash
cd c:\phi\models
```

### lfs को लागि समर्थन थप्नुहोस्

```bash
git lfs install 
```

### Phi-4 मिनी इन्स्ट्रक्ट मोडेल र Phi-4 मल्टि मोडल मोडेल क्लोन र डाउनलोड गर्नुहोस्

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Phi-3 ONNX मोडेलहरू** तपाईंको स्थानीय मेसिनमा डाउनलोड गर्नुहोस्:

### Phi-3 मिनी 4K इन्स्ट्रक्ट मोडेल र Phi-3 भिजन 128K मोडेल क्लोन र डाउनलोड गर्नुहोस्

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**महत्त्वपूर्ण:** हालका डेमोहरू मोडेलका ONNX संस्करणहरू प्रयोग गर्न डिजाइन गरिएको हो। माथिका चरणहरूले निम्न मोडेलहरू क्लोन गर्छन्।

## ल्याबहरूबारे

मुख्य समाधानमा C# प्रयोग गरेर Phi मोडेलहरूको क्षमता देखाउने विभिन्न नमूना ल्याबहरू छन्।

| प्रोजेक्ट | मोडेल | विवरण |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 वा Phi-3.5 | नमूना कन्सोल च्याट जसले प्रयोगकर्तालाई प्रश्न सोध्न अनुमति दिन्छ। प्रोजेक्टले `Microsoft.ML.OnnxRuntime` लाइब्रेरीहरू प्रयोग गरी स्थानीय ONNX Phi-3 मोडेल लोड गर्छ। |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 वा Phi-3.5 | नमूना कन्सोल च्याट जसले प्रयोगकर्तालाई प्रश्न सोध्न अनुमति दिन्छ। प्रोजेक्टले `Microsoft.Semantic.Kernel` लाइब्रेरीहरू प्रयोग गरी स्थानीय ONNX Phi-3 मोडेल लोड गर्छ। |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 वा Phi-3.5 | यो नमूना प्रोजेक्टले स्थानीय phi3 भिजन मोडेल प्रयोग गरी तस्बिरहरू विश्लेषण गर्छ। प्रोजेक्टले `Microsoft.ML.OnnxRuntime` लाइब्रेरीहरू प्रयोग गरी स्थानीय ONNX Phi-3 भिजन मोडेल लोड गर्छ। |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 वा Phi-3.5 | यो नमूना प्रोजेक्टले स्थानीय phi3 भिजन मोडेल प्रयोग गरी तस्बिरहरू विश्लेषण गर्छ। प्रोजेक्टले `Microsoft.ML.OnnxRuntime` लाइब्रेरीहरू प्रयोग गरी स्थानीय ONNX Phi-3 भिजन मोडेल लोड गर्छ। प्रोजेक्टले प्रयोगकर्तासँग अन्तरक्रिया गर्न विभिन्न विकल्पहरू सहित मेनु पनि प्रस्तुत गर्छ। | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | नमूना कन्सोल च्याट जसले प्रयोगकर्तालाई प्रश्न सोध्न अनुमति दिन्छ। प्रोजेक्टले `Microsoft.ML.OnnxRuntime` लाइब्रेरीहरू प्रयोग गरी स्थानीय ONNX Phi-4 मोडेल लोड गर्छ। |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | नमूना कन्सोल च्याट जसले प्रयोगकर्तालाई प्रश्न सोध्न अनुमति दिन्छ। प्रोजेक्टले `Semantic Kernel` लाइब्रेरीहरू प्रयोग गरी स्थानीय ONNX Phi-4 मोडेल लोड गर्छ। |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | नमूना कन्सोल च्याट जसले प्रयोगकर्तालाई प्रश्न सोध्न अनुमति दिन्छ। प्रोजेक्टले `Microsoft.ML.OnnxRuntimeGenAI` लाइब्रेरीहरू प्रयोग गरी स्थानीय ONNX Phi-4 मोडेल लोड गर्छ र `Microsoft.Extensions.AI` बाट `IChatClient` कार्यान्वयन गर्छ। |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | नमूना कन्सोल च्याट जसले प्रयोगकर्तालाई प्रश्न सोध्न अनुमति दिन्छ। च्याटले मेमोरी कार्यान्वयन गर्छ। |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | यो नमूना प्रोजेक्टले स्थानीय Phi-4 मोडेल प्रयोग गरी तस्बिरहरू विश्लेषण गर्छ र नतिजा कन्सोलमा देखाउँछ। प्रोजेक्टले `Microsoft.ML.OnnxRuntime` लाइब्रेरीहरू प्रयोग गरी स्थानीय Phi-4-`multimodal-instruct-onnx` मोडेल लोड गर्छ। |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | यो नमूना प्रोजेक्टले स्थानीय Phi-4 मोडेल प्रयोग गरी अडियो फाइल विश्लेषण गर्छ, फाइलको ट्रान्सक्रिप्ट तयार गर्छ र नतिजा कन्सोलमा देखाउँछ। प्रोजेक्टले `Microsoft.ML.OnnxRuntime` लाइब्रेरीहरू प्रयोग गरी स्थानीय Phi-4-`multimodal-instruct-onnx` मोडेल लोड गर्छ। |

## प्रोजेक्टहरू कसरी चलाउने

प्रोजेक्टहरू चलाउनका लागि यी चरणहरू पालना गर्नुहोस्:

1. रिपोजिटोरीलाई तपाईंको स्थानीय मेसिनमा क्लोन गर्नुहोस्।

1. टर्मिनल खोल्नुहोस् र इच्छित प्रोजेक्टमा जानुहोस्। उदाहरणका लागि, `LabsPhi4-Chat-01OnnxRuntime` चलाऔं।

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. प्रोजेक्ट यस कमाण्डले चलाउनुहोस्

    ```bash
    dotnet run
    ```

1. नमूना प्रोजेक्टले प्रयोगकर्ताबाट इनपुट माग्छ र स्थानीय मोडेल प्रयोग गरी जवाफ दिन्छ।

   चलिरहेको डेमो यस प्रकार देखिन्छ:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।