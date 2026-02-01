### उदाहरण परिदृश्य

कल्पना गर्नुहोस् तपाईंसँग एउटा तस्बिर (`demo.png`) छ र तपाईँले यस्तो Python कोड बनाउन चाहनुहुन्छ जसले यो तस्बिरलाई प्रक्रिया गरी नयाँ संस्करण (`phi-3-vision.jpg`) सुरक्षित गर्छ।

माथिको कोडले यो प्रक्रिया स्वचालित रूपमा गर्छ:

1. वातावरण र आवश्यक कन्फिगरेसनहरू सेटअप गर्दै।
2. मोडेललाई आवश्यक Python कोड बनाउन निर्देशन दिने प्रॉम्प्ट तयार गर्दै।
3. प्रॉम्प्ट मोडेलमा पठाएर उत्पन्न कोड सङ्कलन गर्दै।
4. उत्पन्न कोड निकालेर चलाउँदै।
5. मूल र प्रक्रिया गरिएको तस्बिरहरू प्रदर्शन गर्दै।

यो तरिका AI को शक्ति प्रयोग गरेर तस्बिर प्रक्रिया गर्ने कामहरू स्वचालित बनाउँछ, जसले तपाईँका लक्ष्यहरू सजिलो र छिटो प्राप्त गर्न मद्दत गर्छ।

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

अब सम्पूर्ण कोडले के गर्छ भन्ने कुरा चरणबद्ध रूपमा बुझौं:

1. **आवश्यक प्याकेज इन्स्टल गर्नुहोस्**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    यो कमाण्डले `langchain_nvidia_ai_endpoints` प्याकेज इन्स्टल गर्छ, र यो सुनिश्चित गर्छ कि यो सबैभन्दा नयाँ संस्करण हो।

2. **आवश्यक मोड्युलहरू आयात गर्नुहोस्**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    यी आयातहरूले NVIDIA AI endpoints सँग अन्तरक्रिया गर्न, पासवर्ड सुरक्षित रूपमा ह्यान्डल गर्न, अपरेटिङ सिस्टमसँग अन्तरक्रिया गर्न, र base64 मा डाटा इन्कोड/डिकोड गर्न आवश्यक मोड्युलहरू ल्याउँछन्।

3. **API कुञ्जी सेटअप गर्नुहोस्**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    यो कोडले जाँच गर्छ कि `NVIDIA_API_KEY` वातावरण चर सेट छ कि छैन। नभएमा, प्रयोगकर्तालाई सुरक्षित रूपमा आफ्नो API कुञ्जी प्रविष्ट गर्न अनुरोध गर्छ।

4. **मोडेल र तस्बिरको पथ परिभाषित गर्नुहोस्**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    यसले प्रयोग गर्नुपर्ने मोडेल सेट गर्छ, `ChatNVIDIA` को एउटा उदाहरण बनाउँछ र तस्बिर फाइलको पथ परिभाषित गर्छ।

5. **टेक्स्ट प्रॉम्प्ट तयार गर्नुहोस्**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    यसले मोडेललाई तस्बिर प्रक्रिया गर्ने Python कोड बनाउन निर्देशन दिने टेक्स्ट प्रॉम्प्ट परिभाषित गर्छ।

6. **तस्बिरलाई Base64 मा इन्कोड गर्नुहोस्**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    यो कोडले तस्बिर फाइल पढ्छ, base64 मा इन्कोड गर्छ, र इन्कोड गरिएको डाटासहित HTML इमेज ट्याग बनाउँछ।

7. **टेक्स्ट र तस्बिरलाई प्रॉम्प्टमा संयोजन गर्नुहोस्**:
    ```python
    prompt = f"{text} {image}"
    ```
    यसले टेक्स्ट प्रॉम्प्ट र HTML इमेज ट्यागलाई एउटै स्ट्रिङमा जोड्छ।

8. **ChatNVIDIA प्रयोग गरेर कोड उत्पन्न गर्नुहोस्**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    यो कोडले प्रॉम्प्ट `ChatNVIDIA` मोडेलमा पठाउँछ र उत्पन्न कोडलाई टुक्रामा सङ्कलन गर्छ, प्रत्येक टुक्रा प्रिन्ट र `code` स्ट्रिङमा थप्दै।

9. **उत्पन्न सामग्रीबाट Python कोड निकाल्नुहोस्**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    यो markdown फर्म्याटिङ हटाएर वास्तविक Python कोड निकाल्छ।

10. **उत्पन्न कोड चलाउनुहोस्**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    यो निकालिएको Python कोडलाई subprocess को रूपमा चलाउँछ र यसको आउटपुट समात्छ।

11. **तस्बिरहरू प्रदर्शन गर्नुहोस्**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    यी लाइनहरूले `IPython.display` मोड्युल प्रयोग गरी तस्बिरहरू प्रदर्शन गर्छन्।

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।