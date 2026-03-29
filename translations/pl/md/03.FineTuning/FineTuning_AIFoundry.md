# Dostosowywanie Phi-3 za pomocą Microsoft Foundry

Poznajmy, jak dostosować model językowy Phi-3 Mini firmy Microsoft, korzystając z Microsoft Foundry. Dostosowywanie pozwala przystosować Phi-3 Mini do konkretnych zadań, czyniąc go jeszcze bardziej efektywnym i świadomym kontekstu.

## Wskazówki

- **Możliwości:** Które modele można dostosowywać? Do czego można dostosować model bazowy?
- **Koszty:** Jaki jest model wyceniania dostosowywania?
- **Możliwość dostosowania:** Jak bardzo mogę modyfikować model bazowy – i w jaki sposób?
- **Wygoda:** Jak przebiega dostosowywanie – czy muszę pisać własny kod? Czy muszę zapewnić własne zasoby obliczeniowe?
- **Bezpieczeństwo:** Dostrajane modele mają potencjalne ryzyko bezpieczeństwa – czy istnieją zabezpieczenia chroniące przed niezamierzonymi szkodami?

![AIFoundry Models](../../../../translated_images/pl/AIFoundryModels.0e1b16f7d0b09b73.webp)

## Przygotowanie do dostosowywania

### Wymagania wstępne

> [!NOTE]
> Dla modeli z rodziny Phi-3, oferta dostosowywania w modelu płatności zgodnie z użyciem jest dostępna wyłącznie dla hubów utworzonych w regionach **East US 2**.

- Subskrypcja Azure. Jeśli nie masz subskrypcji Azure, utwórz [płatne konto Azure](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go), aby zacząć.

