## សូមស្វាគមន៍មកកាន់ Phi labs ដែលប្រើ C#

មានជម្រើសនៃ labs ដែលបង្ហាញពីរបៀបបញ្ចូលកំណែផ្សេងៗដ៏មានអំណាចនៃម៉ូឌែល Phi ក្នុងបរិយាកាស .NET ។

## តម្រូវការមុន

មុននឹងរត់ឧទាហរណ៍ សូមធ្វើឲ្យប្រាកដថាអ្នកបានដំឡើងខាងក្រោម៖

**.NET 9:** សូមប្រាកដថាអ្នកបានដំឡើង [កំណែថ្មីបំផុតនៃ .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) លើម៉ាស៊ីនរបស់អ្នក។

**(ជាជម្រើស) Visual Studio ឬ Visual Studio Code:** អ្នកនឹងត្រូវការ IDE ឬកម្មវិធីកែសម្រួលកូដដែលមានសមត្ថភាពរត់គម្រោង .NET។ [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) ឬ [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) ត្រូវបានផ្តល់អនុសាសន៍។

**ប្រើ git** clone មួយក្នុងស្រុកពីកំណែដែលមានដូចជា Phi-3, Phi3.5 ឬ Phi-4 ពី [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c)។

**ទាញយកម៉ូដែល Phi-4 ONNX** ទៅម៉ាស៊ីនក្នុងស្រុករបស់អ្នក៖

### ចូលទៅកាន់ថតសម្រាប់ផ្ទុកម៉ូឌែល

```bash
cd c:\phi\models
```

### បន្ថែមការគាំទ្រសម្រាប់ lfs

```bash
git lfs install 
```

### clone និងទាញយកម៉ូឌែល Phi-4 mini instruct និងម៉ូឌែល Phi-4 multi modal

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**ទាញយកម៉ូដែល Phi-3 ONNX** ទៅម៉ាស៊ីនក្នុងស្រុករបស់អ្នក៖

### clone និងទាញយក Phi-3 mini 4K instruct model និង Phi-3 vision 128K model

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**សំខាន់:** កម្មវិធីបង្ហាញបច្ចុប្បន្ននេះត្រូវបានរចនាឡើងដើម្បីប្រើកំណែ ONNX នៃម៉ូឌែល។ ជំហានមុនៗបាន clone ម៉ូឌែលដូចខាងក្រោម។

## អំពី Labs

ដំណោះស្រាយស្នូលមាន Labs ឧទាហរណ៍ជាច្រើនដែលបង្ហាញពីសមត្ថភាពនៃម៉ូឌែល Phi ដោយប្រើ C#។

