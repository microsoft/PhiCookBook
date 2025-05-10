<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-05-09T20:40:26+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "tr"
}
-->
## Kaito ile İnce Ayar

[Kaito](https://github.com/Azure/kaito), Kubernetes kümesinde AI/ML çıkarım modeli dağıtımını otomatikleştiren bir operatördür.

Kaito, sanal makine altyapıları üzerine kurulu yaygın model dağıtım yöntemlerine kıyasla aşağıdaki temel farklılıklara sahiptir:

- Model dosyalarını konteyner imajları kullanarak yönetir. Model kütüphanesi üzerinden çıkarım çağrıları yapmak için bir http sunucusu sağlar.
- Önceden ayarlanmış konfigürasyonlar sunarak GPU donanımına uyacak şekilde dağıtım parametrelerini ayarlamaktan kaçınır.
- Model gereksinimlerine göre GPU düğümlerini otomatik sağlar.
- Lisans izin veriyorsa büyük model imajlarını halka açık Microsoft Container Registry (MCR) üzerinde barındırır.

Kaito kullanarak, Kubernetes'te büyük AI çıkarım modellerinin entegrasyon süreci büyük ölçüde basitleşir.

## Mimari

Kaito, klasik Kubernetes Özel Kaynak Tanımı (CRD)/kontrolör tasarım desenini takip eder. Kullanıcı, GPU gereksinimlerini ve çıkarım spesifikasyonunu tanımlayan `workspace` özel kaynağını yönetir. Kaito kontrolörleri, `workspace` özel kaynağını dengeleyerek dağıtımı otomatikleştirir.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Yukarıdaki şekil, Kaito mimarisinin genel görünümünü sunar. Ana bileşenleri şunlardır:

- **Workspace kontrolörü**: `workspace` özel kaynağını dengeler, düğüm otomatik sağlama tetiklemek için aşağıda açıklanan `machine` özel kaynaklarını oluşturur ve model ön ayar konfigürasyonlarına göre çıkarım iş yükünü (`deployment` veya `statefulset`) yaratır.
- **Node provisioner kontrolörü**: Kontrolörün adı [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) içinde *gpu-provisioner* olarak geçer. [Karpenter](https://sigs.k8s.io/karpenter) kaynaklı `machine` CRD'sini kullanarak workspace kontrolörü ile etkileşime girer. Azure Kubernetes Service (AKS) API'leri ile entegre olarak AKS kümesine yeni GPU düğümleri ekler.
> Not: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) açık kaynaklı bir bileşendir. Eğer destekliyorsa, diğer kontrolörlerle [Karpenter-core](https://sigs.k8s.io/karpenter) API'leri üzerinden değiştirilebilir.

## Genel Bakış Videosu  
[Kaito Demo'sunu İzle](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Kurulum

Kurulum rehberine [buradan](https://github.com/Azure/kaito/blob/main/docs/installation.md) ulaşabilirsiniz.

## Hızlı Başlangıç

Kaito'yu kurduktan sonra, ince ayar servisini başlatmak için aşağıdaki komutları deneyebilirsiniz.

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

Workspace durumunu takip etmek için aşağıdaki komutu çalıştırabilirsiniz. WORKSPACEREADY sütunu `True` olduğunda model başarıyla dağıtılmış demektir.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Sonrasında, çıkarım servisinin küme IP'sini bulup, kümedeki geçici bir `curl` pod'u kullanarak servis uç noktasını test edebilirsiniz.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek herhangi bir yanlış anlama veya yanlış yorumlamadan sorumlu değiliz.