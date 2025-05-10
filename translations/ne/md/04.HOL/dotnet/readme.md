<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-05-09T22:42:47+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "ne"
}
-->
﻿## C# प्रयोग गर्दै Phi ल्याबहरूमा स्वागत छ

Phi मोडेलका विभिन्न शक्तिशाली संस्करणहरूलाई .NET वातावरणमा कसरी एकीकृत गर्ने देखाउने ल्याबहरूको चयन यहाँ उपलब्ध छ।

## पूर्वशर्तहरू

नमूना चलाउनु अघि, तपाईंसँग तलका वस्तुहरू इन्स्टल गरिएको छ भनी सुनिश्चित गर्नुहोस्:

**.NET 9:** आफ्नो मेसिनमा [सबैभन्दा नयाँ .NET संस्करण](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) इन्स्टल गरेको सुनिश्चित गर्नुहोस्।

**(वैकल्पिक) Visual Studio वा Visual Studio Code:** .NET प्रोजेक्टहरू चलाउन सक्ने IDE वा कोड सम्पादक आवश्यक पर्छ। [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) वा [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) सिफारिस गरिन्छ।

**Git प्रयोग गर्दै** स्थानीय रूपमा Hugging Face बाट उपलब्ध Phi-3, Phi3.5 वा Phi-4 संस्करणहरू मध्ये कुनै एक क्लोन गर्नुहोस्: [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c)।

**Phi-4 ONNX मोडेलहरू** आफ्नो स्थानीय मेसिनमा डाउनलोड गर्नुहोस्:

### मोडेलहरू भण्डारण गर्नको लागि फोल्डरमा जानुहोस्

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

**Phi-3 ONNX मोडेलहरू** आफ्नो स्थानीय मेसिनमा डाउनलोड गर्नुहोस्:

### Phi-3 मिनी 4K इन्स्ट्रक्ट मोडेल र Phi-3 भिजन 128K मोडेल क्लोन र डाउनलोड गर्नुहोस्

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**महत्वपूर्ण:** हालका डेमोहरू मोडेलका ONNX संस्करणहरू प्रयोग गर्न डिजाइन गरिएको छ। माथिका चरणहरूले तलका मोडेलहरू क्लोन गर्छन्।

## ल्याबहरूको बारेमा

मुख्य समाधानमा C# प्रयोग गरी Phi मोडेलहरूको क्षमता प्रदर्शन गर्ने विभिन्न नमूना ल्याबहरू छन्।

| प्रोजेक्ट | मोडेल | विवरण |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 वा Phi-3.5 | प्रयोगकर्तालाई प्रश्न सोध्न अनुमति दिने नमूना कन्सोल च्याट। प्रोजेक्टले स्थानीय ONNX Phi-3 मोडेल लोड गर्छ `Microsoft.ML.OnnxRuntime` libraries. |
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

1. Open a terminal and navigate to the desired project. In example, let's run `LabsPhi4-Chat-01OnnxRuntime` प्रयोग गरेर।

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. प्रोजेक्ट यस कमाण्डबाट चलाउनुहोस्

    ```bash
    dotnet run
    ```

1. नमूना प्रोजेक्टले प्रयोगकर्ताबाट इनपुट माग्छ र स्थानीय मोडेल प्रयोग गरी जवाफ दिन्छ।

   चलिरहेको डेमो यस प्रकार छ:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुनसक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानवीय अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार छैनौं।