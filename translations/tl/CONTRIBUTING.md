# Contributing

Malugod na tinatanggap ng proyektong ito ang mga kontribusyon at suhestiyon. Karamihan sa mga kontribusyon ay nangangailangan na sumang-ayon ka sa isang Contributor License Agreement (CLA) na nagsasaad na may karapatan ka, at talagang binibigyan mo kami, ng mga karapatan na gamitin ang iyong kontribusyon. Para sa mga detalye, bisitahin ang [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Kapag nagsumite ka ng pull request, awtomatikong malalaman ng CLA bot kung kailangan mong magbigay ng CLA at bibigyan ng angkop na marka ang PR (hal., status check, komento). Sundin lamang ang mga tagubiling ibibigay ng bot. Isang beses mo lang ito kailangang gawin para sa lahat ng repos na gumagamit ng aming CLA.

## Code of Conduct

Inampon ng proyektong ito ang [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).  
Para sa karagdagang impormasyon, basahin ang [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) o makipag-ugnayan sa [opencode@microsoft.com](mailto:opencode@microsoft.com) para sa anumang karagdagang tanong o komento.

## Cautions for creating issues

Mangyaring huwag magbukas ng mga GitHub issues para sa mga pangkalahatang tanong sa suporta dahil ang listahan sa GitHub ay dapat gamitin para sa mga kahilingan sa tampok at mga ulat ng bug. Sa ganitong paraan, mas madali naming matutunton ang mga totoong isyu o bug mula sa code at mapanatili ang pangkalahatang talakayan na hiwalay sa aktwal na code.

## How to Contribute

### Pull Requests Guidelines

Kapag nagsusumite ng pull request (PR) sa Phi-3 CookBook repository, pakigamit ang mga sumusunod na gabay:

- **I-fork ang Repository**: Palaging i-fork ang repository sa iyong sariling account bago gawin ang mga pagbabago.

- **Hiwalay na pull requests (PR)**:
  - Isumite ang bawat uri ng pagbabago sa sarili nitong pull request. Halimbawa, ang mga pag-aayos ng bug at mga update sa dokumentasyon ay dapat isumite sa magkahiwalay na PR.
  - Ang mga pag-aayos ng typo at maliliit na update sa dokumentasyon ay maaaring pagsamahin sa isang PR kung naaangkop.

- **Ayusin ang mga merge conflict**: Kung nagpapakita ng merge conflicts ang iyong pull request, i-update ang iyong lokal na `main` branch upang tumugma sa pangunahing repository bago gawin ang mga pagbabago.

- **Pagsumite ng mga pagsasalin**: Kapag nagsusumite ng translation PR, siguraduhing kasama sa translation folder ang mga pagsasalin para sa lahat ng mga file sa orihinal na folder.

### Writing Guidelines

Upang matiyak ang pagkakapare-pareho sa lahat ng dokumento, pakigamit ang mga sumusunod na gabay:

- **Pag-format ng URL**: Balutin ang lahat ng URL sa mga panaklong na parisukat na sinusundan ng panaklong na bilog, nang walang dagdag na espasyo sa paligid o loob nito. Halimbawa: `[example](https://www.microsoft.com)`.

- **Relative links**: Gamitin ang `./` para sa mga relative link na tumutukoy sa mga file o folder sa kasalukuyang direktoryo, at `../` para sa mga nasa parent directory. Halimbawa: `[example](../../path/to/file)` o `[example](../../../path/to/file)`.

- **Hindi Country-Specific na mga locale**: Siguraduhing ang iyong mga link ay hindi naglalaman ng mga country-specific na locale. Halimbawa, iwasan ang `/en-us/` o `/en/`.

- **Pag-iimbak ng mga larawan**: Itago ang lahat ng mga larawan sa `./imgs` na folder.

- **Deskriptibong mga pangalan ng larawan**: Pangalanan ang mga larawan nang deskriptibo gamit ang mga English na karakter, numero, at gitling. Halimbawa: `example-image.jpg`.

## GitHub Workflows

Kapag nagsumite ka ng pull request, ang mga sumusunod na workflows ay awtomatikong tatakbo upang suriin ang mga pagbabago. Sundin ang mga tagubiling nasa ibaba upang matiyak na pumasa ang iyong pull request sa mga workflow check:

- [Check Broken Relative Paths](../..)
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

Tinitiyak ng workflow na ito na lahat ng relative paths sa iyong mga file ay tama.

1. Upang matiyak na gumagana nang maayos ang iyong mga link, gawin ang mga sumusunod gamit ang VS Code:
    - I-hover ang cursor sa anumang link sa iyong mga file.
    - Pindutin ang **Ctrl + Click** upang pumunta sa link.
    - Kung hindi gumana ang link kapag kinlik mo ito nang lokal, magti-trigger ito ng workflow at hindi gagana sa GitHub.

1. Upang ayusin ang isyung ito, gawin ang mga sumusunod gamit ang mga path suggestion na ibinibigay ng VS Code:
    - I-type ang `./` o `../`.
    - Hihilingin sa iyo ng VS Code na pumili mula sa mga available na opsyon base sa iyong tinype.
    - Sundan ang path sa pamamagitan ng pag-click sa nais na file o folder upang matiyak na tama ang iyong path.

Kapag naidagdag mo na ang tamang relative path, i-save at i-push ang iyong mga pagbabago.

### Check URLs Don't Have Locale

Tinitiyak ng workflow na ito na walang web URL na naglalaman ng country-specific na locale. Dahil ang repository na ito ay naa-access sa buong mundo, mahalagang tiyakin na ang mga URL ay walang locale ng iyong bansa.

1. Upang suriin na walang country locale ang iyong mga URL, gawin ang mga sumusunod:

    - Hanapin ang mga teksto tulad ng `/en-us/`, `/en/`, o anumang iba pang language locale sa mga URL.
    - Kung wala ang mga ito sa iyong mga URL, pumasa ka sa check na ito.

1. Upang ayusin ang isyung ito, gawin ang mga sumusunod:
    - Buksan ang file path na tinukoy ng workflow.
    - Alisin ang country locale mula sa mga URL.

Kapag naalis mo na ang country locale, i-save at i-push ang iyong mga pagbabago.

### Check Broken Urls

Tinitiyak ng workflow na ito na ang anumang web URL sa iyong mga file ay gumagana at nagbabalik ng 200 status code.

1. Upang suriin na gumagana nang tama ang iyong mga URL, gawin ang mga sumusunod:
    - Suriin ang status ng mga URL sa iyong mga file.

2. Upang ayusin ang mga sirang URL, gawin ang mga sumusunod:
    - Buksan ang file na naglalaman ng sirang URL.
    - I-update ang URL sa tamang address.

Kapag naayos mo na ang mga URL, i-save at i-push ang iyong mga pagbabago.

> [!NOTE]
>
> Maaaring may mga pagkakataon na mabigo ang URL check kahit na naa-access ang link. Ito ay maaaring mangyari dahil sa ilang mga dahilan, kabilang ang:
>
> - **Mga limitasyon sa network:** Maaaring may mga network restrictions ang mga GitHub actions server na pumipigil sa pag-access sa ilang URL.
> - **Timeout issues:** Ang mga URL na matagal mag-reply ay maaaring mag-trigger ng timeout error sa workflow.
> - **Pansamantalang problema sa server:** Paminsan-minsang downtime o maintenance ng server ay maaaring magpahinto pansamantala sa URL habang sinusuri.

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.