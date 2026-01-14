<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a54cd3d65b6963e4e8ce21e143c3ab04",
  "translation_date": "2025-07-16T21:20:05+00:00",
  "source_file": "md/01.Introduction/03/Remote_Interence.md",
  "language_code": "fi"
}
-->
# Etäinferenzsi hienosäädetyllä mallilla

Kun adapterit on koulutettu etäympäristössä, käytä yksinkertaista Gradio-sovellusta mallin kanssa vuorovaikutukseen.

![Fine-tune complete](../../../../../translated_images/fi/log-finetuning-res.7b92254e7e822c7f.png)

### Azure-resurssien määrittäminen  
Sinun täytyy määrittää Azure-resurssit etäinferenzsiä varten suorittamalla `AI Toolkit: Provision Azure Container Apps for inference` komentopalettista. Tämän asetuksen aikana sinua pyydetään valitsemaan Azure-tilauksesi ja resurssiryhmäsi.  
![Provision Inference Resource](../../../../../translated_images/fi/command-provision-inference.467afc8d351642fc.png)

Oletuksena inferenssin tilaus ja resurssiryhmä tulisi olla samat kuin hienosäädössä käytetyt. Inferenssi käyttää samaa Azure Container App Environment -ympäristöä ja pääsee käsiksi malliin ja mallin adapteriin, jotka on tallennettu Azure Filesiin ja jotka luotiin hienosäätövaiheessa.

## AI Toolkitin käyttö

### Julkaisu inferenssiä varten  
Jos haluat muokata inferenssikoodia tai ladata inferenssimallin uudelleen, suorita `AI Toolkit: Deploy for inference` -komento. Tämä synkronoi viimeisimmän koodisi ACA:n kanssa ja käynnistää replikan uudelleen.

![Deploy for inference](../../../../../translated_images/fi/command-deploy.9adb4e310dd0b0ae.png)

Julkaisun onnistuttua malli on valmis arvioitavaksi tämän päätepisteen kautta.

### Inferenssi-API:n käyttö

Pääset inferenssi-API:iin napsauttamalla VSCode-ilmoituksessa näkyvää "*Go to Inference Endpoint*" -painiketta. Vaihtoehtoisesti web-API-päätepiste löytyy `ACA_APP_ENDPOINT`-kentästä tiedostossa `./infra/inference.config.json` sekä tulospaneelista.

![App Endpoint](../../../../../translated_images/fi/notification-deploy.446e480a44b1be58.png)

> **Note:** Inferenssipäätepisteen täysi toiminta voi kestää muutaman minuutin.

## Mallipohjaan sisältyvät inferenssikomponentit

| Kansio | Sisältö |
| ------ |--------- |
| `infra` | Sisältää kaikki etäkäyttöön tarvittavat asetukset. |
| `infra/provision/inference.parameters.json` | Sisältää parametrit bicep-malleille, joita käytetään Azure-resurssien määrittämiseen inferenssiä varten. |
| `infra/provision/inference.bicep` | Sisältää mallit Azure-resurssien määrittämiseen inferenssiä varten. |
| `infra/inference.config.json` | Konfiguraatiotiedosto, joka luodaan `AI Toolkit: Provision Azure Container Apps for inference` -komennolla. Sitä käytetään syötteenä muille etäkomentopaleteille. |

### AI Toolkitin käyttö Azure-resurssien määrittämiseen  
Määritä [AI Toolkit](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

Suorita `Provision Azure Container Apps for inference` -komento.

Konfiguraatioparametrit löytyvät tiedostosta `./infra/provision/inference.parameters.json`. Tässä tiedot:  
| Parametri | Kuvaus |
| --------- |-------- |
| `defaultCommands` | Komennot web-API:n käynnistämiseen. |
| `maximumInstanceCount` | Määrittää GPU-instanssien maksimimäärän. |
| `location` | Paikka, johon Azure-resurssit määritetään. Oletusarvo on sama kuin valitun resurssiryhmän sijainti. |
| `storageAccountName`, `fileShareName`, `acaEnvironmentName`, `acaEnvironmentStorageName`, `acaAppName`, `acaLogAnalyticsName` | Näitä parametreja käytetään Azure-resurssien nimeämiseen määrittämisen yhteydessä. Oletuksena ne ovat samat kuin hienosäätöresurssin nimet. Voit syöttää uuden, käyttämättömän resurssin nimen luodaksesi omat nimetty resurssit, tai voit käyttää olemassa olevan Azure-resurssin nimeä, jos haluat käyttää sitä. Lisätietoja kohdassa [Using existing Azure Resources](../../../../../md/01.Introduction/03). |

### Olemassa olevien Azure-resurssien käyttö

Oletuksena inferenssin määrittely käyttää samaa Azure Container App Environmentia, Storage Accountia, Azure File Sharea ja Azure Log Analyticsia, joita käytettiin hienosäädössä. Erillinen Azure Container App luodaan pelkästään inferenssi-API:lle.

Jos olet muokannut Azure-resursseja hienosäätövaiheessa tai haluat käyttää omia olemassa olevia Azure-resurssejasi inferenssiä varten, määritä niiden nimet tiedostossa `./infra/inference.parameters.json`. Suorita sitten `AI Toolkit: Provision Azure Container Apps for inference` -komento komentopaletista. Tämä päivittää määritetyt resurssit ja luo puuttuvat.

Esimerkiksi, jos sinulla on olemassa oleva Azure-konttiympäristö, `./infra/finetuning.parameters.json` voisi näyttää tältä:

```json
{
    "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentParameters.json#",
    "contentVersion": "1.0.0.0",
    "parameters": {
      ...
      "acaEnvironmentName": {
        "value": "<your-aca-env-name>"
      },
      "acaEnvironmentStorageName": {
        "value": null
      },
      ...
    }
  }
```

### Manuaalinen määrittely  
Jos haluat määrittää Azure-resurssit manuaalisesti, voit käyttää `./infra/provision` -kansioissa olevia bicep-tiedostoja. Jos olet jo määrittänyt ja konfiguroinut kaikki Azure-resurssit ilman AI Toolkitin komentopalettia, voit yksinkertaisesti syöttää resurssien nimet `inference.config.json` -tiedostoon.

Esimerkiksi:

```json
{
  "SUBSCRIPTION_ID": "<your-subscription-id>",
  "RESOURCE_GROUP_NAME": "<your-resource-group-name>",
  "STORAGE_ACCOUNT_NAME": "<your-storage-account-name>",
  "FILE_SHARE_NAME": "<your-file-share-name>",
  "ACA_APP_NAME": "<your-aca-name>",
  "ACA_APP_ENDPOINT": "<your-aca-endpoint>"
}
```

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.