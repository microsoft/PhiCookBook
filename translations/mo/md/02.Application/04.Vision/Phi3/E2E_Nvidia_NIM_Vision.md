<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "99474e9687279d0657412c806856b559",
  "translation_date": "2025-04-04T13:00:55+00:00",
  "source_file": "md\\02.Application\\04.Vision\\Phi3\\E2E_Nvidia_NIM_Vision.md",
  "language_code": "mo"
}
-->
### Misali Yanayi

Ka yi tunanin kana da hoton (`demo.png`) kuma kana son samar da lambar Python da za ta sarrafa wannan hoto ta kuma adana sabon nau'in sa (`phi-3-vision.jpg`).

Lambar da ke sama tana sarrafa wannan tsari ta hanyar:

1. Kafa muhalli da kuma abubuwan da ake bukata.
2. Kirkirar wani umarni da ke ba da shawara ga samfurin don samar da lambar Python da ake bukata.
3. Aika umarnin zuwa samfurin da kuma tattara lambar da aka samar.
4. Ciro da gudanar da lambar da aka samar.
5. Nuna hoton asali da wanda aka sarrafa.

Wannan dabarar tana amfani da karfin AI don sarrafa ayyukan sarrafa hoto, tana saukaka da kuma sauri wajen cimma burinka.

[Samfurin Maganin Lamba](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Bari mu bayyana abin da duka lambar ke yi mataki-mataki:

1. **Shigar da Kunshin da ake Bukata**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Wannan umarni yana shigar da kunshin `langchain_nvidia_ai_endpoints`, yana tabbatar da cewa sabuwar sigar ce.

2. **Shigo da Moduli da ake Bukata**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Wadannan abubuwan shigo da suke kawo moduli da ake bukata don yin hulɗa da hanyoyin AI na NVIDIA, sarrafa kalmomin shiga cikin tsaro, yin hulɗa da tsarin aiki, da kuma loda/karanta bayanai a tsarin base64.

3. **Kafa Maɓallin API**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Wannan lambar tana duba ko an kafa mahallin `NVIDIA_API_KEY`. Idan ba haka ba, tana tambayar mai amfani don shigar da maɓallin API cikin tsaro.

4. **Bayyana Samfurin da Hanyar Hoton**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Wannan yana kafa samfurin da za a yi amfani da shi, yana ƙirƙirar wani abu na `ChatNVIDIA` tare da samfurin da aka fayyace, da kuma bayyana hanyar fayil ɗin hoton.

5. **Kirkirar Umarnin Rubutu**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Wannan yana fayyace wani umarnin rubutu wanda yake umartar samfurin don samar da lambar Python don sarrafa hoto.

6. **Loda Hoton a Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Wannan lambar tana karanta fayil ɗin hoton, tana loda shi a tsarin base64, kuma tana ƙirƙirar alamar HTML na hoto tare da bayanan da aka loda.

7. **Hada Rubutu da Hoto cikin Umarnin**:
    ```python
    prompt = f"{text} {image}"
    ```
    Wannan yana haɗa umarnin rubutu da alamar HTML na hoto cikin tsari guda.

8. **Samar da Lamba Tare da ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Wannan lambar tana aika umarnin zuwa `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` string.

9. **Ciro Lambar Python daga Abun da Aka Samar**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Wannan yana cire lambar Python daga abun da aka samar ta hanyar cire tsarin markdown.

10. **Gudanar da Lambar da Aka Samar**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Wannan tana gudanar da lambar Python da aka cire a matsayin subprocess tana kuma tattara sakamakonta.

11. **Nuna Hotuna**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Wadannan layukan suna nuna hotuna ta amfani da `IPython.display`.

It seems you've requested a translation to "mo," but could you clarify what "mo" refers to? Are you referring to a specific language or dialect (e.g., Maori, Mongolian, or something else)? Providing more context will help me assist you accurately!