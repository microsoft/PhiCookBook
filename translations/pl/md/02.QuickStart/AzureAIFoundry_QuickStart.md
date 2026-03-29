# **Używanie Phi-3 w Microsoft Foundry**

Wraz z rozwojem generatywnej sztucznej inteligencji mamy nadzieję wykorzystać zunifikowaną platformę do zarządzania różnymi LLM i SLM, integracji danych przedsiębiorstwa, operacji dostrajania/RAG oraz oceny różnych przedsiębiorstw po integracji LLM i SLM, itp., tak aby generatywna sztuczna inteligencja mogła być lepiej wykorzystywana w inteligentnych aplikacjach. [Microsoft Foundry](https://ai.azure.com) to platforma do tworzenia aplikacji generatywnej AI na poziomie przedsiębiorstwa.

![aistudo](../../../../translated_images/pl/aifoundry_home.f28a8127c96c7d93.webp)

Dzięki Microsoft Foundry możesz oceniać odpowiedzi dużych modeli językowych (LLM) oraz organizować komponenty aplikacji prompt za pomocą prompt flow dla lepszej wydajności. Platforma ułatwia skalowanie, umożliwiając łatwe przekształcenie proof of concepts w pełnoprawną produkcję. Ciągły monitoring i ulepszanie wspierają długoterminowy sukces.

Możemy szybko wdrożyć model Phi-3 w Microsoft Foundry za pomocą prostych kroków, a następnie wykorzystać Microsoft Foundry do realizacji powiązanych z Phi-3 działań takich jak Playground/Chat, dostrajanie, ocena i inne powiązane prace.

## **1. Przygotowanie**

Jeśli masz już zainstalowany [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) na swoim komputerze, korzystanie z tego szablonu jest tak proste, jak uruchomienie tego polecenia w nowym katalogu.

## Ręczne tworzenie

Tworzenie projektu i huba w Microsoft Foundry to świetny sposób na organizację i zarządzanie pracą AI. Oto przewodnik krok po kroku, który pomoże Ci zacząć:

### Tworzenie projektu w Microsoft Foundry

1. **Przejdź do Microsoft Foundry**: Zaloguj się do portalu Microsoft Foundry.
2. **Utwórz projekt**:
   - Jeśli jesteś w projekcie, wybierz „Microsoft Foundry” w lewym górnym rogu strony, aby przejść na stronę główną.
   - Wybierz „+ Create project”.
   - Wprowadź nazwę projektu.
   - Jeśli masz hub, zostanie on wybrany domyślnie. Jeśli masz dostęp do więcej niż jednego huba, możesz wybrać inny z listy rozwijanej. Jeśli chcesz utworzyć nowy hub, wybierz „Create new hub” i podaj nazwę.
   - Wybierz „Create”.

### Tworzenie huba w Microsoft Foundry

1. **Przejdź do Microsoft Foundry**: Zaloguj się za pomocą konta Azure.
2. **Utwórz hub**:
   - Wybierz Centrum zarządzania z lewego menu.
   - Wybierz „All resources”, następnie strzałkę w dół obok „+ New project” i wybierz „+ New hub”.
   - W oknie dialogowym „Create a new hub” wprowadź nazwę swojego huba (np. contoso-hub) i zmodyfikuj pozostałe pola według uznania.
   - Wybierz „Next”, sprawdź informacje, a następnie wybierz „Create”.

Po bardziej szczegółowe instrukcje możesz sięgnąć do oficjalnej [dokumentacji Microsoft](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

Po pomyślnym utworzeniu możesz uzyskać dostęp do stworzonego studia poprzez [ai.azure.com](https://ai.azure.com/)

Na jednej platformie AI Foundry może istnieć wiele projektów. Utwórz projekt w AI Foundry, aby się przygotować.

Utwórz Microsoft Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)


## **2. Wdrażanie modelu Phi w Microsoft Foundry**

Kliknij opcję Explore projektu, aby wejść do Katalogu modeli i wybierz Phi-3

Wybierz Phi-3-mini-4k-instruct

Kliknij „Deploy”, aby wdrożyć model Phi-3-mini-4k-instruct

> [!NOTE]
>
> Podczas wdrażania możesz wybrać moc obliczeniową

## **3. Playground Chat Phi w Microsoft Foundry**

Przejdź do strony wdrożenia, wybierz Playground i rozmawiaj z Phi-3 Microsoft Foundry

## **4. Wdrażanie modelu z Microsoft Foundry**

Aby wdrożyć model z Azure Model Catalog, wykonaj następujące kroki:

- Zaloguj się do Microsoft Foundry.
- Wybierz model, który chcesz wdrożyć, z katalogu modeli Microsoft Foundry.
- Na stronie Szczegóły modelu wybierz Deploy, a następnie wybierz Serverless API z Azure AI Content Safety.
- Wybierz projekt, w którym chcesz wdrożyć swoje modele. Aby skorzystać z oferty Serverless API, Twoja przestrzeń robocza musi należeć do regionu East US 2 lub Sweden Central. Możesz dostosować nazwę wdrożenia.
- W kreatorze wdrożenia wybierz Cennik i warunki, aby poznać ceny i warunki użytkowania.
- Wybierz Deploy. Poczekaj, aż wdrożenie będzie gotowe i zostaniesz przekierowany na stronę Wdrożenia.
- Wybierz Otwórz w playground, aby rozpocząć interakcję z modelem.
- Możesz wrócić do strony Wdrożenia, wybrać wdrożenie i zanotować docelowy URL końcówki oraz Klucz tajny, które możesz wykorzystać do wywoływania wdrożenia i generowania uzupełnień.
- Szczegóły końcówki, URL i klucze dostępu zawsze znajdziesz, przechodząc do zakładki Build i wybierając Wdrożenia w sekcji Komponenty.

> [!NOTE]
> Pamiętaj, że Twoje konto musi mieć uprawnienia roli Azure AI Developer na Grupie zasobów, aby móc wykonać te kroki.

## **5. Korzystanie z Phi API w Microsoft Foundry**

Możesz uzyskać dostęp do https://{Your project name}.region.inference.ml.azure.com/swagger.json przez Postman GET i w połączeniu z kluczem zapoznać się z dostępnymi interfejsami

Bardzo wygodnie możesz pobrać parametry żądania oraz parametry odpowiedzi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uważany za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->