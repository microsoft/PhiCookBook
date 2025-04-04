<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "05e69691c294289d217150bec390a5fb",
  "translation_date": "2025-04-04T06:58:42+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Kaito.md",
  "language_code": "tw"
}
-->
## 使用 Kaito 進行微調

[Kaito](https://github.com/Azure/kaito) 是一個操作工具，可自動化在 Kubernetes 集群中部署 AI/ML 推理模型。

與大多數基於虛擬機基礎設施的主流模型部署方法相比，Kaito 具有以下主要差異：

- 使用容器映像管理模型文件。提供一個 HTTP 伺服器，用於使用模型庫進行推理調用。
- 提供預設配置，避免因適配 GPU 硬件而調整部署參數。
- 根據模型需求自動配置 GPU 節點。
- 如果許可證允許，可將大型模型映像托管於 Microsoft Container Registry (MCR)。

使用 Kaito，可以大幅簡化在 Kubernetes 中引入大型 AI 推理模型的工作流程。

## 架構

Kaito 遵循經典的 Kubernetes 自定義資源定義 (CRD) 和控制器設計模式。使用者管理一個 `workspace` 自定義資源，該資源描述了 GPU 需求和推理規範。Kaito 控制器將通過調和 `workspace` 自定義資源自動化部署。
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito 架構" alt="Kaito 架構">
</div>

上圖展示了 Kaito 架構概覽。其主要組件包括：

- **工作區控制器**：調和 `workspace` 自定義資源，創建 `machine`（如下所述）自定義資源以觸發節點自動配置，並根據模型預設配置創建推理工作負載（`deployment` 或 `statefulset`）。
- **節點配置控制器**：該控制器的名稱為 *gpu-provisioner*，位於 [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner)。它使用來自 [Karpenter](https://sigs.k8s.io/karpenter) 的 `machine` CRD 與工作區控制器交互。該控制器整合 Azure Kubernetes Service (AKS) API，為 AKS 集群新增 GPU 節點。
> 注意：[*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) 是一個開源組件。如果其他控制器支持 [Karpenter-core](https://sigs.k8s.io/karpenter) API，也可以替代使用。

## 概覽影片
[觀看 Kaito 演示](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## 安裝

請參考 [安裝指南](https://github.com/Azure/kaito/blob/main/docs/installation.md)。

## 快速入門

安裝 Kaito 後，可以嘗試以下命令啟動微調服務。

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

可以通過以下命令跟蹤工作區狀態。當 WORKSPACEREADY 列顯示 `True` 時，模型已成功部署。

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

接下來，可以找到推理服務的集群 IP，並使用臨時 `curl` pod 測試集群中的服務端點。

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保翻譯的準確性，但請注意，機器翻譯可能包含錯誤或不精確之處。原始語言的文件應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。