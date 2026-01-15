<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7f72d7981ed3640865700f51ae407da4",
  "translation_date": "2026-01-14T15:44:21+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "fi"
}
-->
# Interaktiivinen Phi 3 Mini 4K Instruct -chatbot Whisperillä

## Yleiskatsaus

Interaktiivinen Phi 3 Mini 4K Instruct -chatbot on työkalu, jonka avulla käyttäjät voivat olla vuorovaikutuksessa Microsoft Phi 3 Mini 4K instruct -demolla tekstin tai äänen avulla. Chatbotia voi käyttää monenlaisiin tehtäviin, kuten kääntämiseen, sääpäivityksiin ja yleiseen tiedonhakuun.

### Aloittaminen

Käyttääksesi tätä chatbotia noudata seuraavia ohjeita:

1. Avaa uusi [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. Muistikirjan pääikkunassa näet chat-ikkunan, jossa on tekstikenttä ja "Send"-painike.
3. Käyttääksesi tekstipohjaista chatbotia, kirjoita viestisi tekstikenttään ja klikkaa "Send"-painiketta. Chatbot vastaa äänitiedostolla, jonka voi toistaa suoraan muistikirjan sisällä.

**Huomautus**: Tämä työkalu vaatii GPU:n ja pääsyn Microsoft Phi-3- ja OpenAI Whisper -malleihin, joita käytetään puheentunnistukseen ja käännökseen.

### GPU-vaatimukset

Tämän demon suorittamiseen tarvitset 12 Gt GPU-muistia.

**Microsoft-Phi-3-Mini-4K instruct** -demon muistivaatimukset GPU:lla riippuvat useista tekijöistä, kuten syöteaineiston (ääni tai teksti) koosta, käännökseen käytettävästä kielestä, mallin nopeudesta ja GPU:n käytettävissä olevasta muistista.

Yleisesti Whisper-malli on suunniteltu pyörimään GPU:lla. Suositeltu vähimmäismäärä GPU-muistia Whisper-mallin ajoon on 8 Gt, mutta se voi käsitellä suurempaakin muistimäärää tarvittaessa.

On tärkeää huomata, että suuren datamäärän tai suuren pyyntömääärän käsitteleminen mallissa voi vaatia enemmän GPU-muistia ja/tai aiheuttaa suorituskykyongelmia. Suositellaan testaamaan käyttötapaasi eri kokoonpanoilla ja seuraamaan muistin käyttöä optimaalisimman asetuksen löytämiseksi juuri sinun tarpeisiisi.

## E2E-esimerkki interaktiivisesta Phi 3 Mini 4K Instruct -chatbotista Whisperillä

Jupyter-muistikirja nimeltä [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) demonstroi, kuinka Microsoft Phi 3 Mini 4K instruct Demoa käytetään tekstin luomiseen ääni- tai tekstisyötteestä. Muistikirjassa on määritelty useita toimintoja:

1. `tts_file_name(text)`: Tämä funktio generoi tiedostonimen syötteen tekstin perusteella luodun äänitiedoston tallentamista varten.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Tämä funktio käyttää Edge TTS -APIa luodakseen äänitiedoston syötetekstin paloista. Syötteenä ovat palojen lista, puhenopeus, äänen nimi ja tallennuspolku generoidulle äänitiedostolle.
1. `talk(input_text)`: Tämä funktio generoi äänitiedoston käyttämällä Edge TTS -APIa ja tallentaa sen satunnaiseen tiedostoon hakemistossa /content/audio. Syötteenä on puheeksi muunnettava teksti.
1. `run_text_prompt(message, chat_history)`: Tämä funktio käyttää Microsoft Phi 3 Mini 4K instruct -demoa luodakseen äänitiedoston viesti-syötteestä ja lisää sen keskusteluhistoriaan.
1. `run_audio_prompt(audio, chat_history)`: Tämä funktio muuntaa äänitiedoston tekstiksi Whisper-mallin API:n avulla ja antaa sen `run_text_prompt()` -funktiolle.
1. Koodi käynnistää Gradio-sovelluksen, joka mahdollistaa käyttäjien vuorovaikutuksen Phi 3 Mini 4K instruct -demon kanssa kirjoittamalla viestejä tai lataamalla äänitiedostoja. Tuloste näytetään tekstiviestinä sovelluksessa.

## Ongelmien ratkaisu

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

1. Tarkista Nvidia GPU:n muistin koko (vaadittu 12 Gt GPU-muistia)

    ```bash
    nvidia-smi
    ```

1. Tyhjennä välimuisti: Jos käytät PyTorchia, voit kutsua torch.cuda.empty_cache()-funktiota vapauttaaksesi kaiken käyttämättömän välimuistin, jotta muut GPU-sovellukset voivat käyttää sitä

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
    - Kirjoita käyttöön otettavan projektin **Nimi**.
    - Valitse **Type** arvoksi **Write**.

> [!NOTE]
>
> Jos kohtaat seuraavan virheen:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Ratkaistaksesi ongelman, kirjoita seuraava komento terminaaliisi.
>
> ```bash
> sudo ldconfig
> ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, ole hyvä ja huomioi, että automaattikäännöksissä voi esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulisi pitää luotettavana lähteenä. Tärkeissä tiedoissa suosittelemme ammattimaisen ihmiskääntäjän palvelujen käyttöä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->