<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-05-09T20:42:02+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "id"
}
-->
## Fine-Tuning dengan Kaito

[Kaito](https://github.com/Azure/kaito) adalah operator yang mengotomatiskan penyebaran model inferensi AI/ML di dalam klaster Kubernetes.

Kaito memiliki beberapa keunggulan utama dibandingkan dengan sebagian besar metode penyebaran model mainstream yang dibangun di atas infrastruktur mesin virtual:

- Mengelola file model menggunakan image container. Sebuah server http disediakan untuk melakukan panggilan inferensi menggunakan pustaka model.
- Menghindari penyesuaian parameter penyebaran agar sesuai dengan perangkat keras GPU dengan menyediakan konfigurasi yang sudah ditetapkan sebelumnya.
- Menyediakan node GPU secara otomatis berdasarkan kebutuhan model.
- Menyimpan image model besar di Microsoft Container Registry (MCR) publik jika lisensi mengizinkan.

Dengan menggunakan Kaito, alur kerja untuk mengintegrasikan model inferensi AI besar di Kubernetes menjadi jauh lebih sederhana.

## Arsitektur

Kaito mengikuti pola desain klasik Kubernetes Custom Resource Definition (CRD)/controller. Pengguna mengelola custom resource `workspace` yang menjelaskan kebutuhan GPU dan spesifikasi inferensi. Controller Kaito akan mengotomatiskan penyebaran dengan merekonsiliasi custom resource `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Gambar di atas menunjukkan gambaran umum arsitektur Kaito. Komponen utamanya terdiri dari:

- **Workspace controller**: Mengelola custom resource `workspace`, membuat custom resource `machine` (dijelaskan di bawah) untuk memicu penyediaan node otomatis, dan membuat beban kerja inferensi (`deployment` atau `statefulset`) berdasarkan konfigurasi preset model.
- **Node provisioner controller**: Nama controller ini adalah *gpu-provisioner* dalam [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Controller ini menggunakan CRD `machine` yang berasal dari [Karpenter](https://sigs.k8s.io/karpenter) untuk berinteraksi dengan workspace controller. Ia terintegrasi dengan API Azure Kubernetes Service (AKS) untuk menambahkan node GPU baru ke klaster AKS.
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) adalah komponen open source. Komponen ini bisa diganti dengan controller lain jika mendukung API [Karpenter-core](https://sigs.k8s.io/karpenter).

## Video gambaran umum  
[Tonton Demo Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Instalasi

Silakan cek panduan instalasi [di sini](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Mulai cepat

Setelah memasang Kaito, Anda bisa mencoba perintah berikut untuk memulai layanan fine-tuning.

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

Status workspace dapat dilacak dengan menjalankan perintah berikut. Ketika kolom WORKSPACEREADY menjadi `True`, model sudah berhasil disebarkan.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Selanjutnya, Anda bisa mencari IP klaster layanan inferensi dan menggunakan pod `curl` sementara untuk menguji endpoint layanan di dalam klaster.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi penting, disarankan menggunakan terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang salah yang timbul dari penggunaan terjemahan ini.