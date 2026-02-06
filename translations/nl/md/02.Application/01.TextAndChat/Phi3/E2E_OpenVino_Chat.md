[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Deze code exporteert een model naar het OpenVINO-formaat, laadt het en gebruikt het om een reactie te genereren op een gegeven prompt.

1. **Het model exporteren**:  
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```  
   - Dit commando gebruikt de `optimum-cli` tool om een model te exporteren naar het OpenVINO-formaat, dat geoptimaliseerd is voor efficiënte inferentie.  
   - Het model dat geëxporteerd wordt is `"microsoft/Phi-3-mini-4k-instruct"`, en het is ingesteld voor de taak van tekstgeneratie op basis van eerdere context.  
   - De gewichten van het model worden gequantiseerd naar 4-bits gehele getallen (`int4`), wat helpt om de modelgrootte te verkleinen en de verwerking te versnellen.  
   - Andere parameters zoals `group-size`, `ratio` en `sym` worden gebruikt om het quantisatieproces fijn af te stemmen.  
   - Het geëxporteerde model wordt opgeslagen in de map `./model/phi3-instruct/int4`.

2. **Benodigde libraries importeren**:  
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```  
   - Deze regels importeren klassen uit de `transformers` bibliotheek en de `optimum.intel.openvino` module, die nodig zijn om het model te laden en te gebruiken.

3. **Modelmap en configuratie instellen**:  
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```  
   - `model_dir` geeft aan waar de modelbestanden zijn opgeslagen.  
   - `ov_config` is een dictionary die het OpenVINO-model configureert om lage latency te prioriteren, één inferentiestroom te gebruiken en geen cachemap te gebruiken.

4. **Het model laden**:  
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```  
   - Deze regel laadt het model vanuit de opgegeven map, met gebruik van de eerder gedefinieerde configuratie-instellingen. Het staat ook toe dat er remote code uitgevoerd kan worden indien nodig.

5. **De tokenizer laden**:  
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```  
   - Deze regel laadt de tokenizer, die verantwoordelijk is voor het omzetten van tekst naar tokens die het model kan begrijpen.

6. **Tokenizer-argumenten instellen**:  
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```  
   - Deze dictionary geeft aan dat er geen speciale tokens toegevoegd moeten worden aan de getokeniseerde output.

7. **De prompt definiëren**:  
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```  
   - Deze string stelt een conversatieprompt op waarin de gebruiker de AI-assistent vraagt zich voor te stellen.

8. **De prompt tokenizen**:  
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```  
   - Deze regel zet de prompt om in tokens die het model kan verwerken, en geeft het resultaat terug als PyTorch tensors.

9. **Een reactie genereren**:  
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```  
   - Deze regel gebruikt het model om een reactie te genereren op basis van de inputtokens, met een maximum van 1024 nieuwe tokens.

10. **De reactie decoderen**:  
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```  
    - Deze regel zet de gegenereerde tokens weer om in een leesbare tekst, waarbij speciale tokens worden overgeslagen, en haalt het eerste resultaat op.

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.