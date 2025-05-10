<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-05-09T20:44:12+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "mr"
}
-->
# **Lora सह Phi-3 चे फाइन-ट्यूनिंग**

Microsoft च्या Phi-3 Mini भाषा मॉडेलचे [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) वापरून कस्टम चॅट इंस्ट्रक्शन डेटासेटवर फाइन-ट्यूनिंग.

LORA संभाषण समज आणि प्रतिसाद निर्मिती सुधारण्यास मदत करेल.

## Phi-3 Mini चे फाइन-ट्यूनिंग कसे करायचे यासाठी टप्प्याटप्प्याने मार्गदर्शक:

**इम्पोर्ट्स आणि सेटअप**

loralib इन्स्टॉल करत आहे

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

datasets, transformers, peft, trl, आणि torch सारख्या आवश्यक लायब्ररी इम्पोर्ट करण्यापासून सुरुवात करा.
ट्रेनिंग प्रक्रियेवर लक्ष ठेवण्यासाठी लॉगिंग सेट करा.

काही लेयर्सना loralib मध्ये अंमलात आणलेल्या समकक्षांसह बदलून आपण त्यांना अ‍ॅडॉप्ट करू शकता. सध्या आम्ही nn.Linear, nn.Embedding, आणि nn.Conv2d यांना समर्थन देतो. काहीवेळा एखाद्या nn.Linear मध्ये एकापेक्षा जास्त लेयर्स असतात, जसे की अटेंशन qkv प्रोजेक्शनच्या काही अंमलबजावणींमध्ये (अधिक माहितीसाठी Additional Notes पहा), अशा प्रकरणांसाठी MergedLinear सुद्धा समर्थित आहे.

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

ट्रेनिंग लूप सुरू होण्यापूर्वी, फक्त LoRA पॅरामीटर्सना ट्रेन करण्यायोग्य म्हणून मार्क करा.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

चेकपॉइंट सेव्ह करताना, फक्त LoRA पॅरामीटर्स असलेला state_dict तयार करा.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

load_state_dict वापरताना, strict=False सेट करणे सुनिश्चित करा.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

आता ट्रेनिंग सामान्यप्रमाणे सुरू होऊ शकते.

**हायपरपॅरामीटर्स**

दोन डिक्शनरी define करा: training_config आणि peft_config. training_config मध्ये ट्रेनिंगसाठी हायपरपॅरामीटर्स असतात, जसे की लर्निंग रेट, बॅच साईज, आणि लॉगिंग सेटिंग्ज.

peft_config मध्ये LoRA संबंधित पॅरामीटर्स जसे की rank, dropout, आणि task type दिलेले असतात.

**मॉडेल आणि टोकनायझर लोड करणे**

प्रि-ट्रेन केलेल्या Phi-3 मॉडेलचा पाथ specify करा (उदा., "microsoft/Phi-3-mini-4k-instruct"). मॉडेल सेटिंग्ज कॉन्फिगर करा, ज्यात कॅश वापर, डेटा टाईप (मिश्रित प्रिसिजनसाठी bfloat16), आणि अटेंशन अंमलबजावणी यांचा समावेश आहे.

**ट्रेनिंग**

कस्टम चॅट इंस्ट्रक्शन डेटासेट वापरून Phi-3 मॉडेलचे फाइन-ट्यूनिंग करा. कार्यक्षम अ‍ॅडॉप्टेशनसाठी peft_config मधील LoRA सेटिंग्ज वापरा. दिलेल्या लॉगिंग स्ट्रॅटेजीने ट्रेनिंग प्रगतीवर लक्ष ठेवा.
मूल्यांकन आणि सेव्हिंग: फाइन-ट्यून केलेल्या मॉडेलचे मूल्यांकन करा.
ट्रेनिंग दरम्यान चेकपॉइंट सेव्ह करा, जे नंतर वापरता येतील.

**सॅम्पल्स**
- [या सॅम्पल नोटबुकसह अधिक शिका](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python फाइनट्यूनिंग सॅम्पलचे उदाहरण](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub वर LORA सह फाइन ट्यूनिंगचे उदाहरण](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face मॉडेल कार्डचे उदाहरण - LORA फाइन ट्यूनिंग सॅम्पल](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Hugging Face Hub वर QLORA सह फाइन ट्यूनिंगचे उदाहरण](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात ठेवा की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेत त्रुटी असू शकतात. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी अनुवादाची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.