### ឧទាហរណ៍សេណារីយ៉ូ

សូមនឹកស្រមៃថាអ្នកមានរូបភាពមួយ (`demo.png`) ហើយអ្នកចង់បង្កើតកូដ Python ដែលដំណើរការរូបភាពនេះ និងរក្សាទុកជារូបភាពថ្មីមួយ (`phi-3-vision.jpg`)។ 

កូដខាងលើធ្វើអត្តូម៉ាទិចដំណើរការនេះដោយ៖

1. ការរៀបចំបរិយាកាស និងការកំណត់ដែលចាំបាច់។
2. បង្កើត prompt ដែលណែនាំម៉ូដែលឱ្យបង្កើតកូដ Python តាមដែលត្រូវការ។
3. ផ្ញើ prompt ទៅម៉ូដែល និងប្រមូលកូដដែលបានបង្កើត។
4. ដកចេញ និងដំណើរការកូដដែលបានបង្កើត។
5. បង្ហាញរូបភាពដើម និងរូបភាពដែលបានដំណើរការ។

វិធីនេះប្រើអត្ថិភាពនៃ AI ដើម្បីធ្វើឱ្យការដំណើរការរូបភាពជាអត្តូម៉ាទិច មានភាពងាយស្រួល និងលឿន ដើម្បីជួយឱ្យអ្នកសម្រេចគោលបំណង។

[ឧទាហរណ៍ដំណោះស្រាយកូដ](../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Let's break down what the entire code does step by step:

1. **ដំឡើងកញ្ចប់ដែលត្រូវការ**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    ការបញ្ជានេះដំឡើងកញ្ចប់ `langchain_nvidia_ai_endpoints` ហើយធានាថាវាជាកំណែថ្មីបំផុត។

2. **នាំចូលម៉ូឌុលដែលចាំបាច់**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    ការនាំចូលទាំងនេះនាំឲ្យមានម៉ូឌុលដែលចាំបាច់សម្រាប់អន្តរកម្មជាមួយ NVIDIA AI endpoints, ការដោះស្រាយពាក្យសម្ងាត់យ៉ាងសុវត្ថិភាព, អន្តរកម្មជាមួយប្រព័ន្ធប្រតិបត្តិការ, និង encoding/decoding ទិន្នន័យក្នុងទ្រង់ទ្រាយ base64។

3. **កំណត់ API Key**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    កូដនេះពិនិត្យមើលថាតើបរិយាកាសអថេរ `NVIDIA_API_KEY` ត្រូវបានកំណត់រួចហើយឬនៅ។ ប្រសិនបើមិនមាន វាស្នើឲ្យអ្នកប្រើបញ្ចូល API key របស់ពួកគេយ៉ាងសុវត្ថិភាព។

4. **កំណត់ម៉ូដែល និងផ្លូវរូបភាព**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    នេះកំណត់ម៉ូដែលដែលត្រូវប្រើ បង្កើតអុបទិចក្នុង `ChatNVIDIA` ជាមួយម៉ូដែលដែលបានកំណត់ ហើយកំណត់ផ្លូវទៅកាន់ឯកសាររូបភាព។

5. **បង្កើត Prompt អត្ថបទ**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    នេះកំណត់ prompt អត្ថបទដែលណែនាំម៉ូដែលឱ្យបង្កើតកូដ Python សម្រាប់ដំណើរការរូបភាព។

6. **កូដប្រែរូបភាពជាទ្រង់ទ្រាយ Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    កូដនេះអានឯកសាររូបភាព បកបញ្ជូនទៅជា base64 ហើយបង្កើតស្លាករូបភាព HTML ជាមួយទិន្នន័យដែលបាន encode។

7. **បញ្ចូលអត្ថបទ និងរូបភាពទៅក្នុង Prompt**:
    ```python
    prompt = f"{text} {image}"
    ```
    នេះលាយ prompt អត្ថបទ និងស្លាករូបភាព HTML ទៅជា ខ្សែអក្សរ តែមួយ។

8. **បង្កើតកូដដោយប្រើ ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    កូដនេះផ្ញើ prompt ទៅម៉ូដែល `ChatNVIDIA` និងប្រមូលកូដដែលបានបង្កើតជាប្លុកៗ ដូច្នេះបោះពុម្ពនិងបូកបញ្ចូលរាល់ប្លុកទៅក្នុងខ្សែអក្សរ `code`។

9. **ដកកូដ Python ចេញពីមាតិកាដែលបានបង្កើត**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    នេះដកកូដ Python ពិតប្រាកដចេញពីមាតិកាដែលបានបង្កើតដោយលុប formatting markdown ចេញ។

10. **រត់កូដដែលបានបង្កើត**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    នេះរត់កូដ Python ដែលបានដកចេញជា subprocess ហើយចាប់យកលទ្ធផលរបស់វា។

11. **បង្ហាញរូបភាព**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    បន្ទាត់ទាំងនេះបង្ហាញរូបភាពដោយប្រើម៉ូឌុល `IPython.display`។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយ៉ាងណា យើងខិតខំដើម្បីឲ្យបានត្រឹមត្រូវ សូមយកចិត្តទុកដាក់ថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬមានភាពមិនត្រឹមត្រូវ។ ឯកសារដើមក្នុងភាសាមាតុភូមិគួរត្រូវបានគេចាត់ទុកថាជាប្រភពផ្លូវការ។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមពិចារណាសុំការបកប្រែដោយមនុស្សវិជ្ជាជីវៈ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសណាមួយដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->