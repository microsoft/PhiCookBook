<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7739575218e3244a58516832ad88a9a2",
  "translation_date": "2025-04-04T17:48:37+00:00",
  "source_file": "md\\01.Introduction\\03\\Kaito_Inference.md",
  "language_code": "hk"
}
-->
## Kaito 推理

[Kaito](https://github.com/Azure/kaito) 是一個操作工具，可以在 Kubernetes 群集內自動化部署 AI/ML 推理模型。

相比於大多數基於虛擬機基礎設施的主流模型部署方法，Kaito 具有以下主要差異：

- 使用容器映像管理模型文件，並提供一個 http 伺服器，用於使用模型庫進行推理調用。
- 通過提供預設配置，避免調整部署參數以適配 GPU 硬件。
- 根據模型需求自動配置 GPU 節點。
- 如果許可證允許，將大型模型映像託管在 Microsoft 公共容器註冊表 (MCR)。

使用 Kaito，可以大大簡化在 Kubernetes 中上線大型 AI 推理模型的工作流程。


## 架構

Kaito 遵循經典的 Kubernetes 自定義資源定義 (CRD) / 控制器設計模式。用戶管理 `workspace` 自定義資源，該資源描述了 GPU 需求和推理規範。Kaito 控制器將通過調和 `workspace` 自定義資源來自動化部署。
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito 架構" alt="Kaito 架構">
</div>

上圖展示了 Kaito 架構概覽。其主要組件包括：

- **工作空間控制器**：調和 `workspace` 自定義資源，創建 `machine`（下文解釋）自定義資源以觸發節點自動配置，並根據模型預設配置創建推理工作負載 (`deployment` 或 `statefulset`)。
- **節點配置控制器**：該控制器名稱為 [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) 中的 *gpu-provisioner*。它使用源自 [Karpenter](https://sigs.k8s.io/karpenter) 的 `machine` CRD 與工作空間控制器交互。它集成了 Azure Kubernetes Service (AKS) API，用於向 AKS 群集添加新的 GPU 節點。
> 注意：[*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) 是一個開源組件。如果其他控制器支持 [Karpenter-core](https://sigs.k8s.io/karpenter) API，則可以替換它。

## 安裝

請查看 [這裡](https://github.com/Azure/kaito/blob/main/docs/installation.md) 的安裝指南。

## Phi-3 推理快速入門
[Phi-3 推理範例代碼](https://github.com/Azure/kaito/tree/main/examples/inference)

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

可以通過運行以下命令追蹤工作空間狀態。當 WORKSPACEREADY 列顯示為 `True` 時，模型已成功部署。

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

接下來，可以找到推理服務的群集 IP，並使用一個臨時 `curl` pod 測試群集中的服務端點。

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## 使用適配器的 Phi-3 推理快速入門

安裝 Kaito 後，可以嘗試以下命令啟動推理服務。

[使用適配器的 Phi-3 推理範例代碼](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

可以通過運行以下命令追蹤工作空間狀態。當 WORKSPACEREADY 列顯示為 `True` 時，模型已成功部署。

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

接下來，可以找到推理服務的群集 IP，並使用一個臨時 `curl` pod 測試群集中的服務端點。

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**免責聲明**：  
本文件使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保翻譯準確性，但請注意，自動翻譯可能會包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們不對因使用此翻譯而引起的任何誤解或錯誤解釋承擔責任。