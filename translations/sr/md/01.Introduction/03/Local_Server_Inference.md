<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bcf5dd7031db0031abdb9dd0c05ba118",
  "translation_date": "2025-07-16T20:59:24+00:00",
  "source_file": "md/01.Introduction/03/Local_Server_Inference.md",
  "language_code": "sr"
}
-->
# **Инференција Phi-3 на локалном серверу**

Можемо да покренемо Phi-3 на локалном серверу. Корисници могу да изаберу решења као што су [Ollama](https://ollama.com) или [LM Studio](https://llamaedge.com), или могу написати свој код. Можете повезати локалне сервисе Phi-3 преко [Semantic Kernel](https://github.com/microsoft/semantic-kernel?WT.mc_id=aiml-138114-kinfeylo) или [Langchain](https://www.langchain.com/) како бисте направили Copilot апликације.

## **Коришћење Semantic Kernel за приступ Phi-3-mini**

У Copilot апликацији креирамо апликације преко Semantic Kernel / LangChain. Овај тип апликационог оквира је генерално компатибилан са Azure OpenAI Service / OpenAI моделима, а може подржати и open source моделе са Hugging Face и локалне моделе. Шта треба да урадимо ако желимо да користимо Semantic Kernel за приступ Phi-3-mini? Уз пример .NET-а, можемо га комбиновати са Hugging Face Connector-ом у Semantic Kernel-у. По дифолту, он одговара моделу на Hugging Face (при првом коришћењу модел ће бити преузет са Hugging Face-а, што може потрајати). Такође можете да се повежете на изграђени локални сервис. У поређењу са ова два, препоручујемо коришћење другог јер пружа већу аутономију, посебно у пословним апликацијама.

![sk](../../../../../translated_images/sk.d03785c25edc6d445a2e9ae037979e544e0b0c482f43c7617b0324e717b9af62.sr.png)

Са слике се види да приступ локалним сервисима преко Semantic Kernel-а лако повезује са самостално изграђеним Phi-3-mini сервером модела. Ево резултата извршавања:

![skrun](../../../../../translated_images/skrun.5aafc1e7197dca2020eefcaeaaee184d29bb0cf1c37b00fd9c79acc23a6dc8d2.sr.png)

***Пример кода*** https://github.com/kinfey/Phi3MiniSamples/tree/main/semantickernel

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.