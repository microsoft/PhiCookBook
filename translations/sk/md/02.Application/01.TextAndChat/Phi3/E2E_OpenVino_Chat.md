<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-05-09T16:00:11+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "sk"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Tento kód exportuje model do formátu OpenVINO, načíta ho a použije na generovanie odpovede na zadaný prompt.

1. **Export modelu**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Tento príkaz používa `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **Import potrebných knižníc**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Tieto riadky importujú triedy z modulu `transformers` library and the `optimum.intel.openvino`, ktoré sú potrebné na načítanie a použitie modelu.

3. **Nastavenie adresára modelu a konfigurácie**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` je slovník, ktorý konfiguruje OpenVINO model tak, aby uprednostňoval nízku latenciu, používal jeden inference stream a nepoužíval cache adresár.

4. **Načítanie modelu**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Tento riadok načíta model zo špecifikovaného adresára s použitím predtým definovaných konfiguračných nastavení. Tiež povoľuje vzdialené spúšťanie kódu, ak je to potrebné.

5. **Načítanie tokenizeru**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Tento riadok načíta tokenizer, ktorý je zodpovedný za prevod textu na tokeny, ktoré model dokáže spracovať.

6. **Nastavenie argumentov tokenizeru**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Tento slovník špecifikuje, že do tokenizovaného výstupu sa nemajú pridávať špeciálne tokeny.

7. **Definovanie promptu**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Tento reťazec nastavuje konverzačný prompt, kde používateľ žiada AI asistenta, aby sa predstavil.

8. **Tokenizácia promptu**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Tento riadok prevádza prompt na tokeny, ktoré model dokáže spracovať, a vracia výsledok ako PyTorch tensory.

9. **Generovanie odpovede**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Tento riadok používa model na generovanie odpovede na základe vstupných tokenov s maximálnym počtom 1024 nových tokenov.

10. **Dekódovanie odpovede**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Tento riadok prevádza vygenerované tokeny späť na čitateľný text, preskakuje špeciálne tokeny a vyberá prvý výsledok.

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, berte prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.