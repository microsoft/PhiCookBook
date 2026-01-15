<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "743d7e9cb9c4e8ea642d77bee657a7fa",
  "translation_date": "2025-07-17T10:01:58+00:00",
  "source_file": "md/03.FineTuning/LetPhi3gotoIndustriy.md",
  "language_code": "sl"
}
-->
# **Naj Phi-3 postane industrijski strokovnjak**

Da bi model Phi-3 uporabili v določeni industriji, morate modelu Phi-3 dodati poslovne podatke iz te industrije. Imamo dve različni možnosti: prva je RAG (Retrieval Augmented Generation), druga pa Fine Tuning.

## **RAG proti Fine-Tuning**

### **Retrieval Augmented Generation**

RAG je kombinacija iskanja podatkov in generiranja besedila. Strukturirani in nestrukturirani podatki podjetja so shranjeni v vektorski bazi podatkov. Pri iskanju relevantne vsebine se najde ustrezno povzetek in vsebina, ki tvorita kontekst, nato pa se združi zmožnost dopolnjevanja besedila LLM/SLM za generiranje vsebine.

### **Fine-tuning**

Fine-tuning temelji na izboljšavi določenega modela. Ni ga treba začeti z algoritmom modela, vendar je potrebno nenehno zbiranje podatkov. Če želite v industrijskih aplikacijah natančnejšo terminologijo in jezikovni izraz, je fine-tuning boljša izbira. Če pa se vaši podatki pogosto spreminjajo, je fine-tuning lahko zapleten.

### **Kako izbrati**

1. Če naš odgovor zahteva vključitev zunanjih podatkov, je RAG najboljša izbira.

2. Če potrebujete stabilno in natančno industrijsko znanje, bo fine-tuning dobra izbira. RAG daje prednost pridobivanju relevantne vsebine, vendar morda ne ujame vedno vseh specializiranih odtenkov.

3. Fine-tuning zahteva kakovosten nabor podatkov, pri majhnem obsegu podatkov pa ne bo prinesel velike razlike. RAG je bolj prilagodljiv.

4. Fine-tuning je črna skrinjica, metafizika, in je težko razumeti notranji mehanizem. RAG pa omogoča lažje iskanje izvora podatkov, s čimer učinkovito zmanjšuje halucinacije ali napake v vsebini ter zagotavlja boljšo preglednost.

### **Scenariji**

1. Vertikalne industrije, ki zahtevajo specifično strokovno besedišče in izraze, bodo imele ***Fine-tuning*** kot najboljšo izbiro.

2. QA sistem, ki vključuje sintezo različnih znanj, bo imel ***RAG*** kot najboljšo izbiro.

3. Kombinacija avtomatiziranega poslovnega toka je najbolje rešena z ***RAG + Fine-tuning***.

## **Kako uporabljati RAG**

![rag](../../../../translated_images/sl/rag.2014adc59e6f6007.png)

Vektorska baza podatkov je zbirka podatkov, shranjenih v matematični obliki. Vektorske baze podatkov olajšajo modelom strojnega učenja, da si zapomnijo prejšnje vnose, kar omogoča uporabo strojnega učenja za podporo primerom, kot so iskanje, priporočila in generiranje besedila. Podatke je mogoče prepoznati na podlagi meril podobnosti, ne le natančnih ujemanj, kar računalniškim modelom omogoča razumevanje konteksta podatkov.

Vektorska baza podatkov je ključ do uresničitve RAG. Podatke lahko pretvorimo v vektorsko shrambo preko vektorskih modelov, kot so text-embedding-3, jina-ai-embedding itd.

Več o ustvarjanju RAG aplikacije si oglejte na [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?WT.mc_id=aiml-138114-kinfeylo)

## **Kako uporabljati Fine-tuning**

Pogosto uporabljeni algoritmi pri Fine-tuningu so Lora in QLora. Kako izbrati?
- [Več informacij v tem vzorčnem zvezku](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Primer Python FineTuning vzorca](../../../../code/04.Finetuning/FineTrainingScript.py)

### **Lora in QLora**

![lora](../../../../translated_images/sl/qlora.e6446c988ee04ca0.png)

LoRA (Low-Rank Adaptation) in QLoRA (Quantized Low-Rank Adaptation) sta tehniki za fine-tuning velikih jezikovnih modelov (LLM) z uporabo Parameter Efficient Fine Tuning (PEFT). PEFT tehnike so zasnovane za učinkovitejše treniranje modelov kot tradicionalne metode.  
LoRA je samostojna tehnika fine-tuninga, ki zmanjša porabo pomnilnika z uporabo nizkorangske aproksimacije matrike posodobitev uteži. Omogoča hitro treniranje in ohranja zmogljivost blizu tradicionalnim metodam fine-tuninga.

QLoRA je razširjena različica LoRA, ki vključuje kvantizacijske tehnike za nadaljnjo zmanjšanje porabe pomnilnika. QLoRA kvantizira natančnost uteži v predhodno usposobljenem LLM na 4-bitno natančnost, kar je bolj učinkovito glede pomnilnika kot LoRA. Vendar je treniranje QLoRA približno 30 % počasnejše kot pri LoRA zaradi dodatnih korakov kvantizacije in dekvantizacije.

QLoRA uporablja LoRA kot pripomoček za odpravo napak, ki nastanejo zaradi kvantizacijskih napak. QLoRA omogoča fine-tuning ogromnih modelov z milijardami parametrov na relativno majhnih, široko dostopnih GPU-jih. Na primer, QLoRA lahko fine-tunira model s 70 milijardami parametrov, ki sicer zahteva 36 GPU-jev, z le 2.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.