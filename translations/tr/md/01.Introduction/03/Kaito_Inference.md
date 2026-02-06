## Kaito ile Çıkarım

[Kaito](https://github.com/Azure/kaito), Kubernetes kümesinde AI/ML çıkarım modeli dağıtımını otomatikleştiren bir operatördür.

Kaito, sanal makine altyapıları üzerinde inşa edilmiş çoğu yaygın model dağıtım metodolojisine kıyasla şu önemli farklılıklara sahiptir:

- Model dosyalarını konteyner görüntüleri kullanarak yönetir. Model kütüphanesini kullanarak çıkarım çağrıları yapmak için bir http sunucusu sağlar.
- Ön ayarlı konfigürasyonlar sağlayarak GPU donanımına uyan dağıtım parametrelerini ayarlamaktan kaçınır.
- Model gereksinimlerine göre otomatik GPU düğümü sağlar.
- Lisans izin veriyorsa, büyük model görüntülerini Microsoft Container Registry (MCR) genel havuzunda barındırır.

Kaito kullanarak, Kubernetes'te büyük AI çıkarım modellerinin devreye alınma iş akışı büyük ölçüde basitleşir.

## Mimari

Kaito, klasik Kubernetes Özel Kaynak Tanımı (CRD)/kontrolcü tasarım desenini takip eder. Kullanıcı, GPU gereksinimlerini ve çıkarım spesifikasyonunu tanımlayan bir `workspace` özel kaynağını yönetir. Kaito kontrolcüleri `workspace` özel kaynağını sağlama yoluyla dağıtımı otomatikleştirir.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine mimarisi" alt="KAITO RAGEngine mimarisi">
</div>

Yukarıdaki şekil Kaito mimarisinin genel görünümünü sunmaktadır. Ana bileşenleri şunlardan oluşur:

- **Workspace kontrolcüsü**: `workspace` özel kaynağını sağlamakla görevli olup, düğüm otomatik sağlama tetiklemek için `machine` (aşağıda açıklanmıştır) özel kaynakları oluşturur ve model ön ayarlı konfigürasyonlarına göre çıkarım iş yükünü (`deployment` veya `statefulset`) oluşturur.
- **Düğüm sağlama kontrolcüsü**: Kontrolcünün adı [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) içinde *gpu-provisioner* olarak geçer. Bu kontrolcü, workspace kontrolcüsü ile etkileşmek için [Karpenter](https://sigs.k8s.io/karpenter) kökenli `machine` CRD'sini kullanır. Ayrıca Azure Kubernetes Service (AKS) API'leriyle entegre olur ve AKS kümesine yeni GPU düğümleri ekler.
> Not: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) açık kaynaklı bir bileşendir. Eğer diğer kontrolcüler [Karpenter-core](https://sigs.k8s.io/karpenter) API'lerini destekliyorsa, bu bileşenler ile değiştirilebilir.

## Kurulum

Kurulum rehberini lütfen [buradan](https://github.com/Azure/kaito/blob/main/docs/installation.md) kontrol edin.

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Çıktı ACR Yolunu Ayarlama
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

`workspace` durumunu aşağıdaki komutu çalıştırarak izleyebilirsiniz. WORKSPACEREADY sütunu `True` olduğunda, model başarıyla dağıtılmıştır.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Sonrasında, çıkarım servisinin küme IP'si bulunabilir ve küme içindeki bir geçici `curl` pod'u kullanılarak servis uç noktası test edilebilir.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Adaptörlerle Hızlı Başlangıç Çıkarım Phi-3

Kaito kurulduktan sonra, çıkarım servisini başlatmak için aşağıdaki komutlar denenebilir.

[Adaptörlü Örnek Kod Çıkarım Phi-3](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Çıkış ACR Yolunun Ayarlanması
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

`workspace` durumunu aşağıdaki komutu çalıştırarak izleyebilirsiniz. WORKSPACEREADY sütunu `True` olduğunda, model başarıyla dağıtılmıştır.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Sonrasında, çıkarım servisinin küme IP'si bulunabilir ve küme içindeki bir geçici `curl` pod'u kullanılarak servis uç noktası test edilebilir.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstermemize rağmen, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi diliyle yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum farklılıklarından sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->