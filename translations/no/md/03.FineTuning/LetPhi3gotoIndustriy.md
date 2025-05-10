<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "743d7e9cb9c4e8ea642d77bee657a7fa",
  "translation_date": "2025-05-09T22:27:33+00:00",
  "source_file": "md/03.FineTuning/LetPhi3gotoIndustriy.md",
  "language_code": "no"
}
-->
# **La Phi-3 bli en bransjeekspert**

For å integrere Phi-3-modellen i en bransje, må du legge til bransjespesifikke forretningsdata i Phi-3-modellen. Vi har to forskjellige alternativer: det første er RAG (Retrieval Augmented Generation) og det andre er Fine Tuning.

## **RAG vs Fine-Tuning**

### **Retrieval Augmented Generation**

RAG er datahenting + tekstgenerering. Strukturert og ustrukturert data fra virksomheten lagres i en vektordatabase. Når relevant innhold søkes opp, finner man relevante sammendrag og innhold som danner en kontekst, og kombinerer dette med tekstfullføringskapasiteten til LLM/SLM for å generere innhold.

### **Fine-tuning**

Fine-tuning handler om å forbedre en bestemt modell. Det krever ikke at man starter med selve modellalgoritmen, men data må kontinuerlig samles inn. Hvis du ønsker mer presis terminologi og språkuttrykk i bruksområder for industrien, er fine-tuning det beste valget. Men hvis dataene dine endres ofte, kan fine-tuning bli komplisert.

### **Hvordan velge**

1. Hvis svaret vårt krever innføring av ekstern data, er RAG det beste valget.

2. Hvis du trenger å levere stabil og presis bransjekunnskap, vil fine-tuning være et godt valg. RAG prioriterer å hente relevant innhold, men treffer ikke alltid på de spesialiserte nyansene.

3. Fine-tuning krever et datasett av høy kvalitet, og hvis det bare er et lite datasett, vil det ikke gjøre stor forskjell. RAG er mer fleksibelt.

4. Fine-tuning er en svart boks, en metafysikk, og det er vanskelig å forstå den interne mekanismen. Men RAG gjør det lettere å finne kilden til dataene, noe som effektivt kan justere hallusinasjoner eller innholdsfeil og gi bedre gjennomsiktighet.

### **Bruksscenarier**

1. Vertikale bransjer som krever spesifikt faglig vokabular og uttrykk, ***Fine-tuning*** er det beste valget.

2. QA-systemer som involverer syntese av forskjellige kunnskapspunkter, ***RAG*** er det beste valget.

3. Kombinasjonen av automatisert forretningsflyt ***RAG + Fine-tuning*** er det beste valget.

## **Hvordan bruke RAG**

![rag](../../../../translated_images/rag.36e7cb856f120334d577fde60c6a5d7c5eecae255dac387669303d30b4b3efa4.no.png)

En vektordatabase er en samling data lagret i matematisk form. Vektordatabaser gjør det enklere for maskinlæringsmodeller å huske tidligere input, noe som muliggjør bruk av maskinlæring til støtte for bruksområder som søk, anbefalinger og tekstgenerering. Data kan identifiseres basert på likhetsmål i stedet for eksakte treff, noe som gjør at modeller kan forstå konteksten til dataene.

Vektordatabase er nøkkelen til å realisere RAG. Vi kan konvertere data til vektorlagring gjennom vektormodeller som text-embedding-3, jina-ai-embedding, osv.

Lær mer om å lage RAG-applikasjoner [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?WT.mc_id=aiml-138114-kinfeylo)

## **Hvordan bruke Fine-tuning**

De mest brukte algoritmene i Fine-tuning er Lora og QLora. Hvordan velge?
- [Lær mer med denne eksempelnotatboken](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Eksempel på Python FineTuning Sample](../../../../code/04.Finetuning/FineTrainingScript.py)

### **Lora og QLora**

![lora](../../../../translated_images/qlora.6aeba71122bc0c8d56ccf0bc36b861304939fee087f43c1fc6cc5c9cb8764725.no.png)

LoRA (Low-Rank Adaptation) og QLoRA (Quantized Low-Rank Adaptation) er begge teknikker brukt for å finjustere store språkmodeller (LLMs) ved hjelp av Parameter Efficient Fine Tuning (PEFT). PEFT-teknikker er designet for å trene modeller mer effektivt enn tradisjonelle metoder.  
LoRA er en selvstendig finjusteringsteknikk som reduserer minnebruken ved å bruke en lav-rang tilnærming på vektoppdateringsmatrisen. Den tilbyr rask treningstid og opprettholder ytelse nær tradisjonelle finjusteringsmetoder.

QLoRA er en utvidet versjon av LoRA som inkluderer kvantiseringsteknikker for ytterligere å redusere minnebruk. QLoRA kvantiserer presisjonen på vektparameterne i den forhåndstrente LLM-en til 4-bits presisjon, noe som er mer minneeffektivt enn LoRA. QLoRA-trening er imidlertid omtrent 30 % tregere enn LoRA på grunn av ekstra kvantiserings- og dekvantiseringssteg.

QLoRA bruker LoRA som et tillegg for å korrigere feil som oppstår under kvantisering. QLoRA muliggjør finjustering av enorme modeller med milliarder av parametere på relativt små, lett tilgjengelige GPU-er. For eksempel kan QLoRA finjustere en 70B parameter-modell som normalt krever 36 GPU-er med bare 2 GPU-er.

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved bruk av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.