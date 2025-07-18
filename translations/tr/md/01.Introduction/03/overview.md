<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-07-16T21:09:57+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "tr"
}
-->
Phi-3-mini bağlamında, çıkarım, modelin giriş verilerine dayanarak tahminler yapma veya çıktı üretme sürecini ifade eder. Phi-3-mini ve çıkarım yetenekleri hakkında size daha fazla bilgi vereyim.

Phi-3-mini, Microsoft tarafından yayımlanan Phi-3 serisi modellerin bir parçasıdır. Bu modeller, Küçük Dil Modelleri (SLM) ile mümkün olanı yeniden tanımlamak için tasarlanmıştır.

Phi-3-mini ve çıkarım yetenekleri hakkında bazı önemli noktalar şunlardır:

## **Phi-3-mini Genel Bakış:**
- Phi-3-mini 3.8 milyar parametre büyüklüğündedir.
- Sadece geleneksel bilgisayar cihazlarında değil, aynı zamanda mobil cihazlar ve IoT cihazları gibi uç cihazlarda da çalışabilir.
- Phi-3-mini’nin yayımlanması, bireylerin ve işletmelerin özellikle kaynak kısıtlı ortamlarda farklı donanım cihazlarında SLM’leri dağıtmasına olanak tanır.
- Geleneksel PyTorch formatı, gguf formatının kuantize edilmiş versiyonu ve ONNX tabanlı kuantize versiyon dahil olmak üzere çeşitli model formatlarını kapsar.

## **Phi-3-mini’ye Erişim:**
Phi-3-mini’ye erişmek için bir Copilot uygulamasında [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) kullanabilirsiniz. Semantic Kernel genellikle Azure OpenAI Service, Hugging Face üzerindeki açık kaynak modeller ve yerel modellerle uyumludur.  
Kuantize modelleri çağırmak için ayrıca [Ollama](https://ollama.com) veya [LlamaEdge](https://llamaedge.com) kullanabilirsiniz. Ollama bireysel kullanıcıların farklı kuantize modelleri çağırmasına olanak tanırken, LlamaEdge GGUF modelleri için platformlar arası erişim sağlar.

## **Kuantize Modeller:**
Birçok kullanıcı yerel çıkarım için kuantize modelleri tercih eder. Örneğin, Ollama ile doğrudan Phi-3 modelini çalıştırabilir veya Modelfile kullanarak çevrimdışı yapılandırabilirsiniz. Modelfile, GGUF dosya yolunu ve prompt formatını belirtir.

## **Üretken Yapay Zeka Olanakları:**
Phi-3-mini gibi SLM’lerin birleşimi, üretken yapay zeka için yeni olanaklar sunar. Çıkarım sadece ilk adımdır; bu modeller, kaynak kısıtlı, gecikme sınırlandırılmış ve maliyet kısıtlı senaryolarda çeşitli görevler için kullanılabilir.

## **Phi-3-mini ile Üretken Yapay Zekayı Açmak: Çıkarım ve Dağıtım Rehberi**  
Semantic Kernel, Ollama/LlamaEdge ve ONNX Runtime kullanarak Phi-3-mini modellerine erişmeyi ve çıkarım yapmayı öğrenin, ayrıca çeşitli uygulama senaryolarında üretken yapay zekanın olanaklarını keşfedin.

**Özellikler**  
Phi3-mini modelini çıkarım için kullanma:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)  

Özetle, Phi-3-mini geliştiricilerin farklı model formatlarını keşfetmesine ve çeşitli uygulama senaryolarında üretken yapay zekadan faydalanmasına olanak tanır.

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.