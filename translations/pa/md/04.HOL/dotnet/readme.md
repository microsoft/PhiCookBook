<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-07-17T10:35:06+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "pa"
}
-->
﻿## C# ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi ਲੈਬਜ਼ ਵਿੱਚ ਤੁਹਾਡਾ ਸਵਾਗਤ ਹੈ

ਇੱਥੇ ਕੁਝ ਲੈਬਜ਼ ਹਨ ਜੋ ਦਿਖਾਉਂਦੇ ਹਨ ਕਿ ਕਿਵੇਂ ਵੱਖ-ਵੱਖ Phi ਮਾਡਲਾਂ ਦੇ ਤਾਕਤਵਰ ਵਰਜਨਾਂ ਨੂੰ .NET ਮਾਹੌਲ ਵਿੱਚ ਇੰਟੀਗ੍ਰੇਟ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।

## ਲੋੜੀਂਦੀਆਂ ਚੀਜ਼ਾਂ

ਸੈਂਪਲ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ, ਇਹ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਹੇਠਾਂ ਦਿੱਤੀਆਂ ਚੀਜ਼ਾਂ ਇੰਸਟਾਲ ਹਨ:

**.NET 9:** ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਹਾਡੇ ਕੰਪਿਊਟਰ 'ਤੇ [ਨਵੀਂ .NET ਵਰਜਨ](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) ਇੰਸਟਾਲ ਹੈ।

