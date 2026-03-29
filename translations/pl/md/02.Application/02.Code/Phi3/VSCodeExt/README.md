# **Zbuduj własnego agenta GitHub Copilot Chat w Visual Studio Code z serii Microsoft Phi-3**

Czy korzystałeś z agenta przestrzeni roboczej w GitHub Copilot Chat? Chcesz zbudować własnego agenta kodu dla swojego zespołu? Ten praktyczny lab ma na celu połączenie modelu open source w celu stworzenia agenta biznesowego kodu na poziomie przedsiębiorstwa.

## **Podstawy**

### **Dlaczego wybrać Microsoft Phi-3**

Phi-3 to seria rodzin, obejmująca phi-3-mini, phi-3-small i phi-3-medium, oparta na różnych parametrach treningowych do generowania tekstu, ukończenia dialogu i generowania kodu. Jest również phi-3-vision oparta na Vision. Nadaje się dla przedsiębiorstw lub różnych zespołów do tworzenia offline generatywnych rozwiązań AI.

Zalecane przeczytanie tego linku [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

Rozszerzenie GitHub Copilot Chat daje interfejs czatu, który pozwala na interakcję z GitHub Copilot i otrzymywanie odpowiedzi na pytania związane z kodowaniem bezpośrednio w VS Code, bez konieczności przeglądania dokumentacji lub szukania w internetowych forach.

Copilot Chat może używać podświetlania składni, wcięć i innych funkcji formatowania, aby dodać klarowności generowanej odpowiedzi. W zależności od typu pytania użytkownika, wynik może zawierać linki do kontekstu, jaki Copilot użył do generowania odpowiedzi, takich jak pliki źródłowego kodu lub dokumentacja, lub przyciski do dostępu do funkcji VS Code.

- Copilot Chat integruje się z twoim przepływem pracy programisty i zapewnia wsparcie tam, gdzie go potrzebujesz:

- Rozpocznij rozmowę na czacie bezpośrednio z edytora lub terminala, aby uzyskać pomoc podczas pisania kodu

- Używaj widoku Chat, aby mieć asystenta AI po boku, który pomaga w każdej chwili

- Uruchom Quick Chat, aby zadać szybkie pytanie i wrócić do pracy

Możesz używać GitHub Copilot Chat w różnych scenariuszach, takich jak:

- Odpowiadanie na pytania dotyczące kodowania, jak najlepiej rozwiązać problem

- Tłumaczenie kodu innej osoby i sugerowanie ulepszeń

- Proponowanie poprawek kodu

- Generowanie przypadków testów jednostkowych

- Generowanie dokumentacji kodu

Zalecane przeczytanie tego linku [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)

###  **Microsoft GitHub Copilot Chat @workspace**

Odwołanie do **@workspace** w Copilot Chat pozwala zadawać pytania dotyczące całej twojej bazy kodu. Na podstawie pytania Copilot inteligentnie pobiera odpowiednie pliki i symbole, które następnie odnosi w swojej odpowiedzi jako linki i przykłady kodu.

Aby odpowiedzieć na twoje pytanie, **@workspace** przeszukuje te same źródła, których używa programista podczas nawigacji po bazie kodu w VS Code:

- Wszystkie pliki w przestrzeni roboczej, z wyjątkiem plików ignorowanych przez .gitignore

- Struktura katalogów z zagnieżdżonymi folderami i nazwami plików

- Indeks wyszukiwania kodu GitHub, jeśli przestrzeń robocza jest repozytorium GitHub i jest indeksowana przez wyszukiwanie kodu

- Symbole i definicje w przestrzeni roboczej

- Aktualnie zaznaczony tekst lub widoczny tekst w aktywnym edytorze

Uwaga: .gitignore jest pomijany, jeśli masz otwarty plik lub zaznaczony tekst w pliku ignorowanym.

Zalecane przeczytanie tego linku [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]

## **Dowiedz się więcej o tym labie**

GitHub Copilot znacznie poprawił efektywność programowania w przedsiębiorstwach, a każde przedsiębiorstwo pragnie dostosować odpowiednie funkcje GitHub Copilot. Wiele przedsiębiorstw stworzyło własne rozszerzenia podobne do GitHub Copilot bazujące na swoich scenariuszach biznesowych i modelach open source. Dla przedsiębiorstw, dostosowane rozszerzenia są łatwiejsze do kontrolowania, ale wpływa to również na doświadczenie użytkownika. W końcu GitHub Copilot ma silniejsze funkcje w obsłudze ogólnych scenariuszy i profesjonalizmu. Jeśli doświadczenie może pozostać spójne, lepiej dostosować własne rozszerzenie przedsiębiorstwa. GitHub Copilot Chat udostępnia odpowiednie API dla przedsiębiorstw do rozszerzenia doświadczenia czatu. Utrzymanie spójnego doświadczenia i posiadanie dostosowanych funkcji to lepsze doświadczenie użytkownika.

Ten lab głównie wykorzystuje model Phi-3 w połączeniu z lokalnym NPU i hybrydą Azure do zbudowania niestandardowego Agenta w GitHub Copilot Chat ***@PHI3***, aby wspierać programistów przedsiębiorstw w generowaniu kodu ***(@PHI3 /gen)*** i generowaniu kodu na podstawie obrazów ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/pl/cover.1017ebc9a7c46d09.webp)

### ***Uwaga:*** 

Ten lab jest obecnie wdrażany na AIPC procesorach Intel i Apple Silicon. Będziemy kontynuować aktualizację wersji Qualcomm NPU.

## **Lab**

| Nazwa | Opis | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Instalacje(✅) | Konfiguracja i instalacja powiązanych środowisk i narzędzi instalacyjnych | [Idź](./HOL/AIPC/01.Installations.md) |[Idź](./HOL/Apple/01.Installations.md) |
| Lab1 - Uruchomienie Prompt flow z Phi-3-mini (✅) | W połączeniu z AIPC / Apple Silicon, używając lokalnego NPU do tworzenia generowania kodu przez Phi-3-mini | [Idź](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Idź](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Wdrażanie Phi-3-vision na Azure Machine Learning Service (✅) | Generowanie kodu przez wdrożenie katalogu modeli Azure Machine Learning Service - obraz Phi-3-vision | [Idź](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Idź](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Utwórz agenta @phi-3 w GitHub Copilot Chat (✅)  | Utwórz niestandardowego agenta Phi-3 w GitHub Copilot Chat do generowania kodu, generowania grafów kodu, RAG itd. | [Idź](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Idź](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Przykładowy kod (✅)  | Pobierz przykładowy kod | [Idź](../../../../../../../code/07.Lab/01/AIPC) | [Idź](../../../../../../../code/07.Lab/01/Apple) |

## **Zasoby**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Dowiedz się więcej o GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Dowiedz się więcej o GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Dowiedz się więcej o GitHub Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Dowiedz się więcej o Microsoft Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Dowiedz się więcej o katalogu modeli Microsoft Foundry [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Dokument ten został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub niedokładności. Oryginalny dokument w języku źródłowym powinien być uważany za źródło autorytatywne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->