<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-07-17T03:04:48+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "uk"
}
-->
# Використання Windows GPU для створення рішення Prompt flow з Phi-3.5-Instruct ONNX

Цей документ є прикладом того, як використовувати PromptFlow з ONNX (Open Neural Network Exchange) для розробки AI-додатків на основі моделей Phi-3.

PromptFlow — це набір інструментів для розробки, створений для оптимізації повного циклу розробки AI-додатків на базі LLM (великі мовні моделі), від ідеї та прототипування до тестування та оцінки.

Інтегруючи PromptFlow з ONNX, розробники можуть:

- Оптимізувати продуктивність моделі: використовувати ONNX для ефективного виконання та розгортання моделей.
- Спрощувати розробку: застосовувати PromptFlow для керування робочим процесом і автоматизації рутинних завдань.
- Покращувати співпрацю: забезпечувати кращу взаємодію між членами команди завдяки єдиному середовищу розробки.

**Prompt flow** — це набір інструментів для розробки, який допомагає оптимізувати повний цикл створення AI-додатків на основі LLM: від ідеї, прототипування, тестування, оцінки до розгортання в продакшн і моніторингу. Він значно спрощує інженерію промптів і дозволяє створювати LLM-додатки з якістю, придатною для продакшну.

Prompt flow може підключатися до OpenAI, Azure OpenAI Service та налаштовуваних моделей (Huggingface, локальні LLM/SLM). Ми плануємо розгорнути квантизовану ONNX-модель Phi-3.5 у локальних додатках. Prompt flow допоможе нам краще планувати бізнес і створювати локальні рішення на основі Phi-3.5. У цьому прикладі ми поєднаємо ONNX Runtime GenAI Library для створення рішення Prompt flow на базі Windows GPU.

## **Встановлення**

### **ONNX Runtime GenAI для Windows GPU**

Прочитайте цю інструкцію, щоб налаштувати ONNX Runtime GenAI для Windows GPU [натисніть тут](./ORTWindowGPUGuideline.md)

### **Налаштування Prompt flow у VSCode**

1. Встановіть розширення Prompt flow для VS Code

![pfvscode](../../../../../../translated_images/pfvscode.eff93dfc66a42cbef699fc16fa48f3ed3a23361875a3362037d026896395a00d.uk.png)

2. Після встановлення розширення Prompt flow для VS Code, натисніть на розширення та оберіть **Installation dependencies**, дотримуйтесь цієї інструкції, щоб встановити Prompt flow SDK у вашому середовищі

![pfsetup](../../../../../../translated_images/pfsetup.b46e93096f5a254f74e8b74ce2be7047ce963ef573d755ec897eb1b78cb9c954.uk.png)

3. Завантажте [Приклад коду](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) і відкрийте його у VS Code

![pfsample](../../../../../../translated_images/pfsample.8d89e70584ffe7c4dba182513e3148a989e552c3b8e4948567a6b806b5ae1845.uk.png)

4. Відкрийте **flow.dag.yaml**, щоб обрати ваше Python-середовище

![pfdag](../../../../../../translated_images/pfdag.264a77f7366458ff850a76ae949226391ea382856d543ef9da4b92096aff7e4b.uk.png)

   Відкрийте **chat_phi3_ort.py**, щоб змінити шлях до вашої ONNX-моделі Phi-3.5-instruct

![pfphi](../../../../../../translated_images/pfphi.72da81d74244b45fc78cdfeeb8c7fbd9e7cd610bf2f96814dbade6a4a2dfad7e.uk.png)

5. Запустіть ваш prompt flow для тестування

Відкрийте **flow.dag.yaml** і натисніть візуальний редактор

![pfv](../../../../../../translated_images/pfv.ba8a81f34b20f603cccee3fe91e94113792ed6f5af28f76ab08e1a0b3e77b33b.uk.png)

Після цього натисніть запуск для тестування

![pfflow](../../../../../../translated_images/pfflow.4e1135a089b1ce1b6348b59edefdb6333e5729b54c8e57f9039b7f9463e68fbd.uk.png)

1. Ви можете запускати пакетні завдання у терміналі, щоб переглянути більше результатів


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Результати можна переглянути у вашому браузері за замовчуванням


![pfresult](../../../../../../translated_images/pfresult.c22c826f8062d7cbe871cff35db4a013dcfefc13fafe5da6710a8549a96a4ceb.uk.png)

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.