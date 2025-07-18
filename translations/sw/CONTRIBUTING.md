<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "90d0d072cf26ccc1f271a580d3e45d70",
  "translation_date": "2025-07-16T14:44:42+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "sw"
}
-->
# Kuchangia

Mradi huu unakaribisha michango na mapendekezo. Michango mingi inahitaji ukakubali
Mkataba wa Leseni ya Mchangiaji (CLA) unaothibitisha kuwa una haki, na kwa kweli unatuwezesha
kutumia mchango wako. Kwa maelezo zaidi, tembelea [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Unapowasilisha ombi la pull request, bot ya CLA itagundua moja kwa moja kama unahitaji kutoa
CLA na kuandaa PR ipasavyo (mfano, ukaguzi wa hali, maoni). Fuata tu maelekezo
yanayotolewa na bot. Hii itabidi ufanye mara moja tu kwa repos zote zinazotumia CLA yetu.

## Kanuni za Maadili

Mradi huu umechukua [Kanuni za Maadili za Chanzo Huria za Microsoft](https://opensource.microsoft.com/codeofconduct/).
Kwa taarifa zaidi soma [Maswali Yanayoulizwa Mara kwa Mara kuhusu Kanuni za Maadili](https://opensource.microsoft.com/codeofconduct/faq/) au wasiliana na [opencode@microsoft.com](mailto:opencode@microsoft.com) kwa maswali au maoni zaidi.

## Tahadhari kwa Kuunda Masuala

Tafadhali usifungue masuala ya GitHub kwa maswali ya msaada wa jumla kwani orodha ya GitHub inapaswa kutumika kwa maombi ya vipengele na ripoti za hitilafu. Hii itatusaidia kufuatilia kwa urahisi masuala halisi au hitilafu kutoka kwenye msimbo na kuweka mjadala wa jumla tofauti na msimbo halisi.

## Jinsi ya Kuchangia

### Miongozo ya Pull Requests

Unapowasilisha pull request (PR) kwenye hazina ya Phi-3 CookBook, tafadhali tumia miongozo ifuatayo:

- **Fanya Fork ya Hazina**: Daima fanya fork ya hazina kwenye akaunti yako kabla ya kufanya mabadiliko yako.

- **Pull requests tofauti (PR)**:
  - Wasilisha kila aina ya mabadiliko katika pull request yake. Kwa mfano, marekebisho ya hitilafu na masasisho ya nyaraka yafanyike katika PR tofauti.
  - Marekebisho ya makosa ya tahajia na masasisho madogo ya nyaraka yanaweza kuunganishwa katika PR moja inapofaa.

- **Shughulikia migongano ya kuunganisha**: Ikiwa pull request yako inaonyesha migongano ya kuunganisha, sasisha tawi lako la `main` la ndani ili lifanane na hazina kuu kabla ya kufanya mabadiliko yako.

- **Uwasilishaji wa tafsiri**: Unapowasilisha PR ya tafsiri, hakikisha folda ya tafsiri ina tafsiri za faili zote zilizopo kwenye folda ya asili.

### Miongozo ya Uandishi

Ili kuhakikisha muafaka katika nyaraka zote, tafadhali tumia miongozo ifuatayo:

- **Muundo wa URL**: Weka URL zote ndani ya mabano ya mraba ikifuatiwa na mabano ya mviringo, bila nafasi za ziada ndani au karibu nazo. Mfano: `[example](https://www.microsoft.com)`.

- **Viungo vya jamaa**: Tumia `./` kwa viungo vya jamaa vinavyoelekeza kwenye faili au folda katika saraka ya sasa, na `../` kwa zile katika saraka ya mzazi. Mfano: `[example](../../path/to/file)` au `[example](../../../path/to/file)`.

- **Lugha zisizo za nchi maalum**: Hakikisha viungo vyako havijumuishi lugha za nchi maalum. Mfano, epuka `/en-us/` au `/en/`.

- **Uhifadhi wa picha**: Hifadhi picha zote katika folda ya `./imgs`.

- **Majina ya picha yenye maelezo**: Panga majina ya picha kwa kutumia herufi za Kiingereza, nambari, na dash. Mfano: `example-image.jpg`.

## Mipangilio ya Kazi ya GitHub

Unapowasilisha pull request, mipangilio ifuatayo itatekelezwa kuthibitisha mabadiliko. Fuata maelekezo hapa chini kuhakikisha pull request yako inapita ukaguzi wa mipangilio:

- [Angalia Njia za Jamaa Zilizovunjika](../..)
- [Angalia URL Hazina Lugha ya Nchi](../..)

### Angalia Njia za Jamaa Zilizovunjika

Mpangilio huu unahakikisha kuwa njia zote za jamaa katika faili zako ni sahihi.

1. Ili kuhakikisha viungo vyako vinafanya kazi vizuri, fanya yafuatayo kwa kutumia VS Code:
    - Elea juu ya kiungo chochote katika faili zako.
    - Bonyeza **Ctrl + Bonyeza** kuhamia kwenye kiungo.
    - Ikiwa unabonyeza kiungo na hakifanyi kazi kwa ndani, mpangilio utaanzishwa na hakitafanya kazi kwenye GitHub.

1. Ili kurekebisha tatizo hili, fanya yafuatayo kwa kutumia mapendekezo ya njia yanayotolewa na VS Code:
    - Andika `./` au `../`.
    - VS Code itakuomba uchague kutoka kwa chaguzi zinazopatikana kulingana na uliyoyaandika.
    - Fuata njia kwa kubonyeza faili au folda unayotaka kuhakikisha njia yako ni sahihi.

Mara baada ya kuongeza njia sahihi ya jamaa, hifadhi na tuma mabadiliko yako.

### Angalia URL Hazina Lugha ya Nchi

Mpangilio huu unahakikisha kuwa URL yoyote ya wavuti haina lugha ya nchi maalum. Kwa kuwa hazina hii inapatikana duniani kote, ni muhimu kuhakikisha URL hazina lugha ya nchi yako.

1. Ili kuthibitisha kuwa URL zako hazina lugha za nchi, fanya yafuatayo:

    - Angalia maandishi kama `/en-us/`, `/en/`, au lugha nyingine yoyote katika URL.
    - Ikiwa haya yapo, basi utapita ukaguzi huu.

1. Ili kurekebisha tatizo hili, fanya yafuatayo:
    - Fungua faili lenye njia iliyobainishwa na mpangilio.
    - Ondoa lugha ya nchi kutoka kwenye URL.

Mara baada ya kuondoa lugha ya nchi, hifadhi na tuma mabadiliko yako.

### Angalia URL Zilizovunjika

Mpangilio huu unahakikisha kuwa URL yoyote ya wavuti katika faili zako inafanya kazi na inarudisha msimbo wa hali 200.

1. Ili kuthibitisha kuwa URL zako zinafanya kazi vizuri, fanya yafuatayo:
    - Angalia hali ya URL katika faili zako.

2. Ili kurekebisha URL yoyote iliyovunjika, fanya yafuatayo:
    - Fungua faili lenye URL iliyovunjika.
    - Sasisha URL kwa ile sahihi.

Mara baada ya kurekebisha URL, hifadhi na tuma mabadiliko yako.

> [!NOTE]
>
> Kunaweza kuwa na matukio ambapo ukaguzi wa URL unashindwa ingawa kiungo kinapatikana. Hii inaweza kutokea kwa sababu kadhaa, zikiwemo:
>
> - **Vizuizi vya mtandao:** Seva za vitendo vya GitHub zinaweza kuwa na vizuizi vya mtandao vinavyozuia ufikiaji wa URL fulani.
> - **Masuala ya muda wa kusubiri majibu:** URL zinazochukua muda mrefu kujibu zinaweza kusababisha kosa la muda wa kusubiri katika mpangilio.
> - **Masuala ya muda ya seva:** Kushindwa kwa seva au matengenezo ya mara kwa mara yanaweza kufanya URL isipatikane kwa muda wakati wa uthibitishaji.

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.