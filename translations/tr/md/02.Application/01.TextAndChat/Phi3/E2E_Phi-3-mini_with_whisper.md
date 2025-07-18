<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-07-17T02:18:30+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "tr"
}
-->
# Whisper ile Etkileşimli Phi 3 Mini 4K Instruct Chatbot

## Genel Bakış

Etkileşimli Phi 3 Mini 4K Instruct Chatbot, kullanıcıların Microsoft Phi 3 Mini 4K instruct demo ile metin veya ses girişi kullanarak etkileşimde bulunmasını sağlayan bir araçtır. Chatbot, çeviri, hava durumu güncellemeleri ve genel bilgi toplama gibi çeşitli görevler için kullanılabilir.

### Başlarken

Bu chatbot'u kullanmak için aşağıdaki adımları izleyin:

1. Yeni bir [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) dosyası açın.
2. Notebook’un ana penceresinde, bir metin giriş kutusu ve "Send" butonunun bulunduğu bir sohbet kutusu arayüzü göreceksiniz.
3. Metin tabanlı chatbot’u kullanmak için, mesajınızı metin giriş kutusuna yazın ve "Send" butonuna tıklayın. Chatbot, notebook içinde doğrudan oynatılabilen bir ses dosyası ile yanıt verecektir.

**Not**: Bu araç, GPU ve konuşma tanıma ile çeviri için kullanılan Microsoft Phi-3 ve OpenAI Whisper modellerine erişim gerektirir.

### GPU Gereksinimleri

Bu demoyu çalıştırmak için 12 GB GPU belleğine ihtiyacınız var.

**Microsoft-Phi-3-Mini-4K instruct** demosunu GPU üzerinde çalıştırmak için gereken bellek miktarı, giriş verisinin boyutu (ses veya metin), çeviri için kullanılan dil, modelin hızı ve GPU üzerindeki mevcut bellek gibi çeşitli faktörlere bağlıdır.

Genel olarak, Whisper modeli GPU’larda çalışacak şekilde tasarlanmıştır. Whisper modelini çalıştırmak için önerilen minimum GPU bellek miktarı 8 GB’dır, ancak gerekirse daha büyük bellek miktarlarını da kullanabilir.

Model üzerinde çok büyük veri veya yüksek hacimli istekler çalıştırmak daha fazla GPU belleği gerektirebilir ve/veya performans sorunlarına yol açabilir. Kendi kullanım senaryonuzu farklı yapılandırmalarla test etmeniz ve bellek kullanımını izleyerek ihtiyaçlarınıza en uygun ayarları belirlemeniz önerilir.

## Whisper ile Etkileşimli Phi 3 Mini 4K Instruct Chatbot için E2E Örneği

[Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) başlıklı jupyter notebook, Microsoft Phi 3 Mini 4K instruct Demo’yu ses veya yazılı metin girdisinden metin üretmek için nasıl kullanacağınızı gösterir. Notebook birkaç fonksiyon tanımlar:

1. `tts_file_name(text)`: Bu fonksiyon, oluşturulan ses dosyasını kaydetmek için giriş metnine dayalı bir dosya adı oluşturur.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Bu fonksiyon, Edge TTS API’sini kullanarak giriş metni parçalarından bir ses dosyası oluşturur. Girdi parametreleri, metin parçalarının listesi, konuşma hızı, ses adı ve oluşturulan ses dosyasının kaydedileceği yoldur.
1. `talk(input_text)`: Bu fonksiyon, Edge TTS API’sini kullanarak bir ses dosyası oluşturur ve /content/audio dizininde rastgele bir dosya adına kaydeder. Girdi parametresi, konuşmaya dönüştürülecek metindir.
1. `run_text_prompt(message, chat_history)`: Bu fonksiyon, Microsoft Phi 3 Mini 4K instruct demo’yu kullanarak bir mesaj girdisinden ses dosyası oluşturur ve bunu sohbet geçmişine ekler.
1. `run_audio_prompt(audio, chat_history)`: Bu fonksiyon, Whisper model API’sini kullanarak bir ses dosyasını metne dönüştürür ve sonucu `run_text_prompt()` fonksiyonuna iletir.
1. Kod, kullanıcıların mesaj yazarak veya ses dosyası yükleyerek Phi 3 Mini 4K instruct demo ile etkileşimde bulunmasını sağlayan bir Gradio uygulaması başlatır. Çıktı, uygulama içinde metin mesajı olarak gösterilir.

## Sorun Giderme

Cuda GPU sürücülerinin kurulumu

1. Linux uygulamalarınızın güncel olduğundan emin olun

    ```bash
    sudo apt update
    ```

1. Cuda Sürücülerini yükleyin

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

1. Önbelleği Boşaltma: PyTorch kullanıyorsanız, diğer GPU uygulamalarının kullanabilmesi için tüm kullanılmayan önbellek belleğini serbest bırakmak amacıyla torch.cuda.empty_cache() fonksiyonunu çağırabilirsiniz

    ```python
    torch.cuda.empty_cache() 
    ```

1. Nvidia Cuda’yı kontrol edin

    ```bash
    nvcc --version
    ```

1. Hugging Face token oluşturmak için aşağıdaki adımları gerçekleştirin.

    - [Hugging Face Token Ayarları sayfasına](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo) gidin.
    - **New token** seçeneğini seçin.
    - Kullanmak istediğiniz proje **Adı**nı girin.
    - **Type** olarak **Write** seçin.

> **Not**
>
> Aşağıdaki hatayla karşılaşırsanız:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Bunu çözmek için terminalinize aşağıdaki komutu yazın.
>
> ```bash
> sudo ldconfig
> ```

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.