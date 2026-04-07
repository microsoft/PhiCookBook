# **ការធ្វើ Quantization លើគ្រួសារប្រភេទ Phi ដោយប្រើ llama.cpp**

## **llama.cpp គឺជាអ្វី**

llama.cpp គឺជា​បណ្ណាល័យកម្មវិធី​កូដ​ស្មើ (open-source) ដែលសរសេរជាចម្បងក្នុង C++ ដែលបំពេញការប៉ាន់ស្មានលើម៉ូឌែលភាសាធំនានា (LLMs) ដូចជា Llama។ គោលបំណងចម្បងរបស់វាគឺផ្តល់កម្រិតក الأداء នៃការប៉ាន់ស្មាន LLMs ដែលទាន់សម័យលើឧបករណ៍នានាដោយមានការកំណត់តិចតួចបំផុត។ លើសពីនេះទៀត មានការចងភ្ជាប់ Python សម្រាប់បណ្ណាល័យនេះផង ដែលផ្តល់ API កម្រិតខ្ពស់សម្រាប់ការបញ្ចប់អត្ថបទ និងម៉ាស៊ីនបម្រើបណ្តាញដែលសមស្របជាមួយ OpenAI។

គោលបំណងចម្បងរបស់ llama.cpp គឺធ្វើឲ្យអាចធ្វើការប៉ាន់ស្មាន LLMs បានដោយការកំណត់តិច និងមានការសម្តែងជាន់ខ្ពស់លើឧបករណ៍ជាច្រើន - តាមរយៈកុំព្យូទ័រប្រព័ន្ធជួនខ្លួន និងក្នុងពពក។

- ការអនុវត្តជា C/C++ លាក់សុទ្ធដោយគ្មានការពឹងផ្អែកលើបណ្ណាល័យផ្សេងៗ
- Apple silicon គឺជាឧបករណ៍មានអាទិភាព - បានធ្វើអופטিমីស៍តាម ARM NEON, Accelerate និង Metal frameworks
- ការគាំទ្រ AVX, AVX2 និង AVX512 សម្រាប់ស្ថាបត្យកម្ម x86
- ការធ្វើ Quantization ជា អ៊ីនទេហ្ស៊ែរ 1.5-ប៊ីត, 2-ប៊ីត, 3-ប៊ីត, 4-ប៊ីត, 5-ប៊ីត, 6-ប៊ីត និង 8-ប៊ីត សម្រាប់ការប៉ាន់ស្មានលឿន និងការបន្ថយការប្រើប្រាស់ម៉េមូរី
- គernels CUDA ផ្ទាល់ខ្លួនសម្រាប់រត់ LLMs លើ NVIDIA GPUs (គាំទ្រសម្រាប់ AMD GPUs តាមរយៈ HIP)
- ការគាំទ្រ backend Vulkan និង SYCL
- ការប៉ាន់ស្មាន CPU+GPU រួមគ្នា ដើម្បីលឿនផ្នែកមួយនៃម៉ូឌែលដែលធំជាងសមត្ថភាព VRAM សរុប

## **Quantizing Phi-3.5 with llama.cpp**

ម៉ូឌែល Phi-3.5-Instruct អាចត្រូវបានធ្វើ Quantization ដោយប្រើ llama.cpp, ប៉ុន្តែ Phi-3.5-Vision និង Phi-3.5-MoE មិនទាន់គាំទ្រ។ ទ្រង់ទ្រាយដែលបាន​បម្លែង​ដោយ llama.cpp គឺ gguf, ដែលក៏ជាទ្រង់ទ្រាយ Quantization ដែលមានការប្រើប្រាស់ទូលំទូលាយផងដែរ។

មានម៉ូឌែលទ្រង់ទ្រាយ GGUF ដែលបាន Quantize ច្រើននៅលើ Hugging face។ AI Foundry, Ollama, និង LlamaEdge ពឹងផ្អែកលើ llama.cpp ដូច្នេះម៉ូឌែល GGUF ក៏ត្រូវបានប្រើញឹកញាប់ផងដែរ។

### **GGUF ជាអ្វី**

