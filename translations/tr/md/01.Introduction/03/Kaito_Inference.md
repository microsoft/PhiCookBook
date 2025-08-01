<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-07-16T20:50:28+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "tr"
}
-->
## Kaito ile Çıkarım

[Kaito](https://github.com/Azure/kaito), Kubernetes kümesinde AI/ML çıkarım modeli dağıtımını otomatikleştiren bir operatördür.

Kaito, sanal makine altyapıları üzerine kurulu çoğu yaygın model dağıtım yöntemine kıyasla şu önemli farklara sahiptir:

- Model dosyalarını konteyner imajları kullanarak yönetir. Model kütüphanesi üzerinden çıkarım çağrıları yapmak için bir http sunucusu sağlar.
- GPU donanımına uyacak şekilde dağıtım parametrelerini ayarlamaktan kaçınmak için önceden tanımlanmış yapılandırmalar sunar.
- Model gereksinimlerine göre GPU düğümlerini otomatik olarak sağlar.
- Lisans izin veriyorsa, büyük model imajlarını Microsoft Container Registry (MCR) üzerinde barındırır.

Kaito kullanarak, Kubernetes'te büyük AI çıkarım modellerinin entegrasyon iş akışı büyük ölçüde basitleşir.

## Mimari

Kaito, klasik Kubernetes Custom Resource Definition (CRD)/controller tasarım desenini takip eder. Kullanıcı, GPU gereksinimlerini ve çıkarım spesifikasyonunu tanımlayan bir `workspace` özel kaynağını yönetir. Kaito controller'ları, `workspace` özel kaynağını uzlaştırarak dağıtımı otomatikleştirir.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito mimarisi" alt="Kaito mimarisi">
</div>

Yukarıdaki şekil, Kaito mimarisinin genel görünümünü sunar. Ana bileşenleri şunlardır:

- **Workspace controller**: `workspace` özel kaynağını uzlaştırır, düğüm otomatik sağlama tetiklemek için `machine` (aşağıda açıklanmıştır) özel kaynakları oluşturur ve model ön ayar yapılandırmalarına göre çıkarım iş yükünü (`deployment` veya `statefulset`) oluşturur.
- **Node provisioner controller**: Controller'ın adı [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) içinde *gpu-provisioner* olarak geçer. [Karpenter](https://sigs.k8s.io/karpenter) kaynaklı `machine` CRD'sini kullanarak workspace controller ile etkileşime girer. Azure Kubernetes Service (AKS) API'leri ile entegre olarak AKS kümesine yeni GPU düğümleri ekler.
> Not: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) açık kaynaklı bir bileşendir. Eğer destekliyorsa, [Karpenter-core](https://sigs.k8s.io/karpenter) API'lerini kullanan diğer controller'larla değiştirilebilir.

## Kurulum

Kurulum rehberine [buradan](https://github.com/Azure/kaito/blob/main/docs/installation.md) ulaşabilirsiniz.

## Hızlı Başlangıç Çıkarım Phi-3
[Örnek Kod Çıkarım Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

Workspace durumunu aşağıdaki komutla takip edebilirsiniz. WORKSPACEREADY sütunu `True` olduğunda, model başarıyla dağıtılmış demektir.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Sonrasında, çıkarım servisinin küme IP'si bulunabilir ve geçici bir `curl` pod'u kullanılarak küme içindeki servis uç noktası test edilebilir.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Adaptörlerle Hızlı Başlangıç Çıkarım Phi-3

Kaito kurulduktan sonra, çıkarım servisini başlatmak için aşağıdaki komutlar denenebilir.

[Örnek Kod Adaptörlü Çıkarım Phi-3](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

Workspace durumunu aşağıdaki komutla takip edebilirsiniz. WORKSPACEREADY sütunu `True` olduğunda, model başarıyla dağıtılmış demektir.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Sonrasında, çıkarım servisinin küme IP'si bulunabilir ve geçici bir `curl` pod'u kullanılarak küme içindeki servis uç noktası test edilebilir.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.