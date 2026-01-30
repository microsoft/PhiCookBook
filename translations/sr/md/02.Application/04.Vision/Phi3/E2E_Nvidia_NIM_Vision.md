### Пример сценарија

Замислите да имате слику (`demo.png`) и желите да генеришете Python код који обрађује ту слику и сачува нову верзију (`phi-3-vision.jpg`).

Горњи код аутоматизује овај процес тако што:

1. Подешава окружење и неопходне конфигурације.
2. Креира упит који моделу даје инструкције да генерише потребан Python код.
3. Слање упита моделу и прикупљање генерисаног кода.
4. Извлачи и покреће генерисани код.
5. Приказује оригиналну и обрађену слику.

Овај приступ користи снагу вештачке интелигенције да аутоматизује задатке обраде слика, чинећи их једноставнијим и бржим за извођење.

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Хајде да корак по корак разложимо шта цео код ради:

1. **Инсталирање потребног пакета**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Ова команда инсталира пакет `langchain_nvidia_ai_endpoints`, осигуравајући да је најновија верзија.

2. **Увоз неопходних модула**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Ови увози доносе потребне модуле за интеракцију са NVIDIA AI endpoint-има, безбедно руковање лозинкама, рад са оперативним системом и кодирање/декодирање података у base64 формату.

3. **Подешавање API кључа**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Овај код проверава да ли је постављена `NVIDIA_API_KEY` променљива окружења. Ако није, тражи од корисника да безбедно унесе свој API кључ.

4. **Дефинисање модела и путање до слике**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Овде се подешава модел који ће се користити, креира инстанца `ChatNVIDIA` са наведеним моделом и дефинише путања до слике.

5. **Креирање текстуалног упита**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Овде се дефинише текстуални упит који моделу даје инструкције да генерише Python код за обраду слике.

6. **Кодирање слике у Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Овај код чита слику, кодира је у base64 и креира HTML таг за слику са кодираним подацима.

7. **Комбинација текста и слике у упит**:
    ```python
    prompt = f"{text} {image}"
    ```
    Овде се текстуални упит и HTML таг слике комбинују у један низ.

8. **Генерисање кода коришћењем ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Овај код шаље упит моделу `ChatNVIDIA` и прикупља генерисани код у деловима, штампајући и додајући сваки део у променљиву `code`.

9. **Извлачење Python кода из генерисаног садржаја**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Овде се из генерисаног садржаја уклања markdown форматирање и извлачи стварни Python код.

10. **Покретање генерисаног кода**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Овај код покреће издвојени Python код као subprocess и хвата његов излаз.

11. **Приказивање слика**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Ове линије приказују слике користећи модул `IPython.display`.

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која могу настати коришћењем овог превода.