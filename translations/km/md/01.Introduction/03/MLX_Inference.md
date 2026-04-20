# **បញ្ចេញលទ្ធផល Phi-3 ជាមួយ Apple MLX Framework**

## **MLX Framework ជាអ្វី**

MLX គឺជា​ប្រព័ន្ធ​ម៉ាទ្រីសសម្រាប់ការស្រាវជ្រាវម៉ាស៊ីនរៀនលើ Apple silicon, ដែលផ្តល់ឲ្យអ្នកដោយក្រុមស្រាវជ្រាវម៉ាស៊ីនរៀន Apple។

MLX ត្រូវបានរចនាឡើងដោយអ្នកស្រាវជ្រាវម៉ាស៊ីនរៀនសម្រាប់អ្នកស្រាវជ្រាវម៉ាស៊ីនរៀន។ ប្រព័ន្ធនេះមានគោលបំណងធ្វើឲ្យងាយស្រួលសម្រាប់អ្នកប្រើ ប៉ុន្តែក៏មានប្រសិទ្ធភាពក្នុងការបណ្តុះ បណ្តើរ និងបញ្ចេញម៉ូដែលផងដែរ។ ការរចនានៃប្រព័ន្ធផ្ទាល់ខ្លួនក៏មានភាពសាមញ្ញទ្រឹស្តីផងដែរ។ លោកយើងមានចេតនាធ្វើឲ្យមានភាពងាយស្រួលសម្រាប់អ្នកស្រាវជ្រាវក្នុងការពង្រីក និងបង្កើន MLX ដើម្បីស្វែងរកគំនិតថ្មីៗយ៉ាងរហ័ស។

LLMs អាចទទួលបានការបញ្ឈឺលឿនលើឧបករណ៍ Apple Silicon តាមរយៈ MLX ហើយម៉ូដែលអាចរត់បានក្នុងមូលដ្ឋានយ៉ាងងាយស្រួល។

## **ប្រើ MLX ដើម្បីបញ្ចេញលទ្ធផល Phi-3-mini**

### **1. Set up you MLX env**

1. Python 3.11.x
2. ដំឡើងបណ្ណាល័យ MLX


```bash

pip install mlx-lm

```

### **2. Running Phi-3-mini in Terminal with MLX**


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

លទ្ធផល (បរិយាកាស​របស់ខ្ញុំគឺ Apple M1 Max,64GB) គឺ

![ផ្ទាំងបញ្ជា](../../../../../translated_images/km/01.5cf57df8f7407cf9.webp)

### **3. Quantizing Phi-3-mini with MLX in Terminal**


```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***កំណត់ចំណាំ：*** ម៉ូឌែលអាចត្រូវបានបម្រាស់តាមរយៈ mlx_lm.convert ហើយការបម្រាស់លំនាំដើមគឺ INT4។ ឧទាហរណ៍នេះបានបម្រាស់ Phi-3-mini ទៅជា INT4

ម៉ូឌែលអាចត្រូវបានបម្រាស់តាមរយៈ mlx_lm.convert ហើយការបម្រាស់លំនាំដើមគឺ INT4។ ឧទាហរណ៍នេះគឺដើម្បីបម្រាស់ Phi-3-mini ទៅជា INT4។ បន្ទាប់ពីបម្រាស់ វានឹងត្រូវបានរក្សាទុកនៅក្នុងថតលំនាំដើម ./mlx_model

យើងអាចសាកល្បងម៉ូឌែលដែលបានបម្រាស់ជាមួយ MLX ពី Terminal បាន


```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

លទ្ធផលគឺ

![INT4](../../../../../translated_images/km/02.7b188681a8eadbc1.webp)


### **4. Running Phi-3-mini with MLX in Jupyter Notebook**


![សៀវភៅកត់ត្រា](../../../../../translated_images/km/03.b9705a3a5aaa89f9.webp)

***កំណត់ចំណាំ:*** សូមអានគំរូនេះ [ចុចតំណភ្ជាប់នេះ](../../../code/03.Inference/MLX/MLX_DEMO.ipynb)


## **ធនធាន**

1. ស្វែងយល់អំពី Apple MLX Framework [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. ឃ្លាំងកូដ GitHub របស់ Apple MLX [https://github.com/ml-explore](https://github.com/ml-explore)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការមិនទទួលខុសត្រូវ**:
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាបកប្រែដោយបញ្ញាសិប្បនិម្មិត [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខិតខំដើម្បីឱ្យបានត្រឹមត្រូវ សូមចំណាំថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬមិនត្រឹមត្រូវ។ ឯកសារដើមនៅក្នុងភាសាទីដើមគួរត្រូវបានចាត់ទុកជាប្រភពដែលមានអាទិភាព។ សម្រាប់ព័ត៌មានសំខាន់ៗ យើងសូមណែនាំឱ្យធ្វើការបកប្រែដោយអ្នកបកប្រែវិជ្ជាជីវៈ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសណាមួយដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->