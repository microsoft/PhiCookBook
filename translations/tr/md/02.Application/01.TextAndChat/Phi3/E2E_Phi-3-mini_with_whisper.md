# Whisper ile Etkileşimli Phi 3 Mini 4K Yönergeli Sohbet Botu

## Genel Bakış

Etkileşimli Phi 3 Mini 4K Yönergeli Sohbet Botu, kullanıcıların Microsoft Phi 3 Mini 4K yönergeli demoyla metin veya sesli giriş kullanarak etkileşimde bulunmasını sağlayan bir araçtır. Sohbet botu, çeviri, hava durumu güncellemeleri ve genel bilgi toplama gibi çeşitli görevler için kullanılabilir.

### Başlarken

Bu sohbet botunu kullanmak için şu talimatları izleyin:

1. Yeni bir [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) açın.
2. Defterin ana penceresinde, bir metin giriş kutusu ve bir "Gönder" düğmesi içeren bir sohbet kutusu arayüzü göreceksiniz.
3. Metne dayalı sohbet botunu kullanmak için, mesajınızı metin giriş kutusuna yazın ve "Gönder" düğmesine tıklayın. Sohbet botu, doğrudan defter içinden oynatılabilecek bir ses dosyası ile yanıt verecektir.

**Not**: Bu araç GPU ve konuşma tanıma ile çeviri için kullanılan Microsoft Phi-3 ve OpenAI Whisper modellerine erişim gerektirir.

### GPU Gereksinimleri

Bu demoyu çalıştırmak için 12GB GPU belleğine ihtiyacınız vardır.

**Microsoft-Phi-3-Mini-4K instruct** demosunu bir GPU üzerinde çalıştırmak için gereken bellek, giriş verisinin boyutu (ses veya metin), kullanılan dil, modelin hızı ve GPU üzerindeki mevcut bellek gibi çeşitli faktörlere bağlıdır.

Genel olarak, Whisper modeli GPU'lar üzerinde çalışacak şekilde tasarlanmıştır. Whisper modelini çalıştırmak için önerilen minimum GPU belleği 8 GB'dir, ancak gerekirse daha büyük bellek miktarlarını da kullanabilir.

Model üzerinde büyük miktarda veri veya yüksek istek hacmi çalıştırmanın daha fazla GPU belleği gerektirebileceğini ve/veya performans sorunlarına yol açabileceğini not etmek önemlidir. Özel ihtiyaçlarınız için en uygun ayarları belirlemek amacıyla kullanım durumunuzu farklı yapılandırmalarla test etmek ve bellek kullanımını izlemek önerilir.

## Whisper ile Etkileşimli Phi 3 Mini 4K Yönergeli Sohbet Botu için E2E Örneği

[Whisper ile Etkileşimli Phi 3 Mini 4K Yönergeli Sohbet Botu](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) adlı jupyter defteri, Microsoft Phi 3 Mini 4K yönergeli demoyu ses veya yazılı metin girdisinden metin üretmek için nasıl kullanacağınızı gösterir. Defter birkaç fonksiyon tanımlar:

1. `tts_file_name(text)`: Bu fonksiyon, oluşturulan ses dosyasını kaydetmek için giriş metnine dayalı bir dosya adı üretir.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Bu fonksiyon, Edge TTS API'sini kullanarak giriş metni parçalardan oluşan bir listeden ses dosyası üretir. Girdi parametreleri parça listesi, konuşma hızı, ses adı ve oluşturulan ses dosyasının kaydedileceği çıkış yoludur.
1. `talk(input_text)`: Bu fonksiyon, Edge TTS API'sini kullanarak ses dosyası üretir ve /content/audio dizininde rastgele bir dosya adına kaydeder. Girdi parametresi, sese dönüştürülecek giriş metnidir.
1. `run_text_prompt(message, chat_history)`: Bu fonksiyon, mesaj girdisinden Microsoft Phi 3 Mini 4K yönergeli demoyu kullanarak bir ses dosyası oluşturur ve bunu sohbet geçmişine ekler.
1. `run_audio_prompt(audio, chat_history)`: Bu fonksiyon, bir ses dosyasını Whisper model API'si kullanarak metne dönüştürür ve `run_text_prompt()` fonksiyonuna iletir.
1. Kod, kullanıcıların Phi 3 Mini 4K yönergeli demoyla mesaj yazarak veya ses dosyası yükleyerek etkileşim kurmasını sağlayan bir Gradio uygulaması başlatır. Çıktı, uygulama içinde bir metin mesajı olarak görüntülenir.

## Sorun Giderme

Cuda GPU sürücülerinin kurulması

1. Linux uygulamanızın güncel olduğundan emin olun

    ```bash
    sudo apt update
    ```

1. Cuda Sürücülerini Yükleyin

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Cuda sürücü konumunu kaydedin

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Nvidia GPU bellek boyutunu kontrol edin (Gerekli 12GB GPU Belleği)

    ```bash
    nvidia-smi
    ```

1. Boş Önbellek: PyTorch kullanıyorsanız, diğer GPU uygulamalarının kullanabilmesi için kullanılmayan önbellek belleğini boşaltmak amaçlı torch.cuda.empty_cache() çağrısı yapabilirsiniz

    ```python
    torch.cuda.empty_cache() 
    ```

1. Nvidia Cuda'yı kontrol edin

    ```bash
    nvcc --version
    ```

1. Hugging Face token oluşturmak için aşağıdaki işlemleri yapın.

    - [Hugging Face Token Ayarları sayfasına](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo) gidin.
    - **Yeni token** seçin.
    - Kullanmak istediğiniz proje **Adı** girin.
    - **Tür**ü **Yazma** olarak seçin.

> [!NOTE]
>
> Aşağıdaki hatayla karşılaşırsanız:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Bunu çözmek için terminalinizde aşağıdaki komutu yazın.
>
> ```bash
> sudo ldconfig
> ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini unutmayınız. Orijinal belge, kendi ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucunda ortaya çıkabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->