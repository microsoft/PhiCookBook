<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-05-09T11:56:38+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "id"
}
-->
## Inferensi dengan Kaito

[Kaito](https://github.com/Azure/kaito) adalah operator yang mengotomatiskan deployment model inferensi AI/ML di dalam cluster Kubernetes.

Kaito memiliki beberapa perbedaan utama dibandingkan dengan sebagian besar metode deployment model mainstream yang dibangun di atas infrastruktur mesin virtual:

- Mengelola file model menggunakan container image. Sebuah server http disediakan untuk melakukan panggilan inferensi menggunakan library model.
- Menghindari penyesuaian parameter deployment agar sesuai dengan perangkat keras GPU dengan menyediakan konfigurasi preset.
- Menyediakan node GPU secara otomatis berdasarkan kebutuhan model.
- Menyimpan image model besar di Microsoft Container Registry (MCR) publik jika lisensi mengizinkan.

Dengan menggunakan Kaito, alur kerja onboarding model inferensi AI besar di Kubernetes menjadi jauh lebih sederhana.

## Arsitektur

Kaito mengikuti pola desain klasik Kubernetes Custom Resource Definition(CRD)/controller. Pengguna mengelola custom resource `workspace` yang mendeskripsikan kebutuhan GPU dan spesifikasi inferensi. Controller Kaito akan mengotomatiskan deployment dengan merekonsiliasi custom resource `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Gambar di atas menunjukkan gambaran umum arsitektur Kaito. Komponen utamanya terdiri dari:

- **Workspace controller**: Merekonsiliasi custom resource `workspace`, membuat custom resource `machine` (dijelaskan di bawah) untuk memicu penyediaan node otomatis, dan membuat beban kerja inferensi (`deployment` atau `statefulset`) berdasarkan konfigurasi preset model.
- **Node provisioner controller**: Nama controller ini adalah *gpu-provisioner* dalam [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Controller ini menggunakan CRD `machine` yang berasal dari [Karpenter](https://sigs.k8s.io/karpenter) untuk berinteraksi dengan workspace controller. Controller ini terintegrasi dengan API Azure Kubernetes Service (AKS) untuk menambahkan node GPU baru ke cluster AKS.
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) adalah komponen open source. Komponen ini dapat diganti dengan controller lain jika mendukung API [Karpenter-core](https://sigs.k8s.io/karpenter).

## Instalasi

Silakan cek panduan instalasi [di sini](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Memulai Cepat Inferensi Phi-3  
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

Status workspace dapat dipantau dengan menjalankan perintah berikut. Ketika kolom WORKSPACEREADY menjadi `True`, model sudah berhasil dideploy.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Selanjutnya, Anda dapat mencari IP cluster dari layanan inferensi dan menggunakan pod `curl` sementara untuk menguji endpoint layanan di cluster.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Memulai Cepat Inferensi Phi-3 dengan adapter

Setelah menginstal Kaito, Anda dapat mencoba perintah berikut untuk memulai layanan inferensi.

[Sample Code Inference Phi-3 dengan Adapter](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

Status workspace dapat dipantau dengan menjalankan perintah berikut. Ketika kolom WORKSPACEREADY menjadi `True`, model sudah berhasil dideploy.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Selanjutnya, Anda dapat mencari IP cluster dari layanan inferensi dan menggunakan pod `curl` sementara untuk menguji endpoint layanan di cluster.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang timbul dari penggunaan terjemahan ini.