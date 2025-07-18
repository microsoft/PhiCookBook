<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-07-16T23:04:57+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "sv"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Den här koden exporterar en modell till OpenVINO-formatet, laddar den och använder den för att generera ett svar på en given prompt.

1. **Exportera modellen**:  
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```  
   - Det här kommandot använder verktyget `optimum-cli` för att exportera en modell till OpenVINO-formatet, vilket är optimerat för effektiv inferens.  
   - Modellen som exporteras är `"microsoft/Phi-3-mini-4k-instruct"` och är anpassad för uppgiften att generera text baserat på tidigare kontext.  
   - Modellens vikter kvantiseras till 4-bitars heltal (`int4`), vilket hjälper till att minska modellens storlek och snabba upp bearbetningen.  
   - Andra parametrar som `group-size`, `ratio` och `sym` används för att finjustera kvantiseringsprocessen.  
   - Den exporterade modellen sparas i katalogen `./model/phi3-instruct/int4`.

2. **Importera nödvändiga bibliotek**:  
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```  
   - Dessa rader importerar klasser från `transformers`-biblioteket och `optimum.intel.openvino`-modulen, som behövs för att ladda och använda modellen.

3. **Ställa in modellkatalog och konfiguration**:  
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```  
   - `model_dir` anger var modellfilerna finns.  
   - `ov_config` är en ordbok som konfigurerar OpenVINO-modellen för att prioritera låg latens, använda en inferensström och inte använda någon cachekatalog.

4. **Ladda modellen**:  
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```  
   - Den här raden laddar modellen från den angivna katalogen med de tidigare definierade konfigurationsinställningarna. Den tillåter även fjärrkörning av kod om det behövs.

5. **Ladda tokenizern**:  
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```  
   - Den här raden laddar tokenizern, som ansvarar för att omvandla text till tokens som modellen kan förstå.

6. **Ställa in argument för tokenizern**:  
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```  
   - Denna ordbok anger att specialtecken inte ska läggas till i den tokeniserade utdata.

7. **Definiera prompten**:  
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```  
   - Den här strängen sätter upp en konversationsprompt där användaren ber AI-assistenten att presentera sig själv.

8. **Tokenisera prompten**:  
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```  
   - Den här raden omvandlar prompten till tokens som modellen kan bearbeta och returnerar resultatet som PyTorch-tensorer.

9. **Generera ett svar**:  
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```  
   - Den här raden använder modellen för att generera ett svar baserat på inmatningstokens, med maximalt 1024 nya tokens.

10. **Avkoda svaret**:  
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```  
    - Den här raden omvandlar de genererade tokens tillbaka till en läsbar text, hoppar över specialtecken och hämtar det första resultatet.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål ska betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.