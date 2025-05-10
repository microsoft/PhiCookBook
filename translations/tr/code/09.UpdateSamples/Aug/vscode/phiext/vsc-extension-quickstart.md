<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-09T05:35:31+00:00",
  "source_file": "code/09.UpdateSamples/Aug/vscode/phiext/vsc-extension-quickstart.md",
  "language_code": "tr"
}
-->
# VS Code Eklentinize Hoş Geldiniz

## Klasörde Neler Var

* Bu klasör, eklentiniz için gerekli olan tüm dosyaları içerir.
* `package.json` - eklentinizi ve komutunuzu bildirdiğiniz manifest dosyasıdır.
  * Örnek eklenti, bir komut kaydeder ve başlığını ile komut adını tanımlar. Bu bilgilerle VS Code, komutu komut paletinde gösterebilir. Eklentiyi henüz yüklemesi gerekmez.
* `src/extension.ts` - komutunuzun uygulanmasını sağlayacağınız ana dosyadır.
  * Dosya, eklentinizin etkinleştirildiği ilk anda (bu durumda komut çalıştırıldığında) çağrılan `activate` adlı bir fonksiyon dışa aktarır. `activate` fonksiyonunun içinde `registerCommand` çağrılır.
  * Komutun uygulanmasını içeren fonksiyonu `registerCommand`'e ikinci parametre olarak geçiririz.

## Kurulum

* Önerilen eklentileri yükleyin (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner ve dbaeumer.vscode-eslint)


## Hemen Başlayın

* Eklentiniz yüklü yeni bir pencere açmak için `F5` tuşuna basın.
* Komut paletinden komutunuzu çalıştırmak için (`Ctrl+Shift+P` veya Mac’te `Cmd+Shift+P`) tuşlarına basın ve `Hello World` yazın.
* Eklentinizi hata ayıklamak için `src/extension.ts` içindeki kodunuza duraklama noktaları (breakpoint) koyun.
* Eklentinizin çıktısını hata ayıklama konsolunda bulun.

## Değişiklik Yapın

* `src/extension.ts` içindeki kodu değiştirdikten sonra hata ayıklama araç çubuğundan eklentiyi yeniden başlatabilirsiniz.
* Ayrıca değişikliklerinizi yüklemek için VS Code penceresini (`Ctrl+R` veya Mac’te `Cmd+R`) yeniden yükleyebilirsiniz.

## API’yi Keşfedin

* `node_modules/@types/vscode/index.d.ts` dosyasını açtığınızda API’mizin tamamına erişebilirsiniz.

## Testleri Çalıştırın

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner) eklentisini yükleyin.
* **Tasks: Run Task** komutuyla "watch" görevini çalıştırın. Bu görev çalışmazsa testler bulunamayabilir.
* Aktivite çubuğundan Testing görünümünü açın ve "Run Test" düğmesine tıklayın ya da `Ctrl/Cmd + ; A` kısayolunu kullanın.
* Test sonuçlarını Test Results görünümünde görün.
* `src/test/extension.test.ts` dosyasını değiştirin veya `test` klasöründe yeni test dosyaları oluşturun.
  * Sağlanan test çalıştırıcı yalnızca `**.test.ts` ad desenine uyan dosyaları dikkate alır.
  * Testlerinizi istediğiniz şekilde yapılandırmak için `test` klasöründe yeni klasörler oluşturabilirsiniz.

## Daha İleri Gitmek

* Eklenti boyutunu küçültmek ve başlangıç süresini iyileştirmek için [eklentinizi paketleyin](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* VS Code eklenti pazarında [eklentinizi yayınlayın](https://code.visualstudio.com/api/working-with-extensions/publishing-extension).
* [Sürekli Entegrasyon](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) kurarak derlemeleri otomatikleştirin.

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilindeki haliyle yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı nedeniyle oluşabilecek yanlış anlamalar veya yanlış yorumlamalar konusunda sorumluluk kabul edilmemektedir.