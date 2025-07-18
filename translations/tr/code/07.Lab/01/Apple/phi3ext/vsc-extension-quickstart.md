<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-07-16T17:01:22+00:00",
  "source_file": "code/07.Lab/01/Apple/phi3ext/vsc-extension-quickstart.md",
  "language_code": "tr"
}
-->
# VS Code Eklentinize Hoş Geldiniz

## Klasörde Neler Var

* Bu klasör, eklentiniz için gerekli tüm dosyaları içerir.
* `package.json` - eklentinizi ve komutunuzu bildirdiğiniz manifest dosyasıdır.
  * Örnek eklenti bir komut kaydeder ve başlığını ile komut adını tanımlar. Bu bilgilerle VS Code, komutu komut paletinde gösterebilir. Henüz eklentiyi yüklemesi gerekmez.
* `src/extension.ts` - komutunuzun uygulamasını sağlayacağınız ana dosyadır.
  * Dosya, eklentiniz ilk kez etkinleştirildiğinde (bu durumda komut çalıştırıldığında) çağrılan `activate` adlı bir fonksiyon dışa aktarır. `activate` fonksiyonu içinde `registerCommand` çağrılır.
  * Komutun uygulamasını içeren fonksiyon, `registerCommand`'a ikinci parametre olarak iletilir.

## Kurulum

* Önerilen eklentileri yükleyin (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner ve dbaeumer.vscode-eslint)

## Hemen Başlayın

* Eklentiniz yüklü yeni bir pencere açmak için `F5` tuşuna basın.
* Komut paletinden (`Ctrl+Shift+P` veya Mac'te `Cmd+Shift+P`) `Hello World` yazarak komutunuzu çalıştırın.
* Eklentinizi hata ayıklamak için `src/extension.ts` içindeki kodunuza kesme noktaları (breakpoint) koyun.
* Eklentinizin çıktısını hata ayıklama konsolunda bulun.

## Değişiklik Yapın

* `src/extension.ts` dosyasındaki kodu değiştirdikten sonra hata ayıklama araç çubuğundan eklentiyi yeniden başlatabilirsiniz.
* Ayrıca değişikliklerinizi yüklemek için VS Code penceresini (`Ctrl+R` veya Mac'te `Cmd+R`) yeniden yükleyebilirsiniz.

## API'yi Keşfedin

* `node_modules/@types/vscode/index.d.ts` dosyasını açarak API'nin tamamını inceleyebilirsiniz.

## Testleri Çalıştırın

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner) eklentisini yükleyin.
* **Tasks: Run Task** komutuyla "watch" görevini çalıştırın. Bu görev çalışmazsa testler bulunamayabilir.
* Aktivite çubuğundan Testing görünümünü açın ve "Run Test" butonuna tıklayın veya `Ctrl/Cmd + ; A` kısayolunu kullanın.
* Test sonuçlarını Test Results görünümünde görebilirsiniz.
* `src/test/extension.test.ts` dosyasını değiştirebilir veya `test` klasörü içinde yeni test dosyaları oluşturabilirsiniz.
  * Sağlanan test çalıştırıcı yalnızca `**.test.ts` isim desenine uyan dosyaları dikkate alır.
  * Testlerinizi istediğiniz şekilde düzenlemek için `test` klasörü içinde alt klasörler oluşturabilirsiniz.

## Daha İleri Gidin

* Eklenti boyutunu küçültmek ve başlangıç süresini iyileştirmek için [eklentinizi paketleyin](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* Eklentinizi VS Code eklenti pazarında [yayınlayın](https://code.visualstudio.com/api/working-with-extensions/publishing-extension).
* [Sürekli Entegrasyon](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) kurarak derlemeleri otomatikleştirin.

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.