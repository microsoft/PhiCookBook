<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-07-17T03:03:59+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "sr"
}
-->
# Коришћење Windows GPU-а за креирање Prompt flow решења са Phi-3.5-Instruct ONNX

Следећи документ је пример како користити PromptFlow са ONNX (Open Neural Network Exchange) за развој AI апликација заснованих на Phi-3 моделима.

PromptFlow је скуп алата за развој дизајниран да поједностави цео циклус развоја AI апликација заснованих на LLM-овима (Large Language Model), од идеје и прототиповања до тестирања и евалуације.

Интеграцијом PromptFlow-а са ONNX-ом, програмери могу:

- Оптимизовати перформансе модела: Искористити ONNX за ефикасно извођење и имплементацију модела.
- Поједноставити развој: Користити PromptFlow за управљање током рада и аутоматизацију понављајућих задатака.
- Побољшати сарадњу: Олакшати бољу сарадњу међу члановима тима пружајући јединствено развојно окружење.

**Prompt flow** је скуп алата за развој дизајниран да поједностави цео циклус развоја AI апликација заснованих на LLM-овима, од идеје, прототиповања, тестирања, евалуације до производног распореда и праћења. Чини инжењеринг упита знатно једноставнијим и омогућава вам да градите LLM апликације производног квалитета.

Prompt flow може да се повеже са OpenAI, Azure OpenAI Service и прилагодљивим моделима (Huggingface, локални LLM/SLM). Надамо се да ћемо имплементирати квантовани ONNX модел Phi-3.5 у локалне апликације. Prompt flow нам може помоћи да боље испланирамо пословање и завршимо локална решења заснована на Phi-3.5. У овом примеру ћемо комбиновати ONNX Runtime GenAI библиотеку да завршимо Prompt flow решење засновано на Windows GPU-у.

## **Инсталација**

### **ONNX Runtime GenAI за Windows GPU**

Прочитајте овај водич за подешавање ONNX Runtime GenAI за Windows GPU [кликните овде](./ORTWindowGPUGuideline.md)

### **Подешавање Prompt flow у VSCode**

1. Инсталирајте Prompt flow VS Code екстензију

![pfvscode](../../../../../../translated_images/pfvscode.eff93dfc66a42cbef699fc16fa48f3ed3a23361875a3362037d026896395a00d.sr.png)

2. Након инсталације Prompt flow VS Code екстензије, кликните на екстензију и изаберите **Installation dependencies** пратите овај водич да инсталирате Prompt flow SDK у вашем окружењу

![pfsetup](../../../../../../translated_images/pfsetup.b46e93096f5a254f74e8b74ce2be7047ce963ef573d755ec897eb1b78cb9c954.sr.png)

3. Преузмите [пример кода](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) и отворите га у VS Code-у

![pfsample](../../../../../../translated_images/pfsample.8d89e70584ffe7c4dba182513e3148a989e552c3b8e4948567a6b806b5ae1845.sr.png)

4. Отворите **flow.dag.yaml** да изаберете ваше Python окружење

![pfdag](../../../../../../translated_images/pfdag.264a77f7366458ff850a76ae949226391ea382856d543ef9da4b92096aff7e4b.sr.png)

   Отворите **chat_phi3_ort.py** да промените локацију вашег Phi-3.5-instruct ONNX модела

![pfphi](../../../../../../translated_images/pfphi.72da81d74244b45fc78cdfeeb8c7fbd9e7cd610bf2f96814dbade6a4a2dfad7e.sr.png)

5. Покрените ваш prompt flow за тестирање

Отворите **flow.dag.yaml** и кликните на визуелни едитор

![pfv](../../../../../../translated_images/pfv.ba8a81f34b20f603cccee3fe91e94113792ed6f5af28f76ab08e1a0b3e77b33b.sr.png)

Након клика, покрените га за тестирање

![pfflow](../../../../../../translated_images/pfflow.4e1135a089b1ce1b6348b59edefdb6333e5729b54c8e57f9039b7f9463e68fbd.sr.png)

1. Можете покренути batch у терминалу да проверите више резултата


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Резултате можете проверити у вашем подразумеваном прегледачу


![pfresult](../../../../../../translated_images/pfresult.c22c826f8062d7cbe871cff35db4a013dcfefc13fafe5da6710a8549a96a4ceb.sr.png)

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI сервиса за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо прецизности, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.