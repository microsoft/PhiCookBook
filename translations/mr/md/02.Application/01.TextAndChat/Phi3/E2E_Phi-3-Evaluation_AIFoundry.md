# Microsoft Foundry मध्ये Microsoft च्या जबाबदार AI तत्त्वांवर भर देऊन फाईन-ट्यून केलेल्या Phi-3 / Phi-3.5 मॉडेलचे मूल्यमापन करा

हा एन्ड-टू-एन्ड (E2E) नमुना Microsoft Tech Community मधील "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Microsoft Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" या मार्गदर्शकावर आधारित आहे.

## आढावा

### Microsoft Foundry मध्ये फाईन-ट्यून केलेल्या Phi-3 / Phi-3.5 मॉडेलची सुरक्षितता आणि कामगिरी कशी मूल्यमापन करू शकता?

कधी कधी मॉडेलचे फाईन-ट्यूनिंग अनपेक्षित किंवा नको असलेल्या प्रतिसादांना कारणीभूत ठरू शकते. मॉडेल सुरक्षित आणि प्रभावी राहील याची खात्री करण्यासाठी, त्याच्या हानिकारक सामग्री निर्माण करण्याच्या संभाव्यतेचे आणि अचूक, संबंधित व सुसंगत प्रतिसाद तयार करण्याच्या क्षमतेचे मूल्यमापन करणे महत्त्वाचे आहे. या ट्युटोरियलमध्ये तुम्हाला Microsoft Foundry मधील Prompt flow सह एकत्रित फाईन-ट्यून केलेल्या Phi-3 / Phi-3.5 मॉडेलची सुरक्षितता आणि कामगिरी कशी मूल्यमापन करायची हे शिकता येईल.

येथे Microsoft Foundry चा मूल्यमापन प्रक्रिया आहे.

![Architecture of tutorial.](../../../../../../translated_images/mr/architecture.10bec55250f5d6a4.webp)

*प्रतिमा स्रोत: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Phi-3 / Phi-3.5 बद्दल अधिक तपशीलवार माहिती आणि अतिरिक्त साधने शोधण्यासाठी, कृपया [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723) या ठिकाणी भेट द्या.

### आवश्यकता

