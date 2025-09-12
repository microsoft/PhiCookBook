<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7fe541373802e33568e94e13226d463c",
  "translation_date": "2025-09-12T14:46:26+00:00",
  "source_file": "md/03.FineTuning/Introduce_AzureML.md",
  "language_code": "lt"
}
-->
# **Azure Machine Learning paslaugos pristatymas**

[Azure Machine Learning](https://ml.azure.com?WT.mc_id=aiml-138114-kinfeylo) yra debesų paslauga, skirta paspartinti ir valdyti mašininio mokymosi (ML) projektų gyvavimo ciklą.

ML specialistai, duomenų mokslininkai ir inžinieriai gali ją naudoti kasdieniuose darbo procesuose:

- Modelių mokymui ir diegimui.
- Mašininio mokymosi operacijų (MLOps) valdymui.
- Galite sukurti modelį Azure Machine Learning arba naudoti modelį, sukurtą naudojant atvirojo kodo platformą, tokią kaip PyTorch, TensorFlow ar scikit-learn.
- MLOps įrankiai padeda stebėti, pertreniruoti ir iš naujo diegti modelius.

## Kam skirta Azure Machine Learning?

**Duomenų mokslininkams ir ML inžinieriams**

Jie gali naudoti įrankius, kad paspartintų ir automatizuotų kasdienius darbo procesus.  
Azure ML siūlo funkcijas, susijusias su sąžiningumu, paaiškinamumu, stebėjimu ir auditu.  

**Programų kūrėjai**

Jie gali lengvai integruoti modelius į programas ar paslaugas.

**Platformų kūrėjai**

Jie turi prieigą prie patikimų įrankių, paremtų tvirtais Azure Resource Manager API.  
Šie įrankiai leidžia kurti pažangius ML įrankius.

**Įmonės**

Dirbdamos Microsoft Azure debesyje, įmonės gauna naudos iš pažįstamos saugumo ir vaidmenimis pagrįstos prieigos kontrolės.  
Projektus galima nustatyti taip, kad būtų kontroliuojama prieiga prie saugomų duomenų ir specifinių operacijų.

## Produktyvumas visai komandai

ML projektams dažnai reikia komandos, turinčios įvairių įgūdžių, kad galėtų juos kurti ir palaikyti.

Azure ML siūlo įrankius, kurie leidžia:
- Bendradarbiauti su komanda naudojant bendrus užrašų knygeles, skaičiavimo išteklius, serverless skaičiavimą, duomenis ir aplinkas.
- Kurti modelius su sąžiningumu, paaiškinamumu, stebėjimu ir auditu, kad būtų įvykdyti kilmės ir audito atitikties reikalavimai.
- Greitai ir lengvai diegti ML modelius dideliu mastu bei efektyviai juos valdyti ir prižiūrėti naudojant MLOps.
- Vykdyti mašininio mokymosi užduotis bet kur, naudojant integruotą valdymą, saugumą ir atitiktį.

## Suderinami platformos įrankiai

Kiekvienas ML komandos narys gali naudoti savo mėgstamus įrankius darbui atlikti.  
Nesvarbu, ar vykdote greitus eksperimentus, hiperparametrų derinimą, kuriate procesus ar valdote prognozes, galite naudoti pažįstamas sąsajas, tokias kaip:
- Azure Machine Learning Studio
- Python SDK (v2)
- Azure CLI (v2)
- Azure Resource Manager REST API

Tobulindami modelius ir bendradarbiaudami viso kūrimo ciklo metu, galite dalintis ir rasti išteklius, resursus bei metrikas Azure Machine Learning studijos sąsajoje.

## **LLM/SLM Azure ML**

Azure ML pridėjo daugybę funkcijų, susijusių su LLM/SLM, sujungdama LLMOps ir SLMOps, kad sukurtų įmonės masto generatyvinės dirbtinio intelekto technologijų platformą.

### **Modelių katalogas**

Įmonių vartotojai gali diegti skirtingus modelius pagal skirtingus verslo scenarijus per Modelių katalogą ir teikti paslaugas kaip Model as Service, kad įmonių kūrėjai ar vartotojai galėtų juos pasiekti.

![modeliai](../../../../imgs/03/ft/models.png)

Modelių katalogas Azure Machine Learning studijoje yra centras, kuriame galima atrasti ir naudoti įvairius modelius, leidžiančius kurti generatyvinio dirbtinio intelekto programas. Modelių kataloge yra šimtai modelių iš tokių tiekėjų kaip Azure OpenAI service, Mistral, Meta, Cohere, Nvidia, Hugging Face, įskaitant Microsoft apmokytus modelius. Modeliai iš kitų tiekėjų nei Microsoft yra ne Microsoft produktai, kaip apibrėžta Microsoft produktų sąlygose, ir jiems taikomos sąlygos, pateiktos kartu su modeliu.

### **Užduočių procesai**

Mašininio mokymosi proceso esmė yra suskaidyti visą mašininio mokymosi užduotį į daugiapakopį darbo eigą. Kiekvienas žingsnis yra valdomas komponentas, kurį galima atskirai kurti, optimizuoti, konfigūruoti ir automatizuoti. Žingsniai yra sujungti per aiškiai apibrėžtas sąsajas. Azure Machine Learning proceso paslauga automatiškai koordinuoja visus priklausomybes tarp proceso žingsnių.

Finuodami SLM / LLM, galime valdyti savo duomenis, mokymo ir generavimo procesus per procesus.

![finetuning](../../../../imgs/03/ft/finetuning.png)

### **Prompt flow**

Privalumai naudojant Azure Machine Learning prompt flow  
Azure Machine Learning prompt flow siūlo daugybę privalumų, kurie padeda vartotojams pereiti nuo idėjų generavimo iki eksperimentavimo ir galiausiai iki gamybai paruoštų LLM pagrįstų programų:

**Prompt inžinerijos lankstumas**

Interaktyvi kūrimo patirtis: Azure Machine Learning prompt flow suteikia vizualinį srauto struktūros atvaizdavimą, leidžiantį vartotojams lengvai suprasti ir naršyti savo projektus. Taip pat siūlo užrašų knygelės tipo kodavimo patirtį efektyviam srauto kūrimui ir derinimui.  
Variantai prompt derinimui: Vartotojai gali kurti ir palyginti kelis prompt variantus, palengvinant iteracinį tobulinimo procesą.

Vertinimas: Integruoti vertinimo srautai leidžia vartotojams įvertinti savo prompt ir srautų kokybę bei efektyvumą.

Išsamūs ištekliai: Azure Machine Learning prompt flow apima biblioteką su integruotais įrankiais, pavyzdžiais ir šablonais, kurie yra pradiniai taškai kūrimui, įkvepiantys kūrybiškumą ir paspartinantys procesą.

**Įmonės pasirengimas LLM pagrįstoms programoms**

Bendradarbiavimas: Azure Machine Learning prompt flow palaiko komandinį bendradarbiavimą, leidžiant keliems vartotojams dirbti kartu su prompt inžinerijos projektais, dalintis žiniomis ir palaikyti versijų kontrolę.

Viskas vienoje platformoje: Azure Machine Learning prompt flow supaprastina visą prompt inžinerijos procesą – nuo kūrimo ir vertinimo iki diegimo ir stebėjimo. Vartotojai gali lengvai diegti savo srautus kaip Azure Machine Learning galinius taškus ir stebėti jų veikimą realiuoju laiku, užtikrinant optimalų veikimą ir nuolatinį tobulinimą.

Azure Machine Learning įmonės pasirengimo sprendimai: Prompt flow pasinaudoja Azure Machine Learning tvirtais įmonės pasirengimo sprendimais, suteikdama saugią, mastelio keičiamą ir patikimą pagrindą srautų kūrimui, eksperimentavimui ir diegimui.

Naudodami Azure Machine Learning prompt flow, vartotojai gali išlaisvinti savo prompt inžinerijos lankstumą, efektyviai bendradarbiauti ir pasinaudoti įmonės lygio sprendimais sėkmingam LLM pagrįstų programų kūrimui ir diegimui.

Sujungdami Azure ML skaičiavimo galią, duomenis ir skirtingus komponentus, įmonių kūrėjai gali lengvai kurti savo dirbtinio intelekto programas.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.