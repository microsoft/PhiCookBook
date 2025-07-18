<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-07-16T23:05:25+00:00",
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
   - Tämä komento käyttää `optimum-cli`-työkalua mallin viemiseen OpenVINO-muotoon, joka on optimoitu tehokkaaseen päättelyyn.
   - Viety malli on `"microsoft/Phi-3-mini-4k-instruct"`, ja se on tarkoitettu tekstin generointitehtävään aiemman kontekstin perusteella.
   - Mallin painot kvantisoidaan 4-bittisiksi kokonaisluvuiksi (`int4`), mikä auttaa pienentämään mallin kokoa ja nopeuttamaan käsittelyä.
   - Muut parametrit kuten `group-size`, `ratio` ja `sym` hienosäätävät kvantisointiprosessia.
   - Viety malli tallennetaan hakemistoon `./model/phi3-instruct/int4`.

2. **Tarvittavien kirjastojen tuonti**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Nämä rivit tuovat luokkia `transformers`-kirjastosta ja `optimum.intel.openvino`-moduulista, joita tarvitaan mallin lataamiseen ja käyttämiseen.

3. **Mallihakemiston ja konfiguraation määrittely**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` määrittää, mistä mallin tiedostot löytyvät.
   - `ov_config` on sanakirja, joka konfiguroi OpenVINO-mallin priorisoimaan pienen viiveen, käyttämään yhtä päättelyvirtaa ja olemaan käyttämättä välimuistihakemistoa.

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

6. **Tokenisoijan argumenttien määrittely**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Tämä sanakirja määrittää, ettei tokenisoituun tulokseen lisätä erikoistokeneita.

7. **Kehotteen määrittely**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Tämä merkkijono asettaa keskustelukehotteen, jossa käyttäjä pyytää tekoälyavustajaa esittäytymään.

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
    - Tämä rivi muuntaa generoidut tokenit takaisin ihmisen luettavaksi merkkijonoksi, ohittaen erikoistokenit, ja hakee ensimmäisen tuloksen.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.