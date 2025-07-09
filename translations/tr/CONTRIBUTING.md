<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "90d0d072cf26ccc1f271a580d3e45d70",
  "translation_date": "2025-07-09T18:23:43+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "tr"
}
-->
# Katkıda Bulunma

Bu proje katkılara ve önerilere açıktır. Çoğu katkı için, katkınızı kullanma haklarını bize verdiğinizi ve gerçekten bu haklara sahip olduğunuzu beyan eden bir Contributor License Agreement (CLA) kabul etmeniz gerekir. Detaylar için [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com) adresini ziyaret edin.

Bir pull request gönderdiğinizde, bir CLA botu otomatik olarak CLA sağlamanız gerekip gerekmediğini belirler ve PR'ı uygun şekilde işaretler (örneğin, durum kontrolü, yorum). Botun verdiği talimatları takip etmeniz yeterlidir. CLA, tüm depolarda yalnızca bir kez yapılması gereken bir işlemdir.

## Davranış Kuralları

Bu proje [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) kurallarını benimsemiştir. Daha fazla bilgi için [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) sayfasını okuyabilir veya ek sorularınız ya da yorumlarınız için [opencode@microsoft.com](mailto:opencode@microsoft.com) adresiyle iletişime geçebilirsiniz.

## Sorun Oluştururken Dikkat Edilmesi Gerekenler

Lütfen genel destek soruları için GitHub issue açmayın; GitHub listesi özellik talepleri ve hata raporları için kullanılmalıdır. Bu sayede gerçek kod sorunlarını veya hatalarını daha kolay takip edebilir ve genel tartışmaları koddan ayrı tutabiliriz.

## Katkıda Bulunma Yöntemleri

### Pull Request Kuralları

Phi-3 CookBook deposuna pull request (PR) gönderirken aşağıdaki kurallara uyunuz:

- **Depoyu Forklayın**: Değişiklik yapmadan önce her zaman depoyu kendi hesabınıza forklayın.

- **Ayrı pull requestler (PR)**:
  - Her değişiklik türünü ayrı bir pull request olarak gönderin. Örneğin, hata düzeltmeleri ve dokümantasyon güncellemeleri ayrı PR’larda olmalıdır.
  - Yazım hatası düzeltmeleri ve küçük dokümantasyon güncellemeleri uygun olduğunda tek bir PR’da birleştirilebilir.

- **Birleştirme çatışmalarını çözün**: Pull request’inizde birleştirme çatışmaları varsa, değişiklik yapmadan önce yerel `main` dalınızı ana depoyla güncelleyin.

- **Çeviri gönderimleri**: Çeviri PR’ları gönderirken, çeviri klasörünün orijinal klasördeki tüm dosyaların çevirilerini içerdiğinden emin olun.

### Yazım Kuralları

Tüm belgelerde tutarlılığı sağlamak için aşağıdaki kurallara uyunuz:

- **URL formatı**: Tüm URL’leri köşeli parantez içine alıp ardından parantez içinde yazın, aralarında veya içinde ekstra boşluk bırakmayın. Örnek: `[example](https://www.microsoft.com)`.

- **Göreli bağlantılar**: Geçerli dizindeki dosya veya klasörlere göreli bağlantılar için `./`, üst dizindeki dosya veya klasörler için `../` kullanın. Örnek: `[example](../../path/to/file)` veya `[example](../../../path/to/file)`.

- **Ülkeye özgü yerel ayar kullanmayın**: Bağlantılarınızda ülkeye özgü yerel ayarları içermediğinden emin olun. Örneğin, `/en-us/` veya `/en/` kullanmaktan kaçının.

- **Resimlerin depolanması**: Tüm resimleri `./imgs` klasöründe saklayın.

- **Anlamlı resim isimleri**: Resimleri İngilizce karakterler, rakamlar ve tire kullanarak açıklayıcı şekilde adlandırın. Örnek: `example-image.jpg`.

## GitHub İş Akışları

Pull request gönderdiğinizde, değişikliklerin doğrulanması için aşağıdaki iş akışları tetiklenir. Pull request’inizin iş akışı kontrollerinden geçmesi için aşağıdaki talimatları izleyin:

- [Kırık Göreli Yolları Kontrol Et](../..)
- [URL’lerde Yerel Ayar Olmadığını Kontrol Et](../..)

### Kırık Göreli Yolları Kontrol Et

Bu iş akışı, dosyalarınızdaki tüm göreli yolların doğru olduğunu doğrular.

1. Bağlantılarınızın düzgün çalıştığından emin olmak için VS Code kullanarak aşağıdaki işlemleri yapın:
    - Dosyalarınızdaki herhangi bir bağlantının üzerine gelin.
    - **Ctrl + Tıklama** yaparak bağlantıya gidin.
    - Eğer bağlantıya tıkladığınızda yerelde çalışmıyorsa, bu iş akışını tetikler ve GitHub’da da çalışmaz.

1. Bu sorunu düzeltmek için VS Code’un sunduğu yol önerilerini kullanarak aşağıdaki işlemleri yapın:
    - `./` veya `../` yazın.
    - VS Code, yazdığınıza göre mevcut seçenekleri sunacaktır.
    - Doğru yolu seçmek için istediğiniz dosya veya klasöre tıklayın.

Doğru göreli yolu ekledikten sonra değişikliklerinizi kaydedip gönderin.

### URL’lerde Yerel Ayar Olmadığını Kontrol Et

Bu iş akışı, web URL’lerinde ülkeye özgü yerel ayarların olmadığını doğrular. Bu depo dünya çapında erişilebilir olduğundan, URL’lerde ülkenizin yerel ayarının bulunmaması önemlidir.

1. URL’lerinizde ülkeye özgü yerel ayar olmadığını doğrulamak için aşağıdaki işlemleri yapın:

    - URL’lerde `/en-us/`, `/en/` veya başka bir dil yerel ayarı olup olmadığını kontrol edin.
    - Eğer URL’lerinizde bunlar yoksa, bu kontrolü geçersiniz.

1. Bu sorunu düzeltmek için aşağıdaki işlemleri yapın:
    - İş akışının işaretlediği dosya yolunu açın.
    - URL’lerden ülke yerel ayarını kaldırın.

Yerel ayarı kaldırdıktan sonra değişikliklerinizi kaydedip gönderin.

### Kırık URL’leri Kontrol Et

Bu iş akışı, dosyalarınızdaki tüm web URL’lerinin çalıştığını ve 200 durum kodu döndürdüğünü doğrular.

1. URL’lerinizin doğru çalıştığını doğrulamak için aşağıdaki işlemleri yapın:
    - Dosyalarınızdaki URL’lerin durumunu kontrol edin.

2. Kırık URL’leri düzeltmek için aşağıdaki işlemleri yapın:
    - Kırık URL içeren dosyayı açın.
    - URL’yi doğru olanla güncelleyin.

URL’leri düzelttikten sonra değişikliklerinizi kaydedip gönderin.

> [!NOTE]
>
> Bağlantı erişilebilir olsa bile URL kontrolü başarısız olabilir. Bunun birkaç nedeni olabilir:
>
> - **Ağ kısıtlamaları:** GitHub actions sunucuları bazı URL’lere erişimi engelleyen ağ kısıtlamalarına sahip olabilir.
> - **Zaman aşımı sorunları:** Yanıt vermesi uzun süren URL’ler iş akışında zaman aşımı hatası tetikleyebilir.
> - **Geçici sunucu sorunları:** Ara sıra sunucu bakımı veya kesintileri URL’nin doğrulama sırasında geçici olarak erişilememesine neden olabilir.

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.