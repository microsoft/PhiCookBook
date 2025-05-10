<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cb5648935f63edc17e95ce38f23adc32",
  "translation_date": "2025-05-09T21:55:11+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Scenarios.md",
  "language_code": "pl"
}
-->
## Scenariusze Fine Tuningu

![FineTuning with MS Services](../../../../translated_images/FinetuningwithMS.25759a0154a97ad90e43a6cace37d6bea87f0ac0236ada3ad5d4a1fbacc3bdf7.pl.png)

**Platforma** Obejmuje różne technologie, takie jak Azure AI Foundry, Azure Machine Learning, AI Tools, Kaito oraz ONNX Runtime.

**Infrastruktura** Obejmuje CPU i FPGA, które są niezbędne do procesu fine tuningu. Pokażę Ci ikony dla każdej z tych technologii.

**Narzędzia i Frameworki** Obejmuje ONNX Runtime i ONNX Runtime. Pokażę Ci ikony dla każdej z tych technologii.  
[Wstaw ikony dla ONNX Runtime i ONNX Runtime]

Proces fine tuningu z wykorzystaniem technologii Microsoft obejmuje różne komponenty i narzędzia. Dzięki zrozumieniu i wykorzystaniu tych technologii możemy skutecznie dopracowywać nasze aplikacje i tworzyć lepsze rozwiązania.

## Model jako usługa

Dopasuj model za pomocą hostowanego fine tuningu, bez konieczności tworzenia i zarządzania zasobami obliczeniowymi.

![MaaS Fine Tuning](../../../../translated_images/MaaSfinetune.6184d80a336ea9d7bb67a581e9e5d0b021cafdffff7ba257c2012e2123e0d77e.pl.png)

Bezserwerowy fine tuning jest dostępny dla modeli Phi-3-mini i Phi-3-medium, umożliwiając deweloperom szybkie i łatwe dostosowanie modeli do scenariuszy chmurowych i edge bez konieczności organizowania zasobów obliczeniowych. Ogłosiliśmy również, że Phi-3-small jest teraz dostępny w ramach oferty Models-as-a-Service, dzięki czemu deweloperzy mogą szybko i łatwo rozpocząć rozwój AI bez konieczności zarządzania infrastrukturą.

## Model jako platforma

Użytkownicy zarządzają własnymi zasobami obliczeniowymi, aby dopasować swoje modele.

![Maap Fine Tuning](../../../../translated_images/MaaPFinetune.cf8b08ef05bf57f362da90834be87562502f4370de4a7325a9fb03b8c008e5e7.pl.png)

[Przykład Fine Tuningu](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Scenariusze Fine Tuningu

| | | | | | | |
|-|-|-|-|-|-|-|
|Scenariusz|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DORA|
|Dostosowanie wstępnie wytrenowanych LLM do konkretnych zadań lub dziedzin|Tak|Tak|Tak|Tak|Tak|Tak|
|Fine tuning dla zadań NLP, takich jak klasyfikacja tekstu, rozpoznawanie nazwanych encji i tłumaczenie maszynowe|Tak|Tak|Tak|Tak|Tak|Tak|
|Fine tuning dla zadań QA|Tak|Tak|Tak|Tak|Tak|Tak|
|Fine tuning do generowania odpowiedzi przypominających ludzkie w chatbotach|Tak|Tak|Tak|Tak|Tak|Tak|
|Fine tuning do generowania muzyki, sztuki lub innych form kreatywności|Tak|Tak|Tak|Tak|Tak|Tak|
|Zmniejszenie kosztów obliczeniowych i finansowych|Tak|Tak|Nie|Tak|Tak|Nie|
|Zmniejszenie zużycia pamięci|Nie|Tak|Nie|Tak|Tak|Tak|
|Użycie mniejszej liczby parametrów dla efektywnego fine tuningu|Nie|Tak|Tak|Nie|Nie|Tak|
|Pamięciooszczędna forma paralelizmu danych, która daje dostęp do łącznej pamięci GPU wszystkich dostępnych urządzeń GPU|Nie|Nie|Nie|Tak|Tak|Tak|

## Przykłady wydajności Fine Tuningu

![Finetuning Performance](../../../../translated_images/Finetuningexamples.9dbf84557eef43e011eb7cadf51f51686f9245f7953e2712a27095ab7d18a6d1.pl.png)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu automatycznej usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do jak największej dokładności, prosimy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub niedokładności. Oryginalny dokument w języku źródłowym powinien być uznawany za wiarygodne źródło informacji. W przypadku istotnych informacji zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.