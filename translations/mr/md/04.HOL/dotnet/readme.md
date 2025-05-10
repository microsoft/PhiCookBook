<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-05-09T22:42:38+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "mr"
}
-->
﻿## Phi labs मध्ये C# वापरून स्वागत आहे

Phi मॉडेल्सच्या विविध शक्तिशाली आवृत्त्यांना .NET पर्यावरणात कसे एकत्रित करायचे हे दाखवणाऱ्या काही लॅब्सची निवड येथे आहे.

## आवश्यक अटी

सँपल चालवण्यापूर्वी, खालील गोष्टी तुमच्या संगणकावर इंस्टॉल आहेत याची खात्री करा:

**.NET 9:** तुमच्या मशीनवर [ताजी .NET आवृत्ती](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) इंस्टॉल आहे याची खात्री करा.

**(ऐच्छिक) Visual Studio किंवा Visual Studio Code:** तुम्हाला .NET प्रोजेक्ट्स चालवण्यासाठी एखादे IDE किंवा कोड एडिटर लागेल. [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) किंवा [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) वापरण्याचा सल्ला दिला आहे.

**git वापरून** स्थानिक पद्धतीने Phi-3, Phi3.5 किंवा Phi-4 आवृत्त्यांपैकी कोणतीही एक आवृत्ती [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c) वरून क्लोन करा.

**Phi-4 ONNX मॉडेल्स** तुमच्या स्थानिक संगणकावर डाउनलोड करा:

### मॉडेल्स साठवण्यासाठी फोल्डरमध्ये जा

```bash
cd c:\phi\models
```

### lfs साठी सपोर्ट जोडा

```bash
git lfs install 
```

### Phi-4 मिनी इंस्ट्रक्ट मॉडेल आणि Phi-4 मल्टी मोडल मॉडेल क्लोन व डाउनलोड करा

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Phi-3 ONNX मॉडेल्स** तुमच्या स्थानिक संगणकावर डाउनलोड करा:

### Phi-3 मिनी 4K इंस्ट्रक्ट मॉडेल आणि Phi-3 व्हिजन 128K मॉडेल क्लोन व डाउनलोड करा

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**महत्वाचे:** सध्याच्या डेमोज ONNX आवृत्त्यांचा वापर करण्यासाठी डिझाइन केलेले आहेत. वरील स्टेप्स खालील मॉडेल्स क्लोन करतात.

## लॅब्स विषयी

मुख्य सोल्यूशनमध्ये अनेक नमुना लॅब्स आहेत जे C# वापरून Phi मॉडेल्सच्या क्षमता दाखवतात.

| प्रोजेक्ट | मॉडेल | वर्णन |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 किंवा Phi-3.5 | एक नमुना कन्सोल चॅट ज्यात वापरकर्ता प्रश्न विचारू शकतो. प्रोजेक्ट स्थानिक ONNX Phi-3 मॉडेल लोड करतो `Microsoft.ML.OnnxRuntime` libraries. |
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

1. Open a terminal and navigate to the desired project. In example, let's run `LabsPhi4-Chat-01OnnxRuntime` वापरून.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. प्रोजेक्ट खालील कमांडने चालवा

    ```bash
    dotnet run
    ```

1. नमुना प्रोजेक्ट वापरकर्त्याकडून इनपुट मागतो आणि स्थानिक मॉडेल वापरून उत्तर देतो.

   चालू असलेला डेमो यासारखा आहे:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील आहोत, तरी कृपया लक्षात ठेवा की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याचा सल्ला दिला जातो. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.