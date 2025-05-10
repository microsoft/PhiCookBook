<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a54cd3d65b6963e4e8ce21e143c3ab04",
  "translation_date": "2025-05-09T12:37:28+00:00",
  "source_file": "md/01.Introduction/03/Remote_Interence.md",
  "language_code": "pt"
}
-->
# Inferência Remota com o modelo ajustado

Após os adapters serem treinados no ambiente remoto, use uma aplicação simples do Gradio para interagir com o modelo.

![Fine-tune complete](../../../../../translated_images/log-finetuning-res.4b3ee593f24d3096742d09375adade22b217738cab93bc1139f224e5888a1cbf.pt.png)

### Provisionar Recursos Azure  
Você precisa configurar os Recursos Azure para inferência remota executando o `AI Toolkit: Provision Azure Container Apps for inference` a partir da paleta de comandos. Durante essa configuração, será solicitado que você selecione sua Assinatura Azure e o grupo de recursos.  
![Provision Inference Resource](../../../../../translated_images/command-provision-inference.b294f3ae5764ab45b83246d464ad5329b0de20cf380f75a699b4cc6b5495ca11.pt.png)
   
Por padrão, a assinatura e o grupo de recursos para inferência devem ser os mesmos usados para o fine-tuning. A inferência usará o mesmo Ambiente Azure Container App e acessará o modelo e o adapter do modelo armazenados no Azure Files, que foram gerados durante a etapa de fine-tuning.

## Usando o AI Toolkit

### Implantação para Inferência  
Se desejar revisar o código de inferência ou recarregar o modelo de inferência, execute o comando `AI Toolkit: Deploy for inference`. Isso sincronizará seu código mais recente com o ACA e reiniciará a réplica.

![Deploy for inference](../../../../../translated_images/command-deploy.cb6508c973d6257e649aa4f262d3c170a374da3e9810a4f3d9e03935408a592b.pt.png)

Após a conclusão bem-sucedida da implantação, o modelo estará pronto para avaliação usando este endpoint.

### Acessando a API de Inferência

Você pode acessar a API de inferência clicando no botão "*Go to Inference Endpoint*" exibido na notificação do VSCode. Alternativamente, o endpoint da API web pode ser encontrado em `ACA_APP_ENDPOINT` dentro de `./infra/inference.config.json` e no painel de saída.

![App Endpoint](../../../../../translated_images/notification-deploy.00f4267b7aa6a18cfaaec83a7831b5d09311d5d96a70bb4c9d651ea4a41a8af7.pt.png)

> **Nota:** O endpoint de inferência pode levar alguns minutos para ficar totalmente operacional.

## Componentes de Inferência Incluídos no Template
 
| Pasta | Conteúdo |
| ------ |--------- |
| `infra` | Contém todas as configurações necessárias para operações remotas. |
| `infra/provision/inference.parameters.json` | Contém parâmetros para os templates bicep, usados para provisionar recursos Azure para inferência. |
| `infra/provision/inference.bicep` | Contém templates para provisionar recursos Azure para inferência. |
| `infra/inference.config.json` | O arquivo de configuração, gerado pelo comando `AI Toolkit: Provision Azure Container Apps for inference`. É usado como entrada para outros comandos remotos na paleta de comandos. |

### Usando o AI Toolkit para configurar o Provisionamento de Recursos Azure  
Configure o [AI Toolkit](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

Provisionar Azure Container Apps para inferência` command.

You can find configuration parameters in `./infra/provision/inference.parameters.json` file. Here are the details:
| Parameter | Description |
| --------- |------------ |
| `defaultCommands` | This is the commands to initiate a web API. |
| `maximumInstanceCount` | This parameter sets the maximum capacity of GPU instances. |
| `location` | This is the location where Azure resources are provisioned. The default value is the same as the chosen resource group's location. |
| `storageAccountName`, `fileShareName` `acaEnvironmentName`, `acaEnvironmentStorageName`, `acaAppName`,  `acaLogAnalyticsName` | These parameters are used to name the Azure resources for provision. By default, they will be same to the fine-tuning resource name. You can input a new, unused resource name to create your own custom-named resources, or you can input the name of an already existing Azure resource if you'd prefer to use that. For details, refer to the section [Using existing Azure Resources](../../../../../md/01.Introduction/03). |

### Using Existing Azure Resources

By default, the inference provision use the same Azure Container App Environment, Storage Account, Azure File Share, and Azure Log Analytics that were used for fine-tuning. A separate Azure Container App is created solely for the inference API. 

If you have customized the Azure resources during the fine-tuning step or want to use your own existing Azure resources for inference, specify their names in the `./infra/inference.parameters.json` arquivo. Depois, execute o comando `AI Toolkit: Provision Azure Container Apps for inference` na paleta de comandos. Isso atualiza quaisquer recursos especificados e cria os que estiverem faltando.

Por exemplo, se você já possui um ambiente de container Azure existente, seu arquivo `./infra/finetuning.parameters.json` deve ser parecido com este:

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

### Provisionamento Manual  
Se preferir configurar manualmente os recursos Azure, você pode usar os arquivos bicep fornecidos no arquivo `./infra/provision` folders. If you have already set up and configured all the Azure resources without using the AI Toolkit command palette, you can simply enter the resource names in the `inference.config.json`.

Por exemplo:

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

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.