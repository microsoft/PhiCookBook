<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-07-17T03:04:10+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "hr"
}
-->
# Korištenje Windows GPU-a za izradu Prompt flow rješenja s Phi-3.5-Instruct ONNX

Sljedeći dokument je primjer kako koristiti PromptFlow s ONNX-om (Open Neural Network Exchange) za razvoj AI aplikacija temeljenih na Phi-3 modelima.

PromptFlow je skup razvojnih alata dizajniran za pojednostavljenje cjelokupnog razvojnog ciklusa AI aplikacija baziranih na LLM-u (Large Language Model), od ideje i prototipiranja do testiranja i evaluacije.

Integracijom PromptFlow-a s ONNX-om, developeri mogu:

- Optimizirati performanse modela: Iskoristiti ONNX za učinkovitu inferenciju i implementaciju modela.
- Pojednostaviti razvoj: Koristiti PromptFlow za upravljanje radnim procesom i automatizaciju ponavljajućih zadataka.
- Poboljšati suradnju: Omogućiti bolju suradnju među članovima tima pružajući jedinstveno razvojno okruženje.

**Prompt flow** je skup razvojnih alata osmišljen za pojednostavljenje cjelokupnog razvojnog ciklusa AI aplikacija baziranih na LLM-u, od ideje, prototipiranja, testiranja, evaluacije do produkcijske implementacije i nadzora. Olakšava prompt inženjering i omogućuje izgradnju LLM aplikacija proizvodne kvalitete.

Prompt flow može se povezati s OpenAI, Azure OpenAI Service i prilagodljivim modelima (Huggingface, lokalni LLM/SLM). Cilj nam je implementirati kvantizirani ONNX model Phi-3.5 u lokalne aplikacije. Prompt flow nam može pomoći bolje planirati poslovanje i dovršiti lokalna rješenja temeljena na Phi-3.5. U ovom primjeru kombinirat ćemo ONNX Runtime GenAI Library za dovršetak Prompt flow rješenja baziranog na Windows GPU-u.

## **Instalacija**

### **ONNX Runtime GenAI za Windows GPU**

Pročitajte ovaj vodič za postavljanje ONNX Runtime GenAI za Windows GPU [kliknite ovdje](./ORTWindowGPUGuideline.md)

### **Postavljanje Prompt flow u VSCode**

1. Instalirajte Prompt flow VS Code ekstenziju

![pfvscode](../../../../../../translated_images/pfvscode.eff93dfc66a42cbef699fc16fa48f3ed3a23361875a3362037d026896395a00d.hr.png)

2. Nakon instalacije Prompt flow VS Code ekstenzije, kliknite na ekstenziju i odaberite **Installation dependencies** te slijedite ovaj vodič za instalaciju Prompt flow SDK-a u vašem okruženju

![pfsetup](../../../../../../translated_images/pfsetup.b46e93096f5a254f74e8b74ce2be7047ce963ef573d755ec897eb1b78cb9c954.hr.png)

3. Preuzmite [Sample Code](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) i otvorite ovaj primjer u VS Code-u

![pfsample](../../../../../../translated_images/pfsample.8d89e70584ffe7c4dba182513e3148a989e552c3b8e4948567a6b806b5ae1845.hr.png)

4. Otvorite **flow.dag.yaml** i odaberite svoje Python okruženje

![pfdag](../../../../../../translated_images/pfdag.264a77f7366458ff850a76ae949226391ea382856d543ef9da4b92096aff7e4b.hr.png)

   Otvorite **chat_phi3_ort.py** i promijenite lokaciju Phi-3.5-instruct ONNX modela

![pfphi](../../../../../../translated_images/pfphi.72da81d74244b45fc78cdfeeb8c7fbd9e7cd610bf2f96814dbade6a4a2dfad7e.hr.png)

5. Pokrenite svoj prompt flow za testiranje

Otvorite **flow.dag.yaml** i kliknite na visual editor

![pfv](../../../../../../translated_images/pfv.ba8a81f34b20f603cccee3fe91e94113792ed6f5af28f76ab08e1a0b3e77b33b.hr.png)

nakon klika, pokrenite ga za testiranje

![pfflow](../../../../../../translated_images/pfflow.4e1135a089b1ce1b6348b59edefdb6333e5729b54c8e57f9039b7f9463e68fbd.hr.png)

1. Možete pokrenuti batch u terminalu za pregled dodatnih rezultata


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Rezultate možete provjeriti u svom zadanim pregledniku


![pfresult](../../../../../../translated_images/pfresult.c22c826f8062d7cbe871cff35db4a013dcfefc13fafe5da6710a8549a96a4ceb.hr.png)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.