<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a54cd3d65b6963e4e8ce21e143c3ab04",
  "translation_date": "2025-07-16T21:14:35+00:00",
  "source_file": "md/01.Introduction/03/Remote_Interence.md",
  "language_code": "es"
}
-->
# Inferencia remota con el modelo afinado

Después de entrenar los adaptadores en el entorno remoto, utiliza una aplicación sencilla de Gradio para interactuar con el modelo.

![Fine-tune complete](../../../../../translated_images/log-finetuning-res.7b92254e7e822c7f.es.png)

### Provisión de recursos en Azure  
Debes configurar los recursos de Azure para la inferencia remota ejecutando el comando `AI Toolkit: Provision Azure Container Apps for inference` desde la paleta de comandos. Durante esta configuración, se te pedirá seleccionar tu suscripción de Azure y el grupo de recursos.  
![Provision Inference Resource](../../../../../translated_images/command-provision-inference.467afc8d351642fc.es.png)
   
Por defecto, la suscripción y el grupo de recursos para la inferencia deberían coincidir con los usados para el afinamiento. La inferencia utilizará el mismo entorno de Azure Container App y accederá al modelo y al adaptador de modelo almacenados en Azure Files, que se generaron durante el paso de afinamiento. 

## Uso de AI Toolkit

### Despliegue para inferencia  
Si deseas modificar el código de inferencia o recargar el modelo de inferencia, ejecuta el comando `AI Toolkit: Deploy for inference`. Esto sincronizará tu código más reciente con ACA y reiniciará la réplica.  

![Deploy for inference](../../../../../translated_images/command-deploy.9adb4e310dd0b0ae.es.png)

Una vez completado el despliegue con éxito, el modelo estará listo para ser evaluado usando este endpoint.

### Acceso a la API de inferencia

Puedes acceder a la API de inferencia haciendo clic en el botón "*Go to Inference Endpoint*" que aparece en la notificación de VSCode. Alternativamente, el endpoint de la API web se encuentra en `ACA_APP_ENDPOINT` dentro de `./infra/inference.config.json` y en el panel de salida.

![App Endpoint](../../../../../translated_images/notification-deploy.446e480a44b1be58.es.png)

> **Note:** El endpoint de inferencia puede tardar unos minutos en estar completamente operativo.

## Componentes de inferencia incluidos en la plantilla

| Carpeta | Contenido |
| ------ |--------- |
| `infra` | Contiene todas las configuraciones necesarias para operaciones remotas. |
| `infra/provision/inference.parameters.json` | Contiene los parámetros para las plantillas bicep, usados para provisionar recursos de Azure para inferencia. |
| `infra/provision/inference.bicep` | Contiene las plantillas para provisionar recursos de Azure para inferencia. |
| `infra/inference.config.json` | Archivo de configuración, generado por el comando `AI Toolkit: Provision Azure Container Apps for inference`. Se usa como entrada para otros comandos remotos. |

### Uso de AI Toolkit para configurar la provisión de recursos en Azure  
Configura el [AI Toolkit](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

Ejecuta el comando `Provision Azure Container Apps for inference`.

Puedes encontrar los parámetros de configuración en el archivo `./infra/provision/inference.parameters.json`. Aquí los detalles:  
| Parámetro | Descripción |
| --------- |------------ |
| `defaultCommands` | Comandos para iniciar una API web. |
| `maximumInstanceCount` | Establece la capacidad máxima de instancias GPU. |
| `location` | Ubicación donde se provisionan los recursos de Azure. El valor por defecto es el mismo que la ubicación del grupo de recursos seleccionado. |
| `storageAccountName`, `fileShareName`, `acaEnvironmentName`, `acaEnvironmentStorageName`, `acaAppName`, `acaLogAnalyticsName` | Estos parámetros se usan para nombrar los recursos de Azure a provisionar. Por defecto, serán iguales a los nombres usados en el recurso de afinamiento. Puedes ingresar un nombre nuevo y sin uso para crear recursos personalizados, o el nombre de un recurso de Azure ya existente si prefieres usarlo. Para más detalles, consulta la sección [Using existing Azure Resources](../../../../../md/01.Introduction/03). |

### Uso de recursos existentes en Azure

Por defecto, la provisión para inferencia usa el mismo entorno de Azure Container App, cuenta de almacenamiento, Azure File Share y Azure Log Analytics que se usaron para el afinamiento. Se crea una Azure Container App separada exclusivamente para la API de inferencia.

Si personalizaste los recursos de Azure durante el paso de afinamiento o quieres usar tus propios recursos existentes para la inferencia, especifica sus nombres en el archivo `./infra/inference.parameters.json`. Luego, ejecuta el comando `AI Toolkit: Provision Azure Container Apps for inference` desde la paleta de comandos. Esto actualizará los recursos especificados y creará los que falten.

Por ejemplo, si tienes un entorno de contenedores de Azure existente, tu archivo `./infra/finetuning.parameters.json` debería verse así:

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

### Provisión manual  
Si prefieres configurar manualmente los recursos de Azure, puedes usar los archivos bicep proporcionados en la carpeta `./infra/provision`. Si ya configuraste todos los recursos de Azure sin usar la paleta de comandos de AI Toolkit, simplemente ingresa los nombres de los recursos en el archivo `inference.config.json`.

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

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.