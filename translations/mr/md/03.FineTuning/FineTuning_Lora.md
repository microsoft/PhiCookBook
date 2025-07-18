<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-07-17T06:30:05+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "mr"
}
-->
# **Lora सह Phi-3 चे फाइन-ट्यूनिंग**

Microsoft च्या Phi-3 Mini भाषा मॉडेलचे [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) वापरून कस्टम चॅट इन्स्ट्रक्शन डेटासेटवर फाइन-ट्यूनिंग करणे.

LORA संभाषण समज आणि प्रतिसाद निर्मिती सुधारण्यात मदत करेल.

## Phi-3 Mini चे फाइन-ट्यूनिंग कसे करावे यासाठी टप्प्याटप्प्याने मार्गदर्शक:

**इम्पोर्ट्स आणि सेटअप**

loralib इन्स्टॉल करणे

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

datasets, transformers, peft, trl, आणि torch सारख्या आवश्यक लायब्ररी इम्पोर्ट करून सुरुवात करा.
ट्रेनिंग प्रक्रियेवर लक्ष ठेवण्यासाठी लॉगिंग सेट करा.

आपण काही लेयर्सना loralib मध्ये अंमलात आणलेल्या समकक्षांद्वारे बदलून अ‍ॅडॉप्ट करू शकता. सध्या आम्ही nn.Linear, nn.Embedding, आणि nn.Conv2d यांना समर्थन देतो. काही प्रकरणांमध्ये, जसे की अटेंशन qkv प्रोजेक्शनच्या काही अंमलबजावणीत, जेथे एकाच nn.Linear मध्ये एकापेक्षा जास्त लेयर्स असतात, अशा प्रकरणांसाठी आम्ही MergedLinear देखील समर्थन करतो (अधिक माहितीसाठी Additional Notes पहा).

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

import loralib as lora

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

ट्रेनिंग लूप सुरू होण्यापूर्वी, फक्त LoRA पॅरामीटर्सना ट्रेन करण्यायोग्य म्हणून चिन्हांकित करा.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

चेकपॉइंट सेव्ह करताना, फक्त LoRA पॅरामीटर्स असलेले state_dict तयार करा.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

load_state_dict वापरताना, strict=False सेट करणे आवश्यक आहे.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

आता ट्रेनिंग सामान्यप्रमाणे सुरू करू शकता.

**हायपरपॅरामीटर्स**

training_config आणि peft_config असे दोन डिक्शनरी परिभाषित करा. training_config मध्ये ट्रेनिंगसाठी आवश्यक हायपरपॅरामीटर्स असतात, जसे की लर्निंग रेट, बॅच साईज, आणि लॉगिंग सेटिंग्ज.

peft_config मध्ये LoRA संबंधित पॅरामीटर्स जसे की rank, dropout, आणि task type दिलेले असतात.

**मॉडेल आणि टोकनायझर लोड करणे**

पूर्व-प्रशिक्षित Phi-3 मॉडेलचा पथ निर्दिष्ट करा (उदा. "microsoft/Phi-3-mini-4k-instruct"). मॉडेल सेटिंग्ज कॉन्फिगर करा, ज्यात कॅश वापर, डेटा प्रकार (मिश्रित प्रिसिजनसाठी bfloat16), आणि अटेंशन अंमलबजावणी यांचा समावेश आहे.

**ट्रेनिंग**

कस्टम चॅट इन्स्ट्रक्शन डेटासेट वापरून Phi-3 मॉडेलचे फाइन-ट्यूनिंग करा. कार्यक्षम अ‍ॅडॉप्टेशनसाठी peft_config मधील LoRA सेटिंग्ज वापरा. निर्दिष्ट लॉगिंग धोरण वापरून ट्रेनिंग प्रगतीवर लक्ष ठेवा.
मूल्यांकन आणि जतन: फाइन-ट्यून केलेल्या मॉडेलचे मूल्यांकन करा.
ट्रेनिंग दरम्यान नंतर वापरासाठी चेकपॉइंट जतन करा.

**नमुने**
- [या नमुना नोटबुकसह अधिक जाणून घ्या](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python फाइनट्यूनिंग नमुन्याचे उदाहरण](../../../../code/03.Finetuning/FineTrainingScript.py)
- [LORA सह Hugging Face Hub फाइन ट्यूनिंगचे उदाहरण](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face मॉडेल कार्डचे उदाहरण - LORA फाइन ट्यूनिंग नमुना](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [QLORA सह Hugging Face Hub फाइन ट्यूनिंगचे उदाहरण](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.