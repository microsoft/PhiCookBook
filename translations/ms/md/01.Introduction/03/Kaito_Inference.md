## Inferens dengan Kaito 

[Kaito](https://github.com/Azure/kaito) adalah operator yang mengautomasikan penyebaran model inferens AI/ML dalam kluster Kubernetes.

Kaito mempunyai pembezaan utama berikut berbanding kebanyakan metodologi penyebaran model arus perdana yang dibina di atas infrastruktur mesin maya:

- Mengurus fail model menggunakan imej kontena. Pelayan http disediakan untuk melakukan panggilan inferens menggunakan perpustakaan model.
- Mengelakkan pelarasan parameter penyebaran untuk menyesuaikan perkakasan GPU dengan menyediakan konfigurasi pratetap.
- Penyediaan nod GPU secara automatik berdasarkan keperluan model.
- Mengehoskan imej model besar dalam Microsoft Container Registry (MCR) awam jika lesen membenarkan.

Dengan menggunakan Kaito, aliran kerja pemuatan model inferens AI besar dalam Kubernetes menjadi lebih mudah.


## Senibina

Kaito mengikuti corak reka bentuk Custom Resource Definition (CRD)/pengawal Kubernetes klasik. Pengguna menguruskan sumber tersuai `workspace` yang menerangkan keperluan GPU dan spesifikasi inferens. Pengawal Kaito akan mengautomasikan penyebaran dengan merekonsiliasi sumber tersuai `workspace`.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="Senibina KAITO RAGEngine" alt="Senibina KAITO RAGEngine">
</div>

Rajah di atas mempersembahkan gambaran keseluruhan senibina Kaito. Komponen utamanya terdiri daripada:

- **Pengawal Workspace**: Ia merekonsiliasi sumber tersuai `workspace`, mencipta sumber tersuai `machine` (diterangkan di bawah) untuk mencetuskan penyediaan nod automatik, dan mencipta beban kerja inferens (`deployment` atau `statefulset`) berdasarkan konfigurasi pratetap model.
- **Pengawal penyedia nod**: Nama pengawal ini adalah *gpu-provisioner* dalam [graf helm gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Ia menggunakan `machine` CRD yang berasal dari [Karpenter](https://sigs.k8s.io/karpenter) untuk berinteraksi dengan pengawal workspace. Ia berintegrasi dengan API Azure Kubernetes Service (AKS) untuk menambah nod GPU baru ke kluster AKS. 
> Nota: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) adalah komponen sumber terbuka. Ia boleh digantikan oleh pengawal lain jika menyokong API [Karpenter-core](https://sigs.k8s.io/karpenter).

## Pemasangan

Sila semak panduan pemasangan [di sini](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Mula Pantas Inferens Phi-3
[Contoh Kod Inferens Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Menyelaraskan Laluan Output ACR
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

Status workspace boleh dijejak dengan menjalankan arahan berikut. Apabila lajur WORKSPACEREADY menjadi `True`, model telah berjaya disebarkan.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Seterusnya, seseorang boleh mencari ip kluster perkhidmatan inferens dan menggunakan pod `curl` temporari untuk menguji titik akhir perkhidmatan dalam kluster.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Mula Pantas Inferens Phi-3 dengan penyesuai

Selepas memasang Kaito, seseorang boleh cuba arahan berikut untuk memulakan perkhidmatan inferens.

[Contoh Kod Inferens Phi-3 dengan Penyesuai](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Melaras Laluan Output ACR
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

Status workspace boleh dijejak dengan menjalankan arahan berikut. Apabila lajur WORKSPACEREADY menjadi `True`, model telah berjaya disebarkan.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Seterusnya, seseorang boleh mencari ip kluster perkhidmatan inferens dan menggunakan pod `curl` temporari untuk menguji titik akhir perkhidmatan dalam kluster.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sah. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->