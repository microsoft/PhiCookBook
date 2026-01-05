<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aca91084bc440431571e00bf30d96ab8",
  "translation_date": "2026-01-05T01:18:58+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "ja"
}
-->
## Kaitoによる推論 

[Kaito](https://github.com/Azure/kaito) は Kubernetes クラスターでの AI/ML 推論モデルのデプロイを自動化するオペレーターです。

Kaito は、仮想マシン基盤上に構築された一般的なモデルデプロイ手法と比べて、以下の主な差別化点があります:

- コンテナイメージを用いてモデルファイルを管理します。モデルライブラリを使った推論呼び出しを行うための HTTP サーバーが提供されます。
- プリセット構成を提供することで、GPU ハードウェアに合わせたデプロイパラメーターの調整を回避します。
- モデル要件に基づいて GPU ノードを自動プロビジョニングします。
- ライセンスが許す場合、巨大なモデルイメージをパブリック Microsoft Container Registry (MCR) にホストします。

Kaito を使用することで、Kubernetes における大規模 AI 推論モデルのオンボーディングワークフローが大幅に簡素化されます。


## アーキテクチャ

Kaito は従来の Kubernetes Custom Resource Definition(CRD)/controller 設計パターンに従います。ユーザーは GPU 要件と推論仕様を記述した `workspace` カスタムリソースを管理します。Kaito コントローラは `workspace` カスタムリソースをリコンシルすることでデプロイを自動化します。

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine のアーキテクチャ" alt="KAITO RAGEngine のアーキテクチャ">
</div>

上図は Kaito のアーキテクチャ概要を示しています。主な構成要素は次のとおりです:

- **Workspace controller**: `workspace` カスタムリソースをリコンシルし、ノード自動プロビジョニングをトリガーする `machine`（下記参照）カスタムリソースを作成し、モデルのプリセット構成に基づいて推論ワークロード（`deployment` または `statefulset`）を作成します。
- **Node provisioner controller**: コントローラの名前は [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) 内では *gpu-provisioner* です。ワークスペースコントローラと連携するために [Karpenter](https://sigs.k8s.io/karpenter) に由来する `machine` CRD を使用します。Azure Kubernetes Service(AKS) の API と統合して、AKS クラスターに新しい GPU ノードを追加します。 
> 注: The [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) is an open sourced component. It can be replaced by other controllers if they support [Karpenter-core](https://sigs.k8s.io/karpenter) APIs.

## インストール

インストールの案内は [こちら](https://github.com/Azure/kaito/blob/main/docs/installation.md) をご確認ください。

## Inference Phi-3 クイックスタート
[Phi-3 推論 サンプルコード](https://github.com/Azure/kaito/tree/main/examples/inference)

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

以下のコマンドを実行することで workspace のステータスを追跡できます。WORKSPACEREADY 列が `True` になったら、モデルは正常にデプロイされています。

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

次に、推論サービスのクラスタ ip を確認し、クラスタ内の一時的な `curl` ポッドを使ってサービスエンドポイントをテストできます。

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## アダプター付き Phi-3 推論 クイックスタート

Kaito をインストールしたら、以下のコマンドを実行して推論サービスを起動できます。

[アダプター付き Phi-3 推論 サンプルコード](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # 出力ACRパスのチューニング
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

以下のコマンドを実行することで workspace のステータスを追跡できます。WORKSPACEREADY 列が `True` になったら、モデルは正常にデプロイされています。

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

次に、推論サービスのクラスタ ip を確認し、クラスタ内の一時的な `curl` ポッドを使ってサービスエンドポイントをテストできます。

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免責事項：
本書は AI 翻訳サービス「Co‑op Translator」（https://github.com/Azure/co-op-translator）を使用して翻訳されました。正確性には努めていますが、自動翻訳には誤りや不正確な表現が含まれる可能性があります。重要な情報については、専門の人間による翻訳を推奨します。原文（原語版）を正式な出典としてください。本翻訳の利用により生じた誤解や解釈の相違について、当方は責任を負いません。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->