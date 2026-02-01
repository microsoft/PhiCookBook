[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Questo codice esporta un modello nel formato OpenVINO, lo carica e lo utilizza per generare una risposta a un prompt dato.

1. **Esportazione del Modello**:  
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```  
   - Questo comando utilizza lo strumento `optimum-cli` per esportare un modello nel formato OpenVINO, ottimizzato per un'inferenza efficiente.  
   - Il modello esportato è `"microsoft/Phi-3-mini-4k-instruct"`, configurato per il compito di generare testo basato sul contesto precedente.  
   - I pesi del modello sono quantizzati a interi a 4 bit (`int4`), il che aiuta a ridurre la dimensione del modello e velocizzare l'elaborazione.  
   - Altri parametri come `group-size`, `ratio` e `sym` sono usati per affinare il processo di quantizzazione.  
   - Il modello esportato viene salvato nella directory `./model/phi3-instruct/int4`.

2. **Importazione delle Librerie Necessarie**:  
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```  
   - Queste righe importano classi dalla libreria `transformers` e dal modulo `optimum.intel.openvino`, necessarie per caricare e utilizzare il modello.

3. **Configurazione della Directory del Modello e delle Impostazioni**:  
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```  
   - `model_dir` specifica dove sono memorizzati i file del modello.  
   - `ov_config` è un dizionario che configura il modello OpenVINO per dare priorità alla bassa latenza, usare un solo flusso di inferenza e non utilizzare una directory di cache.

4. **Caricamento del Modello**:  
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```  
   - Questa riga carica il modello dalla directory specificata, utilizzando le impostazioni di configurazione definite in precedenza. Consente anche l'esecuzione di codice remoto se necessario.

5. **Caricamento del Tokenizer**:  
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```  
   - Questa riga carica il tokenizer, che si occupa di convertire il testo in token comprensibili dal modello.

6. **Configurazione degli Argomenti del Tokenizer**:  
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```  
   - Questo dizionario specifica che non devono essere aggiunti token speciali all'output tokenizzato.

7. **Definizione del Prompt**:  
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```  
   - Questa stringa imposta un prompt di conversazione in cui l'utente chiede all'assistente AI di presentarsi.

8. **Tokenizzazione del Prompt**:  
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```  
   - Questa riga converte il prompt in token che il modello può elaborare, restituendo il risultato come tensori PyTorch.

9. **Generazione di una Risposta**:  
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```  
   - Questa riga utilizza il modello per generare una risposta basata sui token di input, con un massimo di 1024 nuovi token.

10. **Decodifica della Risposta**:  
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```  
    - Questa riga converte i token generati in una stringa leggibile dall’uomo, saltando eventuali token speciali, e recupera il primo risultato.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.