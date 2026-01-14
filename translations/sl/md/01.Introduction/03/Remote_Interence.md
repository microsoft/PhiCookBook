<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a54cd3d65b6963e4e8ce21e143c3ab04",
  "translation_date": "2025-07-16T21:23:02+00:00",
  "source_file": "md/01.Introduction/03/Remote_Interence.md",
  "language_code": "sl"
}
-->
# Oddaljeno sklepanje z modelom, ki je bil dodatno prilagojen

Ko so adapterji usposobljeni v oddaljenem okolju, uporabite preprosto aplikacijo Gradio za interakcijo z modelom.

![Fine-tune complete](../../../../../translated_images/sl/log-finetuning-res.7b92254e7e822c7f.png)

### Priprava Azure virov
Za oddaljeno sklepanje morate nastaviti Azure vire z izvajanjem ukaza `AI Toolkit: Provision Azure Container Apps for inference` iz ukazne palete. Med tem postopkom boste morali izbrati svojo Azure naročnino in skupino virov.  
![Provision Inference Resource](../../../../../translated_images/sl/command-provision-inference.467afc8d351642fc.png)
   
Privzeto naj bi bila naročnina in skupina virov za sklepanje enaka tistima, ki sta bili uporabljeni za dodatno prilagajanje. Sklepanje bo uporabljalo isto okolje Azure Container App in dostopalo do modela ter adapterja modela, shranjenih v Azure Files, ki so bili ustvarjeni med korakom dodatnega prilagajanja.

## Uporaba AI Toolkit

### Namestitev za sklepanje  
Če želite spremeniti kodo za sklepanje ali ponovno naložiti model za sklepanje, zaženite ukaz `AI Toolkit: Deploy for inference`. Ta ukaz bo sinhroniziral vašo najnovejšo kodo z ACA in ponovno zagnal repliko.

![Deploy for inference](../../../../../translated_images/sl/command-deploy.9adb4e310dd0b0ae.png)

Po uspešni namestitvi je model pripravljen za ocenjevanje preko tega končnega naslova.

### Dostop do API-ja za sklepanje

Do API-ja za sklepanje lahko dostopate s klikom na gumb "*Go to Inference Endpoint*", ki se prikaže v obvestilu VSCode. Alternativno lahko spletni API končni naslov najdete pod `ACA_APP_ENDPOINT` v datoteki `./infra/inference.config.json` in v izhodnem panelu.

![App Endpoint](../../../../../translated_images/sl/notification-deploy.446e480a44b1be58.png)

> **Note:** Končni naslov za sklepanje lahko potrebuje nekaj minut, da postane popolnoma operativen.

## Komponente za sklepanje, vključene v predlogo

| Mapa | Vsebina |
| ------ |--------- |
| `infra` | Vsebuje vse potrebne konfiguracije za oddaljeno delovanje. |
| `infra/provision/inference.parameters.json` | Vsebuje parametre za bicep predloge, ki se uporabljajo za pripravo Azure virov za sklepanje. |
| `infra/provision/inference.bicep` | Vsebuje predloge za pripravo Azure virov za sklepanje. |
| `infra/inference.config.json` | Konfiguracijska datoteka, ustvarjena z ukazom `AI Toolkit: Provision Azure Container Apps for inference`. Uporablja se kot vhod za druge ukaze v ukazni paleti za oddaljeno delo. |

### Uporaba AI Toolkit za konfiguracijo priprave Azure virov
Konfigurirajte [AI Toolkit](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

Ukaz `Provision Azure Container Apps for inference`.

Konfiguracijske parametre najdete v datoteki `./infra/provision/inference.parameters.json`. Tukaj so podrobnosti:
| Parameter | Opis |
| --------- |------------ |
| `defaultCommands` | Ukazi za zagon spletnega API-ja. |
| `maximumInstanceCount` | Ta parameter določa največjo kapaciteto GPU instanc. |
| `location` | Lokacija, kjer se pripravljajo Azure viri. Privzeta vrednost je enaka lokaciji izbrane skupine virov. |
| `storageAccountName`, `fileShareName`, `acaEnvironmentName`, `acaEnvironmentStorageName`, `acaAppName`,  `acaLogAnalyticsName` | Ti parametri se uporabljajo za poimenovanje Azure virov za pripravo. Privzeto so enaki imenom virov, uporabljenih pri dodatnem prilagajanju. Lahko vnesete novo, neuporabljeno ime vira za ustvarjanje lastnih virov z izbranim imenom ali pa vnesete ime že obstoječega Azure vira, če želite uporabiti tega. Za podrobnosti glejte razdelek [Uporaba obstoječih Azure virov](../../../../../md/01.Introduction/03). |

### Uporaba obstoječih Azure virov

Privzeto priprava za sklepanje uporablja isto okolje Azure Container App, Storage Account, Azure File Share in Azure Log Analytics, ki so bili uporabljeni pri dodatnem prilagajanju. Za API za sklepanje se ustvari ločen Azure Container App.

Če ste med dodatnim prilagajanjem prilagodili Azure vire ali želite za sklepanje uporabiti svoje obstoječe Azure vire, vnesite njihova imena v datoteko `./infra/inference.parameters.json`. Nato zaženite ukaz `AI Toolkit: Provision Azure Container Apps for inference` iz ukazne palete. Ta ukaz posodobi navedene vire in ustvari manjkajoče.

Na primer, če imate obstoječe Azure container okolje, naj bo vaša datoteka `./infra/finetuning.parameters.json` videti takole:

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

### Ročna priprava  
Če želite Azure vire nastaviti ročno, lahko uporabite priložene bicep datoteke v mapah `./infra/provision`. Če ste že nastavili in konfigurirali vse Azure vire brez uporabe ukazne palete AI Toolkit, lahko preprosto vnesete imena virov v datoteko `inference.config.json`.

Na primer:

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

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.