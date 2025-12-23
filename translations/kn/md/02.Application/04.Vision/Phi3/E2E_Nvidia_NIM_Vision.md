<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-12-21T22:02:44+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "kn"
}
-->
### ಉದಾಹರಣಾ ದೃಶ್ಯ

ನೀವು ಒಂದು ಚಿತ್ರ (`demo.png`) ಹೊಂದಿದ್ದೀರಿ ಎಂದು ಭಾವಿಸಿ ಮತ್ತು ಆ ಚಿತ್ರವನ್ನು ಪ್ರಕ್ರಿಯೆಗೊಳಿಸಿ ಅದರ ಹೊಸ ಪ್ರತಿಯನ್ನು (`phi-3-vision.jpg`) ಉಳಿಸುವ Python ಕೋಡ್ ಅನ್ನು ರಚಿಸಲು ನೀವು ಬಯಸುತ್ತೀರಿ. 

ಮೇಲಿನ ಕೋಡ್ ಈ ಪ್ರಕ್ರಿಯೆಯನ್ನು ಸ್ವಯಂಚಾಲಿತಗೊಳಿಸುತ್ತದೆ:

1. ಪರಿಸರ ಮತ್ತು ಅಗತ್ಯ ಕಾನ್ಫಿಗರೇಶನ್‌ಗಳನ್ನು ಸಂರಚಿಸುವುದು.
2. ಮಾದರಿಯನ್ನು ಅಗತ್ಯ Python ಕೋಡ್ ರಚಿಸಲು ಸೂಚಿಸುವ ಪ್ರಾಂಪ್ಟ್ ರಚಿಸುವುದು.
3. ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು ಮಾದರಿಗೆ ಕಳುಹಿಸುವುದು ಮತ್ತು ಉತ್ಪನ್ನವಾದ ಕೋಡ್ ಅನ್ನು ಸಂಗ್ರಹಿಸುವುದು.
4. ಉತ್ಪನ್ನವಾದ ಕೋಡ್ ಅನ್ನು ಹೊರತೆಗೆದು ಓಡಿಸುವುದು.
5. ಮೂಲ ಮತ್ತು ಪ್ರಕ್ರಿಯೆಗೊಳಿಸಿದ ಚಿತ್ರಗಳನ್ನು ಪ್ರದರ್ಶಿಸುವುದು.

