## Kaito ile İnce Ayar

[Kaito](https://github.com/Azure/kaito), Kubernetes kümesinde AI/ML çıkarım modeli dağıtımını otomatikleştiren bir operatördür.

Kaito, sanal makine altyapıları üzerine kurulu çoğu yaygın model dağıtım yöntemine kıyasla şu önemli farklara sahiptir:

- Model dosyalarını konteyner imajlarıyla yönetir. Model kütüphanesini kullanarak çıkarım çağrıları yapmak için bir http sunucusu sağlar.
- GPU donanımına uyacak şekilde dağıtım parametrelerini ayarlama ihtiyacını önlemek için önceden tanımlanmış yapılandırmalar sunar.
- Model gereksinimlerine göre GPU düğümlerini otomatik olarak sağlar.
- Lisans izin veriyorsa, büyük model imajlarını Microsoft Container Registry (MCR) üzerinde barındırır.

Kaito kullanarak, Kubernetes'te büyük AI çıkarım modellerinin entegrasyon süreci büyük ölçüde basitleşir.

## Mimari

Kaito, klasik Kubernetes Custom Resource Definition (CRD)/controller tasarım desenini takip eder. Kullanıcı, GPU gereksinimlerini ve çıkarım spesifikasyonunu tanımlayan bir `workspace` özel kaynağını yönetir. Kaito controller'ları, `workspace` özel kaynağını uzlaştırarak dağıtımı otomatikleştirir.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito mimarisi" alt="Kaito mimarisi">
</div>

Yukarıdaki şekil, Kaito mimarisinin genel görünümünü sunar. Ana bileşenleri şunlardır:

- **Workspace controller**: `workspace` özel kaynağını uzlaştırır, düğüm otomatik sağlama tetiklemek için `machine` (aşağıda açıklanmıştır) özel kaynakları oluşturur ve model ön ayar yapılandırmalarına göre çıkarım iş yükünü (`deployment` veya `statefulset`) oluşturur.
- **Node provisioner controller**: Controller, [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) içinde *gpu-provisioner* olarak adlandırılır. Workspace controller ile etkileşim için [Karpenter](https://sigs.k8s.io/karpenter) kökenli `machine` CRD'sini kullanır. Azure Kubernetes Service (AKS) API'leri ile entegre olarak AKS kümesine yeni GPU düğümleri ekler.
> Not: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) açık kaynaklı bir bileşendir. [Karpenter-core](https://sigs.k8s.io/karpenter) API'lerini destekleyen diğer controller'larla değiştirilebilir.

## Genel Bakış Videosu  
[Kaito Demo'sunu İzle](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Kurulum

Kurulum rehberine [buradan](https://github.com/Azure/kaito/blob/main/docs/installation.md) ulaşabilirsiniz.

## Hızlı Başlangıç

Kaito kurulduktan sonra, ince ayar servisini başlatmak için aşağıdaki komutlar denenebilir.

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

Workspace durumu aşağıdaki komutla takip edilebilir. WORKSPACEREADY sütunu `True` olduğunda, model başarıyla dağıtılmış demektir.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Sonrasında, çıkarım servisinin küme IP'si bulunabilir ve geçici bir `curl` pod'u kullanılarak küme içindeki servis uç noktası test edilebilir.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.