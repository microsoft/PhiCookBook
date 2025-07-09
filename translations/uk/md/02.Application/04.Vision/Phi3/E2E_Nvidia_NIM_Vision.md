<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-07-09T19:30:06+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "uk"
}
-->
### Приклад сценарію

Уявіть, що у вас є зображення (`demo.png`), і ви хочете згенерувати Python-код, який обробляє це зображення та зберігає нову версію (`phi-3-vision.jpg`).

Наведений вище код автоматизує цей процес, виконуючи:

1. Налаштування середовища та необхідних конфігурацій.
2. Створення підказки, яка дає інструкції моделі згенерувати потрібний Python-код.
3. Надсилання підказки моделі та збір згенерованого коду.
4. Витягування та запуск згенерованого коду.
5. Відображення оригінального та обробленого зображень.

Такий підхід використовує потужність ШІ для автоматизації завдань обробки зображень, роблячи процес простішим і швидшим.

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Розглянемо покроково, що робить увесь код:

1. **Встановлення необхідного пакету**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Ця команда встановлює пакет `langchain_nvidia_ai_endpoints`, забезпечуючи його актуальну версію.

2. **Імпорт необхідних модулів**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Ці імпорти підключають потрібні модулі для взаємодії з NVIDIA AI endpoints, безпечного введення паролів, роботи з операційною системою та кодування/декодування даних у форматі base64.

3. **Налаштування API ключа**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Цей код перевіряє, чи встановлена змінна середовища `NVIDIA_API_KEY`. Якщо ні, він безпечно запитує у користувача введення API ключа.

4. **Визначення моделі та шляху до зображення**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Тут задається модель для використання, створюється екземпляр `ChatNVIDIA` з вказаною моделлю, а також визначається шлях до файлу зображення.

5. **Створення текстової підказки**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Визначається текстова підказка, яка дає інструкції моделі згенерувати Python-код для обробки зображення.

6. **Кодування зображення у base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Цей код зчитує файл зображення, кодує його у base64 та створює HTML-тег зображення з закодованими даними.

7. **Об’єднання тексту та зображення у підказку**:
    ```python
    prompt = f"{text} {image}"
    ```
    Тут текстова підказка та HTML-тег зображення об’єднуються в один рядок.

8. **Генерація коду за допомогою ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Цей код надсилає підказку моделі `ChatNVIDIA` і збирає згенерований код по частинах, виводячи та додаючи кожну частину до рядка `code`.

9. **Витягування Python-коду зі згенерованого вмісту**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Цей крок виділяє власне Python-код зі згенерованого вмісту, видаляючи markdown-форматування.

10. **Запуск згенерованого коду**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Тут витягнутий Python-код запускається як підпроцес, а його вивід захоплюється.

11. **Відображення зображень**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Ці рядки відображають зображення за допомогою модуля `IPython.display`.

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.