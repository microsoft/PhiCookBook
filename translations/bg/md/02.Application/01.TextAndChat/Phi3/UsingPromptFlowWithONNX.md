<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-05-09T18:55:30+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "bg"
}
-->
# Използване на Windows GPU за създаване на Prompt flow решение с Phi-3.5-Instruct ONNX

Следният документ е пример как да използвате PromptFlow с ONNX (Open Neural Network Exchange) за разработка на AI приложения, базирани на Phi-3 модели.

PromptFlow е набор от инструменти за разработка, създадени да улеснят целия процес на разработка на AI приложения, базирани на LLM (Large Language Model), от идеята и прототипирането до тестването и оценката.

Чрез интегриране на PromptFlow с ONNX, разработчиците могат да:

- Оптимизират производителността на модела: Използват ONNX за ефективно изпълнение и внедряване на модела.
- Опростят разработката: Използват PromptFlow за управление на работния процес и автоматизиране на повтарящи се задачи.
- Подобрят сътрудничеството: Улесняват по-добрата работа в екип чрез предоставяне на единна среда за разработка.

**Prompt flow** е набор от инструменти за разработка, предназначени да оптимизират целия цикъл на разработка на AI приложения, базирани на LLM, от идеята, прототипирането, тестването, оценката до внедряването и мониторинга в продукция. Той прави prompt инженерството много по-лесно и ви позволява да изграждате LLM приложения с качество за продукция.

Prompt flow може да се свърже с OpenAI, Azure OpenAI Service и персонализирани модели (Huggingface, локални LLM/SLM). Целим да внедрим квантования ONNX модел на Phi-3.5 в локални приложения. Prompt flow може да ни помогне да планираме по-добре бизнеса си и да реализираме локални решения, базирани на Phi-3.5. В този пример ще комбинираме ONNX Runtime GenAI библиотеката, за да завършим Prompt flow решението, базирано на Windows GPU.

## **Инсталация**

### **ONNX Runtime GenAI за Windows GPU**

Прочетете това ръководство за настройка на ONNX Runtime GenAI за Windows GPU [кликнете тук](./ORTWindowGPUGuideline.md)

### **Настройка на Prompt flow във VSCode**

1. Инсталирайте разширението Prompt flow за VS Code

![pfvscode](../../../../../../translated_images/pfvscode.79f42ae5dd93ed35c19d6d978ae75831fef40e0b8440ee48b893b5a0597d2260.bg.png)

2. След като инсталирате разширението Prompt flow за VS Code, кликнете върху него и изберете **Installation dependencies**, следвайте ръководството, за да инсталирате Prompt flow SDK във вашата среда

![pfsetup](../../../../../../translated_images/pfsetup.0c82d99c7760aac29833b37faf4329e67e22279b1c5f37a73724dfa9ebaa32ee.bg.png)

3. Изтеглете [примерния код](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) и го отворете с VS Code

![pfsample](../../../../../../translated_images/pfsample.7bf40b133a558d86356dd6bc0e480bad2659d9c5364823dae9b3e6784e6f2d25.bg.png)

4. Отворете **flow.dag.yaml**, за да изберете вашата Python среда

![pfdag](../../../../../../translated_images/pfdag.c5eb356fa3a96178cd594de9a5da921c4bbe646a9946f32aa20d344ccbeb51a0.bg.png)

   Отворете **chat_phi3_ort.py**, за да промените местоположението на вашия Phi-3.5-instruct ONNX модел

![pfphi](../../../../../../translated_images/pfphi.fff4b0afea47c92c8481174dbf3092823906fca5b717fc642f78947c3e5bbb39.bg.png)

5. Стартирайте prompt flow за тестване

Отворете **flow.dag.yaml** и кликнете върху визуалния редактор

![pfv](../../../../../../translated_images/pfv.7af6ecd65784a98558b344ba69b5ba6233876823fb435f163e916a632394fc1e.bg.png)

след това кликнете и го стартирайте за тест

![pfflow](../../../../../../translated_images/pfflow.9697e0fda67794bb0cf4b78d52e6f5a42002eec935bc2519933064afbbdd34f0.bg.png)

1. Можете да стартирате batch в терминала, за да видите повече резултати


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Можете да прегледате резултатите в браузъра по подразбиране


![pfresult](../../../../../../translated_images/pfresult.972eb57dd5bec646e1aa01148991ba8959897efea396e42cf9d7df259444878d.bg.png)

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.