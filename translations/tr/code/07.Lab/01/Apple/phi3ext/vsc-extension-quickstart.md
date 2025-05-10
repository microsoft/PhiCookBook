<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-09T05:07:41+00:00",
  "source_file": "code/07.Lab/01/Apple/phi3ext/vsc-extension-quickstart.md",
  "language_code": "tr"
}
-->
# VS Code Eklentinize Hoş Geldiniz

## Klasörde Neler Var

* Bu klasör, eklentiniz için gerekli tüm dosyaları içerir.
* `package.json` - eklentinizi ve komutunuzu bildirdiğiniz manifest dosyasıdır.
  * Örnek eklenti bir komut kaydeder ve başlığını ile komut adını tanımlar. Bu bilgilerle VS Code, komutu komut paletinde gösterebilir. Henüz eklentiyi yüklemesine gerek yoktur.
* `src/extension.ts` - komutunuzun uygulamasını sağlayacağınız ana dosyadır.
  * Dosya, eklentiniz ilk kez etkinleştirildiğinde (bu durumda komut çalıştırıldığında) çağrılan `activate` adlı bir fonksiyon dışa aktarır. `activate` fonksiyonunun içinde `registerCommand` çağrılır.
  * Komutun uygulamasını içeren fonksiyonu, `registerCommand` fonksiyonuna ikinci parametre olarak geçiriyoruz.

## Kurulum

* Önerilen eklentileri yükleyin (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner ve dbaeumer.vscode-eslint)

## Hemen Başlayın

* Eklentiniz yüklü yeni bir pencere açmak için `F5` tuşuna basın.
* Komut paletinden (`Ctrl+Shift+P` veya Mac'te `Cmd+Shift+P`) tuşlarına basıp `Hello World` yazarak komutunuzu çalıştırın.
* Eklentinizi hata ayıklamak için `src/extension.ts` içindeki kodunuza kesme noktaları koyun.
* Eklentinizin çıktısını hata ayıklama konsolunda bulun.

## Değişiklik Yapın

* `src/extension.ts` dosyasındaki kodu değiştirdikten sonra hata ayıklama araç çubuğundan eklentiyi yeniden başlatabilirsiniz.
* Ayrıca eklentinizin değişikliklerini yüklemek için VS Code penceresini (`Ctrl+R` veya Mac'te `Cmd+R`) yeniden yükleyebilirsiniz.

## API'yi Keşfedin

* `node_modules/@types/vscode/index.d.ts` dosyasını açtığınızda API’mizin tam setine erişebilirsiniz.

## Testleri Çalıştırın

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner) eklentisini yükleyin
* **Tasks: Run Task** komutu ile "watch" görevini çalıştırın. Bu görev çalışmazsa testler bulunamayabilir.
* Aktivite çubuğundan Testing görünümünü açın ve "Run Test" butonuna tıklayın veya `Ctrl/Cmd + ; A` kısayolunu kullanın.
* Test sonuçlarının çıktısını Test Results görünümünde görebilirsiniz.
* `src/test/extension.test.ts` dosyasını değiştirin veya `test` klasörü içinde yeni test dosyaları oluşturun.
  * Sağlanan test çalıştırıcı sadece `**.test.ts` isim desenine uyan dosyaları dikkate alır.
  * Testlerinizi istediğiniz şekilde düzenlemek için `test` klasörü içinde yeni klasörler oluşturabilirsiniz.

## Daha İleri Gidin

* Eklentinizin boyutunu küçültmek ve başlatma süresini iyileştirmek için [eklentinizi paketleyin](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* VS Code eklenti pazarında [eklentinizi yayınlayın](https://code.visualstudio.com/api/working-with-extensions/publishing-extension).
* [Sürekli Entegrasyon](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) kurarak derlemeleri otomatikleştirin.

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilindeki haliyle yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı nedeniyle ortaya çıkabilecek herhangi bir yanlış anlama veya yorum hatasından sorumlu değiliz.