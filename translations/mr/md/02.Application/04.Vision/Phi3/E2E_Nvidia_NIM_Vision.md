<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-05-09T19:54:41+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "mr"
}
-->
### उदाहरण परिस्थिती

कल्पना करा की तुमच्याकडे एक प्रतिमा (`demo.png`) आहे आणि तुम्हाला अशी Python कोड तयार करायची आहे जी या प्रतिमेवर प्रक्रिया करेल आणि त्याचा एक नवीन आवृत्ती (`phi-3-vision.jpg`) सेव्ह करेल.

वरील कोड हा प्रक्रिया स्वयंचलित करण्यासाठी खालील गोष्टी करतो:

1. वातावरण आणि आवश्यक सेटिंग्ज तयार करणे.
2. मॉडेलला आवश्यक Python कोड तयार करण्याचे निर्देश देणारा प्रॉम्प्ट तयार करणे.
3. प्रॉम्प्ट मॉडेलला पाठवणे आणि तयार झालेला कोड मिळवणे.
4. तयार केलेला कोड काढणे आणि चालवणे.
5. मूळ आणि प्रक्रिया केलेल्या प्रतिमा दाखवणे.

हा दृष्टिकोन AI च्या सामर्थ्यावर आधारित आहे, जो प्रतिमा प्रक्रिया कार्ये स्वयंचलित करतो, ज्यामुळे तुमचे उद्दिष्टे साध्य करणे सोपे आणि जलद होते.

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

चला पाहूया की संपूर्ण कोड टप्प्याटप्प्याने काय करतो:

1. **आवश्यक पॅकेज इन्स्टॉल करा**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    हा आदेश `langchain_nvidia_ai_endpoints` पॅकेजची नवीनतम आवृत्ती इन्स्टॉल करतो.

2. **आवश्यक मॉड्यूल्स आयात करा**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    हे आयात NVIDIA AI endpoints सोबत संवाद साधण्यासाठी, पासवर्ड सुरक्षित ठेवण्यासाठी, ऑपरेटिंग सिस्टमशी संवाद साधण्यासाठी, आणि base64 मध्ये डेटा एन्कोड/डिकोड करण्यासाठी आवश्यक मॉड्यूल्स आणते.

3. **API की सेट करा**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    हा कोड तपासतो की `NVIDIA_API_KEY` पर्यावरण चल (environment variable) सेट आहे का. जर नाही, तर वापरकर्त्याला सुरक्षितपणे API की टाकण्यास सांगतो.

4. **मॉडेल आणि प्रतिमेचा मार्ग निश्चित करा**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    येथे वापरायचा मॉडेल सेट केला आहे, `ChatNVIDIA` चा एक उदाहरण तयार केला आहे, आणि प्रतिमेचा फाइल पथ निश्चित केला आहे.

5. **टेक्स्ट प्रॉम्प्ट तयार करा**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    हा प्रॉम्प्ट मॉडेलला प्रतिमा प्रक्रिया करणारा Python कोड तयार करण्याचे निर्देश देतो.

6. **प्रतिमा base64 मध्ये एन्कोड करा**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    हा कोड प्रतिमा फाइल वाचतो, त्याला base64 मध्ये एन्कोड करतो, आणि एन्कोडेड डेटासह HTML इमेज टॅग तयार करतो.

7. **टेक्स्ट आणि प्रतिमा प्रॉम्प्टमध्ये एकत्र करा**:
    ```python
    prompt = f"{text} {image}"
    ```
    हा टेक्स्ट प्रॉम्प्ट आणि HTML इमेज टॅग एकत्र करून एक स्ट्रिंग तयार करतो.

8. **ChatNVIDIA वापरून कोड तयार करा**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    हा कोड प्रॉम्प्ट `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` स्ट्रिंगला पाठवतो.

9. **तयार झालेल्या कंटेंटमधून Python कोड काढा**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    हा भाग Markdown फॉरमॅटिंग काढून टाकून तयार झालेला Python कोड वेगळा करतो.

10. **तयार केलेला कोड चालवा**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    हा भाग वेगळा केलेला Python कोड subprocess म्हणून चालवतो आणि त्याचा आउटपुट पकडतो.

11. **प्रतिमा दाखवा**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    हे ओळी `IPython.display` मॉड्यूल वापरून प्रतिमा दाखवतात.

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये चुका किंवा अचूकतेच्या त्रुटी असू शकतात. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीकरिता व्यावसायिक मानवी भाषांतर सुचवले जाते. या भाषांतराच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीसाठी आम्ही जबाबदार नाही.