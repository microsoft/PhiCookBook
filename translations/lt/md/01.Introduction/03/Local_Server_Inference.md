# **Inference Phi-3 vietiniame serveryje**

Phi-3 galima įdiegti vietiniame serveryje. Vartotojai gali pasirinkti [Ollama](https://ollama.com) arba [LM Studio](https://llamaedge.com) sprendimus, arba parašyti savo kodą. Phi-3 vietines paslaugas galima prijungti per [Semantic Kernel](https://github.com/microsoft/semantic-kernel?WT.mc_id=aiml-138114-kinfeylo) arba [Langchain](https://www.langchain.com/), kad būtų kuriamos Copilot programos.

## **Naudokite Semantic Kernel, kad pasiektumėte Phi-3-mini**

Copilot programoje mes kuriame programas naudodami Semantic Kernel / LangChain. Tokio tipo programų struktūra paprastai suderinama su Azure OpenAI Service / OpenAI modeliais, taip pat gali palaikyti atvirojo kodo modelius iš Hugging Face ir vietinius modelius. Ką daryti, jei norime naudoti Semantic Kernel, kad pasiektume Phi-3-mini? Naudojant .NET kaip pavyzdį, galime jį sujungti su Hugging Face Connector Semantic Kernel aplinkoje. Pagal numatymą jis gali atitikti modelio ID Hugging Face platformoje (pirmą kartą naudojant modelis bus atsisiųstas iš Hugging Face, o tai užtrunka ilgai). Taip pat galite prisijungti prie sukurto vietinio serverio. Lyginant abu variantus, rekomenduojame naudoti pastarąjį, nes jis suteikia didesnę autonomiją, ypač verslo programose.

![sk](../../../../../imgs/01/03/LocalServer/sk.png)

Iš paveikslėlio matyti, kad prisijungimas prie vietinių paslaugų per Semantic Kernel leidžia lengvai prijungti savarankiškai sukurtą Phi-3-mini modelio serverį. Čia pateikiamas veikimo rezultatas:

![skrun](../../../../../imgs/01/03/LocalServer/skrun.png)

***Pavyzdinis kodas*** https://github.com/kinfey/Phi3MiniSamples/tree/main/semantickernel

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.