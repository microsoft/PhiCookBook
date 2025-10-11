<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-10-11T12:21:09+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "ta"
}
-->
## Kaito மூலம் முடிவுகளை பெறுதல்

[Kaito](https://github.com/Azure/kaito) என்பது Kubernetes களத்தில் AI/ML முடிவு மாடல் பிரயோகத்தை தானியங்கமாக்கும் ஒரு ஆபரேட்டர் ஆகும்.

Kaito, பெரும்பாலான வழக்கமான மாடல் பிரயோக முறைகளுடன் ஒப்பிடும்போது, பின்வரும் முக்கிய வேறுபாடுகளை கொண்டுள்ளது:

- மாடல் கோப்புகளை கெண்டைனர் படங்களைக் கொண்டு நிர்வகிக்கிறது. மாடல் நூலகத்தைப் பயன்படுத்தி முடிவு அழைப்புகளைச் செய்ய ஒரு HTTP சர்வர் வழங்கப்படுகிறது.
- GPU ஹார்ட்வேருக்கு பொருந்த deployment அளவுருக்களை சரிசெய்வதை தவிர்க்க, முன்பே அமைக்கப்பட்ட கட்டமைப்புகளை வழங்குகிறது.
- மாடல் தேவைகளின் அடிப்படையில் GPU node-களை தானாக வழங்குகிறது.
- உரிமம் அனுமதித்தால், Microsoft Container Registry (MCR)-ல் பெரிய மாடல் படங்களை ஹோஸ்ட் செய்கிறது.

Kaito-வைப் பயன்படுத்தி, Kubernetes-ல் பெரிய AI முடிவு மாடல்களை சேர்க்கும் பணிகள் மிகவும் எளிமையாகின்றன.

## கட்டமைப்பு

Kaito, பாரம்பரிய Kubernetes Custom Resource Definition(CRD)/controller வடிவமைப்பு முறையைப் பின்பற்றுகிறது. பயனர் GPU தேவைகள் மற்றும் முடிவு விவரங்களை விவரிக்கும் `workspace` custom resource-ஐ நிர்வகிக்கிறார். Kaito controllers, `workspace` custom resource-ஐ reconcile செய்து deployment-ஐ தானியங்கமாக்கும்.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

மேலே உள்ள படத்தில் Kaito கட்டமைப்பின் மேற்பார்வை கொடுக்கப்பட்டுள்ளது. அதன் முக்கிய கூறுகள்:

- **Workspace controller**: இது `workspace` custom resource-ஐ reconcile செய்கிறது, node auto provisioning-ஐ தொடங்க `machine` (கீழே விளக்கப்பட்டுள்ளது) custom resources-ஐ உருவாக்குகிறது, மற்றும் மாடல் முன்பே அமைக்கப்பட்ட கட்டமைப்புகளின் அடிப்படையில் முடிவு வேலைப்பாடுகளை (`deployment` அல்லது `statefulset`) உருவாக்குகிறது.
- **Node provisioner controller**: இந்த controller-ஐ [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner)-ல் *gpu-provisioner* என்று அழைக்கப்படுகிறது. இது [Karpenter](https://sigs.k8s.io/karpenter) மூலம் உருவாக்கப்பட்ட `machine` CRD-ஐ பயன்படுத்தி workspace controller-ஐ தொடர்பு கொள்ளுகிறது. இது Azure Kubernetes Service(AKS) API-களுடன் ஒருங்கிணைந்து AKS களத்தில் புதிய GPU node-களைச் சேர்க்கிறது.
> குறிப்பு: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ஒரு திறந்த மூல கூறமாகும். [Karpenter-core](https://sigs.k8s.io/karpenter) API-களை ஆதரிக்கும் பிற controllers-ஆல் இதை மாற்றலாம்.

## நிறுவல்

நிறுவல் வழிகாட்டுதல்களை [இங்கே](https://github.com/Azure/kaito/blob/main/docs/installation.md) பார்க்கவும்.

## Phi-3 முடிவுகளை விரைவாக தொடங்குதல்
[Phi-3 முடிவு மாதிரி குறியீடு](https://github.com/Azure/kaito/tree/main/examples/inference)

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

`WORKSPACEREADY` பத்தி `True` ஆக மாறும்போது, மாடல் வெற்றிகரமாக deploy செய்யப்பட்டுள்ளது என்பதை பின்வரும் கட்டளையை இயக்கி workspace நிலையை கண்காணிக்கலாம்.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

அடுத்ததாக, முடிவு சேவையின் cluster ip-ஐ கண்டறிந்து, cluster-ல் சேவை முடுக்கத்தை சோதிக்க ஒரு தற்காலிக `curl` pod-ஐ பயன்படுத்தலாம்.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Adapters உடன் Phi-3 முடிவுகளை விரைவாக தொடங்குதல்

Kaito-ஐ நிறுவிய பிறகு, முடிவு சேவையை தொடங்க பின்வரும் கட்டளைகளை முயற்சிக்கலாம்.

[Adapters உடன் Phi-3 முடிவு மாதிரி குறியீடு](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

`WORKSPACEREADY` பத்தி `True` ஆக மாறும்போது, மாடல் வெற்றிகரமாக deploy செய்யப்பட்டுள்ளது என்பதை பின்வரும் கட்டளையை இயக்கி workspace நிலையை கண்காணிக்கலாம்.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

அடுத்ததாக, முடிவு சேவையின் cluster ip-ஐ கண்டறிந்து, cluster-ல் சேவை முடுக்கத்தை சோதிக்க ஒரு தற்காலிக `curl` pod-ஐ பயன்படுத்தலாம்.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளுங்கள். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.