<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-07-16T21:54:03+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "mr"
}
-->
# **Apple MLX Framework वापरून Phi-3.5 चे क्वांटायझेशन**

MLX हा Apple सिलिकॉनवर मशीन लर्निंग संशोधनासाठी तयार केलेला एक अ‍ॅरे फ्रेमवर्क आहे, जो Apple मशीन लर्निंग संशोधनाद्वारे सादर केला आहे.

MLX मशीन लर्निंग संशोधकांसाठी मशीन लर्निंग संशोधकांनी डिझाइन केलेला आहे. हा फ्रेमवर्क वापरण्यास सोपा असूनही मॉडेल्स ट्रेन आणि डिप्लॉय करण्यासाठी कार्यक्षम आहे. फ्रेमवर्कची रचना संकल्पनात्मकदृष्ट्या सोपी आहे. आम्ही संशोधकांना MLX सहजपणे विस्तारण्यास आणि सुधारण्यास प्रोत्साहित करतो, जेणेकरून नवीन कल्पना लवकरच तपासता येतील.

Apple सिलिकॉन डिव्हाइसेसवर MLX द्वारे LLMs जलदगतीने चालवता येतात आणि मॉडेल्स स्थानिक पातळीवर सहजपणे वापरता येतात.

आता Apple MLX Framework Phi-3.5-Instruct(**Apple MLX Framework support**), Phi-3.5-Vision(**MLX-VLM Framework support**), आणि Phi-3.5-MoE(**Apple MLX Framework support**) च्या क्वांटायझेशन रूपांतरणाला समर्थन देते. चला पुढे प्रयत्न करूया:

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

| Labs    | परिचय | जा |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Apple MLX फ्रेमवर्कसह Phi-3.5 Instruct कसे वापरायचे ते शिका   |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | Apple MLX फ्रेमवर्कसह प्रतिमा विश्लेषणासाठी Phi-3.5 Vision कसे वापरायचे ते शिका     |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Apple MLX फ्रेमवर्कसह Phi-3.5 MoE कसे वापरायचे ते शिका  |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **संसाधने**

1. Apple MLX Framework बद्दल जाणून घ्या [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub रिपॉझिटरी [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub रिपॉझिटरी [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.