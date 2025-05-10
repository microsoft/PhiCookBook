<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bcf5dd7031db0031abdb9dd0c05ba118",
  "translation_date": "2025-05-09T12:05:21+00:00",
  "source_file": "md/01.Introduction/03/Local_Server_Inference.md",
  "language_code": "da"
}
-->
# **Inference Phi-3 på lokal server**

Vi kan implementere Phi-3 på en lokal server. Brugere kan vælge [Ollama](https://ollama.com) eller [LM Studio](https://llamaedge.com) løsninger, eller de kan skrive deres egen kode. Du kan forbinde Phi-3’s lokale tjenester gennem [Semantic Kernel](https://github.com/microsoft/semantic-kernel?WT.mc_id=aiml-138114-kinfeylo) eller [Langchain](https://www.langchain.com/) for at bygge Copilot-applikationer


## **Brug Semantic Kernel til at få adgang til Phi-3-mini**

I Copilot-applikationen opretter vi applikationer gennem Semantic Kernel / LangChain. Denne type applikationsramme er generelt kompatibel med Azure OpenAI Service / OpenAI modeller, og kan også understøtte open source modeller på Hugging Face og lokale modeller. Hvad skal vi gøre, hvis vi vil bruge Semantic Kernel til at få adgang til Phi-3-mini? Ved at bruge .NET som eksempel kan vi kombinere det med Hugging Face Connector i Semantic Kernel. Som standard kan det matche model-id’et på Hugging Face (første gang du bruger det, bliver modellen downloadet fra Hugging Face, hvilket tager lang tid). Du kan også forbinde til den selvbyggede lokale tjeneste. Sammenlignet med de to anbefaler vi den sidste, fordi den har en højere grad af selvstændighed, især i virksomhedsapplikationer.

![sk](../../../../../translated_images/sk.c244b32f4811c6f0938b9e95b0b2f4b28105bff6495bdc3b24cd42b3e3e89bb9.da.png)


Fra figuren kan adgang til lokale tjenester gennem Semantic Kernel nemt forbinde til den selvbyggede Phi-3-mini modelserver. Her er resultatet af kørslen


![skrun](../../../../../translated_images/skrun.fb7a635a22ae8b7919d6e15c0eb27262526ed69728c5a1d2773a97d4562657c7.da.png)

***Sample Code*** https://github.com/kinfey/Phi3MiniSamples/tree/main/semantickernel

**Ansvarsfraskrivelse**:  
Dette dokument er oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.