## Scenariji za fino podešavanje

![FineTuning with MS Services](../../../../translated_images/hr/FinetuningwithMS.3d0cec8ae693e094.webp)

Ovaj odjeljak pruža pregled scenarija finog podešavanja u Microsoft Foundry i Azure okruženjima, uključujući modele rasporeda, slojeve infrastrukture i često korištene tehnike optimizacije.

**Platforma**  
Obuhvaća upravljane usluge kao što su Microsoft Foundry (ranije Microsoft Foundry) i Azure Machine Learning, koje pružaju upravljanje modelima, orkestraciju, praćenje eksperimenata i tijekove rada rasporeda.

**Infrastruktura**  
Fino podešavanje zahtijeva skalabilne računske resurse. U Azure okruženjima to obično uključuje virtualne strojeve s GPU-om i CPU resurse za lakše radne opterećenja, zajedno sa skalabilnom pohranom za skupove podataka i kontrolne točke.

**Alati i okviri**  
Tijekovi rada finog podešavanja često se oslanjaju na okvire i biblioteke za optimizaciju kao što su Hugging Face Transformers, DeepSpeed i PEFT (Parameter-Efficient Fine-Tuning).

Proces finog podešavanja uz Microsoft tehnologije obuhvaća platformne usluge, računalnu infrastrukturu i okvire za treniranje. Razumijevanjem načina na koji ti dijelovi surađuju, programeri mogu učinkovito prilagoditi osnovne modele za specifične zadatke i produkcijske scenarije.

## Model kao usluga

Fino podesite model koristeći hostano fino podešavanje, bez potrebe za kreiranjem i upravljanjem računalnim resursima.

![MaaS Fine Tuning](../../../../translated_images/hr/MaaSfinetune.3eee4630607aff0d.webp)

Serverless fino podešavanje sada je dostupno za Phi-3, Phi-3.5 i Phi-4 obitelji modela, omogućujući programerima brzo i jednostavno prilagođavanje modela za cloud i edge scenarije bez potrebe za organiziranjem računalnih resursa.

## Model kao platforma

Korisnici upravljaju vlastitim računalnim resursima kako bi fino podesili svoje modele.

![Maap Fine Tuning](../../../../translated_images/hr/MaaPFinetune.fd3829c1122f5d1c.webp)

[Primjer finog podešavanja](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Usporedba tehnika finog podešavanja

|Scenarij|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DoRA|
|---|---|---|---|---|---|---|
|Prilagodba prethodno treniranih LLM-ova za specifične zadatke ili domene|Da|Da|Da|Da|Da|Da|
|Fino podešavanje za NLP zadatke kao što su klasifikacija teksta, prepoznavanje imenovanih entiteta i strojno prevođenje|Da|Da|Da|Da|Da|Da|
|Fino podešavanje za QA zadatke|Da|Da|Da|Da|Da|Da|
|Fino podešavanje za generiranje ljudskih odgovora u chatbotovima|Da|Da|Da|Da|Da|Da|
|Fino podešavanje za generiranje glazbe, umjetnosti ili drugih oblika kreativnosti|Da|Da|Da|Da|Da|Da|
|Smanjenje računalnih i financijskih troškova|Da|Da|Da|Da|Da|Da|
|Smanjenje upotrebe memorije|Da|Da|Da|Da|Da|Da|
|Korištenje manje parametara za učinkovito fino podešavanje|Da|Da|Da|Ne|Ne|Da|
|Memorijski učinkoviti oblik paralelizma podataka koji omogućuje pristup ukupnoj GPU memoriji svih dostupnih GPU uređaja|Ne|Ne|Ne|Da|Da|Ne|

> [!NOTE]
> LoRA, QLoRA, PEFT i DoRA su metode finog podešavanja koje su učinkovite u pogledu parametara, dok se DeepSpeed i ZeRO fokusiraju na distribuirano treniranje i optimizaciju memorije.

## Primjeri performansi finog podešavanja

![Finetuning Performance](../../../../translated_images/hr/Finetuningexamples.a9a41214f8f5afc1.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo biti točni, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili krive tumačenja proizašla iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->