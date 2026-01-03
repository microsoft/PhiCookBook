<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a54cd3d65b6963e4e8ce21e143c3ab04",
  "translation_date": "2025-07-16T21:15:53+00:00",
  "source_file": "md/01.Introduction/03/Remote_Interence.md",
  "language_code": "mo"
}
-->
# 使用微調模型進行遠端推論

在遠端環境完成 adapters 訓練後，可以使用簡單的 Gradio 應用程式與模型互動。

![Fine-tune complete](../../../../../translated_images/log-finetuning-res.7b92254e7e822c7f.mo.png)

### 配置 Azure 資源
您需要透過命令面板執行 `AI Toolkit: Provision Azure Container Apps for inference` 來設定遠端推論所需的 Azure 資源。設定過程中，系統會要求您選擇 Azure 訂閱和資源群組。  
![Provision Inference Resource](../../../../../translated_images/command-provision-inference.467afc8d351642fc.mo.png)

預設情況下，推論所使用的訂閱和資源群組應與微調時相同。推論將使用相同的 Azure Container App 環境，並存取在微調階段產生並儲存在 Azure Files 的模型及模型 adapter。

## 使用 AI Toolkit

### 部署推論
如果您想修改推論程式碼或重新載入推論模型，請執行 `AI Toolkit: Deploy for inference` 指令。此操作會將您最新的程式碼同步至 ACA 並重新啟動副本。

![Deploy for inference](../../../../../translated_images/command-deploy.9adb4e310dd0b0ae.mo.png)

部署成功後，模型即可透過此端點進行評估。

### 存取推論 API

您可以點擊 VSCode 通知中顯示的「*Go to Inference Endpoint*」按鈕來存取推論 API。或者，您也可以在 `./infra/inference.config.json` 的 `ACA_APP_ENDPOINT` 欄位以及輸出面板中找到 Web API 端點。

![App Endpoint](../../../../../translated_images/notification-deploy.446e480a44b1be58.mo.png)

> **Note:** 推論端點可能需要幾分鐘時間才能完全啟用。

## 範本中包含的推論元件

| 資料夾 | 內容 |
| ------ |------ |
| `infra` | 包含遠端操作所需的所有設定檔。 |
| `infra/provision/inference.parameters.json` | 儲存 bicep 模板的參數，用於配置推論的 Azure 資源。 |
| `infra/provision/inference.bicep` | 用於配置推論 Azure 資源的 bicep 模板。 |
| `infra/inference.config.json` | 由 `AI Toolkit: Provision Azure Container Apps for inference` 指令產生的設定檔，作為其他遠端命令面板的輸入。 |

### 使用 AI Toolkit 配置 Azure 資源配置
設定 [AI Toolkit](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

執行 `Provision Azure Container Apps for inference` 指令。

您可以在 `./infra/provision/inference.parameters.json` 檔案中找到配置參數。詳細說明如下：

| 參數 | 說明 |
| --------- |------------ |
| `defaultCommands` | 用於啟動 Web API 的指令。 |
| `maximumInstanceCount` | 設定 GPU 實例的最大容量。 |
| `location` | Azure 資源配置的位置，預設值與所選資源群組位置相同。 |
| `storageAccountName`、`fileShareName`、`acaEnvironmentName`、`acaEnvironmentStorageName`、`acaAppName`、`acaLogAnalyticsName` | 用於命名 Azure 資源的參數。預設會與微調時使用的資源名稱相同。您可以輸入新的未使用資源名稱以建立自訂命名的資源，或輸入已存在的 Azure 資源名稱以使用該資源。詳情請參考[使用現有 Azure 資源](../../../../../md/01.Introduction/03)章節。 |

### 使用現有 Azure 資源

預設情況下，推論配置會使用微調時所用的相同 Azure Container App 環境、儲存帳戶、Azure File Share 及 Azure Log Analytics。推論 API 則會建立一個獨立的 Azure Container App。

如果您在微調階段已自訂 Azure 資源，或想使用您自己的現有 Azure 資源進行推論，請在 `./infra/inference.parameters.json` 檔案中指定它們的名稱。接著，從命令面板執行 `AI Toolkit: Provision Azure Container Apps for inference` 指令。此操作會更新指定的資源並建立缺少的資源。

例如，若您已有現成的 Azure container 環境，您的 `./infra/finetuning.parameters.json` 應該如下所示：

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
如果您偏好手動設定 Azure 資源，可以使用 `./infra/provision` 資料夾中提供的 bicep 檔案。如果您已經完成 Azure 資源的設定且未使用 AI Toolkit 命令面板，則只需在 `inference.config.json` 檔案中輸入資源名稱即可。

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
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。