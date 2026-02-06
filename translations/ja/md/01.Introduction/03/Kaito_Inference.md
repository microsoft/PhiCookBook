## Kaitoによる推論

[Kaito](https://github.com/Azure/kaito) は、Kubernetesクラスタ内でのAI/ML推論モデルのデプロイメントを自動化するオペレーターです。

Kaitoは、ほとんどの仮想マシン基盤上に構築された主流のモデルデプロイメント手法と比べて、以下のような主要な差別化ポイントがあります：

- コンテナイメージを使ってモデルファイルを管理。モデルライブラリを用いて推論呼び出しを行うためのHTTPサーバーを提供。
- 事前設定済みの構成を提供し、GPUハードウェアに合わせたデプロイメントパラメーターのチューニングを回避。
- モデルの要件に応じてGPUノードを自動プロビジョニング。
- ライセンスが許す場合に、大規模モデルイメージをMicrosoftのパブリックコンテナレジストリ（MCR）にホスティング。

Kaitoを使うことで、Kubernetes上での大規模AI推論モデルのオンボーディングワークフローが大幅に簡素化されます。

## アーキテクチャ

KaitoはクラシックなKubernetesのカスタムリソース定義(CRD)/コントローラー設計パターンに従っています。ユーザーはGPU要件と推論仕様を記述した`workspace`カスタムリソースを管理します。Kaitoのコントローラーは`workspace`カスタムリソースの差分を調整することによってデプロイメントを自動化します。

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architecture" alt="KAITO RAGEngine architecture">
</div>

上図はKaitoのアーキテクチャ概要を示しています。主なコンポーネントは以下の通りです：

- **Workspace controller**：`workspace`カスタムリソースを調整し、ノードの自動プロビジョニングをトリガーする`machine`（下記参照）カスタムリソースを作成し、モデルの事前設定構成に基づいて推論ワークロード（`deployment`または`statefulset`）を作成します。
- **Node provisioner controller**：このコントローラーは[gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner)内では*gpu-provisioner*という名前です。Karpenter由来の`machine` CRDを用いてworkspace controllerと連携します。Azure Kubernetes Service(AKS)のAPIと統合してAKSクラスタに新しいGPUノードを追加します。  
> 注：[*gpu-provisioner*](https://github.com/Azure/gpu-provisioner)はオープンソースコンポーネントです。Karpenter-coreのAPIをサポートしている他のコントローラーに置き換えることも可能です。

## インストール

インストール手順は[こちら](https://github.com/Azure/kaito/blob/main/docs/installation.md)をご覧ください。

## クイックスタート推論 Phi-3
[サンプルコード 推論 Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # 出力ACRパスの調整
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

以下のコマンドを実行してワークスペースのステータスを追跡できます。WORKSPACEREADY列が`True`になると、モデルのデプロイが成功したことを示します。

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

次に、推論サービスのクラスタIPを探して、一時的な`curl`ポッドを使い、クラスタ内のサービスエンドポイントをテストできます。

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## アダプター付き クイックスタート 推論 Phi-3

Kaitoのインストール後、次のコマンドを試して推論サービスを開始できます。

[サンプルコード アダプター付き推論 Phi-3](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # 出力ACRパスの調整
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

以下のコマンドを実行してワークスペースのステータスを追跡できます。WORKSPACEREADY列が`True`になると、モデルのデプロイが成功したことを示します。

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

次に、推論サービスのクラスタIPを探して、一時的な`curl`ポッドを使い、クラスタ内のサービスエンドポイントをテストできます。

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本書類はAI翻訳サービス「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な表現が含まれる可能性があります。正式な情報源としては、原文の原言語版を参照してください。重要な情報については、専門の翻訳者による人手翻訳を推奨します。本翻訳の利用に伴う誤解や誤用について、当方は一切の責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->