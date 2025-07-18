<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-07-16T20:48:29+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "ja"
}
-->
## Kaitoによる推論

[Kaito](https://github.com/Azure/kaito)は、Kubernetesクラスター内でAI/ML推論モデルのデプロイを自動化するオペレーターです。

Kaitoは、仮想マシン基盤上に構築された一般的なモデルデプロイ手法と比べて、以下のような特徴があります：

- モデルファイルをコンテナイメージで管理。モデルライブラリを使った推論呼び出しを行うためのHTTPサーバーを提供。
- GPUハードウェアに合わせたデプロイパラメーターの調整を避けるため、プリセット構成を提供。
- モデルの要件に基づいてGPUノードを自動プロビジョニング。
- ライセンスが許す場合、大型モデルイメージをMicrosoftのパブリックコンテナレジストリ（MCR）にホスト。

Kaitoを使うことで、Kubernetes上での大規模AI推論モデルの導入ワークフローが大幅に簡素化されます。


## アーキテクチャ

Kaitoは、Kubernetesのカスタムリソース定義（CRD）とコントローラーのクラシックな設計パターンに従っています。ユーザーはGPU要件や推論仕様を記述した`workspace`カスタムリソースを管理します。Kaitoのコントローラーは`workspace`カスタムリソースを調整し、自動的にデプロイを行います。
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

上図はKaitoのアーキテクチャ概要を示しています。主なコンポーネントは以下の通りです：

- **Workspace controller**：`workspace`カスタムリソースを調整し、ノードの自動プロビジョニングをトリガーする`machine`（後述）カスタムリソースを作成し、モデルのプリセット構成に基づいて推論ワークロード（`deployment`または`statefulset`）を作成します。
- **Node provisioner controller**：このコントローラーは[gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner)内で*gpu-provisioner*と呼ばれています。`machine` CRDは[Karpenter](https://sigs.k8s.io/karpenter)由来で、workspace controllerと連携します。Azure Kubernetes Service（AKS）のAPIと統合し、AKSクラスターに新しいGPUノードを追加します。
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner)はオープンソースのコンポーネントです。もし他のコントローラーが[Karpenter-core](https://sigs.k8s.io/karpenter) APIをサポートしていれば、置き換え可能です。

## インストール

インストール手順は[こちら](https://github.com/Azure/kaito/blob/main/docs/installation.md)をご確認ください。

## クイックスタート 推論 Phi-3
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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Tuning Output ACR Path
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

以下のコマンドでworkspaceの状態を確認できます。WORKSPACEREADY列が`True`になれば、モデルのデプロイが成功しています。

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

次に、推論サービスのクラスタIPを取得し、一時的な`curl`ポッドを使ってクラスター内のサービスエンドポイントをテストできます。

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## クイックスタート 推論 Phi-3 アダプター付き

Kaitoをインストールした後、以下のコマンドで推論サービスを起動できます。

[サンプルコード 推論 Phi-3 アダプター付き](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

以下のコマンドでworkspaceの状態を確認できます。WORKSPACEREADY列が`True`になれば、モデルのデプロイが成功しています。

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

次に、推論サービスのクラスタIPを取得し、一時的な`curl`ポッドを使ってクラスター内のサービスエンドポイントをテストできます。

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は責任を負いかねます。