<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-09-12T14:29:23+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "lt"
}
-->
[OpenVino Chat Pavyzdys](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Šis kodas eksportuoja modelį į OpenVINO formatą, įkelia jį ir naudoja atsakymui į pateiktą užklausą generuoti.

1. **Modelio Eksportavimas**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Ši komanda naudoja `optimum-cli` įrankį modelio eksportavimui į OpenVINO formatą, kuris optimizuotas efektyviam inferencijai.
   - Eksportuojamas modelis yra `"microsoft/Phi-3-mini-4k-instruct"`, ir jis pritaikytas tekstui generuoti remiantis ankstesniu kontekstu.
   - Modelio svoriai yra kvantizuoti iki 4 bitų sveikųjų skaičių (`int4`), kas padeda sumažinti modelio dydį ir pagreitinti apdorojimą.
   - Kiti parametrai, tokie kaip `group-size`, `ratio` ir `sym`, naudojami kvantizacijos proceso optimizavimui.
   - Eksportuotas modelis išsaugomas kataloge `./model/phi3-instruct/int4`.

2. **Reikalingų Bibliotekų Importavimas**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Šios eilutės importuoja klases iš `transformers` bibliotekos ir `optimum.intel.openvino` modulio, kurie reikalingi modelio įkėlimui ir naudojimui.

3. **Modelio Katalogo ir Konfigūracijos Nustatymas**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` nurodo, kur saugomi modelio failai.
   - `ov_config` yra žodynas, kuris konfigūruoja OpenVINO modelį, kad būtų prioritetizuojamas mažas vėlavimas, naudojama viena inferencijos srauto linija ir nenaudojamas talpyklos katalogas.

4. **Modelio Įkėlimas**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Ši eilutė įkelia modelį iš nurodyto katalogo, naudojant anksčiau apibrėžtus konfigūracijos nustatymus. Ji taip pat leidžia nuotolinį kodo vykdymą, jei reikia.

5. **Tokenizatoriaus Įkėlimas**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Ši eilutė įkelia tokenizatorių, kuris atsakingas už teksto konvertavimą į tokenus, kuriuos modelis gali suprasti.

6. **Tokenizatoriaus Argumentų Nustatymas**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Šis žodynas nurodo, kad specialūs tokenai neturėtų būti pridedami prie tokenizuoto rezultato.

7. **Užklausos Nustatymas**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Ši eilutė sukuria pokalbio užklausą, kurioje vartotojas prašo AI asistento prisistatyti.

8. **Užklausos Tokenizavimas**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Ši eilutė konvertuoja užklausą į tokenus, kuriuos modelis gali apdoroti, ir grąžina rezultatą kaip PyTorch tensorius.

9. **Atsakymo Generavimas**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Ši eilutė naudoja modelį atsakymui generuoti, remiantis įvesties tokenais, su maksimaliu 1024 naujų tokenų skaičiumi.

10. **Atsakymo Dekodavimas**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Ši eilutė konvertuoja sugeneruotus tokenus atgal į žmogui suprantamą tekstą, praleidžiant specialius tokenus, ir grąžina pirmą rezultatą.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.