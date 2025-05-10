<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-05-09T19:57:38+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "tl"
}
-->
### Halimbawa ng Senaryo

Isipin mo na mayroon kang isang larawan (`demo.png`) at nais mong gumawa ng Python code na magpoproseso sa larawang ito at magsasave ng bagong bersyon nito (`phi-3-vision.jpg`).

Ang code sa itaas ay awtomatikong ginagawa ang prosesong ito sa pamamagitan ng:

1. Pagsasaayos ng kapaligiran at mga kinakailangang setting.
2. Paggawa ng prompt na nagsasabi sa modelo na gumawa ng kinakailangang Python code.
3. Pagpapadala ng prompt sa modelo at pagkolekta ng nagawang code.
4. Pagkuha at pagpapatakbo ng nagawang code.
5. Pagpapakita ng orihinal at naprosesong mga larawan.

Ginagamit ng pamamaraang ito ang lakas ng AI upang gawing awtomatiko ang mga gawain sa pagpoproseso ng larawan, kaya mas madali at mabilis mong makamit ang iyong mga layunin.

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Hatiin natin kung ano ang ginagawa ng buong code, hakbang-hakbang:

1. **I-install ang Kinakailangang Package**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Ini-install ng utos na ito ang `langchain_nvidia_ai_endpoints` package, tinitiyak na ito ay ang pinakabagong bersyon.

2. **I-import ang mga Kinakailangang Module**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Dinadala ng mga import na ito ang mga module na kailangan para makipag-ugnayan sa NVIDIA AI endpoints, ligtas na paghawak ng password, pakikipag-ugnayan sa operating system, at pag-encode/decode ng data sa base64 na format.

3. **I-set Up ang API Key**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Sinusuri ng code na ito kung naka-set ang `NVIDIA_API_KEY` environment variable. Kung hindi, hinihingi nito sa user na ipasok nang ligtas ang kanilang API key.

4. **Itakda ang Modelo at Path ng Larawan**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Itinatakda nito ang modelong gagamitin, gumagawa ng instance ng `ChatNVIDIA` gamit ang tinukoy na modelo, at inilalagay ang path ng file ng larawan.

5. **Gumawa ng Text Prompt**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Itinatakda nito ang isang text prompt na nagsasabi sa modelo na gumawa ng Python code para iproseso ang larawan.

6. **I-encode ang Larawan sa Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Binabasa ng code na ito ang file ng larawan, ini-encode ito sa base64, at gumagawa ng HTML image tag gamit ang naka-encode na data.

7. **Pagsamahin ang Text at Larawan sa Prompt**:
    ```python
    prompt = f"{text} {image}"
    ```
    Pinagsasama nito ang text prompt at ang HTML image tag sa isang string.

8. **Gumawa ng Code Gamit ang ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Ipinapadala ng code na ito ang prompt sa `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` string.

9. **Kunin ang Python Code mula sa Nagawang Nilalaman**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Kinukuha nito ang aktwal na Python code mula sa nagawang nilalaman sa pamamagitan ng pagtanggal ng markdown formatting.

10. **Patakbuhin ang Nagawang Code**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Pinapatakbo nito ang nakuha na Python code bilang subprocess at kinukuha ang output nito.

11. **Ipakita ang mga Larawan**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Ipinapakita ng mga linyang ito ang mga larawan gamit ang `IPython.display` module.

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang serbisyong AI na pagsasalin [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, mangyaring tandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasaling-tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.