# Microsoft Foundry తో Phi-3 ను ఫైట్-ట్యూన్ చేయడం

మైక్రోసాఫ్ట్ యొక్క Phi-3 మినీ భాషా మోడల్‌ను Microsoft Foundry ఉపయోగించి ఎలా ఫైన్-ట్యూన్ చేయాలో ఈ అంశంలో తెలుసుకుందాం. ఫైన్-ట్యూనింగ్ ద్వారా Phi-3 మినీని నిర్దిష్ట పనులకికి అనుకూలపరచవచ్చు, దీనివల్ల అది మరింత శక్తివంతంగా, సందర్భాన్ని అవగాహన చేసుకునేలా మారుతుంది.

## 농ి확ణలు

- **సామర్థ్యాలు:** ఏ మోడల్స్‌ను ఫైన్-ట్యూన్ చేయవచ్చు? బేస్ మోడల్‌ను ఏ పనులకు ఫైన్-ట్యూన్ చేయవచ్చు?
- **ఖర్చు:** ఫైన్-ట్యూనింగ్ కొరకు ధర సరళి ఏంటి?
**అనుకూలీకరణ:** బేస్ మోడల్‌ను ఎంత వరకు మరియు ఎలాంటి మార్పులు చేయగలను?
- **సౌలభ్యం:** ఫైన్-ట్యూనింగ్ ఎలా జరుగుతుంది - నేను ప్రత్యేక కోడ్ రాయాల్సి ఉన్నదా? నేను నా యంత్ర శక్తిని తీసుకొస్తానా?
- **భద్రత:** ఫైన్-ట్యూన్ చేసిన మోడల్స్ భద్రతా సమస్యలు కలిగించే అవకాశాలు ఉంటాయి - ప్రమాదాలను నివారించేందుకు అటువంటి రక్షణ చర్యలు ఉన్నాయా?

![AIFoundry Models](../../../../translated_images/te/AIFoundryModels.0e1b16f7d0b09b73.webp)

## ఫైన్-ట్యూనింగ్ కోసమైన సన్నాహాలు

### ముందస్తు అవసరాలు

> [!NOTE]
> Phi-3 కుటుంబంలోని మోడల్స్ కొరకు, pay-as-you-go ఫైన్-ట్యూన్ ఆఫరింగ్ కేవలం **East US 2** ప్రాంతాలలో సృష్టించబడిన hub లకు మాత్రమే అందుబాటులో ఉంది.

- ఒక Azure సబ్‌స్క్రిప్షన్. Azure సబ్‌స్క్రిప్షన్ వీలులో లేకపోతే, [paid Azure ఖాతా](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) సృష్టించుకోండి.

