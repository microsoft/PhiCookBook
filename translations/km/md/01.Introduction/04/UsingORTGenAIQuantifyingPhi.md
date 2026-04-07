# **ការបរិមាណបន្ថយ (Quantizing) របស់គ្រួសារ Phi ដោយប្រើផ្នែកបន្ថែម Generative AI សម្រាប់ onnxruntime**

## **អ្វីទៅជាផ្នែកបន្ថែម Generative AI សម្រាប់ onnxruntime**

ផ្នែកបន្ថែមនេះជួយអ្នករត់ Generative AI ជាមួយ ONNX Runtime( [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). វាផ្តល់ចង្វាក់ Generative AI សម្រាប់ម៉ូដែល ONNX រួមទាំង inference ជាមួយ ONNX Runtime, ការកែសម្រួល logits, ការស្វែងរក និងការសampling, និងការគ្រប់គ្រង KV cache។ អ្នកអភិវឌ្ឍអាចហៅមួយវិធាន generate() កម្រិតខ្ពស់ ឬរត់រៀងរាល់ iteration នៃម៉ូដែលក្នុង loop ដើម្បីផលិត token មួយៗនៅពេលមួយ ហើយអាចធ្វើការអាប់ដេតប៉ារ៉ាម៉ែត្រចាប់ផលិតក្នុង loop ។ វាសន្សំព័ន្ធគាំទ្រសម្រាប់ greedy/beam search និង TopP, TopK sampling ដើម្បីបង្កើតលំដាប់ token និងមានការកែសម្រួល logits កែលម្អដូចជា repetition penalties។ អ្នកក៏អាចបន្ថែម scoring ផ្ទាល់ខ្លួនបានយ៉ាងងាយស្រួល។

នៅលើកម្រិតកម្មវិធី អ្នកអាចប្រើ Generative AI extensions for onnxruntime ដើម្បីស្ថាបនា​កម្មវិធីប្រើ C++/ C# / Python។ នៅលើកម្រិតម៉ូដែល អ្នកអាចប្រើវាដើម្បីលាយម៉ូដែលដែលបានសិក្សាឡើងវិញ និងធ្វើការងារជាប់ពាក់ព័ន្ធនៃការដាក់បញ្ចូលទៅប្រព័ន្ធ។

## **ការបរិមាណបន្ថយ Phi-3.5 ជាមួយផ្នែកបន្ថែម Generative AI សម្រាប់ onnxruntime**

### **ម៉ូដែលដែលគាំទ្រ**

Generative AI extensions for onnxruntime គាំទ្រការបម្លែង quantization របស់ Microsoft Phi, Google Gemma, Mistral, Meta LLaMA។

### **Model Builder ក្នុង Generative AI extensions for onnxruntime**

Model Builder ជួយឱនល្បឿនយ៉ាងខ្លាំងក្នុងការបង្កើតម៉ូដែល ONNX ដែលបានជម្រុញ និងបាន quantize ដើម្បីរត់ជាមួយ API generate() របស់ ONNX Runtime។

តាមរយៈ Model Builder អ្នកអាចបម្រែបម្រួលម៉ូដែលទៅជា INT4, INT8, FP16, FP32, និងរួមបញ្ចូលវិធីសាស្រ្តកាន់តែជម្រុញរឹងលើ hardware ផ្សេងៗដូចជា CPU, CUDA, DirectML, Mobile, ល។ 

ដើម្បីប្រើ Model Builder អ្នកត្រូវតែដំឡើង

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

ក្រោយពេលដំឡើង អ្នកអាចរត់ស្គ្រីប Model Builder ពី terminal ដើម្បីអនុវត្តការបម្លែងទ្រង់ទ្រាយម៉ូដែល និង quantization។

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

យល់ពីប៉ារ៉ាម៉ែត្រដែលពាក់ព័ន្ធ

1. **model_name** នេះគឺជាម៉ូដែលនៅលើ Hugging face, ឧ. microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct, ល។ វាក៏អាចជាតំបន់ផ្លូវដែលអ្នករក្សាម៉ូដែលបានផ្ទុកផងដែរ

2. **path_to_output_folder** ផ្លូវសម្រាប់រក្សាការបម្លែងដែលបាន quantize

3. **execution_provider** ការគាំទ្រហardenware ផ្សេងៗដូចជា cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** យើងទាញយកម៉ូដែលពី Hugging face ហើយ cache វាទៅក្នុងម៉ាស៊ីនក្នុងស្រុក

***Note：*** <ul>ទោះបីជា Generative AI extensions for onnxruntime គឺនៅក្នុងជំហាន preview ក៏ដោយ វាគឺត្រូវបានដំឡើងចូលទៅក្នុង Microsoft Olive ហើយអ្នកក៏អាចហៅមុខងារ Model Builder របស់ Generative AI extensions for onnxruntime តាមរយៈ Microsoft Olive បានផងដែរ។</ul>

## **របៀបប្រើ Model Builder ដើម្បីធ្វើ Quantizing លើ Phi-3.5**

Model Builder ឥឡូវគាំទ្រការបរិមាណបន្ថយម៉ូដែល ONNX សម្រាប់ Phi-3.5 Instruct និង Phi-3.5-Vision

### **Phi-3.5-Instruct**


**ការបម្លែងដែលបានលឿនដោយ CPU ទៅជាម៉ូដែល Quantized INT 4**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**ការបម្លែងដែលបានលឿនដោយ CUDA ទៅជាម៉ូដែល Quantized INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. កំណត់បរិយាកាសនៅ terminal

```bash

mkdir models

cd models 

```

2. ទាញ microsoft/Phi-3.5-vision-instruct ទៅក្នុងថត models
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. សូមទាញយកឯកសារទាំងនេះទៅក្នុងថត Phi-3.5-vision-instruct របស់អ្នក

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. ទាញឯកសារនេះទៅក្នុងថត models
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. ទៅកាន់ terminal

    បម្លែង ONNX ដើម្បីគាំទ្រជាមួយ FP32


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **សម្គាល់：**

1. Model Builder សព្វថ្ងៃគាំទ្រការបម្លែង Phi-3.5-Instruct និង Phi-3.5-Vision តែម្ដង មិនទាន់គាំទ្រ Phi-3.5-MoE

2. ដើម្បីប្រើម៉ូដែល quantized របស់ ONNX អ្នកអាចប្រើវាតាមរយៈ Generative AI extensions for onnxruntime SDK

3. យើងត្រូវចាប់អារម្មណ៍ច្រើនទាក់ទងនឹង AI ដែលទទួលខុសត្រូវ ដូច្នេះក្រោយពីការបម្លែង quantization គឺផ្តល់ការណែនាំឲ្យ​ធ្វើតេស្តលទ្ធផលឲ្យមានប្រសិទ្ធភាពច្រើនជាងមុន

4. ដោយការបរិមាណបន្ថយម៉ូដែល CPU INT4 យើងអាចដាក់ចេញទៅឧបករណ៍ Edge ដែលមានទស្សនៈអនុវត្តឲ្យល្អប្រសើរ ដូច្នេះយើងបានបញ្ចប់ Phi-3.5-Instruct ជុំវិញ INT 4

## **ធនធាន**

1. ស្វែងយល់បន្ថែមអំពី Generative AI extensions for onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime GitHub Repo [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការមិនទទួលខុសត្រូវ**:
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាប្រែភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះបីយើងខិតខំប៉ុនណាក៏ដោយ សូមយកចិត្តទុកដាក់ថាការបកប្រែដោយស្វ័យប្រវត្តិក្នុងករណីខ្លះអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមក្នុងភាសាដើមគួរត្រូវបានចាត់ទុកជា​ប្រភពផ្លូវការ។ សម្រាប់ព័ត៌មានដែលមានសារៈសំខាន់ យើងសូមផ្ដល់អនុសាសន៍ឱ្យធ្វើការបកប្រែដោយអ្នកបកប្រែវិជ្ជាជីវៈ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសណាមួយដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->