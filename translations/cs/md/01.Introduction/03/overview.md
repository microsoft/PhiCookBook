<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-05-09T12:31:57+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "cs"
}
-->
// Phi-3-mini bağlamında, çıkarım, modelin tahminler yapmak veya giriş verilerine dayanarak çıktılar üretmek için kullanılması sürecini ifade eder. Phi-3-mini ve çıkarım yetenekleri hakkında size daha fazla bilgi vereyim.

// Phi-3-mini, Microsoft tarafından yayınlanan Phi-3 serisi modellerin bir parçasıdır. Bu modeller, Küçük Dil Modelleri (SLM) ile mümkün olanı yeniden tanımlamak için tasarlanmıştır.

// İşte Phi-3-mini ve çıkarım yetenekleri hakkında bazı önemli noktalar:

// ## **Phi-3-mini Genel Bakış:**
// - Phi-3-mini 3,8 milyar parametre boyutuna sahiptir.
// - Sadece geleneksel bilgisayar cihazlarında değil, aynı zamanda mobil cihazlar ve IoT cihazları gibi uç cihazlarda da çalışabilir.
// - Phi-3-mini'nin yayınlanması, bireylerin ve işletmelerin özellikle kaynak kısıtlı ortamlarda farklı donanım cihazlarında SLM'leri dağıtmasına olanak tanır.
// - Geleneksel PyTorch formatı, gguf formatının kuantize edilmiş versiyonu ve ONNX tabanlı kuantize edilmiş versiyon dahil olmak üzere çeşitli model formatlarını kapsar.

// ## **Phi-3-mini'ye Erişim:**
// Phi-3-mini'ye erişmek için Copilot uygulamasında [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) kullanabilirsiniz. Semantic Kernel genel olarak Azure OpenAI Service, Hugging Face üzerindeki açık kaynak modeller ve yerel modellerle uyumludur.
// Ayrıca kuantize edilmiş modelleri çağırmak için [Ollama](https://ollama.com) veya [LlamaEdge](https://llamaedge.com) kullanabilirsiniz. Ollama bireysel kullanıcıların farklı kuantize modelleri çağırmasına izin verirken, LlamaEdge GGUF modelleri için çapraz platform erişimi sağlar.

// ## **Kuantize Modeller:**
// Birçok kullanıcı yerel çıkarım için kuantize modelleri tercih eder. Örneğin, Ollama ile Phi-3'ü doğrudan çalıştırabilir veya Modelfile kullanarak çevrimdışı yapılandırabilirsiniz. Modelfile, GGUF dosya yolunu ve istem formatını belirtir.

// ## **Üretken Yapay Zeka Olanakları:**
// Phi-3-mini gibi SLM'lerin birleştirilmesi, üretken yapay zeka için yeni olanaklar sunar. Çıkarım sadece ilk adımdır; bu modeller, kaynak kısıtlı, gecikme sınırlandırılmış ve maliyet kısıtlı senaryolarda çeşitli görevler için kullanılabilir.

// ## **Phi-3-mini ile Üretken Yapay Zekayı Açmak: Çıkarım ve Dağıtım Rehberi** 
// Semantic Kernel, Ollama/LlamaEdge ve ONNX Runtime kullanarak Phi-3-mini modellerine erişmeyi ve çıkarım yapmayı öğrenin, ayrıca çeşitli uygulama senaryolarında üretken yapay zekanın olanaklarını keşfedin.

// **Özellikler**
// Aşağıda phi3-mini modelinin çıkarımı desteklenir:

// - [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
// - [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
// - [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
// - [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
// - [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

// Özetle, Phi-3-mini geliştiricilere farklı model formatlarını keşfetme ve çeşitli uygulama senaryolarında üretken yapay zekayı kullanma imkanı sunar.

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo chybné výklady vzniklé použitím tohoto překladu.