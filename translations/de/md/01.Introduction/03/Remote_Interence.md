<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a54cd3d65b6963e4e8ce21e143c3ab04",
  "translation_date": "2025-05-07T10:45:29+00:00",
  "source_file": "md/01.Introduction/03/Remote_Interence.md",
  "language_code": "de"
}
-->
# Remote-Inferenz mit dem feinabgestimmten Modell

Nachdem die Adapter in der Remote-Umgebung trainiert wurden, verwenden Sie eine einfache Gradio-Anwendung, um mit dem Modell zu interagieren.

![Fine-tune abgeschlossen](../../../../../translated_images/log-finetuning-res.7b92254e7e822c7ffbec00f51a29199b0a53cefdd7fd2ce8330e4f787d98a94a.de.png)

### Azure-Ressourcen bereitstellen  
Sie müssen die Azure-Ressourcen für die Remote-Inferenz einrichten, indem Sie den `AI Toolkit: Provision Azure Container Apps for inference` aus der Befehls-Palette ausführen. Während dieses Vorgangs werden Sie aufgefordert, Ihr Azure-Abonnement und die Ressourcengruppe auszuwählen.  
![Inference-Ressource bereitstellen](../../../../../translated_images/command-provision-inference.467afc8d351642fc03bc2ae439330ad1253da4f08ed8a8e98cdf89ca5c7ae4c5.de.png)
   
Standardmäßig sollten das Abonnement und die Ressourcengruppe für die Inferenz mit denen übereinstimmen, die beim Fine-Tuning verwendet wurden. Die Inferenz nutzt dieselbe Azure Container App-Umgebung und greift auf das Modell und den Modelladapter zu, die in Azure Files gespeichert sind und während des Fine-Tuning-Schritts erstellt wurden.

## Verwendung des AI Toolkits

### Deployment für die Inferenz  
Wenn Sie den Inferenzcode überarbeiten oder das Inferenzmodell neu laden möchten, führen Sie bitte den `AI Toolkit: Deploy for inference`-Befehl aus. Dadurch wird Ihr aktueller Code mit ACA synchronisiert und die Replik neu gestartet.

![Deployment für Inferenz](../../../../../translated_images/command-deploy.9adb4e310dd0b0aec6bb518f3c5b19a945ca040216da11e210666ad0330702ea.de.png)

Nach erfolgreichem Abschluss des Deployments ist das Modell bereit für die Auswertung über diesen Endpunkt.

### Zugriff auf die Inferenz-API

Sie können auf die Inferenz-API zugreifen, indem Sie auf die Schaltfläche "*Go to Inference Endpoint*" klicken, die in der VSCode-Benachrichtigung angezeigt wird. Alternativ finden Sie den Web-API-Endpunkt unter `ACA_APP_ENDPOINT` in `./infra/inference.config.json` sowie im Ausgabefenster.

![App-Endpunkt](../../../../../translated_images/notification-deploy.446e480a44b1be5848fd31391c467b8d42c2db1d5daffa2250c9fcd3d8486164.de.png)

> **Hinweis:** Der Inferenz-Endpunkt kann einige Minuten benötigen, bis er vollständig betriebsbereit ist.

## Inferenz-Komponenten, die in der Vorlage enthalten sind
 
| Ordner | Inhalt |
| ------ |--------- |
| `infra` | Enthält alle notwendigen Konfigurationen für Remote-Operationen. |
| `infra/provision/inference.parameters.json` | Beinhaltet Parameter für die Bicep-Vorlagen, die für die Bereitstellung von Azure-Ressourcen für die Inferenz verwendet werden. |
| `infra/provision/inference.bicep` | Enthält Vorlagen für die Bereitstellung von Azure-Ressourcen für die Inferenz. |
| `infra/inference.config.json` | Die Konfigurationsdatei, die durch den `AI Toolkit: Provision Azure Container Apps for inference`-Befehl erzeugt wird. Sie dient als Eingabe für andere Remote-Befehls-Paletten. |

### Verwendung des AI Toolkits zur Konfiguration der Azure-Ressourcenbereitstellung  
Konfigurieren Sie das [AI Toolkit](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

Stellen Sie Azure Container Apps für die Inferenz bereit` command.

You can find configuration parameters in `./infra/provision/inference.parameters.json` file. Here are the details:
| Parameter | Description |
| --------- |------------ |
| `defaultCommands` | This is the commands to initiate a web API. |
| `maximumInstanceCount` | This parameter sets the maximum capacity of GPU instances. |
| `location` | This is the location where Azure resources are provisioned. The default value is the same as the chosen resource group's location. |
| `storageAccountName`, `fileShareName` `acaEnvironmentName`, `acaEnvironmentStorageName`, `acaAppName`,  `acaLogAnalyticsName` | These parameters are used to name the Azure resources for provision. By default, they will be same to the fine-tuning resource name. You can input a new, unused resource name to create your own custom-named resources, or you can input the name of an already existing Azure resource if you'd prefer to use that. For details, refer to the section [Using existing Azure Resources](../../../../../md/01.Introduction/03). |

### Using Existing Azure Resources

By default, the inference provision use the same Azure Container App Environment, Storage Account, Azure File Share, and Azure Log Analytics that were used for fine-tuning. A separate Azure Container App is created solely for the inference API. 

If you have customized the Azure resources during the fine-tuning step or want to use your own existing Azure resources for inference, specify their names in the `./infra/inference.parameters.json`-Datei. Führen Sie anschließend den `AI Toolkit: Provision Azure Container Apps for inference`-Befehl aus der Befehls-Palette aus. Dadurch werden alle angegebenen Ressourcen aktualisiert und fehlende erstellt.

Beispielsweise sollte Ihre `./infra/finetuning.parameters.json` so aussehen, wenn Sie bereits eine Azure Container-Umgebung besitzen:

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

### Manuelle Bereitstellung  
Wenn Sie die Azure-Ressourcen lieber manuell konfigurieren möchten, können Sie die bereitgestellten Bicep-Dateien im `./infra/provision` folders. If you have already set up and configured all the Azure resources without using the AI Toolkit command palette, you can simply enter the resource names in the `inference.config.json`-Datei verwenden.

Zum Beispiel:

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

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.