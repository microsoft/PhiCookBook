## ស្វាគមន៍មកកាន់មេរៀន Phi ដែលប្រើប្រាស់ C#

មានមេរៀនជាច្រើនដែលបង្ហាញពីរបៀបបញ្ចូលម៉ូឌែល Phi ជាច្រើនកំណែដ៏មានប្រសិទ្ធភាពក្នុងបរិយាកាស .NET។

## លក្ខខ័ណ្ឌជាមុន

មុនដំណើរការឧទាហរណ៍ សូមប្រាកដថាអ្នកបានដំឡើងវាជាច្រើនដូចខាងក្រោម៖

**.NET 9:** សូមប្រាកដថាអ្នកបានដំឡើង [កំណែថ្មីបំផុតនៃ .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) លើកុំព្យួទ័ររបស់អ្នក។

**(ជាជម្រើស) Visual Studio ឬ Visual Studio Code:** អ្នកនឹងត្រូវការតំបន់អភិវឌ្ឍន៍ឬកម្មវិធីកូដដែលអាចរត់គម្រោង .NET បាន។ [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) ឬ [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) ត្រូវបានណែនាំ។

**ប្រើប្រាស់ git** ដើម្បីគូតចម្លងមួយក្នុងចំណោមកំណែ Phi-3, Phi3.5 ឬ Phi-4 ពី [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c) ។

**ទាញយកម៉ូឌែល Phi-4 ONNX** ទៅកាន់កុំព្យួទ័ររបស់អ្នក៖

### ទៅកាន់ថតដើម្បីពិចារណាទុកម៉ូឌែល

```bash
cd c:\phi\models
```

### បន្ថែមការគាំទ្រ lfs

```bash
git lfs install 
```

### គូតចម្លង និងទាញយកម៉ូឌែល Phi-4 mini instruct និងម៉ូឌែល Phi-4 multi modal

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**ទាញយកម៉ូឌែល Phi-3 ONNX** ទៅកាន់កុំព្យួទ័ររបស់អ្នក៖

### គូតចម្លង និងទាញយកម៉ូឌែល Phi-3 mini 4K instruct និងម៉ូឌែល Phi-3 vision 128K

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**សំខាន់ៈ** សាកល្បងនៅចុងក្រោយបច្ចុប្បន្នត្រូវបានរចនាឡើងដើម្បីប្រើម៉ូឌែលកំណែ ONNX។ ជំហានមុនៗបានគូតចម្លងម៉ូឌែលដូចខាងក្រោម។

## អំពីមេរៀន

ដំណោះស្រាយសំខាន់មានមេរៀនគំរូជាច្រើនដែលបង្ហាញពីសមត្ថភាពនៃម៉ូឌែល Phi ដោយប្រើ C#។

