# **Android'de Phi-3 ile Çıkarım**

Phi-3-mini ile Android cihazlarda nasıl çıkarım yapabileceğinizi keşfedelim. Phi-3-mini, Microsoft'un kenar cihazlar ve IoT cihazlarında Büyük Dil Modelleri (LLM'ler) dağıtımını mümkün kılan yeni bir model serisidir.

## Semantic Kernel ve Çıkarım

[Semantic Kernel](https://github.com/microsoft/semantic-kernel), Azure OpenAI Service, OpenAI modelleri ve hatta yerel modellerle uyumlu uygulamalar oluşturmanızı sağlayan bir uygulama çerçevesidir. Semantic Kernel'e yeniyseniz, [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) sayfasına göz atmanızı öneririz.

### Semantic Kernel ile Phi-3-mini'ye Erişim

Bunu Semantic Kernel'deki Hugging Face Connector ile birleştirebilirsiniz. Bu [Örnek Koda](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo) bakabilirsiniz.

Varsayılan olarak, Hugging Face üzerindeki model kimliği ile uyumludur. Ancak, yerel olarak oluşturulmuş bir Phi-3-mini model sunucusuna da bağlanabilirsiniz.

### Ollama veya LlamaEdge ile Kuantize Modelleri Çağırma

Birçok kullanıcı, modelleri yerel olarak çalıştırmak için kuantize modelleri tercih ediyor. [Ollama](https://ollama.com/) ve [LlamaEdge](https://llamaedge.com), bireysel kullanıcıların farklı kuantize modelleri çağırmasına olanak tanır:

#### Ollama

`ollama run Phi-3` komutunu doğrudan çalıştırabilir veya `.gguf` dosyanızın yolunu içeren bir `Modelfile` oluşturarak çevrimdışı yapılandırabilirsiniz.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Örnek Kod](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Bulutta ve kenar cihazlarda aynı anda `.gguf` dosyalarını kullanmak istiyorsanız, LlamaEdge harika bir seçenektir. Başlamak için bu [örnek koda](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) bakabilirsiniz.

### Android Telefonlara Kurulum ve Çalıştırma

1. Android telefonlar için **MLC Chat uygulamasını** (Ücretsiz) indirin.  
2. APK dosyasını (148MB) indirip cihazınıza kurun.  
3. MLC Chat uygulamasını başlatın. Phi-3-mini dahil AI modellerinin bir listesini göreceksiniz.

Özetle, Phi-3-mini, kenar cihazlarda üretken yapay zeka için heyecan verici olanaklar sunuyor ve Android üzerinde yeteneklerini keşfetmeye başlayabilirsiniz.

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.