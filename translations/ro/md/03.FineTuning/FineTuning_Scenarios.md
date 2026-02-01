## Scenarii de Fine Tuning

![FineTuning cu Servicii MS](../../../../translated_images/ro/FinetuningwithMS.3d0cec8ae693e094.webp)

**Platformă** Aceasta include diverse tehnologii precum Azure AI Foundry, Azure Machine Learning, AI Tools, Kaito și ONNX Runtime.

**Infrastructură** Aceasta include CPU și FPGA, care sunt esențiale pentru procesul de fine-tuning. Permiteți-mi să vă arăt pictogramele pentru fiecare dintre aceste tehnologii.

**Unelte & Framework** Aceasta include ONNX Runtime și ONNX Runtime. Permiteți-mi să vă arăt pictogramele pentru fiecare dintre aceste tehnologii.  
[Introduceți pictogramele pentru ONNX Runtime și ONNX Runtime]

Procesul de fine-tuning cu tehnologiile Microsoft implică diverse componente și unelte. Prin înțelegerea și utilizarea acestor tehnologii, putem ajusta eficient aplicațiile noastre și crea soluții mai bune.

## Model ca Serviciu

Fine-tunează modelul folosind fine-tuning găzduit, fără a fi nevoie să creezi și să gestionezi resurse de calcul.

![MaaS Fine Tuning](../../../../translated_images/ro/MaaSfinetune.3eee4630607aff0d.webp)

Fine-tuning serverless este disponibil pentru modelele Phi-3-mini și Phi-3-medium, permițând dezvoltatorilor să personalizeze rapid și ușor modelele pentru scenarii cloud și edge, fără a fi nevoie să se ocupe de resursele de calcul. De asemenea, am anunțat că Phi-3-small este acum disponibil prin oferta noastră Models-as-a-Service, astfel încât dezvoltatorii să poată începe rapid și ușor dezvoltarea AI fără a gestiona infrastructura de bază.

## Model ca Platformă

Utilizatorii își gestionează propriile resurse de calcul pentru a-și fine-tune modelele.

![Maap Fine Tuning](../../../../translated_images/ro/MaaPFinetune.fd3829c1122f5d1c.webp)

[Exemplu Fine Tuning](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Scenarii de Fine Tuning

| | | | | | | |
|-|-|-|-|-|-|-|
|Scenariu|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DORA|
|Adaptarea LLM-urilor pre-antrenate la sarcini sau domenii specifice|Da|Da|Da|Da|Da|Da|
|Fine-tuning pentru sarcini NLP precum clasificarea textului, recunoașterea entităților numite și traducerea automată|Da|Da|Da|Da|Da|Da|
|Fine-tuning pentru sarcini de QA|Da|Da|Da|Da|Da|Da|
|Fine-tuning pentru generarea de răspunsuri asemănătoare celor umane în chatbots|Da|Da|Da|Da|Da|Da|
|Fine-tuning pentru generarea de muzică, artă sau alte forme de creativitate|Da|Da|Da|Da|Da|Da|
|Reducerea costurilor computaționale și financiare|Da|Da|Nu|Da|Da|Nu|
|Reducerea utilizării memoriei|Nu|Da|Nu|Da|Da|Da|
|Folosirea unui număr mai mic de parametri pentru fine-tuning eficient|Nu|Da|Da|Nu|Nu|Da|
|Formă eficientă din punct de vedere al memoriei de paralelism de date care oferă acces la memoria GPU agregată a tuturor dispozitivelor GPU disponibile|Nu|Nu|Nu|Da|Da|Da|

## Exemple de Performanță în Fine Tuning

![Performanță Fine Tuning](../../../../translated_images/ro/Finetuningexamples.a9a41214f8f5afc1.webp)

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.