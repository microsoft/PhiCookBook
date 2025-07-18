<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-07-17T10:36:38+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "tr"
}
-->
﻿## C# ile Phi laboratuvarlarına hoş geldiniz

.NET ortamında Phi modellerinin farklı güçlü versiyonlarını nasıl entegre edeceğinizi gösteren çeşitli laboratuvar örnekleri bulunmaktadır.

## Gereksinimler

Örneği çalıştırmadan önce aşağıdakilerin yüklü olduğundan emin olun:

**.NET 9:** Makinenizde [en son .NET sürümünün](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) yüklü olduğundan emin olun.

**(İsteğe bağlı) Visual Studio veya Visual Studio Code:** .NET projelerini çalıştırabilecek bir IDE veya kod editörüne ihtiyacınız olacak. [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) veya [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) önerilir.

**Git kullanarak** Hugging Face’den [Phi-3, Phi3.5 veya Phi-4 versiyonlarından](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c) birini yerel olarak klonlayın.

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

**Önemli:** Mevcut demolar modelin ONNX versiyonlarını kullanacak şekilde tasarlanmıştır. Önceki adımlar aşağıdaki modelleri klonlar.

## Laboratuvarlar Hakkında

Ana çözüm, C# kullanarak Phi modellerinin yeteneklerini gösteren birkaç örnek laboratuvar içerir.

| Proje | Model | Açıklama |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 veya Phi-3.5 | Kullanıcının soru sormasına izin veren örnek konsol sohbeti. Proje, `Microsoft.ML.OnnxRuntime` kütüphanelerini kullanarak yerel bir ONNX Phi-3 modelini yükler. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 veya Phi-3.5 | Kullanıcının soru sormasına izin veren örnek konsol sohbeti. Proje, `Microsoft.Semantic.Kernel` kütüphanelerini kullanarak yerel bir ONNX Phi-3 modelini yükler. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 veya Phi-3.5 | Yerel phi3 vision modelini kullanarak görüntüleri analiz eden örnek proje. Proje, `Microsoft.ML.OnnxRuntime` kütüphanelerini kullanarak yerel bir ONNX Phi-3 Vision modelini yükler. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 veya Phi-3.5 | Yerel phi3 vision modelini kullanarak görüntüleri analiz eden örnek proje. Proje, `Microsoft.ML.OnnxRuntime` kütüphanelerini kullanarak yerel bir ONNX Phi-3 Vision modelini yükler. Ayrıca kullanıcı ile etkileşim için farklı seçenekler sunan bir menü içerir. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Kullanıcının soru sormasına izin veren örnek konsol sohbeti. Proje, `Microsoft.ML.OnnxRuntime` kütüphanelerini kullanarak yerel bir ONNX Phi-4 modelini yükler. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Kullanıcının soru sormasına izin veren örnek konsol sohbeti. Proje, `Semantic Kernel` kütüphanelerini kullanarak yerel bir ONNX Phi-4 modelini yükler. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Kullanıcının soru sormasına izin veren örnek konsol sohbeti. Proje, `Microsoft.ML.OnnxRuntimeGenAI` kütüphanelerini kullanarak yerel bir ONNX Phi-4 modelini yükler ve `Microsoft.Extensions.AI` içindeki `IChatClient` arayüzünü uygular. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Kullanıcının soru sormasına izin veren örnek konsol sohbeti. Sohbet belleği uygular. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | Yerel Phi-4 modelini kullanarak görüntüleri analiz eden ve sonucu konsolda gösteren örnek proje. Proje, `Microsoft.ML.OnnxRuntime` kütüphanelerini kullanarak yerel Phi-4-`multimodal-instruct-onnx` modelini yükler. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | Yerel Phi-4 modelini kullanarak bir ses dosyasını analiz eden, dosyanın transkriptini oluşturan ve sonucu konsolda gösteren örnek proje. Proje, `Microsoft.ML.OnnxRuntime` kütüphanelerini kullanarak yerel Phi-4-`multimodal-instruct-onnx` modelini yükler. |

## Projelerin Çalıştırılması

Projeleri çalıştırmak için şu adımları izleyin:

1. Depoyu yerel makinenize klonlayın.

1. Bir terminal açın ve istediğiniz projeye gidin. Örneğin, `LabsPhi4-Chat-01OnnxRuntime` projesini çalıştıralım.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Projeyi şu komutla çalıştırın

    ```bash
    dotnet run
    ```

1. Örnek proje kullanıcıdan giriş ister ve yerel modeli kullanarak yanıt verir.

   Çalışan demo şu şekilde görünür:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.