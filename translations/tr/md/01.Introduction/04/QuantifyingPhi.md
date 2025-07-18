<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-07-16T21:46:25+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "tr"
}
-->
# **Phi Ailesini Nicelleştirme**

Model nicelleştirme, bir sinir ağı modelindeki parametrelerin (ağırlıklar ve aktivasyon değerleri gibi) geniş bir değer aralığından (genellikle sürekli bir değer aralığı) daha küçük ve sonlu bir değer aralığına dönüştürülmesi sürecidir. Bu teknoloji, modelin boyutunu ve hesaplama karmaşıklığını azaltabilir ve mobil cihazlar veya gömülü sistemler gibi kaynak kısıtlı ortamlarda modelin çalışma verimliliğini artırabilir. Model nicelleştirme, parametrelerin hassasiyetini düşürerek sıkıştırma sağlar, ancak bu aynı zamanda belirli bir hassasiyet kaybına da yol açar. Bu nedenle, nicelleştirme sürecinde model boyutu, hesaplama karmaşıklığı ve hassasiyet arasında bir denge kurulması gerekir. Yaygın nicelleştirme yöntemleri arasında sabit nokta nicelleştirme, kayan nokta nicelleştirme vb. bulunur. Spesifik senaryo ve ihtiyaçlara göre uygun nicelleştirme stratejisi seçilebilir.

GenAI modelini uç cihazlara dağıtmayı ve daha fazla cihazın GenAI senaryolarına girmesini sağlamayı hedefliyoruz; örneğin mobil cihazlar, AI PC/Copilot+PC ve geleneksel IoT cihazları gibi. Nicelleştirilmiş model sayesinde, farklı cihazlara göre farklı uç cihazlara dağıtım yapabiliriz. Donanım üreticilerinin sağladığı model hızlandırma çerçevesi ve nicelleştirme modeli ile birleştirildiğinde, daha iyi SLM uygulama senaryaları oluşturabiliriz.

Nicelleştirme senaryosunda farklı hassasiyetlerimiz vardır (INT4, INT8, FP16, FP32). Aşağıda yaygın kullanılan nicelleştirme hassasiyetlerinin açıklaması yer almaktadır.

### **INT4**

INT4 nicelleştirme, modelin ağırlıklarını ve aktivasyon değerlerini 4 bitlik tamsayılara dönüştüren radikal bir nicelleştirme yöntemidir. INT4 nicelleştirme, daha küçük temsil aralığı ve düşük hassasiyet nedeniyle genellikle daha büyük bir hassasiyet kaybına yol açar. Ancak, INT8 nicelleştirmeye kıyasla, INT4 nicelleştirme modelin depolama gereksinimlerini ve hesaplama karmaşıklığını daha da azaltabilir. INT4 nicelleştirmenin pratik uygulamalarda nispeten nadir olduğunu belirtmek gerekir, çünkü çok düşük doğruluk model performansında ciddi düşüşlere neden olabilir. Ayrıca, tüm donanımlar INT4 işlemlerini desteklemediğinden, nicelleştirme yöntemi seçilirken donanım uyumluluğu göz önünde bulundurulmalıdır.

### **INT8**

INT8 nicelleştirme, bir modelin ağırlıklarını ve aktivasyonlarını kayan noktalı sayılardan 8 bitlik tamsayılara dönüştürme sürecidir. INT8 tamsayılarının temsil ettiği sayısal aralık daha küçük ve daha az hassas olsa da, depolama ve hesaplama gereksinimlerini önemli ölçüde azaltabilir. INT8 nicelleştirmede, modelin ağırlıkları ve aktivasyon değerleri ölçeklendirme ve ofset işlemleri dahil olmak üzere bir nicelleştirme sürecinden geçer; böylece orijinal kayan nokta bilgisi mümkün olduğunca korunur. Çıkarım sırasında, bu nicelleştirilmiş değerler hesaplama için tekrar kayan noktalı sayılara dönüştürülür ve ardından bir sonraki adım için tekrar INT8’e nicelleştirilir. Bu yöntem, çoğu uygulamada yeterli doğruluk sağlarken yüksek hesaplama verimliliği sunar.

### **FP16**

FP16 formatı, yani 16 bitlik kayan nokta sayılar (float16), 32 bitlik kayan nokta sayılara (float32) kıyasla bellek kullanımını yarı yarıya azaltır ve bu, büyük ölçekli derin öğrenme uygulamalarında önemli avantajlar sağlar. FP16 formatı, aynı GPU bellek sınırları içinde daha büyük modellerin yüklenmesine veya daha fazla verinin işlenmesine olanak tanır. Modern GPU donanımları FP16 işlemlerini desteklemeye devam ettikçe, FP16 formatının kullanımı hesaplama hızında da iyileşmeler getirebilir. Ancak, FP16 formatının düşük hassasiyet gibi doğuştan gelen dezavantajları vardır; bu da bazı durumlarda sayısal kararsızlığa veya hassasiyet kaybına yol açabilir.

### **FP32**

FP32 formatı daha yüksek hassasiyet sağlar ve geniş bir değer aralığını doğru şekilde temsil edebilir. Karmaşık matematiksel işlemlerin yapıldığı veya yüksek hassasiyetli sonuçların gerektiği senaryolarda FP32 formatı tercih edilir. Ancak yüksek doğruluk, daha fazla bellek kullanımı ve daha uzun hesaplama süresi anlamına gelir. Özellikle çok sayıda model parametresi ve büyük veri setleri içeren büyük ölçekli derin öğrenme modellerinde, FP32 formatı GPU belleğinin yetersiz kalmasına veya çıkarım hızının düşmesine neden olabilir.

Mobil cihazlarda veya IoT cihazlarında Phi-3.x modellerini INT4’e dönüştürebiliriz; AI PC / Copilot PC ise INT8, FP16, FP32 gibi daha yüksek hassasiyetleri kullanabilir.

Şu anda farklı donanım üreticileri, Intel’in OpenVINO’su, Qualcomm’un QNN’si, Apple’ın MLX’i ve Nvidia’nın CUDA’sı gibi generatif modelleri destekleyen farklı çerçevelere sahiptir ve bunlar model nicelleştirme ile birleşerek yerel dağıtımı tamamlar.

Teknoloji açısından, nicelleştirme sonrası PyTorch / Tensorflow formatı, GGUF ve ONNX gibi farklı format desteklerimiz vardır. GGUF ve ONNX arasında format karşılaştırması ve uygulama senaryoları yaptım. Burada, model çerçevesinden donanıma kadar iyi destek sunan ONNX nicelleştirme formatını öneriyorum. Bu bölümde, GenAI için ONNX Runtime, OpenVINO ve Apple MLX kullanarak model nicelleştirmeye odaklanacağız (daha iyi bir yönteminiz varsa, PR göndererek bize iletebilirsiniz).

**Bu bölümde şunlar yer almaktadır**

1. [llama.cpp kullanarak Phi-3.5 / 4 nicelleştirme](./UsingLlamacppQuantifyingPhi.md)

2. [onnxruntime için Generative AI eklentileri kullanarak Phi-3.5 / 4 nicelleştirme](./UsingORTGenAIQuantifyingPhi.md)

3. [Intel OpenVINO kullanarak Phi-3.5 / 4 nicelleştirme](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Apple MLX Çerçevesi kullanarak Phi-3.5 / 4 nicelleştirme](./UsingAppleMLXQuantifyingPhi.md)

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.