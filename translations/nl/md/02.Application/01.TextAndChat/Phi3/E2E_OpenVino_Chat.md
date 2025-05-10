<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-05-09T15:56:59+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "nl"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Deze code exporteert een model naar het OpenVINO-formaat, laadt het en gebruikt het om een reactie te genereren op een gegeven prompt.

1. **Het model exporteren**:  
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```  
   - Dit commando gebruikt de `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **Benodigde libraries importeren**:  
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```  
   - Deze regels importeren klassen uit de `transformers` library and the `optimum.intel.openvino` module, die nodig zijn om het model te laden en te gebruiken.

3. **Modelmap en configuratie instellen**:  
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```  
   - `model_dir` specifies where the model files are stored.
   - `ov_config` is een dictionary die het OpenVINO-model configureert om lage latency te prioriteren, één inference-stream te gebruiken en geen cache-directory te gebruiken.

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
   - Deze regel laadt het model vanuit de opgegeven map, met gebruik van de eerder gedefinieerde configuratie-instellingen. Het staat ook remote code-uitvoering toe indien nodig.

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
   - Deze dictionary geeft aan dat er geen speciale tokens aan de getokenizeerde output toegevoegd moeten worden.

7. **De prompt definiëren**:  
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```  
   - Deze string zet een conversatieprompt op waarin de gebruiker de AI-assistent vraagt zichzelf voor te stellen.

8. **De prompt tokenizen**:  
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```  
   - Deze regel zet de prompt om in tokens die het model kan verwerken, en retourneert het resultaat als PyTorch-tensors.

9. **Een reactie genereren**:  
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```  
   - Deze regel gebruikt het model om een reactie te genereren op basis van de inputtokens, met een maximum van 1024 nieuwe tokens.

10. **De reactie decoderen**:  
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```  
    - Deze regel zet de gegenereerde tokens terug om naar een leesbare tekst, waarbij speciale tokens worden overgeslagen, en haalt het eerste resultaat op.

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onjuistheden kunnen bevatten. Het oorspronkelijke document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.