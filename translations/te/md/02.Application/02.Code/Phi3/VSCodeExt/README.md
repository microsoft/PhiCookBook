# **మీరే మీ వెర్షన్ Visual Studio Code GitHub Copilot Chatని Microsoft Phi-3 ఫ్యామిలीसహ కట్టండి**

GitHub Copilot Chatలో workspace ఏజెంట్‌ను మీరు ఉపయోగించారా? మీ టీమ్‌కు మీ స్వంత కోడ్ ఏజెంట్‌ని నిర్మించాలనుకుంటున్నారా? ఈ హ్యాండ్స్-ఆన్ ల్యాబ్ ఓపెన్ సోర్స్ మోడల్‌ను కేటాయించి ఒక ఎంటర్‌ప్రైజ్ స్థాయి కోడ్ బిజినెస్ ఏజెంట్‌ను నిర్మించడానికి లక్ష్యంగా ఉంది.

## **ఫౌండేషన్**

### **Microsoft Phi-3ని ఎందుకు ఎంచుకోవాలి**

Phi-3 అనేది ఒక ఫ్యామిలీ సిరీస్, దీనిలో phi-3-mini, phi-3-small, మరియు phi-3-medium ఉన్నాయి, వీటిని వచనం ఉత్పత్తి, సంభాషణ పూర్తిచేయడం మరియు కోడ్ ఉత్పత్తికి వేరే శిక్షణ పరిమాణాలపై ఆధారపడి రూపొందించారు. Vision ఆధారంగా phi-3-vision కూడా ఉంది. ఇది సంస్థలు లేదా వేరే టీమ్‌లు ఆఫ్‌లైన్ జనరేటివ్ AI సొల్యూషన్లు సృష్టించేందుకు అనుకూలంగా ఉంటుంది.

