### ਉਦਾਹਰਨ ਸਥਿਤੀ

ਕਲਪਨਾ ਕਰੋ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਇੱਕ ਚਿੱਤਰ (`demo.png`) ਹੈ ਅਤੇ ਤੁਸੀਂ ਐਸਾ Python ਕੋਡ ਬਣਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ ਜੋ ਇਸ ਚਿੱਤਰ ਨੂੰ ਪ੍ਰੋਸੈਸ ਕਰਕੇ ਇਸ ਦੀ ਇੱਕ ਨਵੀਂ ਵਰਜਨ (`phi-3-vision.jpg`) ਸੇਵ ਕਰੇ। 

ਉਪਰ ਦਿੱਤਾ ਕੋਡ ਇਸ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਆਟੋਮੇਟ ਕਰਦਾ ਹੈ:

1. ਵਾਤਾਵਰਣ ਅਤੇ ਜ਼ਰੂਰੀ ਸੰਰਚਨਾਵਾਂ ਸੈੱਟ ਕਰਨਾ।
2. ਇੱਕ ਪ੍ਰਾਂਪਟ ਬਣਾਉਣਾ ਜੋ ਮਾਡਲ ਨੂੰ ਲੋੜੀਂਦਾ Python ਕੋਡ ਬਣਾਉਣ ਲਈ ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼ ਦਿੰਦਾ ਹੈ।
3. ਪ੍ਰਾਂਪਟ ਨੂੰ ਮਾਡਲ ਨੂੰ ਭੇਜਣਾ ਅਤੇ ਬਣਾਏ ਗਏ ਕੋਡ ਨੂੰ ਇਕੱਠਾ ਕਰਨਾ।
4. ਬਣਾਏ ਗਏ ਕੋਡ ਨੂੰ ਕੱਢਣਾ ਅਤੇ ਚਲਾਉਣਾ।
5. ਮੂਲ ਅਤੇ ਪ੍ਰੋਸੈਸ ਕੀਤੇ ਚਿੱਤਰਾਂ ਨੂੰ ਦਿਖਾਉਣਾ।

ਇਹ ਤਰੀਕਾ AI ਦੀ ਤਾਕਤ ਦਾ ਫਾਇਦਾ ਉਠਾਉਂਦਾ ਹੈ ਤਾਂ ਜੋ ਚਿੱਤਰ ਪ੍ਰੋਸੈਸਿੰਗ ਦੇ ਕੰਮ ਆਟੋਮੇਟ ਹੋ ਜਾਣ, ਜਿਸ ਨਾਲ ਤੁਹਾਡੇ ਲਕੜਾਂ ਨੂੰ ਪੂਰਾ ਕਰਨਾ ਆਸਾਨ ਅਤੇ ਤੇਜ਼ ਹੋ ਜਾਂਦਾ ਹੈ। 

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

ਆਓ ਪੂਰੇ ਕੋਡ ਨੂੰ ਕਦਮ ਦਰ ਕਦਮ ਸਮਝੀਏ:

1. **ਲੋੜੀਂਦਾ ਪੈਕੇਜ ਇੰਸਟਾਲ ਕਰੋ**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    ਇਹ ਕਮਾਂਡ `langchain_nvidia_ai_endpoints` ਪੈਕੇਜ ਨੂੰ ਇੰਸਟਾਲ ਕਰਦੀ ਹੈ, ਇਹ ਯਕੀਨੀ ਬਣਾਉਂਦੀ ਹੈ ਕਿ ਇਹ ਸਭ ਤੋਂ ਨਵਾਂ ਵਰਜਨ ਹੈ।

2. **ਜ਼ਰੂਰੀ ਮੋਡੀਊਲ ਇੰਪੋਰਟ ਕਰੋ**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    ਇਹ ਇੰਪੋਰਟ NVIDIA AI endpoints ਨਾਲ ਇੰਟਰੈਕਟ ਕਰਨ, ਪਾਸਵਰਡ ਸੁਰੱਖਿਅਤ ਤਰੀਕੇ ਨਾਲ ਸੰਭਾਲਣ, ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ ਨਾਲ ਕੰਮ ਕਰਨ ਅਤੇ ਡਾਟਾ ਨੂੰ base64 ਫਾਰਮੈਟ ਵਿੱਚ ਐਨਕੋਡ/ਡਿਕੋਡ ਕਰਨ ਲਈ ਜ਼ਰੂਰੀ ਮੋਡੀਊਲ ਲਿਆਉਂਦੇ ਹਨ।

3. **API ਕੀ ਸੈੱਟ ਕਰੋ**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    ਇਹ ਕੋਡ ਜਾਂਚਦਾ ਹੈ ਕਿ `NVIDIA_API_KEY` ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਸੈੱਟ ਹੈ ਜਾਂ ਨਹੀਂ। ਜੇ ਨਹੀਂ, ਤਾਂ ਇਹ ਯੂਜ਼ਰ ਨੂੰ ਸੁਰੱਖਿਅਤ ਤਰੀਕੇ ਨਾਲ ਆਪਣੀ API ਕੀ ਦਰਜ ਕਰਨ ਲਈ ਕਹਿੰਦਾ ਹੈ।

