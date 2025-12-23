<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-12-22T01:13:07+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "te"
}
-->
## Kaito ద్వారా ఇన్ఫరెన్స్ 

[Kaito](https://github.com/Azure/kaito) ఒక ఆపరేటర్, ఇది Kubernetes క్లస్టర్‌లో AI/ML ఇన్ఫరెన్స్ మోడల్ డిప్లాయ్‌మెంట్‌ను ఆటోమేట్ చేస్తుంది.

Kaitoకు వర్చువల్ మెషీన్ ఆధారిత ప్రధాన మోడల్ డిప్లాయ్‌మెంట్ పద్ధతులతో పోలిస్తే క్రింది ముఖ్య తేడాలు ఉన్నాయి:

- కంటైనర్ ఇమేజ్‌ల ద్వారా మోడల్ ఫైళ్లను నిర్వహిస్తుంది. మోడల్ లైబ్రరీ ఉపయోగించి ఇన్ఫరెన్స్ కాల్స్ నిర్వహించడానికి ఒక HTTP సర్వర్ అందించబడింది.
- ప్రీసెట్ కాన్ఫిగరేషన్లు అందించడం ద్వారా GPU హార్డ్వేర్‌కు సరిపడేలా డిప్లాయ్‌మెంట్ పారామీటర్లను ట్యూన్ చేయాల్సిన అవసరాన్ని తప్పిస్తుంది.
- మోడల్ అవసరాల ఆధారంగా GPU నోడ్‌లను ఆటో-ప్రొవిజన్ చేస్తుంది.
- లైసెన్స్ అనుమతిస్తే పెద్ద మోడల్ ఇమేజ్‌లను public Microsoft Container Registry (MCR)లో హోస్ట్ చేస్తుంది.

Kaito ఉపయోగించడం ద్వారా Kubernetesలో పెద్ద AI ఇన్ఫరెన్స్ మోడళ్లను ఆన్‌బోర్డింగ్ చేసే వర్క్‌ఫ్లో చాలా సులభతరం అవుతుంది。


## ఆర్కిటెక్చర్

Kaito సంప్రదాయ Kubernetes Custom Resource Definition(CRD)/controller డిజైన్ ప్యాటర్న్‌ను అనుసరిస్తుంది. యూజర్ GPU అవసరాలు మరియు ఇన్ఫరెన్స్ స్పెసిఫికేషన్‌ను వర్ణించే `workspace` custom resource ను నిర్వహిస్తారు. Kaito కంట్రోలర్లు `workspace` custom resource ను reconcile చేయడం ద్వారా డిప్లాయ్‌మెంట్‌ను ఆటోమేట్ చేస్తాయి.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito ఆర్కిటెక్చర్" alt="Kaito ఆర్కిటెక్చర్">
</div>

పై చిత్రం Kaito ఆర్కిటెక్చర్ అవలోకనాన్ని చూపిస్తుంది. దాని ప్రధాన భాగాలు క్రింది విధంగా ఉన్నాయి:

- **Workspace controller**: ఇది `workspace` custom resource ను reconcile చేస్తుంది, నోడ్ ఆటో ప్రొవిజనింగ్‌ను ట్రిగ్గర్ చేయడానికి `machine` (explained below) custom resources ను సృష్టిస్తుంది, మరియు మోడల్ ప్రీసెట్ కాన్ఫిగరేషన్ల ఆధారంగా ఇన్ఫరెన్స్ వర్క్‌లోడ్‌ను (`deployment` లేదా `statefulset`) సృష్టిస్తుంది.
- **Node provisioner controller**: ఈ కంట్రోలర్ పేరు [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) లో *gpu-provisioner* గా ఉంటుంది. ఇది workspace controller తో పరస్పర చర్యకు [Karpenter](https://sigs.k8s.io/karpenter) నుండి ఉద్భవించిన `machine` CRD ను ఉపయోగిస్తుంది. ఇది Azure Kubernetes Service(AKS) APIs తో అనుసంధానం చేసి AKS క్లస్టర్‌కు కొత్త GPU నోడ్‌లను జోడిస్తుంది. 
> గమనిక: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ఒక ఓపెన్ సోర్స్ కంపోనెంట్. ఇది [Karpenter-core](https://sigs.k8s.io/karpenter) APIs ను మద్దతు ఇస్తే ఇతర కంట్రోలర్లతో బదిలీ చేయవచ్చు.

## ఇన్‌స్టాలేషన్

దయచేసి ఇన్‌స్టాలేషన్ మార్గదర్శకత్వాన్ని [ఇక్కడ](https://github.com/Azure/kaito/blob/main/docs/installation.md) చూడండి.

## త్వరిత ప్రారంభం — Phi-3 ఇన్ఫరెన్స్
[నమూనా కోడ్ Phi-3 ఇన్ఫరెన్స్](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # అవుట్‌పుట్ ACR మార్గాన్ని సర్దుబాటు చేయడం
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

workspace స్థితిని క్రింది కమాండ్ 실행 చేయడం ద్వారా ట్రాక్ చేయవచ్చు. WORKSPACEREADY కాలమ్ `True` అవగానే, మోడల్ విజయవంతంగా డిప్లాయ్ చేయబడింది.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

తదుపరి, ఇన్ఫరెన్స్ సర్వీస్ యొక్క క్లస్టర్ IP కనుగొని క్లస్టర్‌లో సర్వీస్ ఎండ్‌పాయింట్‌ను పరీక్షించడానికి తాత్కాలిక `curl` పోడ్ ఉపయోగించవచ్చు.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## త్వరిత ప్రారంభం — Phi-3 ఇన్ఫరెన్స్ అడాప్టర్లతో

Kaito ఇన్‌స్టాల్ చేసిన తర్వాత, ఇన్ఫరెన్స్ సర్వీస్ ప్రారంభించడానికి క్రింది కమాండ్స్ ప్రయత్నించవచ్చు.

[నమూనా కోడ్ Phi-3 ఇన్ఫరెన్స్ అడాప్టర్లతో](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # ట్యూనింగ్ అవుట్‌పుట్ ACR మార్గం
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

workspace స్థితిని క్రింది కమాండ్ 실행 చేయడం ద్వారా ట్రాక్ చేయవచ్చు. WORKSPACEREADY కాలమ్ `True` అవగానే, మోడల్ విజయవంతంగా డిప్లాయ్ చేయబడింది.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

తదుపరి, ఇన్ఫరెన్స్ సర్వీస్ యొక్క క్లస్టర్ IP కనుగొని క్లస్టర్‌లో సర్వీస్ ఎండ్‌పాయింట్‌ను పరీక్షించడానికి తాత్కాలిక `curl` పోడ్ ఉపయోగించవచ్చు.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
నిరాకరణ (Disclaimer):
ఈ డాక్యుమెంట్‌ను AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించారు. మేము ఖచ్చితత్వానికి శ్రమిస్తున్నప్పటికీ, స్వయంచాలక అనువాదాలలో పొరపాట్లు లేదా అపరిపక్వతలు ఉండవచ్చని దయచేసి గుర్తుంచుకోండి. స్థానిక భాషలోని అసలు డాక్యుమెంట్‌ను అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి వృత్తిపరమైన మానవ అనువాదం చేయించుకోవాలని సూచించబడుతుంది. ఈ అనువాదం వలన జరిగే ఏవైనా అవగాహనా లోపాలు లేదా తప్పుగా అర్థం చేసుకోవడంపై మేము బాధ్యులు కాదేమో అని తెలియజేస్తున్నాము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->