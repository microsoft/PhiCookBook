<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-07-16T23:04:25+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "tr"
}
-->
[OpenVino Chat Örneği](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Bu kod, bir modeli OpenVINO formatına aktarır, yükler ve verilen bir isteme yanıt üretmek için kullanır.

1. **Modeli Dışa Aktarma**:  
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```  
   - Bu komut, modeli verimli çıkarım için optimize edilmiş OpenVINO formatına aktarmak için `optimum-cli` aracını kullanır.  
   - Dışa aktarılan model `"microsoft/Phi-3-mini-4k-instruct"` olup, geçmiş bağlama dayalı metin üretme görevi için ayarlanmıştır.  
   - Model ağırlıkları, model boyutunu küçültmek ve işlemi hızlandırmak için 4-bit tamsayılar (`int4`) olarak kuantize edilmiştir.  
   - `group-size`, `ratio` ve `sym` gibi diğer parametreler kuantizasyon sürecini ince ayar yapmak için kullanılır.  
   - Dışa aktarılan model `./model/phi3-instruct/int4` dizinine kaydedilir.

2. **Gerekli Kütüphaneleri İçe Aktarma**:  
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```  
   - Bu satırlar, modeli yüklemek ve kullanmak için gereken `transformers` kütüphanesinden ve `optimum.intel.openvino` modülünden sınıfları içe aktarır.

3. **Model Dizini ve Yapılandırmasını Ayarlama**:  
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```  
   - `model_dir`, model dosyalarının bulunduğu yeri belirtir.  
   - `ov_config`, OpenVINO modelinin düşük gecikmeye öncelik vermesi, tek bir çıkarım akışı kullanması ve önbellek dizini kullanmaması için yapılandırma sözlüğüdür.

4. **Modeli Yükleme**:  
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```  
   - Bu satır, daha önce tanımlanan yapılandırma ayarlarını kullanarak belirtilen dizinden modeli yükler. Gerekirse uzaktan kod çalıştırmaya da izin verir.

5. **Tokenizer'ı Yükleme**:  
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```  
   - Bu satır, metni modelin anlayabileceği tokenlara dönüştürmekten sorumlu tokenizer'ı yükler.

6. **Tokenizer Argümanlarını Ayarlama**:  
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```  
   - Bu sözlük, tokenlaştırılmış çıktıya özel tokenların eklenmemesi gerektiğini belirtir.

7. **İstemi Tanımlama**:  
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```  
   - Bu metin, kullanıcının yapay zeka asistanından kendini tanıtmasını istediği bir sohbet istemi oluşturur.

8. **İstemi Tokenlaştırma**:  
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```  
   - Bu satır, istemi modelin işleyebileceği tokenlara dönüştürür ve sonucu PyTorch tensörleri olarak döndürür.

9. **Yanıt Üretme**:  
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```  
   - Bu satır, giriş tokenlarına dayanarak modelin yanıt üretmesini sağlar, maksimum 1024 yeni token oluşturur.

10. **Yanıtı Çözümleme**:  
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```  
    - Bu satır, oluşturulan tokenları özel tokenları atlayarak insan tarafından okunabilir bir metne dönüştürür ve ilk sonucu alır.

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.