<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eae2c0ea18160a3e7a63ace7b53897d7",
  "translation_date": "2025-05-09T04:55:56+00:00",
  "source_file": "code/07.Lab/01/AIPC/extensions/phi3ext/vsc-extension-quickstart.md",
  "language_code": "tr"
}
-->
# VS Code Uzantınıza Hoş Geldiniz

## Klasörde Neler Var

* Bu klasör, uzantınız için gerekli tüm dosyaları içerir.
* `package.json` - uzantınızı ve komutunuzu bildirdiğiniz manifest dosyasıdır.
  * Örnek eklenti, bir komut kaydeder ve başlığını ile komut adını tanımlar. Bu bilgilerle VS Code, komutu komut paletinde gösterebilir. Henüz eklentiyi yüklemesi gerekmez.
* `src/extension.ts` - komutunuzun uygulamasını sağlayacağınız ana dosyadır.
  * Dosya, `activate` adında bir fonksiyon dışa aktarır; bu fonksiyon uzantınız ilk kez etkinleştirildiğinde (bu durumda komut çalıştırıldığında) çağrılır. `activate` fonksiyonunun içinde `registerCommand` çağrılır.
  * Komutun uygulamasını içeren fonksiyon, `registerCommand` fonksiyonuna ikinci parametre olarak iletilir.

## Kurulum

* Önerilen uzantıları yükleyin (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner ve dbaeumer.vscode-eslint)

## Hemen Başlayın

* Uzantınız yüklü yeni bir pencere açmak için `F5` tuşuna basın.
* Komut paletinden komutunuzu çalıştırmak için (`Ctrl+Shift+P` veya Mac’te `Cmd+Shift+P`) tuşlarına basıp `Hello World` yazın.
* Uzantınızı hata ayıklamak için `src/extension.ts` içindeki kodunuza kesme noktaları koyun.
* Uzantınızın çıktısını hata ayıklama konsolunda bulun.

## Değişiklik Yapın

* `src/extension.ts` dosyasındaki kodu değiştirdikten sonra hata ayıklama araç çubuğundan uzantıyı yeniden başlatabilirsiniz.
* Ayrıca, değişikliklerinizi yüklemek için uzantınız yüklü VS Code penceresini (`Ctrl+R` veya Mac’te `Cmd+R`) yeniden yükleyebilirsiniz.

## API’yi Keşfedin

* `node_modules/@types/vscode/index.d.ts` dosyasını açtığınızda API’nin tamamını görebilirsiniz.

## Testleri Çalıştırın

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner) uzantısını yükleyin
* **Tasks: Run Task** komutu ile "watch" görevini çalıştırın. Bu görev çalışmazsa testler bulunamayabilir.
* Aktivite çubuğundan Testing görünümünü açın ve "Run Test" düğmesine tıklayın veya `Ctrl/Cmd + ; A` kısayolunu kullanın.
* Test sonuçlarını Test Results görünümünde görün.
* `src/test/extension.test.ts` dosyasını değiştirin veya `test` klasörü içinde yeni test dosyaları oluşturun.
  * Sağlanan test çalıştırıcı yalnızca `**.test.ts` isim desenine uyan dosyaları dikkate alır.
  * Testlerinizi istediğiniz şekilde düzenlemek için `test` klasörü içinde alt klasörler oluşturabilirsiniz.

## Daha İleri Gidin

* Uzantınızın boyutunu küçültmek ve başlangıç süresini hızlandırmak için [uzantınızı paketleyin](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* VS Code uzantı pazarında [uzantınızı yayınlayın](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Sürekli Entegrasyon](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo) ayarlayarak derlemeleri otomatikleştirin.

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yorum farklılıklarından sorumlu değiliz.