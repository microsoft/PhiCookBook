<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-05-09T12:24:48+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "tr"
}
-->
Phi-3-mini bağlamında, çıkarım, modelin giriş verilerine dayanarak tahminler yapmak veya çıktı üretmek için kullanılması sürecini ifade eder. Phi-3-mini ve çıkarım yetenekleri hakkında size daha fazla bilgi vereyim.

Phi-3-mini, Microsoft tarafından yayınlanan Phi-3 serisi modellerin bir parçasıdır. Bu modeller, Küçük Dil Modelleri (SLM'ler) ile mümkün olanı yeniden tanımlamak için tasarlanmıştır.

İşte Phi-3-mini ve çıkarım yetenekleri hakkında bazı önemli noktalar:

## **Phi-3-mini Genel Bakış:**
- Phi-3-mini'nin parametre boyutu 3.8 milyardır.
- Geleneksel bilgisayar cihazlarının yanı sıra mobil cihazlar ve IoT cihazları gibi uç cihazlarda da çalışabilir.
- Phi-3-mini'nin yayınlanması, bireylerin ve işletmelerin özellikle kaynak kısıtlı ortamlarda farklı donanım cihazlarında SLM'leri dağıtmasını sağlar.
- Geleneksel PyTorch formatı, gguf formatının kuantize edilmiş versiyonu ve ONNX tabanlı kuantize versiyon gibi çeşitli model formatlarını kapsar.

## **Phi-3-mini'ye Erişim:**
Phi-3-mini'ye erişmek için Copilot uygulamasında [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) kullanabilirsiniz. Semantic Kernel genellikle Azure OpenAI Service, Hugging Face üzerindeki açık kaynak modeller ve yerel modellerle uyumludur.
Ayrıca kuantize modelleri çağırmak için [Ollama](https://ollama.com) veya [LlamaEdge](https://llamaedge.com) kullanabilirsiniz. Ollama bireysel kullanıcıların farklı kuantize modelleri çağırmasına olanak tanırken, LlamaEdge GGUF modelleri için platformlar arası erişim sağlar.

## **Kuantize Modeller:**
Birçok kullanıcı yerel çıkarım için kuantize modelleri kullanmayı tercih eder. Örneğin, Ollama ile Phi-3'ü doğrudan çalıştırabilir veya Modelfile kullanarak çevrimdışı yapılandırabilirsiniz. Modelfile, GGUF dosya yolunu ve prompt formatını belirtir.

## **Üretken Yapay Zeka Olanakları:**
Phi-3-mini gibi SLM'lerin birleşimi, üretken yapay zeka için yeni olanaklar sunar. Çıkarım sadece ilk adımdır; bu modeller kaynak kısıtlı, gecikme sınırlandırılmış ve maliyet kısıtlı senaryolarda çeşitli görevler için kullanılabilir.

## **Phi-3-mini ile Üretken Yapay Zekayı Açmak: Çıkarım ve Dağıtım Rehberi**
Semantic Kernel, Ollama/LlamaEdge ve ONNX Runtime kullanarak Phi-3-mini modellerine erişmeyi ve çıkarım yapmayı öğrenin, ayrıca çeşitli uygulama senaryolarında üretken yapay zekanın olanaklarını keşfedin.

**Özellikler**  
phi3-mini modelini çıkarımda kullanma:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)  

Özetle, Phi-3-mini geliştiricilere farklı model formatlarını keşfetme ve çeşitli uygulama senaryolarında üretken yapay zekayı kullanma imkanı sunar.

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucunda oluşabilecek yanlış anlamalar veya yanlış yorumlamalardan dolayı sorumluluk kabul edilmemektedir.