### Примерен сценарий

Представете си, че имате изображение (`demo.png`) и искате да генерирате Python код, който обработва това изображение и запазва нова версия на файла (`phi-3-vision.jpg`).

Горният код автоматизира този процес чрез:

1. Настройване на средата и необходимите конфигурации.
2. Създаване на prompt, който инструктира модела да генерира необходимия Python код.
3. Изпращане на prompt-а към модела и събиране на генерирания код.
4. Извличане и изпълнение на генерирания код.
5. Показване на оригиналното и обработеното изображение.

Този подход използва силата на изкуствения интелект за автоматизиране на задачи по обработка на изображения, което прави постигането на целите ви по-лесно и по-бързо.

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Нека разгледаме какво прави целият код стъпка по стъпка:

1. **Инсталиране на необходимия пакет**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Тази команда инсталира пакета `langchain_nvidia_ai_endpoints`, като гарантира, че е най-новата версия.

2. **Импортиране на необходими модули**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Тези импорти зареждат необходимите модули за взаимодействие с NVIDIA AI endpoints, сигурно въвеждане на пароли, работа с операционната система и кодиране/декодиране на данни в base64 формат.

3. **Настройване на API ключ**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Този код проверява дали променливата на средата `NVIDIA_API_KEY` е зададена. Ако не е, подканва потребителя да въведе своя API ключ по сигурен начин.

4. **Дефиниране на модела и пътя към изображението**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Тук се задава моделът, създава се инстанция на `ChatNVIDIA` с посочения модел и се дефинира пътят към файла с изображението.

5. **Създаване на текстов prompt**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Този prompt инструктира модела да генерира Python код за обработка на изображение.

6. **Кодиране на изображението в Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Този код чете файла с изображението, кодира го в base64 и създава HTML таг за изображение с кодираните данни.

7. **Комбиниране на текста и изображението в prompt**:
    ```python
    prompt = f"{text} {image}"
    ```
    Тук текстовият prompt и HTML тагът за изображението се обединяват в един низ.

8. **Генериране на код с помощта на ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Този код изпраща prompt-а към модела `ChatNVIDIA` и събира генерирания код на части, като отпечатва и добавя всяка част към низа `code`.

9. **Извличане на Python кода от генерираното съдържание**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Тук се извлича реалният Python код от генерираното съдържание, като се премахва markdown форматирането.

10. **Изпълнение на генерирания код**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Този код изпълнява извлечения Python код като подпроцес и улавя неговия изход.

11. **Показване на изображенията**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Тези редове показват изображенията с помощта на модула `IPython.display`.

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.