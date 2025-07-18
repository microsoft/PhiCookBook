<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-07-16T22:09:07+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "tr"
}
-->
# **llama.cpp kullanarak Phi Ailesini Kuantize Etme**

## **llama.cpp Nedir**

llama.cpp, öncelikle C++ ile yazılmış açık kaynaklı bir yazılım kütüphanesidir ve Llama gibi çeşitli Büyük Dil Modelleri (LLM) üzerinde çıkarım yapar. Temel amacı, çok çeşitli donanımlarda minimum kurulumla LLM çıkarımı için en son performansı sağlamaktır. Ayrıca, bu kütüphane için Python bağlayıcıları da mevcuttur; bunlar metin tamamlama için yüksek seviyeli bir API ve OpenAI uyumlu bir web sunucusu sunar.

llama.cpp'nin ana hedefi, yerel veya bulut ortamında çok çeşitli donanımlarda minimum kurulumla ve en son performansla LLM çıkarımı yapabilmektir.

- Herhangi bir bağımlılık olmadan saf C/C++ uygulaması
- Apple silicon tam destekli - ARM NEON, Accelerate ve Metal çerçeveleri ile optimize edilmiş
- x86 mimarileri için AVX, AVX2 ve AVX512 desteği
- Daha hızlı çıkarım ve azaltılmış bellek kullanımı için 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit ve 8-bit tamsayı kuantizasyonu
- NVIDIA GPU’larda LLM çalıştırmak için özel CUDA çekirdekleri (AMD GPU desteği HIP ile)
- Vulkan ve SYCL arka uç desteği
- Toplam VRAM kapasitesinden büyük modelleri kısmen hızlandırmak için CPU+GPU hibrit çıkarımı

## **llama.cpp ile Phi-3.5 Kuantizasyonu**

Phi-3.5-Instruct modeli llama.cpp kullanılarak kuantize edilebilir, ancak Phi-3.5-Vision ve Phi-3.5-MoE henüz desteklenmemektedir. llama.cpp tarafından dönüştürülen format gguf’dur ve bu aynı zamanda en yaygın kullanılan kuantizasyon formatıdır.

Hugging Face üzerinde çok sayıda kuantize edilmiş GGUF formatında model bulunmaktadır. AI Foundry, Ollama ve LlamaEdge llama.cpp’ye dayandığı için GGUF modelleri de sıkça kullanılmaktadır.

### **GGUF Nedir**

GGUF, modellerin hızlı yüklenip kaydedilmesi için optimize edilmiş ikili bir formattır ve çıkarım amaçları için oldukça verimlidir. GGUF, GGML ve diğer yürütücülerle kullanım için tasarlanmıştır. GGUF, llama.cpp’nin geliştiricisi @ggerganov tarafından geliştirilmiştir; llama.cpp popüler bir C/C++ LLM çıkarım çerçevesidir. PyTorch gibi çerçevelerde geliştirilen modeller, bu motorlarla kullanmak üzere GGUF formatına dönüştürülebilir.

### **ONNX ve GGUF Karşılaştırması**

ONNX, farklı AI çerçevelerinde iyi desteklenen ve uç cihazlarda kullanım için uygun geleneksel bir makine öğrenimi/derin öğrenme formatıdır. GGUF ise llama.cpp tabanlıdır ve GenAI çağında üretilmiş sayılabilir. İkisi benzer kullanım alanlarına sahiptir. Gömülü donanım ve uygulama katmanlarında daha iyi performans istiyorsanız ONNX tercih edilebilir. llama.cpp’nin türetilmiş çerçevesi ve teknolojisini kullanıyorsanız GGUF daha uygun olabilir.

### **llama.cpp ile Phi-3.5-Instruct Kuantizasyonu**

**1. Ortam Yapılandırması**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Kuantizasyon**

llama.cpp kullanarak Phi-3.5-Instruct modelini FP16 GGUF formatına dönüştürme


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Phi-3.5 modelini INT4 formatına kuantize etme


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Test Etme**

llama-cpp-python paketini yükleyin


```bash

pip install llama-cpp-python -U

```

***Not*** 

Apple Silicon kullanıyorsanız, llama-cpp-python paketini şu şekilde yükleyin


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Test Etme 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Kaynaklar**

1. llama.cpp hakkında daha fazla bilgi için [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
2. onnxruntime hakkında daha fazla bilgi için [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)
3. GGUF hakkında daha fazla bilgi için [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yorumlamalardan sorumlu değiliz.