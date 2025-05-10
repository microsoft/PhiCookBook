<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-05-09T16:02:00+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "sl"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Ta koda izvozi model v OpenVINO format, ga naloži in uporabi za generiranje odgovora na dano vprašanje.

1. **Izvoz modela**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Ta ukaz uporablja `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **Uvoz potrebnih knjižnic**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Ti ukazi uvozijo razrede iz modula `transformers` library and the `optimum.intel.openvino`, ki so potrebni za nalaganje in uporabo modela.

3. **Nastavitev imenika modela in konfiguracije**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` je slovar, ki nastavi OpenVINO model za prioriteto nizke zakasnitve, uporabo enega inferenčnega toka in brez uporabe predpomnilnika.

4. **Nalaganje modela**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Ta vrstica naloži model iz določenega imenika, pri čemer uporabi prej definirane nastavitve konfiguracije. Omogoča tudi oddaljeno izvajanje kode, če je potrebno.

5. **Nalaganje tokenizerja**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Ta vrstica naloži tokenizer, ki pretvarja besedilo v tokene, ki jih model razume.

6. **Nastavitev argumentov tokenizerja**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Ta slovar določa, da posebni tokeni ne smejo biti dodani v tokeniziran izhod.

7. **Definiranje poziva**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Ta niz nastavi pogovorni poziv, kjer uporabnik vpraša AI pomočnika, naj se predstavi.

8. **Tokenizacija poziva**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Ta vrstica pretvori poziv v tokene, ki jih model lahko obdela, in vrne rezultat kot PyTorch tenzorje.

9. **Generiranje odgovora**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Ta vrstica uporabi model za generiranje odgovora na podlagi vhodnih tokenov, z največ 1024 novimi tokeni.

10. **Dekodiranje odgovora**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Ta vrstica pretvori generirane tokene nazaj v berljiv niz, preskoči posebne tokene in pridobi prvi rezultat.

**Izjava o omejitvi odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za strojno prevajanje AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Nismo odgovorni za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.