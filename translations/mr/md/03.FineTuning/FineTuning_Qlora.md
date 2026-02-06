**QLoRA सह Phi-3 चे फाइन-ट्यूनिंग**

Microsoft च्या Phi-3 Mini भाषा मॉडेलचे फाइन-ट्यूनिंग [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora) वापरून केले जाते.

QLoRA संभाषण समज आणि प्रतिसाद निर्मिती सुधारण्यात मदत करेल.

transformers आणि bitsandbytes वापरून 4bits मध्ये मॉडेल लोड करण्यासाठी, तुम्हाला accelerate आणि transformers स्रोताकडून इन्स्टॉल करावे लागेल आणि bitsandbytes लायब्ररीची नवीनतम आवृत्ती असणे आवश्यक आहे.

**नमुने**
- [या नमुना नोटबुकसह अधिक जाणून घ्या](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python फाइनट्यूनिंग नमुन्याचे उदाहरण](../../../../code/03.Finetuning/FineTrainingScript.py)
- [LORA सह Hugging Face Hub फाइन ट्यूनिंगचे उदाहरण](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [QLORA सह Hugging Face Hub फाइन ट्यूनिंगचे उदाहरण](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.