# **Używanie Microsoft Foundry do oceny**

![aistudo](../../../../../translated_images/pl/AIFoundry.9e0b513e999a1c5a.webp)

Jak ocenić swoją aplikację generatywnej sztucznej inteligencji za pomocą [Microsoft Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo). Niezależnie od tego, czy oceniasz konwersacje jednorundowe czy wielorundowe, Microsoft Foundry oferuje narzędzia do oceny wydajności i bezpieczeństwa modelu.

![aistudo](../../../../../translated_images/pl/AIPortfolio.69da59a8e1eaa70f.webp)

## Jak ocenić aplikacje generatywnej AI za pomocą Microsoft Foundry
Szczegółowe instrukcje znajdziesz w [dokumentacji Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

Oto kroki do rozpoczęcia:

## Ocena modeli generatywnej AI w Microsoft Foundry

**Wymagania wstępne**

- Zbiór danych testowych w formacie CSV lub JSON.
- Wdrożony model generatywnej AI (np. Phi-3, GPT 3.5, GPT 4 lub modele Davinci).
- Środowisko wykonawcze z instancją obliczeniową do przeprowadzenia oceny.

## Wbudowane metryki oceny

Microsoft Foundry pozwala ocenić zarówno konwersacje jednorundowe, jak i złożone, wielorundowe.
Dla scenariuszy Retrieval Augmented Generation (RAG), w których model opiera się na konkretnych danych, możesz ocenić wydajność za pomocą wbudowanych metryk oceny.
Dodatkowo, możesz ocenić ogólne scenariusze zadawania pytań jednorundowych (bez RAG).

## Tworzenie sesji oceny

W interfejsie Microsoft Foundry przejdź do strony Evaluate lub Prompt Flow.
Postępuj zgodnie z kreatorem tworzenia oceny, aby ustawić sesję oceny. Podaj opcjonalną nazwę dla swojej oceny.
Wybierz scenariusz odpowiadający celom twojej aplikacji.
Wybierz jedną lub więcej metryk oceny do oceny wyników modelu.

## Niestandardowy przebieg oceny (opcjonalnie)

Dla większej elastyczności możesz utworzyć niestandardowy przebieg oceny. Dostosuj proces oceny do swoich wymagań.

## Przeglądanie wyników

Po przeprowadzeniu oceny zaloguj się, wyświetl i analizuj szczegółowe metryki oceny w Microsoft Foundry. Uzyskaj wgląd w możliwości i ograniczenia swojej aplikacji.

**Note** Microsoft Foundry jest obecnie w publicznej wersji zapoznawczej, więc używaj go do eksperymentów i celów rozwojowych. Do zadań produkcyjnych rozważ inne opcje. Zapoznaj się z oficjalną [dokumentacją AI Foundry](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo) po więcej szczegółów i instrukcji krok po kroku.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w języku źródłowym powinien być traktowany jako autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->