<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-05-09T19:55:46+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "tr"
}
-->
### Örnek Senaryo

Elinizde bir resim (`demo.png`) olduğunu ve bu resmi işleyip yeni bir versiyonunu kaydeden Python kodu oluşturmak istediğinizi hayal edin (`phi-3-vision.jpg`).

Yukarıdaki kod bu süreci otomatikleştirir:

1. Ortamı ve gerekli ayarları kurar.
2. Modelin istenilen Python kodunu üretmesini sağlayan bir komut oluşturur.
3. Komutu modele gönderir ve oluşturulan kodu toplar.
4. Üretilen kodu çıkarır ve çalıştırır.
5. Orijinal ve işlenmiş resimleri gösterir.

Bu yöntem, yapay zekanın gücünden faydalanarak görüntü işleme görevlerini otomatikleştirir, hedeflerinize daha kolay ve hızlı ulaşmanızı sağlar.

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Tüm kodun ne yaptığını adım adım inceleyelim:

1. **Gerekli Paketi Kur**:  
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```  
    Bu komut `langchain_nvidia_ai_endpoints` paketini en güncel sürümüyle kurar.

2. **Gerekli Modülleri İçe Aktar**:  
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```  
    Bu importlar, NVIDIA AI uç noktalarıyla etkileşim, şifrelerin güvenli yönetimi, işletim sistemi işlemleri ve base64 formatında kodlama/çözme için gereken modülleri getirir.

3. **API Anahtarını Ayarla**:  
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```  
    Bu kod, `NVIDIA_API_KEY` ortam değişkeninin ayarlanıp ayarlanmadığını kontrol eder. Ayarlı değilse, kullanıcıdan güvenli bir şekilde API anahtarını girmesini ister.

4. **Model ve Resim Yolunu Tanımla**:  
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```  
    Bu, kullanılacak modeli belirler, belirtilen modelle bir `ChatNVIDIA` örneği oluşturur ve resim dosyasının yolunu tanımlar.

5. **Metin Komutunu Oluştur**:  
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```  
    Modelin bir resmi işlemek için Python kodu üretmesini sağlayan metin komutunu tanımlar.

6. **Resmi Base64 Formatında Kodla**:  
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```  
    Bu kod, resim dosyasını okur, base64 formatında kodlar ve kodlanmış veriyi içeren bir HTML img etiketi oluşturur.

7. **Metin ve Resmi Komutta Birleştir**:  
    ```python
    prompt = f"{text} {image}"
    ```  
    Metin komutu ve HTML img etiketi tek bir stringde birleştirilir.

8. **ChatNVIDIA ile Kod Üret**:  
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```  
    Bu kod, komutu `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` stringine gönderir.

9. **Üretilen İçerikten Python Kodunu Çıkar**:  
    ```python
    begin = code.index('```python') + 9  
    code = code[begin:]  
    end = code.index('```')
    code = code[:end]
    ```  
    Bu, markdown formatını kaldırarak gerçek Python kodunu çıkarır.

10. **Üretilen Kodu Çalıştır**:  
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```  
    Çıkarılan Python kodu bir alt süreç olarak çalıştırılır ve çıktısı yakalanır.

11. **Resimleri Göster**:  
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```  
    Bu satırlar, `IPython.display` modülünü kullanarak resimleri görüntüler.

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek herhangi bir yanlış anlama veya yanlış yorumlamadan sorumlu değiliz.