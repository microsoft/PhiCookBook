<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-05-09T18:30:54+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "tr"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

## Genel Bakış

Interactive Phi 3 Mini 4K Instruct Chatbot, kullanıcıların Microsoft Phi 3 Mini 4K instruct demo ile metin veya ses girişi kullanarak etkileşim kurmasını sağlayan bir araçtır. Chatbot, çeviri, hava durumu güncellemeleri ve genel bilgi toplama gibi çeşitli görevler için kullanılabilir.

### Başlarken

Bu chatbot'u kullanmak için şu adımları izleyin:

1. Yeni bir [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) dosyası açın.
2. Notebook’un ana penceresinde, metin girişi kutusu ve "Send" butonunun bulunduğu bir sohbet kutusu arayüzü göreceksiniz.
3. Metin tabanlı chatbot’u kullanmak için, mesajınızı metin giriş kutusuna yazın ve "Send" butonuna tıklayın. Chatbot, notebook içinde doğrudan oynatılabilen bir ses dosyası ile yanıt verecektir.

**Note**: Bu araç, konuşma tanıma ve çeviri için kullanılan Microsoft Phi-3 ve OpenAI Whisper modellerine erişim ve bir GPU gerektirir.

### GPU Gereksinimleri

Bu demo’yu çalıştırmak için 12GB GPU belleği gereklidir.

**Microsoft-Phi-3-Mini-4K instruct** demosunun GPU’da çalışması için gereken bellek, giriş verisinin boyutu (ses veya metin), çeviri dili, modelin hızı ve GPU’da mevcut olan bellek gibi çeşitli faktörlere bağlıdır.

Genel olarak, Whisper modeli GPU’larda çalışacak şekilde tasarlanmıştır. Whisper modelini çalıştırmak için önerilen minimum GPU bellek miktarı 8 GB’dır, ancak ihtiyaç halinde daha büyük bellekleri de kullanabilir.

Büyük miktarda veri veya yüksek sayıda istek model üzerinde çalıştırıldığında daha fazla GPU belleği gerekebilir ve/veya performans sorunları yaşanabilir. Kendi kullanım senaryonuzda farklı konfigürasyonlarla test yapmanız ve bellek kullanımını izleyerek en uygun ayarları belirlemeniz tavsiye edilir.

## Whisper ile Interactive Phi 3 Mini 4K Instruct Chatbot için E2E Örneği

[Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) başlıklı jupyter notebook, Microsoft Phi 3 Mini 4K instruct Demo’nun ses veya yazılı metin girdisinden metin üretmek için nasıl kullanılacağını gösterir. Notebook aşağıdaki fonksiyonları tanımlar:

1. `tts_file_name(text)`: Üretilen ses dosyasını kaydetmek için giriş metnine göre dosya adı oluşturan fonksiyon.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Giriş metni parçalarından oluşan bir listeyi kullanarak Edge TTS API ile ses dosyası oluşturan fonksiyon. Girdi parametreleri, parçalar listesi, konuşma hızı, ses adı ve oluşturulan ses dosyasının kaydedileceği yol.
1. `talk(input_text)`: Edge TTS API kullanarak ses dosyası oluşturan ve bunu /content/audio dizininde rastgele bir dosya adına kaydeden fonksiyon. Girdi parametresi, konuşmaya dönüştürülecek metindir.
1. `run_text_prompt(message, chat_history)`: Microsoft Phi 3 Mini 4K instruct demo kullanarak mesaj girdisinden ses dosyası oluşturan ve sohbet geçmişine ekleyen fonksiyon.
1. `run_audio_prompt(audio, chat_history)`: Whisper model API’si ile ses dosyasını metne dönüştüren ve sonucu `run_text_prompt()` fonksiyonuna ileten fonksiyon.
1. Kod, kullanıcıların mesaj yazarak veya ses dosyası yükleyerek Phi 3 Mini 4K instruct demo ile etkileşim kurmasını sağlayan bir Gradio uygulaması başlatır. Çıktı, uygulama içinde metin mesajı olarak gösterilir.

## Sorun Giderme

Cuda GPU sürücülerinin kurulumu

1. Linux uygulamalarınızın güncel olduğundan emin olun

    ```bash
    sudo apt update
    ```

1. Cuda Sürücülerini kurun

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Cuda sürücü konumunu kaydedin

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Nvidia GPU bellek boyutunu kontrol edin (Gerekli: 12GB GPU Belleği)

    ```bash
    nvidia-smi
    ```

1. Boş önbellek: PyTorch kullanıyorsanız, tüm kullanılmayan önbellek belleğini serbest bırakmak için torch.cuda.empty_cache() fonksiyonunu çağırabilirsiniz; böylece diğer GPU uygulamaları kullanabilir.

    ```python
    torch.cuda.empty_cache() 
    ```

1. Nvidia Cuda’yı kontrol edin

    ```bash
    nvcc --version
    ```

1. Hugging Face token oluşturmak için aşağıdaki adımları gerçekleştirin.

    - [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo) sayfasına gidin.
    - **New token** seçeneğini seçin.
    - Kullanmak istediğiniz proje **Adı**nı girin.
    - **Type** olarak **Write** seçin.

> **Note**
>
> Aşağıdaki hatayla karşılaşırsanız:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Çözmek için terminalinizde aşağıdaki komutu yazın.
>
> ```bash
> sudo ldconfig
> ```

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı nedeniyle oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.