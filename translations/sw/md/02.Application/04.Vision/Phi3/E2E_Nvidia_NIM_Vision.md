<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-05-09T19:57:47+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "sw"
}
-->
### Mfano wa Hali

Fikiria una picha (`demo.png`) na unataka kuzalisha msimbo wa Python unaoshughulikia picha hii na kuhifadhi toleo jipya la picha (`phi-3-vision.jpg`).

Msimbo uliotangulia unaharakisha mchakato huu kwa:

1. Kuweka mazingira na usanidi unaohitajika.
2. Kuunda maelekezo yanayoelekeza modeli kuzalisha msimbo wa Python unaohitajika.
3. Kutuma maelekezo kwa modeli na kukusanya msimbo uliotengenezwa.
4. Kutoa na kuendesha msimbo uliotengenezwa.
5. Kuonyesha picha asilia na zilizoshughulikiwa.

Njia hii inatumia nguvu ya AI kuharakisha kazi za usindikaji picha, na kufanya iwe rahisi na haraka kufanikisha malengo yako.

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Tuchambue hatua kwa hatua kile msimbo mzima unachofanya:

1. **Sakinisha Kifurushi Kinachohitajika**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Amri hii inasakinisha kifurushi `langchain_nvidia_ai_endpoints`, kuhakikisha kinakuwa toleo la hivi karibuni.

2. **Ingiza Moduli Zinazohitajika**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Ingizo hizi huleta moduli muhimu za kuingiliana na NVIDIA AI endpoints, kushughulikia nywila kwa usalama, kuingiliana na mfumo wa uendeshaji, na kuunda/kutafsiri data kwa muundo wa base64.

3. **Weka API Key**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Msimbo huu unakagua kama mazingira ya `NVIDIA_API_KEY` yamewekwa. Ikiwa hayajashikwa, huuliza mtumiaji kuingiza API key yao kwa usalama.

4. **Tambua Modeli na Njia ya Picha**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Hii inaweka modeli itakayotumika, kuunda mfano wa `ChatNVIDIA` na modeli iliyobainishwa, na kubainisha njia ya faili ya picha.

5. **Unda Maelekezo ya Maandishi**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Hii inaelezea maelekezo ya maandishi yanayoelekeza modeli kuzalisha msimbo wa Python kwa ajili ya usindikaji picha.

6. **Fasiri Picha kwa Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Msimbo huu unasoma faili la picha, kuifasiri kwa base64, na kuunda tagi ya HTML ya picha yenye data iliyofasiriwa.

7. **Changanya Maandishi na Picha Kuunda Maelekezo**:
    ```python
    prompt = f"{text} {image}"
    ```
    Hii inaunganisha maelekezo ya maandishi na tagi ya picha ya HTML kuwa mfuatano mmoja.

8. **Zalisha Msimbo kwa Kutumia ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Msimbo huu hutuma maelekezo kwa `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` string.

9. **Toa Msimbo wa Python kutoka kwa Maudhui yaliyotengenezwa**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Hii hutoa msimbo halisi wa Python kutoka kwa maudhui yaliyotengenezwa kwa kuondoa muundo wa markdown.

10. **Endesha Msimbo Uliotengenezwa**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Hii inaendesha msimbo wa Python uliotolewa kama mchakato mdogo na kunasa matokeo yake.

11. **Onyesha Picha**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Mistari hii inaonyesha picha kwa kutumia moduli ya `IPython.display`.

**Kiasi cha Majumuisho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upotovu wa maana. Hati asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha kuaminika. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatuna dhamana kwa maelewano au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.