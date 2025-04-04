<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "212531c5722978740dcfb73e3995cbba",
  "translation_date": "2025-04-04T11:16:32+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "mo"
}
-->
# Contributing

Yi proyek a amana sababin da ba da shawara. Yawancin gudummawa suna bukatar ku amince da Yarjejeniyar Lasisin Gudummawa (CLA) wanda ke bayyana cewa kuna da haƙƙi kuma kuna ba mu haƙƙin amfani da gudummawarku. Don ƙarin bayani, ziyarci [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Lokacin da kuka gabatar da buƙatar ɗaukarwa, bot na CLA zai ta atomatik tantance ko kuna buƙatar bayar da CLA kuma ya yi wa PR ɗinku alama (misali, binciken matsayi, sharhi). Kawai bi umarnin da bot ɗin ya bayar. Za ku yi wannan sau ɗaya kawai a duk gidajen adana da ke amfani da CLA ɗinmu.

## Dokokin Halayya

Yi wannan aikin ya ɗauki [Dokokin Halayya na Buɗaɗɗen Tushen Microsoft](https://opensource.microsoft.com/codeofconduct/). Don ƙarin bayani karanta [Tambayoyin FAQ na Dokokin Halayya](https://opensource.microsoft.com/codeofconduct/faq/) ko tuntuɓi [opencode@microsoft.com](mailto:opencode@microsoft.com) tare da kowanne karin tambayoyi ko sharhi.

## Gargadi ga ƙirƙirar matsaloli

Don Allah kada ku buɗe matsalolin GitHub don tambayoyin tallafi na gama-gari domin jerin GitHub ya kamata a yi amfani da shi don buƙatun fasali da rahoton kurakurai. Wannan hanyar za mu iya bin diddigin matsaloli ko kurakurai daga lambar kuma mu raba tattaunawar gama-gari daga ainihin lambar.

## Yadda za a ba da gudummawa

### Jagororin Buƙatar Ɗaukarwa

Lokacin da kuke gabatar da buƙatar ɗaukarwa (PR) zuwa rumbun Phi-3 CookBook, don Allah yi amfani da waɗannan jagororin:

- **Yi Fork na Rumbun**: Kullum yi fork na rumbun zuwa asusunku kafin yin gyare-gyarenku.

- **Raba buƙatun ɗaukarwa (PR)**:
  - Gabatar da kowanne nau'in canji cikin buƙatar ɗaukarwa daban-daban. Misali, gyaran kurakurai da sabunta takardu ya kamata a gabatar cikin PR daban-daban.
  - Gyaran rubutu da ƙananan sabunta takardu za a iya haɗawa cikin PR ɗaya idan ya dace.

- **Magance rikice-rikicen haɗawa**: Idan buƙatar ɗaukarwarku ta nuna rikice-rikice, sabunta reshen `main` na gida don yin kama da babban rumbun kafin yin gyare-gyarenku.

- **Gabatar da fassarar**: Lokacin gabatar da PR na fassara, tabbatar da cewa babban fayil na fassara ya haɗa da fassarorin dukkan fayilolin cikin babban fayil ɗin asali.

### Jagororin Fassara

> [!IMPORTANT]
>
> Lokacin fassara rubutu cikin wannan rumbun, kada ku yi amfani da fassarar injin. Kawai yi wa fassara cikin harsunan da kuke da ƙwarewa.

Idan kun ƙware cikin wani harshe wanda ba Ingilishi ba, zaku iya taimakawa wajen fassara abun ciki. Bi waɗannan matakan don tabbatar da cewa gudummawar fassarar ku an haɗa su yadda ya kamata, don Allah yi amfani da waɗannan jagororin:

- **Ƙirƙiri babban fayil na fassara**: Ku je zuwa babban fayil na sashe mai dacewa ku ƙirƙiri babban fayil na fassara don harshen da kuke bayarwa. Misali:
  - Don sashen gabatarwa: `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - Don sashen farawa mai sauri: `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Ci gaba da wannan tsarin don sauran sassa (03.Inference, 04.Finetuning, da sauransu.)

- **Sabunta hanyoyin dangantaka**: Lokacin fassara, daidaita tsarin babban fayil ta hanyar ƙara `../../` zuwa farkon hanyoyin dangantaka cikin fayilolin markdown don tabbatar da cewa haɗin suna aiki yadda ya kamata. Misali, canza kamar haka:
  - Canza `(../../imgs/01/phi3aisafety.png)` zuwa `(../../../../imgs/01/phi3aisafety.png)`

- **Tsara fassarar ku**: Kowanne fayil na fassara ya kamata a sanya shi cikin babban fayil na fassarar sashe mai dacewa. Misali, idan kuna fassara sashen gabatarwa zuwa Spanish, zaku ƙirƙiri kamar haka:
  - `PhiCookBook/md/01.Introduce/translations/es/`

- **Gabatar da PR mai cikakke**: Tabbatar cewa dukkan fayilolin fassara na sashe ɗaya sun haɗa cikin PR ɗaya. Ba mu karɓi fassarar da ba ta cika ba don sashe ɗaya. Lokacin gabatar da PR na fassara, tabbatar da cewa babban fayil na fassara ya haɗa da fassarorin dukkan fayilolin cikin babban fayil ɗin asali.

### Jagororin Rubutu

Don tabbatar da daidaito a dukkan takardu, don Allah yi amfani da waɗannan jagororin:

- **Tsarin URL**: Ku ɗaure dukkan URLs cikin murabba'in madauwari sannan ku bi su da baka, ba tare da kowanne sarari mai yawa a kusa da ko cikin su ba. Misali: `[example](https://www.microsoft.com)`.

- **Hanyoyin dangantaka**: Yi amfani da `./` don hanyoyin dangantaka da ke nuna fayiloli ko manyan fayiloli cikin babban fayil na yanzu, da `../` don waɗanda ke cikin babban fayil na iyaye. Misali: `[example](../../path/to/file)` ko `[example](../../../path/to/file)`.

- **Ba na ƙasashe masu takamaiman yanki**: Tabbatar cewa haɗin ku ba su haɗa da yankin ƙasa mai takamaiman yanki. Misali, guji `/en-us/` ko `/en/`.

- **Ajiyar hotuna**: Ajiye dukkan hotuna cikin babban fayil na `./imgs`.

- **Sunan hotuna mai bayyana**: Sanya hotuna da sunaye masu bayyana ta amfani da haruffan Ingilishi, lambobi, da dashes. Misali: `example-image.jpg`.

## Tsarin Aiki na GitHub

Lokacin da kuka gabatar da buƙatar ɗaukarwa, za a kunna tsarin aiki na gaba don tantance canje-canje. Bi umarnin da ke ƙasa don tabbatar da cewa buƙatar ɗaukarwarku ta wuce binciken tsarin aiki:

- [Duba Hanyoyin Dangantaka Masu Lalacewa](../..)
- [Duba URLs Ba Su Da Yankin Yanki](../..)

### Duba Hanyoyin Dangantaka Masu Lalacewa

Wannan tsarin aiki yana tabbatar da cewa duk hanyoyin dangantaka cikin fayilolinku sun yi daidai.

1. Don tabbatar da cewa haɗin ku suna aiki yadda ya kamata, yi waɗannan ayyukan ta amfani da VS Code:
    - Hover akan kowanne haɗi cikin fayilolinku.
    - Danna **Ctrl + Click** don zuwa haɗin.
    - Idan kun danna kan haɗin kuma bai yi aiki a gida ba, zai kunna tsarin aiki kuma ba zai yi aiki a GitHub ba.

1. Don gyara wannan matsalar, yi waɗannan ayyukan ta amfani da shawarwarin hanya da VS Code ya bayar:
    - Rubuta `./` ko `../`.
    - VS Code zai nuna muku zaɓuɓɓuka bisa abin da kuka rubuta.
    - Bi hanyar ta danna kan fayil ko babban fayil mai so don tabbatar da cewa hanyar ku ta yi daidai.

Da zarar kun ƙara hanyar dangantaka mai dacewa, adana ku turawa canje-canjeku.

### Duba URLs Ba Su Da Yankin Yanki

Wannan tsarin aiki yana tabbatar da cewa dukkan URLs na yanar gizo ba su haɗa da yankin ƙasa mai takamaiman yanki. Tunda wannan rumbun yana samuwa a duniya, yana da mahimmanci a tabbatar da cewa URLs ba su ƙunshi yankin ƙasar ku ba.

1. Don tabbatar da cewa URLs ɗinku ba su da yankin ƙasa, yi waɗannan ayyukan:

    - Duba rubutu kamar `/en-us/`, `/en/`, ko kowanne yanki na harshe cikin URLs.

    - Idan waɗannan ba su kasance cikin URLs ɗinku ba, za ku wuce wannan binciken.

1. Don gyara wannan matsalar, yi waɗannan ayyukan:
    - Buɗe hanyar fayil ɗin da tsarin aiki ya nuna.
    - Cire yankin ƙasa daga URLs.

Da zarar kun cire yankin ƙasa, adana ku turawa canje-canjeku.

### Duba URLs Masu Lalacewa

Wannan tsarin aiki yana tabbatar da cewa dukkan URLs na yanar gizo cikin fayilolinku suna aiki kuma suna dawo da lambar matsayi 200.

1. Don tabbatar da cewa URLs ɗinku suna aiki yadda ya kamata, yi waɗannan ayyukan:
    - Duba matsayi na URLs cikin fayilolinku.

2. Don gyara URLs masu lalacewa, yi waɗannan ayyukan:
    - Buɗe fayil ɗin da ke ƙunshe da URL mai lalacewa.
    - Sabunta URL zuwa mai daidai.

Da zarar kun gyara URLs, adana ku turawa canje-canjeku.

> [!NOTE]
>
> Akwai lokuta da binciken URL zai kasa duk da cewa haɗin yana samuwa. Wannan na iya faruwa saboda dalilai da dama, ciki har da:
>
> - **Ƙuntatawar yanar gizo:** Sabis na aikin GitHub na iya samun ƙuntatawar yanar gizo wanda ke hana samun wasu URLs.
> - **Matsalar lokaci:** URLs waɗanda suka ɗauki lokaci mai tsawo don amsawa na iya kunna kuskuren lokaci a cikin tsarin aiki.
> - **Matsalolin uwar garke na ɗan lokaci:** Lokaci-lokaci uwar garke na iya zama ba samuwa ba na ɗan lokaci yayin tantancewa.

It seems you are asking for a translation to "mo," but could you clarify what "mo" refers to? Are you referring to a specific language or dialect? For example, Māori, Marshallese, or another language?