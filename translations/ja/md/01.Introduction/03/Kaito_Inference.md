<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7739575218e3244a58516832ad88a9a2",
  "translation_date": "2025-04-04T12:04:57+00:00",
  "source_file": "md\\01.Introduction\\03\\Kaito_Inference.md",
  "language_code": "ja"
}
-->
## Kaitoによる推論

[Kaito](https://github.com/Azure/kaito)は、Kubernetesクラスター内でAI/ML推論モデルのデプロイメントを自動化するオペレーターです。

Kaitoは、従来の仮想マシンインフラストラクチャ上に構築された主流のモデルデプロイメント手法と比較して、以下のような主要な差別化要素を持っています：

- コンテナイメージを使用してモデルファイルを管理。モデルライブラリを使用して推論呼び出しを行うためのHTTPサーバーを提供。
- GPUハードウェアに合わせたデプロイメントパラメータの調整を避け、プリセット構成を提供。
- モデルの要件に基づいてGPUノードを自動的にプロビジョニング。
- ライセンスが許可する場合、大規模なモデルイメージをMicrosoft Container Registry(MCR)に公開でホスト。

Kaitoを使用することで、Kubernetesにおける大規模AI推論モデルのオンボーディングワークフローが大幅に簡略化されます。


## アーキテクチャ

Kaitoは、クラシックなKubernetesのCustom Resource Definition(CRD)/コントローラーデザインパターンに従っています。ユーザーは、GPUの要件と推論仕様を記述した`workspace`カスタムリソースを管理します。Kaitoコントローラーは、`workspace`カスタムリソースを調整することでデプロイメントを自動化します。
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

上記の図はKaitoのアーキテクチャ概要を示しています。その主要なコンポーネントは以下の通りです：

- **Workspaceコントローラー**: `workspace`カスタムリソースを調整し、ノード自動プロビジョニングをトリガーする`machine`（以下で説明）カスタムリソースを作成し、モデルプリセット構成に基づいて推論ワークロード(`deployment`または`statefulset`)を作成します。
- **Nodeプロビジョナーコントローラー**: このコントローラーの名前は[*gpu-provisioner*](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner)で、`machine` CRDを使用してWorkspaceコントローラーと対話します。[Karpenter](https://sigs.k8s.io/karpenter)に由来するCRDを使用しており、Azure Kubernetes Service(AKS) APIと統合してAKSクラスターに新しいGPUノードを追加します。
> 注: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner)はオープンソースのコンポーネントです。他のコントローラーが[Karpenter-core](https://sigs.k8s.io/karpenter) APIをサポートしている場合、置き換えることが可能です。

## インストール

インストールガイドについては[こちら](https://github.com/Azure/kaito/blob/main/docs/installation.md)を参照してください。

## Phi-3推論のクイックスタート
[Phi-3推論のサンプルコード](https://github.com/Azure/kaito/tree/main/examples/inference)

```
apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-phi-3-mini
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      apps: phi-3
inference:
  preset:
    name: phi-3-mini-4k-instruct
    # Note: This configuration also works with the phi-3-mini-128k-instruct preset
```

```sh
$ cat examples/inference/kaito_workspace_phi_3.yaml

apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-phi-3-mini
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      app: phi-3-adapter
tuning:
  preset:
    name: phi-3-mini-4k-instruct
  method: qlora
  input:
    urls:
      - "https://huggingface.co/datasets/philschmid/dolly-15k-oai-style/resolve/main/data/train-00000-of-00001-54e3756291ca09c6.parquet?download=true"
  output:
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Tuning Output ACR Path
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

以下のコマンドを実行することでWorkspaceのステータスを追跡できます。WORKSPACEREADY列が`True`になると、モデルが正常にデプロイされたことを意味します。

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

次に、推論サービスのクラスターIPを確認し、一時的な`curl`ポッドを使用してクラスター内のサービスエンドポイントをテストすることができます。

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## アダプター付きPhi-3推論のクイックスタート

Kaitoをインストールした後、以下のコマンドを試して推論サービスを開始することができます。

[アダプター付きPhi-3推論のサンプルコード](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

```
apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-phi-3-mini-adapter
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      apps: phi-3-adapter
inference:
  preset:
    name: phi-3-mini-128k-instruct
  adapters:
    - source:
        name: "phi-3-adapter"
        image: "ACR_REPO_HERE.azurecr.io/ADAPTER_HERE:0.0.1"
      strength: "1.0"
```

```sh
$ cat examples/inference/kaito_workspace_phi_3_with_adapters.yaml

apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-phi-3-mini-adapter
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      app: phi-3-adapter
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
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

以下のコマンドを実行することでWorkspaceのステータスを追跡できます。WORKSPACEREADY列が`True`になると、モデルが正常にデプロイされたことを意味します。

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

次に、推論サービスのクラスターIPを確認し、一時的な`curl`ポッドを使用してクラスター内のサービスエンドポイントをテストすることができます。

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期すよう努めておりますが、自動翻訳には誤りや不正確な部分が含まれる場合があります。元の言語で作成された文書が公式な情報源として考慮されるべきです。重要な情報については、専門の人間による翻訳をお勧めします。本翻訳の使用に起因する誤解や誤認について、当方は一切の責任を負いません。