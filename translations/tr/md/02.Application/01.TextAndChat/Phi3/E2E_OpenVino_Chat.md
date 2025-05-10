<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-05-09T15:54:20+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "tr"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Bu kod, bir modeli OpenVINO formatına dışa aktarır, yükler ve verilen bir prompta yanıt üretmek için kullanır.

1. **Modeli Dışa Aktarma**:  
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```  
   - Bu komut, `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4` kullanır.

2. **Gerekli Kütüphaneleri İçe Aktarma**:  
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```  
   - Bu satırlar, modeli yüklemek ve kullanmak için gereken `transformers` library and the `optimum.intel.openvino` modülünden sınıfları içe aktarır.

3. **Model Dizini ve Konfigürasyonunu Ayarlama**:  
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```  
   - `model_dir` specifies where the model files are stored.
   - `ov_config` OpenVINO modelinin düşük gecikmeyi önceliklendirmesini, tek bir çıkarım akışı kullanmasını ve önbellek dizini kullanmamasını sağlayan bir sözlüktür.

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
   - Bu satır, daha önce tanımlanan konfigürasyon ayarlarını kullanarak belirtilen dizinden modeli yükler. Gerekirse uzaktan kod çalıştırmaya da izin verir.

5. **Tokenizer’ı Yükleme**:  
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```  
   - Bu satır, metni modelin anlayabileceği tokenlara dönüştürmekten sorumlu olan tokenizer’ı yükler.

6. **Tokenizer Argümanlarını Ayarlama**:  
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```  
   - Bu sözlük, tokenize edilen çıktıya özel tokenların eklenmemesi gerektiğini belirtir.

7. **Prompt’u Tanımlama**:  
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```  
   - Bu string, kullanıcının yapay zeka asistanına kendini tanıtmasını istediği bir konuşma promptu oluşturur.

8. **Prompt’u Tokenize Etme**:  
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```  
   - Bu satır, prompt’u modelin işleyebileceği tokenlara dönüştürür ve sonucu PyTorch tensörleri olarak döner.

9. **Yanıt Üretme**:  
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```  
   - Bu satır, giriş tokenlarına dayanarak modelin yanıt üretmesini sağlar, maksimum 1024 yeni token oluşturur.

10. **Yanıtı Decode Etme**:  
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```  
    - Bu satır, oluşturulan tokenları özel tokenları atlayarak insan tarafından okunabilir bir metne çevirir ve ilk sonucu alır.

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Orijinal belge, kendi ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.