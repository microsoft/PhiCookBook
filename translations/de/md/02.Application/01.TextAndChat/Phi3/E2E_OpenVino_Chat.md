<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-05-07T11:05:18+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "de"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Dieser Code exportiert ein Modell in das OpenVINO-Format, lädt es und verwendet es, um auf eine gegebene Eingabeaufforderung zu antworten.

1. **Modell exportieren**:  
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```  
   - Dieser Befehl verwendet `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **Notwendige Bibliotheken importieren**:  
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```  
   - Diese Zeilen importieren Klassen aus dem Modul `transformers` library and the `optimum.intel.openvino`, die benötigt werden, um das Modell zu laden und zu verwenden.

3. **Modellverzeichnis und Konfiguration einrichten**:  
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```  
   - `model_dir` specifies where the model files are stored.
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
   - Diese Zeile lädt das Modell aus dem angegebenen Verzeichnis und verwendet die zuvor definierten Konfigurationseinstellungen. Dabei wird bei Bedarf auch die Ausführung von Remote-Code erlaubt.

5. **Tokenizer laden**:  
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```  
   - Diese Zeile lädt den Tokenizer, der dafür zuständig ist, Text in Tokens umzuwandeln, die das Modell verstehen kann.

6. **Argumente für den Tokenizer festlegen**:  
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```  
   - Dieses Wörterbuch gibt an, dass keine speziellen Tokens zum tokenisierten Ergebnis hinzugefügt werden sollen.

7. **Eingabeaufforderung definieren**:  
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```  
   - Dieser String legt eine Gesprächseingabe fest, in der der Benutzer den KI-Assistenten bittet, sich vorzustellen.

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
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir auf Genauigkeit achten, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.