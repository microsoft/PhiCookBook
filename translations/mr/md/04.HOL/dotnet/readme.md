<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-07-17T10:34:26+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "mr"
}
-->
﻿## C# वापरून Phi लॅब्समध्ये आपले स्वागत आहे

.NET वातावरणात Phi मॉडेल्सच्या विविध शक्तिशाली आवृत्त्यांना कसे एकत्रित करायचे हे दाखवणाऱ्या लॅब्सची निवड येथे आहे.

## पूर्वअट

नमुना चालवण्यापूर्वी, खालील गोष्टी आपल्या संगणकावर स्थापित असल्याची खात्री करा:

**.NET 9:** आपल्या मशीनवर [नवीनतम .NET आवृत्ती](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) स्थापित आहे याची खात्री करा.

**(ऐच्छिक) Visual Studio किंवा Visual Studio Code:** .NET प्रोजेक्ट्स चालवण्यासाठी सक्षम असलेले IDE किंवा कोड एडिटर आवश्यक आहे. [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) किंवा [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) यांची शिफारस केली जाते.

**git वापरून** स्थानिकपणे Phi-3, Phi3.5 किंवा Phi-4 आवृत्त्यांपैकी कोणतीही एक [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c) वरून क्लोन करा.

**Phi-4 ONNX मॉडेल्स** आपल्या स्थानिक मशीनवर डाउनलोड करा:

### मॉडेल्स साठवण्यासाठी फोल्डरमध्ये जा

```bash
cd c:\phi\models
```

### lfs साठी समर्थन जोडा

```bash
git lfs install 
```

### Phi-4 मिनी इन्स्ट्रक्ट मॉडेल आणि Phi-4 मल्टी मोडाल मॉडेल क्लोन आणि डाउनलोड करा

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Phi-3 ONNX मॉडेल्स** आपल्या स्थानिक मशीनवर डाउनलोड करा:

### Phi-3 मिनी 4K इन्स्ट्रक्ट मॉडेल आणि Phi-3 व्हिजन 128K मॉडेल क्लोन आणि डाउनलोड करा

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**महत्त्वाचे:** सध्याचे डेमो मॉडेलच्या ONNX आवृत्त्यांचा वापर करण्यासाठी डिझाइन केलेले आहेत. मागील टप्प्यांमध्ये खालील मॉडेल्स क्लोन केले जातात.

## लॅब्स विषयी

मुख्य सोल्यूशनमध्ये अनेक नमुना लॅब्स आहेत जे C# वापरून Phi मॉडेल्सच्या क्षमतांचे प्रदर्शन करतात.

| प्रोजेक्ट | मॉडेल | वर्णन |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 किंवा Phi-3.5 | वापरकर्त्याला प्रश्न विचारण्याची परवानगी देणारा नमुना कन्सोल चॅट. प्रोजेक्ट स्थानिक ONNX Phi-3 मॉडेल `Microsoft.ML.OnnxRuntime` लायब्ररी वापरून लोड करतो. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 किंवा Phi-3.5 | वापरकर्त्याला प्रश्न विचारण्याची परवानगी देणारा नमुना कन्सोल चॅट. प्रोजेक्ट स्थानिक ONNX Phi-3 मॉडेल `Microsoft.Semantic.Kernel` लायब्ररी वापरून लोड करतो. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 किंवा Phi-3.5 | हा एक नमुना प्रोजेक्ट आहे जो स्थानिक phi3 व्हिजन मॉडेल वापरून प्रतिमा विश्लेषित करतो. प्रोजेक्ट स्थानिक ONNX Phi-3 Vision मॉडेल `Microsoft.ML.OnnxRuntime` लायब्ररी वापरून लोड करतो. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 किंवा Phi-3.5 | हा एक नमुना प्रोजेक्ट आहे जो स्थानिक phi3 व्हिजन मॉडेल वापरून प्रतिमा विश्लेषित करतो. प्रोजेक्ट स्थानिक ONNX Phi-3 Vision मॉडेल `Microsoft.ML.OnnxRuntime` लायब्ररी वापरून लोड करतो. प्रोजेक्ट वापरकर्त्याशी संवाद साधण्यासाठी विविध पर्यायांसह मेनू देखील सादर करतो. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | वापरकर्त्याला प्रश्न विचारण्याची परवानगी देणारा नमुना कन्सोल चॅट. प्रोजेक्ट स्थानिक ONNX Phi-4 मॉडेल `Microsoft.ML.OnnxRuntime` लायब्ररी वापरून लोड करतो. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | वापरकर्त्याला प्रश्न विचारण्याची परवानगी देणारा नमुना कन्सोल चॅट. प्रोजेक्ट स्थानिक ONNX Phi-4 मॉडेल `Semantic Kernel` लायब्ररी वापरून लोड करतो. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | वापरकर्त्याला प्रश्न विचारण्याची परवानगी देणारा नमुना कन्सोल चॅट. प्रोजेक्ट स्थानिक ONNX Phi-4 मॉडेल `Microsoft.ML.OnnxRuntimeGenAI` लायब्ररी वापरून लोड करतो आणि `Microsoft.Extensions.AI` मधील `IChatClient` अंमलात आणतो. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | वापरकर्त्याला प्रश्न विचारण्याची परवानगी देणारा नमुना कन्सोल चॅट. चॅटमध्ये मेमरीची अंमलबजावणी आहे. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | हा एक नमुना प्रोजेक्ट आहे जो स्थानिक Phi-4 मॉडेल वापरून प्रतिमा विश्लेषित करतो आणि निकाल कन्सोलमध्ये दाखवतो. प्रोजेक्ट स्थानिक Phi-4-`multimodal-instruct-onnx` मॉडेल `Microsoft.ML.OnnxRuntime` लायब्ररी वापरून लोड करतो. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | हा एक नमुना प्रोजेक्ट आहे जो स्थानिक Phi-4 मॉडेल वापरून ऑडिओ फाइलचे विश्लेषण करतो, फाइलचा ट्रान्सक्रिप्ट तयार करतो आणि निकाल कन्सोलमध्ये दाखवतो. प्रोजेक्ट स्थानिक Phi-4-`multimodal-instruct-onnx` मॉडेल `Microsoft.ML.OnnxRuntime` लायब्ररी वापरून लोड करतो. |

## प्रोजेक्ट्स कसे चालवायचे

प्रोजेक्ट्स चालवण्यासाठी खालील टप्पे पाळा:

1. रिपॉझिटरी आपल्या स्थानिक मशीनवर क्लोन करा.

1. टर्मिनल उघडा आणि इच्छित प्रोजेक्टच्या फोल्डरमध्ये जा. उदाहरणार्थ, `LabsPhi4-Chat-01OnnxRuntime` चालवूया.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. खालील कमांडने प्रोजेक्ट चालवा

    ```bash
    dotnet run
    ```

1. नमुना प्रोजेक्ट वापरकर्त्याचा इनपुट मागतो आणि स्थानिक मॉडेल वापरून उत्तर देतो.

   चालू असलेले डेमो खालीलप्रमाणे दिसते:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.