<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-12-21T21:41:50+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "te"
}
-->
# Windows GPU ను ఉపయోగించి Phi-3.5-Instruct ONNX తో Prompt flow పరిష్కారాన్ని సృష్టించడం

కింది డాక్యుమెంట్ Phi-3 మోడళ్ల ఆధారంగా AI అప్లికేషన్లను అభివృద్ధి చేయడానికి ONNX (Open Neural Network Exchange) తో PromptFlow ను ఎలా ఉపయోగించాలో ఒక ఉదాహరణగా ఉంది.

PromptFlow అనేది ఐడియేషన్ మరియు ప్రోటోటైపింగ్ నుండి టెస్టింగ్ మరియు మూల్యాంకన వరకు LLM-ఆధారిత (Large Language Model) AI అప్లికేషన్ల ఎండ్-టు-ఎండ్ అభివృద్ధి చక్రాన్ని సులభతరం చేయడానికి రూపొందించిన ఒక అభివృద్ధి సాధనాల సమాహారం.

PromptFlow ను ONNX తో ఇంటిగ్రేట్ చేయడం ద్వారా డెవలపర్లు చేయగలిగే విషయాలు:

- Optimize Model Performance: ONNX ను సమర్థవంతమైన మోడల్ ఇన్ఫరెన్స్ మరియు డిప్లాయ్‌మెంట్ కోసం వినియోగించండి.
- Simplify Development: Workflow ను నిర్వహించడానికి మరియు పునరావృత పనులను ఆటోమేట్ చేయడానికి PromptFlow ను ఉపయోగించండి.
- Enhance Collaboration: ఏకైక అభివృద్ధి వాతావరణాన్ని అందించడం ద్వారా టీమ్ సభ్యుల మద్య మెరుగైన సహకారాన్ని సులభతరం చేయండి.

**Prompt flow** అనేది ఐడియేషన్, ప్రోటోటైపింగ్, టెస్టింగ్, మూల్యాంకన నుంచి ఉత్పత్తి డిప్లాయ్‌మెంట్ మరియు మానిటరింగ్ వరకు LLM-ఆధారిత AI అప్లికేషన్ల ఎండ్-టు-ఎండ్ అభివృద్ధి చక్రాన్ని సరళీకృతం చేయడానికి రూపొందించిన అభివృద్ధి సాధనాల సమాహారం. ఇది prompt ఇంజినీరింగ్‌ను చాలా సులభతరం చేస్తుంది మరియు మీకు ప్రొడక్షన్-నాణ్యత గల LLM అనువర్తనాలను నిర్మించడానికి సహాయపడుతుంది.

Prompt flow OpenAI, Azure OpenAI Service, మరియు కస్టమైజబుల్ మోడల్స్ (Huggingface, local LLM/SLM) కు కనెక్ట్ కావచ్చు. మేము Phi-3.5 యొక్క క్వాంటైజ్డ్ ONNX మోడల్‌ను లోకల్ అప్లికేషన్లకు డిప్లాయ్ చేయాలని ఆశిస్తున్నాము. Prompt flow మాకు మా వ్యాపారాన్ని మెరుగ్గా ప్రణాళిక గావించడంలో మరియు Phi-3.5 ఆధారిత లోకల్ పరిష్కారాలను పూర్తి చేయడంలో సహాయపడుతుంది. ఈ ఉదాహరణలో, మేము Windows GPU ఆధారిత Prompt flow పరిష్కారాన్ని పూర్తి చేయడానికి ONNX Runtime GenAI Library ను కలపబోతున్నాము.

## **సంస్థాపన**

### **Windows GPU కొరకు ONNX Runtime GenAI**

Windows GPU కోసం ONNX Runtime GenAI అమర్చడానికి ఈ మార్గదర్శకాన్ని చదవండి  [ఇక్కడ క్లిక్ చేయండి](./ORTWindowGPUGuideline.md)

### **VSCodeలో Prompt flow సెటప్ చేయండి**

1. Install Prompt flow VS Code Extension

![pfvscode](../../../../../../translated_images/pfvscode.eff93dfc66a42cbef699fc16fa48f3ed3a23361875a3362037d026896395a00d.te.png)

2. After install Prompt flow VS Code Extension， click the extension，and choose **Installation dependencies** follow this guideline to install Prompt flow SDK in your env

![pfsetup](../../../../../../translated_images/pfsetup.b46e93096f5a254f74e8b74ce2be7047ce963ef573d755ec897eb1b78cb9c954.te.png)

3. Download [నమూనా కోడ్](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) and use VS Code to open this sample

![pfsample](../../../../../../translated_images/pfsample.8d89e70584ffe7c4dba182513e3148a989e552c3b8e4948567a6b806b5ae1845.te.png)

4. Open **flow.dag.yaml** to choose your Python env

![pfdag](../../../../../../translated_images/pfdag.264a77f7366458ff850a76ae949226391ea382856d543ef9da4b92096aff7e4b.te.png)

   Open **chat_phi3_ort.py** to change your Phi-3.5-instruct ONNX Model location

![pfphi](../../../../../../translated_images/pfphi.72da81d74244b45fc78cdfeeb8c7fbd9e7cd610bf2f96814dbade6a4a2dfad7e.te.png)

5. Run your prompt flow to testing

Open **flow.dag.yaml** click visual editor

![pfv](../../../../../../translated_images/pfv.ba8a81f34b20f603cccee3fe91e94113792ed6f5af28f76ab08e1a0b3e77b33b.te.png)

after click this,and run it to test

![pfflow](../../../../../../translated_images/pfflow.4e1135a089b1ce1b6348b59edefdb6333e5729b54c8e57f9039b7f9463e68fbd.te.png)

1. You can run batch in terminal to check more result


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

You can check results in your default browser


![pfresult](../../../../../../translated_images/pfresult.c22c826f8062d7cbe871cff35db4a013dcfefc13fafe5da6710a8549a96a4ceb.te.png)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
నిరాకరణ:
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో తప్పులు లేదా లోపాలు ఉండవచ్చని దయచేసి గమనించండి. మూల పత్రాన్ని దాని మాతృభాషలో ఉన్న సంస్కరణను అధికారిక మూలంగా తీసుకోవాలి. కీలక సమాచారానికి, వృత్తిపరమైన మానవ అనువాదం పొందాలని సూచిస్తాము. ఈ అనువాదం ఉపయోగించడంతో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుగా అర్థం చేసుకోవడాలకు మేము బాధ్యులు కాదని తెలియజేస్తాం.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->