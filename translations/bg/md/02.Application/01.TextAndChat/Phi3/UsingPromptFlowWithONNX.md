<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-07-17T03:03:48+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "bg"
}
-->
# Използване на Windows GPU за създаване на Prompt flow решение с Phi-3.5-Instruct ONNX

Следният документ е пример за това как да използвате PromptFlow с ONNX (Open Neural Network Exchange) за разработка на AI приложения, базирани на Phi-3 модели.

PromptFlow е набор от инструменти за разработка, предназначени да улеснят целия цикъл на разработка на AI приложения, базирани на LLM (Large Language Model), от идеята и прототипирането до тестването и оценката.

Чрез интегриране на PromptFlow с ONNX, разработчиците могат да:

- Оптимизират производителността на модела: Използвайте ONNX за ефективно изпълнение и внедряване на модела.
- Опростят разработката: Използвайте PromptFlow за управление на работния процес и автоматизиране на повтарящи се задачи.
- Подобрят сътрудничеството: Улесняват по-добрата комуникация между членовете на екипа чрез предоставяне на единна среда за разработка.

**Prompt flow** е набор от инструменти за разработка, създаден да улесни целия цикъл на разработка на AI приложения, базирани на LLM, от идеята, прототипирането, тестването, оценката до внедряване в продукция и мониторинг. Той прави инженерството на prompt-ове много по-лесно и ви позволява да създавате LLM приложения с качество за продукция.

Prompt flow може да се свърже с OpenAI, Azure OpenAI Service и персонализирани модели (Huggingface, локални LLM/SLM). Надяваме се да внедрим квантования ONNX модел на Phi-3.5 в локални приложения. Prompt flow може да ни помогне по-добре да планираме бизнеса си и да завършим локални решения, базирани на Phi-3.5. В този пример ще комбинираме ONNX Runtime GenAI Library, за да завършим Prompt flow решение, базирано на Windows GPU.

## **Инсталация**

### **ONNX Runtime GenAI за Windows GPU**

Прочетете това ръководство за настройка на ONNX Runtime GenAI за Windows GPU [кликнете тук](./ORTWindowGPUGuideline.md)

### **Настройка на Prompt flow във VSCode**

1. Инсталирайте Prompt flow разширението за VS Code

![pfvscode](../../../../../../translated_images/pfvscode.eff93dfc66a42cbef699fc16fa48f3ed3a23361875a3362037d026896395a00d.bg.png)

2. След инсталиране на Prompt flow разширението за VS Code, кликнете върху разширението и изберете **Installation dependencies**, следвайте това ръководство, за да инсталирате Prompt flow SDK във вашата среда

![pfsetup](../../../../../../translated_images/pfsetup.b46e93096f5a254f74e8b74ce2be7047ce963ef573d755ec897eb1b78cb9c954.bg.png)

3. Изтеглете [примерния код](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) и го отворете с VS Code

![pfsample](../../../../../../translated_images/pfsample.8d89e70584ffe7c4dba182513e3148a989e552c3b8e4948567a6b806b5ae1845.bg.png)

4. Отворете **flow.dag.yaml**, за да изберете вашата Python среда

![pfdag](../../../../../../translated_images/pfdag.264a77f7366458ff850a76ae949226391ea382856d543ef9da4b92096aff7e4b.bg.png)

   Отворете **chat_phi3_ort.py**, за да промените местоположението на вашия Phi-3.5-instruct ONNX модел

![pfphi](../../../../../../translated_images/pfphi.72da81d74244b45fc78cdfeeb8c7fbd9e7cd610bf2f96814dbade6a4a2dfad7e.bg.png)

5. Стартирайте вашия prompt flow за тестване

Отворете **flow.dag.yaml** и кликнете върху визуалния редактор

![pfv](../../../../../../translated_images/pfv.ba8a81f34b20f603cccee3fe91e94113792ed6f5af28f76ab08e1a0b3e77b33b.bg.png)

след това кликнете и го стартирайте за тест

![pfflow](../../../../../../translated_images/pfflow.4e1135a089b1ce1b6348b59edefdb6333e5729b54c8e57f9039b7f9463e68fbd.bg.png)

1. Можете да стартирате batch в терминала, за да проверите повече резултати


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Можете да видите резултатите в браузъра по подразбиране


![pfresult](../../../../../../translated_images/pfresult.c22c826f8062d7cbe871cff35db4a013dcfefc13fafe5da6710a8549a96a4ceb.bg.png)

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.