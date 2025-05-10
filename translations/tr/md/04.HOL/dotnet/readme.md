<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-05-09T22:43:40+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "tr"
}
-->
﻿## C# kullanarak Phi laboratuvarlarına hoş geldiniz

.NET ortamında Phi modellerinin güçlü farklı sürümlerini nasıl entegre edeceğinizi gösteren çeşitli laboratuvar örnekleri bulunmaktadır.

## Önkoşullar

Örneği çalıştırmadan önce, aşağıdakilerin yüklü olduğundan emin olun:

**.NET 9:** Makinenizde [en son .NET sürümünün](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) yüklü olduğundan emin olun.

**(İsteğe bağlı) Visual Studio veya Visual Studio Code:** .NET projelerini çalıştırabilecek bir IDE veya kod düzenleyiciye ihtiyacınız olacak. [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) veya [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) önerilir.

**Git kullanarak** Hugging Face'den [Phi-3, Phi3.5 veya Phi-4 sürümlerinden](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c) birini yerel olarak klonlayın.

**Phi-4 ONNX modellerini** yerel makinenize indirin:

### Modelleri depolamak için klasöre gidin

```bash
cd c:\phi\models
```

### lfs desteği ekleyin

```bash
git lfs install 
```

### Phi-4 mini instruct modeli ve Phi-4 çok modlu modeli klonlayıp indirin

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Phi-3 ONNX modellerini** yerel makinenize indirin:

### Phi-3 mini 4K instruct modeli ve Phi-3 vision 128K modelini klonlayıp indirin

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Önemli:** Mevcut demolar modelin ONNX sürümlerini kullanacak şekilde tasarlanmıştır. Önceki adımlar aşağıdaki modelleri klonlar.

## Laboratuvarlar Hakkında

Ana çözüm, C# kullanarak Phi modellerinin yeteneklerini gösteren birkaç örnek laboratuvar içerir.

| Proje | Model | Açıklama |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 veya Phi-3.5 | Kullanıcının soru sormasına izin veren örnek konsol sohbeti. Proje, yerel bir ONNX Phi-3 modelini `Microsoft.ML.OnnxRuntime` libraries. |
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

1. Open a terminal and navigate to the desired project. In example, let's run `LabsPhi4-Chat-01OnnxRuntime` kullanarak yükler.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Projeyi şu komutla çalıştırın

    ```bash
    dotnet run
    ```

1. Örnek proje kullanıcıdan giriş ister ve yerel modeli kullanarak yanıt verir.

   Çalışan demo şu örneğe benzer:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı nedeniyle ortaya çıkabilecek yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul edilmemektedir.