ఈ లింక్ చదవాలని సూచించబడింది [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

GitHub Copilot Chat విస్తరణ మీరు GitHub Copilotతో సంభాషించడానికి మరియు కోడింగ్-సంబంధిత ప్రశ్నలకు సమాధానాలు అందుకునే చాట్ ఇంటర్‌ఫేస్‌ను ఇస్తుంది, మీరు డాక్యుమెంటేషన్ ని చూడకుండా లేదా ఆన్‌లైన్ ఫోరమ్‌లలో శోధించకుండా నేరుగా VS Code లో.

Copilot Chat సింటాక్స్ హైలైటింగ్, ఇండెంటేషన్ మరియు ఇతర ఫార్మాటింగ్ లక్షణాలను ఉపయోగించి ఉత్పత్తి చేసిన ప్రతిస్పందనలో స్పష్టతను కల్పిస్తుంది. వాడుకరి ప్రశ్న రకాన్ని బట్టి, ఫలితం Copilot ప్రతిస్పందన సృష్టించడానికి ఉపయోగించిన మూలాల లింకులు (ఉదా: సోర్స్ కోడ్ ఫైళ్ల లేదా డాక్యుమెంటేషన్) లేదా VS Code ఫంక్షనాలిటీ యాక్సెస్ చేసే బటన్లను కలిగి ఉండొచ్చు.

- Copilot Chat మీ డెవలపర్ ప్రవాహంలో సమకూర్చబడింది మరియు మీరు అవసరమైన చోట సహాయం ఇస్తుంది:

- ఎడిటర్ లేదా టెర్మినల్ నుండి నేరుగా ఒక ఇన్‌లైన్ చాట్ సంభాషణను ప్రారంభించి కోడింగ్ చేస్తున్నప్పుడు సహాయం పొందండి

- ఎప్పుడైనా సహాయం కోసం సైడ్ AI అసిస్టెంట్ కావాలంటే Chat వీక్షణ ఉపయోగించండి

- సత్వర ప్రశ్న అడిగి వెంటనే మళ్లీ పని లోకి చేరేందుకు Quick Chat ప్రారంభించండి

GitHub Copilot Chatను వివిధ సందర్భాలలో ఉపయోగించవచ్చు, ఉదా:

- ఒక సమస్యను ఎలా ఉత్తమంగా పరిష్కరించాలో కోడింగ్ ప్రశ్నలకు సమాధానం ఇవ్వడం

- మరొకరి కోడ్‌ను వివరించడం మరియు మెరుగుదల సూచించడం

- కోడ్ సవరణలను ప్రతిపాదించడం

- యూనిట్ టెస్ట్ కేసులు జనరేట్ చేయడం

- కోడ్ డాక్యుమెంటేషన్ తయారు చేయడం

ఈ లింక్‌ను చదవాలని సూచించబడింది [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat @workspace**

Copilot Chatలో **@workspace**ని సూచించడం ద్వారా మీరు మీ మొత్తం కోడ్‌బేస్ గురించి ప్రశ్నలు అడగవచ్చు. ప్రశ్న ఆధారంగా, Copilot సత్ఫలామయమైన ఫైళ్ళను మరియు సింబల్స్‌ను తెలివిగా తీసి, వాటిని జవాబులో లింకులు మరియు కోడ్ ఉదాహరణలుగా సూచిస్తుంది.

మీ ప్రశ్నకు సమాధానం ఇవ్వడానికి, **@workspace** కింది మూలాలను వాడుతుంది, అవి VS Codeలో కోడ్‌బేస్‌ను నావిగేట్ చేసే డెవలపర్ వాడే ప్రమాదం ఉంటుంది:

- వర్క్‌స్పేస్‌లోని అన్ని ఫైళ్ళు, .gitignore ఫైల్ ద్వారా నిర్లక్ష్యం చేయబడిన ఫైళ్ళు తప్ప

- డైరెక్టరీ నిర్మాణం, నెస్టెడ్ ఫోల్‌డర్ మరియు ఫైల్ పేర్లు

- వర్క్‌స్పేస్ ఒక GitHub రిపోజిటరీయైనా, కోడ్ సెర్చ్ ద్వారా సూచిక చేయబడిన GitHub కోడ్ సెర్చ్ సూచిక

- వర్క్‌స్పేస్‌లోని సింబల్స్ మరియు నిర్వచనలు

- ప్రస్తుతం ఎంచుకున్న వచనం లేదా ప్రస్తావించిన ఎడిటర్‌లో కనపడే వచనం

గమనిక: మీరు ఓపెన్ చేసిన లేదా ఎంపిక చేసిన వచనం ఉన్న నిర్లక్ష్యం చేయబడిన ఫైల్ ఉన్నా .gitignore ఆవృతం చేయబడదు.

ఈ లింక్‌ను చదవాలని సూచించబడింది [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **ఈ ల్యాబ్ గురించి మరింత తెలుసుకోండి**

GitHub Copilot సంస్థల ప్రోగ్రామింగ్ సామర్థ్యాన్ని గొప్పగా మెరుగుపరిచింది, మరియు ప్రతి సంస్థ GitHub Copilotలో సంబంధిత ఫంక్షన్లను అనుకూలీకరించాలని ఆశిస్తారు. అనేక సంస్థలు తమ స్వంత వ్యాపార పరిస్థితులు మరియు ఓపెన్ సోర్స్ మోడల్స్ ఆధారంగా GitHub Copilotను సదృశంగా ఉన్న అనుకూల విస్తరణలను రూపొందించాయి. సంస్థల కోసం, అనుకూల విస్తరణలు నియంత్రించడానికి సులభంగా ఉంటాయి, కానీ దీని వల్ల వాడుకరి అనుభవం ప్రభావితమవుతుంది. GitHub Copilot సాధారణ పరిస్థితుల మరియు ప్రొఫెషనలిజంతో వ్యవహరించడంలో బలమైన ఫంక్షన్లను కలిగి ఉంది. అనుభవం సुसంగతంగా ఉంటే, సంస్థ యొక్క స్వంత విస్తరణను అనుకూలీకరించడం ఉత్తమం. GitHub Copilot Chat సంస్థలకు చాట్ అనుభవంలో విస్తరించగల సంబంధిత APIలను అందిస్తుంది. సుసంగత అనుభవం మరియు అనుకూల ఫంక్షన్ల కలిగినది మెరుగైన వాడుకరి అనుభవం.

ఈ ల్యాబ్ ప్రధానంగా Phi-3 మోడల్‌ను లోకల్ NPU మరియు Azure హైబ్రిడ్‌తో కలిపి GitHub Copilot Chatలో అనుకూల ఏజెంట్ ***@PHI3*** ని నిర్మించి, సంస్థ డెవలపర్‌లకు కోడ్ జనరేషన్***(@PHI3 /gen)*** మరియు చిత్రాల ఆధారంగా కోడ్ జనరేషన్***(@PHI3 /img)***లో సహాయం చేస్తుంది.

![PHI3](../../../../../../../translated_images/te/cover.1017ebc9a7c46d09.webp)

### ***గమనిక:*** 

ఈ ల్యాబ్ ప్రస్తుతం Intel CPU మరియు Apple Silicon యొక్క AIPCలో అమలు చేయబడింది. Qualcomm యొక్క NPU సంచికను మేము నిరంతరం నవీకరించగలము.


## **ల్యాబ్**


| పేరు | వివరణ | AIPC | యాపిల్ |
| ------------ | ----------- | -------- |-------- |
| Lab0 - ఇన్‌స్టాలేషన్లు(✅) | సంబంధిత పర్యావరణాలు మరియు ఇన్‌స్టాలేషన్ సాధనాలు సెట్ చేయడం, ఇన్‌స్టాల్ చేయడం | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Phi-3-miniతో ప్రాంప్ట్ ఫ్లో నడపడం(✅) | AIPC / Apple Siliconతో కలిపి, లోకల్ NPU ఉపయోగించి Phi-3-mini ద్వారా కోడ్ ఉత్పత్తి సృష్టించడం | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Azure మెషీన్ లెర్నింగ్ సర్వీస్‌పై Phi-3-visionని ఏర్పాటుచేయడం(✅) | Azure మెషీన్ లెర్నింగ్ సర్వీస్ యొక్క మోడల్ క్యాటలాగ్ - Phi-3-vision చిత్రాన్ని డిప్లాయ్ చేసి కోడ్‌ను ఉత్పత్తి చేయడం | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - GitHub Copilot Chatలో @phi-3 ఏజెంట్ సృష్టించడం(✅)  | GitHub Copilot Chatలో అనుకూల Phi-3 ఏజెంట్ సృష్టించి కోడ్ జనరేషన్, గ్రాఫ్ జనరేషన్ కోడ్, RAG మొదలైనవి పూర్తి చేయడం | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| నమూనా కోడ్ (✅)  | నమూనా కోడ్ డౌన్‌లోడ్ చేయండి | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |


## **వనరులు**

1. Phi-3 కుక్‌బుక్ [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. GitHub Copilot గురించి మరింత తెలుసుకోండి [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. GitHub Copilot Chat గురించి మరింత తెలుసుకోండి [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. GitHub Copilot Chat API గురించి మరింత తెలుసుకోండి [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Microsoft Foundry గురించి మరింత తెలుసుకోండి [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Microsoft Foundry యొక్క మోడల్ క్యాటలాగ్ గురించి మరింత తెలుసుకోండి [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**స్వీయ బాధ్యతా నివారణ**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మనం సరైనత కోసం శ్రమిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు పొరపాట్లు లేదా అసాధారణతలు కలిగి ఉండవచ్చు అనే విషయాన్ని గమనించండి. మూల పత్రం దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. కీలక సమాచారానికి, వృత్తిపరమైన మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదాన్ని ఉపయోగించడంనుంచి వచ్చిన ఏ తప్పుదారులవ్వడం లేదా తప్పుదాటుపులకు మేము బాధ్యులు కాదు.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->