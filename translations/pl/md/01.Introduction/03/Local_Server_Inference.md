<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bcf5dd7031db0031abdb9dd0c05ba118",
  "translation_date": "2025-07-16T20:57:07+00:00",
  "source_file": "md/01.Introduction/03/Local_Server_Inference.md",
  "language_code": "pl"
}
-->
# **Inferencja Phi-3 na lokalnym serwerze**

Możemy wdrożyć Phi-3 na lokalnym serwerze. Użytkownicy mogą wybrać rozwiązania [Ollama](https://ollama.com) lub [LM Studio](https://llamaedge.com), albo napisać własny kod. Można połączyć lokalne usługi Phi-3 za pomocą [Semantic Kernel](https://github.com/microsoft/semantic-kernel?WT.mc_id=aiml-138114-kinfeylo) lub [Langchain](https://www.langchain.com/), aby tworzyć aplikacje Copilot.

## **Użycie Semantic Kernel do dostępu do Phi-3-mini**

W aplikacji Copilot tworzymy aplikacje za pomocą Semantic Kernel / LangChain. Ten typ frameworka aplikacji jest zazwyczaj kompatybilny z Azure OpenAI Service / modelami OpenAI, a także może obsługiwać modele open source na Hugging Face oraz modele lokalne. Co zrobić, jeśli chcemy użyć Semantic Kernel do dostępu do Phi-3-mini? Na przykładzie .NET możemy połączyć go z Hugging Face Connector w Semantic Kernel. Domyślnie odpowiada to identyfikatorowi modelu na Hugging Face (przy pierwszym użyciu model zostanie pobrany z Hugging Face, co zajmuje sporo czasu). Można też połączyć się z lokalnie zbudowaną usługą. W porównaniu do obu opcji, zalecamy tę drugą, ponieważ zapewnia większą autonomię, szczególnie w zastosowaniach korporacyjnych.

![sk](../../../../../translated_images/pl/sk.d03785c25edc6d44.webp)

Na ilustracji widać, że dostęp do lokalnych usług przez Semantic Kernel pozwala łatwo połączyć się z samodzielnie zbudowanym serwerem modelu Phi-3-mini. Oto wynik działania:

![skrun](../../../../../translated_images/pl/skrun.5aafc1e7197dca20.webp)

***Przykładowy kod*** https://github.com/kinfey/Phi3MiniSamples/tree/main/semantickernel

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.