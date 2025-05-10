<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7d7afa242a4a041ff4193546d4baf16",
  "translation_date": "2025-05-09T20:00:14+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md",
  "language_code": "tr"
}
-->
Bu demo, önceden eğitilmiş bir modeli kullanarak bir görüntü ve metin istemine dayalı Python kodu oluşturmayı göstermektedir.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

İşte adım adım açıklaması:

1. **İçe Aktarma ve Kurulum**:
   - Gerekli kütüphaneler ve modüller içe aktarılır; görüntü işleme için `requests`, `PIL` ve model ile işlem için `transformers` dahil.

2. **Görüntüyü Yükleme ve Gösterme**:
   - Bir görüntü dosyası (`demo.png`) `PIL` kütüphanesi ile açılır ve gösterilir.

3. **İstemi Tanımlama**:
   - Görüntüyü içeren ve görüntüyü işleyip `plt` (matplotlib) kullanarak kaydetmek için Python kodu oluşturulmasını isteyen bir mesaj hazırlanır.

4. **İşlemciyi Yükleme**:
   - `AutoProcessor`, `out_dir` dizininde belirtilen önceden eğitilmiş modelden yüklenir. Bu işlemci metin ve görüntü girişlerini yönetecektir.

5. **İstemi Oluşturma**:
   - `apply_chat_template` yöntemi, mesajı modele uygun bir isteme dönüştürmek için kullanılır.

6. **Girişleri İşleme**:
   - İstem ve görüntü, modelin anlayabileceği tensörlere dönüştürülür.

7. **Oluşturma Argümanlarını Ayarlama**:
   - Modelin oluşturma süreci için maksimum yeni token sayısı ve çıktı örneklemesi gibi argümanlar tanımlanır.

8. **Kodu Oluşturma**:
   - Model, girişler ve oluşturma argümanlarına dayanarak Python kodu üretir. Çıktı, istem ve özel tokenlar atlanarak `TextStreamer` ile işlenir.

9. **Çıktı**:
   - Üretilen kod yazdırılır; bu kod, görüntüyü işleyip istemde belirtildiği gibi kaydeden Python kodunu içermelidir.

Bu demo, OpenVino kullanarak önceden eğitilmiş bir modeli, kullanıcı girdisi ve görüntülere dayanarak dinamik şekilde kod oluşturmak için nasıl kullanabileceğinizi göstermektedir.

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.