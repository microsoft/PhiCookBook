<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-05-09T11:56:14+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "vi"
}
-->
## Inference với Kaito

[Kaito](https://github.com/Azure/kaito) là một operator tự động hóa việc triển khai mô hình AI/ML inference trong cụm Kubernetes.

Kaito có những điểm khác biệt chính so với hầu hết các phương pháp triển khai mô hình phổ biến dựa trên hạ tầng máy ảo:

- Quản lý file mô hình bằng cách sử dụng container images. Một server http được cung cấp để thực hiện các cuộc gọi inference sử dụng thư viện mô hình.
- Tránh việc điều chỉnh tham số triển khai cho phù hợp với phần cứng GPU bằng cách cung cấp các cấu hình mặc định.
- Tự động cấp phát các node GPU dựa trên yêu cầu của mô hình.
- Lưu trữ các ảnh mô hình lớn trên Microsoft Container Registry (MCR) công khai nếu giấy phép cho phép.

Sử dụng Kaito, quy trình đưa các mô hình AI inference lớn vào Kubernetes được đơn giản hóa rất nhiều.

## Kiến trúc

Kaito tuân theo mẫu thiết kế điển hình của Kubernetes Custom Resource Definition (CRD)/controller. Người dùng quản lý một tài nguyên tùy chỉnh `workspace` mô tả yêu cầu GPU và đặc tả inference. Các controller của Kaito sẽ tự động triển khai bằng cách đồng bộ tài nguyên tùy chỉnh `workspace`.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Hình trên trình bày tổng quan kiến trúc Kaito. Các thành phần chính gồm:

- **Workspace controller**: Đồng bộ tài nguyên tùy chỉnh `workspace`, tạo các tài nguyên tùy chỉnh `machine` (giải thích bên dưới) để kích hoạt tự động cấp phát node, và tạo workload inference (`deployment` hoặc `statefulset`) dựa trên cấu hình mặc định của mô hình.
- **Node provisioner controller**: Controller này có tên *gpu-provisioner* trong [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Nó sử dụng CRD `machine` xuất phát từ [Karpenter](https://sigs.k8s.io/karpenter) để tương tác với workspace controller. Nó tích hợp với API của Azure Kubernetes Service (AKS) để thêm các node GPU mới vào cụm AKS.
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) là một thành phần mã nguồn mở. Nó có thể được thay thế bằng các controller khác nếu chúng hỗ trợ API của [Karpenter-core](https://sigs.k8s.io/karpenter).

## Cài đặt

Vui lòng xem hướng dẫn cài đặt [tại đây](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Bắt đầu nhanh Inference Phi-3

[Sample Code Inference Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

Trạng thái workspace có thể được theo dõi bằng cách chạy lệnh sau. Khi cột WORKSPACEREADY hiện `True`, mô hình đã được triển khai thành công.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Tiếp theo, bạn có thể tìm địa chỉ cluster ip của dịch vụ inference và sử dụng một pod tạm thời `curl` để kiểm tra endpoint dịch vụ trong cụm.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Bắt đầu nhanh Inference Phi-3 với adapters

Sau khi cài đặt Kaito, bạn có thể thử các lệnh sau để khởi động dịch vụ inference.

[Sample Code Inference Phi-3 with Adapters](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

Trạng thái workspace có thể được theo dõi bằng cách chạy lệnh sau. Khi cột WORKSPACEREADY hiện `True`, mô hình đã được triển khai thành công.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Tiếp theo, bạn có thể tìm địa chỉ cluster ip của dịch vụ inference và sử dụng một pod tạm thời `curl` để kiểm tra endpoint dịch vụ trong cụm.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.