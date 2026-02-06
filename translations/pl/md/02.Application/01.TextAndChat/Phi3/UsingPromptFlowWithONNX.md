# Używanie Windows GPU do tworzenia rozwiązania Prompt flow z Phi-3.5-Instruct ONNX

Poniższy dokument jest przykładem, jak używać PromptFlow z ONNX (Open Neural Network Exchange) do tworzenia aplikacji AI opartych na modelach Phi-3.

PromptFlow to zestaw narzędzi deweloperskich zaprojektowany, aby usprawnić cały cykl tworzenia aplikacji AI opartych na LLM (Large Language Model), od pomysłu i prototypowania, przez testowanie, aż po ewaluację.

Integrując PromptFlow z ONNX, deweloperzy mogą:

- Optymalizować wydajność modelu: Wykorzystać ONNX do efektywnego wnioskowania i wdrażania modeli.
- Uprościć rozwój: Korzystać z PromptFlow do zarządzania przepływem pracy i automatyzacji powtarzalnych zadań.
- Zwiększyć współpracę: Ułatwić współpracę w zespole, zapewniając zunifikowane środowisko deweloperskie.

**Prompt flow** to zestaw narzędzi deweloperskich, który usprawnia cały cykl tworzenia aplikacji AI opartych na LLM, od pomysłu, prototypowania, testowania, ewaluacji, aż po wdrożenie produkcyjne i monitorowanie. Ułatwia inżynierię promptów i pozwala tworzyć aplikacje LLM o jakości produkcyjnej.

Prompt flow może łączyć się z OpenAI, Azure OpenAI Service oraz modelami konfigurowalnymi (Huggingface, lokalne LLM/SLM). Planujemy wdrożyć kwantyzowany model ONNX Phi-3.5 do aplikacji lokalnych. Prompt flow pomoże nam lepiej zaplanować biznes i zrealizować lokalne rozwiązania oparte na Phi-3.5. W tym przykładzie połączymy ONNX Runtime GenAI Library, aby stworzyć rozwiązanie Prompt flow oparte na Windows GPU.

## **Instalacja**

### **ONNX Runtime GenAI dla Windows GPU**

Przeczytaj tę instrukcję, aby skonfigurować ONNX Runtime GenAI dla Windows GPU [kliknij tutaj](./ORTWindowGPUGuideline.md)

### **Konfiguracja Prompt flow w VSCode**

1. Zainstaluj rozszerzenie Prompt flow do VS Code

![pfvscode](../../../../../../translated_images/pl/pfvscode.eff93dfc66a42cbe.webp)

2. Po zainstalowaniu rozszerzenia Prompt flow w VS Code, kliknij rozszerzenie i wybierz **Installation dependencies**, aby zgodnie z instrukcją zainstalować Prompt flow SDK w swoim środowisku

![pfsetup](../../../../../../translated_images/pl/pfsetup.b46e93096f5a254f.webp)

3. Pobierz [Przykładowy kod](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) i otwórz go w VS Code

![pfsample](../../../../../../translated_images/pl/pfsample.8d89e70584ffe7c4.webp)

4. Otwórz **flow.dag.yaml**, aby wybrać swoje środowisko Python

![pfdag](../../../../../../translated_images/pl/pfdag.264a77f7366458ff.webp)

   Otwórz **chat_phi3_ort.py**, aby zmienić lokalizację modelu Phi-3.5-instruct ONNX

![pfphi](../../../../../../translated_images/pl/pfphi.72da81d74244b45f.webp)

5. Uruchom swój prompt flow do testów

Otwórz **flow.dag.yaml** i kliknij edytor wizualny

![pfv](../../../../../../translated_images/pl/pfv.ba8a81f34b20f603.webp)

Po kliknięciu uruchom go, aby przetestować

![pfflow](../../../../../../translated_images/pl/pfflow.4e1135a089b1ce1b.webp)

1. Możesz uruchomić batch w terminalu, aby zobaczyć więcej wyników


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Wyniki możesz sprawdzić w domyślnej przeglądarce


![pfresult](../../../../../../translated_images/pl/pfresult.c22c826f8062d7cb.webp)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.