## Scenarii de Ajustare Fină

![FineTuning with MS Services](../../../../translated_images/ro/FinetuningwithMS.3d0cec8ae693e094.webp)

Această secțiune oferă o prezentare generală a scenariilor de ajustare fină în mediile Microsoft Foundry și Azure, incluzând modele de implementare, straturi de infrastructură și tehnici comune de optimizare.

**Platformă**  
Aceasta include servicii gestionate precum Microsoft Foundry (fost Microsoft Foundry) și Azure Machine Learning, care oferă gestionarea modelelor, orchestrare, urmărirea experimentelor și fluxuri de lucru pentru implementare.

**Infrastructură**  
Ajustarea fină necesită resurse de calcul scalabile. În mediile Azure, acestea includ de obicei mașini virtuale bazate pe GPU și resurse CPU pentru sarcini ușoare, alături de stocare scalabilă pentru seturi de date și puncte de verificare.

**Unelte & Cadru**  
Fluxurile de lucru pentru ajustarea fină se bazează de obicei pe cadre și biblioteci de optimizare precum Hugging Face Transformers, DeepSpeed și PEFT (Parameter-Efficient Fine-Tuning).

Procesul de ajustare fină cu tehnologiile Microsoft acoperă servicii de platformă, infrastructură de calcul și cadre de antrenament. Prin înțelegerea modului în care aceste componente funcționează împreună, dezvoltatorii pot adapta eficient modelele fundamentale pentru sarcini specifice și scenarii de producție.

## Model ca Serviciu

Ajustați modelul folosind ajustarea fină găzduită, fără a fi nevoie să creați și să gestionați resurse de calcul.

![MaaS Fine Tuning](../../../../translated_images/ro/MaaSfinetune.3eee4630607aff0d.webp)

Ajustarea fină serverless este acum disponibilă pentru familiile de modele Phi-3, Phi-3.5 și Phi-4, permițând dezvoltatorilor să personalizeze rapid și ușor modelele pentru scenarii cloud și edge fără a se ocupa de resursele de calcul.

## Model ca Platformă

Utilizatorii își gestionează propriile resurse de calcul pentru a-și ajusta fin modelele.

![Maap Fine Tuning](../../../../translated_images/ro/MaaPFinetune.fd3829c1122f5d1c.webp)

[Exemplu de Ajustare Fină](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Compararea Tehnicilor de Ajustare Fină

|Scenariu|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DoRA|
|---|---|---|---|---|---|---|
|Adaptarea LLM-urilor pre-antrenate pentru sarcini sau domenii specifice|Da|Da|Da|Da|Da|Da|
|Ajustare fină pentru sarcini NLP precum clasificare text, recunoaștere entități denumite și traducere automată|Da|Da|Da|Da|Da|Da|
|Ajustare fină pentru sarcini de QA|Da|Da|Da|Da|Da|Da|
|Ajustare fină pentru generarea de răspunsuri asemănătoare omului în chatbot-uri|Da|Da|Da|Da|Da|Da|
|Ajustare fină pentru generarea de muzică, artă sau alte forme de creativitate|Da|Da|Da|Da|Da|Da|
|Reducerea costurilor computaționale și financiare|Da|Da|Da|Da|Da|Da|
|Reducerea consumului de memorie|Da|Da|Da|Da|Da|Da|
|Utilizarea unui număr redus de parametri pentru ajustare eficientă|Da|Da|Da|Nu|Nu|Da|
|Formă eficientă de paralelism pe memorie care oferă acces la memoria GPU agregată a tuturor dispozitivelor GPU disponibile|Nu|Nu|Nu|Da|Da|Nu|

> [!NOTE]
> LoRA, QLoRA, PEFT și DoRA sunt metode de ajustare fină eficiente din punct de vedere al parametrilor, în timp ce DeepSpeed și ZeRO se concentrează pe antrenament distribuit și optimizarea memoriei.

## Exemple de Performanță a Ajustării Fine

![Finetuning Performance](../../../../translated_images/ro/Finetuningexamples.a9a41214f8f5afc1.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională umană. Nu ne asumăm responsabilitatea pentru orice neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->