<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bcf5dd7031db0031abdb9dd0c05ba118",
  "translation_date": "2025-07-16T20:58:42+00:00",
  "source_file": "md/01.Introduction/03/Local_Server_Inference.md",
  "language_code": "sw"
}
-->
# **Uchambuzi wa Phi-3 kwenye Seva ya Ndani**

Tunaweza kupeleka Phi-3 kwenye seva ya ndani. Watumiaji wanaweza kuchagua suluhisho za [Ollama](https://ollama.com) au [LM Studio](https://llamaedge.com), au wanaweza kuandika msimbo wao wenyewe. Unaweza kuunganisha huduma za ndani za Phi-3 kupitia [Semantic Kernel](https://github.com/microsoft/semantic-kernel?WT.mc_id=aiml-138114-kinfeylo) au [Langchain](https://www.langchain.com/) kujenga programu za Copilot.

## **Tumia Semantic Kernel kufikia Phi-3-mini**

Katika programu ya Copilot, tunaunda programu kupitia Semantic Kernel / LangChain. Aina hii ya mfumo wa programu kwa ujumla inafaa na Azure OpenAI Service / mifano ya OpenAI, na pia inaweza kuunga mkono mifano ya chanzo huria kwenye Hugging Face na mifano ya ndani. Tunapaswa kufanya nini tunapotaka kutumia Semantic Kernel kufikia Phi-3-mini? Kwa kutumia .NET kama mfano, tunaweza kuichanganya na Hugging Face Connector katika Semantic Kernel. Kwa kawaida, inaweza kuendana na kitambulisho cha mfano kwenye Hugging Face (mara ya kwanza unapotumia, mfano utapakuliwa kutoka Hugging Face, jambo ambalo huchukua muda mrefu). Pia unaweza kuungana na huduma ya ndani iliyojengwa. Tukilinganisha hizi mbili, tunapendekeza kutumia ya mwisho kwa sababu ina uhuru zaidi, hasa katika programu za biashara.

![sk](../../../../../translated_images/sw/sk.d03785c25edc6d44.png)

Kutoka kwenye picha, kufikia huduma za ndani kupitia Semantic Kernel kunaweza kuunganisha kwa urahisi na seva ya mfano wa Phi-3-mini uliyojijengea mwenyewe. Hapa ni matokeo ya kuendesha

![skrun](../../../../../translated_images/sw/skrun.5aafc1e7197dca20.png)

***Msimbo wa Mfano*** https://github.com/kinfey/Phi3MiniSamples/tree/main/semantickernel

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.