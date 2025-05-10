<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-05-09T20:43:41+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "sl"
}
-->
## Kaito සමඟ සුමට-සැකසුම්

[Kaito](https://github.com/Azure/kaito) යනු Kubernetes කුලකයක AI/ML අනාවරණ මාදිලි යොදා ගැනීම ස්වයංක්‍රීය කරන මෙහෙයුම්කරුකි.

Kaito සම්භන්ධයෙන් බොහෝ ප්‍රචලිත මාදිලි යොදා ගැනීමේ ක්‍රමවේද වලට වඩා විශේෂාංග කිහිපයක් ඇත:

- මාදිලි ගොනු container රූප භාවිතයෙන් කළමනාකරණය කරයි. මාදිලි පුස්තකාලය භාවිතා කර අනාවරණ ඇමතුම් සිදු කිරීමට http සේවාදායකයක් ලබා දේ.
- GPU දෘඩාංගයට ගැලපෙන පරිදි යොදාගත යුතු deployment පරාමිතීන් සකස් කිරීමෙන් වළකියි, පෙරනිමි සැකසුම් ලබාදීමෙන්.
- මාදිලියට අනුව GPU නෝඩ් ස්වයංක්‍රීයව සැපයීම සිදු කරයි.
- බලපත්‍රය ඉඩ දෙන්නේ නම් විශාල මාදිලි රූප Microsoft Container Registry (MCR) පොදු සේවාදායකයේ අරන් තබයි.

Kaito භාවිතා කිරීමෙන් Kubernetes තුළ විශාල AI අනාවරණ මාදිලි එකතු කිරීමේ වැඩ흐ම විශාල ලෙස සරල කරයි.


## ව්‍යුහය

Kaito සම්ප්‍රදායික Kubernetes Custom Resource Definition(CRD)/controller සැලැස්ම අනුගමනය කරයි. පරිශීලකයා GPU අවශ්‍යතා සහ අනාවරණ විස්තරය විස්තර කරන `workspace` custom resource එකක් කළමනාකරණය කරයි. Kaito controllers එම `workspace` custom resource එක සමඟ අනුකූලව deployment ස්වයංක්‍රීය කරයි.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

ඉහත රූපය Kaito ව්‍යුහය සාරාංශය පෙන්වයි. එහි ප්‍රධාන කොටස් පහත පරිදි වේ:

- **Workspace controller**: `workspace` custom resource එක සමඟ අනුකූලව කටයුතු කරයි, නෝඩ් ස්වයං සැපයුමක් ආරම්භ කිරීම සඳහා `machine` (පහත විස්තර කර ඇත) custom resources නිර්මාණය කරයි, සහ මාදිලි පෙරනිමි සැකසුම් අනුව අනාවරණ වැඩබැරිම (`deployment` හෝ `statefulset`) නිර්මාණය කරයි.
- **Node provisioner controller**: මෙහි නම *gpu-provisioner* ලෙස [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) තුළ හැඳින්වේ. එය [Karpenter](https://sigs.k8s.io/karpenter) සිට ආරම්භ වූ `machine` CRD භාවිතා කර workspace controller සමඟ සම්බන්ධ වේ. Azure Kubernetes Service(AKS) APIs සමඟ ඒකාබද්ධ වී AKS කුලකයට නව GPU නෝඩ් එකතු කරයි.
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) යනු විවෘත මූලාශ්‍ර කොටසකි. එය [Karpenter-core](https://sigs.k8s.io/karpenter) APIs සහාය දක්වන වෙනත් controllers වලින් හුවමාරු කළ හැක.

## සාරාංශ වීඩියෝව  
[Kaito ප්‍රදර්ශනය බලන්න](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)
## ස්ථාපනය

ස්ථාපන මාර්ගෝපදේශය [මෙතනින්](https://github.com/Azure/kaito/blob/main/docs/installation.md) පරීක්ෂා කරන්න.

## ඉක්මන් ආරම්භය

Kaito ස්ථාපනය කිරීමෙන් පසු, සුමට-සැකසුම් සේවාවක් ආරම්භ කිරීමට පහත විධාන අනුගමනය කළ හැක.

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

Workspace තත්ත්වය පහත විධානය ධාවනය කරමින් පරික්ෂා කළ හැක. WORKSPACEREADY තීරුව `True` බවට පත්වුනොත්, මාදිලිය සාර්ථකව යොදාගෙන ඇත.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

ඊළඟට, අනාවරණ සේවාවේ cluster ip හොයාගෙන cluster තුළ කාලික `curl` pod එකක් භාවිතා කර සේවා අවසන් ලක්ෂ්‍යය පරීක්ෂා කළ හැක.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Izjava o omejitvi odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvorni jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Ne odgovarjamo za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.