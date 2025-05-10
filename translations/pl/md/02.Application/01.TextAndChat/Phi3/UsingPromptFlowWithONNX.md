<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-05-09T18:52:36+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "pl"
}
-->
# Korzystanie z Windows GPU do tworzenia rozwiązania Prompt flow z Phi-3.5-Instruct ONNX

Poniższy dokument jest przykładem, jak używać PromptFlow z ONNX (Open Neural Network Exchange) do tworzenia aplikacji AI opartych na modelach Phi-3.

PromptFlow to zestaw narzędzi deweloperskich zaprojektowany, aby usprawnić cały cykl tworzenia aplikacji AI opartych na LLM (Large Language Model), od pomysłu i prototypowania, przez testowanie, aż po ewaluację.

Integrując PromptFlow z ONNX, deweloperzy mogą:

- Optymalizować wydajność modelu: Wykorzystać ONNX do efektywnego wnioskowania i wdrażania modeli.
- Uprościć rozwój: Korzystać z PromptFlow do zarządzania przepływem pracy i automatyzacji powtarzalnych zadań.
- Zwiększyć współpracę: Ułatwić współpracę w zespole dzięki jednolitemu środowisku deweloperskiemu.

**Prompt flow** to zestaw narzędzi deweloperskich zaprojektowany, aby usprawnić cały cykl tworzenia aplikacji AI opartych na LLM, od pomysłu, prototypowania, testowania, ewaluacji, aż po wdrożenie produkcyjne i monitorowanie. Ułatwia inżynierię promptów i pozwala tworzyć aplikacje LLM o jakości produkcyjnej.

Prompt flow może łączyć się z OpenAI, Azure OpenAI Service oraz konfigurowalnymi modelami (Huggingface, lokalne LLM/SLM). Planujemy wdrożyć kwantyzowany model ONNX Phi-3.5 do lokalnych aplikacji. Prompt flow pomoże nam lepiej zaplanować biznes i zrealizować lokalne rozwiązania oparte na Phi-3.5. W tym przykładzie połączymy ONNX Runtime GenAI Library, aby stworzyć rozwiązanie Prompt flow oparte na Windows GPU.

## **Instalacja**

### **ONNX Runtime GenAI dla Windows GPU**

Przeczytaj ten przewodnik, aby skonfigurować ONNX Runtime GenAI dla Windows GPU [kliknij tutaj](./ORTWindowGPUGuideline.md)

### **Konfiguracja Prompt flow w VSCode**

1. Zainstaluj rozszerzenie Prompt flow dla VS Code

![pfvscode](../../../../../../translated_images/pfvscode.79f42ae5dd93ed35c19d6d978ae75831fef40e0b8440ee48b893b5a0597d2260.pl.png)

2. Po instalacji rozszerzenia Prompt flow w VS Code, kliknij rozszerzenie i wybierz **Installation dependencies**, aby zgodnie z tym przewodnikiem zainstalować SDK Prompt flow w swoim środowisku

![pfsetup](../../../../../../translated_images/pfsetup.0c82d99c7760aac29833b37faf4329e67e22279b1c5f37a73724dfa9ebaa32ee.pl.png)

3. Pobierz [Przykładowy kod](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) i otwórz go w VS Code

![pfsample](../../../../../../translated_images/pfsample.7bf40b133a558d86356dd6bc0e480bad2659d9c5364823dae9b3e6784e6f2d25.pl.png)

4. Otwórz **flow.dag.yaml**, aby wybrać swoje środowisko Python

![pfdag](../../../../../../translated_images/pfdag.c5eb356fa3a96178cd594de9a5da921c4bbe646a9946f32aa20d344ccbeb51a0.pl.png)

   Otwórz **chat_phi3_ort.py**, aby zmienić lokalizację modelu Phi-3.5-instruct ONNX

![pfphi](../../../../../../translated_images/pfphi.fff4b0afea47c92c8481174dbf3092823906fca5b717fc642f78947c3e5bbb39.pl.png)

5. Uruchom swój prompt flow do testów

Otwórz **flow.dag.yaml** i kliknij edytor wizualny

![pfv](../../../../../../translated_images/pfv.7af6ecd65784a98558b344ba69b5ba6233876823fb435f163e916a632394fc1e.pl.png)

Po kliknięciu uruchom go, aby przetestować

![pfflow](../../../../../../translated_images/pfflow.9697e0fda67794bb0cf4b78d52e6f5a42002eec935bc2519933064afbbdd34f0.pl.png)

1. Możesz uruchomić batch w terminalu, aby sprawdzić więcej wyników


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Wyniki możesz sprawdzić w domyślnej przeglądarce


![pfresult](../../../../../../translated_images/pfresult.972eb57dd5bec646e1aa01148991ba8959897efea396e42cf9d7df259444878d.pl.png)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy traktować jako źródło autorytatywne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.