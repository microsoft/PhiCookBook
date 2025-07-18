<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-07-16T23:06:57+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "cs"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Tento kód exportuje model do formátu OpenVINO, načte ho a použije k vygenerování odpovědi na zadaný prompt.

1. **Export modelu**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Tento příkaz používá nástroj `optimum-cli` k exportu modelu do formátu OpenVINO, který je optimalizovaný pro efektivní inferenci.
   - Exportovaný model je `"microsoft/Phi-3-mini-4k-instruct"` a je určený pro úlohu generování textu na základě předchozího kontextu.
   - Váhy modelu jsou kvantizovány na 4bitové celé čísla (`int4`), což pomáhá zmenšit velikost modelu a urychlit zpracování.
   - Další parametry jako `group-size`, `ratio` a `sym` slouží k doladění procesu kvantizace.
   - Exportovaný model je uložen v adresáři `./model/phi3-instruct/int4`.

2. **Import potřebných knihoven**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Tyto řádky importují třídy z knihovny `transformers` a modulu `optimum.intel.openvino`, které jsou potřeba k načtení a použití modelu.

3. **Nastavení adresáře modelu a konfigurace**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` určuje, kde jsou uloženy soubory modelu.
   - `ov_config` je slovník, který konfiguruje OpenVINO model tak, aby upřednostňoval nízkou latenci, používal jeden inference stream a nepoužíval cache adresář.

4. **Načtení modelu**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Tento řádek načte model z určeného adresáře s použitím dříve definovaných konfiguračních nastavení. Také umožňuje vzdálené spuštění kódu, pokud je to potřeba.

5. **Načtení tokenizeru**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Tento řádek načte tokenizer, který převádí text na tokeny, které model dokáže zpracovat.

6. **Nastavení argumentů tokenizeru**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Tento slovník určuje, že do tokenizovaného výstupu by neměly být přidávány speciální tokeny.

7. **Definování promptu**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Tento řetězec nastavuje konverzační prompt, ve kterém uživatel žádá AI asistenta, aby se představil.

8. **Tokenizace promptu**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Tento řádek převádí prompt na tokeny, které model může zpracovat, a vrací výsledek jako PyTorch tensory.

9. **Generování odpovědi**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Tento řádek používá model k vygenerování odpovědi na základě vstupních tokenů, s maximálním počtem 1024 nových tokenů.

10. **Dekódování odpovědi**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Tento řádek převádí vygenerované tokeny zpět na čitelný text, přeskočí speciální tokeny a získá první výsledek.

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.