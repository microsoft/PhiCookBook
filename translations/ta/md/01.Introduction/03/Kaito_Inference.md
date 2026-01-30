## Kaito உடன் முடிவெடுப்பு

[Kaito](https://github.com/Azure/kaito) என்பது Kubernetes குழாயில் AI/ML முடிவெடுப்பு மொற்சியை இயக்குவதை தானாகச் செய்யும் ஓர் آپரேட்டர் ஆகும்.

Kaito இல் பாரம்பரியமாக உள்ள பெரும்பாலான மொடல் இயக்கல் முறைகளுடன் ஒப்பிடுகையில் பின்வரும் முக்கிய வேறுபாடுகள் உள்ளன:

- மாதிரிப் கோப்புகளை கன்டெய்னர் படங்களாக நிர்வகிக்கும். மாதிரி நூலகத்தைப் பயன்படுத்தி முடிவெடுப்பு அழைப்புகளைச் செய்ய ஒரு http சேவையகத்தை வழங்குகிறது.
- GPU ஹார்ட்வேர் பொருத்தப்பட்டு இயக்க விதிகளை ஒழுங்குபடுத்துவதற்கு தேவையில்லை; அதற்கான முன் வரையறுக்கப்பட்ட அமைப்புகளை வழங்குகிறது.
- மாதிரி தேவைகளின் அடிப்படையில் GPU நோட்களை தானாகக் கொள்கிறது.
- உரிமம் அங்கீகரித்திருந்தால் பெரிய மாதிரி படங்களை பொதுப் பயன்படுத்த Microsoft Container Registry (MCR) இல் வைக்கிறது.

Kaito ஐப் பயன்படுத்தி, Kubernetes இல் பெரிய AI முடிவெடுப்பு மொடல்களை இயக்கும் பணிகள் பெரிதும் எளிமையாக்கப்படுகின்றன.


## கட்டமைப்பு

Kaito பாரம்பரிய Kubernetes Custom Resource Definition(CRD)/controller வடிவமைப்பு முறையை பின்பற்றுகிறது. பயனர் `workspace` என்ற தனித்துவ கூட்டு வளத்தை நிர்வகிக்கிறார், இது GPU தேவைகள் மற்றும் முடிவெடுப்பு விவரக்குறிப்புகளை காட்டுகிறது. Kaito controllers `workspace` தனித்துவ வளத்தை ஒத்திசைத்தல் மூலம் இயக்கலை தானாகச் செய்கின்றன.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architecture" alt="KAITO RAGEngine architecture">
</div>

மேலுள்ள படத்தில் Kaito கட்டமைப்பு காட்சி தரப்பட்டுள்ளது. அதன் முக்கிய அங்கங்கள்:

- **Workspace controller**: இது `workspace` தனித்துவ வளத்தை ஒத்திசைக்கிறது, நோட் தானாக ஒதுக்க ரீதியில் `machine` (தெளிவுபடுத்தப்பட்டுள்ளது கீழே) தனித்துவ வளங்களை உருவாக்குகிறது, மற்றும் மாதிரி முன் வரையறுக்கப்பட்ட அமைப்புகளின் அடிப்படையில் முடிவெடுப்பு பணிகளை (`deployment` அல்லது `statefulset`) உருவாக்குகிறது.
- **Node provisioner controller**: இந்த controller இன் பெயர் [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) இல் *gpu-provisioner* ஆகும். இது [Karpenter](https://sigs.k8s.io/karpenter) மூலம் உருவான `machine` CRD இனை workspace controller உடன் தொடர்புகொண்டு பயன்படுத்துகிறது. Azure Kubernetes Service(AKS) APIs உடன் இணைந்து AKS குழாயில் புதிய GPU நோடுகளை சேர்க்கிறது. 
> குறிப்பு: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) என்பது ஒரு திறந்த மூலக் கூறு ஆகும். அது [Karpenter-core](https://sigs.k8s.io/karpenter) APIs ஐ ஆதரிக்கும் பிற controllers மூலம் மாற்றப்பட வாய்ப்பு உள்ளது.

## நிறுவல்

நிறுவல் வழிகாட்டுதல்களை [இங்கே](https://github.com/Azure/kaito/blob/main/docs/installation.md) பார்க்கவும்.

## விரைவு தொடக்கம் Inference Phi-3
[மாதிரி குறியீடு Inference Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # வெளியீடு ACR பாதையை தொகுத்தல்
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

பின்வரும் கட்டளையை இயக்கி workspace நிலையை கண்காணிக்கலாம். WORKSPACEREADY பத்தி `True` ஆகும்போது மாதிரி வெற்றிகரமாக இயக்கப்பட்டுள்ளது.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

அடுத்து, முடிவெடுப்பு சேவையின் கிளஸ்டர் ஐபியை கண்டுபிடித்து கிளஸ்டரில் சேவை இடத்தை சோதிக்க ஒரு தற்காலிக `curl` போட் பயன்படுத்தலாம்.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## விரைவு தொடக்கம் Inference Phi-3 மூலம் அடாப்டர்கள்

Kaito ஐ நிறுவியபின், கீழ்காணும் கட்டளைகளை முயற்சி செய்து முடிவெடுப்பு சேவையை தொடங்கலாம்.

[மாதிரி குறியீடு Inference Phi-3 அடாப்டர்களுடன்](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # பீர்க்கும் வெளியீடு ACR பாதை
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

பின்வரும் கட்டளையை இயக்கி workspace நிலையை கண்காணிக்கலாம். WORKSPACEREADY பத்தி `True` ஆகும்போது மாதிரி வெற்றிகரமாக இயக்கப்பட்டுள்ளது.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

அடுத்து, முடிவெடுப்பு சேவையின் கிளஸ்டர் ஐபியை கண்டுபிடித்து கிளஸ்டரில் சேவை இடத்தை சோதிக்க ஒரு தற்காலிக `curl` போட் பயன்படுத்தலாம்.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**தயாரிப்பு அறிவிப்பு**:
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) எனும் செயற்கை நுண்ணறிவு மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. துல்லியத்தைப் பின்பற்ற முயற்சித்தாலும், தானாக மொழிபெயர்ப்பு செய்யப்படும் போது பிழைகள் அல்லது தவறுகள் இருக்க வாய்ப்பு உள்ளது என்பதைக் கவனத்தில் கொள்ளவும். அதன் மூலம், அசல் ஆவணம் அதன் சொந்த மொழியில் அதிகாரபூர்வமான மூலமாக கருதப்பட வேண்டும். முக்கியமான தகவலுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பின் பயன்பாட்டினால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறாய்வுகளுக்கும் நாங்கள் பொறுப்பல்ல.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->