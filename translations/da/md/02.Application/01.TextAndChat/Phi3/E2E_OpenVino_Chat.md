[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Denne kode eksporterer en model til OpenVINO-formatet, indlæser den og bruger den til at generere et svar på en given prompt.

1. **Eksport af modellen**:  
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```  
   - Denne kommando bruger `optimum-cli` værktøjet til at eksportere en model til OpenVINO-formatet, som er optimeret til effektiv inferens.  
   - Modellen, der eksporteres, er `"microsoft/Phi-3-mini-4k-instruct"`, og den er sat op til opgaven med at generere tekst baseret på tidligere kontekst.  
   - Modellens vægte kvantiseres til 4-bit heltal (`int4`), hvilket hjælper med at reducere modelstørrelsen og øge hastigheden.  
   - Andre parametre som `group-size`, `ratio` og `sym` bruges til at finjustere kvantiseringen.  
   - Den eksporterede model gemmes i mappen `./model/phi3-instruct/int4`.

2. **Import af nødvendige biblioteker**:  
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```  
   - Disse linjer importerer klasser fra `transformers` biblioteket og `optimum.intel.openvino` modulet, som er nødvendige for at indlæse og bruge modellen.

3. **Opsætning af modelmappe og konfiguration**:  
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```  
   - `model_dir` angiver, hvor model-filerne er gemt.  
   - `ov_config` er en ordbog, der konfigurerer OpenVINO-modellen til at prioritere lav latenstid, bruge én inferensstrøm og ikke bruge en cache-mappe.

4. **Indlæsning af modellen**:  
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```  
   - Denne linje indlæser modellen fra den angivne mappe med de tidligere definerede konfigurationsindstillinger. Den tillader også fjernudførelse af kode, hvis nødvendigt.

5. **Indlæsning af tokenizer**:  
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```  
   - Denne linje indlæser tokenizeren, som er ansvarlig for at omdanne tekst til tokens, som modellen kan forstå.

6. **Opsætning af tokenizer-argumenter**:  
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```  
   - Denne ordbog angiver, at der ikke skal tilføjes specialtegn til den tokeniserede output.

7. **Definition af prompten**:  
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```  
   - Denne tekst sætter en samtaleprompt op, hvor brugeren beder AI-assistenten om at præsentere sig selv.

8. **Tokenisering af prompten**:  
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```  
   - Denne linje omdanner prompten til tokens, som modellen kan behandle, og returnerer resultatet som PyTorch-tensore.

9. **Generering af svar**:  
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```  
   - Denne linje bruger modellen til at generere et svar baseret på input-tokens med op til 1024 nye tokens.

10. **Dekodning af svaret**:  
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```  
    - Denne linje omdanner de genererede tokens tilbage til en menneskelig læsbar tekst, uden specialtegn, og henter det første resultat.

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.