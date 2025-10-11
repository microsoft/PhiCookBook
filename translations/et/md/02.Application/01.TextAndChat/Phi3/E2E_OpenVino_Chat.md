<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-10-11T12:05:29+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "et"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

See kood ekspordib mudeli OpenVINO formaati, laadib selle ja kasutab seda vastuse genereerimiseks antud sisendile.

1. **Mudeli eksportimine**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - See käsk kasutab tööriista `optimum-cli`, et eksportida mudel OpenVINO formaati, mis on optimeeritud tõhusaks järeldamiseks.
   - Eksporditav mudel on `"microsoft/Phi-3-mini-4k-instruct"`, mis on seadistatud teksti genereerimiseks varasema konteksti põhjal.
   - Mudeli kaalud kvantiseeritakse 4-bitisteks täisarvudeks (`int4`), mis aitab vähendada mudeli suurust ja kiirendada töötlemist.
   - Muud parameetrid nagu `group-size`, `ratio` ja `sym` aitavad kvantiseerimisprotsessi täpsustada.
   - Eksporditud mudel salvestatakse kataloogi `./model/phi3-instruct/int4`.

2. **Vajalike teekide importimine**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Need read impordivad klassid teekidest `transformers` ja `optimum.intel.openvino`, mis on vajalikud mudeli laadimiseks ja kasutamiseks.

3. **Mudeli kataloogi ja konfiguratsiooni seadistamine**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` määrab, kus mudeli failid asuvad.
   - `ov_config` on sõnastik, mis konfigureerib OpenVINO mudeli madala latentsuse prioriteediks, kasutab ühte järeldusvoogu ja ei kasuta vahemälu kataloogi.

4. **Mudeli laadimine**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - See rida laadib mudeli määratud kataloogist, kasutades varem määratud konfiguratsiooniseadeid. Samuti võimaldab see vajadusel kaugkoodi täitmist.

5. **Tokeniseerija laadimine**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - See rida laadib tokeniseerija, mis vastutab teksti teisendamise eest mudeli poolt mõistetavateks tokeniteks.

6. **Tokeniseerija argumentide seadistamine**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - See sõnastik määrab, et spetsiaalseid tokeneid ei tohiks tokeniseeritud väljundisse lisada.

7. **Sisendi määratlemine**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - See string loob vestluse sisendi, kus kasutaja palub AI assistendil end tutvustada.

8. **Sisendi tokeniseerimine**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - See rida teisendab sisendi tokeniteks, mida mudel suudab töödelda, tagastades tulemuse PyTorch tensoritena.

9. **Vastuse genereerimine**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - See rida kasutab mudelit vastuse genereerimiseks sisendtokenite põhjal, maksimaalselt 1024 uue tokeniga.

10. **Vastuse dekodeerimine**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - See rida teisendab genereeritud tokenid tagasi inimloetavaks stringiks, jättes vahele kõik spetsiaalsed tokenid, ja tagastab esimese tulemuse.

---

**Vastutusest loobumine**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.