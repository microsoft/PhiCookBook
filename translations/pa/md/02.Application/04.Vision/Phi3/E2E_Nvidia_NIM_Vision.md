<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-05-09T19:55:00+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "pa"
}
-->
### ਉਦਾਹਰਨ ਸਥਿਤੀ

ਕਲਪਨਾ ਕਰੋ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਇੱਕ ਚਿੱਤਰ ਹੈ (`demo.png`) ਅਤੇ ਤੁਸੀਂ ਇਸ ਚਿੱਤਰ ਨੂੰ ਪ੍ਰੋਸੈਸ ਕਰਨ ਅਤੇ ਇਸ ਦੀ ਇੱਕ ਨਵੀਂ ਵਰਜਨ ਸੇਵ ਕਰਨ ਲਈ Python ਕੋਡ ਬਣਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ (`phi-3-vision.jpg`)।

ਉਪਰ ਦਿੱਤਾ ਕੋਡ ਇਸ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਆਟੋਮੇਟ ਕਰਦਾ ਹੈ:

1. ਵਾਤਾਵਰਨ ਅਤੇ ਜਰੂਰੀ ਸੈਟਿੰਗਾਂ ਸੈੱਟ ਕਰਨਾ।
2. ਮਾਡਲ ਨੂੰ ਲੋੜੀਂਦਾ Python ਕੋਡ ਜਨਰੇਟ ਕਰਨ ਲਈ ਇੱਕ ਪ੍ਰੰਪਟ ਬਣਾਉਣਾ।
3. ਪ੍ਰੰਪਟ ਨੂੰ ਮਾਡਲ ਨੂੰ ਭੇਜਣਾ ਅਤੇ ਬਣਾਇਆ ਗਿਆ ਕੋਡ ਇਕੱਠਾ ਕਰਨਾ।
4. ਬਣਾਇਆ ਗਿਆ ਕੋਡ ਕੱਢਣਾ ਅਤੇ ਚਲਾਉਣਾ।
5. ਮੂਲ ਅਤੇ ਪ੍ਰੋਸੈਸ ਕੀਤੇ ਚਿੱਤਰਾਂ ਨੂੰ ਦਿਖਾਉਣਾ।

ਇਹ ਤਰੀਕਾ AI ਦੀ ਤਾਕਤ ਦਾ ਫਾਇਦਾ ਉਠਾਉਂਦਾ ਹੈ ਤਾਂ ਜੋ ਚਿੱਤਰ ਪ੍ਰੋਸੈਸਿੰਗ ਦੇ ਕੰਮ ਆਸਾਨ ਅਤੇ ਤੇਜ਼ ਹੋ ਜਾਣ।

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

ਆਓ ਪੂਰੇ ਕੋਡ ਨੂੰ ਕਦਮ ਦਰ ਕਦਮ ਸਮਝੀਏ:

1. **ਲੋੜੀਂਦਾ ਪੈਕੇਜ ਇੰਸਟਾਲ ਕਰੋ**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```  
    ਇਹ ਕਮਾਂਡ `langchain_nvidia_ai_endpoints` ਪੈਕੇਜ ਇੰਸਟਾਲ ਕਰਦੀ ਹੈ ਅਤੇ ਯਕੀਨੀ ਬਣਾਉਂਦੀ ਹੈ ਕਿ ਇਹ ਨਵੀਨਤਮ ਵਰਜਨ ਹੈ।

2. **ਜਰੂਰੀ ਮੋਡੀਊਲਾਂ ਇੰਪੋਰਟ ਕਰੋ**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```  
    ਇਹ ਇੰਪੋਰਟ NVIDIA AI endpoints ਨਾਲ ਕੰਮ ਕਰਨ, ਪਾਸਵਰਡ ਸੁਰੱਖਿਅਤ ਢੰਗ ਨਾਲ ਸੰਭਾਲਣ, ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ ਨਾਲ ਇੰਟਰੈਕਟ ਕਰਨ ਅਤੇ base64 ਫਾਰਮੈਟ ਵਿੱਚ ਡਾਟਾ ਐਨਕੋਡ/ਡੀਕੋਡ ਕਰਨ ਲਈ ਜਰੂਰੀ ਮੋਡੀਊਲ ਲਿਆਉਂਦੇ ਹਨ।

