## Tervetuloa Phi-laboratorioihin C#:lla

Tarjolla on valikoima laboratorioita, jotka esittelevät, miten eri versioita Phi-malleista voidaan integroida tehokkaasti .NET-ympäristöön.

## Vaatimukset

Ennen esimerkin suorittamista varmista, että sinulla on asennettuna seuraavat:

**.NET 9:** Varmista, että koneellasi on asennettuna [uusin .NET-versio](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo).

**(Valinnainen) Visual Studio tai Visual Studio Code:** Tarvitset IDE:n tai koodieditorin, joka pystyy ajamaan .NET-projekteja. Suositeltuja ovat [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) tai [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo).

**Käyttämällä git:** kloonaa paikallisesti jokin saatavilla olevista Phi-3, Phi3.5 tai Phi-4 versioista osoitteesta [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**Lataa Phi-4 ONNX -mallit** paikalliselle koneellesi:

### siirry kansioon, johon tallennat mallit

```bash
cd c:\phi\models
```

### lisää tuki lfs:lle

```bash
git lfs install 
```

### kloonaa ja lataa Phi-4 mini instruct -malli ja Phi-4 multimodaalinen malli

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Lataa Phi-3 ONNX -mallit** paikalliselle koneellesi:

### kloonaa ja lataa Phi-3 mini 4K instruct -malli ja Phi-3 vision 128K -malli

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Tärkeää:** Nykyiset demot on suunniteltu käyttämään mallin ONNX-versioita. Edelliset vaiheet kloonaavat seuraavat mallit.

## Laboratorioista

Pääratkaisussa on useita esimerkkilaboratorioita, jotka demonstroivat Phi-mallien ominaisuuksia C#:lla.

| Projekti | Malli | Kuvaus |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 tai Phi-3.5 | Esimerkkikeskustelu konsolissa, jossa käyttäjä voi esittää kysymyksiä. Projekti lataa paikallisen ONNX Phi-3 -mallin käyttäen `Microsoft.ML.OnnxRuntime` -kirjastoja. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 tai Phi-3.5 | Esimerkkikeskustelu konsolissa, jossa käyttäjä voi esittää kysymyksiä. Projekti lataa paikallisen ONNX Phi-3 -mallin käyttäen `Microsoft.Semantic.Kernel` -kirjastoja. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 tai Phi-3.5 | Tämä on esimerkkiprojekti, joka käyttää paikallista phi3 vision -mallia kuvien analysointiin. Projekti lataa paikallisen ONNX Phi-3 Vision -mallin käyttäen `Microsoft.ML.OnnxRuntime` -kirjastoja. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 tai Phi-3.5 | Tämä on esimerkkiprojekti, joka käyttää paikallista phi3 vision -mallia kuvien analysointiin. Projekti lataa paikallisen ONNX Phi-3 Vision -mallin käyttäen `Microsoft.ML.OnnxRuntime` -kirjastoja. Projekti tarjoaa myös valikon eri vaihtoehdoilla käyttäjän kanssa vuorovaikutukseen. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Esimerkkikeskustelu konsolissa, jossa käyttäjä voi esittää kysymyksiä. Projekti lataa paikallisen ONNX Phi-4 -mallin käyttäen `Microsoft.ML.OnnxRuntime` -kirjastoja. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Esimerkkikeskustelu konsolissa, jossa käyttäjä voi esittää kysymyksiä. Projekti lataa paikallisen ONNX Phi-4 -mallin käyttäen `Semantic Kernel` -kirjastoja. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Esimerkkikeskustelu konsolissa, jossa käyttäjä voi esittää kysymyksiä. Projekti lataa paikallisen ONNX Phi-4 -mallin käyttäen `Microsoft.ML.OnnxRuntimeGenAI` -kirjastoja ja toteuttaa `IChatClient`-rajapinnan `Microsoft.Extensions.AI`:sta. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Esimerkkikeskustelu konsolissa, jossa käyttäjä voi esittää kysymyksiä. Keskustelu sisältää muistin. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | Tämä on esimerkkiprojekti, joka käyttää paikallista Phi-4 -mallia kuvien analysointiin ja näyttää tulokset konsolissa. Projekti lataa paikallisen Phi-4-`multimodal-instruct-onnx` -mallin käyttäen `Microsoft.ML.OnnxRuntime` -kirjastoja. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | Tämä on esimerkkiprojekti, joka käyttää paikallista Phi-4 -mallia äänitiedoston analysointiin, luo tiedostosta tekstityksen ja näyttää tuloksen konsolissa. Projekti lataa paikallisen Phi-4-`multimodal-instruct-onnx` -mallin käyttäen `Microsoft.ML.OnnxRuntime` -kirjastoja. |

## Projektien suorittaminen

Suorittaaksesi projektit, toimi seuraavasti:

1. Kloonaa repositorio paikalliselle koneellesi.

1. Avaa terminaali ja siirry haluamaasi projektiin. Esimerkiksi suoritetaan `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Suorita projekti komennolla

    ```bash
    dotnet run
    ```

1. Esimerkkiprojekti pyytää käyttäjältä syötteen ja vastaa paikallisen mallin avulla.

   Suoritettava demo näyttää suunnilleen tältä:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.