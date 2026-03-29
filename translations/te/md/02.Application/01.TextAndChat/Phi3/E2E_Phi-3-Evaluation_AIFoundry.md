# Microsoft Foundryలో Microsoft యొక్క బాధ్యతాయుత AI స 원ాలు పై దృష్టి సారించి ఫైన్-ట్యూన్ చేసిన Phi-3 / Phi-3.5 మోడల్‌ను మదింపు చేయండి

ఈ ఎండ్-టూ-ఎండ్ (E2E) నమూనా Microsoft Tech Community నుండి గైడ్ "[Microsoft Foundryలో Microsoft యొక్క బాధ్యతాయుత AI పై దృష్టి సారించి ఫైన్-ట్యూన్ చేసిన Phi-3 / 3.5 మోడల్స్‌ను మదింపు చేయండి](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" ఆధారంగా ఉంది.

## అవలోకనం

### Microsoft Foundryలో ఫైన్-ట్యూన్ చేసిన Phi-3 / Phi-3.5 మోడల్ యొక్క భద్రత మరియు పనితీరును ఎలా మదింపు చేసుకోవచ్చు?

మోడల్‌ను ఫైన్-ట్యూనింగ్ చేయడము కొన్నిసార్లు అనుకోని లేదా ఆకాంక్షించని ప్రతిస్పందనలకు దారితీస్తుంది. మోడల్ భద్రతతో పాటు సమర్థవంతంగా పనిచేస్తున్నదని నిర్ధారించడానికి, హానికరమైన కంటెంట్ను ఉత్పత్తి చేసే అవకాశం మరియు ఖచ్చితమైన, సంబంధిత, సమగ్ర ప్రతిస్పందనలు ఇవ్వగల సామర్థ్యాన్ని మదింపు చేయడం ముఖ్యము. ఈ పాఠంలో, Microsoft Foundryలో Prompt flowతో సమగ్రంగా కూడిన ఫైన్-ట్యూన్ చేసిన Phi-3 / Phi-3.5 మోడల్ యొక్క భద్రత మరియు పనితీరును ఎలా మదింపు చేసుకోవాలో మీరు నేర్చుకుంటారు.

ఇది Microsoft Foundry యొక్క మదింపు ప్రక్రియ.

![Architecture of tutorial.](../../../../../../translated_images/te/architecture.10bec55250f5d6a4.webp)

