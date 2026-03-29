# Microsoft को Responsible AI सिद्धान्तहरूमा ध्यान केन्द्रित गर्दै Microsoft Foundry मा Fine-tuned Phi-3 / Phi-3.5 मोडेलको मूल्याङ्कन गर्नुहोस्

यो अन्त्य-देखि-अन्त्य (E2E) नमुना Microsoft Tech Community बाट "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Microsoft Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" मार्गनिर्देशनमा आधारित छ।

## अवलोकन

### तपाईले Microsoft Foundry मा Fine-tuned Phi-3 / Phi-3.5 मोडेलको सुरक्षा र प्रदर्शन कसरी मूल्याङ्कन गर्न सक्नुहुन्छ?

मोडेललाई फाइन-ट्युन गर्दा कहिलेकाहीं अनपेक्षित वा अवाञ्छित प्रतिक्रियाहरू आउन सक्छन्। मोडेल सुरक्षित र प्रभावकारी रहोस भन्ने सुनिश्चित गर्न, यसको हानिकारक सामग्री सिर्जना गर्ने सम्भाव्यता र सहि, प्रासंगिक, तथा सुसंगत प्रतिक्रियाहरू प्रदान गर्ने क्षमता मूल्याङ्कन गर्नु महत्त्वपूर्ण छ। यस ट्यूटोरियलमा, तपाई Microsoft Foundry मा Prompt flow सँग एकीकृत गरिएको फाइन-ट्युन गरिएको Phi-3 / Phi-3.5 मोडेलको सुरक्षा र प्रदर्शन कसरी मूल्याङ्कन गर्ने सिक्नुहुनेछ।

यहाँ Microsoft Foundry को मूल्याङ्कन प्रक्रिया छ।

![Architecture of tutorial.](../../../../../../translated_images/ne/architecture.10bec55250f5d6a4.webp)

*छवि स्रोत: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Phi-3 / Phi-3.5 सम्बन्धी थप विस्तृत जानकारीका लागि र थप स्रोतहरू अन्वेषण गर्न, कृपया [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723) मा जानुहोस्।

### आवश्यकताहरू