- [Python](https://www.python.org/downloads)
- [Azure subscription](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- फाईन-ट्यून केलेले Phi-3 / Phi-3.5 मॉडेल

### सामग्री निर्देशिका

1. [**परिस्थिती 1: Microsoft Foundry च्या Prompt flow मूल्यमापनाची ओळख**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [सुरक्षितता मूल्यांकनाची ओळख](#सुरक्षितता-मूल्यांकनाची-ओळख)
    - [कामगिरी मूल्यांकनाची ओळख](#कामगिरी-मूल्यांकनाची-ओळख)

1. [**परिस्थिती 2: Microsoft Foundry मध्ये Phi-3 / Phi-3.5 मॉडेलचे मूल्यमापन**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [आपण सुरू करण्यापूर्वी](#आपण-सुरू-करण्यापूर्वी)
    - [Phi-3 / Phi-3.5 मॉडेलचे मूल्यमापन करण्यासाठी Azure OpenAI तैनात करा](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [Microsoft Foundry च्या Prompt flow मूल्यमापनाचा वापर करून फाईन-ट्यून केलेल्या Phi-3 / Phi-3.5 मॉडेलचे मूल्यमापन करा](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [अभिनंदन!](#अभिनंदन)

## **परिस्थिती 1: Microsoft Foundry च्या Prompt flow मूल्यमापनाची ओळख**

### सुरक्षितता मूल्यांकनाची ओळख

आपल्या AI मॉडेलचे नैतिक व सुरक्षित असल्याचे सुनिश्चित करण्यासाठी, Microsoft च्या जबाबदार AI तत्त्वांविरुद्ध त्याचे मूल्यमापन करणे अत्यंत महत्त्वाचे आहे. Microsoft Foundry मध्ये सुरक्षितता मूल्यांकन आपल्याला मॉडेलच्या jailbreak हल्ल्यांबाबत असलेल्या असुरक्षिततेचे आणि हानिकारक सामग्री निर्माण करण्याच्या संभाव्यतेचे मुल्यमापन करण्याची परवानगी देते, जे थेट या तत्त्वांशी संरेखित आहे.

![Safaty evaluation.](../../../../../../translated_images/mr/safety-evaluation.083586ec88dfa950.webp)

*प्रतिमा स्रोत: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoft चे जबाबदार AI तत्त्वे

तांत्रिक टप्पे सुरू करण्यापूर्वी, Microsoft चे जबाबदार AI तत्त्वे समजून घेणे आवश्यक आहे, जे AI प्रणालींच्या जबाबदार विकास, तैनाती आणि कार्यप्रणालीसाठी एक नैतिक चौकट तयार करतात. हे तत्त्व AI तंत्रज्ञान विकसित करताना न्याय्य, पारदर्शक व सर्वसमावेशक बनवण्याचा वचनबद्धता दर्शवतात. हे तत्त्व AI मॉडेलच्या सुरक्षिततेच्या मूल्यमापनासाठी पाया म्हणून काम करतात.

Microsoft चे जबाबदार AI तत्त्वे:

- **न्याय व समावेशीपणा**: AI प्रणाली प्रत्येकाशी न्यायाने वागायला हव्यात आणि समान परिस्थितीत असलेल्या लोकांच्या गटांवर भिन्न पद्धतीने परिणाम होऊ नये. उदाहरणार्थ, जेव्हा AI प्रणाली वैद्यकीय उपचार, कर्ज अर्ज किंवा नोकरी संदर्भात मार्गदर्शन करतात, तेव्हा समान लक्षणे, आर्थिक परिस्थिती किंवा व्यावसायिक पात्रता असलेल्या प्रत्येकासाठी त्यांना समान शिफारसी द्याव्यात.

- **विश्वसनीयता व सुरक्षितता**: विश्वास निर्माण करण्यासाठी, AI प्रणाली विश्वसनीय, सुरक्षित आणि सातत्यपूर्ण चालणे अत्यावश्यक आहे. या प्रणालीने मुळात जसे डिझाइन केले गेले तसे कार्य करणे, अनपेक्षित परिस्थितींना सुरक्षित प्रतिसाद देणे, आणि हानीकारक बदलण्यापासून संरक्षण करणे आवश्यक आहे. त्यांची वागणूक आणि हाताळू शकणाऱ्या विविध परिस्थिती विकासकांनी डिझाइन आणि चाचणी दरम्यान विचारलेले विविध परिस्थिती प्रतिबिंबित करतात.

- **पारदर्शकता**: जेव्हा AI प्रणाली लोकांच्या जीवनावर मोठा परिणाम करणारे निर्णय घेण्यास मदत करतात, तेव्हा लोकांना हे समजणे आवश्यक आहे की ते निर्णय कसे घेण्यात आले. उदाहरणार्थ, एका बँकेने कर्ज देण्याचा निर्णय AI प्रणालीच्या आधारे घेतला तर. एखादी कंपनी सर्वात पात्र उमेदवारांची निवड करण्यासाठी AI प्रणाली वापरू शकते.

- **गोपनीयता व सुरक्षा**: AI अधिक व्यापक होत असल्याने, गोपनीयता संरक्षण व वैयक्तिक व व्यवसायिक माहितीची सुरक्षा अधिक महत्त्वाची आणि गुंतागुंतीची झाली आहे. AI सह, गोपनीयता व डेटा सुरक्षा याकडे विशेष लक्ष देणे गरजेचे आहे कारण डेटा प्रवेश AI प्रणालींना अचूक व माहितीपूर्ण अंदाज व निर्णय घेण्यासाठी आवश्यक आहे.

- **जबाबदारी**: AI प्रणाली डिझाइन व तैनात करणाऱ्यांनी त्यांच्या प्रणाली कशी कार्य करते यासाठी जबाबदार असावे. संस्थांनी उद्योग मानके वापरून जबाबदारीच्या नियमांची निर्मिती करावी. हे नियम सुनिश्चित करू शकतात की AI प्रणाली लोकांच्या जीवनावर परिणाम करणाऱ्या कोणत्याही निर्णयाचे अंतिम अधिकृत प्राधिकरण नसावे. ते तसेच अत्यंत स्वायत्त AI प्रणालींवर मानवी नियंत्रण कायम राहावे याची खात्री करू शकतात.

![Fill hub.](../../../../../../translated_images/mr/responsibleai2.c07ef430113fad8c.webp)

*प्रतिमा स्रोत: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Microsoft च्या जबाबदार AI तत्त्वांविषयी अधिक जाणून घेण्यासाठी, [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723) येथे भेट द्या.

#### सुरक्षितता मेट्रिक्स

या ट्युटोरियलमध्ये, आपण Microsoft Foundry च्या सुरक्षितता मेट्रिक्सचा वापर करून फाईन-ट्यून केलेल्या Phi-3 मॉडेलची सुरक्षितता मूल्यमापन कराल. हे मेट्रिक्स मॉडेलची हानिकारक सामग्री तयार करण्याची क्षमता आणि jailbreak हल्ल्यांबाबत असलेली असुरक्षितता तपासण्यासाठी मदत करतात. सुरक्षितता मेट्रिक्स मध्ये समाविष्ट आहेत:

- **स्वयं-हानिकारक संबंधित सामग्री**: मॉडेलला स्वयं-हानिकारक सामग्री निर्माण करण्याची प्रवृत्ती आहे का हे मूल्यमापन करते.
- **घृणास्पद व अन्यायकारक सामग्री**: मॉडेलला घृणास्पद किंवा अन्यायकारक सामग्री तयार करण्याची प्रवृत्ती आहे का हे मूल्यमापन करते.
- **हिंसात्मक सामग्री**: मॉडेलला हिंसात्मक सामग्री तयार करण्याची प्रवृत्ती आहे का हे मूल्यमापन करते.
- **लैंगिक सामग्री**: मॉडेलला अप्रिय लैंगिक सामग्री तयार करण्याची प्रवृत्ती आहे का हे मूल्यमापन करते.

या पैलूंवर मूल्यमापन केल्याने AI मॉडेल हानिकारक किंवा आक्षेपार्ह सामग्री तयार करू नये याची खात्री होते आणि ते सामाजिक मूल्ये आणि नियामक मानकांशी संरेखित राहते.

![Evaluate based on safety.](../../../../../../translated_images/mr/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### कामगिरी मूल्यांकनाची ओळख

आपल्या AI मॉडेलची कामगिरी अपेक्षित प्रमाणात आहे याची खात्री करण्यासाठी, त्याचे कामगिरी मेट्रिक्सच्या तुलनेत मूल्यमापन करणे महत्त्वाचे आहे. Microsoft Foundry मध्ये कामगिरी मूल्यमापन आपल्याला मॉडेलच्या अचूक, संबंधित आणि सुसंगत प्रतिसाद निर्माण करण्याच्या प्रभावकारकतेचे मूल्यमापन करण्याची परवानगी देते.

![Safaty evaluation.](../../../../../../translated_images/mr/performance-evaluation.48b3e7e01a098740.webp)

*प्रतिमा स्रोत: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### कामगिरी मेट्रिक्स

या ट्युटोरियलमध्ये, आपण Microsoft Foundry च्या कामगिरी मेट्रिक्स वापरून फाईन-ट्यून केलेल्या Phi-3 / Phi-3.5 मॉडेलची कामगिरी मूल्यमापन कराल. हे मेट्रिक्स मॉडेलच्या अचूक, संबंधित आणि सुसंगत प्रतिसाद तयार करण्याच्या प्रभावकारकतेचे मूल्यमापन करण्यात मदत करतात. कामगिरी मेट्रिक्समध्ये समाविष्ट आहेत:

- **संदर्भसमस्यता (Groundedness)**: तयार केलेले उत्तर इनपुट स्रोताच्या माहितीस कितपत सुसंगत आहे हे मूल्यमापन करा.
- **संबंधिता (Relevance)**: दिलेल्या प्रश्नांबाबत तयार केलेल्या प्रतिसादांची सुसंगतता मूल्यमापन करा.
- **सुसंगती (Coherence)**: तयार केलेली मजकूर कितपत सहजतेने वाचली जाते, नैसर्गिक वाटते आणि मानवी भाषेसारखी आहे का हे मूल्यमापन करा.
- **प्रवाहता (Fluency)**: तयार केलेल्या मजकुराची भाषिक प्रावीण्य मूल्यांकन करा.
- **GPT सारखेपणा (GPT Similarity)**: तयार केलेल्या प्रतिसादाची प्रत्यक्ष सत्याशी तुलना करा.
- **F1 गुणांक**: तयार प्रतिसाद आणि स्रोत माहितीतील सामायिक शब्दांचे प्रमाण मोजा.

हे मेट्रिक्स तुम्हाला मॉडेलची अचूक, संबंधित आणि सुसंगत प्रतिसाद तयार करण्यातील प्रभावकारकता मूल्यमापन करण्यात मदत करतात.

![Evaluate based on performance.](../../../../../../translated_images/mr/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **परिस्थिती 2: Microsoft Foundry मध्ये Phi-3 / Phi-3.5 मॉडेलचे मूल्यमापन**

### आपण सुरू करण्यापूर्वी

हा ट्युटोरियल मागील ब्लॉग पोस्टच्या पुढील भाग म्हणून आहे, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" आणि "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." या पोस्टमध्ये, आम्ही Microsoft Foundry मध्ये Phi-3 / Phi-3.5 मॉडेलचे फाईन-ट्यूनिंग आणि Prompt flow सह एकत्रीकरण कसे करायचे ते पाहिले.

या ट्युटोरियलमध्ये, आपण Microsoft Foundry मध्ये मूल्यमापक म्हणून Azure OpenAI मॉडेल तैनात कराल आणि त्याचा वापर करून आपल्या फाईन-ट्यून केलेल्या Phi-3 / Phi-3.5 मॉडेलचे मूल्यमापन कराल.

हे ट्युटोरियल सुरू करण्यापूर्वी, मागील ट्युटोरियलमध्ये वर्णन केलेल्या खालील गरजा पूर्ण आहेत याची खात्री करा:

1. फाईन-ट्यून केलेल्या Phi-3 / Phi-3.5 मॉडेलचे मूल्यमापन करण्यासाठी तयार केलेला डेटासेट.
1. फाईन-ट्यून केलेले व Azure Machine Learning मध्ये तैनात केलेले Phi-3 / Phi-3.5 मॉडेल.
1. Microsoft Foundry मधील आपल्या फाईन-ट्यून Phi-3 / Phi-3.5 मॉडेलसह एकत्रीत Prompt flow.

> [!NOTE]
> मागील ब्लॉग पोस्टमध्ये डाउनलोड केलेल्या **ULTRACHAT_200k** डेटासेटमधील data फोल्डरमध्ये असलेला *test_data.jsonl* फाइल आपण फाईन-ट्यून केलेल्या Phi-3 / Phi-3.5 मॉडेलच्या मूल्यमापनासाठी डेटासेट म्हणून वापरणार आहात.

#### Microsoft Foundry मध्ये Prompt flow सह कस्टम Phi-3 / Phi-3.5 मॉडेलचे एकत्रीकरण (प्रथम कोड दृष्टिकोन)

> [!NOTE]
> जर आपण "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)" मधील लो-कोड दृष्टिकोनाचा वापर केला असेल, तर हा अभ्यास टाळून पुढीलवर जा.
> मात्र, जर आपण "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" मध्ये वर्णन केलेल्या कोड-फर्स्ट दृष्टिकोनाने फाईन-ट्यून आणि तैनात केलेल्या Phi-3 / Phi-3.5 मॉडेलसाठी हे तुलनेने वेगळे आहे. या प्रक्रियेत आपण Prompt flow शी आपल्या मॉडेलच्या कनेक्शनचे तंत्र शिकाल.

प्रारंभ करण्यासाठी, आपल्याला Microsoft Foundry मध्ये आपल्या फाईन-ट्यून केलेल्या Phi-3 / Phi-3.5 मॉडेलला Prompt flow मध्ये एकत्रित करावे लागेल.

#### Microsoft Foundry Hub तयार करा

प्रोजेक्ट तयार करण्यापूर्वी आपल्याला Hub तयार करणे आवश्यक आहे. Hub हे संसाधन गटासारखे कार्य करते, जे आपल्याला Microsoft Foundry मध्ये अनेक प्रोजेक्ट्सचे आयोजन व व्यवस्थापन करण्यास अनुमती देते.
1. [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) मध्ये साइन इन करा.

1. डाव्या बाजूच्या टॅबमधून **All hubs** निवडा.

1. नेव्हिगेशन मेनूमधून **+ New hub** निवडा.

    ![Create hub.](../../../../../../translated_images/mr/create-hub.5be78fb1e21ffbf1.webp)

1. पुढील कामे करा:

    - **Hub name** प्रविष्ट करा. हे एक अद्वितीय मूल्य असले पाहिजे.
    - तुमचा Azure **Subscription** निवडा.
    - आवश्यक असल्यास नवीन तयार करा, वापरण्यासाठी **Resource group** निवडा.
    - तुम्हाला हवा असलेला **Location** निवडा.
    - वापरण्यासाठी **Connect Azure AI Services** निवडा (आवश्यक असल्यास नवीन तयार करा).
    - **Connect Azure AI Search** साठी **Skip connecting** निवडा.

    ![Fill hub.](../../../../../../translated_images/mr/fill-hub.baaa108495c71e34.webp)

1. **Next** निवडा.

#### Microsoft Foundry प्रोजेक्ट तयार करा

1. तुम्ही तयार केलेल्या हबस मध्ये, डाव्या बाजूच्या टॅबमधून **All projects** निवडा.

1. नेव्हिगेशन मेनूमधून **+ New project** निवडा.

    ![Select new project.](../../../../../../translated_images/mr/select-new-project.cd31c0404088d7a3.webp)

1. **Project name** प्रविष्ट करा. हे एक अद्वितीय मूल्य असले पाहिजे.

    ![Create project.](../../../../../../translated_images/mr/create-project.ca3b71298b90e420.webp)

1. **Create a project** निवडा.

#### फाइन-ट्यून केलेल्या Phi-3 / Phi-3.5 मॉडेलसाठी कस्टम कनेक्शन जोडा

तुमच्या कस्टम Phi-3 / Phi-3.5 मॉडेलला Prompt flow सह एकत्रित करण्यासाठी, तुम्हाला मॉडेलचा endpoint आणि की एका कस्टम कनेक्शनमध्ये जतन करावे लागेल. ही सेटअप Prompt flow मध्ये तुमच्या कस्टम Phi-3 / Phi-3.5 मॉडेलमध्ये प्रवेश सुनिश्चित करते.

#### फाइन-ट्यून केलेल्या Phi-3 / Phi-3.5 मॉडेलचा api key आणि endpoint uri सेट करा

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) येथे भेट द्या.

1. तुम्ही तयार केलेल्या Azure Machine learning workspace मध्ये जा.

1. डाव्या बाजूच्या टॅबमधून **Endpoints** निवडा.

    ![Select endpoints.](../../../../../../translated_images/mr/select-endpoints.ee7387ecd68bd18d.webp)

1. तुम्ही तयार केलेला endpoint निवडा.

    ![Select endpoints.](../../../../../../translated_images/mr/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. नेव्हिगेशन मेनूमधून **Consume** निवडा.

1. तुमचा **REST endpoint** आणि **Primary key** कॉपी करा.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/mr/copy-endpoint-key.0650c3786bd646ab.webp)

#### कस्टम कनेक्शन जोडा

1. [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) येथे भेट द्या.

1. तुम्ही तयार केलेल्या Microsoft Foundry प्रोजेक्टमध्ये जा.

1. तुमच्या तयार केलेल्या प्रोजेक्टमध्ये, डाव्या बाजूच्या टॅबमधून **Settings** निवडा.

1. **+ New connection** निवडा.

    ![Select new connection.](../../../../../../translated_images/mr/select-new-connection.fa0f35743758a74b.webp)

1. नेव्हिगेशन मेनूमधून **Custom keys** निवडा.

    ![Select custom keys.](../../../../../../translated_images/mr/select-custom-keys.5a3c6b25580a9b67.webp)

1. पुढील कामे करा:

    - **+ Add key value pairs** निवडा.
    - key नावासाठी, **endpoint** प्रविष्ट करा आणि Azure ML Studio मधून कॉपी केलेला endpoint value फील्डमध्ये पेस्ट करा.
    - पुन्हा **+ Add key value pairs** निवडा.
    - key नावासाठी, **key** प्रविष्ट करा आणि Azure ML Studio मधून कॉपी केलेली की value फील्डमध्ये पेस्ट करा.
    - keys जोडल्यानंतर, की उघड होऊ नये म्हणून **is secret** निवडा.

    ![Add connection.](../../../../../../translated_images/mr/add-connection.ac7f5faf8b10b0df.webp)

1. **Add connection** निवडा.

#### Prompt flow तयार करा

तुम्ही Microsoft Foundry मध्ये कस्टम कनेक्शन जोडले आहे. आता, खालील चरणांचा वापर करून Prompt flow तयार करूया. नंतर, तुम्ही हा Prompt flow कस्टम कनेक्शनशी जोडून फाइन-ट्यून केलेले मॉडेल Prompt flow मध्ये वापरू शकता.

1. तुम्ही तयार केलेल्या Microsoft Foundry प्रोजेक्टमध्ये जा.

1. डाव्या बाजूच्या टॅबमधून **Prompt flow** निवडा.

1. नेव्हिगेशन मेनूमधून **+ Create** निवडा.

    ![Select Promptflow.](../../../../../../translated_images/mr/select-promptflow.18ff2e61ab9173eb.webp)

1. नेव्हिगेशन मेनूमधून **Chat flow** निवडा.

    ![Select chat flow.](../../../../../../translated_images/mr/select-flow-type.28375125ec9996d3.webp)

1. वापरण्यासाठी **Folder name** प्रविष्ट करा.

    ![Select chat flow.](../../../../../../translated_images/mr/enter-name.02ddf8fb840ad430.webp)

1. **Create** निवडा.

#### कस्टम Phi-3 / Phi-3.5 मॉडेलशी चॅट करण्यासाठी Prompt flow सेट करा

तुम्हाला फाइन-ट्यून केलेले Phi-3 / Phi-3.5 मॉडेल Prompt flow मध्ये समाकलित करावे लागेल. तथापि, सध्याच्या उपलब्ध Prompt flow या उद्देशासाठी डिझाइन केलेले नाही. म्हणून, तुम्हाला Prompt flow पुन्हा डिझाइन करावे लागेल जेणेकरून कस्टम मॉडेलचे समाकलन शक्य होईल.

1. Prompt flow मध्ये, सध्याच्या flow चे पुनर्बांधणीसाठी खालील कामे करा:

    - **Raw file mode** निवडा.
    - *flow.dag.yml* फाईलमधील सर्व विद्यमान कोड डिलीट करा.
    - *flow.dag.yml* मध्ये पुढील कोड जोडा.

        ```yml
        inputs:
          input_data:
            type: string
            default: "Who founded Microsoft?"

        outputs:
          answer:
            type: string
            reference: ${integrate_with_promptflow.output}

        nodes:
        - name: integrate_with_promptflow
          type: python
          source:
            type: code
            path: integrate_with_promptflow.py
          inputs:
            input_data: ${inputs.input_data}
        ```

    - **Save** निवडा.

    ![Select raw file mode.](../../../../../../translated_images/mr/select-raw-file-mode.06c1eca581ce4f53.webp)

1. *integrate_with_promptflow.py* मध्ये पुढील कोड जोडा ज्यामुळे कस्टम Phi-3 / Phi-3.5 मॉडेल Prompt flow मध्ये वापरता येईल.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # लॉगिंग सेटअप
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "कनेक्शन" ही कस्टम कनेक्शनचे नाव आहे, "एंडपॉइंट", "की" हे कस्टम कनेक्शनमधील की आहेत
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    data = {
        "input_data": [input_data],
        "params": {
            "temperature": 0.7,
            "max_new_tokens": 128,
            "do_sample": True,
            "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # पूर्ण JSON प्रतिसाद लॉग करा
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Paste prompt flow code.](../../../../../../translated_images/mr/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> Microsoft Foundry मध्ये Prompt flow कसा वापरायचा याविषयी अधिक सविस्तर माहितीसाठी, तुम्ही [Microsoft Foundry मधील Prompt flow](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) पहाता येईल.

1. **Chat input**, **Chat output** निवडून तुमच्या मॉडेलशी चॅट सक्षम करा.

    ![Select Input Output.](../../../../../../translated_images/mr/select-input-output.c187fc58f25fbfc3.webp)

1. आता तुम्ही तुमच्या कस्टम Phi-3 / Phi-3.5 मॉडेलशी चॅट करण्यासाठी तयार आहात. पुढील सरावात, तुम्ही शिकाल की Prompt flow कसे सुरू करायचे आणि फाइन-ट्यून केलेल्या Phi-3 / Phi-3.5 मॉडेलशी त्याचा वापर करून चॅट कसा करायचा.

> [!NOTE]
>
> पुनर्बांधणी केलेला flow खालील चित्रासारखा दिसेल:
>
> ![Flow example](../../../../../../translated_images/mr/graph-example.82fd1bcdd3fc545b.webp)
>

#### Prompt flow सुरू करा

1. Prompt flow सुरू करण्यासाठी **Start compute sessions** निवडा.

    ![Start compute session.](../../../../../../translated_images/mr/start-compute-session.9acd8cbbd2c43df1.webp)

1. पॅरामीटर्स रिफ्रेश करण्यासाठी **Validate and parse input** निवडा.

    ![Validate input.](../../../../../../translated_images/mr/validate-input.c1adb9543c6495be.webp)

1. तुम्ही तयार केलेल्या कस्टम कनेक्शनच्या **connection** चा **Value** निवडा. उदा., *connection*.

    ![Connection.](../../../../../../translated_images/mr/select-connection.1f2b59222bcaafef.webp)

#### तुमच्या कस्टम Phi-3 / Phi-3.5 मॉडेलशी चॅट करा

1. **Chat** निवडा.

    ![Select chat.](../../../../../../translated_images/mr/select-chat.0406bd9687d0c49d.webp)

1. येथे उदाहरण स्वरूप निकाल आहे: आता तुम्ही तुमच्या कस्टम Phi-3 / Phi-3.5 मॉडेलशी चॅट करू शकता. फाइन-ट्यूनिंगसाठी वापरलेल्या डेटावर आधारित प्रश्न विचारणे शिफारसीय आहे.

    ![Chat with prompt flow.](../../../../../../translated_images/mr/chat-with-promptflow.1cf8cea112359ada.webp)

### Phi-3 / Phi-3.5 मॉडेलचे मुल्यांकन करण्यासाठी Azure OpenAI तैनात करा

Microsoft Foundry मध्ये Phi-3 / Phi-3.5 मॉडेलचे मुल्यांकन करण्यासाठी, तुम्हाला Azure OpenAI मॉडेल तैनात करावे लागेल. हे मॉडेल Phi-3 / Phi-3.5 मॉडेलच्या कार्यक्षमता मुल्यांकनासाठी वापरले जाईल.

#### Azure OpenAI तैनात करा

1. [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) मध्ये साइन इन करा.

1. तुम्ही तयार केलेल्या Microsoft Foundry प्रोजेक्टमध्ये जा.

    ![Select Project.](../../../../../../translated_images/mr/select-project-created.5221e0e403e2c9d6.webp)

1. तयार केलेल्या प्रोजेक्टमध्ये, डाव्या बाजूच्या टॅबमधून **Deployments** निवडा.

1. नेव्हिगेशन मेनूमधून **+ Deploy model** निवडा.

1. **Deploy base model** निवडा.

    ![Select Deployments.](../../../../../../translated_images/mr/deploy-openai-model.95d812346b25834b.webp)

1. वापरण्यासाठी Azure OpenAI मॉडेल निवडा. उदा., **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/mr/select-openai-model.959496d7e311546d.webp)

1. **Confirm** निवडा.

### Microsoft Foundry च्या Prompt flow मुल्यांकनाचा वापर करून फाइन-ट्यून केलेल्या Phi-3 / Phi-3.5 मॉडेलचे मुल्यांकन करा

### नवीन मुल्यांकन सुरु करा

1. [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) येथे भेट द्या.

1. तुम्ही तयार केलेल्या Microsoft Foundry प्रोजेक्टमध्ये जा.

    ![Select Project.](../../../../../../translated_images/mr/select-project-created.5221e0e403e2c9d6.webp)

1. तयार केलेल्या प्रोजेक्टमध्ये, डाव्या बाजूच्या टॅबमधून **Evaluation** निवडा.

1. नेव्हिगेशन मेनूमधून **+ New evaluation** निवडा.

    ![Select evaluation.](../../../../../../translated_images/mr/select-evaluation.2846ad7aaaca7f4f.webp)

1. **Prompt flow** evaluation निवडा.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/mr/promptflow-evaluation.cb9758cc19b4760f.webp)

1. पुढील कामे करा:

    - मुल्यांकनाचे नाव प्रविष्ट करा. हे एक अद्वितीय मूल्य असले पाहिजे.
    - कार्य प्रकार म्हणून **Question and answer without context** निवडा. कारण या ट्यूटोरियलमध्ये वापरला गेलेला **UlTRACHAT_200k** डेटासेटमध्ये संदर्भ नाही.
    - तुम्हाला मुल्यांकन करायचा असलेला prompt flow निवडा.

    ![Prompt flow evaluation.](../../../../../../translated_images/mr/evaluation-setting1.4aa08259ff7a536e.webp)

1. **Next** निवडा.

1. पुढील कामे करा:

    - **Add your dataset** निवडून तुमचा डेटासेट अपलोड करा. उदा., तुम्ही **ULTRACHAT_200k** डेटासेट डाउनलोड करताना मिळालेला *test_data.json1* टेस्टर डेटा फाइल अपलोड करू शकता.
    - तुमच्या डेटासेटशी जुळणारा योग्य **Dataset column** निवडा. उदा., जर तुम्ही **ULTRACHAT_200k** डेटासेट वापरत असाल, तर dataset column म्हणून **${data.prompt}** निवडा.

    ![Prompt flow evaluation.](../../../../../../translated_images/mr/evaluation-setting2.07036831ba58d64e.webp)

1. **Next** निवडा.

1. कार्यक्षमता आणि गुणवत्ता मेट्रिक्स कॉन्फिगर करण्यासाठी पुढील कामे करा:

    - वापरायच्या कार्यक्षमता आणि गुणवत्ता मेट्रिक्स निवडा.
    - मुल्यांकनासाठी तुम्ही तयार केलेले Azure OpenAI मॉडेल निवडा. उदा., **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/mr/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. जोखमी आणि सुरक्षा मेट्रिक्स कॉन्फिगर करण्यासाठी पुढील कामे करा:

    - वापरायचे जोखीम आणि सुरक्षा मेट्रिक्स निवडा.
    - दोष दर मोजण्यासाठी वापरायचा थ्रेशोल्ड निवडा. उदा., **Medium**.
    - **question** साठी **Data source** म्हणून **{$data.prompt}** निवडा.
    - **answer** साठी **Data source** म्हणून **{$run.outputs.answer}** निवडा.
    - **ground_truth** साठी **Data source** म्हणून **{$data.message}** निवडा.

    ![Prompt flow evaluation.](../../../../../../translated_images/mr/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. **Next** निवडा.

1. मुल्यांकन सुरू करण्यासाठी **Submit** निवडा.

1. मुल्यांकन पूर्ण होण्यासाठी काही काळ लागेल. तुम्ही प्रगती **Evaluation** टॅबमध्ये पाहू शकता.

### मुल्यांकन परिणामांचा आढावा घ्या

> [!NOTE]
> खाली दिलेले निकाल मुल्यांकन प्रक्रियेचे उदाहरण दर्शवण्यासाठी आहेत. या ट्यूटोरियलमध्ये आपण तुलनेत लहान डेटासेटवर फाइन-ट्यून केलेले मॉडेल वापरले आहे, ज्यामुळे परिणाम उपयुक्त नसेल. वापरलेल्या डेटासेटचा आकार, गुणवत्ता, विविधता तसेच मॉडेलची विशिष्ट रचना यांच्या अवलंबून प्रत्यक्ष निकालात मोठा फरक असू शकतो.

मुल्यांकन पूर्ण झाल्यानंतर, तुम्ही कार्यक्षमता आणि सुरक्षा मेट्रिक्स दोन्हीचे निकाल पाहू शकता.
1. कार्यक्षमता आणि गुणवत्ता मेट्रिक्स:

    - सुसंगत, प्रवाही आणि संबंधित प्रतिसाद निर्माण करण्यात मॉडेलची प्रभावकारिताय मूल्यांकन करा.

    ![मूल्यांकन निकाल.](../../../../../../translated_images/mr/evaluation-result-gpu.85f48b42dfb74254.webp)

1. धोका आणि सुरक्षा मेट्रिक्स:

    - मॉडेलचे उत्पादन सुरक्षित आहेत आणि जबाबदार AI तत्त्वांसह जुळतात याची खात्री करा, कोणत्याही हानिकारक किंवा अपमानास्पद सामग्री टाळा.

    ![मूल्यांकन निकाल.](../../../../../../translated_images/mr/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. **सविस्तर मेट्रिक्स निकाल** पाहण्यासाठी तुम्ही खाली स्क्रोल करू शकता.

    ![मूल्यांकन निकाल.](../../../../../../translated_images/mr/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. आपल्या सानुकूल Phi-3 / Phi-3.5 मॉडेलला कार्यक्षमता आणि सुरक्षा मेट्रिक्सच्या दोन्ही संदर्भात मूल्यांकन करून, तुम्ही पुष्टी करू शकता की मॉडेल केवळ प्रभावी नाही तर जबाबदार AI पद्धतींचे पालन करते, ज्यामुळे ते वास्तविक जगात वापरण्यास तयार आहे.

## अभिनंदन!

### तुम्ही हा प्रशिक्षणक्रम पूर्ण केला आहे

तुम्ही Microsoft Foundry मध्ये Prompt flow सह एकत्रित केलेल्या फाइन-ट्यून केलेल्या Phi-3 मॉडेलचे यशस्वीपणे मूल्यांकन केले आहे. हा तुमच्या AI मॉडेल्स केवळ चांगले काम करत नाहीत असेच नाही तर ते Microsoft च्या जबाबदार AI तत्त्वांचे पालन करतात याची खात्री करण्याचा एक महत्त्वाचा टप्पा आहे, ज्यामुळे तुम्हाला विश्वासार्ह आणि विश्वसनीय AI अनुप्रयोग तयार करता येतील.

![आकृती.](../../../../../../translated_images/mr/architecture.10bec55250f5d6a4.webp)

## Azure संसाधने साफ करा

तुमच्या खात्यावर अतिरिक्त शुल्क टाळण्यासाठी तुमची Azure संसाधने साफ करा. Azure पोर्टलवर जा आणि खालील संसाधने हटवा:

- Azure मशीन लर्निंग संसाधन.
- Azure मशीन लर्निंग मॉडेल एंडपॉइंट.
- Microsoft Foundry प्रोजेक्ट संसाधन.
- Microsoft Foundry Prompt flow संसाधन.

### पुढील टप्पे

#### दस्तऐवजीकरण

- [जबाबदार AI डॅशबोर्ड वापरून AI सिस्टमचे मूल्यांकन करा](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [जनरेटिव्ह AI साठी मूल्यांकन आणि निरीक्षण मेट्रिक्स](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Microsoft Foundry दस्तऐवज](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow दस्तऐवज](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### प्रशिक्षण सामग्री

- [Microsoft च्या जबाबदार AI दृष्टिकोनाची ओळख](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Microsoft Foundry ची ओळख](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### संदर्भ

- [जबाबदार AI काय आहे?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [अधिक सुरक्षित आणि विश्वासार्ह जनरेटिव्ह AI अनुप्रयोग तयार करण्यासाठी Azure AI मध्ये नवीन साधने जाहीर केली](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [जनरेटिव्ह AI अनुप्रयोगांचे मूल्यांकन](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात ठेवा की स्वयंचलित अनुवादांमध्ये त्रुटी किंवा अपूर्णता असू शकते. मूळ भाषा वरील दस्तऐवज अधिकृत स्रोत मानला पाहिजे. महत्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याचा सल्ला दिला जातो. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागासाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->