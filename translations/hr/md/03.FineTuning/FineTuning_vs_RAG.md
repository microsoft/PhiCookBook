<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e4e010400c2918557b36bb932a14004c",
  "translation_date": "2025-07-17T09:31:59+00:00",
  "source_file": "md/03.FineTuning/FineTuning_vs_RAG.md",
  "language_code": "hr"
}
-->
## Finetuning vs RAG

## Retrieval Augmented Generation

RAG je kombinacija dohvaćanja podataka i generiranja teksta. Strukturirani i nestrukturirani podaci poduzeća pohranjuju se u vektorsku bazu podataka. Prilikom pretraživanja relevantnog sadržaja pronalazi se sažetak i sadržaj koji čine kontekst, a zatim se koristi sposobnost dovršetka teksta LLM/SLM modela za generiranje sadržaja.

## RAG proces
![FinetuningvsRAG](../../../../translated_images/hr/rag.2014adc59e6f6007.png)

## Fine-tuning
Fine-tuning se temelji na poboljšanju određenog modela. Nije potrebno započinjati s algoritmom modela, ali podaci se moraju kontinuirano prikupljati. Ako želite precizniju terminologiju i jezični izraz u industrijskim primjenama, fine-tuning je bolji izbor. No, ako se vaši podaci često mijenjaju, fine-tuning može postati složen.

## Kako odabrati
Ako naš odgovor zahtijeva uvođenje vanjskih podataka, RAG je najbolji izbor.

Ako trebate stabilan i precizan izlaz industrijskog znanja, fine-tuning će biti dobar izbor. RAG daje prednost pronalaženju relevantnog sadržaja, ali možda neće uvijek uhvatiti specifične nijanse.

Fine-tuning zahtijeva kvalitetan skup podataka, a ako je riječ o malom opsegu podataka, neće donijeti značajnu razliku. RAG je fleksibilniji.  
Fine-tuning je crna kutija, metafizika, i teško je razumjeti njegov unutarnji mehanizam. No, RAG olakšava pronalazak izvora podataka, čime se učinkovito mogu korigirati halucinacije ili pogreške u sadržaju te pruža bolju transparentnost.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.