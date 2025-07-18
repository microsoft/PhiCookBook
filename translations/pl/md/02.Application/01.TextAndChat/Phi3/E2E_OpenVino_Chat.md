<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-07-16T23:04:16+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "pl"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Ten kod eksportuje model do formatu OpenVINO, ładuje go i używa do wygenerowania odpowiedzi na podany prompt.

1. **Eksportowanie modelu**:  
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```  
   - To polecenie używa narzędzia `optimum-cli` do eksportu modelu do formatu OpenVINO, który jest zoptymalizowany pod kątem wydajnego wnioskowania.  
   - Eksportowany model to `"microsoft/Phi-3-mini-4k-instruct"`, przygotowany do zadania generowania tekstu na podstawie wcześniejszego kontekstu.  
   - Wagi modelu są kwantyzowane do 4-bitowych liczb całkowitych (`int4`), co pomaga zmniejszyć rozmiar modelu i przyspieszyć przetwarzanie.  
   - Inne parametry, takie jak `group-size`, `ratio` i `sym`, służą do precyzyjnego dostrojenia procesu kwantyzacji.  
   - Wyeksportowany model jest zapisywany w katalogu `./model/phi3-instruct/int4`.

2. **Importowanie niezbędnych bibliotek**:  
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```  
   - Te linie importują klasy z biblioteki `transformers` oraz modułu `optimum.intel.openvino`, które są potrzebne do załadowania i użycia modelu.

3. **Konfiguracja katalogu modelu i ustawień**:  
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```  
   - `model_dir` określa, gdzie znajdują się pliki modelu.  
   - `ov_config` to słownik konfigurujący model OpenVINO tak, aby priorytetem była niska latencja, użycie jednego strumienia inferencji oraz brak katalogu cache.

4. **Ładowanie modelu**:  
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```  
   - Ta linia ładuje model z określonego katalogu, korzystając z wcześniej zdefiniowanych ustawień konfiguracyjnych. Pozwala również na zdalne wykonywanie kodu, jeśli jest to konieczne.

5. **Ładowanie tokenizera**:  
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```  
   - Ta linia ładuje tokenizer, który odpowiada za konwersję tekstu na tokeny zrozumiałe dla modelu.

6. **Konfiguracja argumentów tokenizera**:  
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```  
   - Ten słownik określa, że do tokenizowanego tekstu nie powinny być dodawane specjalne tokeny.

7. **Definiowanie promptu**:  
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```  
   - Ten ciąg znaków ustawia prompt konwersacji, w którym użytkownik prosi asystenta AI o przedstawienie się.

8. **Tokenizacja promptu**:  
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```  
   - Ta linia konwertuje prompt na tokeny, które model może przetworzyć, zwracając wynik jako tensory PyTorch.

9. **Generowanie odpowiedzi**:  
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```  
   - Ta linia używa modelu do wygenerowania odpowiedzi na podstawie podanych tokenów, z maksymalną długością 1024 nowych tokenów.

10. **Dekodowanie odpowiedzi**:  
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```  
    - Ta linia konwertuje wygenerowane tokeny z powrotem na czytelny tekst, pomijając specjalne tokeny, i pobiera pierwszy wynik.

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.