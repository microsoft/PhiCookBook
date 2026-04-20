# Phi-3.5-Instruct WebGPU RAG ឆាតបូត

## ឧទាហរណ៍សម្រាប់បង្ហាញ WebGPU និង លំនាំ RAG

លំនាំ RAG ជាមួយម៉ូដែល Phi-3.5 Onnx Hosted ប្រើវិធីសាស្ត្រ Retrieval-Augmented Generation ដោយបូកបញ្ចូលប្រសិទ្ធភាពនៃម៉ូដែល Phi-3.5 ជាមួយការជួលផ្ទុក ONNX សម្រាប់ការដាក់ប្រែប្រួល AI ឱ្យមានប្រសិទ្ធភាព។ លំនាំនេះមានប្រយោជន៍នៅក្នុងការកែលម្អម៉ូដែលសម្រាប់ភារកិច្ចជាក់លាក់ក្នុងដែនកំណត់ ផ្តល់នូវកំលាំងនៃគុណភាព ប្រកាន់ខ្ពស់ ថ្លៃគ្រប់គ្រាន់ និងការយល់ដឹងពីបរិបទរយៈពេលយូរ។ វាជាផ្នែកនៃឧបត្ថម្ភ Azure AI ដែលផ្តល់ជម្រើសម៉ូដែលជាច្រើនដែលងាយស្រួលរក សាកល្បង និងប្រើប្រាស់ ដើម្បីបំពេញតម្រូវការប្តូរផ្ទាល់ខ្លួននៃឧស្សាហកម្មនានា។

## WebGPU គឺជាអ្វី 
WebGPU គឺជាអនុប្បទានក្រាហ្វិកសម័យថ្មីសម្រាប់វែប ដែលរចនាឡើងដើម្បីផ្តល់នូវការចូលប្រើមួយទៅកាន់ GPU របស់ឧបករណ៍យ៉ាងមានប្រសិទ្ធភាពដោយផ្ទាល់ពីកម្មវិធីរុករកវែប។ វាត្រូវបានគេរំពឹងថาจะជាអ្នកជំនួស WebGL ដែលផ្តល់នូវការកែលម្អសំខាន់ៗខាងក្រោម៖

1. **Compatibility with Modern GPUs**: WebGPU ត្រូវបានបង្កើតដើម្បីធ្វើការងារយ៉ាងរលូនជាមួយស្ថាបัตยកម្ម GPU សម័យទំនើប ដោយប្រើប្រាស់ API ប្រព័ន្ធដូចជា Vulkan, Metal, និង Direct3D 12។
2. **Enhanced Performance**: វាគាំទ្រការគណនា GPU សម្រាប់គោលបំណងទូទៅ និងប្រតិបត្តិការយ៉ាងលឿនជាងមុន ធ្វើឱ្យវាសមស្របសម្រាប់ការរៀបចំក្រាហ្វិក និងភារកិច្ចសិក្សាម៉ាស៊ីន។
3. **Advanced Features**: WebGPU ផ្តល់ចូលដល់មុខងារអាចប្រើបានច្រើន និងអាចធ្វើការងារធ្ងន់ធ្ងរជាងមុន សម្រាប់ក្រុមការងារផ្នែកក្រាហ្វិក និងគណនាដែលស្មុគស្មាញ។
4. **Reduced JavaScript Workload**: ដោយផ្ញើភារកិច្ចច្រើនទៅកាន់ GPU វាធ្វើឲ្យមានការកាត់បន្ថយទម្ងន់ការងារលើ JavaScriptយ៉ាងច្រើន រួមនឹងបង្កើនប្រសិទ្ធភាព និងបទពិសោធន៍រលូនជាងមុន។

WebGPU នៅឡើយតែគាំទ្រនៅក្នុងកម្មវិធីរុករកមួយចំនួនដូចជា Google Chrome ជាមួយនឹងការងារដែលកំពុងបន្តដើម្បីពង្រីកការគាំទ្រទៅវេទិកាផ្សេងទៀត។

### 03.WebGPU
Required Environment:

**Supported browsers:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Enable WebGPU:

- In Chrome/Microsoft Edge 

Enable the `chrome://flags/#enable-unsafe-webgpu` flag.

#### Open Your Browser:
បើក Google Chrome ឬ Microsoft Edge។

#### Access the Flags Page:
នៅក្នុងបន្ទាត់អាសយដ្ឋាន (address bar) វាយ `chrome://flags` ហើយចុច Enter។

#### Search for the Flag:
នៅក្នុងប្រអប់ស្វែងរក​នៅខាងលើនៃទំព័រ វាយ 'enable-unsafe-webgpu'

#### Enable the Flag:
ស្វែងរក flag #enable-unsafe-webgpu ក្នុងបញ្ជីលទ្ធផល។

Click the dropdown menu next to it and select Enabled.

#### Restart Your Browser:

បន្ទាប់ពីបើក flag នេះ អ្នកត្រូវការចាប់ផ្តើមកម្មវិធីរុករកឡើងវិញ ដើម្បីឲ្យការផ្លាស់ប្តូរបានមានប្រសិទ្ធភាព។ ចុចប៊ូតុង Relaunch ដែលបង្ហាញនៅទីបញ្ចប់នៃទំព័រ។

- For Linux, launch the browser with `--enable-features=Vulkan`.
- Safari 18 (macOS 15) has WebGPU enabled by default.
- In Firefox Nightly, enter about:config in the address bar and `set dom.webgpu.enabled to true`.

### Setting up GPU for Microsoft Edge 

នេះជាជំហានដើម្បីកំណត់ GPU ប្រសិទ្ធភាពខ្ពស់សម្រាប់ Microsoft Edge លើ Windows:

- **Open Settings:** ចុចម៉ឺនុយ Start ហើយជ្រើស Settings។
- **System Settings:** ទៅកាន់ System ហើយបន្ទាប់មក Display។
- **Graphics Settings:** រំកិលចុះ និងចុច Graphics settings។
- **Choose App:** នៅក្រោម “Choose an app to set preference,” ជ្រើស Desktop app ហើយបន្ទាប់ Browse។
- **Select Edge:** នាវាតិចទៅកាន់ថតដំឡើង Edge (ធម្មតា `C:\Program Files (x86)\Microsoft\Edge\Application`) ហើយជ្រើស `msedge.exe`។
- **Set Preference:** ចុច Options, ជ្រើស High performance, ហើយបន្ទាប់ចុច Save។
This will ensure that Microsoft Edge uses your high-performance GPU for better performance. 
- **Restart** ម៉ាស៊ីនរបស់អ្នក ដើម្បីឲ្យការកំណត់ទាំងនេះមានប្រសិទ្ធភាព 

### Samples : Please [ចុចតំណនេះ](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**សេចក្ដីបដិសេធ**:
ឯកសារនេះត្រូវបានបកប្រែនៅតាមរបៀបដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator). ខណៈពេលដែលយើងខិតខំប្រឹងប្រែងដើម្បីភាពត្រឹមត្រូវ សូមចំណាំថាការបកប្រែដោយស្វ័យប្រវត្តិនេះអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមក្នុងភាសាមាតុភូមិគួរត្រូវបានយកជាប្រភពផ្លូវការដែលអាចទុកចិត្តបាន។ សម្រាប់ព័ត៌មានដែលសំខាន់ យើងសូមណែនាំឱ្យប្រើការបកប្រែដោយអ្នកវិជ្ជាជីវៈជាមនុស្ស។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសណាមួយ ដែលមានបណ្តាលមកពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->