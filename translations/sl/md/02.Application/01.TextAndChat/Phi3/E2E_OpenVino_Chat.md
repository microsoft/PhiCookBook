<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-07-16T23:07:55+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "sl"
}
-->
[OpenVino Chat Primer](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Ta koda izvozi model v OpenVINO format, ga naloži in uporabi za generiranje odgovora na dano vprašanje.

1. **Izvoz modela**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Ta ukaz uporablja orodje `optimum-cli` za izvoz modela v OpenVINO format, ki je optimiziran za učinkovito sklepanje.
   - Model, ki se izvaža, je `"microsoft/Phi-3-mini-4k-instruct"` in je nastavljen za nalogo generiranja besedila na podlagi preteklega konteksta.
   - Teže modela so kvantizirane na 4-bitne cele števke (`int4`), kar pomaga zmanjšati velikost modela in pospešiti obdelavo.
   - Drugi parametri, kot so `group-size`, `ratio` in `sym`, se uporabljajo za natančnejše nastavljanje procesa kvantizacije.
   - Izvoženi model je shranjen v imenik `./model/phi3-instruct/int4`.

2. **Uvoz potrebnih knjižnic**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Ti ukazi uvozijo razrede iz knjižnice `transformers` in modula `optimum.intel.openvino`, ki so potrebni za nalaganje in uporabo modela.

3. **Nastavitev imenika modela in konfiguracije**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` določa, kje so shranjene datoteke modela.
   - `ov_config` je slovar, ki konfigurira OpenVINO model za prednost nizke zakasnitve, uporabo enega toka sklepanja in neuporabo predpomnilnika.

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
   - Ta vrstica naloži model iz določenega imenika z uporabo prej definiranih nastavitev konfiguracije. Prav tako omogoča izvajanje oddaljene kode, če je potrebno.

5. **Nalaganje tokenizerja**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Ta vrstica naloži tokenizer, ki je odgovoren za pretvorbo besedila v tokene, ki jih model lahko razume.

6. **Nastavitev argumentov tokenizerja**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Ta slovar določa, da se posebni tokeni ne dodajajo v tokeniziran izhod.

7. **Definiranje poziva (prompt)**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Ta niz nastavi pogovorni poziv, kjer uporabnik prosi AI asistenta, naj se predstavi.

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
    - Ta vrstica pretvori generirane tokene nazaj v berljiv niz, pri čemer preskoči posebne tokene, in pridobi prvi rezultat.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.