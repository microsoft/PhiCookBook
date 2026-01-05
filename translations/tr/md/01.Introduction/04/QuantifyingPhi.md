<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f4cbbe7bf3e764de52d64a96d97b3c35",
  "translation_date": "2026-01-05T03:45:44+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "tr"
}
-->
# **Phi Ailesinin Kantizasyonu**

Model kantizasyonu, bir sinir ağı modelindeki parametrelerin (ağırlıklar ve aktivasyon değerleri gibi) geniş bir değer aralığından (genellikle sürekli bir değer aralığı) daha küçük bir sonlu değer aralığına eşlenmesi sürecine atıfta bulunur. Bu teknoloji, modelin boyutunu ve hesaplama karmaşıklığını azaltabilir ve mobil cihazlar veya gömülü sistemler gibi kaynak kısıtlı ortamlarda modelin çalışma verimliliğini artırabilir. Model kantizasyonu, parametrelerin hassasiyetini azaltarak sıkıştırma sağlar, ancak aynı zamanda belirli bir doğruluk kaybı da getirir. Bu nedenle, kantizasyon sürecinde model boyutu, hesaplama karmaşıklığı ve doğruluk arasında bir denge kurmak gerekir. Yaygın kantizasyon yöntemleri arasında sabit nokta kantizasyonu, kayan nokta kantizasyonu vb. bulunur. Belirli senaryo ve gereksinimlere göre uygun kantizasyon stratejisi seçilebilir.

GenAI modelini uç cihazlara dağıtmayı ve daha fazla cihazın GenAI senaryolarına girmesine izin vermeyi umuyoruz; örneğin mobil cihazlar, AI PC/Copilot+PC ve geleneksel IoT cihazları. Kantize edilmiş modeller aracılığıyla, farklı cihazlara göre farklı uç cihazlara dağıtım yapabiliriz. Donanım üreticilerinin sağladığı model hızlandırma çerçevesi ve kantize model ile birleştirildiğinde daha iyi SLM uygulama senaryoları oluşturabiliriz.

Kantizasyon senaryosunda farklı hassasiyetlerimiz vardır (INT4, INT8, FP16, FP32). Aşağıda yaygın olarak kullanılan kantizasyon hassasiyetlerinin açıklaması yer almaktadır

### **INT4**

INT4 kantizasyonu, modelin ağırlıklarını ve aktivasyon değerlerini 4 bitlik tamsayılara kantize eden radikal bir kantizasyon yöntemidir. INT4 kantizasyonu, daha küçük gösterim aralığı ve daha düşük hassasiyet nedeniyle genellikle daha büyük bir doğruluk kaybına yol açar. Ancak, INT8 kantizasyona kıyasla INT4 kantizasyonu, modelin depolama gereksinimlerini ve hesaplama karmaşıklığını daha da azaltabilir. INT4 kantizasyonunun pratik uygulamalarda nispeten nadir olduğunu, çünkü çok düşük doğruluğun model performansında önemli bozulmalara yol açabileceğini belirtmek gerekir. Ayrıca, tüm donanımlar INT4 işlemlerini desteklemediğinden, bir kantizasyon yöntemi seçilirken donanım uyumluluğunun dikkate alınması gerekir.

### **INT8**

INT8 kantizasyonu, bir modelin ağırlıklarını ve aktivasyonlarını kayan nokta sayılardan 8 bitlik tamsayılara dönüştürme sürecidir. INT8 tamsayılarının temsil ettiği sayısal aralık daha küçük ve daha az hassas olsa da, depolama ve hesaplama gereksinimlerini önemli ölçüde azaltabilir. INT8 kantizasyonunda, modelin ağırlıkları ve aktivasyon değerleri ölçekleme ve ofsset dahil olmak üzere bir kantizasyon işleminden geçirilir, böylece orijinal kayan nokta bilgisi mümkün olduğunca korunmaya çalışılır. Çıkarım sırasında bu kantize edilmiş değerler hesaplama için tekrar kayan nokta sayılarına de-kantize edilir ve ardından bir sonraki adım için tekrar INT8'e kantize edilir. Bu yöntem, çoğu uygulamada yüksek hesaplama verimliliğini korurken yeterli doğruluk sağlayabilir.

### **FP16**

FP16 formatı, yani 16 bitlik kayan nokta sayılar (float16), 32 bitlik kayan nokta sayılara (float32) kıyasla bellek kullanımını yarı yarıya azaltır ve bu durum büyük ölçekli derin öğrenme uygulamalarında önemli avantajlar sağlar. FP16 formatı, aynı GPU bellek sınırlamaları içinde daha büyük modellerin yüklenmesine veya daha fazla verinin işlenmesine olanak tanır. Modern GPU donanımları FP16 işlemlerini desteklemeye devam ettikçe, FP16 formatını kullanmak hesaplama hızında da iyileşmeler getirebilir. Ancak, FP16 formatının kendi dezavantajı olan daha düşük doğruluk vardır; bu da bazı durumlarda sayısal kararsızlığa veya doğruluk kaybına yol açabilir.

### **FP32**

FP32 formatı daha yüksek doğruluk sağlar ve geniş bir değer aralığını doğru bir şekilde temsil edebilir. Karmaşık matematiksel işlemlerin yapıldığı veya yüksek doğruluklu sonuçların gerektiği senaryolarda FP32 formatı tercih edilir. Ancak yüksek doğruluk daha fazla bellek kullanımı ve daha uzun hesaplama süresi anlamına gelir. Özellikle çok sayıda model parametresi ve büyük miktarda veri içeren büyük ölçekli derin öğrenme modelleri için FP32 formatı GPU belleğinin yetersiz kalmasına veya çıkarım hızının düşmesine neden olabilir.

Mobil cihazlarda veya IoT cihazlarında Phi-3.x modellerini INT4'e dönüştürebiliriz, AI PC / Copilot PC ise INT8, FP16, FP32 gibi daha yüksek hassasiyetleri kullanabilir.

Günümüzde farklı donanım üreticileri jeneratif modelleri desteklemek için farklı çerçevelere sahiptir; örneğin Intel'in OpenVINO'su, Qualcomm'un QNN'i, Apple'ın MLX'i ve Nvidia'nın CUDA'sı gibi. Bunlar model kantizasyonuyla birleştirilerek yerel dağıtım tamamlanabilir.

Teknoloji açısından kantizasyon sonrası farklı format desteğimiz vardır; örneğin PyTorch / TensorFlow formatı, GGUF ve ONNX. GGUF ve ONNX arasında bir format karşılaştırması ve uygulama senaryoları yaptım. Burada model çerçevesinden donanıma kadar iyi desteğe sahip olduğu için ONNX kantizasyon formatını öneriyorum. Bu bölümde, model kantizasyonu yapmak için GenAI için ONNX Runtime, OpenVINO ve Apple MLX üzerinde duracağız (eğer daha iyi bir yolunuz varsa, PR göndererek bize iletebilirsiniz)

**Bu bölümde yer alanlar**

1. [Quantizing Phi-3.5 / 4 using llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantizing Phi-3.5 / 4 using Generative AI extensions for onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantizing Phi-3.5 / 4 using Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantizing Phi-3.5 / 4 using Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Sorumluluk Reddi:**
Bu belge, yapay zeka çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk konusunda titiz olsak da, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilindeki hâliyle yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucunda ortaya çıkabilecek herhangi bir yanlış anlama veya yanlış yorumdan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->