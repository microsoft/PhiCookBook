<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-05-09T22:42:56+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "pa"
}
-->
﻿## C# ਨਾਲ Phi ਲੈਬਜ਼ ਵਿੱਚ ਤੁਹਾਡਾ ਸਵਾਗਤ ਹੈ

ਇੱਕ ਚੁਣੀ ਹੋਈ ਲੈਬਜ਼ ਦੀ ਲੜੀ ਹੈ ਜੋ ਦਿਖਾਉਂਦੀ ਹੈ ਕਿ ਕਿਵੇਂ ਵੱਖ-ਵੱਖ ਸ਼ਕਤਸ਼ਾਲੀ Phi ਮਾਡਲਾਂ ਨੂੰ .NET ਵਾਤਾਵਰਨ ਵਿੱਚ ਜੋੜਿਆ ਜਾ ਸਕਦਾ ਹੈ।

## ਜ਼ਰੂਰੀ ਸ਼ਰਤਾਂ

ਨਮੂਨਾ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ, ਇਹ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਹੇਠਾਂ ਦਿੱਤੀਆਂ ਚੀਜ਼ਾਂ ਇੰਸਟਾਲ ਹਨ:

**.NET 9:** ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਹਾਡੇ ਮਸ਼ੀਨ 'ਤੇ [ਨਵੀਂਤਮ .NET ਵਰਜਨ](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) ਇੰਸਟਾਲ ਹੈ।

**(ਵਿਕਲਪਿਕ) Visual Studio ਜਾਂ Visual Studio Code:** ਤੁਹਾਨੂੰ ਐਸਾ IDE ਜਾਂ ਕੋਡ ਐਡੀਟਰ ਚਾਹੀਦਾ ਹੈ ਜੋ .NET ਪ੍ਰੋਜੈਕਟ ਚਲਾ ਸਕੇ। [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) ਜਾਂ [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ।

**git ਦੀ ਵਰਤੋਂ ਕਰਦਿਆਂ** ਸਥਾਨਕ ਤੌਰ 'ਤੇ Phi-3, Phi3.5 ਜਾਂ Phi-4 ਦੇ ਉਪਲਬਧ ਵਰਜਨਾਂ ਵਿੱਚੋਂ ਕਿਸੇ ਇੱਕ ਨੂੰ [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c) ਤੋਂ ਕਲੋਨ ਕਰੋ।

**Phi-4 ONNX ਮਾਡਲਾਂ ਨੂੰ ਆਪਣੇ ਮਸ਼ੀਨ 'ਤੇ ਡਾਊਨਲੋਡ ਕਰੋ:**

### ਮਾਡਲ ਸਟੋਰ ਕਰਨ ਲਈ ਫੋਲਡਰ ਵਿੱਚ ਜਾਓ

```bash
cd c:\phi\models
```

### lfs ਲਈ ਸਹਾਇਤਾ ਸ਼ਾਮਲ ਕਰੋ

```bash
git lfs install 
```

### Phi-4 ਮਿਨੀ ਇੰਸਟ੍ਰਕਟ ਮਾਡਲ ਅਤੇ Phi-4 ਮਲਟੀ ਮੋਡਲ ਮਾਡਲ ਕਲੋਨ ਅਤੇ ਡਾਊਨਲੋਡ ਕਰੋ

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Phi-3 ONNX ਮਾਡਲਾਂ ਨੂੰ ਆਪਣੇ ਮਸ਼ੀਨ 'ਤੇ ਡਾਊਨਲੋਡ ਕਰੋ:**

### Phi-3 ਮਿਨੀ 4K ਇੰਸਟ੍ਰਕਟ ਮਾਡਲ ਅਤੇ Phi-3 ਵਿਜ਼ਨ 128K ਮਾਡਲ ਕਲੋਨ ਅਤੇ ਡਾਊਨਲੋਡ ਕਰੋ

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**ਮਹੱਤਵਪੂਰਣ:** ਮੌਜੂਦਾ ਡੈਮੋਜ਼ ਮਾਡਲ ਦੇ ONNX ਵਰਜਨਾਂ ਦੀ ਵਰਤੋਂ ਲਈ ਬਣਾਏ ਗਏ ਹਨ। ਪਿਛਲੇ ਕਦਮ ਹੇਠ ਲਿਖੇ ਮਾਡਲ ਕਲੋਨ ਕਰਦੇ ਹਨ।

## ਲੈਬਜ਼ ਬਾਰੇ

ਮੁੱਖ ਹੱਲ ਵਿੱਚ ਕਈ ਨਮੂਨਾ ਲੈਬਜ਼ ਹਨ ਜੋ C# ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi ਮਾਡਲਾਂ ਦੀ ਸਮਰੱਥਾ ਦਰਸਾਉਂਦੇ ਹਨ।

| ਪ੍ਰੋਜੈਕਟ | ਮਾਡਲ | ਵੇਰਵਾ |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 ਜਾਂ Phi-3.5 | ਨਮੂਨਾ ਕਨਸੋਲ ਚੈਟ ਜੋ ਯੂਜ਼ਰ ਨੂੰ ਸਵਾਲ ਪੁੱਛਣ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ। ਪ੍ਰੋਜੈਕਟ ਇੱਕ ਸਥਾਨਕ ONNX Phi-3 ਮਾਡਲ ਨੂੰ ਲੋਡ ਕਰਦਾ ਹੈ `Microsoft.ML.OnnxRuntime` libraries. |
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

1. Open a terminal and navigate to the desired project. In example, let's run `LabsPhi4-Chat-01OnnxRuntime` ਦੀ ਵਰਤੋਂ ਕਰਦਿਆਂ।

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. ਪ੍ਰੋਜੈਕਟ ਨੂੰ ਇਸ ਕਮਾਂਡ ਨਾਲ ਚਲਾਓ

    ```bash
    dotnet run
    ```

1. ਨਮੂਨਾ ਪ੍ਰੋਜੈਕਟ ਯੂਜ਼ਰ ਤੋਂ ਇਨਪੁਟ ਮੰਗਦਾ ਹੈ ਅਤੇ ਸਥਾਨਕ ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਜਵਾਬ ਦਿੰਦਾ ਹੈ।

   ਚਲ ਰਹੇ ਡੈਮੋ ਦਾ ਅੰਦਾਜ਼ਾ ਇਸ ਤਰ੍ਹਾਂ ਹੈ:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**ਅਸਵੀਕਾਰੋਪਣੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਨਾਲ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਣ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਨਾਲ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।