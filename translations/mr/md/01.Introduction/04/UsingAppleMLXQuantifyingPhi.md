<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-05-09T13:41:42+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "mr"
}
-->
# **Apple MLX Framework वापरून Phi-3.5 चे Quantizing**

MLX हा Apple सिलिकॉनवरील मशीन लर्निंग संशोधनासाठी तयार केलेला array framework आहे, जो Apple मशीन लर्निंग संशोधनाद्वारे आणला गेला आहे.

MLX मशीन लर्निंग संशोधकांसाठी मशीन लर्निंग संशोधकांनी तयार केला आहे. हा framework वापरण्यास सोपा असून तरीही मॉडेल ट्रेनिंग आणि डिप्लॉय करण्यासाठी कार्यक्षम आहे. framework चा डिझाइन संकल्पनात्मकदृष्ट्या सोपा आहे. संशोधकांना नवीन कल्पना लवकरपणे एक्सप्लोर करण्यासाठी MLX सहजपणे विस्तारण्याचा आणि सुधारण्याचा उद्देश आहे.

Apple Silicon डिव्हाइसेसवर MLX द्वारे LLMs वेगाने चालवता येतात आणि मॉडेल्स स्थानिकपणे खूप सोप्या पद्धतीने चालवता येतात.

आता Apple MLX Framework Phi-3.5-Instruct(**Apple MLX Framework support**), Phi-3.5-Vision(**MLX-VLM Framework support**), आणि Phi-3.5-MoE(**Apple MLX Framework support**) चे quantization conversion support करतो. चला पुढे प्रयत्न करूया:

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

### **🤖 Apple MLX सह Phi-3.5 साठी नमुने**

| Labs    | परिचय | सुरू करा |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Apple MLX framework सह Phi-3.5 Instruct कसा वापरायचा ते शिका   |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | Apple MLX framework वापरून Phi-3.5 Vision द्वारे प्रतिमा कशी विश्लेषित करायची ते शिका     |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Apple MLX framework सह Phi-3.5 MoE कसा वापरायचा ते शिका  |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Resources**

1. Apple MLX Framework बद्दल जाणून घ्या [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub Rep [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub Repo [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात ठेवा की स्वयंचलित अनुवादांमध्ये चुका किंवा अपूर्णता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीकरिता व्यावसायिक मानवी अनुवादाची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीसाठी आम्ही जबाबदार नाही.