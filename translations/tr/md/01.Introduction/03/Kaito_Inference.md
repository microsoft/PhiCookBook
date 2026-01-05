<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aca91084bc440431571e00bf30d96ab8",
  "translation_date": "2026-01-05T03:44:08+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "tr"
}
-->
## Kaito ile Çıkarım 

[Kaito](https://github.com/Azure/kaito) Kubernetes kümesinde AI/ML çıkarım model dağıtımını otomatikleştiren bir operatördür.

Kaito'ın, sanal makine altyapıları üzerine kurulu çoğu ana akım model dağıtım yöntemlerine kıyasla aşağıdaki temel farklılıkları vardır:

- Model dosyalarını konteyner imajları kullanarak yönetir. Model kitaplığı kullanılarak çıkarım çağrılarını gerçekleştirmek için bir http sunucusu sağlanır.
- Önceden ayarlanmış yapılandırmalar sağlayarak GPU donanımına uyacak şekilde dağıtım parametrelerini ayarlamaktan kaçınır.
- Model gereksinimlerine göre GPU düğümlerini otomatik olarak sağlar.
- Lisans izin veriyorsa büyük model imajlarını genel Microsoft Container Registry (MCR) içinde barındırır.

Kaito kullanılarak, Kubernetes'te büyük AI çıkarım modellerinin alınması iş akışı büyük ölçüde basitleştirilir.


## Mimari

Kaito, klasik Kubernetes Custom Resource Definition(CRD)/controller tasarım desenini takip eder. Kullanıcı, GPU gereksinimlerini ve çıkarım spesifikasyonunu tanımlayan bir `workspace` özel kaynağını yönetir. Kaito denetleyicileri, `workspace` özel kaynağını uzlaştırarak dağıtımı otomatikleştirir.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine mimarisi" alt="KAITO RAGEngine mimarisi">
</div>

Yukarıdaki şekil Kaito mimarisinin genel görünümünü gösterir. Başlıca bileşenleri şunlardan oluşur:

- **Workspace denetleyicisi**: `workspace` özel kaynağını uzlaştırır, düğüm otomatik sağlama tetiklemek için `machine` (aşağıda açıklanmıştır) özel kaynakları oluşturur ve model ön ayarlı yapılandırmalarına göre çıkarım iş yükünü (`deployment` veya `statefulset`) oluşturur.
- **Düğüm sağlayıcı denetleyicisi**: Denetleyicinin adı [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) içinde *gpu-provisioner*'dir. Workspace denetleyicisi ile etkileşim kurmak için [Karpenter](https://sigs.k8s.io/karpenter) kökenli `machine` CRD'sini kullanır. AKS kümesine yeni GPU düğümleri eklemek için Azure Kubernetes Service (AKS) API'leri ile bütünleşir. 
> Not: The [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) is an open sourced component. It can be replaced by other controllers if they support [Karpenter-core](https://sigs.k8s.io/karpenter) APIs.

## Kurulum

Lütfen kurulum rehberine [buradan](https://github.com/Azure/kaito/blob/main/docs/installation.md) bakın.

## Phi-3 için Hızlı Başlangıç Çıkarımı
[Phi-3 Çıkarım Örnek Kodu](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Çıkış Ayarı ACR Yolu
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

Aşağıdaki komutu çalıştırarak workspace durumunu izleyebilirsiniz. WORKSPACEREADY sütunu `True` olduğunda model başarıyla dağıtılmış demektir.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Daha sonra çıkarım servisinin küme IP'sini bulup, hizmet uç noktasını test etmek için geçici bir `curl` pod'u kullanabilirsiniz.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Adaptörlerle Phi-3 için Hızlı Başlangıç

Kaito'yu kurduktan sonra, bir çıkarım servisini başlatmak için aşağıdaki komutları deneyebilirsiniz.

[Adaptörlü Phi-3 Çıkarım Örnek Kodu](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Çıkış ACR Yolu Ayarı
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

Aşağıdaki komutu çalıştırarak workspace durumunu izleyebilirsiniz. WORKSPACEREADY sütunu `True` olduğunda model başarıyla dağıtılmış demektir.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Daha sonra çıkarım servisinin küme IP'sini bulup, hizmet uç noktasını test etmek için geçici bir `curl` pod'u kullanabilirsiniz.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Sorumluluk Reddi:
Bu belge, yapay zeka çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstermemize rağmen, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilindeki metin yetkili kaynak olarak kabul edilmelidir. Önemli bilgiler için profesyonel bir çevirmenin yaptığı çeviri önerilir. Bu çevirinin kullanımı nedeniyle oluşabilecek herhangi bir yanlış anlaşılma veya yanlış yorumlamadan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->