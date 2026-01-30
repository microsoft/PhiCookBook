[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Dieser Code exportiert ein Modell in das OpenVINO-Format, lädt es und verwendet es, um auf eine gegebene Eingabeaufforderung zu antworten.

1. **Modell exportieren**:  
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```  
   - Dieser Befehl nutzt das `optimum-cli`-Tool, um ein Modell in das OpenVINO-Format zu exportieren, das für effiziente Inferenz optimiert ist.  
   - Das exportierte Modell ist `"microsoft/Phi-3-mini-4k-instruct"` und ist für die Aufgabe der Texterzeugung basierend auf vorherigem Kontext ausgelegt.  
   - Die Gewichte des Modells werden auf 4-Bit-Ganzzahlen (`int4`) quantisiert, was die Modellgröße reduziert und die Verarbeitung beschleunigt.  
   - Weitere Parameter wie `group-size`, `ratio` und `sym` dienen zur Feinabstimmung des Quantisierungsprozesses.  
   - Das exportierte Modell wird im Verzeichnis `./model/phi3-instruct/int4` gespeichert.

2. **Notwendige Bibliotheken importieren**:  
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```  
   - Diese Zeilen importieren Klassen aus der `transformers`-Bibliothek und dem Modul `optimum.intel.openvino`, die zum Laden und Verwenden des Modells benötigt werden.

3. **Modellverzeichnis und Konfiguration festlegen**:  
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```  
   - `model_dir` gibt an, wo die Modelldateien gespeichert sind.  
   - `ov_config` ist ein Wörterbuch, das das OpenVINO-Modell so konfiguriert, dass es niedrige Latenz priorisiert, einen Inferenz-Stream verwendet und kein Cache-Verzeichnis nutzt.

4. **Modell laden**:  
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```  
   - Diese Zeile lädt das Modell aus dem angegebenen Verzeichnis unter Verwendung der zuvor definierten Konfiguration. Dabei wird auch die Ausführung von Remote-Code erlaubt, falls nötig.

5. **Tokenizer laden**:  
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```  
   - Diese Zeile lädt den Tokenizer, der dafür zuständig ist, Text in Tokens umzuwandeln, die das Modell verarbeiten kann.

6. **Argumente für den Tokenizer festlegen**:  
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```  
   - Dieses Wörterbuch gibt an, dass keine speziellen Tokens zum tokenisierten Output hinzugefügt werden sollen.

7. **Eingabeaufforderung definieren**:  
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```  
   - Dieser String legt eine Gesprächseingabe fest, in der der Nutzer den KI-Assistenten bittet, sich vorzustellen.

8. **Eingabeaufforderung tokenisieren**:  
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```  
   - Diese Zeile wandelt die Eingabeaufforderung in Tokens um, die das Modell verarbeiten kann, und gibt das Ergebnis als PyTorch-Tensoren zurück.

9. **Antwort generieren**:  
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```  
   - Diese Zeile verwendet das Modell, um basierend auf den Eingabetokens eine Antwort zu generieren, mit maximal 1024 neuen Tokens.

10. **Antwort decodieren**:  
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```  
    - Diese Zeile wandelt die generierten Tokens zurück in einen lesbaren Text um, überspringt dabei spezielle Tokens und gibt das erste Ergebnis zurück.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.