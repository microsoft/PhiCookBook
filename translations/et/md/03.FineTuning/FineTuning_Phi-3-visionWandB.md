<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-10-11T11:46:08+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "et"
}
-->
# Phi-3-Vision-128K-Instruct Projekti Ülevaade

## Mudel

Phi-3-Vision-128K-Instruct, kerge ja tipptasemel multimodaalne mudel, on selle projekti keskmes. See kuulub Phi-3 mudelite perekonda ja toetab konteksti pikkust kuni 128 000 tokenit. Mudel on treenitud mitmekesise andmestiku põhjal, mis sisaldab sünteetilisi andmeid ja hoolikalt filtreeritud avalikult kättesaadavaid veebisaite, rõhutades kvaliteetset ja põhjendustele keskenduvat sisu. Treeningprotsess hõlmas juhendatud peenhäälestust ja otsest eelistuste optimeerimist, et tagada täpne juhiste järgimine, samuti tugevaid turvameetmeid.

## Näidisandmete loomine on oluline mitmel põhjusel:

1. **Testimine**: Näidisandmed võimaldavad testida rakendust erinevates stsenaariumides, mõjutamata tegelikke andmeid. See on eriti oluline arenduse ja testimise etappides.

2. **Jõudluse optimeerimine**: Näidisandmed, mis jäljendavad tegelike andmete ulatust ja keerukust, aitavad tuvastada jõudluse kitsaskohti ja optimeerida rakendust vastavalt.

3. **Prototüüpimine**: Näidisandmeid saab kasutada prototüüpide ja makettide loomiseks, mis aitavad mõista kasutajate vajadusi ja saada tagasisidet.

4. **Andmeanalüüs**: Andmeteaduses kasutatakse näidisandmeid sageli uurivaks andmeanalüüsiks, mudelite treenimiseks ja algoritmide testimiseks.

5. **Turvalisus**: Näidisandmete kasutamine arenduse ja testimise keskkondades aitab vältida tundlike tegelike andmete juhuslikku lekkimist.

6. **Õppimine**: Kui õpid uut tehnoloogiat või tööriista, pakuvad näidisandmed praktilist viisi õpitu rakendamiseks.

Pea meeles, et näidisandmete kvaliteet võib oluliselt mõjutada neid tegevusi. Need peaksid olema struktuuri ja varieeruvuse poolest võimalikult sarnased tegelikele andmetele.

### Näidisandmete loomine
[Andmestiku loomise skript](./CreatingSampleData.md)

## Andmestik

Hea näide näidisandmestikust on [DBQ/Burberry.Product.prices.United.States andmestik](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (saadaval Huggingface'is). 
Burberry toodete näidisandmestik koos metainfoga toodete kategooria, hinna ja pealkirja kohta, kokku 3,040 rida, millest igaüks esindab unikaalset toodet. See andmestik võimaldab testida mudeli võimet mõista ja tõlgendada visuaalseid andmeid, genereerides kirjeldavat teksti, mis kajastab keerukaid visuaalseid detaile ja brändispetsiifilisi omadusi.

**Märkus:** Võid kasutada mis tahes andmestikku, mis sisaldab pilte.

## Keerukas põhjendamine

Mudel peab hindama hindu ja nimetusi ainult pildi põhjal. See nõuab, et mudel mitte ainult ei tunneks ära visuaalseid omadusi, vaid mõistaks ka nende tähendust toote väärtuse ja brändingu kontekstis. Täpsete tekstikirjelduste sünteesimine piltidest toob esile visuaalsete andmete integreerimise potentsiaali mudelite jõudluse ja mitmekülgsuse suurendamiseks reaalses maailmas.

## Phi-3 Vision Arhitektuur

Mudel arhitektuur on Phi-3 multimodaalne versioon. See töötleb nii teksti kui ka pildilisi andmeid, integreerides need sisendid ühtseks järjestuseks, et saavutada terviklik arusaamine ja genereerimisülesanded. Mudel kasutab eraldi sisendkihte teksti ja piltide jaoks. Teksti tokenid muudetakse tihedateks vektoriteks, samal ajal kui pilte töödeldakse CLIP visuaalse mudeli abil, et eraldada omaduste sisendid. Need pildi sisendid projitseeritakse tekstisisendite mõõtmetega sobivaks, tagades nende sujuva integreerimise.

## Teksti ja pildi sisendite integreerimine

Tekstijärjestuses olevad spetsiaalsed tokenid näitavad, kuhu pildi sisendid tuleks lisada. Töötlemise ajal asendatakse need spetsiaalsed tokenid vastavate pildi sisenditega, võimaldades mudelil käsitleda teksti ja pilte ühe järjestusena. Meie andmestiku jaoks on prompt vormindatud spetsiaalse <|image|> tokeni abil järgmiselt:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Näidiskood
- [Phi-3-Vision treenimisskript](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias näide](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.