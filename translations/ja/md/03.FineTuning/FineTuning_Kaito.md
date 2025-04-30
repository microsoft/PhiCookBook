<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "05e69691c294289d217150bec390a5fb",
  "translation_date": "2025-04-04T13:11:40+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Kaito.md",
  "language_code": "ja"
}
-->
## Kaito を使ったファインチューニング

[Kaito](https://github.com/Azure/kaito) は、Kubernetes クラスター内で AI/ML 推論モデルのデプロイを自動化するオペレーターです。

Kaito は、仮想マシンインフラストラクチャ上に構築された主流のモデルデプロイ手法と比較して、以下のような主な差別化ポイントがあります：

- コンテナイメージを使用してモデルファイルを管理します。モデルライブラリを使用して推論呼び出しを行うための HTTP サーバーが提供されます。
- GPU ハードウェアに適合させるためのデプロイパラメーターの調整を、プリセット構成を提供することで回避します。
- モデル要件に基づいて GPU ノードを自動プロビジョニングします。
- ライセンスが許可する場合には、大規模なモデルイメージを Microsoft Container Registry (MCR) にホストします。

Kaito を使用すると、Kubernetes で大規模な AI 推論モデルを導入するワークフローが大幅に簡略化されます。

## アーキテクチャ

Kaito は、Kubernetes のカスタムリソース定義 (CRD)/コントローラーデザインパターンに従っています。ユーザーは、GPU 要件と推論仕様を記述する `workspace` カスタムリソースを管理します。Kaito コントローラーは、この `workspace` カスタムリソースを調整することでデプロイを自動化します。
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito アーキテクチャ" alt="Kaito アーキテクチャ">
</div>

上図は Kaito のアーキテクチャ概要を示しています。主なコンポーネントは以下の通りです：

- **Workspace controller**: `workspace` カスタムリソースを調整し、ノード自動プロビジョニングをトリガーするために `machine`（後述）カスタムリソースを作成し、モデルのプリセット構成に基づいて推論ワークロード（`deployment` または `statefulset`）を作成します。
- **Node provisioner controller**: このコントローラーの名前は [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) では *gpu-provisioner* です。これは、[Karpenter](https://sigs.k8s.io/karpenter) 由来の `machine` CRD を使用して workspace controller と連携します。Azure Kubernetes Service (AKS) の API と統合し、AKS クラスターに新しい GPU ノードを追加します。
> 注意: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) はオープンソースコンポーネントです。他のコントローラーが [Karpenter-core](https://sigs.k8s.io/karpenter) API をサポートしている場合、それらに置き換えることができます。

## 概要ビデオ
[Kaito デモを見る](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## インストール

インストール手順については [こちら](https://github.com/Azure/kaito/blob/main/docs/installation.md) を参照してください。

## クイックスタート

Kaito をインストールした後、以下のコマンドを実行してファインチューニングサービスを開始できます。

```
apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-tuning-phi-3
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      app: tuning-phi-3
tuning:
  preset:
    name: phi-3-mini-128k-instruct
  method: qlora
  input:
    urls:
      - "https://huggingface.co/datasets/philschmid/dolly-15k-oai-style/resolve/main/data/train-00000-of-00001-54e3756291ca09c6.parquet?download=true"
  output:
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Tuning Output ACR Path
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
```

```sh
$ cat examples/fine-tuning/kaito_workspace_tuning_phi_3.yaml

apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-tuning-phi-3
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      app: tuning-phi-3
tuning:
  preset:
    name: phi-3-mini-128k-instruct
  method: qlora
  input:
    urls:
      - "https://huggingface.co/datasets/philschmid/dolly-15k-oai-style/resolve/main/data/train-00000-of-00001-54e3756291ca09c6.parquet?download=true"
  output:
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Tuning Output ACR Path
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/fine-tuning/kaito_workspace_tuning_phi_3.yaml
```

以下のコマンドを実行することで、workspace のステータスを確認できます。WORKSPACEREADY カラムが `True` になると、モデルが正常にデプロイされたことを示します。

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

次に、推論サービスのクラスター IP を確認し、クラスター内のエンドポイントをテストするために一時的な `curl` Pod を使用します。

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期すよう努めておりますが、自動翻訳には誤りや不正確な部分が含まれる場合があります。原文（元の言語で記載された文書）が信頼できる情報源とみなされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤解釈について、当方は一切の責任を負いません。