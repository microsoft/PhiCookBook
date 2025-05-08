<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-05-08T05:22:44+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "hk"
}
-->
## 使用 Kaito 進行微調

[Kaito](https://github.com/Azure/kaito) 是一個操作員，用來自動化 Kubernetes 叢集中 AI/ML 推論模型的部署。

相比於大多數基於虛擬機基礎設施的主流模型部署方法，Kaito 有以下主要優勢：

- 使用容器映像管理模型檔案，並提供一個 HTTP 伺服器以便透過模型庫進行推論呼叫。
- 透過預設配置避免為 GPU 硬件調整部署參數。
- 根據模型需求自動配置 GPU 節點。
- 若授權允許，可將大型模型映像托管於 Microsoft 公共容器註冊表（MCR）。

使用 Kaito，將大型 AI 推論模型引入 Kubernetes 的流程大幅簡化。

## 架構

Kaito 採用經典的 Kubernetes 自訂資源定義（CRD）與控制器設計模式。使用者管理一個 `workspace` 自訂資源，描述 GPU 需求和推論規格。Kaito 控制器會透過調和 `workspace` 自訂資源來自動部署。
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

上圖展示了 Kaito 架構概覽，主要組件包括：

- **Workspace controller**：調和 `workspace` 自訂資源，建立 `machine`（下文說明）自訂資源以觸發節點自動配置，並根據模型預設配置建立推論工作負載（`deployment` 或 `statefulset`）。
- **Node provisioner controller**：此控制器在 [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) 中名為 *gpu-provisioner*。它使用來自 [Karpenter](https://sigs.k8s.io/karpenter) 的 `machine` CRD 與 workspace controller 互動，並整合 Azure Kubernetes Service (AKS) API，向 AKS 叢集新增 GPU 節點。  
> 注意：[*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) 是一個開源元件。如果其他控制器支援 [Karpenter-core](https://sigs.k8s.io/karpenter) API，也可以替代它。

## 概覽影片  
[觀看 Kaito 示範](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## 安裝

請參考此處的安裝指引 [here](https://github.com/Azure/kaito/blob/main/docs/installation.md)。

## 快速開始

安裝 Kaito 後，可以嘗試以下指令啟動微調服務。

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

可以透過執行下列指令來追蹤 workspace 狀態。當 WORKSPACEREADY 欄位變成 `True` 時，表示模型已成功部署。

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

接著，可以找到推論服務的叢集 IP，並使用臨時的 `curl` Pod 測試叢集內的服務端點。

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我哋盡力確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件嘅母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我哋對因使用此翻譯而引致嘅任何誤解或誤釋概不負責。