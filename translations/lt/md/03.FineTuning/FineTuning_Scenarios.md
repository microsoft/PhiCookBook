## Koregavimo scenarijai

![FineTuning with MS Services](../../../../translated_images/lt/FinetuningwithMS.3d0cec8ae693e094.webp)

Šiame skyriuje pateikiama koregavimo scenarijų apžvalga Microsoft Foundry ir Azure aplinkose, įskaitant diegimo modelius, infrastruktūros sluoksnius ir dažnai naudojamas optimizavimo technikas.

**Platforma**  
Tai apima valdomas paslaugas, tokias kaip Microsoft Foundry (anksčiau Microsoft Foundry) ir Azure Machine Learning, kurios suteikia modelių valdymą, orkestravimą, eksperimentų stebėjimą ir diegimo darbo eigas.

**Infrastruktūra**  
Koregavimui reikalingi mastelį keičiantys skaičiavimo ištekliai. Azure aplinkose tai paprastai apima GPU pagrindu veikiančius virtualius kompiuterius ir CPU išteklius lengvoms apkrovoms, kartu su mastelio keičiama saugykla duomenų rinkiniams ir kontrolės taškams.

**Įrankiai ir karkasas**  
Koregavimo darbo eigos dažnai remiasi karkasais ir optimizavimo bibliotekomis, tokiomis kaip Hugging Face Transformers, DeepSpeed ir PEFT (Parameter-Efficient Fine-Tuning).

Koregavimo procesas naudojant Microsoft technologijas apima platformos paslaugas, skaičiavimo infrastruktūrą ir mokymo karkasus. Suprasdami, kaip šios sudedamosios dalys veikia kartu, kūrėjai gali efektyviai pritaikyti pagrindinius modelius specifinėms užduotims ir gamybinėms situacijoms.

## Modelis kaip paslauga

Koreguokite modelį naudodami hostinamą koregavimo paslaugą, be poreikio kurti ir valdyti skaičiavimus.

![MaaS Fine Tuning](../../../../translated_images/lt/MaaSfinetune.3eee4630607aff0d.webp)

Serverless koregavimas dabar prieinamas Phi-3, Phi-3.5 ir Phi-4 modelių šeimoms, leidžiantis kūrėjams greitai ir lengvai pritaikyti modelius debesies ir krašto scenarijams be būtinybės rūpintis skaičiavimais.

## Modelis kaip platforma

Vartotojai patys valdo savo skaičiavimo išteklius, kad galėtų koreguoti savo modelius.

![Maap Fine Tuning](../../../../translated_images/lt/MaaPFinetune.fd3829c1122f5d1c.webp)

[Fine Tuning Sample](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Koregavimo technikų palyginimas

|Scenarijus|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DoRA|
|---|---|---|---|---|---|---|
|Iš anksto apmokytų LLM pritaikymas specifinėms užduotims ar domenams|Taip|Taip|Taip|Taip|Taip|Taip|
|Koregavimas NLP užduotims, tokioms kaip teksto klasifikavimas, vardų atpažinimas ir mašininis vertimas|Taip|Taip|Taip|Taip|Taip|Taip|
|Koregavimas QA užduotims|Taip|Taip|Taip|Taip|Taip|Taip|
|Koregavimas generuoti žmogaus panašius atsakymus pokalbių botams|Taip|Taip|Taip|Taip|Taip|Taip|
|Koregavimas generuoti muzikai, menui ar kitoms kūrybinėms formoms|Taip|Taip|Taip|Taip|Taip|Taip|
|Skaičiavimo ir finansinių sąnaudų mažinimas|Taip|Taip|Taip|Taip|Taip|Taip|
|Atminties naudojimo mažinimas|Taip|Taip|Taip|Taip|Taip|Taip|
|Naudojant mažiau parametrų efektyviam koregavimui|Taip|Taip|Taip|Ne|Ne|Taip|
|Atminties efektyvi duomenų paralelizmo forma, suteikianti prieigą prie viso turimų GPU įrenginių bendros atminties|Ne|Ne|Ne|Taip|Taip|Ne|

> [!NOTE]
> LoRA, QLoRA, PEFT ir DoRA yra parametrų efektyvaus koregavimo metodai, o DeepSpeed ir ZeRO daugiausia orientuojasi į paskirstytą mokymą ir atminties optimizavimą.

## Koregavimo našumo pavyzdžiai

![Finetuning Performance](../../../../translated_images/lt/Finetuningexamples.a9a41214f8f5afc1.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atskyrimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatizuoti vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojamas profesionalus žmogaus vertimas. Mes neatsakome už jokius nesusipratimus ar neteisingus interpretavimus, kilusius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->