- ఒక [AI Foundry ప్రాజెక్ట్](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- Microsoft Foundry లో ఆపరేషన్లు అందజేసేందుకు Azure ఆధారిత అనుమతులు (Azure RBAC) ఉపయోగిస్తారు. ఈ ఆర్టికిల్‌లో చెప్పిన దశలను కొనసాగించేందుకు, మీ యూజర్ ఖాతాకు __Azure AI Developer role__ రీసోర్స్ గ్రూప్ లో కేటాయించాలి.

### సబ్‌స్క్రిప్షన్ ప్రొవైడర్ నమోదు

సబ్‌స్క్రిప్షన్ `Microsoft.Network` రిసోర్స్ ప్రొవైడర్‌కు నమోదు చేయబడిందో లేదో పరిశీలించండి.

1. [Azure పోర్టల్](https://portal.azure.com) లో సైన్ ఇన్ అవ్వండి.
1. ఎడమ మెనూలోనుంచి **Subscriptions** ఎంచుకోండి.
1. ఉపయోగించాల్సిన సబ్‌స్క్రిప్షన్ ను ఎంచుకోండి.
1. ఎడమ మెనూలోని **AI project settings** > **Resource providers** ఎంచుకోండి.
1. **Microsoft.Network** రిసోర్స్ ప్రొవైడర్ల జాబితాలో ఉందో తనిఖీ చేయండి. లేకపోతే జోడించండి.

### డేటా సన్నాహాలు

మీ మోడల్‌ను ఫైన్-ట్యూన్ చేయడానికి మీ శిక్షణ మరియు ధృవీకరణ డేటాను సిద్దం చేసుకోండి. శిక్షణ మరియు ధృవీకరణ డేటాకు మోడల్ ఎలా స్పందించాలో వెల్లడించే ఇన్‌పుట్ మరియు ఔట్‌పుట్ ఉదాహరణలు ఉంటాయి.

మీ శిక్షణ ఉదాహరణలు అందరి అంచనాల మేరకు సరైన ఫార్మాట్‌లో ఉండాలంటే శ్రద్ధ వహించండి. ఫైన్-ట్యూనింగ్ సమర్ధవంతంగా జరిగేందుకు, సమతుల్యమైన, విభిన్నమైన డేటా సెట్ ఉండటం అవసరం.

ఇది డేటా సమతుల్యతను ఉరుంచి, వివిధ పరిస్థితులను చేర్చడం ద్వారా, మరియు ప్రతి సమయంలో రెగ్యులర్ గా ఉపయోగకరమైన శిక్షణ డేటాను మెరుగుపరచడం ద్వారా వాస్తవ ప్రపంచ అంచనాలకు అనుగుణంగా మోడల్ రెస్పాన్స్ లు మెరుగవుతాయి.

వేరే వేరే మోడల్ రకాలకు వేరే వేరే శిక్షణ డేటా ఫార్మాట్ అవసరం.

### చాట్ కంప్లీషన్

మీరు ఉపయోగించే శిక్షణ మరియు ధృవీకరణ డేటా తప్పకుండా JSON Lines (JSONL) ఫార్మాట్‌లో ఉండాలి. `Phi-3-mini-128k-instruct` కోసం ఫైన్-ట్యూన్ డేటాసెట్ చాట్ కంప్లీషన్స్ API ఉపయోగించే సంభాషణ ఫార్మాట్‌లో ఉండాలి.

### ఉదాహరణ ఫైల్ ఫార్మాట్

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```
  
ఆఫర్ కావలసిన ఫైల్ రకం JSON Lines. ఫైళ్ళను డిఫాల్ట్ డేటా స్టోరులో అప్లోడ్ చేసి, ప్రాజెక్ట్‌లో అందుబాటులో ఉంచుతారు.

## Microsoft Foundryతో Phi-3 ను ఫైన్-ట్యూన్ చేయడం

Microsoft Foundry మీరు మీ వ్యక్తిగత డేటాసెట్లకు పెద్ద భాషా మోడల్స్‌ను ఫైన్-ట్యూన్ చేసుకోవడానికి ఒక ప్రక్రియను అందిస్తుంది. ఫైన్-ట్యూనింగ్ ప్రత్యేక పనుల కోసం అనుకూలీకరణ మరియు ఉత్తమీకరణకు సహాయపడుతూ, మెరుగైన పనితీరు, ఖర్చు తగ్గింపు, తక్కువ సమయ వ్యయం, మరియు వ్యక్తిగత అవుట్పుట్లను సాధించేందుకు ఉపయోగపడుతుంది.

![Finetune AI Foundry](../../../../translated_images/te/AIFoundryfinetune.193aaddce48d553c.webp)

### కొత్త ప్రాజెక్ట్ సృష్టించడం

1. [Microsoft Foundry](https://ai.azure.com) లో సైన్ ఇన్ అవ్వండి.

1. Microsoft Foundryలో **+New project** ఎంచుకుని కొత్త ప్రాజెక్ట్ సృష్టించండి.

    ![FineTuneSelect](../../../../translated_images/te/select-new-project.cd31c0404088d7a3.webp)

1. ఈ క్రింది పనులు చేయండి:

    - ప్రాజెక్టు **Hub name** ను నమోదు చేయండి. ఇది ఒక ప్రత్యేకమైన పేరు కావాలి.
    - ఉపయోగించవలసిన **Hub** ను ఎంచుకోండి (తాజాగా సృష్టించడమవలసిన అవసరం ఉంటే సృష్టించండి).

    ![FineTuneSelect](../../../../translated_images/te/create-project.ca3b71298b90e420.webp)

1. కొత్త hub సృష్టించేందుకు ఈ క్రింది పనులు చేయండి:

    - **Hub name** ను నమోదు చేయండి. ఇది ఒక ప్రత్యేకమైన పేరు కావాలి.
    - మీ Azure **Subscription** ను ఎంచుకోండి.
    - ఉపయోగించవలసిన **Resource group** ను ఎంచుకోండి (తాజాగా సృష్టించవలసిన అవసరం ఉంటే సృష్టించండి).
    - మీరు ఉపయోగించదలచిన **Location** ను ఎంచుకోండి.
    - **Connect Azure AI Services** ను ఎంచుకోండి (తాజాగా సృష్టించవలసిన అవసరం ఉంటే సృష్టించండి).
    - **Connect Azure AI Search** లో **Skip connecting** ఎంచుకోండి.

    ![FineTuneSelect](../../../../translated_images/te/create-hub.49e53d235e80779e.webp)

1. **Next** ఎంచుకోండి.
1. **Create a project** ఎంచుకోండి.

### డేటా సన్నాహాలు

ఫైన్-ట్యూటింగ్ ముందు, మీ పని సంబంధిత డేటాసెట్ సేకరించండి లేదా సృష్టించండి, ఉదాహరణకు చాట్ సూచనలు, ప్రశ్న-సమాధాన జంటలు, లేదా ఇతర సంబంధిత పాఠ్య డేటా. ఈ డేటాలో శబ్దాల తొలగింపు, లేమి విలువలను నిర్వహించడం, టోకెనైజేషన్ చేయడం వంటి శుద్ధి మరియు ముందస్తు ప్రాసెసింగ్ చేయండి.

### Microsoft Foundryలో Phi-3 మోడల్స్ ను ఫైన్-ట్యూన్ చేయడం

> [!NOTE]
> Phi-3 మోడల్స్‌కు సంబంధించిన ఫైన్-ట్యూనింగ్ ప్రస్తుతం East US 2 ప్రాంతాల్లో ఉన్న ప్రాజెక్టుల్లో మాత్రమే మద్దతు కలిగి ఉంటుంది.

1. ఎడమవైపు టాబ్ నుండి **Model catalog** ను ఎంచుకోండి.

1. **search bar** లో *phi-3* టైపు చేసి ఉపయోగించదలచిన phi-3 మోడల్ ను ఎంచుకోండి.

    ![FineTuneSelect](../../../../translated_images/te/select-model.60ef2d4a6a3cec57.webp)

1. **Fine-tune** ను ఎంచుకోండి.

    ![FineTuneSelect](../../../../translated_images/te/select-finetune.a976213b543dd9d8.webp)

1. **Fine-tuned model name** నమోదు చేయండి.

    ![FineTuneSelect](../../../../translated_images/te/finetune1.c2b39463f0d34148.webp)

1. **Next** ఎంచుకోండి.

1. ఈ క్రింది పనులు చేయండి:

    - **task type** గా **Chat completion** ఎంచుకోండి.
    - మీరు ఉపయోగించదలచిన **Training data** ఎంచుకోండి. దీన్ని Microsoft Foundry డేటా ద్వారా లేదా మీ స్థానిక వాతావరణం నుండి అప్లోడ్ చేయవచ్చు.

    ![FineTuneSelect](../../../../translated_images/te/finetune2.43cb099b1a94442d.webp)

1. **Next** ఎంచుకోండి.

1. మీరు ఉపయోగించదలచిన **Validation data** ను అప్లోడ్ చేయండి లేదా **Automatic split of training data** ఐచ్ఛికాన్ని ఎంచుకోండి.

    ![FineTuneSelect](../../../../translated_images/te/finetune3.fd96121b67dcdd92.webp)

1. **Next** ఎంచుకోండి.

1. ఈ క్రింది పనులు చేయండి:

    - మీరు ఉపయోగించదలచిన **Batch size multiplier** ఎంచుకోండి.
    - మీరు ఉపయోగించదలచిన **Learning rate** ఎంచుకోండి.
    - మీరు ఉపయోగించదలచిన **Epochs** ఎంచుకోండి.

    ![FineTuneSelect](../../../../translated_images/te/finetune4.e18b80ffccb5834a.webp)

1. ఫైన్-ట్యూనింగ్ ప్రక్రియ ప్రారంభించటానికి **Submit** ఎంచుకోండి.

    ![FineTuneSelect](../../../../translated_images/te/select-submit.0a3802d581bac271.webp)

1. మీ మోడల్ ఫైన్-ట్యూన్ అయిన తర్వాత, క్రింది చిత్రం చూపించినట్లుగా అప్డేట్ "Completed"గా ఉంటుంది. ఇప్పుడు మీరు మోడల్‌ను డిప్లాయ్ చేసి, మీ వినియోగంలో, ప్లేగ్రౌండ్‌లో, లేదా ప్రాంప్ట్ ఫ్లోలో ఉపయోగించవచ్చు. మరింత సమాచారం కొరకు, [Microsoft Foundryతో Phi-3 స్మాల్ లాంగ్వેજ్ మోడల్స్‌ను ఎలా డిప్లాయ్ చేయాలి](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) చూడండి.

    ![FineTuneSelect](../../../../translated_images/te/completed.4dc8d2357144cdef.webp)

> [!NOTE]
> Phi-3 ఫైన్-ట్యూనింగ్ పై సమగ్రమైన సమాచారం కోసం [Fine-tune Phi-3 models in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini) సందర్శించండి.

## ఫైన్-ట్యూన్ చేసిన మోడల్స్‌ను తొలగించటం

[Microsoft Foundry](https://ai.azure.com) లోని ఫైన్-ట్యూనింగ్ మోడల్ జాబితా లేదా మోడల్ వివరాలు పేజీలో ఫైన్-ట్యూన్ మోడల్‌ను తీసివేయవచ్చు. తీసివేయవలసిన ఫైన్-ట్యూన్ మోడల్ ఎంచుకుని Delete బటన్‌ను క్లిక్ చేయండి.

> [!NOTE]
> ఇప్పటికే డిప్లాయ్‌మెంట్ ఉన్న కస్టమ్ మోడల్‌ను మీరు తొలగించలేరు. ముందుగా డిప్లాయ్‌మెంట్ తొలగించాలి మళ్ళీ కస్టమ్ మోడల్ తొలగించవచ్చు.

## ఖర్చు మరియు క్వోటాలు

### ఫైన్-ట్యూన్ చేసిన సర్వీస్ మాదిరిగా Phi-3 మోడల్స్ ఖర్చు మరియు క్వోటా

మైక్రోసాఫ్ట్ ద్వారా అందించబడే ఫైన్-ట్యూన్ సర్వీస్ ద్వారా Phi మోడల్స్ Microsoft Foundryలో ఏకీకృతం చేయబడ్డాయి. మీరు మోడల్స్‌ను [డిప్లాయ్/ఫైన్-ట్యూన్](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) చేసేటప్పుడు ప్రైసింగ్ మరియు షరతుల ట్యాబ్‌లో ధరలను తెలుసుకోవచ్చు.

## కంటెంట్ ఫిల్టరింగ్

Pay-as-you-go సర్వీస్‌తో డిప్లాయ్ చేసిన మోడల్స్ Azure AI Content Safety ద్వారా రక్షించబడతాయి. రియల్-టైమ్ ఎండ్పాయింటులకు డిప్లాయ్ చేసినప్పుడు, ఈ సామర్థ్యం నుండి బయటపడవచ్చు. Azure AI Content Safety ఎనేబుల్ అయితే, ప్రాంప్ట్ మరియు కంప్లీషన్ రెండు హానికర కంటెంట్‌ను గుర్తించి నివారించేందుకు వివిధ తరగతుల క్లాసిఫికేషన్ మోడల్స్‌లోనూ పంపబడతాయి. ఇన్‌పుట్ ప్రాంప్ట్ మరియు అవుట్పుట్ కంప్లీషన్ లోని హానికర కంటెంట్‌ను గుర్తించి చర్యలు తీసుకుంటుంది. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering) గురించి మరింత తెలుసుకోండి.

**ఫైన్-ట్యూన్ కాన్ఫిగరేషన్**

హైపర్పారామీటర్లు: లెర్నింగ్ రేట్, బ్యాచ్ సైజ్, శిక్షణ ఎపోక్స్ వంటి హైపర్‌పారామీటర్లను นิర్ధారించండి.

**లాస్ ఫంక్షన్**

మీ పని కొరకు తగిన లాస్ ఫంక్షన్‌ను ఎంచుకోండి (ఉదా: క్రాస్-ఎంట్రోపీ).

**అప్టిమైజర్**

శిక్షణ సమయంలో గ్రాడియంట్ నవీకరణలకు ఒక అప్టిమైజర్ (ఉదా: అడామ్) ఎంచుకోండి.

**ఫైన్-ట్యూన్ ప్రక్రియ**

- ప్రీ-ట్రైండ్ మోడల్ లోడ్ చేయండి: Phi-3 Mini చెక్‌పాయింట్‌ను లోడ్ చేయండి.
- కస్టమ్ లేయర్లు జోడించండి: నిర్దిష్ట పనులకు అనుగుణంగా (ఉదా: చాట్ సూచనల క్లుాసిఫికేషన్ హెడ్) లేయర్లు చేర్చండి.

**మోడల్‌ను శిక్షణ ఇవ్వండి**

మీ సిద్దం చేసిన డేటాసెట్ ఉపయోగించి ఫైన్-ట్యూన్ చేయండి. శిక్షణ పురోగతిని గమనించి, అవసరమైతే హైపర్‌పారామీటర్లను సవరించండి.

**విలువాలంకరణ మరియు ధృవీకరణ**

ధృవీకరింపుతో: మీ డేటాను శిక్షణ మరియు ధృవీకరణ సెట్లుగా విభజించండి.

**వరిగింపు పనితీరు**

మెట్రిక్స్ లాంటి అక్యురసీ, F1-స్కోర్, లేదా పర్స్‌ప్లెక్సిటీ ఉపయోగించి పనితీరు అంచనా వేయండి.

## ఫైన్-ట్యూన్ చేసిన మోడల్ సేవ్ చేయండి

**చెక్‌పాయింట్**  
భవిష్యత్తు ఉపయోగానికి ఫైన్-ట్యూన్ చేసిన మోడల్ చెక్‌పాయింట్‌ను సేవ్ చేయండి.

## డిప్లాయ్‌మెంట్

- వెబ్ సర్వీస్‌గా డిప్లాయ్ చేయండి: Microsoft Foundryలో మీ ఫైన్-ట్యూన్ చేసిన మోడల్‌ను వెబ్ సర్వీస్‌గా డిప్లాయ్ చేయండి.
- ఎండ్పాయింట్‌ని పరీక్షించండి: డిప్లాయ్ చేసిన ఎండ్పాయింట్‌కు టెస్ట్ ప్రశ్నలు పంపించి పనిచేస్తున్నదో లేదో ధృవీకరించండి.

## పునఃప్రయత్నం మరియు మెరుగుచేయడం

పనితీరు తృప్తికరంగా లేకపోతే, హైపర్‌పారామీటర్లు సవరించడం, మరిన్ని డేటా చేర్చడం, లేదా అదనపు ఎపోక్స్ ఫైన్-ట్యూనింగ్ చేయడం ద్వారా పునఃప్రయత్నం చేయండి.

## పర్యవేక్షణ మరియు శుద్ధి

మోడల్ ప్రవర్తన ను నిరంతరం పర్యవేక్షించి అవసరమైతే మెరుగుచేయండి.

## అనుకూలీకరించండి మరియు విస్తరించండి

కస్టమ్ పనులు: Phi-3 మినీని చాట్ సూచనలకు పక్కగా ఇతర వివిధ పనులకు కూడా ఫైన్-ట్యూన్ చేయవచ్చు. ఇతర వినియోగాలు అన్వేషించండి!

ప్రయోగం: పనితీరు మెరుగుపర్చేందుకు వేర్వేరు ఆర్కిటెక్చర్లు, లేయర్ కలయికలు, సాంకేతిక పద్ధతులు ప్రయోగించండి.

> [!NOTE]
> ఫైన్-ట్యూనింగ్ ఒక పునరావృత ప్రక్రియ. ప్రయోగించండి, నేర్చుకోండి మరియు మీ నిర్దిష్ట పనికి ఉత్తమ ఫలితాల కోసం మీ మోడల్‌ను అనుకూలపరచండి!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అసాధారణ న్యాయమూర్తి**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించారు. మేము సరిగా ఉండేందుకు ప్రయత్నిస్తున్నా, స్వయంచాలిత అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చని దయచేసి గమనించండి. మలాంటి పత్రం స్వభావ భాషలోని అసలు పత్రం అధికారికమైన మూలంగా భావించాలి. ముఖ్యమైన సమాచారానికి వృత్తిపరమైన మానవ అనువాదం సూచించబడుతుంది. ఈ అనువాదం వాడకంలో చూపిన ఏవైనా తప్పు అర్థంప్రత్యర్థాలు లేదా తప్పుదారులు ఏర్పడితే మేము బాధ్యత తీర్చలేము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->