### ఉదాహరణ సన్నివేశం

Imagine you have an image (`demo.png`) and you want to generate Python code that processes this image and saves a new version of it (`phi-3-vision.jpg`). 

The code above automates this process by:

1. Setting up the environment and necessary configurations.
2. Creating a prompt that instructs the model to generate the required Python code.
3. Sending the prompt to the model and collecting the generated code.
4. Extracting and running the generated code.
5. Displaying the original and processed images.

This approach leverages the power of AI to automate image processing tasks, making it easier and faster to achieve your goals. 

[నమూనా కోడ్ పరిష్కారం](../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Let's break down what the entire code does step by step:

1. **Install Required Package**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    ఈ కమాండ్ `langchain_nvidia_ai_endpoints` ప్యాకేజీని ఇన్‌స్టాల్ చేస్తుంది, అది తాజా వెర్షన్‌లో ఉందని నిర్ధారిస్తుంది.

2. **Import Necessary Modules**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    ఈ ఇంపోర్ట్స్ NVIDIA AI ఎండ్పాయింట్స్‌తో ఇంటరాక్ట్ చేయడానికి, పాస్వర్డ్స్‌ను సురక్షితంగా హ్యాండిల్ చేయడానికి, ఆపరేటింగ్ సిస్టమ్‌తో ఇంటరాక్ట్ చేయడానికి, మరియు base64 ఫార్మాట్‌లో డేటాను ఎన్కోడ్/డికోడ్ చేయడానికి అవసరమైన మాడ్యూల్లను తీసుకువస్తాయి.

3. **Set Up API Key**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    ఈ కోడ్ `NVIDIA_API_KEY` ఎన్విరాన్‌మెంట్ వేరియబుల్ సెటైచినదో లేదో తనిఖీ చేస్తుంది. లేకపోతే, ఇది వినియోగదారుడిని వారి API కీని సురక్షితంగా ఎంటర్ చేయమని ప్రాంప్ట్ చేస్తుంది.

4. **Define Model and Image Path**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    ఇది ఉపయోగించాల్సిన మోడల్‌ను సెట్ చేస్తుంది, పేర్కొన్న మోడల్‌తో `ChatNVIDIA` యొక్క ఒక ఇన్‌స్టెన్స్ను సృష్టిస్తుంది, మరియు చిత్రం ఫైల్‌కు మార్గాన్ని నిర్వచిస్తుంది.

5. **Create Text Prompt**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    ఇది ఒక టెక్స్ట్ ప్రాంప్ట్‌ను నిర్వచిస్తుంది, అది మోడల్‌ను ఒక చిత్రాన్ని ప్రాసెస్ చేయడానికి Python కోడ్‌ను రూపొందించమని సూచిస్తుంది.

6. **Encode Image in Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    ఈ కోడ్ చిత్రం ఫైల్‌ను చదివి, దాన్ని base64లో ఇన్‌కోడ్ చేస్తుంది, మరియు ఎన్కోడ్ చేయబడిన డాటాతో ఒక HTML image ట్యాగ్‌ను సృష్టిస్తుంది.

7. **Combine Text and Image into Prompt**:
    ```python
    prompt = f"{text} {image}"
    ```
    ఇది టెక్స్ట్ ప్రాంప్ట్ మరియు HTML image ట్యాగ్‌ను ఒకే స్ట్రింగ్‌గా కలిపి ఉంచుతుంది.

8. **Generate Code Using ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    ఈ కోడ్ ప్రాంప్ట్‌ను `ChatNVIDIA` మోడల్‌కు పంపి ఉత్పన్నమైన కోడ్‌ను చంక్స్‌గా సేకరిస్తుంది, ప్రతి చంక్‌ను ప్రింట్ చేసి `code` స్ట్రింగ్‌కు జతచేస్తుంది.

9. **Extract Python Code from Generated Content**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    ఇది జనరేట్ చేసిన కంటెంట్ నుండి మార్కడౌన్ ఫార్మాటింగ్ తీసివేసి అసలు Python కోడ్‌ను వెలికి తీయుతుంది.

10. **Run the Generated Code**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    ఇది వెలికి సాధించిన Python కోడ్‌ను ఒక subprocessగా నడిపించి దాని అవుట్‌పుట్‌ను క్యాప్చర్ చేస్తుంది.

11. **Display Images**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    ఈ లైన్స్ `IPython.display` మాడ్యూల్‌ను ఉపయోగించి చిత్రాలను ప్రదర్శిస్తాయి.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
అస్పష్టీకరణ:
ఈ డాక్యుమెంట్‌ను AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ద్వారా అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించగా కూడ, ఆటోమేటెడ్ అనువాదాల్లో తప్పులు లేదా లోపాలు ఉండే అవకాశం ఉందని దయచేసి గమనించండి. మూల దస్తావేజును దాని స్వదేశీ భాషలోని ప్రామాణిక సోర్స్‌గా పరిగణించాలి. ముఖ్యమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం వాడినప్పుడు ఏర్పడిన అపార్థాలు లేదా తప్పుగా అర్థం చేసుకోవడంపై మేము బాధ్యులమ్ కాదామని తెలియజేస్తున్నాము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->