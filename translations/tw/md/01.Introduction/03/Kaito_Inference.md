<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aca91084bc440431571e00bf30d96ab8",
  "translation_date": "2026-01-05T17:33:21+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "tw"
}
-->
## 使用 Kaito 進行推論

[Kaito](https://github.com/Azure/kaito) 是一個操作器，用於自動化 Kubernetes 叢集中 AI/ML 推論模型的部署。

與大多數建立在虛擬機基礎設施之上的主流模型部署方法相比，Kaito 具有以下主要差異：

- 使用容器映像管理模型文件。提供一個 HTTP 服務器，使用模型庫執行推論調用。
- 通過提供預設配置，避免為適配 GPU 硬體調整部署參數。
- 根據模型需求自動配置 GPU 節點。
- 如果許可證允許，則在公共 Microsoft Container Registry (MCR) 中託管大型模型映像。

使用 Kaito，可大幅簡化在 Kubernetes 中上線大型 AI 推論模型的工作流程。

## 架構

Kaito 遵循經典的 Kubernetes 自訂資源定義(CRD)/控制器設計模式。使用者管理一個描述 GPU 需求和推論規格的 `workspace` 自訂資源。Kaito 控制器會通過調和 `workspace` 自訂資源來自動部署。

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architecture" alt="KAITO RAGEngine architecture">
</div>

上圖展示了 Kaito 架構概覽。其主要元件包括：

- **Workspace 控制器**：調和 `workspace` 自訂資源，建立 `machine`（下方解釋）自訂資源以觸發節點自動配置，並根據模型預設配置創建推論工作負載（`deployment` 或 `statefulset`）。
- **節點配置控制器**：該控制器名為 *gpu-provisioner*，於 [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) 中。它使用來自 [Karpenter](https://sigs.k8s.io/karpenter) 的 `machine` CRD 與 workspace 控制器互動。整合 Azure Kubernetes Service (AKS) API，向 AKS 叢集添加新的 GPU 節點。
> 注意：[*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) 是一個開源元件。若其他控制器支援 [Karpenter-core](https://sigs.k8s.io/karpenter) API，則可以替換此元件。

## 安裝

請參閱此處的安裝指引 [here](https://github.com/Azure/kaito/blob/main/docs/installation.md)。

## 快速開始推論 Phi-3
[示範程式碼 推論 Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # 調整輸出 ACR 路徑
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

可以使用以下命令追蹤 workspace 狀態。當 WORKSPACEREADY 欄位顯示為 `True`，表示模型已成功部署。

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

接著，可以找到推論服務的叢集 IP，並使用臨時的 `curl` Pod 在叢集內測試服務端點。

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## 快速開始推論 Phi-3，搭配 adapters

安裝 Kaito 後，可以執行以下指令啟動推論服務。

[示範程式碼 推論 Phi-3 搭配 Adapters](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # 調整輸出 ACR 路徑
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

可以使用以下命令追蹤 workspace 狀態。當 WORKSPACEREADY 欄位顯示為 `True`，表示模型已成功部署。

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

接著，可以找到推論服務的叢集 IP，並使用臨時的 `curl` Pod 在叢集內測試服務端點。

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議使用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤用負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->