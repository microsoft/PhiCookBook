# **ការប៉ាន់ស្មានដោយ Phi-3 លើ Android**

ចូរយើងស្វែងយល់ពីរបៀបដែលអ្នកអាចធ្វើការប៉ាន់ស្មាន (inference) ជាមួយ Phi-3-mini លើឧបករណ៍ Android។ Phi-3-mini គឺជាស៊េរីម៉ូដែលថ្មីពី Microsoft ដែលអនុញ្ញាតឲ្យធ្វើការដាក់ប្រើប្រាស់ Large Language Models (LLMs) លើឧបករណ៍ edge និងឧបករណ៍ IoT។

## Semantic Kernel និង ការប៉ាន់ស្មាន

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) ជាស៊ុមប្រព័ន្ធកម្មវិធី (application framework) ដែលអនុញ្ញាតឲ្យអ្នកបង្កើតកម្មវិធីដែលត្រូវគ្នាជាមួយ Azure OpenAI Service, ម៉ូដែល OpenAI, និងម៉ូដែលក្នុងស្រុកផងដែរ។ ប្រសិនបើអ្នកមើលទៅ Semantic Kernel ជាថ្មី យើងសូមណែនាំឲ្យអ្នកមើល [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)។

### ដើម្បីចូលដំណើរការ Phi-3-mini ដោយប្រើ Semantic Kernel

អ្នកអាចរួមបញ្ចូលវាជាមួយ Hugging Face Connector នៅក្នុង Semantic Kernel។ សូមយោងទៅកាន់ [កូដឧទាហរណ៍](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo) នេះ។

ម្យ៉ាងវិញទៀត ដោយលំនាំដើម វាសម្របស្មើនឹង model ID លើ Hugging Face។ ទោះជាយ៉ាងណាក៏ដោយ អ្នកអាចភ្ជាប់ទៅកាន់ម៉ាស៊ីនម៉ូដែល Phi-3-mini ដែលបានសង់ក្នុងស្រុកក៏បាន។

### ការហៅម៉ូដែលដែលបានធ្វើ Quantize ជាមួយ Ollama ឬ LlamaEdge

អ្នកច្រើនចូលចិត្តប្រើម៉ូដែលដែលបានធ្វើ quantized ដើម្បីរត់ម៉ូដែលក្នុងស្រុក។ [Ollama](https://ollama.com/) និង [LlamaEdge](https://llamaedge.com) អនុញ្ញាតឲ្យអ្នកប្រើប្រាស់និចៗហៅម៉ូដែល quantized ផ្សេងៗបាន៖

#### Ollama

អ្នកអាចរត់បានដោយផ្ទាល់ `ollama run Phi-3` ឬកំណត់វាឲ្យអោយដំណើរការបិទបាំង (offline) ដោយបង្កើត `Modelfile` ដែលមានផ្លូវទៅកាន់ឯកសារ `.gguf` របស់អ្នក។

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[កូដឧទាហរណ៍](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

ប្រសិនបើអ្នកចង់ប្រើឯកសារ `.gguf` ទាំងនៅក្នុងពពក និងលើឧបករណ៍ edge ព្រមគ្នា LlamaEdge គឺជាជម្រើសល្អ។ អ្នកអាចយោងទៅកាន់ [កូដឧទាហរណ៍](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) នេះដើម្បីចាប់ផ្តើម។

### ដំឡើង និង រត់លើទូរស័ព្ទ Android

1. **ទាញយកកម្មវិធី MLC Chat** (ឥតគិតថ្លៃ) សម្រាប់ទូរស័ព្ទ Android។
2. ទាញយកឯកសារ APK (148MB) ហើយដំឡើងវាលើឧបករណ៍របស់អ្នក។
3. ចាប់ផ្តើមកម្មវិធី MLC Chat។ អ្នកនឹងឃើញបញ្ជីម៉ូដែល AI មួយចំនួន រួមទាំង Phi-3-mini។

សង្ខេប គឺ Phi-3-mini បើកឲ្យមានឱកាសចំរូងចំរាសសម្រាប់ AI នៃការបង្កើតខ្លួនលើឧបករណ៍ edge ហើយអ្នកអាចចាប់ផ្តើមស្វែងយល់ពីសមត្ថភាពរបស់វាលើ Android។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការមិនទទួលខុសត្រូវ**:
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះបីយើងខិតខំរកភាពត្រឹមត្រូវក៏ដោយ សូមយល់ថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬភាពមិនសមត្រូវបាន។ ឯកសារដើមក្នុងភាសាក្ដីគួរត្រូវបានចាត់ទុកថាជាប្រភពដែលមានសុពលភាព។ សម្រាប់ព័ត៌មានសំខាន់ៗ យើងផ្តល់អនុសាសន៍ឱ្យប្រើការបកប្រែដោយអ្នកជំនាញមនុស្ស។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកអត្ថន័យខុសណាមួយដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->