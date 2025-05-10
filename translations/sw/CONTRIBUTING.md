<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f71f15fee9a73ecfcd4fd40efbe3070",
  "translation_date": "2025-05-09T03:43:13+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "sw"
}
-->
# Kuchangia

Mradi huu unakaribisha michango na mapendekezo. Michango mingi inahitaji ukakubali Mkataba wa Leseni ya Mchango (Contributor License Agreement - CLA) unaothibitisha kuwa una haki, na kwa kweli unatupa haki za kutumia mchango wako. Kwa maelezo zaidi, tembelea [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Unapowasilisha ombi la kuvuta (pull request), bot ya CLA itabaini moja kwa moja kama unahitaji kutoa CLA na kuandaa PR ipasavyo (mfano, ukaguzi wa hali, maoni). Fuata tu maelekezo yanayotolewa na bot. Hii utalazimika kufanya mara moja tu kwa maktaba zote zinazotumia CLA yetu.

## Kanuni za Maadili

Mradi huu umechukua [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Kwa taarifa zaidi soma [Maswali Yanayoulizwa Mara kwa Mara kuhusu Kanuni za Maadili](https://opensource.microsoft.com/codeofconduct/faq/) au wasiliana na [opencode@microsoft.com](mailto:opencode@microsoft.com) kwa maswali au maoni zaidi.

## Tahadhari kwa Kuunda Masuala

Tafadhali usifungue masuala ya GitHub kwa maswali ya msaada wa jumla kwa sababu orodha ya GitHub inapaswa kutumika kwa maombi ya vipengele na ripoti za kasoro. Hii itatusaidia kufuatilia kwa urahisi masuala halisi au kasoro kutoka kwenye msimbo na kuweka mjadala wa jumla tofauti na msimbo halisi.

## Jinsi ya Kuchangia

### Miongozo ya Ombi la Kuvuta (Pull Requests)

Unapowasilisha ombi la kuvuta (PR) kwenye ghala la Phi-3 CookBook, tafadhali tumia miongozo ifuatayo:

- **Fanya Fork ya Ghala**: Daima fanya fork ya ghala kwa akaunti yako kabla ya kufanya marekebisho.

- **Ombi la kuvuta tofauti (PR)**:
  - Wasilisha kila aina ya mabadiliko katika ombi lake la kuvuta. Kwa mfano, marekebisho ya kasoro na masasisho ya nyaraka yafanyike katika PR tofauti.
  - Marekebisho ya makosa ya tahajia na masasisho madogo ya nyaraka yanaweza kuunganishwa katika PR moja inapofaa.

- **Shughulikia migongano ya kuunganisha (merge conflicts)**: Ikiwa ombi lako la kuvuta linaonyesha migongano ya kuunganisha, sasisha tawi lako la `main` la eneo lako ili lilingane na ghala kuu kabla ya kufanya marekebisho.

- **Uwasilishaji wa tafsiri**: Unapowasilisha PR ya tafsiri, hakikisha folda ya tafsiri ina tafsiri za faili zote zilizopo katika folda ya asili.

### Miongozo ya Tafsiri

> [!IMPORTANT]
>
> Unapotafsiri maandishi katika ghala hili, usitumie tafsiri ya mashine. Tafsiri hufanywa tu na watu waliobobea katika lugha husika.

Kama una ujuzi wa lugha isiyo ya Kiingereza, unaweza kusaidia kutafsiri maudhui. Fuata hatua hizi kuhakikisha michango yako ya tafsiri inaingizwa ipasavyo, tafadhali tumia miongozo ifuatayo:

- **Unda folda ya tafsiri**: Nenda kwenye folda ya sehemu husika na unda folda ya tafsiri kwa lugha unayochangia. Kwa mfano:
  - Kwa sehemu ya utangulizi: `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - Kwa sehemu ya kuanza haraka: `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Endelea na muundo huu kwa sehemu nyingine (03.Inference, 04.Finetuning, n.k.)

- **Sasisha njia za uhusiano (relative paths)**: Unapotafsiri, rekebisha muundo wa folda kwa kuongeza `../../` mwanzoni mwa njia za uhusiano ndani ya faili za markdown ili kuhakikisha viungo vinafanya kazi vizuri. Kwa mfano, badilisha kama ifuatavyo:
  - Badilisha `(../../imgs/01/phi3aisafety.png)` kuwa `(../../../../imgs/01/phi3aisafety.png)`

- **Panga tafsiri zako**: Kila faili iliyotafsiriwa iwe katika folda ya tafsiri ya sehemu husika. Kwa mfano, ukitafsiri sehemu ya utangulizi kwa Kihispania, utaunda kama ifuatavyo:
  - `PhiCookBook/md/01.Introduce/translations/es/`

- **Wasilisha PR kamili**: Hakikisha faili zote zilizotafsiriwa za sehemu moja ziko katika PR moja. Hatukubali tafsiri zisizokamilika kwa sehemu moja. Unapowasilisha PR ya tafsiri, hakikisha folda ya tafsiri ina tafsiri za faili zote za folda ya asili.

### Miongozo ya Uandishi

Ili kuhakikisha muafaka katika nyaraka zote, tafadhali tumia miongozo ifuatayo:

- **Uwekaji wa URL**: Weka URL zote katika mabano ya mraba ikifuatiwa na mabano ya mviringo, bila nafasi za ziada ndani au nje yao. Kwa mfano: `[example](https://www.microsoft.com)`.

- **Viungo vya uhusiano**: Tumia `./` kwa viungo vya uhusiano vinavyoelekeza kwa faili au folda katika saraka ya sasa, na `../` kwa zile zinazoko saraka ya juu. Kwa mfano: `[example](../../path/to/file)` au `[example](../../../path/to/file)`.

- **Lugha zisizo za nchi fulani**: Hakikisha viungo vyako havijumuishi lugha za nchi fulani. Kwa mfano, epuka `/en-us/` au `/en/`.

- **Uhifadhi wa picha**: Hifadhi picha zote katika folda ya `./imgs`.

- **Majina ya picha yenye maelezo**: Panga majina ya picha kwa kutumia herufi za Kiingereza, nambari, na dashes. Kwa mfano: `example-image.jpg`.

## Mifumo ya Kazi ya GitHub

Unapowasilisha ombi la kuvuta, mifumo ifuatayo ya kazi itaanzishwa kuthibitisha mabadiliko. Fuata maelekezo hapa chini kuhakikisha ombi lako la kuvuta linapita ukaguzi wa mfumo wa kazi:

- [Angalia Njia za Uhusiano Zilizovunjika](../..)
- [Angalia URL Hazina Lugha ya Nchi](../..)

### Angalia Njia za Uhusiano Zilizovunjika

Mfumo huu wa kazi unahakikisha kwamba njia zote za uhusiano katika faili zako ni sahihi.

1. Ili kuhakikisha viungo vyako vinafanya kazi vizuri, fanya yafuatayo ukitumia VS Code:
    - Elekeza mshale juu ya kiungo chochote katika faili zako.
    - Bonyeza **Ctrl + Bonyeza** ili kwenda kwenye kiungo.
    - Ikiwa unabonyeza kiungo na hakifanyi kazi eneo lako, mfumo wa kazi utaanzishwa na kiungo hakitafanya kazi GitHub.

1. Ili kurekebisha tatizo hili, fanya yafuatayo ukitumia mapendekezo ya njia yanayotolewa na VS Code:
    - Andika `./` au `../`.
    - VS Code itakuomba uchague kutoka kwenye chaguzi zinazopatikana kulingana na uliyoyaandika.
    - Fuata njia kwa kubonyeza faili au folda unayotaka kuhakikisha njia yako ni sahihi.

Mara baada ya kuongeza njia sahihi ya uhusiano, hifadhi na tuma mabadiliko yako.

### Angalia URL Hazina Lugha ya Nchi

Mfumo huu wa kazi unahakikisha kuwa URL yoyote ya wavuti haina lugha ya nchi fulani. Kwa kuwa ghala hili linaweza kufikiwa duniani kote, ni muhimu kuhakikisha kuwa URL hazina lugha ya nchi yako.

1. Ili kuthibitisha kuwa URL zako hazina lugha za nchi, fanya yafuatayo:

    - Angalia maandishi kama `/en-us/`, `/en/`, au lugha nyingine yoyote katika URL.
    - Ikiwa haya hayapo kwenye URL zako, basi utapita ukaguzi huu.

1. Ili kurekebisha tatizo hili, fanya yafuatayo:
    - Fungua faili iliyoonyeshwa na mfumo wa kazi.
    - Ondoa lugha ya nchi kutoka kwenye URL.

Mara baada ya kuondoa lugha ya nchi, hifadhi na tuma mabadiliko yako.

### Angalia URL Zilizovunjika

Mfumo huu wa kazi unahakikisha kuwa URL yoyote ya wavuti katika faili zako inafanya kazi na kurudisha msimbo wa hali 200.

1. Ili kuthibitisha kuwa URL zako zinafanya kazi ipasavyo, fanya yafuatayo:
    - Angalia hali ya URL katika faili zako.

2. Ili kurekebisha URL yoyote iliyovunjika, fanya yafuatayo:
    - Fungua faili lenye URL iliyovunjika.
    - Sasisha URL kwa ile sahihi.

Mara baada ya kurekebisha URL, hifadhi na tuma mabadiliko yako.

> [!NOTE]
>
> Huenda kuwe na visa ambapo ukaguzi wa URL unashindwa ingawa kiungo kiko hai. Hii inaweza kutokea kwa sababu kadhaa, zikiwemo:
>
> - **Vizuizi vya mtandao:** Seva za vitendo vya GitHub zinaweza kuwa na vizuizi vya mtandao vinavyozuia ufikiaji wa URL fulani.
> - **Muda wa kusubiri (timeout):** URL zinazochukua muda mrefu kujibu zinaweza kusababisha hitilafu ya muda wa kusubiri katika mfumo wa kazi.
> - **Tatizo la seva kwa muda mfupi:** Kushindwa kwa seva mara kwa mara au matengenezo kunaweza kufanya URL isipatikane kwa muda wakati wa ukaguzi.

**Kandido**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo halali. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inashauriwa. Hatuwezi kuwajibika kwa kutoelewana au tafsiri potofu zitokanazo na matumizi ya tafsiri hii.