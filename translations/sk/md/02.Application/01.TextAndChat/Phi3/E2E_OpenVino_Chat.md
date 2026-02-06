[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Tento kód exportuje model do formátu OpenVINO, načíta ho a použije na generovanie odpovede na zadaný prompt.

1. **Export modelu**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Tento príkaz používa nástroj `optimum-cli` na export modelu do formátu OpenVINO, ktorý je optimalizovaný pre efektívne inferovanie.
   - Exportovaný model je `"microsoft/Phi-3-mini-4k-instruct"` a je určený na úlohu generovania textu na základe predchádzajúceho kontextu.
   - Váhy modelu sú kvantizované na 4-bitové celé čísla (`int4`), čo pomáha zmenšiť veľkosť modelu a zrýchliť spracovanie.
   - Ďalšie parametre ako `group-size`, `ratio` a `sym` slúžia na doladenie procesu kvantizácie.
   - Exportovaný model je uložený v adresári `./model/phi3-instruct/int4`.

2. **Import potrebných knižníc**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Tieto riadky importujú triedy z knižnice `transformers` a modulu `optimum.intel.openvino`, ktoré sú potrebné na načítanie a použitie modelu.

3. **Nastavenie adresára modelu a konfigurácie**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` určuje, kde sú uložené súbory modelu.
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
   - Tento riadok načíta model zo zadaného adresára s použitím predtým definovaných konfiguračných nastavení. Tiež umožňuje vykonávanie vzdialeného kódu, ak je to potrebné.

5. **Načítanie tokenizéra**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Tento riadok načíta tokenizér, ktorý je zodpovedný za prevod textu na tokeny, ktoré model dokáže spracovať.

6. **Nastavenie argumentov tokenizéra**:
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
   - Tento riadok prevádza prompt na tokeny, ktoré model dokáže spracovať, a vracia výsledok ako PyTorch tenzory.

9. **Generovanie odpovede**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Tento riadok používa model na generovanie odpovede na základe vstupných tokenov, s maximálnym počtom 1024 nových tokenov.

10. **Dekódovanie odpovede**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Tento riadok prevádza vygenerované tokeny späť na čitateľný text, vynecháva špeciálne tokeny a získava prvý výsledok.

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.