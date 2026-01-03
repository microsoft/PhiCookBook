<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "743d7e9cb9c4e8ea642d77bee657a7fa",
  "translation_date": "2025-07-17T09:56:20+00:00",
  "source_file": "md/03.FineTuning/LetPhi3gotoIndustriy.md",
  "language_code": "pl"
}
-->
# **Pozwól, aby Phi-3 stał się ekspertem branżowym**

Aby wdrożyć model Phi-3 w danej branży, musisz dodać do niego dane biznesowe z tej branży. Mamy dwie różne opcje: pierwsza to RAG (Retrieval Augmented Generation), a druga to Fine Tuning.

## **RAG vs Fine-Tuning**

### **Retrieval Augmented Generation**

RAG to połączenie wyszukiwania danych i generowania tekstu. Strukturalne i niestrukturalne dane przedsiębiorstwa są przechowywane w bazie wektorowej. Podczas wyszukiwania odpowiednich treści odnajduje się istotne podsumowania i zawartość, które tworzą kontekst, a następnie łączy się to z możliwością uzupełniania tekstu przez LLM/SLM, aby wygenerować treść.

### **Fine-tuning**

Fine-tuning polega na ulepszaniu konkretnego modelu. Nie wymaga rozpoczynania od algorytmu modelu, ale dane muszą być stale gromadzone. Jeśli zależy Ci na precyzyjnej terminologii i wyrażeniach językowych w zastosowaniach branżowych, fine-tuning będzie lepszym wyborem. Jednak jeśli Twoje dane często się zmieniają, fine-tuning może stać się skomplikowany.

### **Jak wybrać**

1. Jeśli nasza odpowiedź wymaga wprowadzenia danych zewnętrznych, najlepszym wyborem jest RAG.

2. Jeśli potrzebujesz stabilnej i precyzyjnej wiedzy branżowej, fine-tuning będzie dobrym wyborem. RAG skupia się na pobieraniu odpowiednich treści, ale nie zawsze trafia w specjalistyczne niuanse.

3. Fine-tuning wymaga wysokiej jakości zbioru danych, a jeśli jest to tylko niewielki zakres danych, nie przyniesie dużej różnicy. RAG jest bardziej elastyczny.

4. Fine-tuning to czarna skrzynka, coś metafizycznego, trudno zrozumieć jego wewnętrzny mechanizm. Natomiast RAG ułatwia znalezienie źródła danych, co pozwala skutecznie korygować halucynacje lub błędy w treści oraz zapewnia lepszą przejrzystość.

### **Scenariusze**

1. Branże pionowe wymagające specyficznego, profesjonalnego słownictwa i wyrażeń – ***Fine-tuning*** będzie najlepszym wyborem.

2. Systemy QA, obejmujące syntezę różnych punktów wiedzy – ***RAG*** będzie najlepszym wyborem.

3. Połączenie zautomatyzowanego przepływu biznesowego – ***RAG + Fine-tuning*** to najlepszy wybór.

## **Jak korzystać z RAG**

![rag](../../../../translated_images/rag.2014adc59e6f6007.pl.png)

Baza wektorowa to zbiór danych przechowywanych w formie matematycznej. Bazy wektorowe ułatwiają modelom uczenia maszynowego zapamiętywanie wcześniejszych danych wejściowych, co pozwala na wykorzystanie uczenia maszynowego do wspierania takich zastosowań jak wyszukiwanie, rekomendacje czy generowanie tekstu. Dane mogą być identyfikowane na podstawie metryk podobieństwa, a nie dokładnych dopasowań, co pozwala modelom komputerowym rozumieć kontekst danych.

Baza wektorowa jest kluczem do realizacji RAG. Możemy konwertować dane na przechowywanie wektorowe za pomocą modeli wektorowych, takich jak text-embedding-3, jina-ai-embedding i innych.

Dowiedz się więcej o tworzeniu aplikacji RAG [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?WT.mc_id=aiml-138114-kinfeylo)

## **Jak korzystać z Fine-tuning**

Najczęściej używane algorytmy w Fine-tuning to Lora i QLora. Jak wybrać?
- [Dowiedz się więcej z tego przykładowego notatnika](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Przykład skryptu Python FineTuning](../../../../code/04.Finetuning/FineTrainingScript.py)

### **Lora i QLora**

![lora](../../../../translated_images/qlora.e6446c988ee04ca0.pl.png)

LoRA (Low-Rank Adaptation) i QLoRA (Quantized Low-Rank Adaptation) to techniki stosowane do fine-tuningu dużych modeli językowych (LLM) z wykorzystaniem Parameter Efficient Fine Tuning (PEFT). Techniki PEFT zostały zaprojektowane, aby trenować modele bardziej efektywnie niż tradycyjne metody.

LoRA to samodzielna technika fine-tuningu, która zmniejsza zapotrzebowanie na pamięć, stosując niskorzędową aproksymację do macierzy aktualizacji wag. Oferuje szybkie czasy treningu i utrzymuje wydajność bliską tradycyjnym metodom fine-tuningu.

QLoRA to rozszerzona wersja LoRA, która wykorzystuje techniki kwantyzacji, aby jeszcze bardziej zmniejszyć zużycie pamięci. QLoRA kwantyzuje precyzję parametrów wag w wstępnie wytrenowanym LLM do precyzji 4-bitowej, co jest bardziej efektywne pamięciowo niż LoRA. Jednak trening QLoRA jest około 30% wolniejszy niż trening LoRA ze względu na dodatkowe kroki kwantyzacji i dekwantyzacji.

QLoRA wykorzystuje LoRA jako dodatek do korekty błędów wprowadzonych podczas kwantyzacji. QLoRA umożliwia fine-tuning ogromnych modeli z miliardami parametrów na stosunkowo niewielkich, powszechnie dostępnych GPU. Na przykład QLoRA może fine-tunować model 70B parametrów, który normalnie wymagałby 36 GPU, używając tylko 2.

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.