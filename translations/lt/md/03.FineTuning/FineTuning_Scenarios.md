<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cb5648935f63edc17e95ce38f23adc32",
  "translation_date": "2025-09-12T14:46:12+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Scenarios.md",
  "language_code": "lt"
}
-->
## Scenarijai, susiję su modelio pritaikymu

![Modelio pritaikymas su MS paslaugomis](../../../../imgs/03/intro/FinetuningwithMS.png)

**Platforma** Tai apima įvairias technologijas, tokias kaip Azure AI Foundry, Azure Machine Learning, AI Tools, Kaito ir ONNX Runtime.

**Infrastruktūra** Tai apima CPU ir FPGA, kurie yra būtini modelio pritaikymo procesui. Leiskite parodyti kiekvienos iš šių technologijų piktogramas.

**Įrankiai ir karkasai** Tai apima ONNX Runtime ir ONNX Runtime. Leiskite parodyti kiekvienos iš šių technologijų piktogramas.
[Įterpti ONNX Runtime ir ONNX Runtime piktogramas]

Modelio pritaikymo procesas naudojant Microsoft technologijas apima įvairius komponentus ir įrankius. Suprasdami ir naudodami šias technologijas, galime efektyviai pritaikyti savo programas ir kurti geresnius sprendimus.

## Modelis kaip paslauga

Pritaikykite modelį naudodami pritaikymą, kuris yra talpinamas, nereikalaujant kurti ir valdyti skaičiavimo infrastruktūros.

![MaaS modelio pritaikymas](../../../../imgs/03/intro/MaaSfinetune.png)

Serverless pritaikymas yra prieinamas Phi-3-mini ir Phi-3-medium modeliams, leidžiantis kūrėjams greitai ir lengvai pritaikyti modelius debesų ir kraštinių scenarijams, nereikalaujant organizuoti skaičiavimo infrastruktūros. Taip pat paskelbėme, kad Phi-3-small modelis dabar yra prieinamas per mūsų „Modelis kaip paslauga“ pasiūlymą, todėl kūrėjai gali greitai ir lengvai pradėti dirbti su AI kūrimu, nereikalaujant valdyti pagrindinės infrastruktūros.

## Modelis kaip platforma

Vartotojai valdo savo skaičiavimo infrastruktūrą, kad galėtų pritaikyti savo modelius.

![Maap modelio pritaikymas](../../../../imgs/03/intro/MaaPFinetune.png)

[Modelio pritaikymo pavyzdys](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Modelio pritaikymo scenarijai

| | | | | | | |
|-|-|-|-|-|-|-|
|Scenarijus|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DORA|
|Priešmokytų LLM pritaikymas specifinėms užduotims ar sritims|Taip|Taip|Taip|Taip|Taip|Taip|
|Modelio pritaikymas NLP užduotims, tokioms kaip teksto klasifikacija, vardų atpažinimas ir mašininis vertimas|Taip|Taip|Taip|Taip|Taip|Taip|
|Modelio pritaikymas klausimų-atsakymų užduotims|Taip|Taip|Taip|Taip|Taip|Taip|
|Modelio pritaikymas generuoti žmogaus tipo atsakymus pokalbių robotuose|Taip|Taip|Taip|Taip|Taip|Taip|
|Modelio pritaikymas generuoti muziką, meną ar kitus kūrybos formas|Taip|Taip|Taip|Taip|Taip|Taip|
|Skaičiavimo ir finansinių išlaidų mažinimas|Taip|Taip|Ne|Taip|Taip|Ne|
|Atminties naudojimo mažinimas|Ne|Taip|Ne|Taip|Taip|Taip|
|Naudojant mažiau parametrų efektyviam pritaikymui|Ne|Taip|Taip|Ne|Ne|Taip|
|Atminties efektyvi duomenų paralelizmo forma, suteikianti prieigą prie visų GPU įrenginių bendros GPU atminties|Ne|Ne|Ne|Taip|Taip|Taip|

## Modelio pritaikymo našumo pavyzdžiai

![Modelio pritaikymo našumas](../../../../imgs/03/intro/Finetuningexamples.png)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipiame dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus aiškinimus, kylančius dėl šio vertimo naudojimo.