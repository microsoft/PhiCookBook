<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bcf5dd7031db0031abdb9dd0c05ba118",
  "translation_date": "2025-07-16T20:59:11+00:00",
  "source_file": "md/01.Introduction/03/Local_Server_Inference.md",
  "language_code": "ro"
}
-->
# **Inferență Phi-3 pe Server Local**

Putem implementa Phi-3 pe un server local. Utilizatorii pot alege soluțiile [Ollama](https://ollama.com) sau [LM Studio](https://llamaedge.com), sau pot scrie propriul cod. Poți conecta serviciile locale Phi-3 prin [Semantic Kernel](https://github.com/microsoft/semantic-kernel?WT.mc_id=aiml-138114-kinfeylo) sau [Langchain](https://www.langchain.com/) pentru a construi aplicații Copilot.

## **Folosește Semantic Kernel pentru a accesa Phi-3-mini**

În aplicația Copilot, creăm aplicații prin Semantic Kernel / LangChain. Acest tip de framework pentru aplicații este, în general, compatibil cu Azure OpenAI Service / modelele OpenAI, și poate susține, de asemenea, modele open source de pe Hugging Face și modele locale. Ce trebuie să facem dacă vrem să folosim Semantic Kernel pentru a accesa Phi-3-mini? Folosind .NET ca exemplu, îl putem combina cu Hugging Face Connector în Semantic Kernel. Implicit, acesta corespunde cu id-ul modelului de pe Hugging Face (prima dată când îl folosești, modelul va fi descărcat de pe Hugging Face, ceea ce durează ceva timp). De asemenea, poți conecta serviciul local construit. Comparativ cu cele două, recomandăm folosirea celei de-a doua opțiuni deoarece oferă un grad mai mare de autonomie, în special în aplicațiile enterprise.

![sk](../../../../../translated_images/ro/sk.d03785c25edc6d44.png)

Din imagine, accesarea serviciilor locale prin Semantic Kernel poate conecta cu ușurință serverul modelului Phi-3-mini construit intern. Iată rezultatul rulării:

![skrun](../../../../../translated_images/ro/skrun.5aafc1e7197dca20.png)

***Sample Code*** https://github.com/kinfey/Phi3MiniSamples/tree/main/semantickernel

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.