[ನಮೂನಾ ಕೋಡ್ ಪರಿಹಾರ](../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

ಈ ಸಂಪೂರ್ಣ ಕೋಡ್ ಹಂತ ಹಂತವಾಗಿ ಏನು ಮಾಡುತ್ತದೆ ಎಂಬುದನ್ನು ವಿವರಿಸೋಣ:

1. **Install Required Package**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    ಈ ಕಮಾಂಡ್ `langchain_nvidia_ai_endpoints` ಪ್ಯಾಕೇಜ್ ಅನ್ನು ಸ್ಥಾಪಿಸುತ್ತದೆ ಮತ್ತು ಅದು ಇತ್ತೀಚಿನ ಆವೃತ್ತಿಯಲ್ಲಿತ್ತೆಂದು ಖಚಿತಪಡಿಸುತ್ತದೆ.

2. **Import Necessary Modules**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    ಈ ಇಂಪೋರ್ಟ್‌ಗಳು NVIDIA AI ಎಂಡ್ಪಾಯಿಂಟ್‌ಗಳೊಂದಿಗೆ ಸಂವಹನ ನಡೆಸಲು, ಪಾಸ್‌ವರ್ಡ್‌ಗಳನ್ನು ಸುರಕ್ಷಿತವಾಗಿ ನಿರ್ವಹಿಸಲು, ಆಪರೇಟಿಂಗ್ ಸಿಸ್ಟಮ್ ಜೊತೆ ಸಂವಹನ ಮಾಡಲು ಮತ್ತು ಡೇಟಾವನ್ನು base64 ಸ್ವರೂಪದಲ್ಲಿ ಎನ್ಕೋಡ್/ಡಿಕೋಡ್ ಮಾಡಲು ಅಗತ್ಯವಾದ ಮಾಡ್ಯೂಲ್‌ಗಳನ್ನು ತರುತ್ತವೆ.

3. **Set Up API Key**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    ಈ ಕೋಡ್ `NVIDIA_API_KEY` ಪರಿಸರ ಚರವನ್ನು ಸೆಟ್ ಮಾಡಲಾಗಿದೆ ಎಂಬುದನ್ನು ಪರಿಶೀಲಿಸುತ್ತದೆ. ಇಲ್ಲದಿದ್ದಲ್ಲಿ, ಬಳಕೆದಾರರಿಗೆ ಅವರ API ಕೀ ಅನ್ನು ಸುರಕ್ಷಿತವಾಗಿ ನಮೂದಿಸಲು ಕೇಳುತ್ತದೆ.

4. **Define Model and Image Path**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    ಇದು ಬಳಸಬೇಕಾದ ಮಾದರಿಯನ್ನು ನಿಗದಿಮಾಡುತ್ತದೆ, ಆ ಮಾದರಿಯೊಂದಿಗೆ `ChatNVIDIA` ಇನ್ಸ್ಟಾನ್ಸ್ ಅನ್ನು ರಚಿಸುತ್ತದೆ, ಮತ್ತು ಚಿತ್ರ ಫೈಲಿನ ಮಾರ್ಗವನ್ನು ವಿವರಿಸುತ್ತದೆ.

5. **Create Text Prompt**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    ಇದು ಒಂದು ಪಠ್ಯ ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು ವ್ಯಾಖ್ಯಾನಿಸುತ್ತದೆ, ಅದು ಮಾದರಿಯನ್ನು ಚಿತ್ರವನ್ನು ಪ್ರಕ್ರಿಯೆಗೊಳಿಸುವ Python ಕೋಡ್ ರಚಿಸಲು ಸೂಚಿಸುತ್ತದೆ.

6. **Encode Image in Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    ಈ ಕೋಡ್ ಚಿತ್ರ ಫೈಲ್ ಅನ್ನು ಓದಿ, ಅದನ್ನು base64 ನಲ್ಲಿ ಎನ್‌ಕೋಡ್ ಮಾಡಿ, ಎನ್‌ಕೋಡ್ ಮಾಡಿದ ಡೇಟಾ ಜೊತೆ HTML ಚಿತ್ರ ಟ್ಯಾಗ್ ರಚಿಸುತ್ತದೆ.

7. **Combine Text and Image into Prompt**:
    ```python
    prompt = f"{text} {image}"
    ```
    ಇದು ಪಠ್ಯ ಪ್ರಾಂಪ್ಟ್ ಮತ್ತು HTML ಚಿತ್ರ ಟ್ಯಾಗ್ ಅನ್ನು ಒಂದೇ ಸ್ಟ್ರಿಂಗ್ ಆಗಿ ಸಂಯೋಜಿಸುತ್ತದೆ.

8. **Generate Code Using ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    ಈ ಕೋಡ್ ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು `ChatNVIDIA` ಮಾದರಿಗೆ ಕಳುಹಿಸಿ ಉತ್ಪನ್ನವಾದ ಕೋಡ್ ಅನ್ನು ತುಂಡು ತುಂಡಾಗಿ ಸಂಗ್ರಹಿಸುತ್ತದೆ, ಪ್ರತಿಯೊಂದು ತುಂಡನ್ನು ತೋರಿಸಿ ಮತ್ತು `code` ಸ್ಟ್ರಿಂಗ್‌ಗೆ ಸೇರಿಸುತ್ತದೆ.

9. **Extract Python Code from Generated Content**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    ಇದು markdown ಸ್ವರೂಪವನ್ನು ತೆಗೆದುಹಾಕಿ ಉತ್ಪನ್ನವಾದ ವಿಷಯದಿಂದ ನಿಜವಾದ Python ಕೋಡ್ ಅನ್ನು ಹೊರತೆಗೆದುಕೊಳ್ಳುತ್ತದೆ.

10. **Run the Generated Code**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    ಇದು ಹೊರತೆಗೆದ Python ಕೋಡ್ ಅನ್ನು subprocess ಆಗಿ ಚಾಲನೆ ಮಾಡಿ ಅದರ ಔಟ್‌ಪುಟ್ ಅನ್ನು ಸೆರೆಹಿಡಿಯುತ್ತದೆ.

11. **Display Images**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    ಈ ಸಾಲುಗಳು `IPython.display` ಮಾಡ್ಯೂಲ್ ಅನ್ನು ಉಪಯೋಗಿಸಿ ಚಿತ್ರಗಳನ್ನು ಪ್ರದರ್ಶಿಸುತ್ತವೆ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ಅಸ್ವೀಕರಣ:
ಈ ದಾಖಲೆಯನ್ನು AI ಅನುವಾದ ಸೇವೆ Co‑op Translator (https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಕಾಯ್ದುಕೊಳ್ಳಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸಂಬದ್ಧತೆಗಳು ಇರಬಹುದು ಎಂಬುದನ್ನು ದಯವಿಟ್ಟು ಗಮನಿಸಿರಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಾಖಲೆನ್ನು ಆದಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಗಂಭೀರ ಅಥವಾ ನಿರ್ಧಾರಾತ್ಮಕ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ತಿಳಿವಳಿಕೆಗಳು ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳಿಗಾಗಿ ನಾವು ಜವಾಬ್ದಾರಿಯನ್ನು ಹೊತ್ತುಕೊಳ್ಳುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->