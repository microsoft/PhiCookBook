<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-05-09T21:47:26+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "tr"
}
-->
# Phi-3-Vision-128K-Instruct Proje Genel Bakışı

## Model

Phi-3-Vision-128K-Instruct, bu projenin merkezinde yer alan, hafif ve son teknoloji çok modlu bir modeldir. Phi-3 model ailesinin bir parçası olup, 128.000 token’a kadar bağlam uzunluğunu destekler. Model, sentetik veriler ve özenle filtrelenmiş halka açık web siteleri dahil olmak üzere çeşitli bir veri seti üzerinde eğitilmiştir; yüksek kaliteli, muhakeme gerektiren içeriklere özellikle önem verilmiştir. Eğitim süreci, talimatlara tam uyumu sağlamak için denetimli ince ayar ve doğrudan tercih optimizasyonunu içermekte olup, güçlü güvenlik önlemleriyle desteklenmiştir.

## Örnek veri oluşturmak birkaç açıdan çok önemlidir:

1. **Test Etme**: Örnek veriler, gerçek verileri etkilemeden uygulamanızı çeşitli senaryolarda test etmenizi sağlar. Bu, özellikle geliştirme ve test aşamalarında önemlidir.

2. **Performans Ayarı**: Gerçek verilerin ölçeğini ve karmaşıklığını taklit eden örnek verilerle, performans darboğazlarını tespit edip uygulamanızı buna göre optimize edebilirsiniz.

3. **Prototip Oluşturma**: Örnek veriler, kullanıcı gereksinimlerini anlamak ve geri bildirim almak için prototipler ve taslaklar oluşturmakta kullanılabilir.

4. **Veri Analizi**: Veri bilimi alanında, örnek veriler genellikle keşifsel veri analizi, model eğitimi ve algoritma testi için kullanılır.

5. **Güvenlik**: Geliştirme ve test ortamlarında örnek veri kullanmak, hassas gerçek verilerin yanlışlıkla sızmasını önlemeye yardımcı olur.

6. **Öğrenme**: Yeni bir teknoloji veya araç öğrenirken, örnek veriler üzerinde çalışmak öğrendiklerinizi uygulamak için pratik bir yol sağlar.

Unutmayın, örnek verinizin kalitesi bu faaliyetleri önemli ölçüde etkiler. Yapı ve çeşitlilik açısından gerçek verilere mümkün olduğunca yakın olmalıdır.

### Örnek Veri Oluşturma
[Generate DataSet Script](./CreatingSampleData.md)

## Veri Seti

İyi bir örnek veri seti olarak [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (Huggingface üzerinde mevcut) gösterilebilir.  
Burberry ürünlerinin örnek veri seti, ürün kategorisi, fiyatı ve başlığına dair meta verilerle birlikte toplamda 3.040 satır içerir ve her satır benzersiz bir ürünü temsil eder. Bu veri seti, modelin görsel veriyi anlama ve yorumlama yeteneğini test etmemize olanak sağlar; karmaşık görsel detayları ve marka özgü özellikleri yakalayan açıklayıcı metinler üretir.

**Note:** Görüntü içeren herhangi bir veri setini kullanabilirsiniz.

## Karmaşık Muhakeme

Modelin yalnızca görüntüye dayanarak fiyatlar ve isimlendirme üzerinde muhakeme yapması gerekir. Bu, modelin görsel özellikleri tanımasının yanı sıra, ürün değeri ve marka açısından bunların anlamlarını da kavramasını gerektirir. Görüntülerden doğru metinsel açıklamalar sentezleyerek, proje görsel verinin entegrasyonunun gerçek dünya uygulamalarında modellerin performansını ve çok yönlülüğünü artırmadaki potansiyelini vurgular.

## Phi-3 Vision Mimari

Model mimarisi, Phi-3’ün çok modlu bir versiyonudur. Hem metin hem de görüntü verilerini işler, bu girdileri kapsamlı anlama ve üretim görevleri için birleşik bir dizi halinde entegre eder. Model, metin ve görüntüler için ayrı gömme katmanları kullanır. Metin tokenları yoğun vektörlere dönüştürülürken, görüntüler özellik gömmeleri çıkarmak için bir CLIP vision modeli aracılığıyla işlenir. Bu görüntü gömmeleri daha sonra metin gömmelerinin boyutlarına projekte edilerek sorunsuz entegrasyon sağlanır.

## Metin ve Görüntü Gömme Entegrasyonu

Metin dizisi içindeki özel tokenlar, görüntü gömmelerinin nereye yerleştirileceğini gösterir. İşlem sırasında bu özel tokenlar ilgili görüntü gömmeleriyle değiştirilir ve modelin metin ve görüntüleri tek bir dizi olarak işlemesine olanak tanır. Veri setimiz için istek, özel <|image|> tokenı kullanılarak aşağıdaki şekilde formatlanmıştır:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Örnek Kod
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Example walkthrough](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucunda ortaya çıkabilecek herhangi bir yanlış anlama veya yanlış yorumdan sorumlu değiliz.