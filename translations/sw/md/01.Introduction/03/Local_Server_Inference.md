<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bcf5dd7031db0031abdb9dd0c05ba118",
  "translation_date": "2025-05-09T12:07:38+00:00",
  "source_file": "md/01.Introduction/03/Local_Server_Inference.md",
  "language_code": "sw"
}
-->
# **Inference Phi-3 kwenye Server ya Ndani**

Tunaweza kupeleka Phi-3 kwenye server ya ndani. Watumiaji wanaweza kuchagua suluhisho za [Ollama](https://ollama.com) au [LM Studio](https://llamaedge.com), au wanaweza kuandika msimbo wao wenyewe. Unaweza kuunganisha huduma za ndani za Phi-3 kupitia [Semantic Kernel](https://github.com/microsoft/semantic-kernel?WT.mc_id=aiml-138114-kinfeylo) au [Langchain](https://www.langchain.com/) kujenga programu za Copilot.

## **Tumia Semantic Kernel kufikia Phi-3-mini**

Katika programu ya Copilot, tunaunda programu kupitia Semantic Kernel / LangChain. Aina hii ya mfumo wa programu kwa kawaida inalingana na Azure OpenAI Service / mifano ya OpenAI, na pia inaweza kuunga mkono mifano ya chanzo huria kwenye Hugging Face na mifano ya ndani. Tunapaswa kufanya nini tunapotaka kutumia Semantic Kernel kufikia Phi-3-mini? Tukichukua .NET kama mfano, tunaweza kuichanganya na Hugging Face Connector katika Semantic Kernel. Kwa default, inaweza kuendana na kitambulisho cha mfano kwenye Hugging Face (wakati wa kwanza unapotumia, mfano utapakuliwa kutoka Hugging Face, jambo ambalo huchukua muda mrefu). Pia unaweza kuungana na huduma ya ndani uliyojijengea mwenyewe. Kulinganisha kati ya hizo mbili, tunapendekeza kutumia ile ya mwisho kwa sababu ina uhuru zaidi, hasa katika matumizi ya biashara.

![sk](../../../../../translated_images/sk.c244b32f4811c6f0938b9e95b0b2f4b28105bff6495bdc3b24cd42b3e3e89bb9.sw.png)

Kutoa huduma za ndani kupitia Semantic Kernel kunaweza kuunganishwa kwa urahisi na server ya mfano wa Phi-3-mini uliyojijengea mwenyewe. Hapa ni matokeo ya kuendesha

![skrun](../../../../../translated_images/skrun.fb7a635a22ae8b7919d6e15c0eb27262526ed69728c5a1d2773a97d4562657c7.sw.png)

***Sample Code*** https://github.com/kinfey/Phi3MiniSamples/tree/main/semantickernel

**Kangamsha**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upotovu wa maana. Hati asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubeba dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.