<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bcf5dd7031db0031abdb9dd0c05ba118",
  "translation_date": "2025-07-16T20:59:38+00:00",
  "source_file": "md/01.Introduction/03/Local_Server_Inference.md",
  "language_code": "sl"
}
-->
# **Inferenca Phi-3 na lokalnem strežniku**

Phi-3 lahko namestimo na lokalni strežnik. Uporabniki lahko izberejo rešitve [Ollama](https://ollama.com) ali [LM Studio](https://llamaedge.com), lahko pa napišejo tudi svojo kodo. Lokalnim storitvam Phi-3 se lahko povežemo preko [Semantic Kernel](https://github.com/microsoft/semantic-kernel?WT.mc_id=aiml-138114-kinfeylo) ali [Langchain](https://www.langchain.com/), da zgradimo aplikacije Copilot.

## **Uporaba Semantic Kernel za dostop do Phi-3-mini**

V aplikaciji Copilot ustvarjamo aplikacije preko Semantic Kernel / LangChain. Ta vrsta aplikacijskega ogrodja je na splošno združljiva z Azure OpenAI Service / OpenAI modeli, prav tako pa podpira odprtokodne modele na Hugging Face in lokalne modele. Kaj storiti, če želimo uporabiti Semantic Kernel za dostop do Phi-3-mini? Kot primer uporabimo .NET, ki ga lahko združimo s Hugging Face Connectorjem v Semantic Kernel. Privzeto se poveže z id-jem modela na Hugging Face (ob prvem zagonu se model prenese z Hugging Face, kar traja nekaj časa). Povežemo se lahko tudi z lokalno zgrajeno storitvijo. Priporočamo slednjo možnost, saj omogoča večjo avtonomijo, še posebej v poslovnih aplikacijah.

![sk](../../../../../translated_images/sk.d03785c25edc6d445a2e9ae037979e544e0b0c482f43c7617b0324e717b9af62.sl.png)

Iz slike je razvidno, da dostop do lokalnih storitev preko Semantic Kernel enostavno poveže s samostojno zgrajenim strežnikom modela Phi-3-mini. Tukaj je rezultat zagona:

![skrun](../../../../../translated_images/skrun.5aafc1e7197dca2020eefcaeaaee184d29bb0cf1c37b00fd9c79acc23a6dc8d2.sl.png)

***Primer kode*** https://github.com/kinfey/Phi3MiniSamples/tree/main/semantickernel

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.