| គម្រោង | ម៉ូឌែល | ពិពណ៌នា |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 ឬ Phi-3.5 | ការជជែកតាមផ្សារ console គំរូដែលអនុញ្ញាតឲ្យអ្នកប្រើសួរប្រការកម្មវិធី។ គម្រោងទាញយកម៉ូឌែល Phi-3 ONNX របស់មូលដ្ឋានដោយប្រើបណ្ណាល័យ `Microsoft.ML.OnnxRuntime`។ |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 ឬ Phi-3.5 | ការជជែកតាមផ្សារ console គំរូដែលអនុញ្ញាតឲ្យអ្នកប្រើសួរប្រការកម្មវិធី។ គម្រោងទាញយកម៉ូឌែល Phi-3 ONNX របស់មូលដ្ឋានដោយប្រើបណ្ណាល័យ `Microsoft.Semantic.Kernel`។ |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 ឬ Phi-3.5 | គម្រោងគំរូនេះប្រើម៉ូឌែល phi3 vision របស់មូលដ្ឋានដើម្បីវិភាគរូបភាព។ គម្រោងទាញយកម៉ូឌែល Phi-3 Vision ONNX របស់មូលដ្ឋានដោយប្រើបណ្ណាល័យ `Microsoft.ML.OnnxRuntime`។ |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 ឬ Phi-3.5 | គម្រោងគំរូនេះប្រើម៉ូឌែល phi3 vision របស់មូលដ្ឋានដើម្បីវិភាគរូបភាព។ គម្រោងទាញយកម៉ូឌែល Phi-3 Vision ONNX របស់មូលដ្ឋានដោយប្រើបណ្ណាល័យ `Microsoft.ML.OnnxRuntime`។ គម្រោងក៏បង្ហាញមឺនុយជាមួយជម្រើសផ្សេងៗដើម្បីអន្តរកម្មជាមួយអ្នកប្រើ។ | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | ការជជែកតាមផ្សារ console គំរូដែលអនុញ្ញាតឲ្យអ្នកប្រើសួរប្រការកម្មវិធី។ គម្រោងទាញយកម៉ូឌែល Phi-4 ONNX របស់មូលដ្ឋានដោយប្រើបណ្ណាល័យ `Microsoft.ML.OnnxRuntime`។ |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | ការជជែកតាមផ្សារ console គំរូដែលអនុញ្ញាតឲ្យអ្នកប្រើសួរប្រការកម្មវិធី។ គម្រោងទាញយកម៉ូឌែល Phi-4 ONNX របស់មូលដ្ឋានដោយប្រើបណ្ណាល័យ `Semantic Kernel`។ |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | ការជជែកតាមផ្សារ console គំរូដែលអនុញ្ញាតឲ្យអ្នកប្រើសួរប្រការកម្មវិធី។ គម្រោងទាញយកម៉ូឌែល Phi-4 ONNX របស់មូលដ្ឋានដោយប្រើបណ្ណាល័យ `Microsoft.ML.OnnxRuntimeGenAI` ហើយអនុវត្ត `IChatClient` ពី `Microsoft.Extensions.AI`។ |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | ការជជែកតាមផ្សារ console គំរូដែលអនុញ្ញាតឲ្យអ្នកប្រើសួរប្រការកម្មវិធី។ ការជជែកមានមេម៉ូរី។ |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | គម្រោងគំរូដែលប្រើម៉ូឌែល Phi-4 របស់មូលដ្ឋានដើម្បីវិភាគរូបភាព ហើយបង្ហាញលទ្ធផលនៅលើ console។ គម្រោងទាញយកម៉ូឌែល Phi-4-`multimodal-instruct-onnx` របស់មូលដ្ឋានដោយប្រើបណ្ណាល័យ `Microsoft.ML.OnnxRuntime`។ |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | គម្រោងគំរូដែលប្រើម៉ូឌែល Phi-4 របស់មូលដ្ឋានដើម្បីវិភាគឯកសារសំឡេង បង្កើតអត្ថាធិប្បាយនៃឯកសារ ហើយបង្ហាញលទ្ធផលនៅលើ console។ គម្រោងទាញយកម៉ូឌែល Phi-4-`multimodal-instruct-onnx` របស់មូលដ្ឋានដោយប្រើបណ្ណាល័យ `Microsoft.ML.OnnxRuntime`។ |

## របៀបរត់គម្រោង

ដើម្បីរត់គម្រោង ទៅតាមជំហានដូចខាងក្រោម៖

1. គូតចម្លងឃ្លាំងរក្សាទុកទៅកាន់កុំព្យួទ័ររបស់អ្នក។

1. បើក terminal ហើយទៅកាន់គម្រោងដែលចង់រត់។ ជាឧទាហរណ៍ យើងមាន `LabsPhi4-Chat-01OnnxRuntime`។

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. រត់គម្រោងដោយបញ្ជា

    ```bash
    dotnet run
    ```

1. គំរូគម្រោងស្នើសុំបញ្ចូលពីអ្នកប្រើ និងឆ្លើយតបដោយប្រើម៉ូឌែលក្នុងកន្លែង។

   សាកល្បងរត់មានរូបរាងស្រដៀងនឹងនេះ៖

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារ​នេះ​ត្រូវ​បាន​បកប្រែ​ដោយ​ប្រើសេវាកម្ម​បកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេល​យើង​ព្យាយាម​សម្រាប់​ភាព​ត្រឹមត្រូវ សូម​កុំភ្លេច​ថា​ការ​បកប្រែដោយ​ស្វ័យប្រវត្តិ​អាច​មាន​កំហុស ឬ​ការ​ត្រឹមត្រូវ​កន្លះ​កន្លែង​បាន។ ឯកសារ​ដើម​នៅ​ក្នុង​ភាសា​ដើម​គួរត្រូវបាន​លើកឡើង​ជា​ប្រភព​ដើម​ដែល​មានសារៈសំខាន់។ សម្រាប់​ព័ត៌មាន​សំខាន់ៗ ការបកប្រែ​ដោយ​ជំនាញ​មនុស្ស​ប្រកប​ដោយ​វិជ្ជាជីវៈ​ត្រូវ​បាន​ផ្តល់អនុសាសន៍។ យើង​មិន​ទទួល​ខុសត្រូវ​ចំពោះ​ការ​ច្របូកច្របល់ ឬ​ការបក​ប្រែ​ខុសៗ​ដែល​កើតមាន​ពីការប្រើប្រាស់​បកប្រែ​នេះ​ទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->