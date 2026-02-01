[OpenVino Chat Primjer](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Ovaj kod izvozi model u OpenVINO format, učitava ga i koristi za generiranje odgovora na zadani upit.

1. **Izvoz modela**:  
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```  
   - Ova naredba koristi alat `optimum-cli` za izvoz modela u OpenVINO format, koji je optimiziran za učinkovito izvođenje.  
   - Model koji se izvozi je `"microsoft/Phi-3-mini-4k-instruct"`, a namijenjen je zadatku generiranja teksta na temelju prethodnog konteksta.  
   - Težine modela su kvantizirane na 4-bitne cijele brojeve (`int4`), što pomaže smanjiti veličinu modela i ubrzati obradu.  
   - Ostali parametri poput `group-size`, `ratio` i `sym` koriste se za fino podešavanje procesa kvantizacije.  
   - Izvezeni model se sprema u direktorij `./model/phi3-instruct/int4`.

2. **Uvoz potrebnih biblioteka**:  
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```  
   - Ove linije uvoze klase iz biblioteke `transformers` i modula `optimum.intel.openvino`, koje su potrebne za učitavanje i korištenje modela.

3. **Postavljanje direktorija modela i konfiguracije**:  
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```  
   - `model_dir` označava gdje se nalaze datoteke modela.  
   - `ov_config` je rječnik koji konfigurira OpenVINO model da prioritizira nisku latenciju, koristi jedan tok izvođenja i ne koristi direktorij za predmemoriju.

4. **Učitavanje modela**:  
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```  
   - Ova linija učitava model iz navedenog direktorija, koristeći prethodno definirane postavke konfiguracije. Također omogućuje izvođenje udaljenog koda ako je potrebno.

5. **Učitavanje tokenizatora**:  
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```  
   - Ova linija učitava tokenizator, koji je zadužen za pretvaranje teksta u tokene koje model može razumjeti.

6. **Postavljanje argumenata za tokenizator**:  
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```  
   - Ovaj rječnik specificira da se posebni tokeni ne dodaju u tokenizirani izlaz.

7. **Definiranje upita (prompt)**:  
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```  
   - Ovaj niz postavlja razgovorni upit u kojem korisnik traži od AI asistenta da se predstavi.

8. **Tokenizacija upita**:  
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```  
   - Ova linija pretvara upit u tokene koje model može obraditi, vraćajući rezultat kao PyTorch tenzore.

9. **Generiranje odgovora**:  
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```  
   - Ova linija koristi model za generiranje odgovora na temelju ulaznih tokena, s maksimalno 1024 nova tokena.

10. **Dekodiranje odgovora**:  
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```  
    - Ova linija pretvara generirane tokene natrag u čitljiv tekst, preskačući posebne tokene, i dohvaća prvi rezultat.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za važne informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.