- Projekt [AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- Do przyznawania dostępu do operacji w Microsoft Foundry używane są kontrole dostępu oparte na rolach Azure (Azure RBAC). Aby wykonać kroki w tym artykule, twoje konto użytkownika musi mieć przypisaną __rolę Azure AI Developer__ na grupie zasobów.

### Rejestracja dostawcy subskrypcji

Sprawdź, czy subskrypcja jest zarejestrowana dla dostawcy zasobów `Microsoft.Network`.

1. Zaloguj się do [portalu Azure](https://portal.azure.com).
1. Wybierz **Subskrypcje** z lewego menu.
1. Wybierz subskrypcję, której chcesz użyć.
1. Wybierz **Ustawienia projektu AI** > **Dostawcy zasobów** z lewego menu.
1. Potwierdź, że **Microsoft.Network** jest na liście dostawców zasobów. W przeciwnym razie dodaj go.

### Przygotowanie danych

Przygotuj dane treningowe i walidacyjne do dostosowania modelu. Twoje zbiory danych treningowych i walidacyjnych składają się z przykładów wejścia i wyjścia, pokazujących, jak chcesz, aby model działał.

Upewnij się, że wszystkie przykłady treningowe są zgodne z oczekiwanym formatem do inferencji. Aby skutecznie dostosować modele, zapewnij zrównoważony i różnorodny zbiór danych.

Oznacza to utrzymywanie równowagi danych, uwzględnianie różnych scenariuszy oraz okresowe dopracowywanie danych treningowych, aby odpowiadały rzeczywistym oczekiwaniom, co ostatecznie prowadzi do dokładniejszych i bardziej zrównoważonych odpowiedzi modelu.

Różne typy modeli wymagają różnego formatu danych treningowych.

### Chat Completion

Dane treningowe i walidacyjne, które używasz, **muszą** być sformatowane jako dokument JSON Lines (JSONL). Dla `Phi-3-mini-128k-instruct` zestaw danych do dostosowywania musi być sformatowany w formacie konwersacyjnym, używanym przez API Chat completions.

### Przykładowy format pliku

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

Obsługiwany typ pliku to JSON Lines. Pliki są przesyłane do domyślnego magazynu i udostępniane w twoim projekcie.

## Dostosowywanie Phi-3 za pomocą Microsoft Foundry

Microsoft Foundry pozwala dostosowywać duże modele językowe do twoich własnych zbiorów danych, korzystając z procesu znanego jako fine-tuning. Dostosowywanie daje znaczną wartość, umożliwiając personalizację i optymalizację pod kątem konkretnych zadań i zastosowań. Skutkuje to lepszą wydajnością, efektywnością kosztową, mniejszą latencją oraz dopasowanymi wynikami.

![Finetune AI Foundry](../../../../translated_images/pl/AIFoundryfinetune.193aaddce48d553c.webp)

### Utwórz nowy projekt

1. Zaloguj się do [Microsoft Foundry](https://ai.azure.com).

1. Wybierz **+Nowy projekt**, aby utworzyć nowy projekt w Microsoft Foundry.

    ![FineTuneSelect](../../../../translated_images/pl/select-new-project.cd31c0404088d7a3.webp)

1. Wykonaj następujące czynności:

    - Nazwa huba projektu (**Hub name**). Musi to być unikatowa nazwa.
    - Wybierz **Hub**, którego chcesz użyć (w razie potrzeby utwórz nowy).

    ![FineTuneSelect](../../../../translated_images/pl/create-project.ca3b71298b90e420.webp)

1. Wykonaj następujące czynności, aby utworzyć nowy hub:

    - Wpisz nazwę huba (**Hub name**). Musi to być unikatowa nazwa.
    - Wybierz subskrypcję Azure (**Subscription**).
    - Wybierz grupę zasobów (**Resource group**), której chcesz użyć (utwórz nową, jeśli to konieczne).
    - Wybierz lokalizację (**Location**), której chcesz użyć.
    - Wybierz usługę Azure AI, z którą chcesz się połączyć (**Connect Azure AI Services**) (utwórz nową, jeśli to konieczne).
    - Wybierz **Connect Azure AI Search** i wybierz opcję **Pomiń łączenie**.

    ![FineTuneSelect](../../../../translated_images/pl/create-hub.49e53d235e80779e.webp)

1. Kliknij **Dalej**.
1. Kliknij **Utwórz projekt**.

### Przygotowanie danych

Przed dostosowaniem zbierz lub utwórz zbiór danych istotny dla twojego zadania, na przykład instrukcje czatu, pary pytań i odpowiedzi lub inne odpowiednie dane tekstowe. Wyczyść i przetwórz dane, usuwając zakłócenia, obsługując brakujące wartości oraz dokonując tokenizacji tekstu.

### Dostosuj modele Phi-3 w Microsoft Foundry

> [!NOTE]
> Dostosowywanie modeli Phi-3 jest obecnie obsługiwane tylko w projektach zlokalizowanych w regionie East US 2.

1. Wybierz **Katalog modeli** z zakładki po lewej stronie.

1. Wpisz *phi-3* w polu **wyszukiwania** i wybierz model phi-3, którego chcesz użyć.

    ![FineTuneSelect](../../../../translated_images/pl/select-model.60ef2d4a6a3cec57.webp)

1. Wybierz **Dostosuj (Fine-tune)**.

    ![FineTuneSelect](../../../../translated_images/pl/select-finetune.a976213b543dd9d8.webp)

1. Wpisz nazwę **dostosowanego modelu**.

    ![FineTuneSelect](../../../../translated_images/pl/finetune1.c2b39463f0d34148.webp)

1. Kliknij **Dalej**.

1. Wykonaj następujące kroki:

    - Wybierz typ zadania (**task type**) jako **Chat completion**.
    - Wybierz dane treningowe, których chcesz użyć. Możesz je przesłać przez dane Microsoft Foundry albo z lokalnego środowiska.

    ![FineTuneSelect](../../../../translated_images/pl/finetune2.43cb099b1a94442d.webp)

1. Kliknij **Dalej**.

1. Prześlij dane walidacyjne, których chcesz użyć, lub wybierz **Automatyczne podzielenie danych treningowych**.

    ![FineTuneSelect](../../../../translated_images/pl/finetune3.fd96121b67dcdd92.webp)

1. Kliknij **Dalej**.

1. Wykonaj następujące kroki:

    - Wybierz współczynnik mnożnik wielkości partii (**Batch size multiplier**).
    - Wybierz współczynnik uczenia się (**Learning rate**).
    - Wybierz liczbę epok treningowych (**Epochs**).

    ![FineTuneSelect](../../../../translated_images/pl/finetune4.e18b80ffccb5834a.webp)

1. Kliknij **Zatwierdź (Submit)**, aby rozpocząć proces dostosowywania.

    ![FineTuneSelect](../../../../translated_images/pl/select-submit.0a3802d581bac271.webp)

1. Po zakończeniu dostosowywania, status będzie widoczny jako **Completed**, jak pokazano na poniższym obrazku. Teraz możesz wdrożyć model i używać go w swojej aplikacji, w środowisku testowym (playground) lub w prompt flow. Więcej informacji znajdziesz w [Jak wdrożyć rodzinę modeli językowych Phi-3 za pomocą Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![FineTuneSelect](../../../../translated_images/pl/completed.4dc8d2357144cdef.webp)

> [!NOTE]
> Aby uzyskać więcej szczegółów o dostosowywaniu Phi-3, odwiedź [Dostosowywanie modeli Phi-3 w Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini).

## Usuwanie dostosowanych modeli

Możesz usunąć dostosowany model z listy modeli dostosowywanych w [Microsoft Foundry](https://ai.azure.com) lub ze strony szczegółów modelu. Wybierz model dostosowany do usunięcia na stronie dostosowywania, a następnie kliknij przycisk usuń.

> [!NOTE]
> Nie możesz usunąć modelu niestandardowego jeśli istnieje jego wdrożenie. Musisz najpierw usunąć wdrożenie modelu, aby móc usunąć model niestandardowy.

## Koszty i limity

### Koszty i limity dla modeli Phi-3 dostosowywanych jako usługa

Modele Phi dostosowywane jako usługa są oferowane przez Microsoft i zintegrowane z Microsoft Foundry do użytku. Ceny można znaleźć podczas [wdrażania](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) lub dostosowywania modeli, w zakładce Cena i warunki w kreatorze wdrażania.

## Filtrowanie treści

Modele wdrażane jako usługa w modelu "pay-as-you-go" są chronione przez Azure AI Content Safety. Po wdrożeniu na punkty końcowe w czasie rzeczywistym, możesz zrezygnować z tej możliwości. Z włączoną ochroną treści Azure AI, zarówno polecenie (prompt), jak i wygenerowana odpowiedź przechodzą przez zestaw modeli klasyfikacyjnych, które mają na celu wykrywanie i zapobieganie generowaniu szkodliwych treści. System filtrowania treści wykrywa i podejmuje działania względem określonych kategorii potencjalnie szkodliwych treści zarówno w danych wejściowych, jak i wyjściowych. Dowiedz się więcej o [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering).

**Konfiguracja dostosowywania**

Hyperparametry: Definiuj hiperparametry takie jak współczynnik uczenia, wielkość partii i liczba epok treningowych.

**Funkcja straty**

Wybierz odpowiednią funkcję straty dla swojego zadania (np. entropię krzyżową).

**Optymalizator**

Wybierz optymalizator (np. Adam) do aktualizacji gradientów podczas treningu.

**Proces dostosowywania**

- Załaduj model wytrenowany wstępnie: załaduj checkpoint Phi-3 Mini.
- Dodaj warstwy niestandardowe: dodaj warstwy specyficzne dla zadania (np. warstwę klasyfikacyjną dla instrukcji czatu).

**Trenuj model**

Dostosuj model przy użyciu przygotowanego zbioru danych. Monitoruj postępy treningu i w razie potrzeby dostosowuj hiperparametry.

**Ewaluacja i walidacja**

Zestaw walidacyjny: Podziel dane na zestawy treningowe i walidacyjne.

**Oceń wydajność**

Używaj metryk takich jak dokładność, F1-score lub perplexity, aby ocenić wydajność modelu.

## Zapisz dostosowany model

**Checkpoint**

Zapisz checkpoint dostosowanego modelu do przyszłego użytku.

## Wdrażanie

- Wdróż jako usługę internetową: wdroż dostosowany model jako usługę webową w Microsoft Foundry.
- Przetestuj punkt końcowy: wyślij testowe zapytania do wdrożonego punktu końcowego, aby zweryfikować jego działanie.

## Iteruj i ulepszaj

Iteruj: jeśli wyniki nie są zadowalające, iteruj, dostosowując hiperparametry, dodając więcej danych lub trenując przez kolejne epoki.

## Monitoruj i dopracowuj

Monitoruj nieustannie zachowanie modelu i dopracowuj go w razie potrzeby.

## Dostosuj i rozszerzaj

Zadania niestandardowe: Phi-3 Mini można dostosowywać do różnych zadań poza instrukcjami czatu. Eksploruj inne zastosowania!
Eksperymentuj: Wypróbuj różne architektury, kombinacje warstw i techniki, by podnieść wydajność.

> [!NOTE]
> Dostosowywanie to proces iteracyjny. Eksperymentuj, ucz się i dostosowuj model, aby osiągnąć najlepsze wyniki dla swojego konkretnego zadania!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub niedokładności. Oryginalny dokument w języku macierzystym powinien być uważany za źródło wiarygodne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->