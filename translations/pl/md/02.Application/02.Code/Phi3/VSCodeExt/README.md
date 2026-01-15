<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00b7a699de8ac405fa821f4c0f7fc0ab",
  "translation_date": "2025-07-17T03:38:47+00:00",
  "source_file": "md/02.Application/02.Code/Phi3/VSCodeExt/README.md",
  "language_code": "pl"
}
-->
# **Zbuduj własnego Visual Studio Code GitHub Copilot Chat z rodziną Microsoft Phi-3**

Czy korzystałeś z agenta workspace w GitHub Copilot Chat? Chcesz stworzyć własnego agenta kodu dla swojego zespołu? Ten praktyczny lab ma na celu połączenie modelu open source, aby zbudować agent biznesowy do kodu na poziomie przedsiębiorstwa.

## **Podstawy**

### **Dlaczego warto wybrać Microsoft Phi-3**

Phi-3 to seria modeli, obejmująca phi-3-mini, phi-3-small oraz phi-3-medium, różniące się parametrami treningowymi do generowania tekstu, uzupełniania dialogów i generowania kodu. Istnieje także phi-3-vision oparty na Vision. Model ten jest odpowiedni dla przedsiębiorstw lub różnych zespołów do tworzenia offline’owych rozwiązań generatywnej AI.

Zalecane do przeczytania: [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

Rozszerzenie GitHub Copilot Chat oferuje interfejs czatu, który pozwala na interakcję z GitHub Copilot i otrzymywanie odpowiedzi na pytania związane z kodowaniem bezpośrednio w VS Code, bez konieczności przeglądania dokumentacji czy szukania w internetowych forach.

Copilot Chat może używać podświetlania składni, wcięć i innych elementów formatowania, aby zwiększyć czytelność generowanej odpowiedzi. W zależności od rodzaju pytania użytkownika, wynik może zawierać linki do kontekstu, z którego Copilot korzystał przy generowaniu odpowiedzi, takie jak pliki źródłowe lub dokumentacja, albo przyciski umożliwiające dostęp do funkcji VS Code.

- Copilot Chat integruje się z Twoim procesem programistycznym i oferuje pomoc tam, gdzie jej potrzebujesz:

- Rozpocznij rozmowę inline bezpośrednio z edytora lub terminala, aby uzyskać pomoc podczas kodowania

- Użyj widoku Chat, aby mieć asystenta AI obok siebie, który pomoże Ci w każdej chwili

- Uruchom Quick Chat, aby zadać szybkie pytanie i wrócić do pracy

Możesz korzystać z GitHub Copilot Chat w różnych scenariuszach, takich jak:

- Odpowiadanie na pytania dotyczące kodowania i najlepszych rozwiązań problemów

- Tłumaczenie kodu napisanego przez innych i sugerowanie ulepszeń

- Proponowanie poprawek w kodzie

- Generowanie testów jednostkowych

- Tworzenie dokumentacji kodu

Zalecane do przeczytania: [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)

### **Microsoft GitHub Copilot Chat @workspace**

Odwołanie do **@workspace** w Copilot Chat pozwala zadawać pytania dotyczące całej bazy kodu. Na podstawie pytania Copilot inteligentnie wyszukuje odpowiednie pliki i symbole, które następnie wykorzystuje w odpowiedzi jako linki i przykłady kodu.

Aby odpowiedzieć na Twoje pytanie, **@workspace** przeszukuje te same źródła, z których korzysta programista podczas nawigacji po kodzie w VS Code:

- Wszystkie pliki w workspace, z wyjątkiem tych ignorowanych przez plik .gitignore

- Strukturę katalogów wraz z zagnieżdżonymi folderami i nazwami plików

- Indeks wyszukiwania kodu GitHub, jeśli workspace jest repozytorium GitHub i jest indeksowany przez code search

- Symbole i definicje w workspace

- Aktualnie zaznaczony tekst lub widoczny tekst w aktywnym edytorze

Uwaga: .gitignore jest pomijany, jeśli masz otwarty plik lub zaznaczony tekst w pliku ignorowanym.

Zalecane do przeczytania: [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]

## **Dowiedz się więcej o tym labie**

GitHub Copilot znacznie poprawił efektywność programowania w przedsiębiorstwach, a każde z nich chce dostosować odpowiednie funkcje GitHub Copilot do swoich potrzeb. Wiele firm tworzy własne rozszerzenia podobne do GitHub Copilot, bazując na swoich scenariuszach biznesowych i modelach open source. Dla przedsiębiorstw spersonalizowane rozszerzenia są łatwiejsze do kontrolowania, ale wpływa to również na doświadczenie użytkownika. W końcu GitHub Copilot ma silniejsze funkcje w obsłudze ogólnych scenariuszy i profesjonalizmu. Jeśli można zachować spójne doświadczenie, lepiej jest dostosować własne rozszerzenie przedsiębiorstwa. GitHub Copilot Chat udostępnia odpowiednie API, które pozwalają firmom rozszerzać doświadczenie czatu. Utrzymanie spójnego doświadczenia i posiadanie spersonalizowanych funkcji to lepsze doświadczenie użytkownika.

Ten lab głównie wykorzystuje model Phi-3 w połączeniu z lokalnym NPU i hybrydą Azure do zbudowania niestandardowego Agenta w GitHub Copilot Chat ***@PHI3***, który pomaga programistom przedsiębiorstwa w generowaniu kodu***(@PHI3 /gen)*** oraz generowaniu kodu na podstawie obrazów ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/pl/cover.1017ebc9a7c46d09.png)

### ***Uwaga:***

Ten lab jest obecnie realizowany na AIPC z procesorami Intel CPU i Apple Silicon. Będziemy kontynuować aktualizacje wersji Qualcomm NPU.

## **Lab**

| Nazwa | Opis | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Instalacje(✅) | Konfiguracja i instalacja powiązanych środowisk i narzędzi instalacyjnych | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Uruchomienie Prompt flow z Phi-3-mini (✅) | W połączeniu z AIPC / Apple Silicon, wykorzystanie lokalnego NPU do tworzenia generowania kodu przez Phi-3-mini | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Wdrożenie Phi-3-vision na Azure Machine Learning Service(✅) | Generowanie kodu przez wdrożenie modelu Phi-3-vision z katalogu modeli Azure Machine Learning Service | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Stwórz agenta @phi-3 w GitHub Copilot Chat(✅)  | Utwórz niestandardowego agenta Phi-3 w GitHub Copilot Chat do generowania kodu, kodu grafów, RAG itp. | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Przykładowy kod (✅)  | Pobierz przykładowy kod | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |

## **Zasoby**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Dowiedz się więcej o GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Dowiedz się więcej o GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Dowiedz się więcej o GitHub Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Dowiedz się więcej o Azure AI Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Dowiedz się więcej o katalogu modeli Azure AI Foundry [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.