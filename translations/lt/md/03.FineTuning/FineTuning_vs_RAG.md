<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e4e010400c2918557b36bb932a14004c",
  "translation_date": "2025-09-12T14:38:57+00:00",
  "source_file": "md/03.FineTuning/FineTuning_vs_RAG.md",
  "language_code": "lt"
}
-->
## Derinimas vs RAG

## Duomenų paieška ir generavimas

RAG apjungia duomenų paiešką ir teksto generavimą. Įmonės struktūrizuoti ir nestruktūrizuoti duomenys saugomi vektorinėje duomenų bazėje. Ieškant aktualaus turinio, surandama atitinkama santrauka ir turinys, kurie sudaro kontekstą, o LLM/SLM teksto užbaigimo galimybės naudojamos turiniui generuoti.

## RAG procesas
![FinetuningvsRAG](../../../../imgs/03/intro/rag.png)

## Derinimas
Derinimas remiasi tam tikro modelio tobulinimu. Nereikia pradėti nuo modelio algoritmo, tačiau duomenys turi būti nuolat kaupiami. Jei pramonės taikymuose reikia tikslesnės terminologijos ir kalbos išraiškos, derinimas yra geresnis pasirinkimas. Tačiau jei jūsų duomenys dažnai keičiasi, derinimas gali tapti sudėtingas.

## Kaip pasirinkti
Jei atsakymui reikia įtraukti išorinius duomenis, RAG yra geriausias pasirinkimas.

Jei reikia pateikti stabilias ir tikslias pramonės žinias, derinimas bus geras pasirinkimas. RAG prioritetą teikia aktualaus turinio paieškai, tačiau ne visada gali perteikti specializuotus niuansus.

Derinimui reikalingas aukštos kokybės duomenų rinkinys, o jei duomenų apimtis yra nedidelė, skirtumas nebus didelis. RAG yra lankstesnis.

Derinimas yra tarsi juodoji dėžė, metafizika, ir sunku suprasti vidinį mechanizmą. Tačiau RAG leidžia lengviau rasti duomenų šaltinį, taip efektyviau koreguoti klaidingą informaciją ar turinio klaidas ir užtikrinti didesnį skaidrumą.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.