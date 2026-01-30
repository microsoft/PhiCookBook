# **Azure Machine Learning teenuse tutvustus**

[Azure Machine Learning](https://ml.azure.com?WT.mc_id=aiml-138114-kinfeylo) on pilveteenus, mis kiirendab ja haldab masinõppe (ML) projektide elutsüklit.

ML spetsialistid, andmeteadlased ja insenerid saavad seda kasutada igapäevastes töövoogudes, et:

- Treenida ja juurutada mudeleid.
- Hallata masinõppe operatsioone (MLOps).
- Mudeli saab luua Azure Machine Learningis või kasutada avatud lähtekoodiga platvormil, nagu PyTorch, TensorFlow või scikit-learn, loodud mudelit.
- MLOps tööriistad aitavad mudeleid jälgida, uuesti treenida ja uuesti juurutada.

## Kellele on Azure Machine Learning mõeldud?

**Andmeteadlased ja ML insenerid**

Nad saavad kasutada tööriistu, et kiirendada ja automatiseerida igapäevaseid töövooge.  
Azure ML pakub funktsioone, nagu õiglus, selgitatavus, jälgimine ja auditeeritavus.  

**Rakenduste arendajad**

Nad saavad integreerida mudeleid rakendustesse või teenustesse sujuvalt.

**Platvormi arendajad**

Neil on juurdepääs vastupidavatele tööriistadele, mida toetavad Azure Resource Manager API-d.  
Need tööriistad võimaldavad luua täiustatud ML tööriistu.

**Ettevõtted**

Töötades Microsoft Azure pilves, saavad ettevõtted kasu tuttavast turvalisusest ja rollipõhisest juurdepääsu kontrollist.  
Projektide seadistamine võimaldab kontrollida juurdepääsu kaitstud andmetele ja konkreetsetele toimingutele.

## Tootlikkus kogu meeskonnale

ML projektid nõuavad sageli meeskonda, kellel on mitmekesine oskuste komplekt, et projekte luua ja hallata.

Azure ML pakub tööriistu, mis võimaldavad:
- Teha koostööd meeskonnaga jagatud märkmike, arvutusressursside, serverivaba arvutuse, andmete ja keskkondade kaudu.
- Arendada mudeleid, mis vastavad õigluse, selgitatavuse, jälgitavuse ja auditeeritavuse nõuetele, et täita päritolu ja auditi nõudeid.
- Juurutada ML mudeleid kiiresti ja lihtsalt suuremahuliselt ning hallata ja juhtida neid tõhusalt MLOps abil.
- Käitada masinõppe töökoormusi kõikjal, kasutades sisseehitatud juhtimist, turvalisust ja vastavust.

## Platvormi tööriistade ühilduvus

Iga ML meeskonna liige saab kasutada oma eelistatud tööriistu, et töö tehtud saada.  
Olgu tegemist kiirete katsetuste, hüperparameetrite häälestamise, torujuhtmete loomise või järelduste haldamisega, saab kasutada tuttavaid liideseid, sealhulgas:
- Azure Machine Learning Studio
- Python SDK (v2)
- Azure CLI (v2)
- Azure Resource Manager REST API-d

Mudelite täiustamise ja arendustsükli jooksul koostööd tehes saate jagada ja leida ressursse, andmeid ja mõõdikuid Azure Machine Learning Studio kasutajaliideses.

## **LLM/SLM Azure ML-is**

Azure ML on lisanud palju LLM/SLM-ga seotud funktsioone, kombineerides LLMOps-i ja SLMOps-i, et luua ettevõtte tasemel generatiivse tehisintellekti tehnoloogiaplatvorm.

### **Mudelikataloog**

Ettevõtte kasutajad saavad juurutada erinevaid mudeleid vastavalt erinevatele äristsenaariumidele Mudelikataloogi kaudu ning pakkuda teenuseid mudelina teenusena (Model as Service), et ettevõtte arendajad või kasutajad saaksid neile juurde pääseda.

![mudelid](../../../../imgs/03/ft/models.png)

Azure Machine Learning Studio mudelikataloog on keskus, kus avastada ja kasutada laia valikut mudeleid, mis võimaldavad luua generatiivse tehisintellekti rakendusi. Mudelikataloog sisaldab sadu mudeleid erinevatelt mudelipakkujatelt, nagu Azure OpenAI teenus, Mistral, Meta, Cohere, Nvidia, Hugging Face, sealhulgas Microsofti treenitud mudelid. Mudelid, mis pärinevad Microsoftist erinevatelt pakkujatelt, on Microsofti toodete tingimuste kohaselt määratletud kui mitte-Microsofti tooted ja nende suhtes kehtivad mudeliga kaasnevad tingimused.

### **Töövoo torujuhe**

Masinõppe torujuhtme tuumaks on jagada täielik masinõppe ülesanne mitmeastmeliseks töövooks. Iga samm on hallatav komponent, mida saab eraldi arendada, optimeerida, konfigureerida ja automatiseerida. Sammud on ühendatud hästi määratletud liideste kaudu. Azure Machine Learning torujuhtme teenus korraldab automaatselt kõik torujuhtme sammude vahelised sõltuvused.

SLM / LLM peenhäälestamisel saame hallata oma andmeid, treenimis- ja genereerimisprotsesse torujuhtme kaudu.

![peenhäälestamine](../../../../imgs/03/ft/finetuning.png)

### **Prompt flow**

Azure Machine Learning prompt flow kasutamise eelised  
Azure Machine Learning prompt flow pakub mitmeid eeliseid, mis aitavad kasutajatel liikuda ideest katsetamiseni ja lõpuks tootmisvalmis LLM-põhiste rakendusteni:

**Prompt'i insenerimise paindlikkus**

Interaktiivne autorikogemus: Azure Machine Learning prompt flow pakub visuaalset esitust töövoo struktuurist, võimaldades kasutajatel oma projekte hõlpsalt mõista ja navigeerida. Samuti pakub see märkmikulaadset kodeerimiskogemust tõhusaks töövoo arendamiseks ja silumiseks.  
Variantide loomine prompt'i häälestamiseks: Kasutajad saavad luua ja võrrelda mitmeid prompt'i variante, hõlbustades iteratiivset täiustamisprotsessi.

Hindamine: Sisseehitatud hindamisvood võimaldavad kasutajatel hinnata oma prompt'ide ja töövoogude kvaliteeti ja tõhusust.

Ulatuslikud ressursid: Azure Machine Learning prompt flow sisaldab sisseehitatud tööriistade, näidete ja mallide raamatukogu, mis toimib arenduse lähtepunktina, inspireerides loovust ja kiirendades protsessi.

**Ettevõtte valmisolek LLM-põhiste rakenduste jaoks**

Koostöö: Azure Machine Learning prompt flow toetab meeskonnatööd, võimaldades mitmel kasutajal koos töötada prompt'i insenerimise projektide kallal, jagada teadmisi ja säilitada versioonikontrolli.

Kõik-ühes platvorm: Azure Machine Learning prompt flow sujuvdab kogu prompt'i insenerimise protsessi, alates arendamisest ja hindamisest kuni juurutamise ja jälgimiseni. Kasutajad saavad oma töövood hõlpsalt juurutada Azure Machine Learningi lõpp-punktidena ja jälgida nende jõudlust reaalajas, tagades optimaalse toimimise ja pideva täiustamise.

Azure Machine Learningi ettevõtte valmisoleku lahendused: Prompt flow kasutab ära Azure Machine Learningi vastupidavaid ettevõtte valmisoleku lahendusi, pakkudes turvalist, skaleeritavat ja usaldusväärset alust töövoogude arendamiseks, katsetamiseks ja juurutamiseks.

Azure Machine Learning prompt flow abil saavad kasutajad maksimeerida oma prompt'i insenerimise paindlikkust, teha tõhusalt koostööd ja kasutada ettevõtte tasemel lahendusi edukaks LLM-põhiste rakenduste arendamiseks ja juurutamiseks.

Kombineerides Azure ML-i arvutusvõimsust, andmeid ja erinevaid komponente, saavad ettevõtte arendajad hõlpsasti luua oma tehisintellekti rakendusi.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.