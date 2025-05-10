<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-05-09T15:55:47+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "da"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Denne kode eksporterer en model til OpenVINO-formatet, indlæser den og bruger den til at generere et svar på en given prompt.

1. **Eksport af modellen**:  
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```  
   - Denne kommando bruger `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **Import af nødvendige biblioteker**:  
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```  
   - Disse linjer importerer klasser fra `transformers` library and the `optimum.intel.openvino` modulet, som er nødvendige for at indlæse og bruge modellen.

3. **Opsætning af modelmappe og konfiguration**:  
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```  
   - `model_dir` specifies where the model files are stored.
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
   - Denne linje indlæser modellen fra den angivne mappe og bruger de tidligere definerede konfigurationsindstillinger. Den tillader også fjernkørsel af kode, hvis nødvendigt.

5. **Indlæsning af tokenizer**:  
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```  
   - Denne linje indlæser tokenizer, som er ansvarlig for at omdanne tekst til tokens, som modellen kan forstå.

6. **Opsætning af tokenizer-argumenter**:  
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```  
   - Denne ordbog angiver, at specielle tokens ikke skal tilføjes til den tokeniserede output.

7. **Definition af prompt**:  
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```  
   - Denne streng sætter en samtaleprompt op, hvor brugeren beder AI-assistenten om at præsentere sig selv.

8. **Tokenisering af prompt**:  
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```  
   - Denne linje omdanner prompten til tokens, som modellen kan bearbejde, og returnerer resultatet som PyTorch-tensore.

9. **Generering af svar**:  
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```  
   - Denne linje bruger modellen til at generere et svar baseret på inputtokens, med et maksimum på 1024 nye tokens.

10. **Dekodning af svaret**:  
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```  
    - Denne linje omdanner de genererede tokens tilbage til en menneskeligt læsbar tekst, uden specielle tokens, og henter det første resultat.

**Ansvarsfraskrivelse**:  
Dette dokument er oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiske oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For vigtig information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.