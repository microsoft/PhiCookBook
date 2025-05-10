<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-05-09T18:55:48+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "hr"
}
-->
# Korištenje Windows GPU-a za kreiranje Prompt flow rješenja s Phi-3.5-Instruct ONNX

Sljedeći dokument je primjer kako koristiti PromptFlow s ONNX-om (Open Neural Network Exchange) za razvoj AI aplikacija temeljenih na Phi-3 modelima.

PromptFlow je skup razvojnih alata dizajniran za pojednostavljenje cjelokupnog razvojog ciklusa AI aplikacija baziranih na LLM-u (Large Language Model), od ideje i prototipiranja do testiranja i evaluacije.

Integracijom PromptFlow-a s ONNX-om, developeri mogu:

- Optimizirati performanse modela: Iskoristiti ONNX za učinkovitu inferenciju i implementaciju modela.
- Pojednostaviti razvoj: Koristiti PromptFlow za upravljanje radnim procesom i automatizaciju ponavljajućih zadataka.
- Poboljšati suradnju: Omogućiti bolju suradnju među članovima tima pružajući jedinstveno razvojno okruženje.

**Prompt flow** je skup razvojnih alata dizajniran za pojednostavljenje cjelokupnog razvojog ciklusa AI aplikacija baziranih na LLM-u, od ideje, prototipiranja, testiranja, evaluacije do produkcijske implementacije i nadzora. Značajno olakšava prompt inženjering i omogućuje vam izgradnju LLM aplikacija proizvodne kvalitete.

Prompt flow može se povezati s OpenAI, Azure OpenAI Service, te prilagodljivim modelima (Huggingface, lokalni LLM/SLM). Cilj nam je implementirati kvantizirani ONNX model Phi-3.5 u lokalne aplikacije. Prompt flow nam može pomoći bolje planirati poslovanje i dovršiti lokalna rješenja temeljena na Phi-3.5. U ovom primjeru kombinirat ćemo ONNX Runtime GenAI biblioteku za dovršetak Prompt flow rješenja na Windows GPU-u.

## **Instalacija**

### **ONNX Runtime GenAI za Windows GPU**

Pročitajte ovaj vodič za postavljanje ONNX Runtime GenAI za Windows GPU [kliknite ovdje](./ORTWindowGPUGuideline.md)

### **Postavljanje Prompt flow u VSCode**

1. Instalirajte Prompt flow VS Code ekstenziju

![pfvscode](../../../../../../translated_images/pfvscode.79f42ae5dd93ed35c19d6d978ae75831fef40e0b8440ee48b893b5a0597d2260.hr.png)

2. Nakon instalacije Prompt flow VS Code ekstenzije, kliknite na ekstenziju i odaberite **Installation dependencies** te slijedite upute za instalaciju Prompt flow SDK-a u vašem okruženju

![pfsetup](../../../../../../translated_images/pfsetup.0c82d99c7760aac29833b37faf4329e67e22279b1c5f37a73724dfa9ebaa32ee.hr.png)

3. Preuzmite [Sample Code](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) i otvorite ovaj uzorak u VS Code-u

![pfsample](../../../../../../translated_images/pfsample.7bf40b133a558d86356dd6bc0e480bad2659d9c5364823dae9b3e6784e6f2d25.hr.png)

4. Otvorite **flow.dag.yaml** i odaberite svoje Python okruženje

![pfdag](../../../../../../translated_images/pfdag.c5eb356fa3a96178cd594de9a5da921c4bbe646a9946f32aa20d344ccbeb51a0.hr.png)

   Otvorite **chat_phi3_ort.py** i promijenite lokaciju Phi-3.5-instruct ONNX modela

![pfphi](../../../../../../translated_images/pfphi.fff4b0afea47c92c8481174dbf3092823906fca5b717fc642f78947c3e5bbb39.hr.png)

5. Pokrenite svoj prompt flow za testiranje

Otvorite **flow.dag.yaml** i kliknite na vizualni editor

![pfv](../../../../../../translated_images/pfv.7af6ecd65784a98558b344ba69b5ba6233876823fb435f163e916a632394fc1e.hr.png)

nakon klika, pokrenite ga za testiranje

![pfflow](../../../../../../translated_images/pfflow.9697e0fda67794bb0cf4b78d52e6f5a42002eec935bc2519933064afbbdd34f0.hr.png)

1. Možete pokrenuti batch u terminalu za detaljnije rezultate


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Rezultate možete pogledati u svom zadanim pregledniku


![pfresult](../../../../../../translated_images/pfresult.972eb57dd5bec646e1aa01148991ba8959897efea396e42cf9d7df259444878d.hr.png)

**Odricanje od odgovornosti**:  
Ovaj dokument preveden je korištenjem AI usluge prevođenja [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.