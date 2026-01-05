<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aca91084bc440431571e00bf30d96ab8",
  "translation_date": "2026-01-05T15:00:05+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "te"
}
-->
## కైటోతో సూచన

[కైటో](https://github.com/Azure/kaito) అనేది Kubernetes క్లస్టర్‌లో AI/ML సూచన మోడల్ డిప్లాయ్‌మెంట్‌ను ఆటోమేట్ చేసే ఆపరేటర్.

వర్చువల్ మిషన్ ఇన్ఫ్రాస్ట్రక్చర్‌లపై నిర్మితమైన ప్రధానధార మోడల్ డిప్లాయ్‌మెంట్ పద్ధతులతో పోల్చితే కైటోకు కింది ముఖ్య తేడాలు ఉన్నాయి:

- మోడల్ ఫైళ్లను కంటైనర్ ఇమేజెస్ ద్వారా నిర్వహించండి. మోడల్ లైబ్రరీ ఉపయోగించి సూచన కాల్స్ చేయడానికి ఒక http సర్వర్ అందించబడింది.
- GPU హార్డ్వేర్‌ను సరిపోల్చడానికి డిప్లాయ్‌మెంట్ పరామితులను ట్యూన్ చేయకుండా ప్రిసెట్ కాన్ఫిగరేషన్లను అందించడం.
- మోడల్ అవసరాల ఆధారంగా GPU నోడ్‌లను ఆటో ప్రావిజన్ చేయడం.
- లైసెన్సు అనుమతిస్తే, పెద్ద మోడల్ ఇమేజెస్‌ను పబ్లిక్ Microsoft కంటైనర్ రిజిస్ట్రీ (MCR)లో హోస్ట్ చేయండి.

కైటో ఉపయోగించి, Kubernetesలో పెద్ద AI సూచన మోడల్స్‌ను ఆన్‌బోర్డింగ్ చేసే వర్క్‌ఫ్లో చాలా సులభతరం అవుతుంది.

## సాంకేతిక వేళ

కైటో క్లాసిక్ Kubernetes కస్టమ్ రిసోర్స్ డిఫినిషన్(CRD)/కంట్రోలర్ డిజైన్ నమూనాను అనుసరిస్తుంది. యూజర్ GPU అవసరాలు మరియు సూచన స్పెసిఫికేషన్‌ను వివరించే `workspace` కస్టమ్ రిసోర్స్‌ను నిర్వహిస్తారు. కైటో కంట్రోలర్‌లు `workspace` కస్టమ్ రిసోర్స్‌ను రీకాంసిల్ చేసి డిప్లాయ్‌మెంట్‌ను ఆటోమేట్ చేస్తాయి.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architecture" alt="KAITO RAGEngine architecture">
</div>

పైన ఇచ్చిన ఫిగర్ కైటో ఆర్కిటెక్చర్ అవలోకనాన్ని చూపిస్తుంది. దాని ప్రధాన భాగాలు:

- **వర్క్‌స్పేస్ కంట్రోలర్**: ఇది `workspace` కస్టమ్ రిసోర్స్‌ను రీకాంసిల్ చేస్తుంది, నోడ్ ఆటో ప్రావిజనിംഗ് ప్రారంభించడానికి `machine` (క్రింది మూడు వివరించబడింది) కస్టమ్ రిసోర్స్‌లను సృష్టిస్తుంది మరియు మోడల్ ప్రిసెట్ కాన్ఫిగరేషన్ల ఆధారంగా సూచన వర్క్‌లోడ్ (`deployment` లేదా `statefulset`) సృష్టిస్తుంది.
- **నోడ్ ప్రావిజనర్ కంట్రోలర్**: కంట్రోలర్ పేరు [gpu-provisioner helm చార్ట్](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner)లో *gpu-provisioner*. ఇది [Karpenter](https://sigs.k8s.io/karpenter) నుండి వచ్చిన `machine` CRD ఉపయోగించి వర్క్‌స్పేస్ కంట్రోలర్‌తో ఇంటరాక్ట్ చేస్తుంది. Azure Kubernetes Service(AKS) APIs తో సమన్వయం చేసి AKS క్లస్టర్‌లో కొత్త GPU నోడ్‌లను జోడిస్తుంది.  
> గమనిక: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ఓపెన్ సోర్స్ కాంపోనెంట్. ఇది [Karpenter-core](https://sigs.k8s.io/karpenter) APIs మద్దతు ఉంటే ఇతర కంట్రోలర్‌లతో మార్చవచ్చు.

## ఇన్‌స్టాలేషన్

ఇన్‌స్టాలేషన్ గైడెన్స్ కోసం [ఇక్కడ](https://github.com/Azure/kaito/blob/main/docs/installation.md) చూడండి.

## త్వరిత ప్రారంభ సూచన Phi-3
[సాంపిల్ కోడ్ సూచన Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # అవుట్పుట్ ACR మార్గం ట్యూనింగ్ చేయడం
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

వర్క్‌స్పేస్ స్థితిని క్రింద ఇవ్వబడిన కమాండ్ ద్వారా ట్రాక్ చేయవచ్చు. WORKSPACEREADY కాలమ్ `True` అయితే, మోడల్ విజయవంతంగా డిప్లాయ్ అయింది.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

తర్వాత, సూచన సేవ యొక్క క్లస్టర్ IP కనుగొని క్లస్టర్‌లో సర్వీస్ ఎండ్‌పాయింట్‌ను పరీక్షించడానికి తాత్కాలిక `curl` పోడ్ ఉపయోగించవచ్చు.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## అడాప్టర్లతో త్వరిత ప్రారంభ సూచన Phi-3

కైటో ఇన్‌స్టాల్ చేసిన తరువాత, క్రింది కమాండ్లు ఉపయోగించి సూచన 서비스를 ప్రారంభించవచ్చు.

[అడాప్టర్లుతో సాంపిల్ కోడ్ సూచన Phi-3](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # అవుట్పుట్ ACR మార్గాన్ని ట్యూనింగ్ చేసుకుంటుంది
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

వర్క్‌స్పేస్ స్థితిని క్రింద చెప్పిన కమాండ్‌తో ట్రాక్ చేయవచ్చు. WORKSPACEREADY కాలమ్ `True` అయితే, మోడల్ విజయవంతంగా డిప్లాయ్ అయింది.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

తర్వాత, సూచన సేవ యొక్క క్లస్టర్ IP కనుగొని క్లస్టర్‌లో సర్వీస్ ఎండ్‌పాయింట్‌ను పరీక్షించడానికి తాత్కాలిక `curl` పోడ్‌ను ఉపయోగించవచ్చు.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:  
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువాదం చేయబడింది. మేము ఖచ్చితత్వానికి యత్నిస్తున్నప్పటికీ, యాంత్రిక అనువాదాల్లో తప్పులే లేదా అపరిశుద్ధతలు ఉండవచ్చు. అసలు పత్రం దాని స్థానిక భాషలోనే అధికారిక వనరు గా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫారసు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏదైనా తప్పుదోవ లేదా తప్పుదోవ తీసుకోవడంపై మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->