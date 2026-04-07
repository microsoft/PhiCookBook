# **ការបញ្ច្រាស់កម្រិត (Quantizing) Phi-3.5 ដោយប្រើរចនាសម្ព័ន្ធ Apple MLX**


MLX គឺជារចនាសម្ព័ន្ធអារេសម្រាប់ការស្រាវជ្រាវแมชชีนឡឺនីងលើស៊ីលីកុងរបស់ Apple ដែលបានផ្តល់ដោយក្រុមស្រាវជ្រាវแมชชีนឡឺនីងរបស់ Apple។

MLX ត្រូវបានរចនាឡើងដោយអ្នកស្រាវជ្រាវแมชชีนឡឺនីង សម្រាប់អ្នកស្រាវជ្រាវแมชชีนឡឺនីង។ រចនាសម្ព័ន្ធនេះមានគោលដៅឱ្យងាយស្រួលសម្រាប់អ្នកប្រើ ប៉ុន្តែគឺមានប្រសិទ្ធភាពសម្រាប់បណ្តុះបណ្តាល និងដាក់បំពាក់ម៉ូដែល។ ការរចនារបស់រចនាសម្ព័ន្ធផ្ទាល់ខ្លួនក៏មានសេចក្តីងាយស្រួលផ្នែកខាងគ្រោងការ។ យើងមានបំណងឱ្យងាយសម្រាប់អ្នកស្រាវជ្រាវក្នុងការពង្រីក និងប្រសើរឡើង MLX ដើម្បីអាចស្វែងរកគំនិតថ្មីៗបានយ៉ាងលឿន។

LLMs អាចលឿនឡើងនៅលើឧបករណ៍ Apple Silicon តាមរយៈ MLX និងអាចរត់ម៉ូដែលនៅលើរដ្ឋកន្លែងក្នុងម៉ាស៊ីនបានយ៉ាងងាយស្រួល។

ឥឡូវនេះ រចនាសម្ព័ន្ធ Apple MLX គាំទ្រការបម្លែង quantization របស់ Phi-3.5-Instruct(**គាំទ្រដោយរចនាសម្ព័ន្ធ Apple MLX**), Phi-3.5-Vision(**គាំទ្រដោយរចនាសម្ព័ន្ធ MLX-VLM**) គាំទ្រ**), and Phi-3.5-MoE(**គាំទ្រដោយរចនាសម្ព័ន្ធ Apple MLX**). Let's try it next:

### **Phi-3.5-Instruct**


```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-mini-instruct -q

```


### **Phi-3.5-Vision**


```bash

python -m mlxv_lm.convert --hf-path microsoft/Phi-3.5-vision-instruct -q

```

### **Phi-3.5-MoE**


```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-MoE-instruct  -q

```



### **🤖 ឧទាហរណ៍សម្រាប់ Phi-3.5 ជាមួយ Apple MLX**

| មន្ទីរពិសោធន៍    | ការណែនាំ | ទៅ |
| -------- | ------- |  ------- |
| 🚀 មន្ទីរ-ណែនាំ Phi-3.5 Instruct  | រៀនពីរបៀបប្រើ Phi-3.5 Instruct ជាមួយរចនាសម្ព័ន្ធ Apple MLX   |  [ទៅ](../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 មន្ទីរ-ណែនាំ Phi-3.5 Vision (រូបភាព) | រៀនពីរបៀបប្រើ Phi-3.5 Vision ដើម្បីវិភាគរូបភាព ជាមួយរចនាសម្ព័ន្ធ Apple MLX     |  [ទៅ](../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 មន្ទីរ-ណែនាំ Phi-3.5 Vision (moE)   | រៀនពីរបៀបប្រើ Phi-3.5 MoE ជាមួយរចនាសម្ព័ន្ធ Apple MLX  |  [ទៅ](../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |


## **ធនធាន**

1. សូមស្គាល់អំពីរចនាសម្ព័ន្ធ Apple MLX [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. រ៉េបូ GitHub របស់ Apple MLX [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. រ៉េបូ GitHub សម្រាប់ MLX-VLM [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការមិនទទួលខុសត្រូវ**:
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator). ខណៈដែលយើងខិតខំសម្រាប់ភាពត្រឹមត្រូវ សូមចំណាំថាការបកប្រែដោយស្វ័យប្រវត្តិនេះអាចមានកំហុស ឬខ្វះភាពត្រឹមត្រូវ។ ឯកសារដើមនៅក្នុងភាសាដើមគួរត្រូវបានគេចាត់ទុកជាប្រភពផ្លូវការដែលមានអំណាច។ សម្រាប់ព័ត៌មានសំខាន់ៗ យើងសូមផ្តល់អនុសាសន៍ឲ្យប្រើការបកប្រែដោយមនុស្សជំនាញវិជ្ជាជីវៈ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសណាមួយដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->