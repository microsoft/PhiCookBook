<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cb5648935f63edc17e95ce38f23adc32",
  "translation_date": "2025-07-17T08:30:19+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Scenarios.md",
  "language_code": "ro"
}
-->
## Scenarii de Fine Tuning

![FineTuning cu Servicii MS](../../../../translated_images/FinetuningwithMS.3d0cec8ae693e094c38c72575e63f2c9bf1cf980ab90f1388e102709f9c979e5.ro.png)

**Platformă** Aceasta include diverse tehnologii precum Azure AI Foundry, Azure Machine Learning, AI Tools, Kaito și ONNX Runtime.

**Infrastructură** Aceasta include CPU și FPGA, care sunt esențiale pentru procesul de fine-tuning. Permiteți-mi să vă arăt pictogramele pentru fiecare dintre aceste tehnologii.

**Unelte & Framework** Aceasta include ONNX Runtime și ONNX Runtime. Permiteți-mi să vă arăt pictogramele pentru fiecare dintre aceste tehnologii.  
[Introduceți pictogramele pentru ONNX Runtime și ONNX Runtime]

Procesul de fine-tuning cu tehnologiile Microsoft implică diverse componente și unelte. Prin înțelegerea și utilizarea acestor tehnologii, putem ajusta eficient aplicațiile noastre și crea soluții mai bune.

## Model ca Serviciu

Fine-tunează modelul folosind fine-tuning găzduit, fără a fi nevoie să creezi și să gestionezi resurse de calcul.

![MaaS Fine Tuning](../../../../translated_images/MaaSfinetune.3eee4630607aff0d0a137b16ab79ec5977ece923cd1fdd89557a2655c632669d.ro.png)

Fine-tuning serverless este disponibil pentru modelele Phi-3-mini și Phi-3-medium, permițând dezvoltatorilor să personalizeze rapid și ușor modelele pentru scenarii cloud și edge, fără a fi nevoie să se ocupe de resursele de calcul. De asemenea, am anunțat că Phi-3-small este acum disponibil prin oferta noastră Models-as-a-Service, astfel încât dezvoltatorii să poată începe rapid și ușor dezvoltarea AI fără a gestiona infrastructura de bază.

## Model ca Platformă

Utilizatorii își gestionează propriile resurse de calcul pentru a-și fine-tune modelele.

![Maap Fine Tuning](../../../../translated_images/MaaPFinetune.fd3829c1122f5d1c4a6a91593ebc348548410e162acda34f18034384e3b3816a.ro.png)

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

![Performanță Fine Tuning](../../../../translated_images/Finetuningexamples.a9a41214f8f5afc186adb16a413b1c17e2f43a89933ba95feb5aee84b0b24add.ro.png)

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.