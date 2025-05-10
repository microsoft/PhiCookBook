<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-05-09T19:58:32+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "bg"
}
-->
### Примерен сценарий

Представете си, че имате изображение (`demo.png`) и искате да генерирате Python код, който обработва това изображение и записва нова версия (`phi-3-vision.jpg`).

Горният код автоматизира този процес, като:

1. Настройва средата и необходимите конфигурации.
2. Създава prompt, който инструктира модела да генерира необходимия Python код.
3. Изпраща prompt-а към модела и събира генерирания код.
4. Извлича и изпълнява генерирания код.
5. Показва оригиналното и обработеното изображение.

Този подход използва силата на изкуствения интелект, за да автоматизира задачи по обработка на изображения, правейки процеса по-лесен и по-бърз за постигане на целите ви.

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Нека разгледаме какво прави целият код стъпка по стъпка:

1. **Инсталиране на необходимия пакет**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Тази команда инсталира пакета `langchain_nvidia_ai_endpoints`, като гарантира, че е най-актуалната версия.

2. **Импортиране на необходими модули**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Тези импорти добавят необходимите модули за взаимодействие с NVIDIA AI endpoints, сигурно въвеждане на пароли, работа с операционната система и кодиране/декодиране в base64 формат.

3. **Настройка на API ключ**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Този код проверява дали променливата на средата `NVIDIA_API_KEY` е зададена. Ако не е, подканва потребителя да въведе API ключа си по сигурен начин.

4. **Дефиниране на модел и път към изображението**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Тук се задава моделът за използване, създава се инстанция на `ChatNVIDIA` с избрания модел и се дефинира пътят към файла с изображението.

5. **Създаване на текстов prompt**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Този код дефинира текстов prompt, който инструктира модела да генерира Python код за обработка на изображение.

6. **Кодиране на изображението в Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Тук се чете файла с изображението, кодира се в base64 и се създава HTML таг за изображение с кодираното съдържание.

7. **Комбиниране на текста и изображението в prompt**:
    ```python
    prompt = f"{text} {image}"
    ```
    Този код обединява текстовия prompt и HTML тага за изображение в един низ.

8. **Генериране на код с помощта на ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Този код изпраща prompt-а към `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` низ.

9. **Извличане на Python кода от генерираното съдържание**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Тук се извлича действителният Python код от генерираното съдържание чрез премахване на markdown форматирането.

10. **Изпълнение на генерирания код**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Този код изпълнява извлечения Python код като под-процес и улавя изхода му.

11. **Показване на изображенията**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Тези редове показват изображенията чрез модула `IPython.display`.

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за никакви недоразумения или неправилни тълкувания, произтичащи от използването на този превод.