<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-05-09T14:09:41+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "tr"
}
-->
# **llama.cpp kullanarak Phi Ailesini Kantitatif Hale Getirme**

## **llama.cpp Nedir**

llama.cpp, başta Llama olmak üzere çeşitli Büyük Dil Modelleri (LLM) üzerinde çıkarım yapan, esasen C++ ile yazılmış açık kaynaklı bir yazılım kütüphanesidir. Temel amacı, minimal kurulumla geniş bir donanım yelpazesinde LLM çıkarımı için son teknoloji performans sunmaktır. Ayrıca, bu kütüphane için metin tamamlama için yüksek seviyeli API ve OpenAI uyumlu bir web sunucusu sağlayan Python bağlayıcıları mevcuttur.

llama.cpp'nin temel hedefi, yerel ve bulutta olmak üzere çok çeşitli donanımlarda minimal kurulumla ve son teknoloji performansla LLM çıkarımını mümkün kılmaktır.

- Herhangi bir bağımlılık olmadan sade C/C++ uygulaması
- Apple silikon tam destekli - ARM NEON, Accelerate ve Metal framework’leri ile optimize edilmiş
- x86 mimarileri için AVX, AVX2 ve AVX512 desteği
- Daha hızlı çıkarım ve azaltılmış bellek kullanımı için 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit ve 8-bit tamsayı kantitatifleştirme
- NVIDIA GPU’larda LLM çalıştırmak için özel CUDA çekirdekleri (AMD GPU desteği HIP üzerinden)
- Vulkan ve SYCL arka uç desteği
- Toplam VRAM kapasitesinden büyük modelleri kısmen hızlandırmak için CPU+GPU hibrit çıkarımı

## **llama.cpp ile Phi-3.5 Kantitatif Hale Getirme**

Phi-3.5-Instruct modeli llama.cpp kullanılarak kantitatif hale getirilebilir, ancak Phi-3.5-Vision ve Phi-3.5-MoE henüz desteklenmemektedir. llama.cpp tarafından dönüştürülen format gguf’tur ve bu aynı zamanda en yaygın kullanılan kantitatif formattır.

Hugging Face üzerinde çok sayıda kantitatif GGUF formatında model bulunmaktadır. AI Foundry, Ollama ve LlamaEdge llama.cpp’ye dayandığı için GGUF modelleri de sıkça kullanılmaktadır.

### **GGUF Nedir**

GGUF, modellerin hızlı yüklenmesi ve kaydedilmesi için optimize edilmiş ikili bir formattır ve çıkarım için yüksek verimlilik sağlar. GGUF, GGML ve diğer yürütücülerle kullanım için tasarlanmıştır. GGUF, popüler C/C++ LLM çıkarım çerçevesi llama.cpp’nin geliştiricisi @ggerganov tarafından geliştirilmiştir. PyTorch gibi çerçevelerde ilk geliştirilen modeller, bu motorlarda kullanmak üzere GGUF formatına dönüştürülebilir.

### **ONNX ve GGUF Karşılaştırması**

ONNX, farklı AI Çerçevelerinde iyi desteklenen ve uç cihazlarda kullanım için uygun geleneksel bir makine öğrenimi/derin öğrenme formatıdır. GGUF ise llama.cpp’ye dayanmaktadır ve GenAI döneminde üretilmiş sayılabilir. İkisi benzer amaçlarla kullanılır. Gömülü donanım ve uygulama katmanlarında daha iyi performans istiyorsanız ONNX tercih edilebilir. llama.cpp türev çerçevesi ve teknolojisini kullanıyorsanız GGUF daha uygun olabilir.

### **llama.cpp kullanarak Phi-3.5-Instruct Kantitatif Hale Getirme**

**1. Ortam Yapılandırması**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Kantitatif Hale Getirme**

llama.cpp kullanarak Phi-3.5-Instruct’ı FP16 GGUF’ye dönüştürme


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Phi-3.5’i INT4 olarak kantitatif hale getirme


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Test Etme**

llama-cpp-python kurun


```bash

pip install llama-cpp-python -U

```

***Not*** 

Apple Silicon kullanıyorsanız, llama-cpp-python’ı şu şekilde kurun


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Test Etme 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Kaynaklar**

1. llama.cpp hakkında daha fazla bilgi edinin [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)  
2. onnxruntime hakkında daha fazla bilgi edinin [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)  
3. GGUF hakkında daha fazla bilgi edinin [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.