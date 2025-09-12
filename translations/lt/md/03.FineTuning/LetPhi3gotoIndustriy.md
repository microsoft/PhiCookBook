<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "743d7e9cb9c4e8ea642d77bee657a7fa",
  "translation_date": "2025-09-12T14:43:36+00:00",
  "source_file": "md/03.FineTuning/LetPhi3gotoIndustriy.md",
  "language_code": "lt"
}
-->
# **Leiskite Phi-3 tapti pramonės ekspertu**

Norint įdiegti Phi-3 modelį pramonėje, reikia pridėti pramonės verslo duomenis prie Phi-3 modelio. Turime du skirtingus pasirinkimus: pirmasis yra RAG (Retrieval Augmented Generation), o antrasis – Fine Tuning.

## **RAG vs Fine-Tuning**

### **Retrieval Augmented Generation**

RAG yra duomenų paieška + teksto generavimas. Struktūrizuoti ir nestruktūrizuoti įmonės duomenys saugomi vektoriniame duomenų bazėje. Ieškant atitinkamo turinio, randamas susijęs santrauka ir turinys, kurie sudaro kontekstą, o LLM/SLM teksto užbaigimo galimybės naudojamos turiniui generuoti.

### **Fine-tuning**

Fine-tuning yra modelio tobulinimas. Nereikia pradėti nuo modelio algoritmo, tačiau duomenys turi būti nuolat kaupiami. Jei pramonės taikymuose reikia tikslesnės terminologijos ir kalbos išraiškos, Fine-tuning yra geresnis pasirinkimas. Tačiau jei jūsų duomenys dažnai keičiasi, Fine-tuning gali tapti sudėtingu procesu.

### **Kaip pasirinkti**

1. Jei mūsų atsakymui reikia išorinių duomenų įtraukimo, RAG yra geriausias pasirinkimas.

2. Jei reikia pateikti stabilias ir tikslias pramonės žinias, Fine-tuning bus geras pasirinkimas. RAG prioritetą teikia susijusio turinio paieškai, tačiau gali ne visada tiksliai perteikti specializuotus niuansus.

3. Fine-tuning reikalauja aukštos kokybės duomenų rinkinio, o jei tai tik nedidelis duomenų diapazonas, skirtumas nebus didelis. RAG yra lankstesnis.

4. Fine-tuning yra tarsi „juodoji dėžė“, sunkiai suprantama vidinė mechanika. Tačiau RAG leidžia lengviau rasti duomenų šaltinį, efektyviai koreguoti klaidingus duomenis ar turinio klaidas ir suteikti daugiau skaidrumo.

### **Scenarijai**

1. Vertikalios pramonės, kuriose reikalinga specifinė profesinė terminologija ir išraiška, ***Fine-tuning*** bus geriausias pasirinkimas.

2. Klausimų-atsakymų sistema, apimanti skirtingų žinių taškų sintezę, ***RAG*** bus geriausias pasirinkimas.

3. Automatinio verslo srauto derinys ***RAG + Fine-tuning*** yra geriausias pasirinkimas.

## **Kaip naudoti RAG**

![rag](../../../../imgs/03/intro/rag.png)

Vektorinė duomenų bazė yra duomenų rinkinys, saugomas matematinėje formoje. Vektorinės duomenų bazės palengvina mašininio mokymosi modeliams prisiminti ankstesnius įvesties duomenis, leidžiant mašininį mokymąsi naudoti tokiems atvejams kaip paieška, rekomendacijos ir teksto generavimas. Duomenys gali būti identifikuojami pagal panašumo metrikas, o ne tikslų atitikimą, leidžiant kompiuterio modeliams suprasti duomenų kontekstą.

Vektorinė duomenų bazė yra pagrindinis RAG įgyvendinimo elementas. Duomenis galime konvertuoti į vektorinį saugojimą naudodami vektorinius modelius, tokius kaip text-embedding-3, jina-ai-embedding ir kt.

Sužinokite daugiau apie RAG programos kūrimą [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?WT.mc_id=aiml-138114-kinfeylo)

## **Kaip naudoti Fine-tuning**

Dažniausiai naudojami Fine-tuning algoritmai yra Lora ir QLora. Kaip pasirinkti?
- [Sužinokite daugiau naudodami šį pavyzdinį užrašų knygelę](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python FineTuning pavyzdys](../../../../code/04.Finetuning/FineTrainingScript.py)

### **Lora ir QLora**

![lora](../../../../imgs/03/intro/qlora.png)

LoRA (Low-Rank Adaptation) ir QLoRA (Quantized Low-Rank Adaptation) yra technikos, naudojamos didelių kalbos modelių (LLMs) tobulinimui naudojant efektyvų parametrų tobulinimą (PEFT). PEFT technikos yra sukurtos modeliams treniruoti efektyviau nei tradiciniai metodai. 
LoRA yra savarankiška tobulinimo technika, kuri sumažina atminties naudojimą taikant mažo rango aproksimaciją svorio atnaujinimo matricai. Ji siūlo greitą treniravimo laiką ir išlaiko našumą, artimą tradiciniams tobulinimo metodams.

QLoRA yra išplėstinė LoRA versija, kuri įtraukia kvantavimo technikas, dar labiau sumažindama atminties naudojimą. QLoRA kvantuoja iš anksto apmokyto LLM svorio parametrų tikslumą iki 4 bitų, kas yra efektyviau nei LoRA. Tačiau QLoRA treniravimas yra apie 30% lėtesnis nei LoRA treniravimas dėl papildomų kvantavimo ir dekvantavimo žingsnių.

QLoRA naudoja LoRA kaip priedą klaidoms, atsiradusioms kvantavimo metu, ištaisyti. QLoRA leidžia tobulinti didžiulius modelius su milijardais parametrų naudojant palyginti mažus, lengvai prieinamus GPU. Pavyzdžiui, QLoRA gali tobulinti 70B parametrų modelį, kuriam reikia 36 GPU, naudojant tik 2.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.