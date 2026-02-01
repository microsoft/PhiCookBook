# **Phi Ailesini Nicelleştirme**

Model nicelleştirme, bir sinir ağı modelindeki parametrelerin (ağırlıklar ve aktivasyon değerleri gibi) genellikle sürekli bir değer aralığından daha küçük ve sonlu bir değer aralığına eşlenmesi işlemine denir. Bu teknoloji, modelin boyutunu ve hesaplama karmaşıklığını azaltabilir ve mobil cihazlar veya gömülü sistemler gibi kaynak kısıtlı ortamlarda modelin işletim verimliliğini artırabilir. Model nicelleştirme, parametrelerin hassasiyetini düşürerek sıkıştırma sağlar, ancak belli bir doğruluk kaybı da getirir. Bu nedenle, nicelleştirme sürecinde model boyutu, hesaplama karmaşıklığı ve doğruluk arasında denge kurulması gerekir. Yaygın nicelleştirme yöntemleri arasında sabit nokta nicelleştirme, kayan nokta nicelleştirme vb. bulunur. Spesifik senaryo ve ihtiyaçlara göre uygun nicelleştirme stratejisi seçebilirsiniz.

GenAI modelini uç cihazlara dağıtmayı ve mobil cihazlar, AI PC/Copilot+PC ve geleneksel IoT cihazları gibi daha fazla cihazın GenAI senaryolarına erişmesini sağlamayı hedefliyoruz. Nicelleştirme modeli sayesinde, cihazlara göre farklı uç cihazlara dağıtım yapabiliriz. Donanım üreticileri tarafından sağlanan model hızlandırma çerçevesi ve nicelleştirme modeli ile birleştiğinde, daha iyi SLM uygulama senaryaları oluşturabiliriz.

Nicelleştirme senaryosunda farklı hassasiyetlerimiz bulunmaktadır (INT4, INT8, FP16, FP32). Aşağıda yaygın kullanılan nicelleştirme hassasiyetlerinin açıklaması yer almaktadır.

### **INT4**

INT4 nicelleştirme, modelin ağırlıklarını ve aktivasyon değerlerini 4 bitlik tam sayılara nicelleştiren radikal bir yöntemdir. INT4 nicelleştirme, daha küçük temsil aralığı ve düşük hassasiyet nedeniyle genellikle daha büyük bir doğruluk kaybına neden olur. Ancak, INT8 nicelleştirmeye kıyasla, INT4 nicelleştirme modelin depolama gereksinimlerini ve hesaplama karmaşıklığını daha da azaltabilir. Pratik uygulamalarda INT4 nicelleştirmenin nispeten nadir olduğu unutulmamalıdır çünkü çok düşük doğruluk model performansında önemli bozulmalara yol açabilir. Ayrıca, tüm donanımlar INT4 işlemlerini desteklemediğinden, nicelleştirme yöntemi seçilirken donanım uyumluluğu dikkate alınmalıdır.

### **INT8**

INT8 nicelleştirme, modelin ağırlıklarını ve aktivasyonlarını kayar nokta sayılardan 8 bitlik tam sayılara dönüştürme işlemidir. INT8 tam sayılarının temsil ettiği sayısal aralık daha küçük ve daha az hassas olmasına rağmen, depolama ve hesaplama gereksinimlerini önemli ölçüde azaltabilir. INT8 nicelleştirmede, modelin ağırlık ve aktivasyon değerleri olabildiğince orijinal kayan nokta bilgisi korunacak şekilde ölçekleme ve ofset dahil nicelleştirme işleminden geçer. Çıkarım sırasında, bu nicelleştirilmiş değerler hesaplama için tekrar kayan noktalı sayılara dönüştürülür ve ardından bir sonraki adıma geçmek için tekrar INT8'e nicelleştirilir. Bu yöntem, çoğu uygulamada yüksek hesaplama verimliliği sağlarken yeterli doğruluk sunabilir.

### **FP16**

FP16 formatı, yani 16 bitlik kayan nokta sayılar (float16), 32 bitlik kayan noktalı sayılara (float32) kıyasla hafıza kullanımını yarı yarıya azaltır ve bu, büyük ölçekli derin öğrenme uygulamalarında önemli avantajlar sağlar. FP16 formatı, aynı GPU bellek kısıtlamaları içinde daha büyük modelleri yüklemeye veya daha fazla veri işlemeye olanak tanır. Modern GPU donanımı FP16 işlemlerini desteklemeye devam ettikçe, FP16 kullanımı hesaplama hızında da iyileştirmeler getirebilir. Ancak FP16 formatının düşük hassasiyet gibi doğuştan gelen dezavantajları vardır ve bazı durumlarda sayısal kararsızlık veya doğruluk kaybına yol açabilir.

### **FP32**

FP32 formatı daha yüksek doğruluk sağlar ve geniş bir değer aralığını doğru şekilde temsil edebilir. Karmaşık matematiksel işlemlerin yapıldığı veya yüksek doğruluk gerektiren senaryolarda FP32 formatı tercih edilir. Ancak yüksek doğruluk daha fazla bellek kullanımı ve daha uzun hesaplama süresi anlamına gelir. Özellikle birçok model parametresi ve büyük veri hacminin bulunduğu büyük ölçekli derin öğrenme modellerinde FP32 formatı GPU belleğinin yetmemesine veya çıkarım hızının düşmesine neden olabilir.

Mobil cihazlarda veya IoT cihazlarında Phi-3.x modelleri INT4'e dönüştürebilirken; AI PC / Copilot PC gibi platformlar daha yüksek doğruluklu INT8, FP16, FP32 kullanabilir.

Şu anda farklı donanım üreticileri, Intel OpenVINO, Qualcomm QNN, Apple MLX, Nvidia CUDA gibi farklı çerçevelerle üretken modelleri desteklemekte ve model nicelleştirme ile birleşerek yerel dağıtımı tamamlamaktadır.

Teknolojik açıdan, nicelleştirmeden sonra PyTorch / TensorFlow formatı, GGUF ve ONNX gibi farklı format desteğimiz vardır. GGUF ve ONNX arasında format karşılaştırması ve uygulama senaryoları yaptım. Burada model çerçevesinden donanıma iyi destek sunan ONNX nicelleştirme formatını önermekteyim. Bu bölümde, model nicelleştirmeyi gerçekleştirmek için ONNX Runtime for GenAI, OpenVINO ve Apple MLX üzerine odaklanacağız (daha iyi bir yönteminiz varsa PR göndererek bize iletebilirsiniz).

**Bu bölümde şunlar yer almaktadır**

1. [llama.cpp kullanarak Phi-3.5 / 4 nicelleştirme](./UsingLlamacppQuantifyingPhi.md)

2. [onnxruntime için Üretken AI uzantıları kullanarak Phi-3.5 / 4 nicelleştirme](./UsingORTGenAIQuantifyingPhi.md)

3. [Intel OpenVINO kullanarak Phi-3.5 / 4 nicelleştirme](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Apple MLX Çerçevesi kullanarak Phi-3.5 / 4 nicelleştirme](./UsingAppleMLXQuantifyingPhi.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf edilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilindeki haliyle yetkili kaynak olarak kabul edilmelidir. Önemli bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanılması sonucu oluşabilecek yanlış anlamalar veya yorum farklılıklarından sorumlu tutulamayız.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->