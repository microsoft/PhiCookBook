# Nuotolinis modelio įvertinimas su pritaikytu modeliu

Po to, kai adapteriai yra apmokyti nuotolinėje aplinkoje, galite naudoti paprastą Gradio aplikaciją, kad sąveikautumėte su modeliu.

![Pritaikymas baigtas](../../../../../imgs/03/RemoteServer/log-finetuning-res.png)

### Azure išteklių paruošimas
Norėdami nustatyti Azure išteklius nuotoliniam įvertinimui, vykdykite komandą `AI Toolkit: Provision Azure Container Apps for inference` iš komandų paletės. Šio proceso metu jums reikės pasirinkti savo Azure prenumeratą ir išteklių grupę.  
![Paruošti įvertinimo išteklius](../../../../../imgs/03/RemoteServer/command-provision-inference.png)
   
Pagal numatymą, prenumerata ir išteklių grupė, naudojama įvertinimui, turėtų sutapti su tomis, kurios buvo naudojamos pritaikymui. Įvertinimas naudos tą pačią Azure Container App aplinką ir pasieks modelį bei modelio adapterį, saugomą Azure Files, kurie buvo sukurti pritaikymo metu.

## AI Toolkit naudojimas

### Įvertinimo diegimas  
Jei norite peržiūrėti įvertinimo kodą arba iš naujo įkelti įvertinimo modelį, vykdykite komandą `AI Toolkit: Deploy for inference`. Tai sinchronizuos naujausią kodą su ACA ir iš naujo paleis repliką.  

![Diegti įvertinimui](../../../../../imgs/01/03/RemoteServer/command-deploy.png)

Po sėkmingo diegimo modelis bus paruoštas vertinimui naudojant šį galinį tašką.

### Prieiga prie įvertinimo API

Prie įvertinimo API galite prisijungti paspaudę "*Go to Inference Endpoint*" mygtuką, rodomą VSCode pranešime. Alternatyviai, internetinio API galinio taško adresą galite rasti `ACA_APP_ENDPOINT` faile `./infra/inference.config.json` ir išvesties skydelyje.

![Programos galinis taškas](../../../../../imgs/01/03/RemoteServer/notification-deploy.png)

> **Pastaba:** Įvertinimo galinis taškas gali užtrukti kelias minutes, kol taps visiškai funkcionalus.

## Įvertinimo komponentai, įtraukti į šabloną
 
| Aplankas | Turinys |
| ------ |--------- |
| `infra` | Sudėtyje yra visos būtinos konfigūracijos nuotolinėms operacijoms. |
| `infra/provision/inference.parameters.json` | Laiko parametrus bicep šablonams, naudojamiems Azure išteklių paruošimui įvertinimui. |
| `infra/provision/inference.bicep` | Sudėtyje yra šablonai Azure išteklių paruošimui įvertinimui. |
| `infra/inference.config.json` | Konfigūracijos failas, sukurtas vykdant komandą `AI Toolkit: Provision Azure Container Apps for inference`. Jis naudojamas kaip įvestis kitoms nuotolinėms komandų paletėms. |

### AI Toolkit naudojimas Azure išteklių paruošimui
Konfigūruokite [AI Toolkit](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

Komandą `Provision Azure Container Apps for inference`.

Konfigūracijos parametrus galite rasti faile `./infra/provision/inference.parameters.json`. Štai detalės:
| Parametras | Aprašymas |
| --------- |------------ |
| `defaultCommands` | Komandos, skirtos internetinio API inicijavimui. |
| `maximumInstanceCount` | Nustato maksimalų GPU instancijų pajėgumą. |
| `location` | Vietovė, kurioje paruošiami Azure ištekliai. Pagal numatymą, tai yra ta pati vietovė kaip pasirinktos išteklių grupės vietovė. |
| `storageAccountName`, `fileShareName` `acaEnvironmentName`, `acaEnvironmentStorageName`, `acaAppName`,  `acaLogAnalyticsName` | Šie parametrai naudojami Azure išteklių pavadinimams. Pagal numatymą, jie bus tokie pat kaip pritaikymo išteklių pavadinimai. Galite įvesti naują, nenaudotą išteklių pavadinimą, kad sukurtumėte savo pasirinktinius išteklius, arba galite įvesti jau egzistuojančio Azure ištekliaus pavadinimą, jei norite naudoti jį. Daugiau informacijos rasite skyriuje [Naudojant esamus Azure išteklius](../../../../../md/01.Introduction/03). |

### Naudojant esamus Azure išteklius

Pagal numatymą, įvertinimo paruošimas naudoja tą pačią Azure Container App aplinką, saugojimo paskyrą, Azure File Share ir Azure Log Analytics, kurie buvo naudojami pritaikymui. Atskirai sukuriama Azure Container App, skirta tik įvertinimo API. 

Jei pritaikymo metu pritaikėte Azure išteklius arba norite naudoti savo esamus Azure išteklius įvertinimui, nurodykite jų pavadinimus faile `./infra/inference.parameters.json`. Tada vykdykite komandą `AI Toolkit: Provision Azure Container Apps for inference` iš komandų paletės. Tai atnaujins nurodytus išteklius ir sukurs trūkstamus.

Pavyzdžiui, jei turite esamą Azure konteinerio aplinką, jūsų `./infra/finetuning.parameters.json` turėtų atrodyti taip:

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

### Rankinis paruošimas  
Jei norite rankiniu būdu konfigūruoti Azure išteklius, galite naudoti pateiktus bicep failus aplanke `./infra/provision`. Jei jau nustatėte ir sukonfigūravote visus Azure išteklius nenaudodami AI Toolkit komandų paletės, tiesiog įveskite išteklių pavadinimus faile `inference.config.json`.

Pavyzdžiui:

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

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.