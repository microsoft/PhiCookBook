<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-07-17T06:29:40+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "hi"
}
-->
# **Lora के साथ Phi-3 का फाइन-ट्यूनिंग**

Microsoft के Phi-3 Mini भाषा मॉडल को [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) का उपयोग करके एक कस्टम चैट इंस्ट्रक्शन डेटासेट पर फाइन-ट्यून करना।

LORA संवाद की समझ और प्रतिक्रिया निर्माण को बेहतर बनाने में मदद करेगा।

## Phi-3 Mini को फाइन-ट्यून करने के लिए चरण-दर-चरण मार्गदर्शिका:

**इंपोर्ट्स और सेटअप**

loralib इंस्टॉल करना

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

आवश्यक लाइब्रेरी जैसे datasets, transformers, peft, trl, और torch को इंपोर्ट करके शुरुआत करें।  
ट्रेनिंग प्रक्रिया को ट्रैक करने के लिए लॉगिंग सेटअप करें।

आप कुछ लेयर्स को loralib में उपलब्ध उनके समकक्षों से बदलकर अनुकूलित कर सकते हैं। फिलहाल हम केवल nn.Linear, nn.Embedding, और nn.Conv2d को सपोर्ट करते हैं। इसके अलावा, हम MergedLinear को भी सपोर्ट करते हैं, जो उन मामलों में उपयोग होता है जहां एक nn.Linear कई लेयर्स का प्रतिनिधित्व करता है, जैसे कि कुछ attention qkv projection के इम्प्लीमेंटेशन में (अधिक जानकारी के लिए Additional Notes देखें)।

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

ट्रेनिंग लूप शुरू होने से पहले, केवल LoRA पैरामीटर्स को ट्रेन करने योग्य मार्क करें।

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

चेकपॉइंट सेव करते समय, एक state_dict बनाएं जिसमें केवल LoRA पैरामीटर्स शामिल हों।

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

load_state_dict का उपयोग करते समय, strict=False सेट करना सुनिश्चित करें।

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

अब ट्रेनिंग सामान्य रूप से जारी रखी जा सकती है।

**हाइपरपैरामीटर्स**

दो डिक्शनरीज़ परिभाषित करें: training_config और peft_config।  
training_config में ट्रेनिंग के लिए हाइपरपैरामीटर्स होते हैं, जैसे learning rate, batch size, और लॉगिंग सेटिंग्स।

peft_config में LoRA से संबंधित पैरामीटर्स होते हैं, जैसे rank, dropout, और task type।

**मॉडल और टोकनाइज़र लोडिंग**

प्रि-ट्रेंड Phi-3 मॉडल का पाथ निर्दिष्ट करें (जैसे, "microsoft/Phi-3-mini-4k-instruct")।  
मॉडल सेटिंग्स कॉन्फ़िगर करें, जिसमें cache उपयोग, डेटा टाइप (मिश्रित प्रिसिजन के लिए bfloat16), और attention इम्प्लीमेंटेशन शामिल हैं।

**ट्रेनिंग**

कस्टम चैट इंस्ट्रक्शन डेटासेट का उपयोग करके Phi-3 मॉडल को फाइन-ट्यून करें।  
प्रभावी अनुकूलन के लिए peft_config से LoRA सेटिंग्स का उपयोग करें।  
ट्रेनिंग प्रगति को निर्दिष्ट लॉगिंग रणनीति के माध्यम से मॉनिटर करें।  
मूल्यांकन और सेविंग: फाइन-ट्यून किए गए मॉडल का मूल्यांकन करें।  
ट्रेनिंग के दौरान बाद में उपयोग के लिए चेकपॉइंट सेव करें।

**नमूने**  
- [इस सैंपल नोटबुक के साथ और जानें](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Python FineTuning सैंपल का उदाहरण](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [Hugging Face Hub पर LORA के साथ Fine Tuning का उदाहरण](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Hugging Face मॉडल कार्ड का उदाहरण - LORA Fine Tuning सैंपल](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [Hugging Face Hub पर QLORA के साथ Fine Tuning का उदाहरण](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।