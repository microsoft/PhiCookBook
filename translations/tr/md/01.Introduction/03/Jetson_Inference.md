# **Nvidia Jetson'da Phi-3 Çıkarımı**

Nvidia Jetson, Nvidia tarafından geliştirilen gömülü bilgisayar kartları serisidir. Jetson TK1, TX1 ve TX2 modelleri, ARM mimarisine sahip bir merkezi işlem birimini (CPU) entegre eden Nvidia Tegra işlemcisi (veya SoC) taşır. Jetson, düşük güç tüketimli bir sistemdir ve makine öğrenimi uygulamalarını hızlandırmak için tasarlanmıştır. Nvidia Jetson, profesyonel geliştiriciler tarafından tüm sektörlerde çığır açan yapay zeka ürünleri oluşturmak için, öğrenciler ve meraklılar tarafından ise uygulamalı yapay zeka öğrenimi ve harika projeler yapmak için kullanılır. SLM, Jetson gibi uç cihazlarda konuşlandırılır ve endüstriyel üretken yapay zeka uygulama senaryolarının daha iyi uygulanmasını sağlar.

## NVIDIA Jetson Üzerinde Dağıtım:
Otonom robotik ve gömülü cihazlar üzerinde çalışan geliştiriciler Phi-3 Mini’den faydalanabilir. Phi-3’ün nispeten küçük boyutu, onu uç dağıtımlar için ideal kılar. Parametreler eğitim sırasında titizlikle ayarlanmış olup, yanıtların yüksek doğrulukta olmasını sağlar.

### TensorRT-LLM Optimizasyonu:
NVIDIA’nın [TensorRT-LLM kütüphanesi](https://github.com/NVIDIA/TensorRT-LLM?WT.mc_id=aiml-138114-kinfeylo), büyük dil modeli çıkarımını optimize eder. Phi-3 Mini’nin uzun bağlam penceresini destekleyerek hem verimliliği hem de gecikmeyi iyileştirir. Optimizasyonlar arasında LongRoPE, FP8 ve uçuşta toplu işleme gibi teknikler bulunur.

### Kullanılabilirlik ve Dağıtım:
Geliştiriciler, 128K bağlam penceresine sahip Phi-3 Mini’yi [NVIDIA AI](https://www.nvidia.com/en-us/ai-data-science/generative-ai/) üzerinden keşfedebilir. Bu, standart API’ye sahip bir mikroservis olan NVIDIA NIM olarak paketlenmiştir ve her yerde dağıtılabilir. Ayrıca, [TensorRT-LLM uygulamaları GitHub’da](https://github.com/NVIDIA/TensorRT-LLM) mevcuttur.

## **1. Hazırlık**

a. Jetson Orin NX / Jetson NX

b. JetPack 5.1.2+

c. Cuda 11.8

d. Python 3.8+

## **2. Jetson’da Phi-3’ü Çalıştırma**

[Ollama](https://ollama.com) veya [LlamaEdge](https://llamaedge.com) tercih edilebilir.

Bulut ve uç cihazlarda aynı anda gguf kullanmak istiyorsanız, LlamaEdge, WasmEdge olarak düşünülebilir (WasmEdge, bulut yerel, uç ve merkezi olmayan uygulamalar için uygun, hafif, yüksek performanslı ve ölçeklenebilir bir WebAssembly çalışma zamanı ortamıdır. Sunucusuz uygulamaları, gömülü fonksiyonları, mikroservisleri, akıllı sözleşmeleri ve IoT cihazlarını destekler). gguf’nun nicel modelini LlamaEdge aracılığıyla uç cihazlara ve buluta dağıtabilirsiniz.

![llamaedge](../../../../../translated_images/tr/llamaedge.e9d6ff96dff11cf7.webp)

Kullanım adımları:

1. İlgili kütüphaneleri ve dosyaları indirip kurun

```bash

curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | bash -s -- --plugin wasi_nn-ggml

curl -LO https://github.com/LlamaEdge/LlamaEdge/releases/latest/download/llama-api-server.wasm

curl -LO https://github.com/LlamaEdge/chatbot-ui/releases/latest/download/chatbot-ui.tar.gz

tar xzf chatbot-ui.tar.gz

```

**Not**: llama-api-server.wasm ve chatbot-ui aynı dizinde olmalıdır

2. Terminalde scriptleri çalıştırın

```bash

wasmedge --dir .:. --nn-preload default:GGML:AUTO:{Your gguf path} llama-api-server.wasm -p phi-3-chat

```

Çalıştırma sonucu aşağıdaki gibidir

![llamaedgerun](../../../../../translated_images/tr/llamaedgerun.bed921516c9a821c.webp)

***Örnek kod*** [Phi-3 mini WASM Notebook Örneği](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm)

Özetle, Phi-3 Mini, verimlilik, bağlam farkındalığı ve NVIDIA’nın optimizasyon gücünü bir araya getirerek dil modellemede önemli bir ilerleme sunar. İster robotlar ister uç uygulamalar geliştiriyor olun, Phi-3 Mini güçlü bir araç olarak dikkate değerdir.

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.