*చిత్ర మూలం: [సృష్టించే AI అప్లికేషన్ల మదింపు](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Phi-3 / Phi-3.5 సూచించిన మరిన్ని వివరాలకు మరియు అదనపు వనరులు తెలుసుకోవడానికి, దయచేసి [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723) ను సందర్శించండి.

### ముందస్తు ఇవంచనలు

- [Python](https://www.python.org/downloads)
- [Azure సభ్యత్వం](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- ఫైన్-ట్యూన్ చేసిన Phi-3 / Phi-3.5 మోడల్

### సూచిక

1. [**సన్నివేశం 1: Microsoft Foundry యొక్క Prompt flow మదింపు పరిచయం**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [భద్రతా మదింపుకు పరిచయం](#భద్రతా-మదింపుకు-పరిచయం)
    - [పనితీరు మదింపుకు పరిచయం](#పనితీరును-మదింపు-చేయడానికి-పరిచయం)

1. [**సన్నివేశం 2: Microsoft Foundryలో Phi-3 / Phi-3.5 మోడల్ మదింపు**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [మొదట మీరు చేయాల్సింది](#మొదలు-పెట్టేముందు)
    - [Phi-3 / Phi-3.5 మోడల్‌ను మదింపు చేయడానికి Azure OpenAIను నియోజకవర్గం చేయండి](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [Microsoft Foundry యొక్క Prompt flow మదింపు ఉపయోగించి ఫైన్-ట్యూన్ చేసిన Phi-3 / Phi-3.5 మోడల్‌ను మదింపు చేయండి](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [అభినందనలు!](#అభినందనలు)

## **సన్నివేశం 1: Microsoft Foundry యొక్క Prompt flow మదింపు పరిచయం**

### భద్రతా మదింపుకు పరిచయం

మీ AI మోడల్ నైతికమైనది మరియు భద్రతారహితమైనదని నిర్ధారించడానికి, Microsoft యొక్క బాధ్యతాయుత AI స 원ాలు ఆధారంగా దీన్ని మదింపు చేయడం చాలా ముఖ్యం. Microsoft Foundryలో భద్రతా మదింపులు మీ మోడల్‌కి jailbreak దాడులకు అద్భుతమైన సంభావ్యత ఉన్నదా లేదా హానికరమైన కంటెంట్ ఉత్పత్తి చేసే అవకాశం ఉందా అన్న దాన్ని అంచనా వేయడానికి అనుమతిస్తాయి, ఇది ఈ స 원ాలతో నేరుగా అనుసంధానంగా ఉంటాయి.

![Safaty evaluation.](../../../../../../translated_images/te/safety-evaluation.083586ec88dfa950.webp)

*చిత్ర మూలం: [సృష్టించే AI అప్లికేషన్ల మదింపు](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoft యొక్క బాధ్యతాయుత AI స 원ాలు

సాంకేతిక దశలను ప్రారంభించే ముందు, Microsoft యొక్క బాధ్యతాయుత AI స 원ాలు గురించి అర్థం చేసుకోవడం అత్యవసరం. ఇవి AI సిస్టమ్‌ల బాధ్యతాపూర్వక అభివృద్ధి, వినియోగం మరియు ఆపరేషన్‌ను మార్గనిర్దేశం చేసే నైతిక ఫ్రేమ్‌వర్క్. ఈ స 원ాలు AI టెక్నాలజీలను న్యాయమైన, పారదర్శకమైన మరియు సమగ్రత కలిగిన విధంగా తయారు చేయాలని నిర్ధారిస్తాయి. ఇవే AI మోడల్స్ భద్రతా మదింపులకు ఆదారం.

Microsoft బాధ్యతాయుత AI స 원ాలు:

- **న్యాయం మరియు సమగ్రత:** AI సిస్టమ్‌లు అందరికీ సమానంగా నివేదించాలి మరియు సారూప్యమైన పరిస్థితులలో ఉన్న గ్రూపులపై వేరు విధంగా ప్రవర్తించడం తప్పించాలి. ఉదాహరణకు, AI సిస్టమ్‌లు వైద్య చికిత్స, రుణ దరఖాస్తులు, లేదా ఉద్యోగ సిఫారసుల విషయంలో సమాన లక్షణాలు లేదా అర్హతలు ఉన్న వారికి సమాన సిఫారసులు ఇవ్వాలి.

- **నమ్మకం మరియు భద్రత:** నమ్మకం ఏర్పరచడానికి, AI సిస్టమ్‌లు నమ్మకంగా, భద్రతగా, స్థిరంగా పని చేయాలి. అవి అసలు రూపకల్పన ప్రకారంగా పనిచేయడం, అప్రత్యాశిత పరిస్థితులకు భద్రతగా స్పందించడం మరియు హానికరమైన మార్పులకు ప్రతిఘటించడం వీలవ్వాలి. అవి ఎలా ప్రవర్తిస్తాయో మరియు ఎలా పరిస్థితులను నిర్వహిస్తాయో అవసరమైన వేరియేషన్లు డిజైన్, పరీక్షలో అంచనా వేయబడతాయి.

- **పారదర్శకత:** AI సిస్టమ్‌లు ప్రజల జీవితాలపై తీవ్ర ప్రభావం చూపే నిర్ణయాలకు సహాయం చేస్తే, ఆ నిర్ణయాలు ఎలా తీసుకోవడమైందో ప్రజలు అర్థం చేసుకోవడం చాలా ముఖ్యము. ఉదాహరణకు, ఓ బ్యాంకు రుణయోగ్యత నిర్ణయించడానికి AI ఉపయోగిస్తే లేదా కంపెనీ ఉత్తమ అభ్యర్థులను నియమించడానికి AI ఉపయోగిస్తే.

- **గోప్యత మరియు భద్రత:** AI విస్తృతంగా ఉపయోగించినప్పుడు, వ్యక్తిగత మరియు వ్యాపార సమాచార గోప్యత మరియు భద్రత ముఖ్యంగా మరియు సంక్లిష్టంగా మారిపోతుంది. AIకు చెందిన డేటాకు యాక్సెస్ అవసరం కావడంతో, గోప్యత మరియు డేటా భద్రత పై శ్రద్ధ మరింత అవసరం.

- **వప్పనివ్వకత:** AI సిస్టమ్‌లను రూపకల్పన చేసే మరియు ఉపయోగించే వ్యక్తులు అందించిన విధంగా వాటి కార్యకలాపాలకి బాధ్యత వహించాలి. సంస్థలు పరిశ్రమ ప్రమాణాల ఆధారంగా బాధ్యతా నియమాలు రూపొందించాలి. వీటివల్ల AI సిస్టమ్‌లు చరిత్రలో చివరి అధికారిగా నిలుచుకోవకుండా మరియు మానవులు సాంకేతిక వ్యాసంగం ఉన్న AIపై అర్థవంతమైన నియంత్రణ కలిగి ఉండేలా నిర్ధారించవచ్చు.

![Fill hub.](../../../../../../translated_images/te/responsibleai2.c07ef430113fad8c.webp)

*చిత్ర మూలం: [బాధ్యతాయుత AI అంటే ఏమిటి?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Microsoft యొక్క బాధ్యతాయుత AI స 원ాలు గురించి మరింత తెలుసుకోవడానికి, [బాధ్యతాయుత AI అంటే ఏమిటి?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723) ను సందర్శించండి.

#### భద్రతా ప్రమాణాలు

ఈ పాఠంలో, మీరు Microsoft Foundry యొక్క భద్రతా ప్రమాణాలను ఉపయోగించి ఫైన్-ట్యూన్ చేసిన Phi-3 మోడల్ యొక్క భద్రతను మదింపు చేస్తారు. ఈ ప్రమాణాలు మోడల్ హానికరమైన కంటెంట్ తయారుచేసే అవకాశాన్ని మరియు jailbreak దాడులకు సున్నితత్వాన్ని అంచనా వేయడానికి సహాయపడతాయి. భద్రతా ప్రమాణాలు:

- **ఆత్మ-హాని సంబంధిత కంటెంట్**: మోడల్ ఆత్మ-హాని సంబంధిత కంటెంట్ ఉత్పత్తికి దూరంగా ఉందా అన్నది అంచనా వేస్తుంది.
- **ద్వేష మరియు అన్యాయ కంటెంట్**: మోడల్ ద్వేషపూరిత లేదా అన్యాయ కంటెంట్ ఉత్పత్తి చేసే అవకాశం ఉందా అన్నది అంచనా వేస్తుంది.
- **హింసాత్మక కంటెంట్**: మోడల్ హింసాత్మక కంటెంట్ ఉత్పత్తి చేసే అవకాశాన్ని అంచనా వేస్తుంది.
- **లైంగిక కంటెంట్**: మోడల్ అణవంటి లైంగిక కంటెంట్ ఉత్పత్తి చేసే అవకాశం ఉందా అన్నది అంచనా వేస్తుంది.

ఈ అంశాలను మదింపు చేయడం వలన AI మోడల్ హానికర లేదా దోషపూరిత కంటెంట్ ఇవ్వకుండా ఉన్నదని, సామాజిక విలువలు మరియు నియంత్రణ ప్రమాణాలతో సరిపోలుతుందని నిర్ధారించవచ్చు.

![Evaluate based on safety.](../../../../../../translated_images/te/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### పనితీరును మదింపు చేయడానికి పరిచయం

మీ AI మోడల్ ఆగకుండా పనితీరు అందించడం కోసం, దాన్ని పనితీరు ప్రమాణాలతో మదింపు చేయడం ముఖ్యం. Microsoft Foundryలో, పనితీరు మదింపు మీ మోడల్ ఖచ్చితమైన, సంబంధిత మరియు సమగ్ర ప్రతిస్పందనలు ఉత్పత్తి చేయడంలో సమర్థమై ఉందా అన్నది అంచనా వేయడానికి అనుమతిస్తుంది.

![Safaty evaluation.](../../../../../../translated_images/te/performance-evaluation.48b3e7e01a098740.webp)

*చిత్ర మూలం: [సృష్టించే AI అప్లికేషన్ల మదింపు](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### పనితీరు ప్రమాణాలు

ఈ పాఠంలో, మీరు Microsoft Foundry యొక్క పనితీరు ప్రమాణాలను ఉపయోగించి ఫైన్-ట్యూన్ చేసిన Phi-3 / Phi-3.5 మోడల్ పనితీరును మదింపు చేయబోతున్నారు. ఈ ప్రమాణాలు ఖచ్చితమైన, సంబంధిత మరియు సమగ్ర ప్రతిస్పందనలు ఉత్పత్తి చేయడంలో మోడల్ సమర్థతను అంచనా వేయడానికి సహాయపడతాయి. పనితీరు ప్రమాణాలు:

- **ఆధారపడటం (Groundedness)**: ఉత్పత్తి చేయబడిన సమాధానాలు ఇన్పుట్ మూల సమాచారం తగినట్లు సరిపోతాయా అని అంచనా వేయండి.
- **సంబంధితత (Relevance)**: ఇచ్చిన ప్రశ్నలకు ఉత్పత్తి చేయబడిన ప్రతిస్పందనలు ఎంత వరకూ సంభందిస్తున్నారు అని అంచనా వేయండి.
- **సమ్మేళనం (Coherence)**: ఉత్పత్తి చేయబడిన టెక్స్ సజావుగా, సహజంగా చదవబడి, మానవ భాషలా ఉందా అన్నది అంచనా వేయండి.
- **ప్రవాహం (Fluency)**: ఉత్పత్తి టెక్స్ భాషా నైపుణ్యం ఎలా ఉందో అంచనా వేయండి.
- **GPT సారూప్యత (GPT Similarity)**: ఉత్పత్తి సమాధానాన్ని భూయ తీవ్రతతో పోల్చడం ద్వారా సమానత అంచనా వేయండి.
- **F1 స్కోరు**: ఉత్పత్తి సమాధానము మరియు మూల డేటా మధ్య పంచుకున్న పదాల అనుపాతం లెక్కించడం.

ఈ ప్రమాణాలు మోడల్ ఖచ్చితమైన, సంబంధిత, సమగ్ర ప్రతిస్పందనలు ఇవ్వడంలో ఎంత సమర్థమో అంచనా వేయడానికి సహాయపడతాయి.

![Evaluate based on performance.](../../../../../../translated_images/te/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **సన్నివేశం 2: Microsoft Foundryలో Phi-3 / Phi-3.5 మోడల్ మదింపు**

### మొదలు పెట్టేముందు

ఈ పాఠం పూర్వపు బ్లాగ్ పోస్టులు "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" మరియు "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)"కు అనుసంధానంగా ఉంటుంది. ఆ పోస్టుల్లో, Microsoft Foundryలో Phi-3 / Phi-3.5 మోడల్‌ను ఫైన్-ట్యూన్ చేసి Prompt flowతో ఏకీకృతం చేసే ప్రక్రియను మేము చూశాము.

ఈ పాఠంలో, మీరు Microsoft Foundryలో Azure OpenAI మోడల్‌ను మదింపు యంత్రంగా నియೋಜించి, దానితో మీ ఫైన్-ట్యూన్ చేసిన Phi-3 / Phi-3.5 మోడల్‌ను మదింపు చేస్తారు.

ఈ పాఠం మొదలు పెట్టేముందు, క్రింద పేర్కొన్న ముందస్తు అవసరాలు ఉన్నాయని నిర్ధారించుకోండి, ఇవి పూర్వపు పాఠాల వివరణల్లో చెప్పబడ్డవి:

1. ఫైన్-ట్యూన్ చేసిన Phi-3 / Phi-3.5 మోడల్‌ను మదింపు చేసుకునేందుకు సిద్ధమైన డేటా సెట్.
1. ఫైన్-ట్యూన్ చేసి Azure Machine Learningకు విస్తరించిన Phi-3 / Phi-3.5 మోడల్.
1. Microsoft Foundryలో మీ ఫైన్-ట్యూన్ చేసిన Phi-3 / Phi-3.5 మోడల్‌తో ఏకీకృతమైన Prompt flow.

> [!NOTE]
> మీరు పూర్వపు బ్లాగ్ పోస్టులలో డౌన్‌లోడ్ చేసిన **ULTRACHAT_200k** డేటా ఫోల్‌డర్‌లో ఉన్న *test_data.jsonl* ఫైల్‌ను ఫైన్-ట్యూన్ చేసిన Phi-3 / Phi-3.5 మోడల్‌ను మదింపు చేయడానికి ఉపయోగిస్తారు.

#### Microsoft Foundryలో Prompt flowతో కస్టమ్ Phi-3 / Phi-3.5 మోడల్ ఏకీకరణ (మొదటి కోడ్ దృష్టాంతం)

> [!NOTE]
> మీరు "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)" లో చెప్పిన తక్కువ-కోడ్ దృష్టాంతాన్ని అనుసరిస్తే, ఈ వ్యాయామాన్ని వదలివేయి మరియు తదుపరి దశకు ముందడుగు వేస్తే సరిపోతుంది.
> అయినప్పటికీ, మీరు "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" లో చెప్పిన కోడ్-ముందుగా విధానాన్ని అనుసరించి Phi-3 / Phi-3.5 మోడల్‌ను ఫైన్-ట్యూన్ చేసి విస్తరించినట్లయితే, Prompt flowకు మీ మోడల్‌ను కనెక్ట్ చేసే ప్రక్రియ కొంత భిన్నంగా ఉంటుంది. ఈ వ్యాయామంలో మీరు ఆ విధానాన్ని నేర్చుకుంటారు.

ముందుకు సాగేందుకు, Microsoft Foundryలో Prompt flowలో మీ ఫైన్-ట్యూన్ చేసిన Phi-3 / Phi-3.5 మోడల్‌ను ఏకీకృతం చేయాల్సి ఉంటుంది.

#### Microsoft Foundry హబ్ సృష్టించండి

ప్రాజెక్ట్ సృష్టించేముందు హబ్‌ను సృష్టించాలి. హబ్ ఒక రిసోర్స్ గ్రూప్ లాగా నిర్వహణా భాగస్వామ్యాన్ని అందిస్తుంది, దీని ద్వారా Microsoft Foundryలో అనేక ప్రాజెక్టులను సమగ్రముగా నిర్వహించవచ్చు.
1. [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) లో సైన్ ఇన్ చేయండి.

1. ఎడమ వైపు ట్యాబ్ నుండి **అన్ని హబ్లు** ఎంచుకోండి.

1. నావిగేషన్ మెనూ నుండి **+ కొత్త హబ్** ఎంచుకోండి.

    ![Create hub.](../../../../../../translated_images/te/create-hub.5be78fb1e21ffbf1.webp)

1. క్రింది పనులు చేయండి:

    - **హబ్ పేరు**ను నమోదు చేయండి. అది ప్రత్యేకమైన విలువగా ఉండాలి.
    - మీ Azure **సబ్‌స్క్రిప్షన్** ఎంచుకోండి.
    - ఉపయోగించడానికి **రిసోర్స్ గ్రూప్** ఎంచుకోండి (అవసరం అయితే కొత్తదాన్ని సృష్టించండి).
    - మీరు ఉపయోగించదలచిన **ఉపాకరణం** ఎంచుకోండి.
    - ఉపయోగించడానికి **Azure AI సర్వీసులను కनेक్ట్ చేయండి** ఎంచుకోండి (అవసరం అయితే కొత్తదాన్ని సృష్టించండి).
    - **Azure AI సెర్చ్ కनेक్ట్ చేయండి** చే **స్కిప్ కనెక్టింగ్** ఎంచుకోండి.

    ![Fill hub.](../../../../../../translated_images/te/fill-hub.baaa108495c71e34.webp)

1. **తరువాత** ఎంచుకోండి.

#### Microsoft Foundry ప్రాజెక్ట్ సృష్టించండి

1. మీరు సృష్టించిన హబ్‌లో, ఎడమ వైపు ట్యాబ్ నుండి **అన్ని ప్రాజెక్టులు** ఎంచుకోండి.

1. నావిగేషన్ మెనూ నుండి **+ కొత్త ప్రాజెక్ట్** ఎంచుకోండి.

    ![Select new project.](../../../../../../translated_images/te/select-new-project.cd31c0404088d7a3.webp)

1. **ప్రాజెక్ట్ పేరు**ను ఎంటర్ చేయండి. ఇది ప్రత్యేకమైన విలువ కావాలి.

    ![Create project.](../../../../../../translated_images/te/create-project.ca3b71298b90e420.webp)

1. **ప్రాజెక్ట్ సృష్టించండి** ఎంచుకోండి.

#### ఫైన్-ట్యూన్ చేసిన Phi-3 / Phi-3.5 మోడల్ కోసం కస్టమ్ కనెక్షన్ జత చేయండి

మీ కస్టమ్ Phi-3 / Phi-3.5 మోడల్‌ను Prompt flow తో అనుసంధానం చేయడానికి, మోడల్ యొక్క ఎండ్‌పాయింట్ మరియు కీని కస్టమ్ కనెక్షన్‌లో సేవ్ చేయాలి. ఈ సెటప్ Prompt flow లో మీ కస్టమ్ Phi-3 / Phi-3.5 మోడల్‌కు ప్రాప్యం నిర్ధారిస్తుంది.

#### ఫైన్-ట్యూన్ చేసిన Phi-3 / Phi-3.5 మోడల్ యొక్క api కీ మరియు endpoint uri సెటప్ చేయండి

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) సందర్శించండి.

1. మీరు సృష్టించిన Azure మెషీన్ లెర్నింగ్ వర్క్‌స్పేస్‌కు వెళ్లండి.

1. ఎడమ వైపు ట్యాబ్ నుండి **ఎండ్‌పాయింట్‌లు** ఎంచుకోండి.

    ![Select endpoints.](../../../../../../translated_images/te/select-endpoints.ee7387ecd68bd18d.webp)

1. మీరు సృష్టించిన ఎండ్‌పాయింట్ ఎంచుకోండి.

    ![Select endpoints.](../../../../../../translated_images/te/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. నావిగేషన్ మెనూ నుండి **కన్స్యూమ్** ఎంచుకోండి.

1. మీ **REST ఎండ్‌పాయింట్** మరియు **ప్రైమరీ కీ**ని కాపీ చేయండి.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/te/copy-endpoint-key.0650c3786bd646ab.webp)

#### కస్టమ్ కనెక్షన్ జత చేయండి

1. [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) కి వెళ్లండి.

1. మీరు సృష్టించిన Microsoft Foundry ప్రాజెక్ట్‌కు వెళ్లండి.

1. మీరు సృష్టించిన ప్రాజెక్టులో, ఎడమ వైపు ట్యాబ్ నుండి **సెట్టింగ్స్** ఎంచుకోండి.

1. **+ కొత్త కనెక్షన్** ఎంచుకోండి.

    ![Select new connection.](../../../../../../translated_images/te/select-new-connection.fa0f35743758a74b.webp)

1. నావిగేషన్ మెనూ నుండి **కస్టమ్ కీలు** ఎంచుకోండి.

    ![Select custom keys.](../../../../../../translated_images/te/select-custom-keys.5a3c6b25580a9b67.webp)

1. క్రింది పనులు చేయండి:

    - **+ కీ విలువ జోడించండి** ఎంచుకోండి.
    - కీ పేరుగా **endpoint** ఎంటర్ చేసి Azure ML Studio నుండి కాపీ చేసిన ఎండ్‌పాయింట్‌ను విలువ ఫీల్డ్‌లో పేస్టు చేయండి.
    - మళ్ళీ **+ కీ విలువ జోడించండి** ఎంచుకోండి.
    - కీ పేరుగాను **key** ఎంటర్ చేసి Azure ML Studio నుండి కాపీ చేసిన కీని విలువ ఫీల్డ్‌లో పేస్టు చేయండి.
    - కీలు జోడించిన తరువాత, కీ ఎక్స్‌పోజ్ కాకుండా **is secret** ఎంచుకోండి.

    ![Add connection.](../../../../../../translated_images/te/add-connection.ac7f5faf8b10b0df.webp)

1. **Add connection** ఎంచుకోండి.

#### Prompt flow సృష్టించండి

మీరు Microsoft Foundryలో కస్టమ్ కనెక్షన్ జతచేశారు. ఇప్పుడు, క్రింది దశలను ఉపయోగించి ఒక Prompt flow సృష్టిద్దాం. తరువాత ఈ Prompt flow ను కస్టమ్ కనెక్షన్‌కు కనెక్ట్ చేసి ఫైన్-ట్యూన్ చేయబడిన మోడల్‌ను Prompt flow లో ఉపయోగించవచ్చు.

1. మీరు సృష్టించిన Microsoft Foundry ప్రాజెక్ట్‌కు వెళ్లండి.

1. ఎడమ వైపు ట్యాబ్ నుండి **Prompt flow** ఎంచుకోండి.

1. నావిగేషన్ మెనూ నుండి **+ సృష్టించండి** ఎంచుకోండి.

    ![Select Promptflow.](../../../../../../translated_images/te/select-promptflow.18ff2e61ab9173eb.webp)

1. నావిగేషన్ మెనూ నుండి **చాట్ ఫ్లో** ఎంచుకోండి.

    ![Select chat flow.](../../../../../../translated_images/te/select-flow-type.28375125ec9996d3.webp)

1. ఉపయోగించవలసిన **ఫోల్డర్ పేరు** ఎంటర్ చేయండి.

    ![Select chat flow.](../../../../../../translated_images/te/enter-name.02ddf8fb840ad430.webp)

1. **సృష్టించండి** ఎంచుకోండి.

#### Prompt flow ను మీ కస్టమ్ Phi-3 / Phi-3.5 మోడల్‌తో చాట్ చేయడానికి సెటప్ చేయండి

ఫైన్-ట్యూన్ చేసిన Phi-3 / Phi-3.5 మోడల్‌ను Prompt flow లో సమగ్రపరచాలి. కానీ ప్రస్తుత Prompt flow దీనికి తగిన విధంగా రూపొందించబడలేదు. అందుకే, ఈ Prompt flow ను తిరిగి డిజైన్ చేసి కస్టమ్ మోడల్ ఇంటిగ్రేషన్‌కు అనుకూలంగా మార్చాలి.

1. Prompt flow లో క్రింది పనులు చేయండి:

    - **Raw file mode** ఎంచుకోండి.
    - *flow.dag.yml* ఫైల్‌లో ఉన్న అన్ని కోడ్ తీసివేయండి.
    - *flow.dag.yml* లో క్రింది కోడ్ జోడించండి.

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

    - **Save** ఎంచుకోండి.

    ![Select raw file mode.](../../../../../../translated_images/te/select-raw-file-mode.06c1eca581ce4f53.webp)

1. Prompt flow లో మీ కస్టమ్ Phi-3 / Phi-3.5 మోడల్ ఉపయోగించడానికి *integrate_with_promptflow.py* లో క్రింది కోడ్ జోడించండి.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # లాగింగు సెటప్
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

        # "connection" అనేది కస్టమ్ కనెక్షన్ పేరు, "endpoint", "key" అనేవి కస్టమ్ కనెక్షన్‌లో కీలు
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
            
            # పూర్తి JSON ప్రతిస్పందనను లాగ్ చేయండి
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

    ![Paste prompt flow code.](../../../../../../translated_images/te/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> Microsoft Foundryలో Prompt flow ఉపయోగించడానికి మరిన్ని వివరాలకు మీరు [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) చూడవచ్చు.

1. మీ మోడల్‌తో చాట్ చేయడానికి **Chat input**, **Chat output** ఎంచుకోండి.

    ![Select Input Output.](../../../../../../translated_images/te/select-input-output.c187fc58f25fbfc3.webp)

1. ఇప్పుడు మీరు మీ కస్టమ్ Phi-3 / Phi-3.5 మోడల్‌తో చాట్ చేయడానికి సిద్ధంగా ఉన్నారు. తరువాతి వ్యాయామంలో మీరు Prompt flow ఎలా ప్రారంభించి, దానిలో మీ ఫైన్-ట్యూన్ చేసిన Phi-3 / Phi-3.5 మోడల్‌తో ఎలా చాట్ చేయాలో నేర్చుకోబడుతుంది.

> [!NOTE]
>
> తిరిగి నిర్మించిన ఫ్లో క్రింది చిత్రం లాగే ఉండాలి:
>
> ![Flow example](../../../../../../translated_images/te/graph-example.82fd1bcdd3fc545b.webp)
>

#### Prompt flow ప్రారంభించండి

1. Prompt flow ప్రారంభించడానికి **Start compute sessions** ఎంచుకోండి.

    ![Start compute session.](../../../../../../translated_images/te/start-compute-session.9acd8cbbd2c43df1.webp)

1. పారామీటర్లను నవీకరించడానికి **Validate and parse input** ఎంచుకోండి.

    ![Validate input.](../../../../../../translated_images/te/validate-input.c1adb9543c6495be.webp)

1. మీరు సృష్టించిన కస్టమ్ కనెక్షన్ **connection** యొక్క **Value** ని ఎంచుకోండి.

    ![Connection.](../../../../../../translated_images/te/select-connection.1f2b59222bcaafef.webp)

#### మీ కస్టమ్ Phi-3 / Phi-3.5 మోడల్‌తో చాట్ చేయండి

1. **Chat** ఎంచుకోండి.

    ![Select chat.](../../../../../../translated_images/te/select-chat.0406bd9687d0c49d.webp)

1. ఫలితాల ఉదాహరణ ఇక్కడ ఉంది: ఇప్పుడు మీరు మీ కస్టమ్ Phi-3 / Phi-3.5 మోడల్‌తో చాట్ చేయవచ్చు. ఫైన్-ట్యూన్‌కి ఉపయోగించిన డేటాకు సంబంధించిన ప్రశ్నలు అడగడం సూచించబడుతుంది.

    ![Chat with prompt flow.](../../../../../../translated_images/te/chat-with-promptflow.1cf8cea112359ada.webp)

### Phi-3 / Phi-3.5 మోడల్‌ను అంచనా వేయడానికి Azure OpenAIని డిప్లాయ్ చేయండి

Microsoft Foundryలో Phi-3 / Phi-3.5 మోడల్‌ను అంచనా వేయడానికి, మీరు Azure OpenAI మోడల్‌ను డిప్లాయ్ చేయాలి. ఈ మోడల్ Phi-3 / Phi-3.5 యొక్క ప్రదర్శనను అంచనా వేయడానికి ఉపయోగించబడుతుంది.

#### Azure OpenAI డిప్లాయ్ చేయండి

1. [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) లో సైన్ ఇన్ అయ్యండి.

1. మీరు సృష్టించిన Microsoft Foundry ప్రాజెక్ట్‌కు వెళ్లండి.

    ![Select Project.](../../../../../../translated_images/te/select-project-created.5221e0e403e2c9d6.webp)

1. మీరు సృష్టించిన ప్రాజెక్టులో, ఎడమ వైపు ట్యాబ్ నుండి **Deployments** ఎంచుకోండి.

1. నావిగేషన్ మెనూ నుండి **+ Deploy model** ఎంచుకోండి.

1. **Deploy base model** ఎంచుకోండి.

    ![Select Deployments.](../../../../../../translated_images/te/deploy-openai-model.95d812346b25834b.webp)

1. మీరు ఉపయోగించదలచిన Azure OpenAI మోడల్ ఎంచుకోండి. ఉదాహరణకు, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/te/select-openai-model.959496d7e311546d.webp)

1. **Confirm** ఎంచుకోండి.

### Microsoft Foundry యొక్క Prompt flow అంచనా ఉపయోగించి ఫైన్-ట్యూన్ చేసిన Phi-3 / Phi-3.5 మోడల్‌ను అంచనా వేశారు

### కొత్త అంచనా ప్రారంభించండి

1. [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) కు వెళ్లండి.

1. మీరు సృష్టించిన Microsoft Foundry ప్రాజెక్ట్‌కు వెళ్లండి.

    ![Select Project.](../../../../../../translated_images/te/select-project-created.5221e0e403e2c9d6.webp)

1. మీరు సృష్టించిన ప్రాజెక్టులో, ఎడమ వైపు ట్యాబ్ నుండి **Evaluation** ఎంచుకోండి.

1. నావిగేషన్ మెనూ నుండి **+ New evaluation** ఎంచుకోండి.

    ![Select evaluation.](../../../../../../translated_images/te/select-evaluation.2846ad7aaaca7f4f.webp)

1. **Prompt flow** అంచనా ఎంచుకోండి.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/te/promptflow-evaluation.cb9758cc19b4760f.webp)

1. క్రింది పనులు చేయండి:

    - అంచనా పేరును నమోదు చేయండి. అది ప్రత్యేకమైన విలువ కావాలి.
    - టాస్క్ తరం గా **సందర్భంలేని ప్రశ్న మరియు జవాబు** ఎంచుకోండి. ఎందుకంటే, ఈ ట్యుటోరియల్‌లో ఉపయోగించిన **UltraChat_200k** డేటాసెట్‌లో సందర్భం లేదు.
    - మీరు అంచనా వేయదలచిన prompt flow ఎంచుకోండి.

    ![Prompt flow evaluation.](../../../../../../translated_images/te/evaluation-setting1.4aa08259ff7a536e.webp)

1. **తరువాత** ఎంచుకోండి.

1. క్రింది పనులు చేయండి:

    - డేటాసెట్ అప్లోడ్ చేయడానికి **మీ డేటాసెట్ జోడించండి** ఎంచుకోండి. ఉదాహరణకు, **ULTRACHAT_200k** డాటాసెట్ డౌన్లోడ్ చేసినప్పుడు ఉండే *test_data.json1* అనే టెస్ట్ డేటాసెట్ ఫైల్ అప్లోడ్ చేయవచ్చు.
    - మీ డేటాసెట్‌కు సరిపోయే **డేటాసెట్ కాలమ్** ఎంచుకోండి. ఉదాహరణకు, **ULTRACHAT_200k** డేటాసెట్ వుంటే **${data.prompt}** డేటాసెట్ కాలమ్ ఎంచుకోండి.

    ![Prompt flow evaluation.](../../../../../../translated_images/te/evaluation-setting2.07036831ba58d64e.webp)

1. **తరువాత** ఎంచుకోండి.

1. ప్రదర్శన మరియు నాణ్యత మాపకాలను సెటప్ చేయండి:

    - మీరు ఉపయోగించదలచిన ప్రదర్శన మరియు నాణ్యత మాపకాలు ఎంచుకోండి.
    - అంచనా కోసం మీరు సృష్టించిన Azure OpenAI మోడల్ ఎంచుకోండి. ఉదాహరణకు, **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/te/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. ప్రమాదం మరియు సురక్షితత మాపకాలను సెటప్ చేయండి:

    - మీరు ఉపయోగించదలచిన ప్రమాదం మరియు సురక్షితత మాపకాలు ఎంచుకోండి.
    - దోష రేటును అంచనా వేయడానికి మీరు ఉపయోగించదలచిన థ్రెషోల్డ్ ఎంచుకోండి. ఉదాహరణకు, **మధ్యస్థం (Medium)**.
    - **question**కి, **డేటా సోర్స్** గా **{$data.prompt}** ఎంచుకోండి.
    - **answer**కి, **డేటా సోర్స్** గా **{$run.outputs.answer}** ఎంచుకోండి.
    - **ground_truth**కి, **డేటా సోర్స్** గా **{$data.message}** ఎంచుకోండి.

    ![Prompt flow evaluation.](../../../../../../translated_images/te/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. **తరువాత** ఎంచుకోండి.

1. అంచనా ప్రారంభించడానికి **Submit** ఎంచుకోండి.

1. అంచనా పూర్తయ్యే వరకు కొంత సమయం తీసుకుంటుంది. మీరు **Evaluation** ట్యాబ్‌లో ప్రగతిని పర్యవేక్షించవచ్చు.

### అంచనా ఫలితాలను సమీక్షించండి

> [!NOTE]
> క్రింద ఇచ్చిన ఫలితాలు అంచనా ప్రక్రియను వివరించడానికి మాత్రమే ఉద్దేశించబడ్డాయి. ఈ ట్యుటోరియల్‌లో, తక్కువ పరిమాణంలో డేటాసెట్‌తో ఫైన్-ట్యూన్ చేసిన మోడల్ ఉపయోగించాం, అందువల్ల ఫలితాలు కొన్ని చోట్ల తక్కువగా ఉండవచ్చును. వాస్తవ ఫలితాలు డేటాసెట్ పరిమాణం, నాణ్యత, వైవిధ్యం మరియు మోడల్ యొక్క ప్రత్యేక సెటప్ ఆధారంగా చాలా భిన్నంగా ఉండవచ్చు.

అంచనా పూర్తైన తరువాత, మీరు ప్రదర్శన మరియు సురక్షితత మాపకాల ఫలితాలను సమీక్షించవచ్చు.
1. ప్రదర్శన మరియు నాణ్యత ప్రమాణాలు:

    - సుసంబద్ధమైన, సరళమైన, మరియు సంబంధిత స్పందనలను ఉత్పత్తి చేయడంలో మోడల్ యొక్క సమర్థతను అంచనా వేయండి.

    ![వ interioresం ఫలితం.](../../../../../../translated_images/te/evaluation-result-gpu.85f48b42dfb74254.webp)

1. రిస్క్ మరియు సురక్షా ప్రమాణాలు:

    - మోడల్ యొక్క అవుట్‌పుట్లు సురక్షితం మరియు బాధ్యతాయుత AI సూత్రాలతో అనుగుణంగా ఉండేలా చూసుకోండి, ఏవైనా హానికరమైన లేదా అపుడుగోపిం అంశాలు దూరంగా ఉండండి.

    ![వ interioresం ఫలితం.](../../../../../../translated_images/te/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. మీరు క్రింద స్ర్కోల్ చేసి **వివరిచిన ప్రమాణాల ఫలితాన్ని** చూడవచ్చు.

    ![వ interioresం ఫలితం.](../../../../../../translated_images/te/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. పనితీరు మరియు సురక్షా ప్రమాణాల రెండింటినీ మీ కస్టమ్ Phi-3 / Phi-3.5 మోడల్‌తో అంచనా వేశారు అంటే, ఆ మోడల్ సమర్థవంతంగా మాత్రమే కాకుండా బాధ్యతాయుత AI ఆచారాలకు కూడా అనుగుణంగా ఉందని నిర్ధారించవచ్చు, ఇది వాస్తవ ప్రపంచంలో వినియోగానికి సన్నద్ధంగా ఉండేలా చేస్తుంది.

## అభినందనలు!

### మీరు ఈ పాఠ్యक्रमాన్ని పూర్తిచేసుకున్నారు

Microsoft Foundryలో Prompt flowతో అనుసంధానించిన ఫైన్-ట్యూన్ చేసిన Phi-3 మోడల్‌ను మీరు విజయవంతంగా అంచనా వేశారు. ఇది మీ AI నమూనాలు బాగా పనితీరం చేయడమే కాకుండా Microsoft's బాధ్యతాయుత AI సూత్రాలు పాటిస్తూ నమ్మదగిన, విశ్వసనీయ AI అప్లికేషన్లు రూపొందించడంలో సహాయపడుతాయని నిర్ధారించే ఒక ముఖ్యమైన దశ.

![ఆర్కిటెక్చర్.](../../../../../../translated_images/te/architecture.10bec55250f5d6a4.webp)

## Azure వనరులను శుభ్రపరుచుకోండి

మీ అకౌంట్‌కు అదనపు ఛార్జీల నుండి తప్పించుకునేందుకు Azure వనరులను శుభ్రపరుచుకోండి. Azure పోర్టల్‌కు వెళ్లి క్రింది వనరులను తొలగించండి:

- Azure మెషీన్ లెర్నింగ్ వనరు.
- Azure మెషీన్ లెర్నింగ్ మోడల్ ఎండ్పాయింట్.
- Microsoft Foundry ప్రాజెక్ట్ వనరు.
- Microsoft Foundry Prompt flow వనరు.

### తదుపరి దశలు

#### డాక్యుమెంటేషన్

- [బాధ్యతాయుత AI డాష్‌బోర్డ్ను ఉపయోగించి AI సిస్టమ్లను అంచనా వేయండి](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [సృష్టింప జెనరేటివ్ AI కొరకు అంచనా మరియు మానిటరింగ్ ప్రమాణాలు](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Microsoft Foundry డాక్యుమెంటేషన్](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow డాక్యుమెంటేషన్](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### శిక్షణా విషయాలు

- [Microsoft యొక్క బాధ్యతాయుత AI దృష్టికోణం పరిచయం](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Microsoft Foundry పరిచయం](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### సూచనలు

- [బాధ్యతాయుత AI అంటే ఏమిటి?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [మీరు మరింత సురక్షితమైన మరియు నమ్మదగిన జెనరేటివ్ AI అప్లికేషన్‌లు రూపొందించేందుకు Azure AIలో కొత్త టూల్స్ ప్రకటించడం](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [జెనరేటివ్ AI అప్లికేషన్ల అంచనా](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**నివేదిక**:  
ఈ డాక్యుమెంట్‌ను ఏఐ అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము సరిగ్గా ఉండేందుకు ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాలలో పొరపాట్లు లేదా లోపాలు ఉండవచ్చు. మౌలిక భాషలో ఉన్న అసలు డాక్యుమెంట్‌ను అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారంకోసం, ప్రొఫెషనల్ మానవ అనువాదం సూచించబడుతుంది. ఈ అనువాదం ఉపయోగించడం ద్వారా వచ్చే ఏవైనా అపార్థాలు లేదా తప్పుగా అర్థం చేసుకోవడంపై మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->