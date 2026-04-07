### ឧទាហរណ៍សេណារីយ៉ូ

សន្មត់ថាអ្នកមានរូបភាពមួយ (`demo.png`) ហើយអ្នកចង់បង្កើតកូដ Python ដែលដំណើរការរូបភាពនេះ និងរក្សាទុកជាវერსិនថ្មីមួយ (`phi-3-vision.jpg`)។

កូដខាងលើគឺធ្វើការ​អូតូម៉ាទ័រ​ដងនេះដោយ:

1. កំណត់បរិយាកាស និងការកំណត់តម្លៃចាំបាច់។
2. បង្កើតប្រអប់សារ​ដែលណែនាំម៉ូដែលឲ្យបង្កើតកូដ Python ដែលត្រូវការជាកូដ។
3. បញ្ជូនប្រអប់សារទៅម៉ូដែល និងប្រមូលកូដដែលបានបង្កើត។
4. ដកស្រង់ និងរត់កូដដែលបានបង្កើត។
5. បង្ហាញរូបភាពដើម និងរូបភាពដែលបានដំណើរការ។

វិធីសាស្រ្តនេះបង្ហាញពីថាមពលនៃ AI ដើម្បីអូតូម៉ាទ័រដំណើរការរូបភាព ដែលធ្វើឲ្យមានភាពងាយស្រួល និងលឿនក្នុងការសម្រេចគោលដៅរបស់អ្នក។

[Sample Code Solution](../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

មកបំបែកតំណាងនូវអ្វីដែលកូដទាំងមូលធ្វើជា​ជំហានៗ៖

1. **ដំឡើងកញ្ចប់ដែលត្រូវការ**:  
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    ពាក្យបញ្ជានេះដំឡើងកញ្ចប់ `langchain_nvidia_ai_endpoints` ដែលធ្វើឲ្យប្រាកដថាវាជាការប៉ុនប៉ងកំណែចុងក្រោយបំផុត។

2. **នាំចូលម៉ូឌុលចាំបាច់**:  
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    ការនាំចូលទាំងនេះនាំយកម៉ូឌុលដែលត្រូវការសម្រាប់ធ្វើការ ជាមួយ NVIDIA AI endpoints ហាមឃាត់ពាក្យសម្ងាត់យ៉ាងសុវត្ថិភាព អន្តរកម្មជាមួយប្រព័ន្ធប្រតិបត្តិការ និងបំលែង/បកប្រែក្នុងទ្រង់ទ្រាយ base64។

3. **កំណត់កូនសោ API**:  
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    កូដនេះពិនិត្យថាតើអថេរបរិយាកាស `NVIDIA_API_KEY` ត្រូវបានកំណត់រួចហើយឬនៅ។ ប្រសិនបើមិនទាន់ដាក់វា នោះវានឹងស្នើឲ្យអ្នកបញ្ចូលកូនសោ API របស់អ្នកយ៉ាងសុវត្ថិភាព។

4. **កំណត់ម៉ូដែល និងផ្លូវរូបភាព**:  
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    កូដនេះកំណត់ម៉ូដែលដែលត្រូវប្រើ បង្កើតអ实例មួយនៃ `ChatNVIDIA` ជាមួយម៉ូដែលដែលបានបញ្ជាក់ និងកំណត់ផ្លូវទៅឯកសាររូបភាព។

5. **បង្កើតប្រអប់សារបែបអក្សរ**:  
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    កូដនេះកំណត់ប្រអប់សារអក្សរដែលណែនាំម៉ូដែលឲ្យបង្កើតកូដ Python សម្រាប់ដំណើរការរូបភាពមួយ។

6. **បំលែងរូបភាពទៅទ្រង់ទ្រាយ Base64**:  
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    កូដនេះអានឯកសាររូបភាព បំលែងវាទៅជាទ្រង់ទ្រាយ base64 ហើយបង្កើតតែគ HTML រូបភាពជាមួយទិន្នន័យដែលបានបំលែង។

7. **បញ្ចូលអក្សរ និងរូបភាពចូលប្រអប់សារ**:  
    ```python
    prompt = f"{text} {image}"
    ```
    កូដនេះបញ្ចូលប្រអប់សារអក្សរ និងតែគ HTML រូបភាពចូលជាស្រទាប់តែមួយ។

8. **បង្កើតកូដដោយប្រើ ChatNVIDIA**:  
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    កូដនេះបញ្ជូនប្រអប់សារទៅម៉ូដែល `ChatNVIDIA` ហើយប្រមូលកូដដែលបានបង្កើតជាចំណែកៗ កាស្រីនិងភ្ជាប់ចំណែកនីមួយៗទៅអថេរ `code`។

9. **ដកស្រង់កូដ Python ពីមាតិកាដែលបានបង្កើត**:  
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    កូដនេះដកស្រង់កូដ Python ពិតប្រាកដពីមាតិកាដែលបានបង្កើត ដោយយកចេញពីទ្រង់ទ្រាយ markdown។

10. **រត់កូដដែលបានបង្កើត**:  
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    កូដនេះរត់កូដ Python ដែលបានដកស្រង់ក្នុងជាកម្មវិធីរង (subprocess) ហើយចាប់យកលទ្ធផលរបស់វា។

11. **បង្ហាញរូបភាព**:  
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    បន្ទាត់ទាំងនេះបង្ហាញរូបភាពដោយប្រើម៉ូឌុល `IPython.display`។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបញ្ជាក់**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលដែលយើងខិតខំដើម្បីមានភាពត្រឹមត្រូវ សូមយកចិត្តទុកដាក់ថាបកប្រែដោយស្វ័យប្រវត្តិនេះអាចមានកំហុស ឬការមិនត្រឹមត្រូវ។ ឯកសារដើមក្នុងភាសាតំណើររបស់វាគួរត្រូវបានគិតថាជាប្រភពត្រឹមត្រូវបំផុត។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមផ្តល់អាទិភាពដល់ការបកប្រែដោយមនុស្សដែលមានវិជ្ជាជីវៈ។ យើងមិនទទួលខុសត្រូវចំពោះករណីច្រឡំ ឬការបកប្រែខុសពីការប្រើប្រាស់បកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->