<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-09-12T14:32:20+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "lt"
}
-->
# Naudojant Windows GPU sukurti Prompt flow sprendimą su Phi-3.5-Instruct ONNX

Šis dokumentas yra pavyzdys, kaip naudoti PromptFlow su ONNX (Open Neural Network Exchange) kuriant dirbtinio intelekto programas, pagrįstas Phi-3 modeliais.

PromptFlow yra įrankių rinkinys, skirtas supaprastinti visą LLM (Didelių Kalbos Modelių) pagrįstų dirbtinio intelekto programų kūrimo ciklą – nuo idėjų generavimo ir prototipavimo iki testavimo ir vertinimo.

Integruojant PromptFlow su ONNX, kūrėjai gali:

- **Optimizuoti modelio našumą**: Naudoti ONNX efektyviam modelio įvertinimui ir diegimui.
- **Supaprastinti kūrimą**: Naudoti PromptFlow darbo eigai valdyti ir automatizuoti pasikartojančias užduotis.
- **Pagerinti bendradarbiavimą**: Palengvinti komandos narių bendradarbiavimą, suteikiant vieningą kūrimo aplinką.

**Prompt flow** yra įrankių rinkinys, skirtas supaprastinti visą LLM pagrįstų dirbtinio intelekto programų kūrimo ciklą – nuo idėjų generavimo, prototipavimo, testavimo, vertinimo iki diegimo ir stebėjimo gamyboje. Jis palengvina promptų kūrimą ir leidžia kurti aukštos kokybės LLM programas.

Prompt flow gali prisijungti prie OpenAI, Azure OpenAI Service ir pritaikomų modelių (Huggingface, vietiniai LLM/SLM). Tikimės diegti Phi-3.5 kvantizuotą ONNX modelį vietinėse programose. Prompt flow gali padėti geriau planuoti mūsų verslą ir įgyvendinti vietinius sprendimus, pagrįstus Phi-3.5. Šiame pavyzdyje mes sujungsime ONNX Runtime GenAI biblioteką, kad užbaigtume Prompt flow sprendimą, pagrįstą Windows GPU.

## **Įdiegimas**

### **ONNX Runtime GenAI Windows GPU**

Perskaitykite šį vadovą, kaip nustatyti ONNX Runtime GenAI Windows GPU [spauskite čia](./ORTWindowGPUGuideline.md)

### **Prompt flow nustatymas VSCode**

1. Įdiekite Prompt flow VS Code plėtinį

![pfvscode](../../../../../../imgs/02/pfonnx/pfvscode.png)

2. Po Prompt flow VS Code plėtinio įdiegimo, spustelėkite plėtinį ir pasirinkite **Installation dependencies**, vadovaukitės šiuo vadovu, kad įdiegtumėte Prompt flow SDK savo aplinkoje.

![pfsetup](../../../../../../imgs/02/pfonnx/pfsetup.png)

3. Atsisiųskite [Pavyzdinį kodą](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) ir atidarykite šį pavyzdį naudodami VS Code.

![pfsample](../../../../../../imgs/02/pfonnx/pfsample.png)

4. Atidarykite **flow.dag.yaml**, kad pasirinktumėte savo Python aplinką.

![pfdag](../../../../../../imgs/02/pfonnx/pfdag.png)

   Atidarykite **chat_phi3_ort.py**, kad pakeistumėte Phi-3.5-instruct ONNX modelio vietą.

![pfphi](../../../../../../imgs/02/pfonnx/pfphi.png)

5. Paleiskite savo Prompt flow testavimui.

Atidarykite **flow.dag.yaml** ir spustelėkite vizualų redaktorių.

![pfv](../../../../../../imgs/02/pfonnx/pfv.png)

Po to spustelėkite ir paleiskite testavimui.

![pfflow](../../../../../../imgs/02/pfonnx/pfflow.png)

1. Galite paleisti paketą terminale, kad patikrintumėte daugiau rezultatų.

```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Rezultatus galite peržiūrėti savo numatytoje naršyklėje.

![pfresult](../../../../../../imgs/02/pfonnx/pfresult.png)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.