## 使用 Kaito 進行推理

[Kaito](https://github.com/Azure/kaito) 是一個在 Kubernetes 叢集內自動化 AI/ML 推理模型部署的運營器。

與大多數基於虛擬機基礎設施構建的主流模型部署方法相比，Kaito 具有以下主要差異：

- 使用容器映像管理模型文件。提供 HTTP 伺服器以使用模型庫執行推理調用。
- 透過預設配置避免調整部署參數以適應 GPU 硬體。
- 根據模型需求自動配置 GPU 節點。
- 如果許可證允許，將大型模型映像託管於公共 Microsoft 容器註冊表 (MCR)。

使用 Kaito，將大型 AI 推理模型導入 Kubernetes 的工作流程大幅簡化。

## 架構

Kaito 採用經典的 Kubernetes 自訂資源定義（CRD）/控制器設計模式。使用者管理描述 GPU 需求和推理規範的 `workspace` 自訂資源。Kaito 控制器將通過調和 `workspace` 自訂資源來自動化部署。

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architecture" alt="KAITO RAGEngine architecture">
</div>

上述圖示呈現了 Kaito 架構概覽。其主要組件包括：

- **Workspace 控制器**：調和 `workspace` 自訂資源，建立 `machine`（如下說明）自訂資源以觸發節點自動配置，並根據模型預設配置建立推理工作負載（`deployment` 或 `statefulset`）。
- **節點配置器控制器**：該控制器在 [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) 中名為 *gpu-provisioner*。它使用源自 [Karpenter](https://sigs.k8s.io/karpenter) 的 `machine` CRD 與 workspace 控制器互動。它整合 Azure Kubernetes Service (AKS) API，將新的 GPU 節點新增至 AKS 叢集。
> 注意：[*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) 是開源元件。如果其他控制器支援 [Karpenter-core](https://sigs.k8s.io/karpenter) API，則可替代使用它。

## 安裝

請參考此處的安裝指引：[here](https://github.com/Azure/kaito/blob/main/docs/installation.md)。

## 快速開始推理 Phi-3
[Phi-3 推理範例程式碼](https://github.com/Azure/kaito/tree/main/examples/inference)

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
  
可透過下列指令追蹤 workspace 狀態。當 WORKSPACEREADY 欄位顯示 `True`，表示模型已成功部署。

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```
  
接著，可以尋找推理服務的叢集 IP，並使用臨時的 `curl` pod 在叢集中測試該服務端點。

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```
  
## 快速開始搭配 adapters 推理 Phi-3

安裝 Kaito 後，可以嘗試以下指令啟動推理服務。

[搭配 Adapters 的 Phi-3 推理範例程式碼](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # 調整輸出ACR路徑
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```
  
可透過下列指令追蹤 workspace 狀態。當 WORKSPACEREADY 欄位顯示 `True`，表示模型已成功部署。

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```
  
接著，可以尋找推理服務的叢集 IP，並使用臨時的 `curl` pod 在叢集中測試該服務端點。

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
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 所翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的原文版本應被視為權威來源。對於重要資訊，建議採用專業人類翻譯。我們不對因使用本翻譯而引致的任何誤解或錯譯負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->