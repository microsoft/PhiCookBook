<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3a1e48b628022485aac989c9f733e792",
  "translation_date": "2025-07-17T05:23:21+00:00",
  "source_file": "md/02.QuickStart/AzureAIFoundry_QuickStart.md",
  "language_code": "pl"
}
-->
# **Korzystanie z Phi-3 w Azure AI Foundry**

Wraz z rozwojem Generative AI, chcemy korzystać z zunifikowanej platformy do zarządzania różnymi LLM i SLM, integracji danych przedsiębiorstwa, operacji fine-tuningu/RAG oraz oceny różnych biznesów po integracji LLM i SLM, itp., aby generatywna AI mogła lepiej wspierać inteligentne aplikacje. [Azure AI Foundry](https://ai.azure.com) to platforma generatywnej AI na poziomie przedsiębiorstwa.

![aistudo](../../../../translated_images/aifoundry_home.f28a8127c96c7d93.pl.png)

Dzięki Azure AI Foundry możesz oceniać odpowiedzi dużych modeli językowych (LLM) oraz orkiestrację komponentów aplikacji prompt za pomocą prompt flow dla lepszej wydajności. Platforma ułatwia skalowanie, umożliwiając łatwe przekształcenie proof of concept w pełnoprawną produkcję. Ciągły monitoring i udoskonalanie wspierają długoterminowy sukces.

Możemy szybko wdrożyć model Phi-3 na Azure AI Foundry za pomocą prostych kroków, a następnie wykorzystać Azure AI Foundry do realizacji zadań związanych z Phi-3, takich jak Playground/Chat, fine-tuning, ocena i inne.

## **1. Przygotowanie**

Jeśli masz już zainstalowany [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) na swoim komputerze, korzystanie z tego szablonu jest tak proste, jak uruchomienie tej komendy w nowym katalogu.

## Ręczne tworzenie

Utworzenie projektu i huba w Microsoft Azure AI Foundry to świetny sposób na organizację i zarządzanie pracą z AI. Oto przewodnik krok po kroku, który pomoże Ci zacząć:

### Tworzenie projektu w Azure AI Foundry

1. **Przejdź do Azure AI Foundry**: Zaloguj się do portalu Azure AI Foundry.
2. **Utwórz projekt**:
   - Jeśli jesteś w projekcie, wybierz „Azure AI Foundry” w lewym górnym rogu strony, aby przejść do strony głównej.
   - Wybierz „+ Create project”.
   - Wprowadź nazwę projektu.
   - Jeśli masz hub, zostanie on wybrany domyślnie. Jeśli masz dostęp do więcej niż jednego huba, możesz wybrać inny z listy rozwijanej. Jeśli chcesz utworzyć nowy hub, wybierz „Create new hub” i podaj nazwę.
   - Wybierz „Create”.

### Tworzenie huba w Azure AI Foundry

1. **Przejdź do Azure AI Foundry**: Zaloguj się na swoje konto Azure.
2. **Utwórz hub**:
   - Wybierz Centrum zarządzania z lewego menu.
   - Wybierz „All resources”, następnie strzałkę w dół obok „+ New project” i wybierz „+ New hub”.
   - W oknie „Create a new hub” wpisz nazwę swojego huba (np. contoso-hub) i zmodyfikuj pozostałe pola według potrzeb.
   - Wybierz „Next”, sprawdź informacje, a następnie wybierz „Create”.

Szczegółowe instrukcje znajdziesz w oficjalnej [dokumentacji Microsoft](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

Po pomyślnym utworzeniu możesz uzyskać dostęp do stworzonego studia przez [ai.azure.com](https://ai.azure.com/)

Na jednym AI Foundry może być wiele projektów. Utwórz projekt w AI Foundry, aby się przygotować.

Utwórz Azure AI Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)


## **2. Wdrożenie modelu Phi w Azure AI Foundry**

Kliknij opcję Explore w projekcie, aby wejść do Model Catalog i wybierz Phi-3

Wybierz Phi-3-mini-4k-instruct

Kliknij „Deploy”, aby wdrożyć model Phi-3-mini-4k-instruct

> [!NOTE]
>
> Podczas wdrażania możesz wybrać moc obliczeniową

## **3. Playground Chat Phi w Azure AI Foundry**

Przejdź do strony wdrożenia, wybierz Playground i rozmawiaj z Phi-3 w Azure AI Foundry

## **4. Wdrażanie modelu z Azure AI Foundry**

Aby wdrożyć model z Azure Model Catalog, wykonaj następujące kroki:

- Zaloguj się do Azure AI Foundry.
- Wybierz model, który chcesz wdrożyć z katalogu modeli Azure AI Foundry.
- Na stronie Szczegóły modelu wybierz Deploy, a następnie wybierz Serverless API z Azure AI Content Safety.
- Wybierz projekt, w którym chcesz wdrożyć modele. Aby korzystać z oferty Serverless API, Twoje środowisko musi należeć do regionu East US 2 lub Sweden Central. Możesz dostosować nazwę wdrożenia.
- W kreatorze wdrożenia wybierz Pricing and terms, aby zapoznać się z cenami i warunkami użytkowania.
- Wybierz Deploy. Poczekaj, aż wdrożenie będzie gotowe i zostaniesz przekierowany na stronę Deployments.
- Wybierz Open in playground, aby rozpocząć interakcję z modelem.
- Możesz wrócić do strony Deployments, wybrać wdrożenie i zanotować adres URL endpointu (Target URL) oraz Secret Key, które możesz wykorzystać do wywoływania wdrożenia i generowania odpowiedzi.
- Szczegóły endpointu, URL i klucze dostępu znajdziesz zawsze w zakładce Build, wybierając Deployments w sekcji Components.

> [!NOTE]
> Pamiętaj, że Twoje konto musi mieć uprawnienia roli Azure AI Developer na grupie zasobów, aby wykonać te kroki.

## **5. Korzystanie z Phi API w Azure AI Foundry**

Możesz uzyskać dostęp do https://{NazwaTwojegoProjektu}.region.inference.ml.azure.com/swagger.json przez Postman GET i połączyć to z kluczem, aby poznać dostępne interfejsy.

Bardzo wygodnie możesz poznać parametry żądania oraz parametry odpowiedzi.

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.