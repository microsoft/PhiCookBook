<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-03-27T12:50:36+00:00",
  "source_file": "md\\02.Application\\04.Vision\\Phi3\\E2E_Nvidia_NIM_Vision.md",
  "language_code": "ru"
}
-->
### Пример сценария

Представьте, что у вас есть изображение (`demo.png`), и вы хотите сгенерировать Python-код, который обработает это изображение и сохранит его новую версию (`phi-3-vision.jpg`).

Приведённый выше код автоматизирует этот процесс, выполняя следующие шаги:

1. Настройка окружения и необходимых конфигураций.
2. Создание запроса, который инструктирует модель сгенерировать требуемый Python-код.
3. Отправка запроса модели и получение сгенерированного кода.
4. Извлечение и выполнение сгенерированного кода.
5. Отображение оригинального и обработанного изображений.

Этот подход использует возможности ИИ для автоматизации задач обработки изображений, делая их выполнение проще и быстрее.

[Пример решения кода](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Давайте разберём, что делает весь код шаг за шагом:

1. **Установка необходимого пакета**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Эта команда устанавливает пакет `langchain_nvidia_ai_endpoints`, гарантируя, что используется его последняя версия.

2. **Импорт необходимых модулей**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Эти импорты добавляют необходимые модули для взаимодействия с NVIDIA AI endpoints, безопасной работы с паролями, взаимодействия с операционной системой и кодирования/декодирования данных в формате base64.

3. **Настройка API-ключа**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Этот код проверяет, установлен ли переменная окружения `NVIDIA_API_KEY`. Если нет, он запрашивает у пользователя ввод API-ключа безопасным способом.

4. **Определение модели и пути к изображению**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Здесь задаётся используемая модель, создаётся экземпляр `ChatNVIDIA` с указанной моделью и определяется путь к файлу изображения.

5. **Создание текстового запроса**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Этот шаг формирует текстовый запрос, который инструктирует модель сгенерировать Python-код для обработки изображения.

6. **Кодирование изображения в base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Этот код читает файл изображения, кодирует его в формате base64 и создаёт HTML-тег изображения с закодированными данными.

7. **Объединение текста и изображения в запрос**:
    ```python
    prompt = f"{text} {image}"
    ```
    Здесь текстовый запрос и HTML-тег изображения объединяются в одну строку.

8. **Генерация кода с использованием ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Этот код отправляет запрос в `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` строку.

9. **Извлечение Python-кода из сгенерированного содержимого**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Этот шаг извлекает фактический Python-код из сгенерированного содержимого, удаляя форматирование markdown.

10. **Выполнение сгенерированного кода**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Этот шаг выполняет извлечённый Python-код как подпроцесс и захватывает его вывод.

11. **Отображение изображений**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Эти строки отображают изображения с использованием модуля `IPython.display`.

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Хотя мы стремимся к точности, пожалуйста, учитывайте, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неверные интерпретации, возникающие в результате использования данного перевода.