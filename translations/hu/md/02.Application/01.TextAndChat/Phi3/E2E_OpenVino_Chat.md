<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-05-09T15:59:20+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "hu"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Ez a kód egy modellt exportál OpenVINO formátumba, betölti azt, és használja, hogy választ generáljon egy adott kérdésre.

1. **A modell exportálása**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Ez a parancs az `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4` használatával exportál.

2. **Szükséges könyvtárak importálása**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Ezek a sorok a `transformers` library and the `optimum.intel.openvino` modulból importálnak osztályokat, amelyek szükségesek a modell betöltéséhez és használatához.

3. **A modell könyvtár és konfiguráció beállítása**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - A `model_dir` specifies where the model files are stored.
   - `ov_config` egy szótár, amely az OpenVINO modellt úgy konfigurálja, hogy alacsony késleltetésű legyen, egyetlen inferencia szálat használjon, és ne használjon gyorsítótár könyvtárat.

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
   - Ez a sor betölti a modellt a megadott könyvtárból, a korábban definiált konfigurációs beállításokat használva. Szükség esetén engedélyezi a távoli kód végrehajtást is.

5. **A tokenizáló betöltése**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Ez a sor betölti a tokenizálót, amely a szöveget olyan tokenekre alakítja, amelyeket a modell értelmezni tud.

6. **Tokenizáló argumentumok beállítása**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Ez a szótár meghatározza, hogy ne adjon hozzá speciális tokeneket a tokenizált kimenethez.

7. **A prompt meghatározása**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Ez a szöveg egy beszélgetés kezdetét állítja be, ahol a felhasználó arra kéri az AI asszisztenst, hogy mutatkozzon be.

8. **A prompt tokenizálása**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Ez a sor a promptot tokenekre alakítja, amelyeket a modell feldolgozni tud, és az eredményt PyTorch tenzorként adja vissza.

9. **Válasz generálása**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Ez a sor a modellt használva generál választ a bemeneti tokenek alapján, legfeljebb 1024 új tokennel.

10. **A válasz dekódolása**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Ez a sor a generált tokeneket ember számára olvasható szöveggé alakítja vissza, kihagyva a speciális tokeneket, és az első eredményt veszi.

**Jogi nyilatkozat**:  
Ezt a dokumentumot az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.