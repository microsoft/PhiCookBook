<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cbe7629d254f1043193b7fe22524d55",
  "translation_date": "2025-09-12T14:50:10+00:00",
  "source_file": "md/01.Introduction/05/Promptflow.md",
  "language_code": "lt"
}
-->
# **Pristatome Promptflow**

[Microsoft Prompt Flow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=aiml-138114-kinfeylo) yra vizualinis darbo eigų automatizavimo įrankis, leidžiantis vartotojams kurti automatizuotas darbo eigas naudojant iš anksto paruoštus šablonus ir pasirinktinius jungiklius. Jis sukurtas tam, kad kūrėjai ir verslo analitikai galėtų greitai kurti automatizuotus procesus, skirtus tokioms užduotims kaip duomenų valdymas, bendradarbiavimas ir procesų optimizavimas. Naudodami Prompt Flow, vartotojai gali lengvai sujungti skirtingas paslaugas, programas ir sistemas bei automatizuoti sudėtingus verslo procesus.

Microsoft Prompt Flow yra sukurtas tam, kad supaprastintų visą dirbtinio intelekto programų, paremtų dideliais kalbos modeliais (LLMs), kūrimo ciklą. Nesvarbu, ar generuojate idėjas, kuriate prototipus, testuojate, vertinate ar diegiate LLM pagrįstas programas, Prompt Flow palengvina procesą ir leidžia kurti aukštos kokybės LLM programas.

## Pagrindinės Microsoft Prompt Flow funkcijos ir privalumai:

**Interaktyvi kūrimo patirtis**

Prompt Flow pateikia vizualinį jūsų darbo eigos struktūros vaizdą, kuris padeda lengvai suprasti ir naršyti projektus.
Siūlo užrašų knygelės tipo kodavimo patirtį, leidžiančią efektyviai kurti ir derinti darbo eigas.

**Skirtingų užklausų variantai ir jų derinimas**

Kurti ir lyginti kelis užklausų variantus, kad būtų lengviau iteratyviai tobulinti procesą. Įvertinti skirtingų užklausų efektyvumą ir pasirinkti veiksmingiausius.

**Įmontuotos vertinimo darbo eigos**

Įvertinti užklausų ir darbo eigų kokybę bei efektyvumą naudojant įmontuotus vertinimo įrankius.
Suprasti, kaip gerai veikia jūsų LLM pagrįstos programos.

**Išsamūs ištekliai**

Prompt Flow apima įrankių, pavyzdžių ir šablonų biblioteką. Šie ištekliai padeda pradėti kūrimą, įkvepia kūrybiškumui ir pagreitina procesą.

**Bendradarbiavimas ir pasirengimas įmonėms**

Palaikyti komandinį darbą, leidžiant keliems vartotojams kartu dirbti su užklausų kūrimo projektais.
Užtikrinti versijų kontrolę ir efektyviai dalintis žiniomis. Supaprastinti visą užklausų kūrimo procesą – nuo kūrimo ir vertinimo iki diegimo ir stebėjimo.

## Vertinimas Prompt Flow aplinkoje

Microsoft Prompt Flow aplinkoje vertinimas yra esminis procesas, padedantis įvertinti, kaip gerai veikia jūsų dirbtinio intelekto modeliai. Pažvelkime, kaip galite pritaikyti vertinimo darbo eigas ir metrikas Prompt Flow aplinkoje:

![PFVizualise](../../../../../imgs/01/05/PromptFlow/pfvisualize.png)

**Vertinimo supratimas Prompt Flow aplinkoje**

Prompt Flow aplinkoje darbo eiga reiškia mazgų seką, kuri apdoroja įvestį ir generuoja išvestį. Vertinimo darbo eigos yra specialios darbo eigos, skirtos įvertinti vykdymo efektyvumą pagal konkrečius kriterijus ir tikslus.

**Pagrindinės vertinimo darbo eigų savybės**

Jos paprastai vykdomos po testuojamos darbo eigos, naudojant jos išvestis. Jos apskaičiuoja balus ar metrikas, kad įvertintų testuojamos darbo eigos efektyvumą. Metrikos gali apimti tikslumą, aktualumo balus ar kitus svarbius rodiklius.

### Vertinimo darbo eigų pritaikymas

**Įvesties apibrėžimas**

Vertinimo darbo eigos turi priimti testuojamos darbo eigos išvestis. Įvestis apibrėžkite panašiai kaip standartinėse darbo eigose.
Pavyzdžiui, jei vertinate klausimų ir atsakymų darbo eigą, įvestį pavadinkite „atsakymas“. Jei vertinate klasifikavimo darbo eigą, įvestį pavadinkite „kategorija“. Taip pat gali prireikti tikrų duomenų (pvz., faktinių etikečių).

**Išvestys ir metrikos**

Vertinimo darbo eigos generuoja rezultatus, kurie matuoja testuojamos darbo eigos efektyvumą. Metrikos gali būti apskaičiuojamos naudojant Python arba LLM (didelius kalbos modelius). Naudokite log_metric() funkciją, kad užregistruotumėte svarbias metrikas.

**Naudojant pritaikytas vertinimo darbo eigas**

Sukurkite savo vertinimo darbo eigą, pritaikytą jūsų specifinėms užduotims ir tikslams. Pritaikykite metrikas pagal savo vertinimo tikslus.
Taikykite šią pritaikytą vertinimo darbo eigą masinėms vykdymo sesijoms, skirtoms didelio masto testavimui.

## Įmontuoti vertinimo metodai

Prompt Flow taip pat siūlo įmontuotus vertinimo metodus.
Galite pateikti masines vykdymo sesijas ir naudoti šiuos metodus, kad įvertintumėte, kaip gerai jūsų darbo eiga veikia su dideliais duomenų rinkiniais.
Peržiūrėkite vertinimo rezultatus, palyginkite metrikas ir, jei reikia, atlikite iteracijas.
Atminkite, kad vertinimas yra būtinas, norint užtikrinti, kad jūsų dirbtinio intelekto modeliai atitiktų norimus kriterijus ir tikslus. Išsamias instrukcijas, kaip kurti ir naudoti vertinimo darbo eigas Microsoft Prompt Flow aplinkoje, rasite oficialioje dokumentacijoje.

Apibendrinant, Microsoft Prompt Flow suteikia kūrėjams galimybę kurti aukštos kokybės LLM programas, supaprastindamas užklausų kūrimą ir siūlydamas patikimą kūrimo aplinką. Jei dirbate su LLM, Prompt Flow yra vertingas įrankis, kurį verta išbandyti. Išsamias instrukcijas, kaip kurti ir naudoti vertinimo darbo eigas Microsoft Prompt Flow aplinkoje, rasite [Prompt Flow vertinimo dokumentuose](https://learn.microsoft.com/azure/machine-learning/prompt-flow/how-to-develop-an-evaluation-flow?view=azureml-api-2?WT.mc_id=aiml-138114-kinfeylo).

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.