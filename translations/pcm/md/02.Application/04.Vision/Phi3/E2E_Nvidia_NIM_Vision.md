### Example Scenario

Imagine say you get one image (`demo.png`) and you wan generate Python code wey go process dat image and save new version of am (`phi-3-vision.jpg`). 

Di code wey dey up dere dey automate dis process by:

1. Setting up di environment and necessary configurations.
2. Creating one prompt wey dey instruct di model make e generate di Python code wey dem need.
3. Sending di prompt go di model and collect di generated code.
4. Extracting and running di generated code.
5. Displaying di original and di processed images.

Dis approach dey use di power of AI to automate image processing tasks, make am easier and faster to reach your goals. 

[Sample Code Solution](../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Make we break down wetin di whole code dey do step by step:

1. **Install Required Package**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Dis command dey install di `langchain_nvidia_ai_endpoints` package, make sure say e be di latest version.

2. **Import Necessary Modules**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Dem imports dis bring di necessary modules wey you go need to interact wit di NVIDIA AI endpoints, handle passwords securely, interact wit di operating system, and encode/decode data for base64 format.

3. **Set Up API Key**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Dis code dey check if di `NVIDIA_API_KEY` environment variable don set. If e never set, e go prompt di user make dem enter dia API key securely.

4. **Define Model and Image Path**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Dis one set di model wey dem go use, create instance of `ChatNVIDIA` wit di specified model, and define di path to di image file.

5. **Create Text Prompt**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Dis one define text prompt wey dey tell di model make e generate Python code for processing one image.

6. **Encode Image in Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Dis code go read di image file, encode am for base64, and create one HTML image tag wit di encoded data.

7. **Combine Text and Image into Prompt**:
    ```python
    prompt = f"{text} {image}"
    ```
    Dis one combine di text prompt and di HTML image tag into one string.

8. **Generate Code Using ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Dis code send di prompt go di `ChatNVIDIA` model and collect di generated code in chunks, dey print and append each chunk to di `code` string.

9. **Extract Python Code from Generated Content**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Dis one extract di actual Python code from di generated content by removing di markdown formatting.

10. **Run the Generated Code**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Dis one run di extracted Python code as subprocess and capture di output.

11. **Display Images**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Dem lines dis dey display di images using di `IPython.display` module.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dis dokument don translate by AI translation service Co-op Translator (https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg note say automated translations fit get mistakes or wrong tins. Di original dokument for im own language na di official/authority source. For important mata, e better make professional human translator do am. We no dey responsible for any misunderstanding or wrong interpretation wey fit happen because of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->