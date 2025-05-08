<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a54cd3d65b6963e4e8ce21e143c3ab04",
  "translation_date": "2025-05-08T05:57:48+00:00",
  "source_file": "md/01.Introduction/03/Remote_Interence.md",
  "language_code": "hk"
}
-->
# 使用微調模型進行遠端推理

當 adapters 在遠端環境完成訓練後，可以用一個簡單的 Gradio 應用程式與模型互動。

![Fine-tune complete](../../../../../translated_images/log-finetuning-res.7b92254e7e822c7ffbec00f51a29199b0a53cefdd7fd2ce8330e4f787d98a94a.hk.png)

### 配置 Azure 資源
你需要透過在命令面板執行 `AI Toolkit: Provision Azure Container Apps for inference` 來設定遠端推理的 Azure 資源。設定過程中，系統會要求你選擇 Azure 訂閱和資源群組。  
![Provision Inference Resource](../../../../../translated_images/command-provision-inference.467afc8d351642fc03bc2ae439330ad1253da4f08ed8a8e98cdf89ca5c7ae4c5.hk.png)

預設情況下，推理的訂閱和資源群組應該與微調時使用的相同。推理會使用相同的 Azure Container App 環境，並存取在微調步驟中生成並儲存在 Azure Files 的模型及模型 adapter。

## 使用 AI Toolkit

### 推理部署
如果你想修改推理程式碼或重新載入推理模型，請執行 `AI Toolkit: Deploy for inference` 指令。這會同步你最新的程式碼到 ACA，並重新啟動副本。

![Deploy for inference](../../../../../translated_images/command-deploy.9adb4e310dd0b0aec6bb518f3c5b19a945ca040216da11e210666ad0330702ea.hk.png)

部署成功完成後，模型即可透過此端點進行評估。

### 存取推理 API

你可以點擊 VSCode 通知中的「*Go to Inference Endpoint*」按鈕來存取推理 API。或者，也可以在 `./infra/inference.config.json` 的 `ACA_APP_ENDPOINT` 下找到 Web API 端點，並在輸出面板查看。

![App Endpoint](../../../../../translated_images/notification-deploy.446e480a44b1be5848fd31391c467b8d42c2db1d5daffa2250c9fcd3d8486164.hk.png)

> **Note:** 推理端點可能需要幾分鐘才能完全啟用。

## 模板中包含的推理元件

| 資料夾 | 內容 |
| ------ |--------- |
| `infra` | 包含所有遠端操作所需的設定。 |
| `infra/provision/inference.parameters.json` | 儲存 bicep 範本的參數，用於配置推理的 Azure 資源。 |
| `infra/provision/inference.bicep` | 包含用於配置推理 Azure 資源的範本。 |
| `infra/inference.config.json` | 由 `AI Toolkit: Provision Azure Container Apps for inference` 指令生成的設定檔，用作其他遠端命令面板的輸入。 |

### 使用 AI Toolkit 配置 Azure 資源配置
設定 [AI Toolkit](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

配置 Azure Container Apps 進行推理，請參考 ` command.

You can find configuration parameters in `./infra/provision/inference.parameters.json` file. Here are the details:
| Parameter | Description |
| --------- |------------ |
| `defaultCommands` | This is the commands to initiate a web API. |
| `maximumInstanceCount` | This parameter sets the maximum capacity of GPU instances. |
| `location` | This is the location where Azure resources are provisioned. The default value is the same as the chosen resource group's location. |
| `storageAccountName`, `fileShareName` `acaEnvironmentName`, `acaEnvironmentStorageName`, `acaAppName`,  `acaLogAnalyticsName` | These parameters are used to name the Azure resources for provision. By default, they will be same to the fine-tuning resource name. You can input a new, unused resource name to create your own custom-named resources, or you can input the name of an already existing Azure resource if you'd prefer to use that. For details, refer to the section [Using existing Azure Resources](../../../../../md/01.Introduction/03). |

### Using Existing Azure Resources

By default, the inference provision use the same Azure Container App Environment, Storage Account, Azure File Share, and Azure Log Analytics that were used for fine-tuning. A separate Azure Container App is created solely for the inference API. 

If you have customized the Azure resources during the fine-tuning step or want to use your own existing Azure resources for inference, specify their names in the `./infra/inference.parameters.json` 檔案。然後，從命令面板執行 `AI Toolkit: Provision Azure Container Apps for inference` 指令。這會更新已指定的資源，並建立缺少的資源。

例如，如果你已有現成的 Azure container 環境，你的 `./infra/finetuning.parameters.json` 應該長這樣：

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
如果你想手動設定 Azure 資源，可以使用 `./infra/provision` folders. If you have already set up and configured all the Azure resources without using the AI Toolkit command palette, you can simply enter the resource names in the `inference.config.json` 檔案中提供的 bicep 檔案。

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
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯。雖然我哋盡力確保準確，但請注意自動翻譯可能包含錯誤或不準確之處。原文文件嘅母語版本應視為權威來源。對於重要資料，建議使用專業人工翻譯。我哋概不負責因使用此翻譯而引致嘅任何誤解或誤釋。