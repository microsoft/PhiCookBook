<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a54cd3d65b6963e4e8ce21e143c3ab04",
  "translation_date": "2025-07-16T21:16:27+00:00",
  "source_file": "md/01.Introduction/03/Remote_Interence.md",
  "language_code": "ja"
}
-->
# ファインチューニング済みモデルを使ったリモート推論

リモート環境でアダプターのトレーニングが完了したら、シンプルなGradioアプリケーションを使ってモデルと対話します。

![Fine-tune complete](../../../../../translated_images/ja/log-finetuning-res.7b92254e7e822c7f.png)

### Azureリソースのプロビジョニング
リモート推論用にAzureリソースをセットアップするには、コマンドパレットから `AI Toolkit: Provision Azure Container Apps for inference` を実行してください。このセットアップ中に、Azureサブスクリプションとリソースグループの選択を求められます。  
![Provision Inference Resource](../../../../../translated_images/ja/command-provision-inference.467afc8d351642fc.png)
   
デフォルトでは、推論用のサブスクリプションとリソースグループはファインチューニングで使用したものと同じにする必要があります。推論は同じAzure Container App環境を使用し、ファインチューニング時に生成されたAzure Filesに保存されたモデルとモデルアダプターにアクセスします。

## AI Toolkitの使用方法

### 推論用のデプロイ  
推論コードを修正したり、推論モデルを再読み込みしたい場合は、`AI Toolkit: Deploy for inference` コマンドを実行してください。これにより最新のコードがACAと同期され、レプリカが再起動されます。

![Deploy for inference](../../../../../translated_images/ja/command-deploy.9adb4e310dd0b0ae.png)

デプロイが正常に完了すると、このエンドポイントを使ってモデルの評価が可能になります。

### 推論APIへのアクセス

VSCodeの通知に表示される「*Go to Inference Endpoint*」ボタンをクリックすると推論APIにアクセスできます。あるいは、`./infra/inference.config.json` の `ACA_APP_ENDPOINT` や出力パネルからWeb APIのエンドポイントを確認できます。

![App Endpoint](../../../../../translated_images/ja/notification-deploy.446e480a44b1be58.png)

> **注意:** 推論エンドポイントが完全に稼働するまでに数分かかる場合があります。

## テンプレートに含まれる推論コンポーネント

| フォルダー | 内容 |
| ------ |--------- |
| `infra` | リモート操作に必要なすべての設定を含みます。 |
| `infra/provision/inference.parameters.json` | bicepテンプレート用のパラメーターを保持し、推論用Azureリソースのプロビジョニングに使用されます。 |
| `infra/provision/inference.bicep` | 推論用Azureリソースのプロビジョニングテンプレートを含みます。 |
| `infra/inference.config.json` | `AI Toolkit: Provision Azure Container Apps for inference` コマンドで生成される設定ファイルで、他のリモートコマンドパレットの入力として使われます。 |

### AI Toolkitを使ったAzureリソースのプロビジョニング設定
[AI Toolkit](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)を設定し、`Provision Azure Container Apps for inference` コマンドを実行します。

設定パラメーターは `./infra/provision/inference.parameters.json` ファイルにあります。詳細は以下の通りです：

| パラメーター | 説明 |
| --------- |------------ |
| `defaultCommands` | Web APIを起動するためのコマンドです。 |
| `maximumInstanceCount` | GPUインスタンスの最大数を設定します。 |
| `location` | Azureリソースをプロビジョニングする場所です。デフォルトは選択したリソースグループの場所と同じです。 |
| `storageAccountName`, `fileShareName`, `acaEnvironmentName`, `acaEnvironmentStorageName`, `acaAppName`, `acaLogAnalyticsName` | これらはプロビジョニングするAzureリソースの名前に使われます。デフォルトではファインチューニング用リソース名と同じです。新しい未使用のリソース名を入力してカスタムリソースを作成することも、既存のAzureリソース名を指定して使用することも可能です。詳細は[既存のAzureリソースの使用](../../../../../md/01.Introduction/03)セクションを参照してください。 |

### 既存のAzureリソースの使用

デフォルトでは、推論のプロビジョニングはファインチューニングで使用したAzure Container App環境、ストレージアカウント、Azureファイル共有、Azure Log Analyticsをそのまま利用します。推論API用に別のAzure Container Appが作成されます。

ファインチューニング時にAzureリソースをカスタマイズした場合や、推論に既存のAzureリソースを使いたい場合は、`./infra/inference.parameters.json` ファイルにそれらの名前を指定してください。その後、コマンドパレットから `AI Toolkit: Provision Azure Container Apps for inference` を実行します。これにより指定されたリソースが更新され、存在しないリソースは新たに作成されます。

例えば、既存のAzureコンテナ環境がある場合、`./infra/finetuning.parameters.json` は以下のようになります：

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

### 手動プロビジョニング  
Azureリソースを手動で設定したい場合は、`./infra/provision` フォルダー内のbicepファイルを使用できます。AI Toolkitのコマンドパレットを使わずにすでにAzureリソースをセットアップ済みの場合は、`inference.config.json` ファイルにリソース名を入力するだけで構いません。

例：

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

**免責事項**：  

本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。
