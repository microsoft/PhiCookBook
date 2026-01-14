<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7b4235159486df4000e16b7b46ddfec3",
  "translation_date": "2025-07-16T22:31:00+00:00",
  "source_file": "md/01.Introduction/05/AIFoundry.md",
  "language_code": "pl"
}
-->
# **Korzystanie z Azure AI Foundry do oceny**

![aistudo](../../../../../translated_images/pl/AIFoundry.9e0b513e999a1c5a.png)

Jak ocenić swoją aplikację generatywnej AI za pomocą [Azure AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo). Niezależnie od tego, czy analizujesz rozmowy jednokrotne, czy wielokrotne, Azure AI Foundry oferuje narzędzia do oceny wydajności i bezpieczeństwa modeli.

![aistudo](../../../../../translated_images/pl/AIPortfolio.69da59a8e1eaa70f.png)

## Jak ocenić aplikacje generatywnej AI za pomocą Azure AI Foundry
Szczegółowe instrukcje znajdziesz w [dokumentacji Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

Oto kroki, aby zacząć:

## Ocena modeli generatywnej AI w Azure AI Foundry

**Wymagania wstępne**

- Zestaw testowy w formacie CSV lub JSON.
- Wdrożony model generatywnej AI (np. Phi-3, GPT 3.5, GPT 4 lub modele Davinci).
- Środowisko uruchomieniowe z instancją obliczeniową do przeprowadzenia oceny.

## Wbudowane metryki oceny

Azure AI Foundry pozwala oceniać zarówno rozmowy jednokrotne, jak i złożone, wielokrotne.
W scenariuszach Retrieval Augmented Generation (RAG), gdzie model opiera się na konkretnych danych, możesz ocenić wydajność za pomocą wbudowanych metryk.
Dodatkowo, możesz ocenić ogólne scenariusze jednokrotnego odpowiadania na pytania (poza RAG).

## Tworzenie sesji oceny

W interfejsie Azure AI Foundry przejdź do strony Evaluate lub Prompt Flow.
Postępuj zgodnie z kreatorem tworzenia oceny, aby skonfigurować sesję oceny. Możesz podać opcjonalną nazwę dla swojej oceny.
Wybierz scenariusz odpowiadający celom Twojej aplikacji.
Wybierz jedną lub więcej metryk oceny do analizy wyników modelu.

## Niestandardowy przepływ oceny (opcjonalnie)

Dla większej elastyczności możesz stworzyć niestandardowy przepływ oceny. Dostosuj proces oceny do swoich indywidualnych potrzeb.

## Przeglądanie wyników

Po przeprowadzeniu oceny zaloguj się, przeglądaj i analizuj szczegółowe metryki oceny w Azure AI Foundry. Uzyskaj wgląd w możliwości i ograniczenia swojej aplikacji.

**Note** Azure AI Foundry jest obecnie w publicznej wersji zapoznawczej, dlatego używaj go do eksperymentów i rozwoju. Do zastosowań produkcyjnych rozważ inne opcje. Zapoznaj się z oficjalną [dokumentacją AI Foundry](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo) po więcej szczegółów i instrukcji krok po kroku.

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy traktować jako źródło wiarygodne i ostateczne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.