GGUF គឺជា​ទ្រង់ទ្រាយពីរមាន (binary) ដែលបានអុបទុំព្យូសម្រាប់ការលោតចូល និងរក្សាទុកម៉ូឌែលយ៉ាងរហ័ស រួមផ្តល់នូវប្រសិទ្ធភាពខ្ពស់សម្រាប់គោលបំណងប៉ាន់ស្មាន។ GGUF ត្រូវបានរចនាឡើងសម្រាប់ការប្រើប្រាស់ជាមួយ GGML និងកម្មវិធីអនុវត្តផ្សេងៗ។ GGUF ត្រូវបានអភិវឌ្ឍដោយ @ggerganov ដែលក៏ជាអ្នកអភិវឌ្ឍ llama.cpp ផង, គឺជា​ក្របខ័ណ្ឌ C/C++ សម្រាប់ការប៉ាន់ស្មាន LLM ដែលពេញនិយម។ ម៉ូឌែលដែលបានអភិវឌ្ឍដំបូងក្នុងក្របខ័ណ្ឌដូចជា PyTorch អាចត្រូវបានបម្លែងទៅទ្រង់ទ្រាយ GGUF សម្រាប់ការប្រើប្រាស់ជាមួយនឹងម៉ាស៊ីនដោះស្រាយទាំងនេះ។

### **ONNX ប្រៀបធៀបនឹង GGUF**

ONNX គឺជា​ទ្រង់ទ្រាយរំនងដំណើរការแมชชีนឡឺណាំង/ឌីពឡឺណាំង ដែលមានការគាំទ្រល្អនៅក្នុងក្របខ័ណ្ឌ AI ផ្សេងៗ និងមានស្ថានភាពប្រើប្រាស់ល្អនៅលើឧបករណ៍អេជ (edge devices)។ សម្រាប់ GGUF វាគឺផ្អែកលើ llama.cpp ហើយអាចនិយាយបានថាត្រូវបានផលិតក្នុងសម័យ GenAI។ ទាំងពីរមានការប្រើប្រាស់ដូចគ្នាក្នុងក្របខ័ណ្ឌមួយចំនួន។ ប្រសិនបើអ្នកចង់បានការសម្តែងល្អនៅលើឧបករណ៍បញ្ចូល ហើយស្របតាម​ស្រទាប់កម្មវិធី អ្នកអាចជ្រើស ONNX។ ប្រសិនបើអ្នកប្រើបច្ចេកវិទ្យា និងក្របខ័ណ្ឌដែលបាននាំចេញពី llama.cpp, GGUF អាចល្អជាង។

### **ការធ្វើ Quantization លើ Phi-3.5-Instruct ដោយប្រើ llama.cpp**

**1. ការរៀបចំបរិយាកាស**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Quantization**

ប្រើ llama.cpp ដើម្បីបម្លែង Phi-3.5-Instruct ទៅ FP16 GGUF


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Quantizing Phi-3.5 to INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. ការធ្វើតេស្ត**

ដំឡើង llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***ចំណាំ*** 

ប្រសិនបើអ្នកប្រើ Apple Silicon , សូមដំឡើង llama-cpp-python ដូចនេះ


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

ការធ្វើតេស្ត 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **ធនធាន**

1. រៀន​បន្ថែម​អំពី llama.cpp [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
2. រៀន​បន្ថែម​អំពី onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)
3. រៀន​បន្ថែម​អំពី GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការមិនទទួលខុសត្រូវ**:
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាបកប្រែក្នុងប្រព័ន្ធ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះបីយើងព្យាយាមឲ្យមានភាពត្រឹមត្រូវ សូមជ្រាបថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬមានចំណុចមិនត្រឹមត្រូវ។ ឯកសារដើមនៅក្នុងភាសាដើមគួរត្រូវបានយកទៅជាមូលដ្ឋានដែលមានអំណាចបំផុត។ សម្រាប់ព័ត៌មានសំខាន់ៗ យើងផ្តល់អនុសាសន៍ឲ្យប្រើការបកប្រែដោយអ្នកជំនាញជាមនុស្ស។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកប្រែខុសដែលកើតឡើងដោយសារការប្រើការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->