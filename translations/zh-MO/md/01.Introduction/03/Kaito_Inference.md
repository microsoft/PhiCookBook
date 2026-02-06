## 使用 Kaito 進行推理

[Kaito](https://github.com/Azure/kaito) 是一個在 Kubernetes 叢集內自動化 AI/ML 推理模型部署的運營者。

與大多數基於虛擬機基礎架構構建的主流模型部署方法相比，Kaito 擁有以下主要區別：

- 使用容器映像管理模型文件。提供一個 http 伺服器，以使用模型庫執行推理呼叫。
- 通過提供預設配置，避免微調部署參數以適配 GPU 硬體。
- 根據模型需求自動配置 GPU 節點。
- 如果許可證允許，可在公共 Microsoft Container Registry (MCR) 中託管大型模型映像。

使用 Kaito，將大型 AI 推理模型引入 Kubernetes 的工作流程大為簡化。

## 架構

Kaito 遵循經典的 Kubernetes 自訂資源定義（CRD）／控制器設計模式。使用者管理一個描述 GPU 要求和推理規格的 `workspace` 自訂資源。Kaito 控制器將透過調和 `workspace` 自訂資源自動化部署。

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architecture" alt="KAITO RAGEngine architecture">
</div>

上圖展示了 Kaito 架構概覽。其主要元件包括：

- **Workspace 控制器**：調和 `workspace` 自訂資源，創建 `machine`（如下所述）自訂資源以觸發節點自動配置，並根據模型預設配置創建推理工作負載（`deployment` 或 `statefulset`）。
- **節點配置控制器**：該控制器在 [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) 中名為 *gpu-provisioner*。它使用源自 [Karpenter](https://sigs.k8s.io/karpenter) 的 `machine` CRD 與 workspace 控制器互動。它整合 Azure Kubernetes Service(AKS) API，向 AKS 叢集新增 GPU 節點。
> 注意：[ *gpu-provisioner* ](https://github.com/Azure/gpu-provisioner) 是一個開源元件。若其他控制器支持 [Karpenter-core](https://sigs.k8s.io/karpenter) API，可替代使用。

## 安裝

請查看此[安裝指南](https://github.com/Azure/kaito/blob/main/docs/installation.md)。

## 快速開始推理 Phi-3
[範例程式碼推理 Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # 調校輸出 ACR 路徑
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

可藉由執行以下指令來追蹤 workspace 狀態。當 WORKSPACEREADY 欄位顯示 `True` ，表示模型已成功部署。

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

接著，可找到推理服務的 cluster IP 並使用臨時的 `curl` Pod 來測試叢集內服務端點。

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## 快速開始推理 Phi-3 搭配適配器

安裝 Kaito 後，可嘗試以下指令來啟動推理服務。

[範例程式碼推理 Phi-3 搭配適配器](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # 調校輸出自動增益控制路徑
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

可藉由執行以下指令來追蹤 workspace 狀態。當 WORKSPACEREADY 欄位顯示 `True` ，表示模型已成功部署。

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

接著，可找到推理服務的 cluster IP 並使用臨時的 `curl` Pod 來測試叢集內服務端點。

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
本文件係使用人工智能翻譯服務[Co-op Translator](https://github.com/Azure/co-op-translator)進行翻譯。儘管我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。文件之原文版本應視為權威資料。對於重要信息，建議採用專業人工翻譯。我們不對因使用本翻譯而引致之任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->