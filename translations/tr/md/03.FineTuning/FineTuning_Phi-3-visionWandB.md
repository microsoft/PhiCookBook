<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-07-17T08:09:56+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "tr"
}
-->
# Phi-3-Vision-128K-Instruct Proje Genel Bakışı

## Model

Phi-3-Vision-128K-Instruct, hafif ve son teknoloji çok modlu bir model olup bu projenin merkezinde yer almaktadır. Phi-3 model ailesinin bir parçasıdır ve 128.000 token’a kadar bağlam uzunluğunu destekler. Model, sentetik veriler ve özenle filtrelenmiş halka açık web siteleri dahil olmak üzere çeşitli bir veri seti üzerinde eğitilmiştir; burada yüksek kaliteli ve muhakeme gerektiren içeriklere özellikle önem verilmiştir. Eğitim süreci, talimatlara tam uyumu sağlamak için denetimli ince ayar ve doğrudan tercih optimizasyonunu içerirken, aynı zamanda güçlü güvenlik önlemleri de uygulanmıştır.

## Örnek veri oluşturmanın birkaç önemli nedeni vardır:

1. **Test Etme**: Örnek veriler, gerçek verileri etkilemeden uygulamanızı farklı senaryolar altında test etmenizi sağlar. Bu, özellikle geliştirme ve hazırlık aşamalarında önemlidir.

2. **Performans Ayarı**: Gerçek verilerin ölçeğini ve karmaşıklığını taklit eden örnek verilerle, performans darboğazlarını tespit edebilir ve uygulamanızı buna göre optimize edebilirsiniz.

3. **Prototip Oluşturma**: Örnek veriler, kullanıcı gereksinimlerini anlamaya ve geri bildirim almaya yardımcı olan prototipler ve taslaklar oluşturmak için kullanılabilir.

4. **Veri Analizi**: Veri bilimi alanında, örnek veriler keşifsel veri analizi, model eğitimi ve algoritma testleri için sıklıkla kullanılır.

5. **Güvenlik**: Geliştirme ve test ortamlarında örnek veri kullanmak, hassas gerçek verilerin kazara sızdırılmasını önlemeye yardımcı olabilir.

6. **Öğrenme**: Yeni bir teknoloji veya araç öğrenirken, örnek verilerle çalışmak öğrendiklerinizi pratikte uygulamanın etkili bir yoludur.

Unutmayın, örnek verinizin kalitesi bu faaliyetleri önemli ölçüde etkiler. Yapı ve çeşitlilik açısından gerçek veriye mümkün olduğunca yakın olmalıdır.

### Örnek Veri Oluşturma
[Generate DataSet Script](./CreatingSampleData.md)

## Veri Seti

İyi bir örnek veri seti, [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (Huggingface üzerinde mevcuttur) olabilir.  
Burberry ürünlerine ait örnek veri seti, ürün kategorisi, fiyat ve başlık gibi meta verilerle birlikte toplam 3.040 satırdan oluşur ve her satır benzersiz bir ürünü temsil eder. Bu veri seti, modelin görsel veriyi anlama ve yorumlama yeteneğini test etmemize olanak tanır; karmaşık görsel detayları ve marka özgü özellikleri yakalayan açıklayıcı metinler üretir.

**Not:** Görüntü içeren herhangi bir veri setini kullanabilirsiniz.

## Karmaşık Muhakeme

Model, yalnızca görüntüye dayanarak fiyatlar ve isimlendirme hakkında muhakeme yapmalıdır. Bu, modelin sadece görsel özellikleri tanıması değil, aynı zamanda bunların ürün değeri ve markalaşma açısından ne anlama geldiğini anlamasını gerektirir. Görüntülerden doğru metinsel açıklamalar sentezleyerek, proje görsel verinin entegrasyonunun gerçek dünya uygulamalarında modellerin performansını ve çok yönlülüğünü artırmadaki potansiyelini vurgulamaktadır.

## Phi-3 Vision Mimarisi

Model mimarisi, Phi-3’ün çok modlu bir versiyonudur. Hem metin hem de görüntü verilerini işler ve bu girdileri kapsamlı anlama ve üretim görevleri için birleşik bir diziye entegre eder. Model, metin ve görüntüler için ayrı gömme katmanları kullanır. Metin tokenları yoğun vektörlere dönüştürülürken, görüntüler özellik gömmeleri çıkarmak için bir CLIP vision modeli aracılığıyla işlenir. Bu görüntü gömmeleri, metin gömmelerinin boyutlarıyla uyumlu olacak şekilde projekte edilir ve böylece sorunsuz entegrasyon sağlanır.

## Metin ve Görüntü Gömme Entegrasyonu

Metin dizisi içindeki özel tokenlar, görüntü gömmelerinin nereye yerleştirileceğini belirtir. İşlem sırasında bu özel tokenlar, karşılık gelen görüntü gömmeleriyle değiştirilir ve modelin metin ve görüntüleri tek bir dizi olarak işlemesine olanak tanır. Veri setimiz için prompt, özel <|image|> tokenı kullanılarak şu şekilde biçimlendirilmiştir:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Örnek Kod
- [Phi-3-Vision Eğitim Scripti](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Örnek İnceleme](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.