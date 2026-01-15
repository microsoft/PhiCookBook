<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7fe541373802e33568e94e13226d463c",
  "translation_date": "2025-07-17T09:49:16+00:00",
  "source_file": "md/03.FineTuning/Introduce_AzureML.md",
  "language_code": "sl"
}
-->
# **Predstavitev storitve Azure Machine Learning**

[Azure Machine Learning](https://ml.azure.com?WT.mc_id=aiml-138114-kinfeylo) je oblačna storitev za pospeševanje in upravljanje življenjskega cikla projektov strojnega učenja (ML).

Strokovnjaki za ML, podatkovni znanstveniki in inženirji jo lahko uporabljajo v svojih vsakodnevnih delovnih procesih za:

- Učenje in uvajanje modelov.  
- Upravljanje operacij strojnega učenja (MLOps).  
- Ustvarite lahko model v Azure Machine Learning ali uporabite model, zgrajen na odprtokodni platformi, kot so PyTorch, TensorFlow ali scikit-learn.  
- Orodja MLOps vam pomagajo spremljati, ponovno usposobiti in ponovno uvajati modele.

## Za koga je Azure Machine Learning?

**Podatkovni znanstveniki in ML inženirji**

Lahko uporabljajo orodja za pospešitev in avtomatizacijo svojih vsakodnevnih delovnih procesov.  
Azure ML ponuja funkcije za pravičnost, razložljivost, sledenje in revizijsko sledljivost.

**Razvijalci aplikacij:**  
Lahko brez težav integrirajo modele v aplikacije ali storitve.

**Razvijalci platform**

Imajo dostop do robustnega nabora orodij, podprtih z zanesljivimi Azure Resource Manager API-ji.  
Ta orodja omogočajo gradnjo naprednih ML orodij.

**Podjetja**

Z delom v Microsoft Azure oblaku podjetja izkoristijo znano varnost in nadzor dostopa na podlagi vlog.  
Nastavijo lahko projekte za nadzor dostopa do zaščitenih podatkov in določenih operacij.

## Produktivnost za celotno ekipo  
Projekti ML pogosto zahtevajo ekipo z raznolikimi znanji za gradnjo in vzdrževanje.

Azure ML ponuja orodja, ki omogočajo:  
- Sodelovanje z ekipo prek skupnih zvezkov, računalniških virov, strežniško brezplačnih računalniških zmogljivosti, podatkov in okolij.  
- Razvijanje modelov s poudarkom na pravičnosti, razložljivosti, sledenju in revizijski sledljivosti za izpolnjevanje zahtev glede izvora in skladnosti.  
- Hitro in enostavno uvajanje ML modelov v obsegu ter učinkovito upravljanje in nadzor z MLOps.  
- Izvajanje del strojnega učenja kjerkoli z vgrajenim upravljanjem, varnostjo in skladnostjo.

## Orodja, združljiva med platformami

Vsak član ML ekipe lahko uporablja svoja priljubljena orodja za opravljanje dela.  
Ne glede na to, ali izvajate hitre eksperimente, prilagajate hiperparametre, gradite cevovode ali upravljate sklepe, lahko uporabljate znane vmesnike, kot so:  
- Azure Machine Learning Studio  
- Python SDK (v2)  
- Azure CLI (v2)  
- Azure Resource Manager REST API-ji

Med izboljševanjem modelov in sodelovanjem skozi razvojni cikel lahko v uporabniškem vmesniku Azure Machine Learning studia delite in najdete vire, sredstva in metrike.

## **LLM/SLM v Azure ML**

Azure ML je dodal številne funkcije, povezane z LLM/SLM, ki združujejo LLMOps in SLMOps za ustvarjanje generativne umetne inteligence na ravni celotnega podjetja.

### **Katalog modelov**

Uporabniki v podjetjih lahko prek Kataloga modelov uvajajo različne modele glede na različne poslovne scenarije in nudijo storitve kot Model kot storitev za dostop razvijalcev ali uporabnikov v podjetju.

![models](../../../../translated_images/sl/models.e6c7ff50a51806fd.png)

Katalog modelov v Azure Machine Learning studiu je središče za odkrivanje in uporabo širokega nabora modelov, ki omogočajo gradnjo generativnih AI aplikacij. Katalog modelov vsebuje stotine modelov različnih ponudnikov, kot so Azure OpenAI service, Mistral, Meta, Cohere, Nvidia, Hugging Face, vključno z modeli, ki jih je usposobil Microsoft. Modeli ponudnikov, ki niso Microsoftovi, so Ne-Microsoftovi izdelki, kot je določeno v Microsoftovih pogojih za izdelke, in so predmet pogojev, priloženih modelu.

### **Cevovod opravil**

Jedro cevovoda strojnega učenja je razdelitev celotne naloge strojnega učenja na večstopenjski delovni tok. Vsak korak je obvladljiva komponenta, ki jo je mogoče razvijati, optimizirati, konfigurirati in avtomatizirati posamično. Koraki so povezani z jasno določenimi vmesniki. Storitev cevovoda Azure Machine Learning samodejno usklajuje vse odvisnosti med koraki cevovoda.

Pri fino nastavitvi SLM / LLM lahko upravljamo naše podatke, učenje in procese generiranja prek cevovoda.

![finetuning](../../../../translated_images/sl/finetuning.6559da198851fa52.png)

### **Prompt flow**

Prednosti uporabe Azure Machine Learning prompt flow  
Azure Machine Learning prompt flow ponuja vrsto prednosti, ki uporabnikom pomagajo preiti od ideje do eksperimentiranja in na koncu do proizvodno pripravljenih aplikacij na osnovi LLM:

**Agilnost pri oblikovanju pozivov**

Interaktivna izkušnja ustvarjanja: Azure Machine Learning prompt flow prikazuje vizualno strukturo toka, kar uporabnikom omogoča enostavno razumevanje in navigacijo po projektih. Prav tako ponuja izkušnjo kodiranja, podobno zvezku, za učinkovito razvoj in odpravljanje napak toka.  
Variantnost za prilagajanje pozivov: Uporabniki lahko ustvarijo in primerjajo več različic pozivov, kar omogoča iterativno izboljševanje.

Vrednotenje: Vgrajeni tokovi za vrednotenje omogočajo uporabnikom oceno kakovosti in učinkovitosti njihovih pozivov in tokov.

Obsežni viri: Azure Machine Learning prompt flow vključuje knjižnico vgrajenih orodij, vzorcev in predlog, ki služijo kot izhodišče za razvoj, spodbujajo ustvarjalnost in pospešujejo proces.

**Pripravljenost za podjetja pri aplikacijah na osnovi LLM**

Sodelovanje: Azure Machine Learning prompt flow podpira timsko sodelovanje, kar omogoča več uporabnikom, da skupaj delajo na projektih oblikovanja pozivov, delijo znanje in vzdržujejo nadzor različic.

Vse-v-enem platforma: Azure Machine Learning prompt flow poenostavlja celoten proces oblikovanja pozivov, od razvoja in vrednotenja do uvajanja in spremljanja. Uporabniki lahko brez težav uvajajo svoje tokove kot Azure Machine Learning končne točke in spremljajo njihovo delovanje v realnem času, kar zagotavlja optimalno delovanje in stalne izboljšave.

Rešitve Azure Machine Learning za pripravljenost podjetij: Prompt flow izkorišča robustne rešitve Azure Machine Learning za pripravljenost podjetij, ki zagotavljajo varno, razširljivo in zanesljivo osnovo za razvoj, eksperimentiranje in uvajanje tokov.

Z Azure Machine Learning prompt flow lahko uporabniki izkoristijo agilnost pri oblikovanju pozivov, učinkovito sodelujejo in uporabljajo rešitve na ravni podjetij za uspešen razvoj in uvajanje aplikacij na osnovi LLM.

S kombinacijo računalniške moči, podatkov in različnih komponent Azure ML lahko razvijalci v podjetjih enostavno zgradijo svoje lastne aplikacije umetne inteligence.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.