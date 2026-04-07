# **ការសន្មត់ Phi-3 ជាមួយស៊ុម Apple MLX**

## **MLX Framework ជាអ្វី**

MLX គឺជាស៊ុមអារេសម្រាប់ស្រាវជ្រាវម៉ាស៊ីនរៀនលើស៊ីលីកុន Apple ដែលផ្តល់ដោយការស្រាវជ្រាវម៉ាស៊ីនរៀនរបស់ Apple ។

MLX ត្រូវបានរចនាឡើងដោយអ្នកស្រាវជ្រាវម៉ាស៊ីនរៀនសម្រាប់អ្នកស្រាវជ្រាវម៉ាស៊ីនរៀន។ ស៊ុមនេះមានគោលបំណងធ្វើឱ្យមានភាពងាយស្រួលសម្រាប់អ្នកប្រើ ប៉ុន្តែក៏ប្រសិទ្ធភាពក្នុងការបណ្តុះបណ្តាលនិងបញ្ចូលម៉ូដែល។ ការរចនាស៊ុមដោយខ្លួនវាក៏គឺមានគំនិតត្រឹមត្រូវសាមញ្ញ ផងដែរ។ យើងមានបំណងធ្វើឱ្យងាយស្រួលសម្រាប់អ្នកស្រាវជ្រាវក្នុងការពង្រីកនិងបង្កើន MLX ដោយមានគោលដៅសម្រាប់ស្វែងយល់គំនិតថ្មីៗឆាប់រហ័ស។

LLMs អាចបង្កើនល្បឿនលើឧបករណ៍ស៊ីលីកុន Apple តាមរយៈ MLX ហើយម៉ូដែលអាចរត់ក្នុងផ្ទះបានយ៉ាងងាយស្រួល។

## **ការប្រើ MLX ក្នុងការសន្មត់ Phi-3-mini**

### **1. តំឡើងបរិបទ MLX របស់អ្នក**

1. Python 3.11.x  
2. តំឡើងបណ្ណាល័យ MLX  


```bash

pip install mlx-lm

```

### **2. ការរត់ Phi-3-mini នៅក្នុង Terminal ជាមួយ MLX**


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

លទ្ធផល (បរិបទរបស់ខ្ញុំគឺ Apple M1 Max, 64GB) គឺ

![Terminal](../../../../../translated_images/km/01.5cf57df8f7407cf9.webp)

### **3. ការបំលែងគុណភាព Phi-3-mini ជាមួយ MLX នៅក្នុង Terminal**


```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***ចំណាំ៖*** ម៉ូដែលអាចបំលែងគុណភាពតាម mlx_lm.convert ហើយការបំលែងគុណភាពលំនាំដើមគឺ INT4 ។ ឧទាហរណ៍នេះបំលែង Phi-3-mini ទៅជា INT4

ម៉ូដែលអាចបំលែងគុណភាពតាម mlx_lm.convert ហើយការបំលែងគុណភាពលំនាំដើមគឺជា INT4។ ឧទាហរណ៍នេះគឺដើម្បីបំលែង Phi-3-mini ទៅជា INT4។ បន្ទាប់ពីការបំលែងគុណភាព វានឹងត្រូវរក្សាទុកក្នុងថតលំនាំដើម ./mlx_model

យើងអាចសាកល្បងម៉ូដែលដែលបានបំលែងគុណភាពជាមួយ MLX ពី terminal បាន


```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

លទ្ធផលគឺ

![INT4](../../../../../translated_images/km/02.7b188681a8eadbc1.webp)


### **4. ការរត់ Phi-3-mini ជាមួយ MLX នៅក្នុង Jupyter Notebook**


![Notebook](../../../../../translated_images/km/03.b9705a3a5aaa89f9.webp)

***ចំណាំ៖*** សូមអានឧទាហរណ៍នេះ [ចុចតំណរនេះ](../../../code/03.Inference/MLX/MLX_DEMO.ipynb)


## **ធនធាន**

1. រៀនអំពី Apple MLX Framework [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. ផ្ទាំង GitHub របស់ Apple MLX [https://github.com/ml-explore](https://github.com/ml-explore)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការព្រមាន**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ក្នុងពេលដែលយើងព្យាយាមរកភាពជាក់លាក់ សូមយល់ថាការបកប្រែដោយម៉ាស៊ីនអាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមក្នុងភាសាម្ចាស់របស់វានឹងត្រូវបានដឹងថាជា​លទ្ធផលដ៏មានសារៈសំខាន់។ សម្រាប់ព័ត៌មានដ៏សំខាន់ ការបកប្រែដោយមនុស្សជំនាញគឺជាការផ្ដល់អនុសាសន៍។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកប្រែខុសពីការប្រើប្រាស់ការបកប្រែនេះ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->