| គម្រោង | ម៉ូឌែល | ការពិពណ៌នា |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 or Phi-3.5 | ឧទាហរណ៍សេចក្តីជជែកក្នុងកុងសូលដែលអនុញ្ញាតឲ្យអ្នកប្រើសួរសំណួរ។ គម្រោងនេះផ្ទុកម៉ូឌែល ONNX Phi-3 ក្នុងស្រុកដោយប្រើបណ្ណាល័យ `Microsoft.ML.OnnxRuntime`។ |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 or Phi-3.5 | ឧទាហរណ៍សេចក្តីជជែកក្នុងកុងសូលដែលអនុញ្ញាតឲ្យអ្នកប្រើសួរសំណួរ។ គម្រោងនេះផ្ទុកម៉ូឌែល ONNX Phi-3 ក្នុងស្រុកដោយប្រើបណ្ណាល័យ `Microsoft.Semantic.Kernel`។ |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 or Phi-3.5 | នេះជាគម្រោងឧទាហរណ៍ដែលប្រើម៉ូឌែល phi3 vision ក្នុងស្រុកដើម្បីវិភាគរូបភាព។ គម្រោងនេះផ្ទុកម៉ូឌែល ONNX Phi-3 Vision ក្នុងស្រុកដោយប្រើបណ្ណាល័យ `Microsoft.ML.OnnxRuntime`។ |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 or Phi-3.5 | នេះជាគម្រោងឧទាហរណ៍ដែលប្រើម៉ូឌែល phi3 vision ក្នុងស្រុកដើម្បីវិភាគរូបភាព។ គម្រោងនេះផ្ទុកម៉ូឌែល ONNX Phi-3 Vision ក្នុងស្រុកដោយប្រើបណ្ណាល័យ `Microsoft.ML.OnnxRuntime`។ គម្រោងនេះក៏បង្ហាញម៉ឺនុយជាមួយជម្រើសផ្សេងៗសម្រាប់អន្តរកម្មជាមួយអ្នកប្រើ។ | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | ឧទាហរណ៍សេចក្តីជជែកក្នុងកុងសូលដែលអនុញ្ញាតឲ្យអ្នកប្រើសួរសំណួរ។ គម្រោងនេះផ្ទុកម៉ូឌែល ONNX Phi-4 ក្នុងស្រុកដោយប្រើបណ្ណាល័យ `Microsoft.ML.OnnxRuntime`។ |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | ឧទាហរណ៍សេចក្តីជជែកក្នុងកុងសូលដែលអនុញ្ញាតឲ្យអ្នកប្រើសួរសំណួរ។ គម្រោងនេះផ្ទុកម៉ូឌែល ONNX Phi-4 ក្នុងស្រុកដោយប្រើបណ្ណាល័យ `Semantic Kernel`។ |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | ឧទាហរណ៍សេចក្តីជជែកក្នុងកុងសូលដែលអនុញ្ញាតឲ្យអ្នកប្រើសួរសំណួរ។ គម្រោងនេះផ្ទុកម៉ូឌែល ONNX Phi-4 ក្នុងស្រុកដោយប្រើបណ្ណាល័យ `Microsoft.ML.OnnxRuntimeGenAI` ហើយអ롭ផ្តល់អនុវត្ត `IChatClient` ពី `Microsoft.Extensions.AI`។ |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | ឧទាហរណ៍សេចក្តីជជែកក្នុងកុងសូលដែលអនុញ្ញាតឲ្យអ្នកប្រើសួរសំណួរ។ chat នេះអនុវត្តប្រព័ន្ធចងចាំ។ |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | នេះជាគម្រោងឧទាហរណ៍ដែលប្រើម៉ូឌែល Phi-4 ក្នុងស្រុកដើម្បីវិភាគរូបភាព ហើយបង្ហាញលទ្ធផលនៅក្នុងកុងសូល។ គម្រោងនេះផ្ទុកម៉ូឌែល Phi-4-`multimodal-instruct-onnx` ក្នុងស្រុកដោយប្រើបណ្ណាល័យ `Microsoft.ML.OnnxRuntime`។ |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | នេះជាគម្រោងឧទាហរណ៍ដែលប្រើម៉ូឌែល Phi-4 ក្នុងស្រុកដើម្បីវិភាគឯកសារសំលេង បង្កើតបទចម្លងនៃឯកសារ ហើយបង្ហាញលទ្ធផលនៅក្នុងកុងសូល។ គម្រោងនេះផ្ទុកម៉ូឌែល Phi-4-`multimodal-instruct-onnx` ក្នុងស្រុកដោយប្រើបណ្ណាល័យ `Microsoft.ML.OnnxRuntime`។ |

## របៀបរត់គម្រោង

ដើម្បីរត់គម្រោង ទូទាំងអនុវត្តជំហានដូចខាងក្រោម៖

1. Clone ឃ្លៀបធុងកូដទៅម៉ាស៊ីនក្នុងស្រុករបស់អ្នក។

1. បើក terminal ហើយចូលទៅគម្រោងដែលចង់រត់។ ឧទាហរណ៍ អ្នកអាចរត់ `LabsPhi4-Chat-01OnnxRuntime`។

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. រត់គម្រោងដោយប្រើពាក្យបញ្ជា

    ```bash
    dotnet run
    ```

1. គម្រោងឧទាហរណ៍នឹងសុំការបញ្ចូលពីអ្នកប្រើ ហើយឆ្លើយតបទៅវិញដោយប្រើម៉ូដក្នុងស្រុក។ 

   ការបង្ហាញដំណើរការដូចខាងក្រោម៖

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែតាម AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈដែលយើងខិតខំរកភាពត្រឹមត្រូវ សូមកត់សម្គាល់ថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬការមិនត្រឹមត្រូវ។ ឯកសារដើមក្នុងភាសាដើមគួរត្រូវបានចាត់ទុកជាប្រភពចម្បង។ សម្រាប់ព័ត៌មានសំខាន់ៗ យើងសូមផ្តល់អនុសាសន៍ឱ្យប្រើការបកប្រែដោយអ្នកជំនាញមនុស្ស។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសណាមួយដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->