<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-07-17T02:19:55+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "fi"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

## Yleiskatsaus

Interactive Phi 3 Mini 4K Instruct Chatbot on työkalu, jonka avulla käyttäjät voivat olla vuorovaikutuksessa Microsoft Phi 3 Mini 4K instruct -demolla tekstin tai äänen avulla. Chatbottia voi käyttää monenlaisiin tehtäviin, kuten kääntämiseen, sääpäivityksiin ja yleiseen tiedonhakuun.

### Aloittaminen

Käyttääksesi tätä chatbotia, noudata seuraavia ohjeita:

1. Avaa uusi [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. Muistikirjan pääikkunassa näet chat-ikkunan, jossa on tekstinsyöttökenttä ja "Send"-painike.
3. Käyttääksesi tekstipohjaista chatbotia, kirjoita viestisi tekstikenttään ja klikkaa "Send"-painiketta. Chatbot vastaa äänitiedostolla, jonka voi toistaa suoraan muistikirjassa.

**Note**: Tämä työkalu vaatii GPU:n sekä pääsyn Microsoft Phi-3 ja OpenAI Whisper -malleihin, joita käytetään puheentunnistukseen ja kääntämiseen.

### GPU-vaatimukset

Tämän demon suorittamiseen tarvitset 12 Gt GPU-muistia.

Muistivaatimukset **Microsoft-Phi-3-Mini-4K instruct** -demon ajamiseen GPU:lla riippuvat useista tekijöistä, kuten syötteen koosta (ääni tai teksti), käännöskielestä, mallin nopeudesta ja GPU:n käytettävissä olevasta muistista.

Yleisesti Whisper-malli on suunniteltu toimimaan GPU:lla. Suositeltu vähimmäismuisti Whisper-mallin ajamiseen on 8 Gt, mutta se pystyy hyödyntämään suurempaa muistimäärää tarvittaessa.

On tärkeää huomioida, että suuren datamäärän tai suuren pyyntömääärän käsittely mallilla voi vaatia enemmän GPU-muistia ja/tai aiheuttaa suorituskykyongelmia. Suosittelemme testaamaan käyttötapauksesi eri asetuksilla ja seuraamaan muistin käyttöä optimaalisten asetusten löytämiseksi.

## E2E-esimerkki Interactive Phi 3 Mini 4K Instruct Chatbotin ja Whisperin kanssa

Jupyter-muistikirja nimeltä [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) näyttää, miten Microsoft Phi 3 Mini 4K instruct Demoa käytetään tekstin luomiseen ääni- tai kirjoitetusta tekstisyötteestä. Muistikirjassa määritellään useita funktioita:

1. `tts_file_name(text)`: Tämä funktio luo tiedostonimen syötetyn tekstin perusteella tallentaakseen luodun äänitiedoston.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Tämä funktio käyttää Edge TTS -APIa luodakseen äänitiedoston syötetyn tekstin paloista. Syöteparametreina ovat tekstipalojen lista, puhenopeus, äänen nimi ja polku, johon äänitiedosto tallennetaan.
1. `talk(input_text)`: Tämä funktio luo äänitiedoston käyttämällä Edge TTS -APIa ja tallentaa sen satunnaisella tiedostonimellä /content/audio-kansioon. Syötteenä on puheeksi muutettava teksti.
1. `run_text_prompt(message, chat_history)`: Tämä funktio käyttää Microsoft Phi 3 Mini 4K instruct -demoa luodakseen äänitiedoston viestisyötteestä ja lisää sen keskusteluhistoriaan.
1. `run_audio_prompt(audio, chat_history)`: Tämä funktio muuntaa äänitiedoston tekstiksi Whisper-mallin APIa käyttäen ja välittää sen `run_text_prompt()`-funktiolle.
1. Koodi käynnistää Gradio-sovelluksen, jonka avulla käyttäjät voivat olla vuorovaikutuksessa Phi 3 Mini 4K instruct -demon kanssa joko kirjoittamalla viestejä tai lataamalla äänitiedostoja. Tulokset näytetään tekstiviestinä sovelluksessa.

## Vianmääritys

Cuda GPU -ajureiden asennus

1. Varmista, että Linux-sovelluksesi ovat ajan tasalla

    ```bash
    sudo apt update
    ```

1. Asenna Cuda-ajurit

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Rekisteröi cuda-ajurin sijainti

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Tarkista Nvidia GPU:n muistimäärä (vaaditaan 12 Gt GPU-muistia)

    ```bash
    nvidia-smi
    ```

1. Tyhjennä välimuisti: Jos käytät PyTorchia, voit kutsua torch.cuda.empty_cache() vapauttaaksesi käyttämättömän välimuistin, jotta muut GPU-sovellukset voivat käyttää sitä

    ```python
    torch.cuda.empty_cache() 
    ```

1. Tarkista Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Suorita seuraavat toimenpiteet luodaksesi Hugging Face -tokenin.

    - Siirry [Hugging Face Token Settings -sivulle](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Valitse **New token**.
    - Anna projektille haluamasi **Name**.
    - Valitse **Type** arvoksi **Write**.

> **Note**
>
> Jos kohtaat seuraavan virheen:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Ratkaistaksesi tämän, kirjoita seuraava komento terminaaliisi.
>
> ```bash
> sudo ldconfig
> ```

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.