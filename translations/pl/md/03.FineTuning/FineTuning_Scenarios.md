## Scenariusze Dostosowywania

![FineTuning with MS Services](../../../../translated_images/pl/FinetuningwithMS.3d0cec8ae693e094.webp)

Sekcja ta przedstawia przegląd scenariuszy dostosowywania (fine-tuning) w środowiskach Microsoft Foundry i Azure, w tym modele wdrożeniowe, warstwy infrastruktury oraz powszechnie stosowane techniki optymalizacji.

**Platforma**  
Obejmuje zarządzane usługi, takie jak Microsoft Foundry (dawniej Microsoft Foundry) i Azure Machine Learning, które zapewniają zarządzanie modelami, orkiestrację, śledzenie eksperymentów oraz procesy wdrożeniowe.

**Infrastruktura**  
Dostosowywanie wymaga skalowalnych zasobów obliczeniowych. W środowiskach Azure zazwyczaj obejmuje ono maszyny wirtualne z GPU oraz zasoby CPU dla lekkich zadań, wraz ze skalowalną pamięcią masową dla zbiorów danych i punktów kontrolnych.

**Narzędzia i Frameworki**  
Procesy dostosowywania często opierają się na frameworkach i bibliotekach optymalizacyjnych, takich jak Hugging Face Transformers, DeepSpeed oraz PEFT (Parameter-Efficient Fine-Tuning).

Proces dostosowywania za pomocą technologii Microsoft obejmuje usługi platformowe, infrastrukturę obliczeniową oraz frameworki treningowe. Zrozumienie, jak te elementy współdziałają, umożliwia programistom efektywne dostosowanie modeli bazowych do konkretnych zadań i scenariuszy produkcyjnych.

## Model jako Usługa

Dostosuj model korzystając z hostowanego fine-tuningu, bez konieczności tworzenia i zarządzania zasobami obliczeniowymi.

![MaaS Fine Tuning](../../../../translated_images/pl/MaaSfinetune.3eee4630607aff0d.webp)

Dostosowywanie bezserwerowe jest dostępne teraz dla rodzin modeli Phi-3, Phi-3.5 i Phi-4, umożliwiając programistom szybkie i łatwe dostosowanie modeli do scenariuszy w chmurze i na krawędzi, bez potrzeby organizowania zasobów obliczeniowych.

## Model jako Platforma

Użytkownicy zarządzają własnymi zasobami obliczeniowymi w celu dostosowania swoich modeli.

![Maap Fine Tuning](../../../../translated_images/pl/MaaPFinetune.fd3829c1122f5d1c.webp)

[Przykład Fine Tuningu](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Porównanie Technik Dostosowywania

|Scenariusz|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DoRA|
|---|---|---|---|---|---|---|
|Dostosowywanie uprzednio wytrenowanych dużych modeli językowych do konkretnych zadań lub dziedzin|Tak|Tak|Tak|Tak|Tak|Tak|
|Dostosowywanie do zadań NLP, takich jak klasyfikacja tekstu, rozpoznawanie nazwanych encji i tłumaczenie maszynowe|Tak|Tak|Tak|Tak|Tak|Tak|
|Dostosowywanie do zadań pytań i odpowiedzi (QA)|Tak|Tak|Tak|Tak|Tak|Tak|
|Dostosowywanie do generowania odpowiedzi przypominających ludzkie w chatbotach|Tak|Tak|Tak|Tak|Tak|Tak|
|Dostosowywanie do generowania muzyki, sztuki lub innych form kreatywności|Tak|Tak|Tak|Tak|Tak|Tak|
|Redukcja kosztów obliczeniowych i finansowych|Tak|Tak|Tak|Tak|Tak|Tak|
|Redukcja zużycia pamięci|Tak|Tak|Tak|Tak|Tak|Tak|
|Wykorzystanie mniejszej liczby parametrów dla efektywnego dostosowywania|Tak|Tak|Tak|Nie|Nie|Tak|
|Pamięciooszczędna forma równoległości danych dająca dostęp do łącznej pamięci GPU wszystkich dostępnych urządzeń GPU|Nie|Nie|Nie|Tak|Tak|Nie|

> [!NOTE]
> LoRA, QLoRA, PEFT i DoRA to metody efektywnego dostosowywania parametrów, podczas gdy DeepSpeed i ZeRO skupiają się na treningu rozproszonym i optymalizacji pamięci.

## Przykłady Wydajności Dostosowywania

![Finetuning Performance](../../../../translated_images/pl/Finetuningexamples.a9a41214f8f5afc1.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Dokument ten został przetłumaczony przy użyciu usługi tłumaczeń AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w wersji w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->