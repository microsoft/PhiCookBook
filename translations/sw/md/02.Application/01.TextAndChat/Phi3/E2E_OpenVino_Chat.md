<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-05-09T15:59:01+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "sw"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Msimbo huu unasafirisha modeli kwa muundo wa OpenVINO, kuipakia, na kuitumia kuunda jibu kwa ombi lililotolewa.

1. **Kusafirisha Modeli**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Amri hii inatumia `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **Kuleta Maktaba Muhimu**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Mistari hii inaingiza madarasa kutoka kwa moduli ya `transformers` library and the `optimum.intel.openvino`, ambayo yanahitajika kupakia na kutumia modeli.

3. **Kuweka Saraka ya Modeli na Mipangilio**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` ni kamusi inayopanga modeli ya OpenVINO ili kuzingatia ucheleweshaji mdogo, kutumia mfululizo mmoja wa inference, na kutotumia saraka ya cache.

4. **Kupakia Modeli**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Mstari huu unapakia modeli kutoka saraka iliyotajwa, ukitumia mipangilio iliyowekwa awali. Pia unaruhusu utekelezaji wa msimbo wa mbali ikiwa ni lazima.

5. **Kupakia Tokenizer**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Mstari huu unapakia tokenizer, inayohusika na kubadilisha maandishi kuwa tokens ambazo modeli inaweza kuelewa.

6. **Kuweka Hoja za Tokenizer**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Kamusi hii inaeleza kuwa tokeni maalum hazitapaswa kuongezwa kwenye matokeo ya tokenization.

7. **Kufafanua Ombi**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Mstari huu unaweka mazungumzo ambapo mtumiaji anaomba msaidizi wa AI kujitambulisha.

8. **Kutoa Tokeni kwa Ombi**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Mstari huu hubadilisha ombi kuwa tokeni ambazo modeli inaweza kushughulikia, na kurudisha matokeo kama tensors za PyTorch.

9. **Kutengeneza Jibu**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Mstari huu unatumia modeli kuunda jibu kulingana na tokeni za ingizo, kwa kiwango cha juu cha tokeni mpya 1024.

10. **Kutoa Maana ya Jibu**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Mstari huu hubadilisha tokeni zilizotengenezwa kurudi kuwa maandishi yanayosomeka na binadamu, bila kuzingatia tokeni maalum, na huchukua matokeo ya kwanza.

**Kang’aru**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upotovu. Hati ya asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha kuaminika. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.