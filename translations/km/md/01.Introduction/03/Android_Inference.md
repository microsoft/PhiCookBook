# **ការបញ្ចេញផលសន្និដ្ឋាន Phi-3 លើ Android**

មកស្វែងយល់ពីវិធីដែលអ្នកអាចបញ្ចេញផលសន្និដ្ឋានជាមួយ Phi-3-mini លើឧបករណ៍ Android បាន។ Phi-3-mini គឺជាស៊េរីម៉ូឌែលថ្មីពី Microsoft ដែលអាចអនុញ្ញាតឱ្យដំឡើងម៉ូឌែលភាសាធំៗ (LLMs) លើឧបករណ៍កម្រិតខាងចុង និងឧបករណ៍ IoT។

## Semantic Kernel និងការបញ្ចេញផលសន្និដ្ឋាន

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) គឺជាស៊ុមប្រើកម្មវិធីដែលអនុញ្ញាតឱ្យអ្នកបង្កើតកម្មវិធីដែលត្រូវគ្នាក្នុងសេវាកម្ម Azure OpenAI, ម៉ូឌែល OpenAI, និងម៉ូឌែលក្នុងតំបន់ផ្ទាល់។ ប្រសិនបើអ្នកថ្មីចំពោះ Semantic Kernel យើងសូមណែនាំឱ្យសូមមើល [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)។

### ដើម្បីចូលប្រើ Phi-3-mini ដោយប្រើ Semantic Kernel

អ្នកអាចចម្រុះវាជាមួយកម្មវិធី Hugging Face Connector ក្នុង Semantic Kernel។ សូមយោងទៅកូដគំរូនេះ [Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)។

ដំណើរការដើមវានឹងផ្គូរផ្គងទៅម៉ូឌែលគោលលើ Hugging Face ប៉ុន្តែអ្នកក៏អាចភ្ជាប់ទៅម៉ូឌែល Phi-3-mini ដែលបានបង្កើតនៅក្នុងតំបន់ផ្ទាល់បានផងដែរ។

### ការហៅម៉ូឌែល Quantized ជាមួយ Ollama ឬ LlamaEdge

អ្នកប្រើប្រាស់ច្រើនចូលចិត្តប្រើម៉ូឌែល quantized ដើម្បីដំណើរការ ម៉ូឌែលក្នុងតំបន់ផ្ទាល់។ [Ollama](https://ollama.com/) និង [LlamaEdge](https://llamaedge.com) អនុញ្ញាតឱ្យអ្នកប្រើតែម្នាក់ៗអាចហៅម៉ូឌែល quantized ផ្សេងៗគ្នា។

#### Ollama

អ្នកអាចដំណើរការ `ollama run Phi-3` តាមផ្ទាល់ ឬក៏កំណត់វាពីក្រៅបណ្តាញដោយបង្កើត `Modelfile` ជាមួយផ្លូវទៅឯកសារ `.gguf` របស់អ្នក។

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

ប្រសិនបើអ្នកចង់ប្រើឯកសារ `.gguf` លើពពក និងឧបករណ៍កម្រិតខាងចុងជាលាយលក្ខណៈសម័យនាពេលតែមួយ LlamaEdge គឺជាជម្រើសដ៏ល្អ។ អ្នកអាចយោងទៅកូដគំរូនេះ [sample code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) ដើម្បីចាប់ផ្តើម។

### ដំឡើង និងដំណើរការលើទូរស័ព្ទ Android

1. **ទាញយកកម្មវិធី MLC Chat** (ឥតគិតថ្លៃ) សម្រាប់ទូរស័ព្ទ Android។
2. ទាញយកឯកសារ APK (148MB) ហើយដំឡើងវាលើឧបករណ៍របស់អ្នក។
3. បើកកម្មវិធី MLC Chat។ អ្នកនឹងឃើញបញ្ជីម៉ូឌែល AI រួមមាន Phi-3-mini។

សង្ខេបមកវិញ Phi-3-mini បើកឱ្យមានឱកាសច្រើនសម្រាប់ AI បង្កើតលើឧបករណ៍កម្រិតខាងចុង ហើយអ្នកអាចចាប់ផ្តើមស្វែងយល់ពីសមត្ថភាពរបស់វាលើ Android បាន។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទាំងពួកយើងខិតខំប្រឹងប្រែងឱ្យបានត្រឹមត្រូវ ប៉ុន្តែសូមយល់ឱ្យបានថាការបកប្រែដោយស្វ័យប្រវត្តិក្នុងខ្លះអាចមានកំហុសឬច្របល់។ ឯកសារដើមជាភាសាទុំដើមគួរត្រូវបានទទួលស្គាល់ថាជាឯកសារដោយផ្លូវការជាមូលដ្ឋាន។ សម្រាប់ព័ត៌មានសំខាន់ៗ គួរត្រូវប្រើប្រាស់ការបកប្រែដោយមនុស្សអ្នកជំនាញ។ ពួកយើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការពន្យល់ខុសពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->