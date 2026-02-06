## Suy luận với Kaito

[Kaito](https://github.com/Azure/kaito) là một operator tự động hóa việc triển khai mô hình suy luận AI/ML trong cụm Kubernetes.

Kaito có những điểm khác biệt chính so với hầu hết các phương pháp triển khai mô hình phổ biến được xây dựng trên cơ sở hạ tầng máy ảo:

- Quản lý tệp mô hình bằng cách sử dụng hình ảnh container. Một máy chủ http được cung cấp để thực hiện các cuộc gọi suy luận sử dụng thư viện mô hình.
- Tránh tinh chỉnh các tham số triển khai để phù hợp với phần cứng GPU bằng cách cung cấp các cấu hình đặt trước.
- Tự động cấp phát các node GPU dựa trên yêu cầu mô hình.
- Lưu trữ hình ảnh mô hình lớn trong Microsoft Container Registry (MCR) công khai nếu giấy phép cho phép.

Sử dụng Kaito, quy trình đưa các mô hình suy luận AI lớn vào Kubernetes được đơn giản hóa đáng kể.

## Kiến trúc

Kaito tuân theo mẫu thiết kế điển hình Kubernetes Custom Resource Definition (CRD)/controller. Người dùng quản lý một tài nguyên tùy chỉnh `workspace` mô tả các yêu cầu GPU và đặc tả suy luận. Các controller của Kaito sẽ tự động triển khai bằng cách điều chỉnh tài nguyên tùy chỉnh `workspace`.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architecture" alt="KAITO RAGEngine architecture">
</div>

Hình trên trình bày tổng quan kiến trúc Kaito. Các thành phần chính bao gồm:

- **Workspace controller**: Nó điều chỉnh tài nguyên tùy chỉnh `workspace`, tạo các tài nguyên tùy chỉnh `machine` (giải thích bên dưới) để kích hoạt việc tự động cấp phát node, và tạo workload suy luận (`deployment` hoặc `statefulset`) dựa trên các cấu hình mô hình đặt trước.
- **Node provisioner controller**: Tên controller là *gpu-provisioner* trong [helm chart gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Nó sử dụng CRD `machine` xuất phát từ [Karpenter](https://sigs.k8s.io/karpenter) để tương tác với workspace controller. Nó tích hợp với các API Azure Kubernetes Service (AKS) để thêm các node GPU mới vào cụm AKS.
> Lưu ý: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) là một thành phần mã nguồn mở. Nó có thể được thay thế bằng các controller khác nếu chúng hỗ trợ các API [Karpenter-core](https://sigs.k8s.io/karpenter).

## Cài đặt

Vui lòng xem hướng dẫn cài đặt [tại đây](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Bắt đầu nhanh Suy luận Phi-3
[Mã mẫu Suy luận Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Điều chỉnh Đường dẫn ACR Đầu ra
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

Trạng thái workspace có thể được theo dõi bằng cách chạy lệnh sau. Khi cột WORKSPACEREADY trở thành `True`, mô hình đã được triển khai thành công.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Tiếp theo, bạn có thể tìm địa chỉ ip của dịch vụ suy luận trong cụm và sử dụng một pod `curl` tạm thời để kiểm tra điểm cuối dịch vụ trong cụm.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Bắt đầu nhanh Suy luận Phi-3 với bộ chuyển đổi

Sau khi cài đặt Kaito, bạn có thể thử các lệnh sau để khởi động dịch vụ suy luận.

[Mã mẫu Suy luận Phi-3 với Bộ chuyển đổi](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Tinh chỉnh Đường dẫn ACR Đầu ra
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

Trạng thái workspace có thể được theo dõi bằng cách chạy lệnh sau. Khi cột WORKSPACEREADY trở thành `True`, mô hình đã được triển khai thành công.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Tiếp theo, bạn có thể tìm địa chỉ ip của dịch vụ suy luận trong cụm và sử dụng một pod `curl` tạm thời để kiểm tra điểm cuối dịch vụ trong cụm.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn chính xác nhất. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp của con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->