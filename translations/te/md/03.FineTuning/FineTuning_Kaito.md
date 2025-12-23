<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-12-21T18:39:57+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "te"
}
-->
## Kaito తో ఫైన్-ట్యూనింగ్ 

[Kaito](https://github.com/Azure/kaito) ఒక ఆపరేటర్, ఇది Kubernetes క్లస్టర్‌లో AI/ML ఇన్ఫరెన్స్ మోడల్‌ను డిప్లాయ్ చేయడాన్ని ఆటోమేట్ చేస్తుంది.

Kaito కి వర్చువల్ మెషీన్ ఇన్ఫ్రాస్ట్రక్చర్‌లపై నిర్మించిన చాలా ప్రధాన మోడల్ డిప్లాయ్‌మెంట్ పద్ధతులతో పోలిస్తే క్రింది ముఖ్యమైన భిన్నతలు ఉన్నాయి:

- కంటెయినర్ ఇమేజ్‌లను ఉపయోగించి మోడల్ ఫైళ్లను నిర్వహిస్తుంది. మోడల్ లైబ్రరీ ఉపయోగించి ఇన్ఫరెన్స్ కాల్స్ చేయడానికి ఒక http సర్వర్ అందించబడుతుంది.
- ప్రీసెట్ కాన్ఫిగరేషన్లను అందించడం ద్వారా GPU హార్డ్‌వేర్‌కు తగిన విధంగా డిప్లాయ్‌మెంట్ పారామీటర్లను ట్యూన్ చేయకుండా ఉంచుతుంది.
- మోడల్ అవసరాల ఆధారంగా GPU నోడ్లను ఆటో-ప్రొవిజన్ చేస్తుంది.
- లైసెన్స్ అనుమతిస్తే పెద్ద మోడల్ ఇమేజ్‌లను public Microsoft Container Registry (MCR) లో హోస్ట్ చేస్తుంది.

Kaito ఉపయోగించి, Kubernetes లో పెద్ద AI ఇన్ఫరెన్స్ మోడల్‌లను ఆన్‌బోర్డింగ్ చేసే పని ప్రవాహం ప్రధానంగా సరళంగా మారుతుంది。


## ఆర్కిటెక్చర్

Kaito సంప్రదాయ Kubernetes Custom Resource Definition(CRD)/controller డిజైన్ ప్యాటర్న్‌ను అనుసరిస్తుంది. వినియోగదారు GPU అవసరాలు మరియు ఇన్ఫరెన్స్ స్పెసిఫికేషన్‌ను వర్ణించే `workspace` కస్టమ్ రీసోర్స్‌ను నిర్వహిస్తారు. Kaito కంట్రోలర్లు `workspace` కస్టమ్ రీసోర్స్‌ను రీకన్సిల్ చేయడం ద్వారా డిప్లాయ్‌మెంట్‌ను ఆటోమేట్ చేస్తాయి.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito ఆర్కిటెక్చర్" alt="Kaito ఆర్కిటెక్చర్">
</div>

పై చిత్రం Kaito ఆర్కిటెక్చర్ అవలోకనాన్ని చూపిస్తుంది. దీని ప్రధాన భాగాలు ఈ విధంగా ఉన్నాయి:

- **Workspace controller**: ఇది `workspace` కస్టమ్ రీసోర్స్‌ను రీకన్సిల్ చేస్తుంది, నోడ్ ఆటో ప్రోవిజనింగ్‌ను ట్రిగ్గర్ చేయడానికి `machine` (క్రింద వివరించబడింది) కస్టమ్ రీసోర్స్‌లను సృష్టిస్తుంది, మరియు మోడల్ ప్రీసెట్ కాన్ఫిగరేషన్ల ఆధారంగా ఇన్ఫరెన్స్ వర్క్లోడ్ (`deployment` లేదా `statefulset`) ను సృష్టిస్తుంది.
- **Node provisioner controller**: The controller's name is *gpu-provisioner* in [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). It uses the `machine` CRD originated from [Karpenter](https://sigs.k8s.io/karpenter) to interact with the workspace controller. It integrates with Azure Kubernetes Service(AKS) APIs to add new GPU nodes to the AKS cluster. 
> గమనిక: The [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) is an open sourced component. It can be replaced by other controllers if they support [Karpenter-core](https://sigs.k8s.io/karpenter) APIs.

## అవలోకన వీడియో 
[Kaito డెమో చూడండి](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)
## ఇన్‌స్టాలేషన్

దయచేసి ఇన్‌స్టాలేషన్ గైడ్‌ను [ఇక్కడ](https://github.com/Azure/kaito/blob/main/docs/installation.md) చూడండి.

## త్వరిత ప్రారంభం

Kaito ఇన్‌స్టాల్ చేసిన తర్వాత, ఫైన్-ట్యూనింగ్ సేవ ప్రారంభించడానికి కింది ఆజ్ఞలు ప్రయత్నించవచ్చు.

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # ట్యూనింగ్ అవుట్పుట్ ACR మార్గం
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/fine-tuning/kaito_workspace_tuning_phi_3.yaml
```

The workspace status can be tracked by running the following command. When the WORKSPACEREADY column becomes `True`, the model has been deployed successfully.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Next, one can find the inference service's cluster ip and use a temporal `curl` pod to test the service endpoint in the cluster.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
బాధ్యతాప్రత్యామ్నాయం:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ద్వారా అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో తప్పులు లేదా లోపాలు ఉండొచ్చు అని దయచేసి గమనించండి. స్థానిక భాషలోని అసలు పత్రాన్ని అధికారిక మూలంగా పరిగణించాలి. కీలకమైన సమాచారానికి వృత్తిపరులైన మానవ అనువాదాన్ని సూచించబడుతుంది. ఈ అనువాదాన్ని ఉపయోగించడంతో ఏర్పడిన ఏవైనా భావాభిప్రాయాల భిన్నత్వాలు లేదా తప్పుదోవలకు మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->