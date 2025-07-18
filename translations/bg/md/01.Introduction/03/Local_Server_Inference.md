<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bcf5dd7031db0031abdb9dd0c05ba118",
  "translation_date": "2025-07-16T20:59:18+00:00",
  "source_file": "md/01.Introduction/03/Local_Server_Inference.md",
  "language_code": "bg"
}
-->
# **Инференция Phi-3 на локален сървър**

Можем да разположим Phi-3 на локален сървър. Потребителите могат да изберат решения като [Ollama](https://ollama.com) или [LM Studio](https://llamaedge.com), или да напишат собствен код. Можете да свържете локалните услуги на Phi-3 чрез [Semantic Kernel](https://github.com/microsoft/semantic-kernel?WT.mc_id=aiml-138114-kinfeylo) или [Langchain](https://www.langchain.com/), за да изградите приложения Copilot.

## **Използване на Semantic Kernel за достъп до Phi-3-mini**

В приложението Copilot създаваме приложения чрез Semantic Kernel / LangChain. Този тип рамка за приложения обикновено е съвместима с Azure OpenAI Service / OpenAI модели и може също да поддържа отворени модели на Hugging Face и локални модели. Какво трябва да направим, ако искаме да използваме Semantic Kernel за достъп до Phi-3-mini? Като пример с .NET, можем да го комбинираме с Hugging Face Connector в Semantic Kernel. По подразбиране той съответства на model id в Hugging Face (при първото използване моделът ще бъде изтеглен от Hugging Face, което отнема време). Можете също да се свържете с локално изградена услуга. В сравнение с двете, препоръчваме да използвате последната, тъй като предлага по-голяма автономия, особено в корпоративни приложения.

![sk](../../../../../translated_images/sk.d03785c25edc6d445a2e9ae037979e544e0b0c482f43c7617b0324e717b9af62.bg.png)

От фигурата се вижда, че достъпът до локални услуги чрез Semantic Kernel лесно може да се свърже със самостоятелно изградения сървър на модела Phi-3-mini. Ето резултата от изпълнението:

![skrun](../../../../../translated_images/skrun.5aafc1e7197dca2020eefcaeaaee184d29bb0cf1c37b00fd9c79acc23a6dc8d2.bg.png)

***Примерен код*** https://github.com/kinfey/Phi3MiniSamples/tree/main/semantickernel

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.