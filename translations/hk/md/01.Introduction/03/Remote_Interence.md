<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8782d16f62bc2bdae1f0b38f39a2417c",
  "translation_date": "2025-04-04T17:52:40+00:00",
  "source_file": "md\\01.Introduction\\03\\Remote_Interence.md",
  "language_code": "hk"
}
-->
# 遠端推理使用微調模型

當適配器在遠端環境完成訓練後，可以使用簡單的 Gradio 應用程式來與模型互動。

![微調完成](../../../../../translated_images/log-finetuning-res.4b3ee593f24d3096742d09375adade22b217738cab93bc1139f224e5888a1cbf.hk.png)

### 配置 Azure 資源
您需要透過命令面板執行 `AI Toolkit: Provision Azure Container Apps for inference` 來設置遠端推理所需的 Azure 資源。在此過程中，系統會要求您選擇 Azure 訂閱和資源群組。  
![配置推理資源](../../../../../translated_images/command-provision-inference.b294f3ae5764ab45b83246d464ad5329b0de20cf380f75a699b4cc6b5495ca11.hk.png)

預設情況下，推理所用的訂閱和資源群組應與微調時使用的相同。推理過程將使用相同的 Azure Container App 環境，並訪問存儲於 Azure Files 的模型及模型適配器，這些都是在微調階段生成的。

## 使用 AI 工具包

### 推理部署
如果您希望修改推理代碼或重新加載推理模型，請執行 `AI Toolkit: Deploy for inference` 命令。此命令會同步最新代碼至 ACA 並重新啟動副本。

![推理部署](../../../../../translated_images/command-deploy.cb6508c973d6257e649aa4f262d3c170a374da3e9810a4f3d9e03935408a592b.hk.png)

部署成功完成後，模型即可透過此端點進行評估。

### 訪問推理 API

您可以通過 VSCode 通知中顯示的 "*Go to Inference Endpoint*" 按鈕訪問推理 API。或者，Web API 端點可以在 `ACA_APP_ENDPOINT` 中找到，並顯示於 `./infra/inference.config.json` 和輸出面板中。

![應用端點](../../../../../translated_images/notification-deploy.00f4267b7aa6a18cfaaec83a7831b5d09311d5d96a70bb4c9d651ea4a41a8af7.hk.png)

> **注意:** 推理端點可能需要幾分鐘才能完全啟動。

## 模板中包含的推理元件

| 資料夾 | 內容 |
| ------ |--------- |
| `infra` | 包含所有遠端操作所需的配置。 |
| `infra/provision/inference.parameters.json` | 保存用於配置 Azure 資源的 bicep 模板參數。 |
| `infra/provision/inference.bicep` | 包含配置 Azure 資源的模板。 |
| `infra/inference.config.json` | 配置文件，由 `AI Toolkit: Provision Azure Container Apps for inference` 命令生成，用作其他遠端命令面板的輸入。 |

### 使用 AI 工具包配置 Azure 資源
配置 [AI 工具包](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

配置 Azure Container Apps 推理 ` command.

You can find configuration parameters in `./infra/provision/inference.parameters.json` file. Here are the details:
| Parameter | Description |
| --------- |------------ |
| `defaultCommands` | This is the commands to initiate a web API. |
| `maximumInstanceCount` | This parameter sets the maximum capacity of GPU instances. |
| `location` | This is the location where Azure resources are provisioned. The default value is the same as the chosen resource group's location. |
| `storageAccountName`, `fileShareName` `acaEnvironmentName`, `acaEnvironmentStorageName`, `acaAppName`,  `acaLogAnalyticsName` | These parameters are used to name the Azure resources for provision. By default, they will be same to the fine-tuning resource name. You can input a new, unused resource name to create your own custom-named resources, or you can input the name of an already existing Azure resource if you'd prefer to use that. For details, refer to the section [Using existing Azure Resources](../../../../../md/01.Introduction/03). |

### Using Existing Azure Resources

By default, the inference provision use the same Azure Container App Environment, Storage Account, Azure File Share, and Azure Log Analytics that were used for fine-tuning. A separate Azure Container App is created solely for the inference API. 

If you have customized the Azure resources during the fine-tuning step or want to use your own existing Azure resources for inference, specify their names in the `./infra/inference.parameters.json` 文件。接著，從命令面板執行 `AI Toolkit: Provision Azure Container Apps for inference` 命令。此命令會更新指定的資源並創建缺失的資源。

例如，如果您已擁有 Azure 容器環境，您的 `./infra/finetuning.parameters.json` 應如下所示：

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

### 手動配置  
如果您更喜歡手動設置 Azure 資源，可以使用 `./infra/provision` folders. If you have already set up and configured all the Azure resources without using the AI Toolkit command palette, you can simply enter the resource names in the `inference.config.json` 文件中提供的 bicep 文件。

例如：

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

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原文檔的母語版本應被視為具有權威性的來源。對於重要資訊，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。