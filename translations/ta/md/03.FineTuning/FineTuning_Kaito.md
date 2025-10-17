<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-10-11T11:39:43+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "ta"
}
-->
## Kaito மூலம் Fine-Tuning 

[Kaito](https://github.com/Azure/kaito) என்பது Kubernetes களத்தில் AI/ML inference மாடல் deployment ஐ தானியங்கி செய்யும் ஒரு operator ஆகும்.

Kaito, பொதுவாக virtual machine அடிப்படையிலான மாடல் deployment முறைகளுடன் ஒப்பிடும்போது, பின்வரும் முக்கிய வேறுபாடுகளை கொண்டுள்ளது:

- மாடல் கோப்புகளை container images மூலம் நிர்வகிக்கிறது. மாடல் நூலகத்தைப் பயன்படுத்தி inference calls செய்ய ஒரு http server வழங்கப்படுகிறது.
- GPU hardware-க்கு பொருந்த deployment அளவுருக்களை fine-tune செய்யாமல், முன்பதிவு செய்யப்பட்ட கட்டமைப்புகளை வழங்குகிறது.
- மாடல் தேவைகளின் அடிப்படையில் GPU nodes-ஐ தானாகவே வழங்குகிறது.
- உரிமம் அனுமதித்தால், Microsoft Container Registry (MCR)-ல் பெரிய மாடல் images-ஐ host செய்கிறது.

Kaito-ஐ பயன்படுத்தி, Kubernetes-ல் பெரிய AI inference மாடல்களை onboard செய்யும் வேலைப்பாடுகள் மிகவும் எளிமையாகின்றன.

## கட்டமைப்பு

Kaito, பாரம்பரிய Kubernetes Custom Resource Definition(CRD)/controller வடிவமைப்பு முறையை பின்பற்றுகிறது. பயனர் `workspace` custom resource-ஐ நிர்வகிக்கிறார், இது GPU தேவைகள் மற்றும் inference விவரக்குறிப்புகளை விவரிக்கிறது. Kaito controllers, `workspace` custom resource-ஐ சமநிலைப்படுத்துவதன் மூலம் deployment ஐ தானியங்கி செய்கிறது.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

மேலே உள்ள படத்தில் Kaito கட்டமைப்பின் மேற்பார்வை கொடுக்கப்பட்டுள்ளது. அதன் முக்கிய கூறுகள்:

- **Workspace controller**: இது `workspace` custom resource-ஐ சமநிலைப்படுத்துகிறது, node auto provisioning-ஐ தொடங்க `machine` (கீழே விளக்கப்பட்டுள்ளது) custom resources-ஐ உருவாக்குகிறது, மற்றும் மாடல் முன்பதிவு செய்யப்பட்ட கட்டமைப்புகளின் அடிப்படையில் inference workload (`deployment` அல்லது `statefulset`) உருவாக்குகிறது.
- **Node provisioner controller**: இந்த controller-ஐ [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) இல் *gpu-provisioner* என்று அழைக்கப்படுகிறது. இது [Karpenter](https://sigs.k8s.io/karpenter) மூலம் உருவாக்கப்பட்ட `machine` CRD-ஐ பயன்படுத்தி workspace controller உடன் தொடர்பு கொள்ளுகிறது. இது Azure Kubernetes Service(AKS) APIs உடன் ஒருங்கிணைந்து AKS களத்தில் புதிய GPU nodes-ஐ சேர்க்கிறது.
> குறிப்பு: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ஒரு open sourced கூறாகும். [Karpenter-core](https://sigs.k8s.io/karpenter) APIs-ஐ ஆதரிக்கும் பிற controllers-ஆல் இதை மாற்றலாம்.

## மேற்பார்வை வீடியோ 
[Kaito Demo-ஐ பார்க்க](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)
## நிறுவல்

நிறுவல் வழிகாட்டுதலுக்கான தகவல்களை [இங்கே](https://github.com/Azure/kaito/blob/main/docs/installation.md) பார்க்கவும்.

## விரைவான தொடக்கம்

Kaito-ஐ நிறுவிய பிறகு, fine-tuning சேவையை தொடங்க பின்வரும் கட்டளைகளை முயற்சிக்கலாம்.

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

Workspace நிலையை பின்வரும் கட்டளையை இயக்கி கண்காணிக்கலாம். WORKSPACEREADY பத்தி `True` ஆக மாறும்போது, மாடல் வெற்றிகரமாக deploy செய்யப்பட்டுள்ளது.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

அடுத்ததாக, inference சேவையின் cluster ip ஐ கண்டறிந்து, cluster இல் சேவை endpoint ஐ சோதிக்க ஒரு தற்காலிக `curl` pod ஐ பயன்படுத்தலாம்.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.