- [Python](https://www.python.org/downloads)
- [Azure subscription](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Fine-tuned Phi-3 / Phi-3.5 मोडेल

### विषय सूची

1. [**परिदृश्य 1: Microsoft Foundry को Prompt flow मूल्याङ्कन परिचय**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [सुरक्षा मूल्याङ्कन परिचय](#सुरक्षा-मूल्याङ्कन-परिचय)
    - [प्रदर्शन मूल्याङ्कन परिचय](#प्रदर्शन-मूल्याङ्कन-परिचय)

1. [**परिदृश्य 2: Microsoft Foundry मा Phi-3 / Phi-3.5 मोडेलको मूल्याङ्कन**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [शुरु गर्नु अघि](#सुरु-गर्नु-अघि)
    - [Phi-3 / Phi-3.5 मोडेल मूल्याङ्कनको लागि Azure OpenAI डिप्लोय गर्नुहोस्](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [Microsoft Foundry को Prompt flow मूल्याङ्कन प्रयोग गरेर फाइन-ट्युन गरिएको Phi-3 / Phi-3.5 मोडेल मूल्याङ्कन गर्नुहोस्](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [बधाई छ!](#बधाई-छ)

## **परिदृश्य 1: Microsoft Foundry को Prompt flow मूल्याङ्कन परिचय**

### सुरक्षा मूल्याङ्कन परिचय

तपाईको AI मोडेल नैतिक र सुरक्षित छ भन्ने सुनिश्चित गर्न, Microsoft को Responsible AI सिद्धान्तहरू विरुद्ध यसको मूल्याङ्कन गर्नु अत्यन्त महत्वपूर्ण छ। Microsoft Foundry मा सुरक्षा मूल्याङ्कनहरूले तपाईलाई तपाईको मोडेलको जेलब्रेक आक्रमणहरू प्रति संवेदनशीलता र हानिकारक सामग्री उत्पादन गर्ने सम्भाव्यता मूल्याङ्कन गर्न अनुमति दिन्छ, जुन यी सिद्धान्तहरूसँग प्रत्यक्ष रूपमा मेल खान्छ।

![Safaty evaluation.](../../../../../../translated_images/ne/safety-evaluation.083586ec88dfa950.webp)

*छवि स्रोत: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoft को Responsible AI सिद्धान्तहरू

प्राविधिक कदमहरू सुरु गर्नु अघि, Microsoft को Responsible AI सिद्धान्तहरू बुझ्न महत्वपूर्ण छ, जुन AI प्रणालीहरूको जिम्मेवार विकास, सञ्चालन र परिचालनलाई निर्देशन दिन डिजाइन गरिएको एक नैतिक रूपरेखा हो। यी सिद्धान्तहरूले AI प्रणालीहरूको जिम्मेवार डिजाइन, विकास र परिचालनलाई दिशानिर्देश दिन्छन्, जसले AI प्रविधिहरूलाई न्यायसंगत, पारदर्शी, र समावेशी तरिकाले निर्माण गर्न सुनिश्चित गर्दछ। यी सिद्धान्तहरूले AI मोडेलहरूको सुरक्षा मूल्याङ्कनको आधार प्रदान गर्दछन्।

Microsoft का Responsible AI सिद्धान्तहरू समावेश छन्:

- **न्याय र समावेशीपन**: AI प्रणालीहरूले सबैलाई न्यायपूर्ण व्यवहार गर्नुपर्छ र समान अवस्थाका मानिसहरूलाई फरक तरिकाले प्रभाबित गर्नेबाट जोगिनुपर्छ। जस्तै, जब AI प्रणालीहरूले चिकित्सा उपचार, ऋण आवेदन वा रोजगारमा मार्गदर्शन दिन्छन्, तब सबैलाई समान लक्षण, आर्थिक स्थिति वा पेशागत योग्यताका आधारमा समान सिफारिशहरू दिनुपर्छ।

- **विश्वसनीयता र सुरक्षा**: विश्वास निर्माण गर्नका लागि, AI प्रणालीहरू विश्वसनीय, सुरक्षित र निरन्तर रूपमा सञ्चालन हुनुपर्छ। यी प्रणालीहरूले जस्तो डिजाइन गरिएका थिए त्यसै अनुरूप काम गर्न सक्षम हुनुपर्छ, अप्रत्याशित अवस्थाहरूमा सुरक्षित प्रतिक्रिया दिन सक्नुपर्छ, र हानिकारक हेरफेरबाट बच्न सक्नुपर्छ। तिनीहरूको व्यवहार र विभिन्न अवस्थाहरूमा उनीहरूले कसरी प्रतिक्रिया दिन्छन् भन्ने कुरा विकासकर्ताहरूले डिजाइन र परीक्षण क्रममा विचार गरेका स्थिति र परिस्थितिहरूको दायरा प्रतिबिम्बित गर्दछ।

- **पारदर्शिता**: जब AI प्रणालीहरूले मानिसहरूको जीवनमा ठूलो प्रभाव पार्ने निर्णयहरूमा सहायता गर्दछन्, तब मानिसहरूले ती निर्णयहरू कसरी गरिएका हुन् बुझ्नु अत्यावश्यक हुन्छ। जस्तै, बैंकले AI प्रणाली प्रयोग गरी कसैलाई क्रेडिटयोग्य छ वा छैन निर्णय गर्न सक्छ। कम्पनीले सबैभन्दा योग्य उम्मेदवारहरू छान्न AI प्रणाली प्रयोग गर्न सक्छ।

- **गोपनीयता र सुरक्षा**: AI बढी प्रचलित हुँदा, गोपनीयता संरक्षण र व्यक्तिगत तथा व्यवसायिक जानकारीको सुरक्षा अझ महत्त्वपूर्ण र जटिल हुँदै गएको छ। AI सँग सम्बन्धित रूपमा, गोपनीयता र डाटा सुरक्षामा गहिरो ध्यान दिनुपर्छ किनभने AI प्रणालीहरूले मानिसहरूबारे सहि र सूचित पूर्वानुमान लगाउन र निर्णय लिन डाटामा पहुँच अनिवार्य छ।

- **जवाफदेहिता**: AI प्रणालीहरू डिजाइन र परिचालन गर्ने मानिसहरूले तिनीहरूको प्रणाली कसरी सञ्चालन हुन्छ त्यसका लागि जवाफदेही हुनुपर्छ। संगठनहरूले जवाफदेहिता मापदण्ड विकास गर्न उद्योग मापदण्ड प्रयोग गर्नुपर्छ। यी मापदण्डहरूले AI प्रणालीहरूलाई मानिसहरूको जीवनमा प्रभाव पार्ने कुनै निर्णयको अन्तिम अधिकार नभएको सुनिश्चित गर्न सक्छन्। साथै, यीले अत्यन्त स्वायत्त AI प्रणालीहरूमा मानिसहरूले अर्थपूर्ण नियन्त्रण कायम राख्न सकून् भनी सुनिश्चित गर्न सक्छन्।

![Fill hub.](../../../../../../translated_images/ne/responsibleai2.c07ef430113fad8c.webp)

*छवि स्रोत: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Microsoft को Responsible AI सिद्धान्तहरू बारे थप जान्नको लागि, कृपया [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723) भ्रमण गर्नुहोस्।

#### सुरक्षा मेट्रिक्सहरू

यस ट्यूटोरियलमा, तपाई Microsoft Foundry को सुरक्षा मेट्रिक्स प्रयोग गरी फाइन-ट्युन गरिएको Phi-3 मोडेलको सुरक्षा मूल्याङ्कन गर्नुहुनेछ। यी मेट्रिक्सहरूले मोडेलको हानिकारक सामग्री उत्पादन गर्ने सम्भाव्यता र जेलब्रेक आक्रमणहरू प्रति संवेदनशीलता जाँच्न मद्दत गर्छन्। सुरक्षा मेट्रिक्सहरूमा समावेश छन्:

- **आत्म-हानिसम्बन्धी सामग्री**: मोडेलमा आत्म-हानिसम्बन्धी सामग्री उत्पादन गर्ने प्रवृत्ति छ कि छैन जाँच्छ।
- **घृणास्पद र अन्यायपूर्ण सामग्री**: मोडेलमा घृणास्पद वा अन्यायपूर्ण सामग्री उत्पादन गर्ने प्रवृत्ति छ कि छैन जाँच्छ।
- **हिंसात्मक सामग्री**: मोडेलमा हिंसात्मक सामग्री उत्पादन गर्ने प्रवृत्ति छ कि छैन जाँच्छ।
- **यौन सामग्री**: मोडेलमा अनुपयुक्त यौन सामग्री उत्पादन गर्ने प्रवृत्ति छ कि छैन जाँच्छ।

यी पक्षहरूको मूल्याङ्कनले AI मोडेलले हानिकारक वा अपमानजनक सामग्री उत्पादन नगर्ने सुनिश्चित गर्दछ, जसले सामाजिक मूल्य र नियामकीय मानदण्डहरूसँग मेल खान्छ।

![Evaluate based on safety.](../../../../../../translated_images/ne/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### प्रदर्शन मूल्याङ्कन परिचय

तपाईको AI मोडेल अपेक्षित रूपमा प्रदर्शन गरिरहेको छ भन्ने सुनिश्चित गर्न, यसको प्रदर्शन मेट्रिक्सहरू विरुद्ध मूल्याङ्कन गर्नु महत्त्वपूर्ण छ। Microsoft Foundry मा प्रदर्शन मूल्याङ्कनहरूले तपाईलाई सुरक्षित, प्रासंगिक र सुसंगत प्रतिक्रियाहरू उत्पन्न गर्ने मोडेलको प्रभावकारितालाई जाँच गर्न अनुमति दिन्छ।

![Safaty evaluation.](../../../../../../translated_images/ne/performance-evaluation.48b3e7e01a098740.webp)

*छवि स्रोत: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### प्रदर्शन मेट्रिक्सहरू

यस ट्यूटोरियलमा, तपाई Microsoft Foundry को प्रदर्शन मेट्रिक्सहरू प्रयोग गरी फाइन-ट्युन गरिएको Phi-3 / Phi-3.5 मोडेलको प्रदर्शन मूल्याङ्कन गर्नुहुनेछ। यी मेट्रिक्सहरूले तपाईलाई मोडेलले सहि, प्रासंगिक र सुसंगत प्रतिक्रियाहरू उत्पन्न गर्ने क्षमतामा मूल्याङ्कन गर्न मद्दत गर्छन्। प्रदर्शन मेट्रिक्सहरूमा समावेश छन्:

- **Groundedness**: उत्पन्न उत्तरहरू इनपुट स्रोतबाट आएको जानकारीसँग कत्तिको मेल खान्छन् मूल्याङ्कन गर्नुहोस्।
- **Relevance**: दिइएका प्रश्नहरूसँग उत्पन्न प्रतिक्रियाहरू कत्तिको प्रासंगिक छन् जाँच्नुहोस्।
- **Coherence**: उत्पन्न पाठ कत्तिको सहज र प्राकृतिक रूपमा बग्छ, र मानवीय भाषा जस्तो देखिन्छ कत्तिको मूल्याङ्कन गर्नुहोस्।
- **Fluency**: उत्पन्न पाठको भाषा दक्षता मूल्याङ्कन गर्नुहोस्।
- **GPT Similarity**: उत्पन्न प्रतिक्रियालाई जरुरी वास्तविकताको सँग मेल खान्छ कि छैन तुलना गर्नुहोस्।
- **F1 Score**: उत्पन्न प्रतिक्रिया र स्रोत डेटा बीच साझा शब्दहरूको अनुपात गणना गर्नुहोस्।

यी मेट्रिक्सहरूले मोडेलको सहि, प्रासंगिक र सुसंगत प्रतिक्रियाहरू उत्पन्न गर्ने क्षमतामा मूल्याङ्कन गर्न मद्दत गर्छन्।

![Evaluate based on performance.](../../../../../../translated_images/ne/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **परिदृश्य 2: Microsoft Foundry मा Phi-3 / Phi-3.5 मोडेलको मूल्याङ्कन**

### सुरु गर्नु अघि

यो ट्यूटोरियल अघिल्लो ब्लग पोस्टहरू, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" र "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)" को अनगनिया हो। ती पोष्टहरूमा, हामीले Microsoft Foundry मा Phi-3 / Phi-3.5 मोडेललाई फाइन-ट्युन गर्ने र Prompt flow सँग एकीकृत गर्ने प्रक्रिया सिकेका थियौं।

यस ट्यूटोरियलमा, तपाई Microsoft Foundry मा एक evaluator को रूपमा Azure OpenAI मोडेल डिप्लोय गर्नुहुनेछ र यसलाई प्रयोग गरी तपाईंको फाइन-ट्युन गरिएको Phi-3 / Phi-3.5 मोडेलको मूल्याङ्कन गर्नु हुनेछ।

यस ट्यूटोरियल सुरु गर्नु अघि, कृपया अघिल्लो ट्यूटोरियलहरूमा वर्णन गरिएको निम्न आवश्यकताहरू सुनिश्चित गर्नुहोस्:

1. फाइन-ट्युन गरिएको Phi-3 / Phi-3.5 मोडेल मूल्याङ्कन गर्न तयार गरिएको डाटासेट।
1. फाइन-ट्युन गरी Azure Machine Learning मा डिप्लोय गरिएको Phi-3 / Phi-3.5 मोडेल।
1. Microsoft Foundry मा तपाईको फाइन-ट्युन गरिएको Phi-3 / Phi-3.5 मोडेलसँग एकीकृत गरिएको Prompt flow।

> [!NOTE]
> अघिल्लो ब्लग पोष्टहरूबाट डाउनलोड गरिएको **ULTRACHAT_200k** डेटासेटको data फोल्डरमा रहेको *test_data.jsonl* फाइललाई फाइन-ट्युन गरिएको Phi-3 / Phi-3.5 मोडेल मूल्याङ्कनको लागि डाटासेटको रूपमा प्रयोग गर्नुहुनेछ।

#### Microsoft Foundry मा Prompt flow सँग अनुकूल Phi-3 / Phi-3.5 मोडेल एकीकृत गर्नुहोस् (पहिले कोड विधि)

> [!NOTE]
> यदि तपाईले "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)" मा वर्णन गरिएको कम-कोड विधि अनुसरण गर्नुभएको छ भने, यो अभ्यास छोडेर अर्कोमा जान सक्नुहुन्छ। 
> तर यदि तपाईले "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" मा वर्णन गरिएको कोड-प्रथम विधि प्रयोग गरी तपाईको Phi-3 / Phi-3.5 मोडेल फाइन-ट्युन र डिप्लोय गर्नुभएको छ भने, तपाईको मोडेललाई Prompt flow सँग जडान गर्ने प्रक्रिया अलिक फरक हुन्छ। यो अभ्यासमा तपाईले यो प्रक्रिया सिक्नुहुनेछ।

अगाडि बढ्न, Microsoft Foundry मा तपाईको फाइन-ट्युन गरिएको Phi-3 / Phi-3.5 मोडेललाई Prompt flow मा एकीकृत गर्न आवश्यक छ।

#### Microsoft Foundry Hub सिर्जना गर्नुहोस्

Project सिर्जना गर्नु अघि तपाई Hub सिर्जना गर्न आवश्यक छ। Hub संसाधन समूह जस्तै काम गर्छ, जसले Microsoft Foundry भित्र विभिन्न Projects लाई व्यवस्थित र व्यवस्थापन गर्न मद्दत गर्दछ।
1. साइन इन गर्नुहोस् [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) मा।

1. बायाँपट्टि ट्याबबाट **All hubs** छान्नुहोस्।

1. नेभिगेसन मेनुबाट **+ New hub** छान्नुहोस्।

    ![Create hub.](../../../../../../translated_images/ne/create-hub.5be78fb1e21ffbf1.webp)

1. तलका कार्यहरू गर्नुहोस्:

    - **Hub name** प्रविष्ट गर्नुहोस्। यो अनौठो मान हुनुपर्छ।
    - आफ्नो Azure **Subscription** छान्नुहोस्।
    - प्रयोग गर्नको लागि **Resource group** छान्नुहोस् (आवश्यक भए नयाँ सिर्जना गर्नुहोस्)।
    - प्रयोग गर्न चाहेको **Location** छान्नुहोस्।
    - प्रयोग गर्न चाहेको **Connect Azure AI Services** छान्नुहोस् (आवश्यक भए नयाँ सिर्जना गर्नुहोस्)।
    - **Connect Azure AI Search** छान्दा **Skip connecting** चयन गर्नुहोस्।

    ![Fill hub.](../../../../../../translated_images/ne/fill-hub.baaa108495c71e34.webp)

1. **Next** चयन गर्नुहोस्।

#### Microsoft Foundry प्रोजेक्ट सिर्जना गर्नुहोस्

1. तपाईंले सिर्जना गर्नुभएको Hub मा, बायाँपट्टि ट्याबबाट **All projects** छान्नुहोस्।

1. नेभिगेसन मेनुबाट **+ New project** छान्नुहोस्।

    ![Select new project.](../../../../../../translated_images/ne/select-new-project.cd31c0404088d7a3.webp)

1. **Project name** प्रविष्ट गर्नुहोस्। यो अनौठो मान हुनुपर्छ।

    ![Create project.](../../../../../../translated_images/ne/create-project.ca3b71298b90e420.webp)

1. **Create a project** छान्नुहोस्।

#### Fine-tuned Phi-3 / Phi-3.5 मोडेलको लागि कस्टम कनेक्शन थप्नुहोस्

तपाईंको कस्टम Phi-3 / Phi-3.5 मोडेललाई Prompt flow मा समावेश गर्न, मोडेलको endpoint र key कस्टम कनेक्शनमा सुरक्षित गर्नुपर्छ। यसले Prompt flow मा तपाईंको कस्टम मोडेल पहुँच सुनिश्चित गर्छ।

#### Fine-tuned Phi-3 / Phi-3.5 मोडेलको api key र endpoint uri सेटअप गर्नुहोस्

1. जानुहोस् [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)।

1. तपाईंले सिर्जना गरेको Azure Machine Learning workspace मा नेभिगेट गर्नुहोस्।

1. बायाँपट्टि ट्याबबाट **Endpoints** छान्नुहोस्।

    ![Select endpoints.](../../../../../../translated_images/ne/select-endpoints.ee7387ecd68bd18d.webp)

1. तपाईंले सिर्जना गरेको endpoint छान्नुहोस्।

    ![Select endpoints.](../../../../../../translated_images/ne/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. नेभिगेसन मेनुबाट **Consume** छान्नुहोस्।

1. तपाईंको **REST endpoint** र **Primary key** कपी गर्नुहोस्।

    ![Copy api key and endpoint uri.](../../../../../../translated_images/ne/copy-endpoint-key.0650c3786bd646ab.webp)

#### कस्टम कनेक्शन थप्नुहोस्

1. जानुहोस् [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)।

1. तपाईंले सिर्जना गरेको Microsoft Foundry प्रोजेक्टमा नेभिगेट गर्नुहोस्।

1. तपाईंले सिर्जना गरेको प्रोजेक्टमा, बायाँपट्टि ट्याबबाट **Settings** छान्नुहोस्।

1. **+ New connection** छान्नुहोस्।

    ![Select new connection.](../../../../../../translated_images/ne/select-new-connection.fa0f35743758a74b.webp)

1. नेभिगेसन मेनुबाट **Custom keys** छान्नुहोस्।

    ![Select custom keys.](../../../../../../translated_images/ne/select-custom-keys.5a3c6b25580a9b67.webp)

1. तलका कार्यहरू गर्नुहोस्:

    - **+ Add key value pairs** छान्नुहोस्।
    - की नामका लागि **endpoint** प्रविष्ट गर्नुहोस् र Azure ML Studio बाट कपी गरेको endpoint मान मूल्य क्षेत्रमा पेस्ट गर्नुहोस्।
    - पुन: **+ Add key value pairs** छान्नुहोस्।
    - की नामका लागि **key** प्रविष्ट गर्नुहोस् र Azure ML Studio बाट कपी गरेको key मान मूल्य क्षेत्रमा पेस्ट गर्नुहोस्।
    - कुञ्जीहरू थपिसकेपछि, कुञ्जी लुकाउन **is secret** चयन गर्नुहोस्।

    ![Add connection.](../../../../../../translated_images/ne/add-connection.ac7f5faf8b10b0df.webp)

1. **Add connection** छान्नुहोस्।

#### Prompt flow सिर्जना गर्नुहोस्

तपाईंले Microsoft Foundry मा कस्टम कनेक्शन थप्नुभयो। अब, तलका चरणहरू प्रयोग गरी Prompt flow सिर्जना गर्नुहोस्। त्यसपछि, यो Prompt flow लाई कस्टम कनेक्शनसँग जडान गरेर fine-tuned मोडेल प्रयोग गर्नुहोस्।

1. तपाईंले सिर्जना गरेको Microsoft Foundry प्रोजेक्टमा नेभिगेट गर्नुहोस्।

1. बायाँपट्टि ट्याबबाट **Prompt flow** छान्नुहोस्।

1. नेभिगेसन मेनुबाट **+ Create** छान्नुहोस्।

    ![Select Promptflow.](../../../../../../translated_images/ne/select-promptflow.18ff2e61ab9173eb.webp)

1. नेभिगेसन मेनुबाट **Chat flow** छान्नुहोस्।

    ![Select chat flow.](../../../../../../translated_images/ne/select-flow-type.28375125ec9996d3.webp)

1. प्रयोग गर्न **Folder name** प्रविष्ट गर्नुहोस्।

    ![Select chat flow.](../../../../../../translated_images/ne/enter-name.02ddf8fb840ad430.webp)

1. **Create** छान्नुहोस्।

#### तपाईंको कस्टम Phi-3 / Phi-3.5 मोडेलसँग कुराकानी गर्न Prompt flow सेटअप गर्नुहोस्

तपाईंले fine-tuned Phi-3 / Phi-3.5 मोडेललाई Prompt flow मा समाहित गर्न आवश्यक छ। तर, अहिलेको उपलब्ध Prompt flow यस उद्देश्यका लागि डिजाइन गरिएको छैन। त्यसैले, तपाईंले Prompt flow पुनः डिजाइन गर्न आवश्यक छ ताकि कस्टम मोडेल समावेश गर्न सकियोस्।

1. Prompt flow मा तलका कार्यहरू गरी पुरानो flow पुनर्निर्माण गर्नुहोस्:

    - **Raw file mode** छान्नुहोस्।
    - *flow.dag.yml* फाइलमा भएको सबै कोड मेटाउनुहोस्।
    - *flow.dag.yml* मा तलको कोड थप्नुहोस्।

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

    - **Save** छान्नुहोस्।

    ![Select raw file mode.](../../../../../../translated_images/ne/select-raw-file-mode.06c1eca581ce4f53.webp)

1. आफ्नो कस्टम Phi-3 / Phi-3.5 मोडेल Prompt flow मा प्रयोग गर्न *integrate_with_promptflow.py* मा तलको कोड थप्नुहोस्।

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # लगिङ सेटअप
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

        # "connection" अनुकूल कनेक्सनको नाम हो, "endpoint", "key" अनुकूल कनेक्सनमा भएका कुञ्जीहरू हुन्
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
            
            # पूर्ण JSON प्रतिक्रिया लग गर्नुहोस्
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

    ![Paste prompt flow code.](../../../../../../translated_images/ne/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> Microsoft Foundry मा Prompt flow प्रयोग सम्बन्धी विस्तृत जानकारीको लागि तपाईं [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) सन्दर्भ गर्न सक्नुहुन्छ।

1. **Chat input**, **Chat output** छान्नुहोस् ताकि तपाईंले मोडेलसँग कुराकानी गर्न सक्नुहोस्।

    ![Select Input Output.](../../../../../../translated_images/ne/select-input-output.c187fc58f25fbfc3.webp)

1. अब तपाईं तयार हुनुहुन्छ तपाईँको कस्टम Phi-3 / Phi-3.5 मोडेलसँग कुराकानी गर्न। अर्को अभ्यासमा, तपाईं Prompt flow सुरु गर्ने र fine-tuned Phi-3 / Phi-3.5 मोडेलसँग कुराकानी गर्ने तरिका सिक्नुहुनेछ।

> [!NOTE]
>
> पुनर्निर्मित flow तलको चित्र जस्तो देखिनु पर्छ:
>
> ![Flow example](../../../../../../translated_images/ne/graph-example.82fd1bcdd3fc545b.webp)
>

#### Prompt flow सुरु गर्नुहोस्

1. Prompt flow सुरु गर्न **Start compute sessions** छान्नुहोस्।

    ![Start compute session.](../../../../../../translated_images/ne/start-compute-session.9acd8cbbd2c43df1.webp)

1. प्यारामिटरहरू नवीकरण गर्न **Validate and parse input** छान्नुहोस्।

    ![Validate input.](../../../../../../translated_images/ne/validate-input.c1adb9543c6495be.webp)

1. तपाईंले सिर्जना गरेको कस्टम कनेक्शनको **connection** को **Value** छान्नुहोस्। उदाहरणका लागि, *connection*।

    ![Connection.](../../../../../../translated_images/ne/select-connection.1f2b59222bcaafef.webp)

#### तपाईंको कस्टम Phi-3 / Phi-3.5 मोडेलसँग कुराकानी गर्नुहोस्

1. **Chat** छान्नुहोस्।

    ![Select chat.](../../../../../../translated_images/ne/select-chat.0406bd9687d0c49d.webp)

1. यहाँ नतिजाको उदाहरण छ: अब तपाईं आफ्नो कस्टम Phi-3 / Phi-3.5 मोडेलसँग कुराकानी गर्न सक्नुहुन्छ। fine-tuning को लागि प्रयोग गरिएको डाटामा आधारित प्रश्न सोध्न सुझाव दिइन्छ।

    ![Chat with prompt flow.](../../../../../../translated_images/ne/chat-with-promptflow.1cf8cea112359ada.webp)

### Phi-3 / Phi-3.5 मोडेलको मूल्याङ्कन गर्न Azure OpenAI कार्यान्वयन गर्नुहोस्

Microsoft Foundry मा Phi-3 / Phi-3.5 मोडेल मूल्याङ्कन गर्न, Azure OpenAI मोडेल कार्यान्वयन गर्नुपर्छ। यो मोडेलले Phi-3 / Phi-3.5 मोडेलको प्रदर्शन मूल्याङ्कन गर्न प्रयोग गरिनेछ।

#### Azure OpenAI कार्यान्वयन गर्नुहोस्

1. साइन इन गर्नुहोस् [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) मा।

1. तपाईंले सिर्जना गरेको Microsoft Foundry प्रोजेक्टमा नेभिगेट गर्नुहोस्।

    ![Select Project.](../../../../../../translated_images/ne/select-project-created.5221e0e403e2c9d6.webp)

1. तपाईंले सिर्जना गरेको प्रोजेक्टमा, बायाँपट्टि ट्याबबाट **Deployments** छान्नुहोस्।

1. नेभिगेसन मेनुबाट **+ Deploy model** छान्नुहोस्।

1. **Deploy base model** छान्नुहोस्।

    ![Select Deployments.](../../../../../../translated_images/ne/deploy-openai-model.95d812346b25834b.webp)

1. तपाईँले प्रयोग गर्न चाहनुभएको Azure OpenAI मोडेल छान्नुहोस्। उदाहरणका लागि, **gpt-4o**।

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/ne/select-openai-model.959496d7e311546d.webp)

1. **Confirm** छान्नुहोस्।

### Microsoft Foundry को Prompt flow मूल्याङ्कन प्रयोग गरी fine-tuned Phi-3 / Phi-3.5 मोडेल मूल्याङ्कन गर्नुहोस्

### नयाँ मूल्याङ्कन सुरु गर्नुहोस्

1. जानुहोस् [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)।

1. तपाईंले सिर्जना गरेको Microsoft Foundry प्रोजेक्टमा नेभिगेट गर्नुहोस्।

    ![Select Project.](../../../../../../translated_images/ne/select-project-created.5221e0e403e2c9d6.webp)

1. तपाईंले सिर्जना गरेको प्रोजेक्टमा, बायाँपट्टि ट्याबबाट **Evaluation** छान्नुहोस्।

1. नेभिगेसन मेनुबाट **+ New evaluation** छान्नुहोस्।

    ![Select evaluation.](../../../../../../translated_images/ne/select-evaluation.2846ad7aaaca7f4f.webp)

1. **Prompt flow** मूल्याङ्कन छान्नुहोस्।

    ![Select Prompt flow evaluation.](../../../../../../translated_images/ne/promptflow-evaluation.cb9758cc19b4760f.webp)

1. तलका कार्यहरू गर्नुहोस्:

    - मूल्याङ्कनको नाम प्रविष्ट गर्नुहोस्। यो अनौठो मान हुनुपर्छ।
    - कार्य प्रकारका रूपमा **Question and answer without context** छान्नुहोस्। किनकि यस ट्युटोरियलमा प्रयोग गरिएको **ULTRACHAT_200k** डेटासेटमा सन्दर्भ छैन।
    - मूल्याङ्कन गर्न चाहेको prompt flow छान्नुहोस्।

    ![Prompt flow evaluation.](../../../../../../translated_images/ne/evaluation-setting1.4aa08259ff7a536e.webp)

1. **Next** छान्नुहोस्।

1. तलका कार्यहरू गर्नुहोस्:

    - **Add your dataset** छानेर डेटासेट अपलोड गर्नुहोस्। उदाहरणका लागि, तपाईँ *test_data.json1* फाइल जुन **ULTRACHAT_200k** डेटासेटमा समावेश हुन्छ, अपलोड गर्न सक्नुहुन्छ।
    - तपाईंको डेटासेटसँग मेल खाने उपयुक्त **Dataset column** छान्नुहोस्। उदाहरणका लागि, यदि तपाईं **ULTRACHAT_200k** डेटासेट प्रयोग गर्दै हुनुहुन्छ भने, **${data.prompt}** चयन गर्नुहोस्।

    ![Prompt flow evaluation.](../../../../../../translated_images/ne/evaluation-setting2.07036831ba58d64e.webp)

1. **Next** छान्नुहोस्।

1. प्रदर्शन र गुणस्तर मेट्रिक्स सेटअप गर्न तलका कार्यहरू गर्नुहोस्:

    - प्रयोग गर्न चाहिएको प्रदर्शन र गुणस्तर मेट्रिक्स चयन गर्नुहोस्।
    - मूल्याङ्कनका लागि तपाईंले सिर्जना गरेको Azure OpenAI मोडेल छान्नुहोस्। उदाहरणका लागि, **gpt-4o**।

    ![Prompt flow evaluation.](../../../../../../translated_images/ne/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. जोखिम र सुरक्षा मेट्रिक्स सेटअप गर्न तलका कार्यहरू गर्नुहोस्:

    - प्रयोग गर्न चाहिने जोखिम र सुरक्षा मेट्रिक्स छान्नुहोस्।
    - दोष दर गणना गर्न प्रयोग गर्न चाहेको थ्रेसहोल्ड छान्नुहोस्। उदाहरणका लागि, **Medium**।
    - **question** का लागि, **Data source** लाई **{$data.prompt}** मा सेट गर्नुहोस्।
    - **answer** का लागि, **Data source** लाई **{$run.outputs.answer}** मा सेट गर्नुहोस्।
    - **ground_truth** का लागि, **Data source** लाई **{$data.message}** मा सेट गर्नुहोस्।

    ![Prompt flow evaluation.](../../../../../../translated_images/ne/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. **Next** छान्नुहोस्।

1. मूल्याङ्कन सुरु गर्न **Submit** छान्नुहोस्।

1. मूल्याङ्कन पूरा हुन केही समय लाग्न सक्छ। तपाईं प्रगति **Evaluation** ट्याबमा अनुगमन गर्न सक्नुहुन्छ।

### मूल्याङ्कन परिणाम समीक्षा गर्नुहोस्

> [!NOTE]
> तल दिइएको परिणामहरू मूल्याङ्कन प्रक्रियाको उदाहरणका लागि मात्र हुन्। यस ट्युटोरियलमा हामीले सानो डेटासेटमा fine-tuned गरिएको मोडेल प्रयोग गरेका छौं, जसले उपयुक्त परिणाम नआउन सक्छ। वास्तविक परिणामहरू डेटासेटको आकार, गुणस्तर, विविधता, र मोडेलको विशेष कन्फिगरेसन अनुसार फरक पर्न सक्छन्।

मूल्याङ्कन पूरा भएपछि, तपाईं प्रदर्शन र सुरक्षा मेट्रिक्स दुबैको परिणाम समीक्षा गर्न सक्नुहुन्छ।
1. प्रदर्शन र गुणस्तर मापनहरू:

    - एकअर्कासँग मेल खाने, प्रवाही, र सान्दर्भिक प्रतिक्रिया उत्पन्न गर्न मोडेलको प्रभावकारिताको मूल्याङ्कन गर्नुहोस्।

    ![Evaluation result.](../../../../../../translated_images/ne/evaluation-result-gpu.85f48b42dfb74254.webp)

1. जोखिम र सुरक्षा मापनहरू:

    - मोडेलका आउटपुटहरू सुरक्षित छन् र जिम्मेवार AI सिद्धान्तहरूसँग मेल खान्छन् भनी सुनिश्चित गर्नुहोस्, कुनै हानिकारक वा आपत्तिजनक सामग्रीबाट बच्दै।

    ![Evaluation result.](../../../../../../translated_images/ne/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. तपाईंले तल स्क्रोल गरेर **विस्तृत मापन परिणाम** हेर्न सक्नुहुन्छ।

    ![Evaluation result.](../../../../../../translated_images/ne/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. तपाइँको कस्टम Phi-3 / Phi-3.5 मोडेललाई प्रदर्शन र सुरक्षा मापन दुवैका विरुद्ध मूल्याङ्कन गरेर, तपाई मोडेल केवल प्रभावकारी मात्र नभई जिम्मेवार AI अभ्यासहरू पनि पालन गर्ने छ भनी पुष्टि गर्न सक्नुहुन्छ, जसले वास्तविक दुनियाँमा तैनाथीका लागि तयार बनाउँछ।

## बधाई छ!

### तपाईंले यो ट्युटोरियल पूरा गर्नुभयो

तपाईंले Microsoft Foundry मा Prompt flow सँग एकीकृत गरिएको फाइन-ट्यून गरिएको Phi-3 मोडेल सफलतापूर्वक मूल्याङ्कन गर्नुभएको छ। यो तपाईंका AI मोडेलहरूले राम्रो प्रदर्शन मात्र होइन, Microsoft का जिम्मेवार AI सिद्धान्तहरू पनि पालना गर्छन् भनेर सुनिश्चित गर्ने एक महत्वपूर्ण कदम हो, जसले तपाईंलाई विश्वासिलो र विश्वसनीय AI अनुप्रयोगहरू निर्माण गर्न मद्दत गर्दछ।

![Architecture.](../../../../../../translated_images/ne/architecture.10bec55250f5d6a4.webp)

## Azure स्रोतहरू सफा गर्नुहोस्

तपाईंका Azure स्रोतहरू सफा गरेर थप शुल्कबाट बच्नुहोस्। Azure पोर्टलमा जानुहोस् र निम्न स्रोतहरू मेटाउनुहोस्:

- Azure Machine learning स्रोत।
- Azure Machine learning मोडेल अन्त बिन्दु।
- Microsoft Foundry परियोजना स्रोत।
- Microsoft Foundry Prompt flow स्रोत।

### अर्को कदमहरू

#### दस्तावेजहरू

- [जिम्मेवार AI ड्यासबोर्ड प्रयोग गरेर AI प्रणालीहरू मूल्याङ्कन गर्नुहोस्](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [उत्तराधिकारिक AI का लागि मूल्याङ्कन र अनुगमन मापनहरू](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Microsoft Foundry दस्तावेजीकरण](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow दस्तावेजीकरण](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### प्रशिक्षण सामग्री

- [Microsoft को जिम्मेवार AI दृष्टिकोणमा परिचय](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Microsoft Foundry मा परिचय](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### सन्दर्भ

- [जिम्मेवार AI के हो?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Azure AI मा नयाँ उपकरणहरू घोषणा जसले तपाईंलाई बढी सुरक्षित र विश्वासिलो उत्तराधिकारिक AI अनुप्रयोगहरू निर्माण गर्न मद्दत गर्दछ](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [उत्तराधिकारिक AI अनुप्रयोगहरूको मूल्याङ्कन](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनूदित गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वतः अनुवादमा त्रुटिहरू वा गलतफहमीहरू हुन सक्छन्। मूल दस्तावेज यसको स्वदेशी भाषामा अधिकारप्राप्त स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतधारणा वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->