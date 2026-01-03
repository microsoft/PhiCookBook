<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cbe7629d254f1043193b7fe22524d55",
  "translation_date": "2025-07-16T22:45:19+00:00",
  "source_file": "md/01.Introduction/05/Promptflow.md",
  "language_code": "hr"
}
-->
# **Uvod u Promptflow**

[Microsoft Prompt Flow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=aiml-138114-kinfeylo) je vizualni alat za automatizaciju tijeka rada koji korisnicima omogućuje kreiranje automatiziranih tijekova rada koristeći unaprijed izrađene predloške i prilagođene konektore. Dizajniran je kako bi programerima i poslovnim analitičarima omogućio brzo izgradnju automatiziranih procesa za zadatke poput upravljanja podacima, suradnje i optimizacije procesa. Uz Prompt Flow, korisnici mogu jednostavno povezivati različite usluge, aplikacije i sustave te automatizirati složene poslovne procese.

Microsoft Prompt Flow je osmišljen da pojednostavi cjelokupni razvojni ciklus AI aplikacija koje pokreću Large Language Models (LLM). Bilo da smišljate ideje, izrađujete prototipove, testirate, evaluirate ili implementirate aplikacije temeljene na LLM-ovima, Prompt Flow olakšava proces i omogućuje vam izradu LLM aplikacija proizvodne kvalitete.

## Ključne značajke i prednosti korištenja Microsoft Prompt Flow:

**Interaktivno iskustvo izrade**

Prompt Flow pruža vizualni prikaz strukture vašeg tijeka rada, što olakšava razumijevanje i navigaciju kroz projekte.  
Nudi iskustvo kodiranja slično bilježnici za učinkoviti razvoj i otklanjanje pogrešaka u tijeku rada.

**Varijante i podešavanje prompta**

Kreirajte i uspoređujte više varijanti prompta kako biste olakšali iterativni proces usavršavanja. Procijenite izvedbu različitih prompta i odaberite one najučinkovitije.

**Ugrađeni evaluacijski tijekovi**  
Procijenite kvalitetu i učinkovitost svojih prompta i tijekova rada koristeći ugrađene alate za evaluaciju.  
Razumite koliko dobro vaše aplikacije temeljene na LLM-ovima funkcioniraju.

**Sveobuhvatni resursi**

Prompt Flow uključuje biblioteku ugrađenih alata, primjera i predložaka. Ti resursi služe kao polazna točka za razvoj, potiču kreativnost i ubrzavaju proces.

**Suradnja i spremnost za poduzeća**

Podržava timsku suradnju omogućujući više korisnika da zajedno rade na projektima inženjeringa prompta.  
Održava kontrolu verzija i učinkovito dijeljenje znanja. Pojednostavljuje cijeli proces inženjeringa prompta, od razvoja i evaluacije do implementacije i nadzora.

## Evaluacija u Prompt Flow

U Microsoft Prompt Flow-u, evaluacija ima ključnu ulogu u procjeni koliko dobro vaši AI modeli rade. Pogledajmo kako možete prilagoditi evaluacijske tijekove i metrike unutar Prompt Flow-a:

![PFVizualizacija](../../../../../translated_images/pfvisualize.c1d9ca75baa2a222.hr.png)

**Razumijevanje evaluacije u Prompt Flow-u**

U Prompt Flow-u, tijek rada predstavlja niz čvorova koji obrađuju ulaz i generiraju izlaz. Evaluacijski tijekovi su posebne vrste tijekova dizajnirane za procjenu izvedbe izvođenja na temelju određenih kriterija i ciljeva.

**Ključne značajke evaluacijskih tijekova**

Obično se pokreću nakon tijeka rada koji se testira, koristeći njegove izlaze. Izračunavaju rezultate ili metrike za mjerenje izvedbe testiranog tijeka. Metrike mogu uključivati točnost, ocjene relevantnosti ili druge relevantne mjere.

### Prilagodba evaluacijskih tijekova

**Definiranje ulaza**

Evaluacijski tijekovi trebaju primati izlaze testiranog tijeka rada. Definirajte ulaze slično kao kod standardnih tijekova.  
Na primjer, ako evaluirate QnA tijek, nazovite ulaz "answer". Ako evaluirate klasifikacijski tijek, nazovite ulaz "category". Mogu biti potrebni i ulazi s točnim vrijednostima (npr. stvarne oznake).

**Izlazi i metrike**

Evaluacijski tijekovi proizvode rezultate koji mjere izvedbu testiranog tijeka. Metrike se mogu izračunavati pomoću Pythona ili LLM-a (Large Language Models). Koristite funkciju log_metric() za evidentiranje relevantnih metrika.

**Korištenje prilagođenih evaluacijskih tijekova**

Razvijte vlastiti evaluacijski tijek prilagođen vašim specifičnim zadacima i ciljevima. Prilagodite metrike prema svojim evaluacijskim potrebama.  
Primijenite ovaj prilagođeni evaluacijski tijek na serijska izvođenja za testiranje u velikom opsegu.

## Ugrađene metode evaluacije

Prompt Flow također nudi ugrađene metode evaluacije.  
Možete poslati serijska izvođenja i koristiti ove metode za procjenu koliko dobro vaš tijek rada funkcionira s velikim skupovima podataka.  
Pregledajte rezultate evaluacije, usporedite metrike i po potrebi iterirajte.  
Imajte na umu da je evaluacija ključna za osiguravanje da vaši AI modeli zadovoljavaju željene kriterije i ciljeve. Za detaljne upute o razvoju i korištenju evaluacijskih tijekova u Microsoft Prompt Flow-u, proučite službenu dokumentaciju.

Ukratko, Microsoft Prompt Flow omogućuje programerima izradu visokokvalitetnih LLM aplikacija pojednostavljujući inženjering prompta i pružajući snažno razvojno okruženje. Ako radite s LLM-ovima, Prompt Flow je vrijedan alat za istraživanje. Pogledajte [Prompt Flow Evaluation Documents](https://learn.microsoft.com/azure/machine-learning/prompt-flow/how-to-develop-an-evaluation-flow?view=azureml-api-2?WT.mc_id=aiml-138114-kinfeylo) za detaljne upute o razvoju i korištenju evaluacijskih tijekova u Microsoft Prompt Flow-u.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.