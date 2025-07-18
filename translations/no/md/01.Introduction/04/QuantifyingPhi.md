<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-07-16T21:47:38+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "no"
}
-->
# **Kvantifisering av Phi-familien**

Modellkvantisering refererer til prosessen med å kartlegge parametrene (som vekter og aktiveringsverdier) i en nevralt nettverksmodell fra et stort verdirekkevidde (vanligvis et kontinuerlig verdirekkevidde) til et mindre, endelig verdirekkevidde. Denne teknologien kan redusere størrelsen og den beregningsmessige kompleksiteten til modellen, og forbedre driftseffektiviteten i ressursbegrensede miljøer som mobiltelefoner eller innebygde systemer. Modellkvantisering oppnår komprimering ved å redusere presisjonen til parametrene, men det medfører også et visst presisjonstap. Derfor må man i kvantiseringsprosessen balansere modellstørrelse, beregningskompleksitet og presisjon. Vanlige kvantiseringsmetoder inkluderer fastpunktkvantisering, flyttallskvantisering osv. Du kan velge passende kvantiseringsstrategi basert på det spesifikke scenariet og behovene.

Vi ønsker å distribuere GenAI-modeller til edge-enheter og la flere enheter komme inn i GenAI-scenarier, som mobiltelefoner, AI-PC/Copilot+PC og tradisjonelle IoT-enheter. Gjennom kvantiserte modeller kan vi distribuere dem til ulike edge-enheter basert på forskjellige enheter. Kombinert med modellakselerasjonsrammeverk og kvantiserte modeller levert av maskinvareprodusenter, kan vi bygge bedre SLM-applikasjonsscenarier.

I kvantiseringsscenarier har vi ulike presisjoner (INT4, INT8, FP16, FP32). Følgende er en forklaring på de vanligste kvantiseringspresisjonene.

### **INT4**

INT4-kvantisering er en radikal kvantiseringsmetode som kvantiserer vektene og aktiveringsverdiene i modellen til 4-bits heltall. INT4-kvantisering fører vanligvis til større presisjonstap på grunn av det mindre representasjonsområdet og lavere presisjon. Samtidig kan INT4-kvantisering, sammenlignet med INT8, ytterligere redusere lagringsbehov og beregningskompleksitet. Det bør bemerkes at INT4-kvantisering er relativt sjelden i praktiske anvendelser, fordi for lav nøyaktighet kan føre til betydelig forringelse av modellens ytelse. I tillegg støtter ikke all maskinvare INT4-operasjoner, så maskinvarekompatibilitet må vurderes ved valg av kvantiseringsmetode.

### **INT8**

INT8-kvantisering er prosessen med å konvertere modellens vekter og aktiveringer fra flyttall til 8-bits heltall. Selv om det numeriske området representert av INT8-heltall er mindre og mindre presist, kan det betydelig redusere lagrings- og beregningsbehov. I INT8-kvantisering gjennomgår vekter og aktiveringsverdier en kvantiseringsprosess, inkludert skalering og offset, for å bevare den opprinnelige flyttallsinformasjonen så mye som mulig. Under inferens blir disse kvantiserte verdiene dekvantisert tilbake til flyttall for beregning, og deretter kvantisert tilbake til INT8 for neste steg. Denne metoden kan gi tilstrekkelig nøyaktighet i de fleste applikasjoner samtidig som den opprettholder høy beregningseffektivitet.

### **FP16**

FP16-formatet, altså 16-bits flyttall (float16), halverer minnebruken sammenlignet med 32-bits flyttall (float32), noe som gir betydelige fordeler i storskala dyp læring. FP16-formatet tillater lasting av større modeller eller behandling av mer data innenfor samme GPU-minnebegrensninger. Ettersom moderne GPU-maskinvare stadig støtter FP16-operasjoner, kan bruk av FP16-format også gi forbedringer i beregningshastighet. FP16-formatet har imidlertid også sine iboende ulemper, nemlig lavere presisjon, som i noen tilfeller kan føre til numerisk ustabilitet eller presisjonstap.

### **FP32**

FP32-formatet gir høyere presisjon og kan nøyaktig representere et bredt spekter av verdier. I scenarier hvor komplekse matematiske operasjoner utføres eller høy presisjon kreves, foretrekkes FP32-formatet. Høy presisjon betyr imidlertid også større minnebruk og lengre beregningstid. For storskala dype læringsmodeller, spesielt når det er mange modellparametere og store datamengder, kan FP32-formatet føre til utilstrekkelig GPU-minne eller redusert inferenshastighet.

På mobile enheter eller IoT-enheter kan vi konvertere Phi-3.x-modeller til INT4, mens AI-PC / Copilot-PC kan bruke høyere presisjon som INT8, FP16, FP32.

Per i dag har ulike maskinvareprodusenter forskjellige rammeverk for å støtte generative modeller, som Intels OpenVINO, Qualcomms QNN, Apples MLX og Nvidias CUDA, kombinert med modellkvantisering for lokal distribusjon.

Teknologisk sett har vi ulike formatstøtter etter kvantisering, som PyTorch / Tensorflow-format, GGUF og ONNX. Jeg har gjort en format-sammenligning og vurdert bruksområder mellom GGUF og ONNX. Her anbefaler jeg ONNX-kvantiseringsformatet, som har god støtte fra modellrammeverk til maskinvare. I dette kapitlet vil vi fokusere på ONNX Runtime for GenAI, OpenVINO og Apple MLX for å utføre modellkvantisering (hvis du har en bedre metode, kan du også sende oss en PR).

**Dette kapitlet inkluderer**

1. [Kvantifisering av Phi-3.5 / 4 med llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Kvantifisering av Phi-3.5 / 4 med Generative AI-utvidelser for onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Kvantifisering av Phi-3.5 / 4 med Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Kvantifisering av Phi-3.5 / 4 med Apple MLX-rammeverket](./UsingAppleMLXQuantifyingPhi.md)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.