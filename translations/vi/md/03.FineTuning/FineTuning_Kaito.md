## Tinh chỉnh với Kaito

[Kaito](https://github.com/Azure/kaito) là một operator tự động hóa việc triển khai mô hình suy luận AI/ML trong cụm Kubernetes.

Kaito có những điểm khác biệt chính so với hầu hết các phương pháp triển khai mô hình phổ biến dựa trên hạ tầng máy ảo:

- Quản lý các tệp mô hình bằng cách sử dụng hình ảnh container. Một máy chủ http được cung cấp để thực hiện các cuộc gọi suy luận sử dụng thư viện mô hình.
- Tránh việc điều chỉnh các tham số triển khai để phù hợp với phần cứng GPU bằng cách cung cấp các cấu hình mặc định.
- Tự động cấp phát các node GPU dựa trên yêu cầu của mô hình.
- Lưu trữ các hình ảnh mô hình lớn trong Microsoft Container Registry (MCR) công khai nếu giấy phép cho phép.

Sử dụng Kaito, quy trình đưa các mô hình suy luận AI lớn vào Kubernetes được đơn giản hóa đáng kể.

## Kiến trúc

Kaito tuân theo mẫu thiết kế điển hình của Kubernetes Custom Resource Definition (CRD)/controller. Người dùng quản lý một tài nguyên tùy chỉnh `workspace` mô tả yêu cầu GPU và đặc tả suy luận. Các controller của Kaito sẽ tự động triển khai bằng cách đồng bộ tài nguyên tùy chỉnh `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Hình trên trình bày tổng quan kiến trúc Kaito. Các thành phần chính bao gồm:

- **Workspace controller**: Nó đồng bộ tài nguyên tùy chỉnh `workspace`, tạo các tài nguyên tùy chỉnh `machine` (giải thích bên dưới) để kích hoạt việc tự động cấp phát node, và tạo workload suy luận (`deployment` hoặc `statefulset`) dựa trên các cấu hình mặc định của mô hình.
- **Node provisioner controller**: Controller này có tên là *gpu-provisioner* trong [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Nó sử dụng CRD `machine` bắt nguồn từ [Karpenter](https://sigs.k8s.io/karpenter) để tương tác với workspace controller. Nó tích hợp với API của Azure Kubernetes Service (AKS) để thêm các node GPU mới vào cụm AKS.
> Lưu ý: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) là một thành phần mã nguồn mở. Nó có thể được thay thế bằng các controller khác nếu chúng hỗ trợ API [Karpenter-core](https://sigs.k8s.io/karpenter).

## Video tổng quan  
[Xem Demo Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Cài đặt

Vui lòng xem hướng dẫn cài đặt [tại đây](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Bắt đầu nhanh

Sau khi cài đặt Kaito, bạn có thể thử các lệnh sau để khởi động dịch vụ tinh chỉnh.

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

Trạng thái workspace có thể được theo dõi bằng cách chạy lệnh sau. Khi cột WORKSPACEREADY hiển thị `True`, mô hình đã được triển khai thành công.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Tiếp theo, bạn có thể tìm địa chỉ IP của dịch vụ suy luận trong cụm và sử dụng một pod `curl` tạm thời để kiểm tra endpoint dịch vụ trong cụm.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.