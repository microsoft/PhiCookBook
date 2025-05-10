<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cbe7629d254f1043193b7fe22524d55",
  "translation_date": "2025-05-09T15:13:23+00:00",
  "source_file": "md/01.Introduction/05/Promptflow.md",
  "language_code": "sv"
}
-->
# **Introducera Promptflow**

[Microsoft Prompt Flow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=aiml-138114-kinfeylo) är ett visuellt verktyg för arbetsflödesautomatisering som låter användare skapa automatiserade arbetsflöden med hjälp av förbyggda mallar och anpassade kopplingar. Det är utformat för att göra det möjligt för utvecklare och affärsanalytiker att snabbt bygga automatiserade processer för uppgifter som databehandling, samarbete och processoptimering. Med Prompt Flow kan användare enkelt koppla ihop olika tjänster, applikationer och system samt automatisera komplexa affärsprocesser.

Microsoft Prompt Flow är utformat för att effektivisera hela utvecklingscykeln för AI-applikationer som drivs av Large Language Models (LLMs). Oavsett om du idéutvecklar, prototypar, testar, utvärderar eller distribuerar LLM-baserade applikationer förenklar Prompt Flow processen och gör det möjligt för dig att bygga LLM-appar med produktionskvalitet.

## Här är de viktigaste funktionerna och fördelarna med att använda Microsoft Prompt Flow:

**Interaktiv Authoring-upplevelse**

Prompt Flow ger en visuell översikt av strukturen i ditt flöde, vilket gör det enkelt att förstå och navigera i dina projekt.  
Det erbjuder en notebook-liknande kodningsupplevelse för effektiv utveckling och felsökning av flöden.

**Promptvarianter och finjustering**

Skapa och jämför flera promptvarianter för att underlätta en iterativ förfiningsprocess. Utvärdera prestandan hos olika prompts och välj de mest effektiva.

**Inbyggda utvärderingsflöden**  
Bedöm kvaliteten och effektiviteten hos dina prompts och flöden med hjälp av inbyggda utvärderingsverktyg.  
Förstå hur väl dina LLM-baserade applikationer presterar.

**Omfattande resurser**

Prompt Flow inkluderar ett bibliotek med inbyggda verktyg, exempel och mallar. Dessa resurser fungerar som en startpunkt för utveckling, inspirerar kreativitet och påskyndar processen.

**Samarbete och företagsanpassning**

Stöd samarbete i team genom att låta flera användare arbeta tillsammans på prompt engineering-projekt.  
Bibehåll versionskontroll och dela kunskap effektivt. Effektivisera hela prompt engineering-processen, från utveckling och utvärdering till distribution och övervakning.

## Utvärdering i Prompt Flow

I Microsoft Prompt Flow spelar utvärdering en avgörande roll för att bedöma hur väl dina AI-modeller presterar. Låt oss utforska hur du kan anpassa utvärderingsflöden och mätvärden inom Prompt Flow:

![PFVizualise](../../../../../translated_images/pfvisualize.93c453890f4088830217fa7308b1a589058ed499bbfff160c85676066b5cbf2d.sv.png)

**Förstå utvärdering i Prompt Flow**

I Prompt Flow representerar ett flöde en sekvens av noder som bearbetar indata och genererar utdata. Utvärderingsflöden är speciella typer av flöden som är designade för att bedöma prestandan hos ett körning baserat på specifika kriterier och mål.

**Nyckelfunktioner för utvärderingsflöden**

De körs vanligtvis efter det flöde som testas och använder dess utdata. De beräknar poäng eller mätvärden för att mäta prestandan hos det testade flödet. Mätvärden kan inkludera noggrannhet, relevanspoäng eller andra relevanta mått.

### Anpassa utvärderingsflöden

**Definiera indata**

Utvärderingsflöden behöver ta emot utdata från den körning som testas. Definiera indata på samma sätt som för vanliga flöden.  
Till exempel, om du utvärderar ett QnA-flöde, namnge en indata som "answer". Vid utvärdering av ett klassificeringsflöde, namnge en indata som "category". Även grundläggande sanning-indata (t.ex. faktiska etiketter) kan behövas.

**Utdata och mätvärden**

Utvärderingsflöden genererar resultat som mäter prestandan hos det testade flödet. Mätvärden kan beräknas med Python eller LLM (Large Language Models). Använd funktionen log_metric() för att logga relevanta mätvärden.

**Använda anpassade utvärderingsflöden**

Utveckla ditt eget utvärderingsflöde anpassat efter dina specifika uppgifter och mål. Anpassa mätvärden baserat på dina utvärderingsmål.  
Applicera detta anpassade utvärderingsflöde på batchkörningar för storskalig testning.

## Inbyggda utvärderingsmetoder

Prompt Flow erbjuder även inbyggda utvärderingsmetoder.  
Du kan skicka batchkörningar och använda dessa metoder för att utvärdera hur väl ditt flöde presterar med stora datamängder.  
Visa utvärderingsresultat, jämför mätvärden och iterera vid behov.  
Kom ihåg att utvärdering är avgörande för att säkerställa att dina AI-modeller uppfyller önskade kriterier och mål. Utforska den officiella dokumentationen för detaljerade instruktioner om hur du utvecklar och använder utvärderingsflöden i Microsoft Prompt Flow.

Sammanfattningsvis ger Microsoft Prompt Flow utvecklare möjlighet att skapa högkvalitativa LLM-applikationer genom att förenkla prompt engineering och erbjuda en robust utvecklingsmiljö. Om du arbetar med LLMs är Prompt Flow ett värdefullt verktyg att utforska. Utforska [Prompt Flow Evaluation Documents](https://learn.microsoft.com/azure/machine-learning/prompt-flow/how-to-develop-an-evaluation-flow?view=azureml-api-2?WT.mc_id=aiml-138114-kinfeylo) för detaljerade instruktioner om hur du utvecklar och använder utvärderingsflöden i Microsoft Prompt Flow.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För viktig information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.