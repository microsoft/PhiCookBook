Bu demo, önceden eğitilmiş bir modeli kullanarak bir görüntü ve metin istemine dayalı Python kodu nasıl oluşturulacağını gösterir.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Adım adım açıklama:

1. **İçe Aktarmalar ve Kurulum**:
   - Gerekli kütüphaneler ve modüller, `requests`, görüntü işleme için `PIL` ve modeli ve işlemleri yönetmek için `transformers` dahil olmak üzere içe aktarılır.

2. **Görüntüyü Yükleme ve Gösterme**:
   - `PIL` kütüphanesi kullanılarak bir görüntü dosyası (`demo.png`) açılır ve gösterilir.

3. **İstemi Tanımlama**:
   - Görüntüyü içeren ve görüntüyü işlemek ve `plt` (matplotlib) kullanarak kaydetmek için Python kodu oluşturulmasını isteyen bir mesaj oluşturulur.

4. **İşlemciyi Yükleme**:
   - `AutoProcessor`, `out_dir` diziniyle belirtilen önceden eğitilmiş modelden yüklenir. Bu işlemci, metin ve görüntü girdilerini işleyecektir.

5. **İstemi Oluşturma**:
   - `apply_chat_template` yöntemi, mesajı modele uygun bir isteme dönüştürmek için kullanılır.

6. **Girdileri İşleme**:
   - İstem ve görüntü, modelin anlayabileceği tensörlere dönüştürülür.

7. **Üretim Argümanlarını Ayarlama**:
   - Modelin üretim süreci için, oluşturulacak maksimum yeni token sayısı ve çıktının örneklenip örneklenmeyeceği gibi argümanlar tanımlanır.

8. **Kodu Üretme**:
   - Model, girdiler ve üretim argümanlarına dayanarak Python kodunu üretir. `TextStreamer`, istem ve özel tokenları atlayarak çıktıyı yönetmek için kullanılır.

9. **Çıktı**:
   - Üretilen kod yazdırılır; bu kod, istemde belirtildiği gibi görüntüyü işleyip kaydeden Python kodunu içermelidir.

Bu demo, OpenVino kullanarak önceden eğitilmiş bir modeli, kullanıcı girdisi ve görüntülere dayalı olarak dinamik kod üretmek için nasıl kullanabileceğinizi gösterir.

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.