**(ਵਿਕਲਪਿਕ) Visual Studio ਜਾਂ Visual Studio Code:** ਤੁਹਾਨੂੰ ਇੱਕ IDE ਜਾਂ ਕੋਡ ਐਡੀਟਰ ਦੀ ਲੋੜ ਹੋਵੇਗੀ ਜੋ .NET ਪ੍ਰੋਜੈਕਟ ਚਲਾ ਸਕੇ। [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) ਜਾਂ [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ।

**git ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋਏ** Hugging Face ਤੋਂ Phi-3, Phi3.5 ਜਾਂ Phi-4 ਦੇ ਉਪਲਬਧ ਵਰਜਨਾਂ ਵਿੱਚੋਂ ਕਿਸੇ ਇੱਕ ਨੂੰ ਲੋਕਲ ਕਲੋਨ ਕਰੋ [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c)।

**Phi-4 ONNX ਮਾਡਲ ਆਪਣੇ ਲੋਕਲ ਮਸ਼ੀਨ 'ਤੇ ਡਾਊਨਲੋਡ ਕਰੋ:**

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

**Phi-3 ONNX ਮਾਡਲ ਆਪਣੇ ਲੋਕਲ ਮਸ਼ੀਨ 'ਤੇ ਡਾਊਨਲੋਡ ਕਰੋ:**

### Phi-3 ਮਿਨੀ 4K ਇੰਸਟ੍ਰਕਟ ਮਾਡਲ ਅਤੇ Phi-3 ਵਿਜ਼ਨ 128K ਮਾਡਲ ਕਲੋਨ ਅਤੇ ਡਾਊਨਲੋਡ ਕਰੋ

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**ਮਹੱਤਵਪੂਰਨ:** ਮੌਜੂਦਾ ਡੈਮੋਜ਼ ONNX ਵਰਜਨਾਂ ਦੀ ਵਰਤੋਂ ਲਈ ਬਣਾਏ ਗਏ ਹਨ। ਪਿਛਲੇ ਕਦਮ ਹੇਠਾਂ ਦਿੱਤੇ ਮਾਡਲ ਕਲੋਨ ਕਰਦੇ ਹਨ।

## ਲੈਬਜ਼ ਬਾਰੇ

ਮੁੱਖ ਸੌਲਿਊਸ਼ਨ ਵਿੱਚ ਕਈ ਸੈਂਪਲ ਲੈਬਜ਼ ਹਨ ਜੋ C# ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi ਮਾਡਲਾਂ ਦੀਆਂ ਖੂਬੀਆਂ ਦਿਖਾਉਂਦੇ ਹਨ।

| ਪ੍ਰੋਜੈਕਟ | ਮਾਡਲ | ਵੇਰਵਾ |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 ਜਾਂ Phi-3.5 | ਸੈਂਪਲ ਕਨਸੋਲ ਚੈਟ ਜੋ ਯੂਜ਼ਰ ਨੂੰ ਸਵਾਲ ਪੁੱਛਣ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ। ਪ੍ਰੋਜੈਕਟ `Microsoft.ML.OnnxRuntime` ਲਾਇਬ੍ਰੇਰੀਜ਼ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਲੋਕਲ ONNX Phi-3 ਮਾਡਲ ਲੋਡ ਕਰਦਾ ਹੈ। |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 ਜਾਂ Phi-3.5 | ਸੈਂਪਲ ਕਨਸੋਲ ਚੈਟ ਜੋ ਯੂਜ਼ਰ ਨੂੰ ਸਵਾਲ ਪੁੱਛਣ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ। ਪ੍ਰੋਜੈਕਟ `Microsoft.Semantic.Kernel` ਲਾਇਬ੍ਰੇਰੀਜ਼ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਲੋਕਲ ONNX Phi-3 ਮਾਡਲ ਲੋਡ ਕਰਦਾ ਹੈ। |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 ਜਾਂ Phi-3.5 | ਇਹ ਇੱਕ ਸੈਂਪਲ ਪ੍ਰੋਜੈਕਟ ਹੈ ਜੋ ਲੋਕਲ phi3 ਵਿਜ਼ਨ ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਤਸਵੀਰਾਂ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਦਾ ਹੈ। ਪ੍ਰੋਜੈਕਟ `Microsoft.ML.OnnxRuntime` ਲਾਇਬ੍ਰੇਰੀਜ਼ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਲੋਕਲ ONNX Phi-3 ਵਿਜ਼ਨ ਮਾਡਲ ਲੋਡ ਕਰਦਾ ਹੈ। |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 ਜਾਂ Phi-3.5 | ਇਹ ਇੱਕ ਸੈਂਪਲ ਪ੍ਰੋਜੈਕਟ ਹੈ ਜੋ ਲੋਕਲ phi3 ਵਿਜ਼ਨ ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਤਸਵੀਰਾਂ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਦਾ ਹੈ। ਪ੍ਰੋਜੈਕਟ `Microsoft.ML.OnnxRuntime` ਲਾਇਬ੍ਰੇਰੀਜ਼ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਲੋਕਲ ONNX Phi-3 ਵਿਜ਼ਨ ਮਾਡਲ ਲੋਡ ਕਰਦਾ ਹੈ। ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ ਯੂਜ਼ਰ ਨਾਲ ਇੰਟਰੈਕਟ ਕਰਨ ਲਈ ਵੱਖ-ਵੱਖ ਵਿਕਲਪਾਂ ਵਾਲਾ ਮੀਨੂ ਵੀ ਹੈ। | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | ਸੈਂਪਲ ਕਨਸੋਲ ਚੈਟ ਜੋ ਯੂਜ਼ਰ ਨੂੰ ਸਵਾਲ ਪੁੱਛਣ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ। ਪ੍ਰੋਜੈਕਟ `Microsoft.ML.OnnxRuntime` ਲਾਇਬ੍ਰੇਰੀਜ਼ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਲੋਕਲ ONNX Phi-4 ਮਾਡਲ ਲੋਡ ਕਰਦਾ ਹੈ। |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | ਸੈਂਪਲ ਕਨਸੋਲ ਚੈਟ ਜੋ ਯੂਜ਼ਰ ਨੂੰ ਸਵਾਲ ਪੁੱਛਣ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ। ਪ੍ਰੋਜੈਕਟ `Semantic Kernel` ਲਾਇਬ੍ਰੇਰੀਜ਼ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਲੋਕਲ ONNX Phi-4 ਮਾਡਲ ਲੋਡ ਕਰਦਾ ਹੈ। |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | ਸੈਂਪਲ ਕਨਸੋਲ ਚੈਟ ਜੋ ਯੂਜ਼ਰ ਨੂੰ ਸਵਾਲ ਪੁੱਛਣ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ। ਪ੍ਰੋਜੈਕਟ `Microsoft.ML.OnnxRuntimeGenAI` ਲਾਇਬ੍ਰੇਰੀਜ਼ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਲੋਕਲ ONNX Phi-4 ਮਾਡਲ ਲੋਡ ਕਰਦਾ ਹੈ ਅਤੇ `Microsoft.Extensions.AI` ਤੋਂ `IChatClient` ਨੂੰ ਇੰਪਲੀਮੈਂਟ ਕਰਦਾ ਹੈ। |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | ਸੈਂਪਲ ਕਨਸੋਲ ਚੈਟ ਜੋ ਯੂਜ਼ਰ ਨੂੰ ਸਵਾਲ ਪੁੱਛਣ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ। ਚੈਟ ਵਿੱਚ ਮੈਮੋਰੀ ਦੀ ਵਰਤੋਂ ਕੀਤੀ ਗਈ ਹੈ। |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | ਇਹ ਇੱਕ ਸੈਂਪਲ ਪ੍ਰੋਜੈਕਟ ਹੈ ਜੋ ਲੋਕਲ Phi-4 ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਤਸਵੀਰਾਂ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਦਾ ਹੈ ਅਤੇ ਨਤੀਜਾ ਕਨਸੋਲ ਵਿੱਚ ਦਿਖਾਉਂਦਾ ਹੈ। ਪ੍ਰੋਜੈਕਟ `Microsoft.ML.OnnxRuntime` ਲਾਇਬ੍ਰੇਰੀਜ਼ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਲੋਕਲ Phi-4-`multimodal-instruct-onnx` ਮਾਡਲ ਲੋਡ ਕਰਦਾ ਹੈ। |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | ਇਹ ਇੱਕ ਸੈਂਪਲ ਪ੍ਰੋਜੈਕਟ ਹੈ ਜੋ ਲੋਕਲ Phi-4 ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਡੀਓ ਫਾਈਲ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਦਾ ਹੈ, ਫਾਈਲ ਦਾ ਟ੍ਰਾਂਸਕ੍ਰਿਪਟ ਬਣਾਉਂਦਾ ਹੈ ਅਤੇ ਨਤੀਜਾ ਕਨਸੋਲ ਵਿੱਚ ਦਿਖਾਉਂਦਾ ਹੈ। ਪ੍ਰੋਜੈਕਟ `Microsoft.ML.OnnxRuntime` ਲਾਇਬ੍ਰੇਰੀਜ਼ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਲੋਕਲ Phi-4-`multimodal-instruct-onnx` ਮਾਡਲ ਲੋਡ ਕਰਦਾ ਹੈ। |

## ਪ੍ਰੋਜੈਕਟ ਕਿਵੇਂ ਚਲਾਉਣੇ

ਪ੍ਰੋਜੈਕਟ ਚਲਾਉਣ ਲਈ, ਹੇਠਾਂ ਦਿੱਤੇ ਕਦਮਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ:

1. ਰਿਪੋਜ਼ਿਟਰੀ ਨੂੰ ਆਪਣੇ ਲੋਕਲ ਮਸ਼ੀਨ 'ਤੇ ਕਲੋਨ ਕਰੋ।

1. ਟਰਮੀਨਲ ਖੋਲ੍ਹੋ ਅਤੇ ਚਾਹੁੰਦੇ ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ ਜਾਓ। ਉਦਾਹਰਨ ਵਜੋਂ, ਆਓ `LabsPhi4-Chat-01OnnxRuntime` ਚਲਾਈਏ।

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. ਕਮਾਂਡ ਨਾਲ ਪ੍ਰੋਜੈਕਟ ਚਲਾਓ

    ```bash
    dotnet run
    ```

1. ਸੈਂਪਲ ਪ੍ਰੋਜੈਕਟ ਯੂਜ਼ਰ ਇਨਪੁੱਟ ਮੰਗਦਾ ਹੈ ਅਤੇ ਲੋਕਲ ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਜਵਾਬ ਦਿੰਦਾ ਹੈ।

   ਚਲ ਰਹੇ ਡੈਮੋ ਦਾ ਨਮੂਨਾ ਇਸ ਤਰ੍ਹਾਂ ਹੈ:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।