4. **ਮਾਡਲ ਅਤੇ ਚਿੱਤਰ ਦਾ ਰਸਤਾ ਪਰਿਭਾਸ਼ਿਤ ਕਰੋ**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    ਇਹ ਮਾਡਲ ਨੂੰ ਸੈੱਟ ਕਰਦਾ ਹੈ, `ChatNVIDIA` ਦਾ ਇੱਕ ਇੰਸਟੈਂਸ ਬਣਾਉਂਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਦਿੱਤਾ ਮਾਡਲ ਹੈ, ਅਤੇ ਚਿੱਤਰ ਫਾਇਲ ਦਾ ਰਸਤਾ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ।

5. **ਟੈਕਸਟ ਪ੍ਰਾਂਪਟ ਬਣਾਓ**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    ਇਹ ਇੱਕ ਟੈਕਸਟ ਪ੍ਰਾਂਪਟ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ ਜੋ ਮਾਡਲ ਨੂੰ ਚਿੱਤਰ ਪ੍ਰੋਸੈਸਿੰਗ ਲਈ Python ਕੋਡ ਬਣਾਉਣ ਦੀ ਹਦਾਇਤ ਦਿੰਦਾ ਹੈ।

6. **ਚਿੱਤਰ ਨੂੰ base64 ਵਿੱਚ ਐਨਕੋਡ ਕਰੋ**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    ਇਹ ਕੋਡ ਚਿੱਤਰ ਫਾਇਲ ਨੂੰ ਪੜ੍ਹਦਾ ਹੈ, ਇਸਨੂੰ base64 ਵਿੱਚ ਐਨਕੋਡ ਕਰਦਾ ਹੈ, ਅਤੇ ਐਨਕੋਡ ਕੀਤੇ ਡਾਟਾ ਨਾਲ ਇੱਕ HTML ਚਿੱਤਰ ਟੈਗ ਬਣਾਉਂਦਾ ਹੈ।

7. **ਟੈਕਸਟ ਅਤੇ ਚਿੱਤਰ ਨੂੰ ਪ੍ਰਾਂਪਟ ਵਿੱਚ ਜੋੜੋ**:
    ```python
    prompt = f"{text} {image}"
    ```
    ਇਹ ਟੈਕਸਟ ਪ੍ਰਾਂਪਟ ਅਤੇ HTML ਚਿੱਤਰ ਟੈਗ ਨੂੰ ਇੱਕ ਸਿੰਗਲ ਸਟਰਿੰਗ ਵਿੱਚ ਜੋੜਦਾ ਹੈ।

8. **ChatNVIDIA ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੋਡ ਬਣਾਓ**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    ਇਹ ਕੋਡ ਪ੍ਰਾਂਪਟ ਨੂੰ `ChatNVIDIA` ਮਾਡਲ ਨੂੰ ਭੇਜਦਾ ਹੈ ਅਤੇ ਬਣਾਏ ਗਏ ਕੋਡ ਨੂੰ ਟੁਕੜਿਆਂ ਵਿੱਚ ਇਕੱਠਾ ਕਰਦਾ ਹੈ, ਹਰ ਟੁਕੜਾ ਪ੍ਰਿੰਟ ਕਰਦਾ ਅਤੇ `code` ਸਟਰਿੰਗ ਵਿੱਚ ਜੋੜਦਾ ਹੈ।

9. **ਬਣਾਏ ਗਏ ਸਮੱਗਰੀ ਵਿੱਚੋਂ Python ਕੋਡ ਕੱਢੋ**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    ਇਹ markdown ਫਾਰਮੈਟਿੰਗ ਹਟਾ ਕੇ ਬਣਾਏ ਗਏ ਸਮੱਗਰੀ ਵਿੱਚੋਂ ਅਸਲੀ Python ਕੋਡ ਕੱਢਦਾ ਹੈ।

10. **ਬਣਾਏ ਗਏ ਕੋਡ ਨੂੰ ਚਲਾਓ**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    ਇਹ ਕੱਢਿਆ ਹੋਇਆ Python ਕੋਡ ਇੱਕ subprocess ਵਜੋਂ ਚਲਾਉਂਦਾ ਹੈ ਅਤੇ ਇਸਦਾ ਆਉਟਪੁੱਟ ਕੈਪਚਰ ਕਰਦਾ ਹੈ।

11. **ਚਿੱਤਰ ਦਿਖਾਓ**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    ਇਹ ਲਾਈਨਾਂ `IPython.display` ਮੋਡੀਊਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਚਿੱਤਰਾਂ ਨੂੰ ਦਿਖਾਉਂਦੀਆਂ ਹਨ।

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।