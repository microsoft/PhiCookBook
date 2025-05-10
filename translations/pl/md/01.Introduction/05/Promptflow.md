<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cbe7629d254f1043193b7fe22524d55",
  "translation_date": "2025-05-09T15:10:26+00:00",
  "source_file": "md/01.Introduction/05/Promptflow.md",
  "language_code": "pl"
}
-->
# **Wprowadzenie do Promptflow**

[Microsoft Prompt Flow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=aiml-138114-kinfeylo) to wizualne narzędzie do automatyzacji przepływów pracy, które pozwala użytkownikom tworzyć zautomatyzowane procesy korzystając z gotowych szablonów i niestandardowych konektorów. Zostało zaprojektowane tak, aby umożliwić programistom i analitykom biznesowym szybkie budowanie zautomatyzowanych procesów do zadań takich jak zarządzanie danymi, współpraca czy optymalizacja procesów. Dzięki Prompt Flow użytkownicy mogą łatwo łączyć różne usługi, aplikacje i systemy oraz automatyzować złożone procesy biznesowe.

Microsoft Prompt Flow ma na celu usprawnienie pełnego cyklu rozwoju aplikacji AI opartych na dużych modelach językowych (LLM). Niezależnie od tego, czy tworzysz pomysły, prototypujesz, testujesz, oceniasz czy wdrażasz aplikacje oparte na LLM, Prompt Flow upraszcza cały proces i pozwala tworzyć aplikacje LLM o jakości produkcyjnej.

## Oto kluczowe funkcje i zalety korzystania z Microsoft Prompt Flow:

**Interaktywne środowisko tworzenia**

Prompt Flow oferuje wizualną reprezentację struktury przepływu, co ułatwia zrozumienie i poruszanie się po projektach.  
Zapewnia doświadczenie podobne do notatnika, co sprzyja efektywnemu tworzeniu i debugowaniu przepływów.

**Warianty i dostrajanie promptów**

Twórz i porównuj różne warianty promptów, aby ułatwić iteracyjny proces ich ulepszania. Oceń skuteczność różnych promptów i wybierz te najefektywniejsze.

**Wbudowane przepływy oceny**  
Oceniaj jakość i skuteczność swoich promptów i przepływów za pomocą wbudowanych narzędzi oceniających.  
Zrozum, jak dobrze działają Twoje aplikacje oparte na LLM.

**Kompleksowe zasoby**

Prompt Flow zawiera bibliotekę wbudowanych narzędzi, przykładów i szablonów. Te zasoby stanowią punkt wyjścia do tworzenia, inspirują kreatywność i przyspieszają proces.

**Współpraca i gotowość dla przedsiębiorstw**

Wspieraj współpracę zespołową, umożliwiając wielu użytkownikom pracę nad projektami inżynierii promptów.  
Zachowuj kontrolę wersji i skutecznie dziel się wiedzą. Usprawnij cały proces inżynierii promptów – od tworzenia i oceny po wdrożenie i monitorowanie.

## Ocena w Prompt Flow

W Microsoft Prompt Flow ocena odgrywa kluczową rolę w analizie wydajności modeli AI. Sprawdźmy, jak można dostosować przepływy oceny i metryki w Prompt Flow:

![PFVizualise](../../../../../translated_images/pfvisualize.93c453890f4088830217fa7308b1a589058ed499bbfff160c85676066b5cbf2d.pl.png)

**Zrozumienie oceny w Prompt Flow**

W Prompt Flow przepływ to sekwencja węzłów, które przetwarzają dane wejściowe i generują wyjścia. Przepływy oceniające to specjalne rodzaje przepływów, które służą do oceny wydajności uruchomienia na podstawie określonych kryteriów i celów.

**Kluczowe cechy przepływów oceniających**

Zazwyczaj uruchamiają się po przepływie testowanym, wykorzystując jego wyniki. Obliczają wyniki lub metryki, które mierzą skuteczność testowanego przepływu. Metryki mogą obejmować dokładność, oceny trafności lub inne odpowiednie wskaźniki.

### Dostosowywanie przepływów oceniających

**Definiowanie wejść**

Przepływy oceniające muszą przyjmować wyniki uruchomienia testowanego przepływu. Definiuj wejścia podobnie jak w standardowych przepływach.  
Na przykład, jeśli oceniasz przepływ QnA, nazwij wejście "answer". Jeśli oceniasz przepływ klasyfikacji, nazwij wejście "category". Mogą być również potrzebne wejścia z prawdziwymi etykietami (ground truth).

**Wyjścia i metryki**

Przepływy oceniające generują wyniki mierzące skuteczność testowanego przepływu. Metryki można obliczać za pomocą Pythona lub LLM. Używaj funkcji log_metric() do rejestrowania odpowiednich metryk.

**Korzystanie z dostosowanych przepływów oceniających**

Stwórz własny przepływ oceniający dopasowany do swoich konkretnych zadań i celów. Dostosuj metryki w zależności od celów oceny.  
Zastosuj ten dostosowany przepływ oceniający do wsadowych uruchomień w celu testów na dużą skalę.

## Wbudowane metody oceny

Prompt Flow oferuje również wbudowane metody oceny.  
Możesz uruchamiać wsadowe testy i korzystać z tych metod, aby ocenić, jak dobrze działa Twój przepływ na dużych zbiorach danych.  
Przeglądaj wyniki oceny, porównuj metryki i wprowadzaj poprawki według potrzeby.  
Pamiętaj, że ocena jest kluczowa, aby upewnić się, że Twoje modele AI spełniają założone kryteria i cele. Zapoznaj się z oficjalną dokumentacją, aby uzyskać szczegółowe instrukcje dotyczące tworzenia i używania przepływów oceniających w Microsoft Prompt Flow.

Podsumowując, Microsoft Prompt Flow umożliwia programistom tworzenie wysokiej jakości aplikacji LLM, upraszczając inżynierię promptów i oferując solidne środowisko rozwojowe. Jeśli pracujesz z LLM, Prompt Flow to wartościowe narzędzie warte poznania. Zapoznaj się z [Prompt Flow Evaluation Documents](https://learn.microsoft.com/azure/machine-learning/prompt-flow/how-to-develop-an-evaluation-flow?view=azureml-api-2?WT.mc_id=aiml-138114-kinfeylo), aby uzyskać szczegółowe instrukcje dotyczące tworzenia i stosowania przepływów oceniających w Microsoft Prompt Flow.

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku źródłowym powinien być traktowany jako źródło wiarygodne. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.