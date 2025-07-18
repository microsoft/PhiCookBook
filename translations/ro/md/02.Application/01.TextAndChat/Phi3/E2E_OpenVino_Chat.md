<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-07-16T23:07:17+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "ro"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Acest cod exportă un model în format OpenVINO, îl încarcă și îl folosește pentru a genera un răspuns la un prompt dat.

1. **Exportarea Modelului**:  
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```  
   - Această comandă folosește instrumentul `optimum-cli` pentru a exporta un model în format OpenVINO, optimizat pentru inferență eficientă.  
   - Modelul exportat este `"microsoft/Phi-3-mini-4k-instruct"` și este configurat pentru generarea de text pe baza contextului anterior.  
   - Greutățile modelului sunt cuantificate la întregi pe 4 biți (`int4`), ceea ce ajută la reducerea dimensiunii modelului și la accelerarea procesării.  
   - Alți parametri precum `group-size`, `ratio` și `sym` sunt folosiți pentru a ajusta procesul de cuantificare.  
   - Modelul exportat este salvat în directorul `./model/phi3-instruct/int4`.

2. **Importarea Bibliotecilor Necesare**:  
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```  
   - Aceste linii importă clase din biblioteca `transformers` și modulul `optimum.intel.openvino`, necesare pentru încărcarea și utilizarea modelului.

3. **Configurarea Directorului Modelului și a Setărilor**:  
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```  
   - `model_dir` specifică locația fișierelor modelului.  
   - `ov_config` este un dicționar care configurează modelul OpenVINO pentru a prioritiza latența scăzută, a folosi un singur flux de inferență și a nu utiliza un director cache.

4. **Încărcarea Modelului**:  
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```  
   - Această linie încarcă modelul din directorul specificat, folosind setările de configurare definite anterior. De asemenea, permite executarea codului de la distanță dacă este necesar.

5. **Încărcarea Tokenizer-ului**:  
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```  
   - Această linie încarcă tokenizer-ul, responsabil pentru convertirea textului în tokeni pe care modelul îi poate înțelege.

6. **Configurarea Argumentelor pentru Tokenizer**:  
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```  
   - Acest dicționar specifică faptul că tokenii speciali nu trebuie adăugați la rezultatul tokenizării.

7. **Definirea Promptului**:  
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```  
   - Acest șir configurează un prompt de conversație în care utilizatorul îi cere asistentului AI să se prezinte.

8. **Tokenizarea Promptului**:  
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```  
   - Această linie convertește promptul în tokeni pe care modelul îi poate procesa, returnând rezultatul ca tensori PyTorch.

9. **Generarea unui Răspuns**:  
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```  
   - Această linie folosește modelul pentru a genera un răspuns bazat pe tokenii de intrare, cu un maxim de 1024 tokeni noi.

10. **Decodarea Răspunsului**:  
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```  
    - Această linie convertește tokenii generați înapoi într-un șir lizibil de oameni, sărind peste tokenii speciali, și preia primul rezultat.

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.