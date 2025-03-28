<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a54cd3d65b6963e4e8ce21e143c3ab04",
  "translation_date": "2025-03-27T07:59:20+00:00",
  "source_file": "md\\01.Introduction\\03\\Remote_Interence.md",
  "language_code": "es"
}
-->
# Inferencia remota con el modelo ajustado

Después de entrenar los adaptadores en el entorno remoto, utiliza una aplicación sencilla de Gradio para interactuar con el modelo.

![Ajuste completado](../../../../../translated_images/log-finetuning-res.4b3ee593f24d3096742d09375adade22b217738cab93bc1139f224e5888a1cbf.es.png)

### Aprovisionar recursos de Azure
Debes configurar los recursos de Azure para la inferencia remota ejecutando el comando `AI Toolkit: Provision Azure Container Apps for inference` desde el panel de comandos. Durante esta configuración, se te pedirá que selecciones tu suscripción de Azure y el grupo de recursos.  
![Aprovisionar recurso de inferencia](../../../../../translated_images/command-provision-inference.b294f3ae5764ab45b83246d464ad5329b0de20cf380f75a699b4cc6b5495ca11.es.png)

Por defecto, la suscripción y el grupo de recursos para la inferencia deberían coincidir con los utilizados para el ajuste fino. La inferencia usará el mismo entorno de Azure Container App y accederá al modelo y al adaptador del modelo almacenados en Azure Files, que fueron generados durante el paso de ajuste fino.

## Uso del AI Toolkit 

### Despliegue para inferencia  
Si deseas revisar el código de inferencia o recargar el modelo de inferencia, ejecuta el comando `AI Toolkit: Deploy for inference`. Esto sincronizará tu código más reciente con ACA y reiniciará la réplica.  

![Desplegar para inferencia](../../../../../translated_images/command-deploy.cb6508c973d6257e649aa4f262d3c170a374da3e9810a4f3d9e03935408a592b.es.png)

Una vez completado el despliegue exitosamente, el modelo estará listo para ser evaluado utilizando este endpoint.

### Acceso a la API de inferencia

Puedes acceder a la API de inferencia haciendo clic en el botón "*Ir al endpoint de inferencia*" que se muestra en la notificación de VSCode. Alternativamente, el endpoint de la API web se puede encontrar bajo `ACA_APP_ENDPOINT` en `./infra/inference.config.json` y en el panel de salida.

![Endpoint de la aplicación](../../../../../translated_images/notification-deploy.00f4267b7aa6a18cfaaec83a7831b5d09311d5d96a70bb4c9d651ea4a41a8af7.es.png)

> **Nota:** El endpoint de inferencia puede tardar unos minutos en estar completamente operativo.

## Componentes de inferencia incluidos en la plantilla

| Carpeta | Contenido |
| ------- | --------- |
| `infra` | Contiene todas las configuraciones necesarias para operaciones remotas. |
| `infra/provision/inference.parameters.json` | Contiene parámetros para las plantillas bicep, utilizadas para aprovisionar recursos de Azure para inferencia. |
| `infra/provision/inference.bicep` | Contiene plantillas para aprovisionar recursos de Azure para inferencia. |
| `infra/inference.config.json` | El archivo de configuración generado por el comando `AI Toolkit: Provision Azure Container Apps for inference`. Se utiliza como entrada para otros comandos remotos del panel. |

### Uso del AI Toolkit para configurar el aprovisionamiento de recursos de Azure
Configura el [AI Toolkit](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

Aprovisiona Azure Container Apps para inferencia ` command.

You can find configuration parameters in `./infra/provision/inference.parameters.json` file. Here are the details:
| Parameter | Description |
| --------- |------------ |
| `defaultCommands` | This is the commands to initiate a web API. |
| `maximumInstanceCount` | This parameter sets the maximum capacity of GPU instances. |
| `location` | This is the location where Azure resources are provisioned. The default value is the same as the chosen resource group's location. |
| `storageAccountName`, `fileShareName` `acaEnvironmentName`, `acaEnvironmentStorageName`, `acaAppName`,  `acaLogAnalyticsName` | These parameters are used to name the Azure resources for provision. By default, they will be same to the fine-tuning resource name. You can input a new, unused resource name to create your own custom-named resources, or you can input the name of an already existing Azure resource if you'd prefer to use that. For details, refer to the section [Using existing Azure Resources](../../../../../md/01.Introduction/03). |

### Using Existing Azure Resources

By default, the inference provision use the same Azure Container App Environment, Storage Account, Azure File Share, and Azure Log Analytics that were used for fine-tuning. A separate Azure Container App is created solely for the inference API. 

If you have customized the Azure resources during the fine-tuning step or want to use your own existing Azure resources for inference, specify their names in the `./infra/inference.parameters.json`. Luego, ejecuta el comando `AI Toolkit: Provision Azure Container Apps for inference` desde el panel de comandos. Esto actualiza los recursos especificados y crea aquellos que falten.

Por ejemplo, si ya tienes un entorno de contenedor de Azure existente, tu archivo `./infra/finetuning.parameters.json` debería verse así:

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

### Aprovisionamiento manual  
Si prefieres configurar manualmente los recursos de Azure, puedes usar los archivos bicep proporcionados en el archivo `./infra/provision` folders. If you have already set up and configured all the Azure resources without using the AI Toolkit command palette, you can simply enter the resource names in the `inference.config.json`.

Por ejemplo:

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

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.