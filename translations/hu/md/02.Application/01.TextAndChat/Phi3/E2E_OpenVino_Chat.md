[OpenVino Chat Minta](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Ez a kód egy modellt exportál OpenVINO formátumba, betölti azt, és egy adott kérésre választ generál.

1. **A modell exportálása**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Ez a parancs az `optimum-cli` eszközt használja a modell OpenVINO formátumba történő exportálásához, amely hatékonyabb futtatásra van optimalizálva.
   - Az exportálandó modell a `"microsoft/Phi-3-mini-4k-instruct"`, amely szöveg generálására van beállítva a korábbi kontextus alapján.
   - A modell súlyai 4-bites egész számokra (`int4`) vannak kvantálva, ami csökkenti a modell méretét és gyorsítja a feldolgozást.
   - Egyéb paraméterek, mint a `group-size`, `ratio` és `sym` a kvantálási folyamat finomhangolására szolgálnak.
   - Az exportált modell a `./model/phi3-instruct/int4` könyvtárba kerül mentésre.

2. **Szükséges könyvtárak importálása**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Ezek a sorok a `transformers` könyvtárból és az `optimum.intel.openvino` modulból importálnak osztályokat, amelyek a modell betöltéséhez és használatához szükségesek.

3. **A modell könyvtárának és konfigurációjának beállítása**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - A `model_dir` megadja, hol találhatók a modell fájljai.
   - Az `ov_config` egy szótár, amely az OpenVINO modellt alacsony késleltetésre, egyetlen inferencia szál használatára és cache könyvtár mellőzésére konfigurálja.

4. **A modell betöltése**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Ez a sor betölti a modellt a megadott könyvtárból, az előzőleg definiált konfigurációs beállításokkal. Szükség esetén engedélyezi a távoli kód végrehajtását is.

5. **A tokenizer betöltése**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Ez a sor betölti a tokenizálót, amely a szöveget a modell által értelmezhető tokenekre alakítja.

6. **A tokenizer argumentumainak beállítása**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Ez a szótár megadja, hogy a speciális tokenek ne kerüljenek hozzáadásra a tokenizált kimenethez.

7. **A prompt definiálása**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Ez a szöveg egy beszélgetési promptot állít be, ahol a felhasználó arra kéri az AI asszisztenst, hogy mutatkozzon be.

8. **A prompt tokenizálása**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Ez a sor a promptot tokenekre bontja, amelyeket a modell feldolgozni tud, és PyTorch tenzorokként adja vissza az eredményt.

9. **Válasz generálása**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Ez a sor a modell segítségével választ generál a bemeneti tokenek alapján, legfeljebb 1024 új tokennel.

10. **A válasz dekódolása**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Ez a sor a generált tokeneket visszaalakítja ember által olvasható szöveggé, kihagyva a speciális tokeneket, és az első eredményt adja vissza.

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.