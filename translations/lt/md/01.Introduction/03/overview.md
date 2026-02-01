Phi-3-mini kontekste, išvedimas reiškia procesą, kai modelis naudojamas prognozėms ar rezultatams generuoti remiantis įvesties duomenimis. Pateiksiu daugiau informacijos apie Phi-3-mini ir jo išvedimo galimybes.

Phi-3-mini yra dalis Phi-3 modelių serijos, kurią išleido Microsoft. Šie modeliai sukurti tam, kad iš naujo apibrėžtų, ką galima pasiekti naudojant mažus kalbos modelius (SLM).

Štai keletas pagrindinių punktų apie Phi-3-mini ir jo išvedimo galimybes:

## **Phi-3-mini apžvalga:**
- Phi-3-mini turi 3,8 milijardo parametrų.
- Jis gali veikti ne tik tradiciniuose kompiuteriuose, bet ir kraštiniuose įrenginiuose, tokiuose kaip mobilieji įrenginiai ir IoT įrenginiai.
- Phi-3-mini išleidimas leidžia tiek pavieniams vartotojams, tiek įmonėms diegti SLM įvairiuose techninės įrangos įrenginiuose, ypač ribotų resursų aplinkose.
- Jis palaiko įvairius modelių formatus, įskaitant tradicinį PyTorch formatą, kvantizuotą gguf formato versiją ir ONNX pagrįstą kvantizuotą versiją.

## **Phi-3-mini pasiekimas:**
Norėdami pasiekti Phi-3-mini, galite naudoti [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) Copilot programoje. Semantic Kernel paprastai suderinamas su Azure OpenAI Service, atvirojo kodo modeliais Hugging Face platformoje ir vietiniais modeliais.
Taip pat galite naudoti [Ollama](https://ollama.com) arba [LlamaEdge](https://llamaedge.com) kvantizuotiems modeliams iškviesti. Ollama leidžia pavieniams vartotojams iškviesti skirtingus kvantizuotus modelius, o LlamaEdge suteikia GGUF modelių prieinamumą įvairiose platformose.

## **Kvantizuoti modeliai:**
Daugelis vartotojų renkasi kvantizuotus modelius vietiniam išvedimui. Pavyzdžiui, galite tiesiogiai paleisti Ollama run Phi-3 arba konfigūruoti jį neprisijungus naudodami Modelfile. Modelfile nurodo GGUF failo kelią ir raginimo formatą.

## **Generatyviosios AI galimybės:**
SLM, tokie kaip Phi-3-mini, derinimas atveria naujas generatyviosios AI galimybes. Išvedimas yra tik pirmasis žingsnis; šie modeliai gali būti naudojami įvairioms užduotims ribotų resursų, mažo delsimo ir mažų kaštų scenarijuose.

## **Generatyviosios AI atrakinimas su Phi-3-mini: vadovas išvedimui ir diegimui** 
Sužinokite, kaip naudoti Semantic Kernel, Ollama/LlamaEdge ir ONNX Runtime, kad pasiektumėte ir išvestumėte Phi-3-mini modelius, bei tyrinėkite generatyviosios AI galimybes įvairiuose taikymo scenarijuose.

**Funkcijos**
Phi-3-mini modelio išvedimas:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

Apibendrinant, Phi-3-mini leidžia kūrėjams tyrinėti skirtingus modelių formatus ir pasinaudoti generatyviosios AI galimybėmis įvairiuose taikymo scenarijuose.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.