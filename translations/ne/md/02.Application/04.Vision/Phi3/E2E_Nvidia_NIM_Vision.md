<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-05-09T19:54:51+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "ne"
}
-->
### उदाहरण परिदृश्य

कल्पना गर्नुहोस् तपाईंसँग एउटा छवि (`demo.png`) छ र तपाईँले Python कोड सिर्जना गर्न चाहनुहुन्छ जुन यस छविलाई प्रक्रिया गरी नयाँ संस्करण (`phi-3-vision.jpg`) बचत गर्छ।

माथिको कोडले यो प्रक्रिया स्वचालित बनाउँछ:

1. वातावरण र आवश्यक कन्फिगरेसनहरू सेट अप गर्दै।
2. मोडेललाई आवश्यक Python कोड सिर्जना गर्न निर्देशन दिने प्रॉम्प्ट तयार गर्दै।
3. प्रॉम्प्ट मोडेलमा पठाउँदै र सिर्जित कोड सङ्कलन गर्दै।
4. सिर्जित कोड निकालेर चलाउँदै।
5. मूल र प्रक्रिया गरिएको छविहरू प्रदर्शन गर्दै।

यो विधिले AI को शक्तिलाई उपयोग गरेर छवि प्रक्रिया कार्यहरू स्वचालित बनाउँछ, जसले तपाईँका लक्ष्यहरू सजिलै र छिटो प्राप्त गर्न मद्दत गर्छ।

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

अब सम्पूर्ण कोडले के गर्छ भन्ने क्रमशः विश्लेषण गरौं:

1. **आवश्यक प्याकेज स्थापना गर्नुहोस्**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    यो कमाण्डले `langchain_nvidia_ai_endpoints` प्याकेज स्थापना गर्छ र यसको नवीनतम संस्करण सुनिश्चित गर्छ।

2. **आवश्यक मोड्युलहरू आयात गर्नुहोस्**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    यी आयातहरूले NVIDIA AI endpoints सँग अन्तरक्रिया गर्न, पासवर्ड सुरक्षित रूपमा ह्यान्डल गर्न, अपरेटिङ सिस्टमसँग अन्तरक्रिया गर्न, र base64 ढाँचामा डाटा एन्कोड/डिकोड गर्न आवश्यक मोड्युलहरू ल्याउँछन्।

3. **API कुञ्जी सेट अप गर्नुहोस्**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    यो कोडले जाँच गर्छ कि `NVIDIA_API_KEY` वातावरण चर सेट छ कि छैन। नभएमा, प्रयोगकर्तालाई सुरक्षित रूपमा आफ्नो API कुञ्जी प्रविष्ट गर्न अनुरोध गर्छ।

4. **मोडेल र छवि पथ परिभाषित गर्नुहोस्**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    यसले प्रयोग गर्नुपर्ने मोडेल सेट गर्छ, `ChatNVIDIA` को एउटा उदाहरण बनाउँछ र छवि फाइलको पथ परिभाषित गर्छ।

5. **टेक्स्ट प्रॉम्प्ट तयार गर्नुहोस्**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    यो एउटा टेक्स्ट प्रॉम्प्ट परिभाषित गर्छ जसले मोडेललाई छवि प्रक्रिया गर्ने Python कोड सिर्जना गर्न निर्देशन दिन्छ।

6. **छविलाई Base64 मा एन्कोड गर्नुहोस्**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    यो कोडले छवि फाइल पढ्छ, base64 मा एन्कोड गर्छ र एन्कोड गरिएको डाटासहित HTML इमेज ट्याग बनाउँछ।

7. **टेक्स्ट र छविलाई प्रॉम्प्टमा संयोजन गर्नुहोस्**:
    ```python
    prompt = f"{text} {image}"
    ```
    यो टेक्स्ट प्रॉम्प्ट र HTML इमेज ट्यागलाई एउटै स्ट्रिङमा जोड्छ।

8. **ChatNVIDIA प्रयोग गरी कोड सिर्जना गर्नुहोस्**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    यो कोडले प्रॉम्प्टलाई `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` स्ट्रिङमा पठाउँछ।

9. **सिर्जित सामग्रीबाट Python कोड निकाल्नुहोस्**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    यो markdown फर्म्याटिङ हटाएर वास्तविक Python कोड निकाल्छ।

10. **सिर्जित कोड चलाउनुहोस्**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    यो निकालिएको Python कोडलाई subprocess मा चलाउँछ र यसको आउटपुट क्याप्चर गर्छ।

11. **छविहरू प्रदर्शन गर्नुहोस्**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    यी लाइनहरूले `IPython.display` मोड्युल प्रयोग गरी छविहरू प्रदर्शन गर्छन्।

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) को प्रयोग गरी अनुवाद गरिएको हो। हामी सटीकता सुनिश्चित गर्न प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धिहरू हुन सक्छन्। मूल दस्तावेज यसको मूल भाषामा नै आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।