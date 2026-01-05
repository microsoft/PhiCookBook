<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f4cbbe7bf3e764de52d64a96d97b3c35",
  "translation_date": "2026-01-05T12:39:01+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "no"
}
-->
# **Kvantifisering av Phi-familien**

Modellkvantisering refererer til prosessen med å kartlegge parameterne (for eksempel vekter og aktiveringsverdier) i en nevralt nettverksmodell fra et stort verdiareale (vanligvis et kontinuerlig verdiareale) til et mindre endelig verdiareale. Denne teknologien kan redusere størrelsen og beregningskompleksiteten til modellen og forbedre driftseffektiviteten til modellen i ressursbegrensede miljøer som mobile enheter eller innebygde systemer. Modellkvantisering oppnår komprimering ved å redusere presisjonen til parametrene, men det introduserer også et visst presisjonstap. Derfor er det nødvendig å balansere modellstørrelse, beregningskompleksitet og presisjon i kvantiseringsprosessen. Vanlige kvantiseringsmetoder inkluderer fastpunktkvantisering, flytpunktkvantisering osv. Du kan velge passende kvantiseringsstrategi etter de spesifikke scenariene og behovene.

Vi håper å distribuere GenAI-modeller til enhetsnære enheter og la flere enheter komme inn i GenAI-scenarier, som mobile enheter, AI-PC/Copilot+PC, og tradisjonelle IoT-enheter. Gjennom kvantiserte modeller kan vi distribuere dem til forskjellige enhetsnære enheter avhengig av ulike enheter. Kombinert med modellerakseringsrammeverket og kvantiseringsmodellen levert av maskinvareprodusenter, kan vi bygge bedre SLM-applikasjonsscenarier.

I kvantiseringsscenarier har vi forskjellige presisjoner (INT4, INT8, FP16, FP32). Følgende er en forklaring av de vanlig brukte kvantiseringspresisjonene

### **INT4**

INT4-kvantisering er en radikal kvantiseringsmetode som kvantiserer vektene og aktiveringsverdiene i modellen til 4-bits heltall. INT4-kvantisering resulterer vanligvis i et større presisjonstap på grunn av det mindre representasjonsområdet og lavere presisjon. Imidlertid kan INT4-kvantisering, sammenlignet med INT8-kvantisering, ytterligere redusere lagringsbehovet og beregningskompleksiteten til modellen. Det bør bemerkes at INT4-kvantisering er relativt sjelden i praktiske applikasjoner, fordi for lav nøyaktighet kan føre til betydelig degradering i modellens ytelse. I tillegg støtter ikke all maskinvare INT4-operasjoner, så maskinvarekompatibilitet må vurderes ved valg av kvantiseringsmetode.

### **INT8**

INT8-kvantisering er prosessen med å konvertere en modells vekter og aktiveringer fra flyttall til 8-bits heltall. Selv om det numeriske området som representeres av INT8-heltall er mindre og mindre presist, kan det betydelig redusere lagrings- og beregningsbehov. I INT8-kvantisering går modellens vekter og aktiveringsverdier gjennom en kvantiseringsprosess, inkludert skalering og offset, for å bevare den opprinnelige flyttallsinformasjonen så mye som mulig. Under inferens vil disse kvantiserte verdiene dekvantiseres tilbake til flyttall for beregning, og deretter kvantiseres tilbake til INT8 for neste trinn. Denne metoden kan gi tilstrekkelig nøyaktighet i de fleste applikasjoner samtidig som den opprettholder høy beregningseffektivitet.

### **FP16**

FP16-formatet, det vil si 16-bits flyttall (float16), reduserer minnebruk med halvparten sammenlignet med 32-bits flyttall (float32), noe som har betydelige fordeler i storskala dyp læringsapplikasjoner. FP16-formatet tillater lasting av større modeller eller behandling av mer data innen samme GPU-minnebegrensninger. Ettersom moderne GPU-maskinvare fortsetter å støtte FP16-operasjoner, kan bruk av FP16-formatet også gi forbedringer i regnehastigheten. Imidlertid har FP16-formatet også sine iboende ulemper, nemlig lavere presisjon, som i noen tilfeller kan føre til numerisk ustabilitet eller presisjonstap.

### **FP32**

FP32-formatet gir høyere presisjon og kan nøyaktig representere et bredt spekter av verdier. I scenarioer hvor komplekse matematiske operasjoner utføres eller høy presisjonsresultater kreves, foretrekkes FP32-formatet. Imidlertid betyr høy nøyaktighet også større minnebruk og lengre beregningstid. For storskala dype læringsmodeller, spesielt når det er mange modellparametere og enorme datamengder, kan FP32-formatet føre til utilstrekkelig GPU-minne eller redusert inferenshastighet.

På mobile enheter eller IoT-enheter kan vi konvertere Phi-3.x-modeller til INT4, mens AI-PC / Copilot PC kan bruke høyere presisjon som INT8, FP16, FP32.

Per i dag har forskjellige maskinvareprodusenter ulike rammeverk for å støtte generative modeller, som Intels OpenVINO, Qualcomms QNN, Apples MLX, og Nvidias CUDA, kombinert med modellkvantisering for å fullføre lokal distribusjon.

Når det gjelder teknologi, har vi ulike formatstøtter etter kvantisering, som PyTorch / TensorFlow-format, GGUF og ONNX. Jeg har gjort en format sammenligning og applikasjonsscenarier mellom GGUF og ONNX. Her anbefaler jeg ONNX-kvantisering, som har god støtte fra modellrammeverket til maskinvaren. I dette kapittelet vil vi fokusere på ONNX Runtime for GenAI, OpenVINO og Apple MLX for å utføre modellkvantisering (hvis du har en bedre metode, kan du også gi den til oss ved å sende inn PR)

**Dette kapitlet inkluderer**

1. [Kvantifisering av Phi-3.5 / 4 ved bruk av llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Kvantifisering av Phi-3.5 / 4 ved bruk av Generative AI-utvidelser for onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Kvantifisering av Phi-3.5 / 4 ved bruk av Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Kvantifisering av Phi-3.5 / 4 ved bruk av Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->