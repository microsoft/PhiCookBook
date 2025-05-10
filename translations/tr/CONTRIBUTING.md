<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f71f15fee9a73ecfcd4fd40efbe3070",
  "translation_date": "2025-05-09T03:39:29+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "tr"
}
-->
# Katkıda Bulunma

Bu proje katkıları ve önerileri memnuniyetle karşılar. Çoğu katkı için, katkınızı kullanma hakkını size ait olduğunu ve gerçekten bize verdiğinizi belirten bir Katkıda Bulunma Lisans Sözleşmesi'ni (CLA) kabul etmeniz gerekir. Detaylar için [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com) adresini ziyaret edin.

Bir pull request gönderdiğinizde, bir CLA botu otomatik olarak CLA sağlamanız gerekip gerekmediğini belirleyecek ve PR'ı uygun şekilde işaretleyecektir (örneğin, durum kontrolü, yorum). Botun verdiği talimatları izleyin. CLA'yı kullanan tüm depolar için bunu yalnızca bir kez yapmanız yeterlidir.

## Davranış Kuralları

Bu proje [Microsoft Açık Kaynak Davranış Kuralları](https://opensource.microsoft.com/codeofconduct/)nu benimsemiştir. Daha fazla bilgi için [Davranış Kuralları SSS](https://opensource.microsoft.com/codeofconduct/faq/) sayfasını okuyabilir veya ek sorularınız ya da yorumlarınız için [opencode@microsoft.com](mailto:opencode@microsoft.com) adresiyle iletişime geçebilirsiniz.

## Sorun Oluştururken Dikkat Edilmesi Gerekenler

Lütfen genel destek soruları için GitHub sorunları açmayın, çünkü GitHub listesi özellik istekleri ve hata bildirimleri için kullanılmalıdır. Böylece gerçek kodla ilgili sorunları veya hataları daha kolay takip edebilir ve genel tartışmayı koddan ayrı tutabiliriz.

## Katkıda Bulunma Yöntemi

### Pull Request Kuralları

Phi-3 CookBook deposuna bir pull request (PR) gönderirken lütfen aşağıdaki kurallara uyun:

- **Depoyu Forklayın**: Değişiklik yapmadan önce her zaman depoyu kendi hesabınıza forklayın.

- **Ayrı pull requestler (PR)**:
  - Her değişiklik türünü ayrı bir pull request olarak gönderin. Örneğin, hata düzeltmeleri ve dokümantasyon güncellemeleri ayrı PR'lar olmalıdır.
  - Yazım hatası düzeltmeleri ve küçük dokümantasyon güncellemeleri uygun olduğunda tek bir PR'da birleştirilebilir.

- **Birleştirme çatışmalarını çözün**: Pull request'inizde birleştirme çatışmaları varsa, değişiklik yapmadan önce yerel `main` dalınızı ana depoyla eşitleyin.

- **Çeviri gönderimleri**: Çeviri PR'sı gönderirken, çeviri klasörünün orijinal klasördeki tüm dosyaların çevirilerini içerdiğinden emin olun.

### Çeviri Kuralları

> [!IMPORTANT]
>
> Bu depoda metin çevirisi yaparken makine çevirisi kullanmayın. Sadece iyi bildiğiniz dillerde gönüllü olarak çeviri yapın.

İngilizce dışındaki bir dilde yetkin iseniz, içeriğin çevirisine yardımcı olabilirsiniz. Çeviri katkılarınızın doğru şekilde entegre edilmesi için aşağıdaki kurallara uyun:

- **Çeviri klasörü oluşturun**: İlgili bölüm klasörüne gidin ve katkıda bulunduğunuz dil için bir çeviri klasörü oluşturun. Örneğin:
  - Giriş bölümü için: `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - Hızlı başlangıç bölümü için: `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Diğer bölümler (03.Inference, 04.Finetuning vb.) için aynı deseni takip edin.

- **Göreli yolları güncelleyin**: Çeviri yaparken, markdown dosyalarındaki göreli yolların başına `../../` ekleyerek klasör yapısını ayarlayın ki bağlantılar doğru çalışsın. Örneğin, şu şekilde değiştirin:
  - `(../../imgs/01/phi3aisafety.png)` yerine `(../../../../imgs/01/phi3aisafety.png)`

- **Çevirilerinizi düzenleyin**: Her çevrilmiş dosya, karşılık geldiği bölümün çeviri klasörüne yerleştirilmelidir. Örneğin, giriş bölümünü İspanyolcaya çeviriyorsanız, şu şekilde oluşturmalısınız:
  - `PhiCookBook/md/01.Introduce/translations/es/`

- **Tam bir PR gönderin**: Bir bölüm için tüm çevrilmiş dosyaların tek bir PR içinde olduğundan emin olun. Bölümün kısmi çevirilerini kabul etmiyoruz. Çeviri PR'sı gönderirken, çeviri klasörünün orijinal klasördeki tüm dosyaların çevirilerini içerdiğinden emin olun.

### Yazım Kuralları

Tüm belgelerde tutarlılığı sağlamak için lütfen aşağıdaki kuralları kullanın:

- **URL formatı**: Tüm URL'leri köşeli parantez içine alın ve ardından parantezle kapatın, aralarında veya içinde ekstra boşluk bırakmayın. Örneğin: `[example](https://www.microsoft.com)`.

- **Göreli bağlantılar**: Mevcut dizindeki dosya veya klasörlere yönelik göreli bağlantılar için `./`, üst dizindeki dosya veya klasörler için `../` kullanın. Örneğin: `[example](../../path/to/file)` veya `[example](../../../path/to/file)`.

- **Ülkeye özel yerel ayarlar kullanmayın**: Bağlantılarınızda ülkeye özgü yerel ayarları içermediğinden emin olun. Örneğin, `/en-us/` veya `/en/` kullanmaktan kaçının.

- **Resim depolama**: Tüm resimleri `./imgs` klasöründe saklayın.

- **Anlamlı resim adları**: Resim adlarını İngilizce karakterler, rakamlar ve tire kullanarak açıklayıcı şekilde adlandırın. Örneğin: `example-image.jpg`.

## GitHub İş Akışları

Bir pull request gönderdiğinizde, değişikliklerin doğrulanması için aşağıdaki iş akışları tetiklenir. Pull request'inizin iş akışı kontrollerinden geçmesi için aşağıdaki talimatları izleyin:

- [Kırık Göreli Yolları Kontrol Et](../..)
- [URL'lerin Yerel Ayar İçermediğini Kontrol Et](../..)

### Kırık Göreli Yolları Kontrol Et

Bu iş akışı, dosyalarınızdaki tüm göreli yolların doğru olduğunu doğrular.

1. Bağlantılarınızın düzgün çalıştığından emin olmak için VS Code kullanarak şu işlemleri yapın:
    - Dosyalarınızdaki herhangi bir bağlantının üzerine gelin.
    - **Ctrl + Tıklama** yaparak bağlantıya gidin.
    - Eğer bağlantı yerel olarak çalışmıyorsa, iş akışı tetiklenir ve GitHub'da da çalışmaz.

1. Bu sorunu düzeltmek için VS Code tarafından önerilen yol seçeneklerini kullanarak şu işlemleri yapın:
    - `./` veya `../` yazın.
    - VS Code, yazdıklarınıza göre mevcut seçeneklerden birini seçmenizi isteyecektir.
    - Doğru yolu seçmek için istediğiniz dosya veya klasöre tıklayın.

Doğru göreli yolu ekledikten sonra değişikliklerinizi kaydedin ve gönderin.

### URL'lerin Yerel Ayar İçermediğini Kontrol Et

Bu iş akışı, herhangi bir web URL'sinin ülkeye özgü yerel ayar içermediğini doğrular. Bu depo küresel olarak erişilebilir olduğu için URL'lerin ülkenizin yerel ayarını içermemesi önemlidir.

1. URL'lerinizin ülkeye özgü yerel ayar içermediğini doğrulamak için şu işlemleri yapın:

    - URL'lerde `/en-us/`, `/en/` veya başka herhangi bir dil yerel ayarına bakın.
    - Eğer bunlar URL'lerinizde yoksa, bu kontrolü geçersiniz.

1. Bu sorunu düzeltmek için şu işlemleri yapın:
    - İş akışı tarafından işaretlenen dosya yolunu açın.
    - URL'lerden ülke yerel ayarını kaldırın.

Ülke yerel ayarını kaldırdıktan sonra dosyayı kaydedin ve değişikliklerinizi gönderin.

### Kırık URL'leri Kontrol Et

Bu iş akışı, dosyalarınızdaki herhangi bir web URL'sinin çalıştığını ve 200 durum kodu döndürdüğünü doğrular.

1. URL'lerinizin düzgün çalıştığını doğrulamak için şu işlemleri yapın:
    - Dosyalarınızdaki URL'lerin durumunu kontrol edin.

2. Kırık URL'leri düzeltmek için şu işlemleri yapın:
    - Kırık URL içeren dosyayı açın.
    - URL'yi doğru olanla güncelleyin.

URL'leri düzelttikten sonra dosyayı kaydedin ve değişikliklerinizi gönderin.

> [!NOTE]
>
> Bağlantı erişilebilir olsa bile URL kontrolü başarısız olabilir. Bunun birkaç nedeni olabilir:
>
> - **Ağ kısıtlamaları:** GitHub eylem sunucularının bazı URL'lere erişimi engellenmiş olabilir.
> - **Zaman aşımı sorunları:** Yanıt vermesi uzun süren URL'ler iş akışında zaman aşımı hatası oluşturabilir.
> - **Geçici sunucu sorunları:** Sunucu bakımı veya arızaları doğrulama sırasında URL'nin geçici olarak erişilememesine neden olabilir.

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucunda oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.