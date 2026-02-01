[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Msimbo huu unasafirisha mfano kwa muundo wa OpenVINO, kuupakia, na kuutumia kuunda jibu kwa ombi lililotolewa.

1. **Kusafirisha Mfano**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Amri hii inatumia zana ya `optimum-cli` kusafirisha mfano kwa muundo wa OpenVINO, ambao umeboreshwa kwa ajili ya utambuzi wa haraka.
   - Mfano unaosafirishwa ni `"microsoft/Phi-3-mini-4k-instruct"`, na umeandaliwa kwa kazi ya kuunda maandishi kulingana na muktadha wa awali.
   - Uzito wa mfano umebadilishwa kuwa nambari za 4-bit (`int4`), jambo linalosaidia kupunguza ukubwa wa mfano na kuharakisha usindikaji.
   - Vigezo vingine kama `group-size`, `ratio`, na `sym` vinatumika kuboresha mchakato wa kubadilisha uzito.
   - Mfano uliosafirishwa umehifadhiwa katika saraka `./model/phi3-instruct/int4`.

2. **Kuleta Maktaba Muhimu**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Mistari hii inaingiza madarasa kutoka maktaba ya `transformers` na moduli ya `optimum.intel.openvino`, ambayo yanahitajika kupakia na kutumia mfano.

3. **Kuweka Saraka ya Mfano na Mipangilio**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` inaeleza mahali ambapo faili za mfano zipo.
   - `ov_config` ni kamusi inayopanga mfano wa OpenVINO kuzingatia kuchelewa kidogo, kutumia mtiririko mmoja wa utambuzi, na kuto tumia saraka ya cache.

4. **Kupakia Mfano**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Mstari huu unapakua mfano kutoka saraka iliyotajwa, ukitumia mipangilio iliyowekwa awali. Pia unaruhusu utekelezaji wa msimbo wa mbali ikiwa ni lazima.

5. **Kupakia Tokenizer**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Mstari huu unapakua tokenizer, ambayo inahusika na kubadilisha maandishi kuwa tokeni ambazo mfano unaweza kuelewa.

6. **Kuweka Hoja za Tokenizer**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Kamusi hii inaeleza kwamba tokeni maalum hazitafunganywa kwenye matokeo ya tokenized.

7. **Kufafanua Ombi**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Mstari huu unaweka ombi la mazungumzo ambapo mtumiaji anaomba msaidizi wa AI kujitambulisha.

8. **Kutoa Tokeni kwa Ombi**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Mstari huu hubadilisha ombi kuwa tokeni ambazo mfano unaweza kushughulikia, na kurudisha matokeo kama tensors za PyTorch.

9. **Kuzalisha Jibu**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Mstari huu unatumia mfano kuunda jibu kulingana na tokeni za ingizo, kwa kiwango cha juu cha tokeni 1024 mpya.

10. **Kufasiri Jibu**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Mstari huu hubadilisha tokeni zilizozalishwa kurudi kuwa maandishi yanayoweza kusomwa na binadamu, akiepuka tokeni maalum, na kuchukua matokeo ya kwanza.

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.