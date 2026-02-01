# **Lora सँग Phi-3 लाई फाइन-ट्यून गर्ने तरिका**

Microsoft को Phi-3 Mini भाषा मोडेललाई [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) प्रयोग गरेर कस्टम च्याट निर्देशन डेटासेटमा फाइन-ट्यून गर्दै।

LORA ले संवाद बुझाइ र प्रतिक्रिया उत्पादन सुधार्न मद्दत गर्नेछ।

## Phi-3 Mini लाई फाइन-ट्यून गर्ने चरण-दर-चरण मार्गदर्शन:

**इम्पोर्ट र सेटअप**

loralib इन्स्टल गर्दै

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

आवश्यक लाइब्रेरीहरू जस्तै datasets, transformers, peft, trl, र torch इम्पोर्ट गरेर सुरु गर्नुहोस्।  
ट्रेनिङ प्रक्रिया ट्र्याक गर्न लगिङ सेटअप गर्नुहोस्।

तपाईंले केही लेयरहरूलाई loralib मा कार्यान्वयन गरिएका समकक्षहरूसँग प्रतिस्थापन गरेर अनुकूलन गर्न सक्नुहुन्छ। हाल हामीले nn.Linear, nn.Embedding, र nn.Conv2d मात्र समर्थन गर्छौं। साथै, हामी MergedLinear पनि समर्थन गर्छौं जुन एकल nn.Linear ले एक भन्दा बढी लेयरहरू प्रतिनिधित्व गर्ने अवस्थामा प्रयोग हुन्छ, जस्तै केही attention qkv projection को कार्यान्वयनमा (थप जानकारीका लागि Additional Notes हेर्नुहोस्)।

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

ट्रेनिङ लूप सुरु हुनु अघि, केवल LoRA प्यारामिटरहरूलाई मात्र ट्रेन योग्य (trainable) मार्क गर्नुहोस्।

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

चेकपोइन्ट सेभ गर्दा, केवल LoRA प्यारामिटरहरू समावेश गर्ने state_dict बनाउनुहोस्।

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

load_state_dict प्रयोग गरेर चेकपोइन्ट लोड गर्दा, strict=False सेट गर्न नबिर्सनुहोस्।

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

अब ट्रेनिङ सामान्य रूपमा अगाडि बढ्न सक्छ।

**हाइपरप्यारामिटरहरू**

दुई डिक्सनरीहरू परिभाषित गर्नुहोस्: training_config र peft_config।  
training_config मा ट्रेनिङका लागि हाइपरप्यारामिटरहरू समावेश हुन्छन्, जस्तै learning rate, batch size, र लगिङ सेटिङहरू।

peft_config मा LoRA सम्बन्धित प्यारामिटरहरू जस्तै rank, dropout, र task type निर्दिष्ट गरिन्छ।

**मोडेल र टोकनाइजर लोडिङ**

पूर्व-प्रशिक्षित Phi-3 मोडेलको पथ निर्दिष्ट गर्नुहोस् (जस्तै, "microsoft/Phi-3-mini-4k-instruct")। मोडेल सेटिङहरू कन्फिगर गर्नुहोस्, जसमा cache प्रयोग, डेटा प्रकार (मिश्रित प्रिसिजनका लागि bfloat16), र attention कार्यान्वयन समावेश छन्।

**ट्रेनिङ**

कस्टम च्याट निर्देशन डेटासेट प्रयोग गरेर Phi-3 मोडेललाई फाइन-ट्यून गर्नुहोस्।  
peft_config बाट LoRA सेटिङहरू प्रयोग गरी प्रभावकारी अनुकूलन गर्नुहोस्।  
ट्रेनिङ प्रगति निर्दिष्ट लगिङ रणनीतिले अनुगमन गर्नुहोस्।  
मूल्याङ्कन र सेभिङ: फाइन-ट्यून गरिएको मोडेलको मूल्याङ्कन गर्नुहोस्।  
ट्रेनिङको क्रममा चेकपोइन्टहरू सेभ गर्नुहोस् ताकि पछि प्रयोग गर्न सकियोस्।

**नमूनाहरू**  
- [यो नमूना नोटबुकसँग थप जान्नुहोस्](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Python फाइनट्यूनिङ नमूनाको उदाहरण](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [Hugging Face Hub मा LORA सँग फाइन ट्यूनिङको उदाहरण](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Hugging Face मोडेल कार्ड - LORA फाइन ट्यूनिङ नमूना](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [Hugging Face Hub मा QLORA सँग फाइन ट्यूनिङको उदाहरण](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।