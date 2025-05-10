<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f71f15fee9a73ecfcd4fd40efbe3070",
  "translation_date": "2025-05-09T03:42:56+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "tl"
}
-->
# Contributing

Malugod na tinatanggap ng proyektong ito ang mga kontribusyon at mungkahi. Karamihan sa mga kontribusyon ay nangangailangan ng iyong pagsang-ayon sa isang Contributor License Agreement (CLA) na nagsasaad na ikaw ay may karapatan, at talagang nagbibigay sa amin ng karapatan na gamitin ang iyong kontribusyon. Para sa mga detalye, bisitahin ang [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Kapag nagsumite ka ng pull request, awtomatikong tutukuyin ng CLA bot kung kailangan mong magbigay ng CLA at aayusin ang PR nang naaayon (hal., status check, komento). Sundin lamang ang mga tagubiling ibinibigay ng bot. Isang beses mo lang ito kailangang gawin para sa lahat ng repos na gumagamit ng aming CLA.

## Code of Conduct

Inampon ng proyektong ito ang [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). Para sa karagdagang impormasyon, basahin ang [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) o makipag-ugnayan sa [opencode@microsoft.com](mailto:opencode@microsoft.com) para sa anumang karagdagang tanong o komento.

## Mga Paalala sa Paggawa ng Isyu

Mangyaring huwag magbukas ng GitHub issues para sa pangkalahatang mga tanong sa suporta dahil ang listahan sa GitHub ay dapat gamitin para sa mga feature request at ulat ng bug. Sa ganitong paraan, mas madali naming masusubaybayan ang mga totoong isyu o bug mula sa code at mapanatili ang pangkalahatang talakayan na hiwalay sa aktwal na code.

## Paano Mag-ambag

### Mga Patnubay sa Pull Requests

Kapag nagsusumite ng pull request (PR) sa Phi-3 CookBook repository, mangyaring sundin ang mga sumusunod na patnubay:

- **I-fork ang Repository**: Laging i-fork ang repository sa iyong sariling account bago gawin ang mga pagbabago.

- **Ihiwalay na pull requests (PR)**:
  - Isumite ang bawat uri ng pagbabago sa sarili nitong pull request. Halimbawa, ang mga pag-aayos ng bug at mga update sa dokumentasyon ay dapat isumite sa magkahiwalay na PR.
  - Ang mga pagwawasto ng typo at maliliit na update sa dokumentasyon ay maaaring pagsamahin sa isang PR kung naaangkop.

- **Ayusin ang mga merge conflict**: Kung nagpapakita ng merge conflicts ang iyong pull request, i-update ang iyong lokal na `main` branch upang tumugma sa pangunahing repository bago gawin ang mga pagbabago.

- **Pagsusumite ng mga salin**: Kapag nagsusumite ng translation PR, tiyakin na ang translation folder ay may kasamang salin para sa lahat ng mga file sa orihinal na folder.

### Mga Patnubay sa Pagsasalin

> [!IMPORTANT]
>
> Kapag nagsasalin ng teksto sa repositoryong ito, huwag gumamit ng machine translation. Mag-volunteer lamang para sa mga pagsasalin sa mga wikang bihasa ka.

Kung bihasa ka sa isang wikang hindi Ingles, maaari kang tumulong na isalin ang nilalaman. Sundin ang mga hakbang na ito upang matiyak na maayos na maisasama ang iyong mga kontribusyon sa pagsasalin, mangyaring gamitin ang mga sumusunod na patnubay:

- **Gumawa ng translation folder**: Pumunta sa angkop na section folder at gumawa ng translation folder para sa wikang iyong kontribusyon. Halimbawa:
  - Para sa introduction section: `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - Para sa quick start section: `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Ipagpatuloy ang pattern na ito para sa iba pang mga seksyon (03.Inference, 04.Finetuning, atbp.)

- **I-update ang relative paths**: Kapag nagsasalin, ayusin ang folder structure sa pamamagitan ng pagdagdag ng `../../` sa simula ng mga relative path sa loob ng mga markdown file upang masigurong gumagana nang tama ang mga link. Halimbawa, palitan ang:
  - `(../../imgs/01/phi3aisafety.png)` sa `(../../../../imgs/01/phi3aisafety.png)`

- **Ayusin ang iyong mga salin**: Ang bawat isinaling file ay dapat ilagay sa katumbas na translation folder ng seksyon. Halimbawa, kung nagsasalin ka ng introduction section sa Spanish, gagawin mo ang sumusunod:
  - `PhiCookBook/md/01.Introduce/translations/es/`

- **Isumite ang kumpletong PR**: Siguraduhing lahat ng isinaling file para sa isang seksyon ay kasama sa isang PR. Hindi kami tumatanggap ng mga partial na pagsasalin para sa isang seksyon. Kapag nagsusumite ng translation PR, tiyakin na ang translation folder ay may kasamang lahat ng mga isinaling file mula sa orihinal na folder.

### Mga Patnubay sa Pagsusulat

Upang matiyak ang pagkakapare-pareho sa lahat ng dokumento, mangyaring gamitin ang mga sumusunod na patnubay:

- **Pag-format ng URL**: Balutin ang lahat ng URL sa mga square brackets na sinusundan ng parentheses, nang walang dagdag na espasyo sa paligid o loob nito. Halimbawa: `[example](https://www.microsoft.com)`.

- **Relative links**: Gamitin ang `./` para sa mga relative link na tumutukoy sa mga file o folder sa kasalukuyang direktoryo, at `../` para sa mga nasa parent directory. Halimbawa: `[example](../../path/to/file)` o `[example](../../../path/to/file)`.

- **Hindi Country-Specific na mga locale**: Siguraduhin na ang iyong mga link ay hindi naglalaman ng mga country-specific na locale. Halimbawa, iwasan ang `/en-us/` o `/en/`.

- **Imbakan ng mga larawan**: Ilagay ang lahat ng mga larawan sa folder na `./imgs`.

- **Deskriptibong pangalan ng larawan**: Pangalanan ang mga larawan nang deskriptibo gamit ang mga karakter sa Ingles, mga numero, at mga gitling. Halimbawa: `example-image.jpg`.

## GitHub Workflows

Kapag nagsumite ka ng pull request, ang mga sumusunod na workflows ay tatakbo upang i-validate ang mga pagbabago. Sundin ang mga tagubiling nasa ibaba upang matiyak na makapasa ang iyong pull request sa mga workflow check:

- [Check Broken Relative Paths](../..)
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

Tinitiyak ng workflow na ito na tama ang lahat ng relative path sa iyong mga file.

1. Para matiyak na gumagana nang maayos ang iyong mga link, gawin ang mga sumusunod na hakbang gamit ang VS Code:
    - I-hover ang anumang link sa iyong mga file.
    - Pindutin ang **Ctrl + Click** upang pumunta sa link.
    - Kung ang pag-click sa isang link ay hindi gumana nang lokal, magti-trigger ito ng workflow at hindi gagana sa GitHub.

1. Para ayusin ang isyung ito, gawin ang mga sumusunod na hakbang gamit ang mga path suggestion na ibinibigay ng VS Code:
    - I-type ang `./` o `../`.
    - Hihilingin ng VS Code na pumili ka mula sa mga available na opsyon base sa iyong tinype.
    - Sundan ang path sa pamamagitan ng pag-click sa nais na file o folder upang matiyak na tama ang iyong path.

Kapag naidagdag mo na ang tamang relative path, i-save at i-push ang iyong mga pagbabago.

### Check URLs Don't Have Locale

Tinitiyak ng workflow na ito na walang web URL na may kasamang country-specific locale. Dahil ang repositoryong ito ay accessible sa buong mundo, mahalagang matiyak na walang mga URL na naglalaman ng locale ng iyong bansa.

1. Para i-verify na walang country locale ang iyong mga URL, gawin ang mga sumusunod:

    - Hanapin ang mga teksto tulad ng `/en-us/`, `/en/`, o anumang ibang language locale sa mga URL.
    - Kung wala ito sa iyong mga URL, pasado ka sa check na ito.

1. Para ayusin ang isyung ito, gawin ang mga sumusunod:
    - Buksan ang file path na tinukoy ng workflow.
    - Alisin ang country locale mula sa mga URL.

Kapag natanggal mo na ang country locale, i-save at i-push ang iyong mga pagbabago.

### Check Broken Urls

Tinitiyak ng workflow na ito na gumagana ang anumang web URL sa iyong mga file at nagbibigay ng 200 status code.

1. Para i-verify na gumagana nang tama ang iyong mga URL, gawin ang mga sumusunod:
    - Suriin ang status ng mga URL sa iyong mga file.

2. Para ayusin ang anumang sirang URL, gawin ang mga sumusunod:
    - Buksan ang file na may sirang URL.
    - I-update ang URL sa tamang address.

Kapag naayos mo na ang mga URL, i-save at i-push ang iyong mga pagbabago.

> [!NOTE]
>
> Maaaring may mga pagkakataon na mabigo ang URL check kahit na accessible ang link. Ito ay maaaring mangyari dahil sa ilang mga dahilan, kabilang ang:
>
> - **Mga network restriction:** Maaaring may mga network restriction ang mga GitHub actions server na pumipigil sa pag-access sa ilang mga URL.
> - **Timeout issues:** Ang mga URL na matagal mag-response ay maaaring mag-trigger ng timeout error sa workflow.
> - **Pansamantalang problema sa server:** Paminsan-minsan, ang downtime o maintenance ng server ay maaaring magpahinto sa URL na ma-access pansamantala habang sinusuri.

**Pagsisiwalat**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na bahagi. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.