3. **API ਕੀ ਸੈੱਟ ਕਰੋ**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```  
    ਇਹ ਕੋਡ ਜਾਂਚਦਾ ਹੈ ਕਿ `NVIDIA_API_KEY` ਵਾਤਾਵਰਨ ਵੈਰੀਏਬਲ ਸੈੱਟ ਹੈ ਜਾਂ ਨਹੀਂ। ਜੇ ਨਹੀਂ, ਤਾਂ ਯੂਜ਼ਰ ਨੂੰ ਆਪਣੀ API ਕੀ ਸੁਰੱਖਿਅਤ ਢੰਗ ਨਾਲ ਦਰਜ ਕਰਨ ਲਈ ਕਹਿੰਦਾ ਹੈ।

4. **ਮਾਡਲ ਅਤੇ ਚਿੱਤਰ ਦਾ ਪਾਥ ਪਰਿਭਾਸ਼ਿਤ ਕਰੋ**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```  
    ਇਹ ਮਾਡਲ ਨੂੰ ਸੈੱਟ ਕਰਦਾ ਹੈ, `ChatNVIDIA` ਦਾ ਇੰਸਟੈਂਸ ਬਣਾਉਂਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਮਾਡਲ ਦਿੱਤਾ ਗਿਆ ਹੈ, ਅਤੇ ਚਿੱਤਰ ਫਾਈਲ ਦਾ ਪਾਥ ਦੱਸਦਾ ਹੈ।

5. **ਟੈਕਸਟ ਪ੍ਰੰਪਟ ਬਣਾਓ**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```  
    ਇਹ ਇੱਕ ਟੈਕਸਟ ਪ੍ਰੰਪਟ ਬਣਾਉਂਦਾ ਹੈ ਜੋ ਮਾਡਲ ਨੂੰ ਚਿੱਤਰ ਪ੍ਰੋਸੈਸਿੰਗ ਲਈ Python ਕੋਡ ਜਨਰੇਟ ਕਰਨ ਲਈ ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼ ਦਿੰਦਾ ਹੈ।

6. **ਚਿੱਤਰ ਨੂੰ base64 ਵਿੱਚ ਐਨਕੋਡ ਕਰੋ**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```  
    ਇਹ ਕੋਡ ਚਿੱਤਰ ਫਾਈਲ ਨੂੰ ਪੜ੍ਹਦਾ ਹੈ, base64 ਵਿੱਚ ਐਨਕੋਡ ਕਰਦਾ ਹੈ, ਅਤੇ ਐਨਕੋਡ ਕੀਤੇ ਡਾਟਾ ਨਾਲ ਇੱਕ HTML ਚਿੱਤਰ ਟੈਗ ਬਣਾਉਂਦਾ ਹੈ।

7. **ਟੈਕਸਟ ਅਤੇ ਚਿੱਤਰ ਨੂੰ ਪ੍ਰੰਪਟ ਵਿੱਚ ਮਿਲਾਓ**:
    ```python
    prompt = f"{text} {image}"
    ```  
    ਇਹ ਟੈਕਸਟ ਪ੍ਰੰਪਟ ਅਤੇ HTML ਚਿੱਤਰ ਟੈਗ ਨੂੰ ਇੱਕ ਸਤਰ ਵਿੱਚ ਜੋੜਦਾ ਹੈ।

8. **ChatNVIDIA ਨਾਲ ਕੋਡ ਜਨਰੇਟ ਕਰੋ**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```  
    ਇਹ ਕੋਡ ਪ੍ਰੰਪਟ ਨੂੰ `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` ਸਤਰ ਨੂੰ ਭੇਜਦਾ ਹੈ।

9. **ਜਨਰੇਟ ਕੀਤੇ ਸਮੱਗਰੀ ਵਿੱਚੋਂ Python ਕੋਡ ਕੱਢੋ**:
    ```python
    begin = code.index('```python') + 9  
    code = code[begin:]  
    end = code.index('```')
    code = code[:end]
    ```  
    ਇਹ ਜਨਰੇਟ ਕੀਤੀ ਸਮੱਗਰੀ ਵਿੱਚੋਂ markdown ਫਾਰਮੈਟਿੰਗ ਹਟਾ ਕੇ ਅਸਲੀ Python ਕੋਡ ਕੱਢਦਾ ਹੈ।

10. **ਜਨਰੇਟ ਕੀਤੇ ਕੋਡ ਨੂੰ ਚਲਾਓ**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```  
    ਇਹ ਕੱਢਿਆ ਗਿਆ Python ਕੋਡ ਇੱਕ ਸਬਪ੍ਰੋਸੈਸ ਵਜੋਂ ਚਲਾਉਂਦਾ ਹੈ ਅਤੇ ਇਸ ਦਾ ਆਉਟਪੁੱਟ ਕੈਪਚਰ ਕਰਦਾ ਹੈ।

11. **ਚਿੱਤਰ ਦਿਖਾਓ**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```  
    ਇਹ ਲਾਈਨਾਂ `IPython.display` ਮੋਡੀਊਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਚਿੱਤਰ ਦਿਖਾਉਂਦੀਆਂ ਹਨ।

**ਡਿਸਕਲੇਮਰ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਣਸਹੀਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਇਸਤੇਮਾਲ ਤੋਂ ਉੱਪਜਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਭ੍ਰਮਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।