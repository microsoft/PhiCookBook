<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-05-08T05:22:51+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "ja"
}
-->
## Kaitoによるファインチューニング

[Kaito](https://github.com/Azure/kaito)は、Kubernetesクラスター内でAI/ML推論モデルのデプロイを自動化するオペレーターです。

Kaitoは、仮想マシン基盤上に構築された従来のモデルデプロイ手法と比べて、以下のような特徴を持っています：

- モデルファイルをコンテナイメージで管理。モデルライブラリを使った推論呼び出し用のHTTPサーバーを提供。
- GPUハードウェアに合わせたデプロイパラメーターの調整を不要にするプリセット構成を提供。
- モデル要件に基づいてGPUノードを自動プロビジョニング。
- ライセンスが許す場合、大規模モデルイメージをMicrosoft Container Registry (MCR)のパブリック領域にホスト。

Kaitoを使うことで、Kubernetes上での大規模AI推論モデルのオンボーディングが大幅に簡素化されます。


## アーキテクチャ

Kaitoは、クラシックなKubernetesのCustom Resource Definition(CRD)/コントローラーデザインパターンに従っています。ユーザーはGPU要件と推論仕様を記述した`workspace`カスタムリソースを管理します。Kaitoのコントローラーは`workspace`カスタムリソースを調整し、自動的にデプロイを行います。
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

上図はKaitoのアーキテクチャ概要を示しています。主な構成要素は以下の通りです：

- **Workspace controller**：`workspace`カスタムリソースを調整し、ノード自動プロビジョニングをトリガーする`machine`（後述）カスタムリソースを作成し、モデルのプリセット構成に基づいて推論ワークロード（`deployment`または`statefulset`）を作成します。
- **Node provisioner controller**：このコントローラーは[gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner)内で*gpu-provisioner*という名前です。[Karpenter](https://sigs.k8s.io/karpenter)由来の`machine` CRDを利用してworkspace controllerと連携し、Azure Kubernetes Service (AKS)のAPIと統合してAKSクラスターに新しいGPUノードを追加します。  
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner)はオープンソースのコンポーネントです。他のコントローラーで[Karpenter-core](https://sigs.k8s.io/karpenter) APIをサポートしていれば置き換え可能です。

## 概要動画  
[Kaitoデモを見る](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## インストール

インストール手順は[こちら](https://github.com/Azure/kaito/blob/main/docs/installation.md)をご確認ください。

## クイックスタート

Kaitoをインストールした後、以下のコマンドを試してファインチューニングサービスを開始できます。

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

ワークスペースの状態は次のコマンドで確認できます。WORKSPACEREADY列が`True`になれば、モデルのデプロイが成功しています。

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

次に、推論サービスのクラスタIPを取得し、一時的な`curl`ポッドを使ってクラスター内のサービスエンドポイントをテストできます。

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されています。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用により生じた誤解や誤訳について、当方は一切責任を負いかねます。