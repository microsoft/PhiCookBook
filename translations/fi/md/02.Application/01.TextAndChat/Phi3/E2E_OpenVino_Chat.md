<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-05-09T15:56:38+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "fi"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Tämä koodi vie mallin OpenVINO-muotoon, lataa sen ja käyttää sitä vastauksen luomiseen annettuun kehotteeseen.

1. **Mallin vienti**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Tämä komento käyttää `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **Tarvittavien kirjastojen tuonti**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Nämä rivit tuovat luokkia `transformers` library and the `optimum.intel.openvino`-moduulista, joita tarvitaan mallin lataamiseen ja käyttämiseen.

3. **Mallihakemiston ja konfiguraation määrittäminen**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` on sanakirja, joka määrittää OpenVINO-mallille prioriteetin matalalle viiveelle, yhden inferenssivirran käytön ja välimuistihakemiston pois päältä.

4. **Mallin lataaminen**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Tämä rivi lataa mallin määritetystä hakemistosta käyttäen aiemmin määriteltyjä konfiguraatioasetuksia. Se sallii myös etäkoodin suorittamisen tarvittaessa.

5. **Tokenisoijan lataaminen**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Tämä rivi lataa tokenisoijan, joka vastaa tekstin muuntamisesta mallelle ymmärrettäviksi tokeneiksi.

6. **Tokenisoijan argumenttien asettaminen**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Tämä sanakirja määrittää, ettei erityisiä tokeneita lisätä tokenisoituun tulokseen.

7. **Kehotteen määrittely**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Tämä merkkijono määrittää keskustelun kehotteen, jossa käyttäjä pyytää tekoälyavustajaa esittäytymään.

8. **Kehotteen tokenisointi**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Tämä rivi muuntaa kehotteen tokeneiksi, joita malli voi käsitellä, ja palauttaa tuloksen PyTorch-tensoreina.

9. **Vastauksen generointi**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Tämä rivi käyttää mallia vastaamaan syötettyjen tokenien perusteella, enintään 1024 uudella tokenilla.

10. **Vastauksen dekoodaus**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Tämä rivi muuntaa generoidut tokenit takaisin luettavaksi merkkijonoksi, ohittaen erityiset tokenit, ja hakee ensimmäisen tuloksen.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää auktoritatiivisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinymmärryksistä tai tulkinnoista.