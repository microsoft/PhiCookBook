<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-07-16T23:05:15+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "no"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Denne koden eksporterer en modell til OpenVINO-formatet, laster den inn, og bruker den til å generere et svar på en gitt prompt.

1. **Eksportere modellen**:  
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```  
   - Denne kommandoen bruker `optimum-cli`-verktøyet for å eksportere en modell til OpenVINO-formatet, som er optimalisert for effektiv inferens.  
   - Modellen som eksporteres er `"microsoft/Phi-3-mini-4k-instruct"`, og den er satt opp for oppgaven med å generere tekst basert på tidligere kontekst.  
   - Modellens vekter er kvantisert til 4-bits heltall (`int4`), noe som bidrar til å redusere modellstørrelsen og øke hastigheten på behandlingen.  
   - Andre parametere som `group-size`, `ratio` og `sym` brukes for å finjustere kvantiseringsprosessen.  
   - Den eksporterte modellen lagres i katalogen `./model/phi3-instruct/int4`.

2. **Importere nødvendige biblioteker**:  
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```  
   - Disse linjene importerer klasser fra `transformers`-biblioteket og `optimum.intel.openvino`-modulen, som trengs for å laste og bruke modellen.

3. **Sette opp modellkatalog og konfigurasjon**:  
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```  
   - `model_dir` angir hvor modellfilene er lagret.  
   - `ov_config` er en ordbok som konfigurerer OpenVINO-modellen til å prioritere lav ventetid, bruke én inferensstrøm, og ikke bruke en cache-katalog.

4. **Laste modellen**:  
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```  
   - Denne linjen laster modellen fra den angitte katalogen, med konfigurasjonsinnstillingene definert tidligere. Den tillater også fjernkjøring av kode om nødvendig.

5. **Laste tokenizer**:  
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```  
   - Denne linjen laster tokenizer, som har ansvar for å konvertere tekst til tokens som modellen kan forstå.

6. **Sette opp tokenizer-argumenter**:  
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```  
   - Denne ordboken spesifiserer at spesialtegn ikke skal legges til i den tokeniserte outputen.

7. **Definere prompten**:  
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```  
   - Denne strengen setter opp en samtaleprompt hvor brukeren ber AI-assistenten om å introdusere seg selv.

8. **Tokenisere prompten**:  
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```  
   - Denne linjen konverterer prompten til tokens som modellen kan behandle, og returnerer resultatet som PyTorch-tensorer.

9. **Generere et svar**:  
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```  
   - Denne linjen bruker modellen til å generere et svar basert på input-tokens, med en maksimal lengde på 1024 nye tokens.

10. **Dekode svaret**:  
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```  
    - Denne linjen konverterer de genererte tokens tilbake til en lesbar tekst, hopper over spesialtegn, og henter ut det første resultatet.

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.