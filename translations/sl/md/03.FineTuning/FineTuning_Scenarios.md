## Scenariji fino nastavitve

![FineTuning with MS Services](../../../../translated_images/sl/FinetuningwithMS.3d0cec8ae693e094.webp)

Ta razdelek ponuja pregled scenarijev fino nastavitve v okoljih Microsoft Foundry in Azure, vključno z modeli uvajanja, plastmi infrastrukture in pogosto uporabljenimi tehnikami optimizacije.

**Platforma**  
To vključuje upravljane storitve, kot so Microsoft Foundry (prej Microsoft Foundry) in Azure Machine Learning, ki zagotavljajo upravljanje modelov, orkestracijo, sledenje poskusom in delovne tokove uvajanja.

**Infrastruktura**  
Fino nastavljanje zahteva razširljive računske vire. V okoljih Azure to običajno vključuje virtualne stroje na osnovi GPU in CPU vire za lahke obremenitve, skupaj z razširljivo shrambo za podatkovne zbirke in kontrolne točke.

**Orodja in Okviri**  
Poteki dela fino nastavljanja se običajno zanašajo na okvire in optimizacijske knjižnice, kot so Hugging Face Transformers, DeepSpeed in PEFT (Parameter-Efficient Fine-Tuning).

Proces fino nastavljanja z Microsoftovimi tehnologijami zajema platformne storitve, računsko infrastrukturo in okvirje za učenje. Z razumevanjem, kako ti sestavni deli delujejo skupaj, lahko razvijalci učinkovito prilagodijo osnovne modele za specifične naloge in produkcijske scenarije.

## Model kot storitev

Fino nastavite model z uporabo gostovane fino nastavitve, brez potrebe po ustvarjanju in upravljanju računalnih virov.

![MaaS Fine Tuning](../../../../translated_images/sl/MaaSfinetune.3eee4630607aff0d.webp)

Brezstrežnično fino nastavljanje je zdaj na voljo za družine modelov Phi-3, Phi-3.5 in Phi-4, kar razvijalcem omogoča hitro in enostavno prilagajanje modelov za oblačne in robne scenarije, brez urejanja računalniških virov.

## Model kot platforma

Uporabniki upravljajo svoje računske vire, da lahko fino nastavijo svoje modele.

![Maap Fine Tuning](../../../../translated_images/sl/MaaPFinetune.fd3829c1122f5d1c.webp)

[Primer fino nastavitve](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Primerjava tehnik fino nastavitve

|Scenarij|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DoRA|
|---|---|---|---|---|---|---|
|Prilagajanje vnaprej naučenih LLM-jev za specifične naloge ali domene|Da|Da|Da|Da|Da|Da|
|Fino nastavljanje za NLP naloge, kot so klasifikacija besedil, prepoznavanje imenovanih entitet in strojni prevod|Da|Da|Da|Da|Da|Da|
|Fino nastavljanje za QA naloge|Da|Da|Da|Da|Da|Da|
|Fino nastavljanje za generiranje odzivov, ki so podobni človeškim, v klepetalnikih|Da|Da|Da|Da|Da|Da|
|Fino nastavljanje za generiranje glasbe, umetnosti ali drugih oblik ustvarjalnosti|Da|Da|Da|Da|Da|Da|
|Zmanjšanje računalniških in finančnih stroškov|Da|Da|Da|Da|Da|Da|
|Zmanjšanje porabe pomnilnika|Da|Da|Da|Da|Da|Da|
|Uporaba manjšega števila parametrov za učinkovito fino nastavljanje|Da|Da|Da|Ne|Ne|Da|
|Oblika pomnilniško učinkovite podatkovne paralelizacije, ki omogoča dostop do skupnega GPU pomnilnika vseh razpoložljivih GPU naprav|Ne|Ne|Ne|Da|Da|Ne|

> [!NOTE]
> LoRA, QLoRA, PEFT in DoRA so metode parametrično učinkovite fino nastavitve, medtem ko se DeepSpeed in ZeRO osredotočata na distribuirano učenje in optimizacijo pomnilnika.

## Primeri zmogljivosti fino nastavitve

![Finetuning Performance](../../../../translated_images/sl/Finetuningexamples.a9a41214f8f5afc1.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v izvorni jezik se šteje za avtoritativni vir. Za kritične informacije je priporočljiv strokoven človeški prevod. Nismo odgovorni za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->