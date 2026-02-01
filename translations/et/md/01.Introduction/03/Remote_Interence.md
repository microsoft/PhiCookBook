# Kaugjäreldamine peenhäälestatud mudeliga

Pärast seda, kui adapterid on kaugkeskkonnas treenitud, saate mudeliga suhelda lihtsa Gradio rakenduse abil.

![Peenhäälestus lõpetatud](../../../../../imgs/03/RemoteServer/log-finetuning-res.png)

### Azure'i ressursside ettevalmistamine
Kaugjäreldamise jaoks on vaja seadistada Azure'i ressursid, käivitades käsu paletist `AI Toolkit: Provision Azure Container Apps for inference`. Selle seadistuse käigus palutakse teil valida oma Azure'i tellimus ja ressursigrupp.  
![Järeldamisressursi ettevalmistamine](../../../../../imgs/03/RemoteServer/command-provision-inference.png)
   
Vaikimisi peaksid tellimus ja ressursigrupp järeldamiseks olema samad, mida kasutati peenhäälestamiseks. Järeldamine kasutab sama Azure Container App Environment'i ja pääseb ligi mudelile ning mudeli adapterile, mis salvestati Azure Files'i peenhäälestamise käigus.

## AI Toolkit'i kasutamine 

### Järeldamise juurutamine  
Kui soovite järeldamiskoodi muuta või järeldamismudelit uuesti laadida, käivitage käsk `AI Toolkit: Deploy for inference`. See sünkroonib teie uusima koodi ACA-ga ja taaskäivitab replika.  

![Järeldamise juurutamine](../../../../../imgs/01/03/RemoteServer/command-deploy.png)

Pärast juurutamise edukat lõpetamist on mudel valmis hindamiseks selle lõpp-punkti kaudu.

### Järeldamise API-le juurdepääs

Järeldamise API-le pääseb ligi, klõpsates VSCode'i teavituses kuvatavat nuppu "*Go to Inference Endpoint*". Alternatiivselt leiate veebirakenduse API lõpp-punkti `ACA_APP_ENDPOINT` alt failis `./infra/inference.config.json` ja väljundpaneelilt.

![Rakenduse lõpp-punkt](../../../../../imgs/01/03/RemoteServer/notification-deploy.png)

> **Märkus:** Järeldamise lõpp-punkti täielikuks töövalmiduseks võib kuluda paar minutit.

## Mallis sisalduvad järeldamiskomponendid
 
| Kaust | Sisu |
| ------ |--------- |
| `infra` | Sisaldab kõiki vajalikke konfiguratsioone kaugtoiminguteks. |
| `infra/provision/inference.parameters.json` | Sisaldab bicep-mallide parameetreid, mida kasutatakse Azure'i ressursside ettevalmistamiseks järeldamiseks. |
| `infra/provision/inference.bicep` | Sisaldab malle Azure'i ressursside ettevalmistamiseks järeldamiseks. |
| `infra/inference.config.json` | Konfiguratsioonifail, mille genereerib käsk `AI Toolkit: Provision Azure Container Apps for inference`. Seda kasutatakse sisendina teistele kaugkäskudele. |

### AI Toolkit'i kasutamine Azure'i ressursside ettevalmistamiseks
Seadistage [AI Toolkit](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

Käivitage käsk `Provision Azure Container Apps for inference`.

Konfiguratsiooniparameetrid leiate failist `./infra/provision/inference.parameters.json`. Siin on üksikasjad:
| Parameeter | Kirjeldus |
| --------- |------------ |
| `defaultCommands` | Need on käsud veebirakenduse API käivitamiseks. |
| `maximumInstanceCount` | See parameeter määrab GPU instantside maksimaalse mahutavuse. |
| `location` | Azure'i ressursside ettevalmistamise asukoht. Vaikeväärtus on sama, mis valitud ressursigrupi asukoht. |
| `storageAccountName`, `fileShareName` `acaEnvironmentName`, `acaEnvironmentStorageName`, `acaAppName`,  `acaLogAnalyticsName` | Need parameetrid määravad Azure'i ressursside nimed ettevalmistamiseks. Vaikimisi vastavad need peenhäälestamise ressursside nimedele. Võite sisestada uue, kasutamata ressursi nime, et luua oma kohandatud nimega ressursid, või sisestada olemasoleva Azure'i ressursi nimi, kui eelistate seda kasutada. Üksikasjade jaoks vaadake jaotist [Olemasolevate Azure'i ressursside kasutamine](../../../../../md/01.Introduction/03). |

### Olemasolevate Azure'i ressursside kasutamine

Vaikimisi kasutab järeldamise ettevalmistus sama Azure Container App Environment'i, Storage Account'i, Azure File Share'i ja Azure Log Analytics'i, mida kasutati peenhäälestamiseks. Eraldi Azure Container App luuakse ainult järeldamise API jaoks. 

Kui olete peenhäälestamise käigus Azure'i ressursse kohandanud või soovite kasutada oma olemasolevaid Azure'i ressursse järeldamiseks, määrake nende nimed failis `./infra/inference.parameters.json`. Seejärel käivitage käsu paletist `AI Toolkit: Provision Azure Container Apps for inference`. See värskendab määratud ressursse ja loob kõik puuduvad.

Näiteks, kui teil on olemasolev Azure'i konteinerikeskkond, peaks teie fail `./infra/finetuning.parameters.json` välja nägema selline:

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

### Käsitsi ettevalmistamine  
Kui eelistate Azure'i ressursse käsitsi konfigureerida, saate kasutada kaustas `./infra/provision` olevaid bicep-faile. Kui olete juba kõik Azure'i ressursid seadistanud ja konfigureerinud ilma AI Toolkit'i käsupaletti kasutamata, saate lihtsalt sisestada ressursside nimed faili `inference.config.json`.

Näiteks:

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

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.