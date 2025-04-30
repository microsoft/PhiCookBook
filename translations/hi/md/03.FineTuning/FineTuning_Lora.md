<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "98eb289883c5e181a74e72a59e1ddc6d",
  "translation_date": "2025-04-04T18:51:43+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Lora.md",
  "language_code": "hi"
}
-->
# **Phi-3 को Lora के साथ फाइन-ट्यून करना**

Microsoft के Phi-3 Mini भाषा मॉडल को [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) का उपयोग करके एक कस्टम चैट इंस्ट्रक्शन डेटासेट पर फाइन-ट्यून करना। 

LORA बातचीत को बेहतर समझने और उत्तर जनरेट करने में मदद करेगा। 

## Phi-3 Mini को फाइन-ट्यून करने की चरण-दर-चरण गाइड:

**इंपोर्ट्स और सेटअप** 

loralib इंस्टॉल करना

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

आवश्यक लाइब्रेरी जैसे datasets, transformers, peft, trl, और torch को इंपोर्ट करें। 
ट्रेनिंग प्रक्रिया को ट्रैक करने के लिए लॉगिंग सेट करें।

आप कुछ लेयर्स को बदलकर उन्हें loralib में लागू किए गए समकक्षों के साथ एडाप्ट कर सकते हैं। फिलहाल हम केवल nn.Linear, nn.Embedding, और nn.Conv2d को सपोर्ट करते हैं। हम MergedLinear को भी सपोर्ट करते हैं, जो उन मामलों में उपयोगी है जहां एक nn.Linear एक से अधिक लेयर्स का प्रतिनिधित्व करता है, जैसे कि ध्यान qkv प्रोजेक्शन के कुछ इम्प्लीमेंटेशन में (अधिक जानकारी के लिए अतिरिक्त नोट्स देखें)।

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

ट्रेनिंग लूप शुरू होने से पहले, केवल LoRA पैरामीटर्स को trainable के रूप में मार्क करें।

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

चेकपॉइंट सेव करते समय, एक state_dict जनरेट करें जिसमें केवल LoRA पैरामीटर्स शामिल हों।

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

load_state_dict का उपयोग करके चेकपॉइंट लोड करते समय, strict=False सेट करना सुनिश्चित करें।

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

अब ट्रेनिंग सामान्य रूप से जारी रखी जा सकती है।

**हाइपरपैरामीटर्स** 

दो डिक्शनरी परिभाषित करें: training_config और peft_config। training_config में ट्रेनिंग के लिए हाइपरपैरामीटर्स जैसे learning rate, batch size, और लॉगिंग सेटिंग्स शामिल हैं।

peft_config LoRA से संबंधित पैरामीटर्स जैसे rank, dropout, और task type को निर्दिष्ट करता है।

**मॉडल और टोकनाइज़र लोड करना** 

प्रशिक्षित Phi-3 मॉडल का पथ निर्दिष्ट करें (जैसे, "microsoft/Phi-3-mini-4k-instruct")। मॉडल सेटिंग्स को कॉन्फ़िगर करें, जिसमें कैश उपयोग, डेटा टाइप (मिश्रित प्रिसिजन के लिए bfloat16), और ध्यान कार्यान्वयन शामिल हैं।

**ट्रेनिंग** 

Phi-3 मॉडल को कस्टम चैट इंस्ट्रक्शन डेटासेट का उपयोग करके फाइन-ट्यून करें। peft_config से LoRA सेटिंग्स का उपयोग करके कुशल एडाप्टेशन सुनिश्चित करें। निर्दिष्ट लॉगिंग रणनीति का उपयोग करके ट्रेनिंग प्रगति की निगरानी करें। 
मूल्यांकन और सेविंग: फाइन-ट्यून किए गए मॉडल का मूल्यांकन करें। 
बाद में उपयोग के लिए ट्रेनिंग के दौरान चेकपॉइंट्स सेव करें।

**उदाहरण**
- [इस सैंपल नोटबुक के साथ अधिक जानें](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python फाइन-ट्यूनिंग सैंपल का उदाहरण](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub पर LoRA के साथ फाइन ट्यूनिंग का उदाहरण](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face मॉडल कार्ड - LoRA फाइन ट्यूनिंग सैंपल का उदाहरण](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [QLORA के साथ Hugging Face Hub पर फाइन ट्यूनिंग का उदाहरण](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।