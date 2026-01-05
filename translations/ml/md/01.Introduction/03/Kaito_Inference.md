<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aca91084bc440431571e00bf30d96ab8",
  "translation_date": "2026-01-05T15:07:44+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "ml"
}
-->
## Kaito ഉപയോഗിച്ചുള്ള നിർണ്ണയം

[Kaito](https://github.com/Azure/kaito) ഒരു ഓപ്പറೇಟറാണ്, ഇത് Kubernetes ക്ലസ്റ്ററിൽ AI/ML നിർണ്ണയ മോഡൽ വിന്യാസം ഓട്ടോമേറ്റുചെയ്യുന്നു.

സാധാരണമേയുള്ള മിക്ക പ്രധാന മോഡൽ വിന്യാസ രീതി ഫെയർചെയ്യുന്ന വെർച്വൽ മെഷീൻ ഇൻ‌ഫ്രാസ്ട്രക്ചറുകളുടെ മുകളിൽ Kaito-യ്ക്ക് വമ്പിച്ച പ്രധാന വ്യത്യാസങ്ങൾ ഇപ്രകാരം:

- മോഡൽ ഫയലുകൾ കണ്ടെയ്‌നർ ഇമേജുകൾ ഉപയോഗിച്ച് മാനേജ് ചെയ്യും. മോഡൽ ലൈബ്രറി ഉപയോഗിച്ച് നിർണ്ണയ കോളുകൾ നടത്താൻ ഒരു HTTP സർവർ ലഭ്യമാണ്.
- GPU ഹാർഡ്‌വെയർ ഫിറ്റാക്കാൻ വിന്യാസ പരാമീറ്ററുകൾ ട്യൂൺ ചെയ്യേണ്ടതില്ല, മുൻസ്വീകൃത കോൺഫിഗറേഷനുകൾ നൽകുന്നു.
- മോഡൽ ആവശ്യകതകൾ അടിസ്ഥാനമാക്കി GPU നോഡുകൾ സ്വയം പ്രോവിഷൻ ചെയ്യുന്നു.
- ലൈസൻസ് അനുവദിച്ചാൽ, വലുത് മോഡൽ ഇമേജുകൾ പൊതു Microsoft Container Registry (MCR)-ൽ ഹോസ്റ്റ് ചെയ്യുന്നു.

Kaito ഉപയോഗിച്ച്, Kubernetes-ൽ വലുത് AI നിർണ്ണയ മോഡലുകളുടെ ഓൺബോർഡിംഗ് വർക്ക്‌ഫ്ലോ വളരെ ലളിതമാക്കുന്നു.


## ആർക്കിടെക്ചർ

Kaito പരമ്പരാഗത Kubernetes Custom Resource Definition (CRD)/controller രൂപരേഖ പിന്തുടരുന്നു. ഉപയോക്താവ് GPU ആവശ്യകതകളും നിർണ്ണയ നിർദ്ദേശങ്ങളും വിവരണ ചെയ്യുന്ന `workspace` കസ്റ്റം റിസോഴ്‌സ് മാനേജ് ചെയ്യുന്നു. Kaito контроллерുകൾ `workspace` കസ്റ്റം റിസോഴ്‌സ് റെക്കൺസൈൽ ചെയ്ത് വിന്യാസം ഓട്ടോമേറ്റുചെയ്യും.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architecture" alt="KAITO RAGEngine architecture">
</div>

മുകളിൽ കാണുന്ന ചിത്രം Kaito ആർക്കിടെക്ചർ അവലോകനമാണ്. പ്രധാന ഘടകങ്ങൾ:

- **Workspace controller**: `workspace` കസ്റ്റം റിസോഴ്‌സ് റെക്കൺസൈൽ ചെയ്യുന്നു, നോഡ് ഓട്ടോ പ്രോവിഷനിംഗ് ട്രിഗർ ചെയ്യാൻ `machine` (താഴെ വിശദീകരിക്കുന്നു) കസ്റ്റം റിസോഴ്‌സുകൾ സൃഷ്ടിക്കുന്നു, മോഡൽ മുൻസ്വീകൃത കോൺഫിഗറേഷനുകൾ അടിസ്ഥാനമാക്കി നിർണ്ണയ വർക്ക്‌ലോഡ് (`deployment` അല്ലെങ്കിൽ `statefulset`) തയാറാക്കുന്നു.
- **Node provisioner controller**: ഈ കൺട്രോളറിന്റെ പേര് [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) യിൽ *gpu-provisioner* ആണ്. ഇത് [Karpenter](https://sigs.k8s.io/karpenter) നിന്നുള്ള `machine` CRD ഉപയോഗിച്ച് workspace controller-ഉടൻ ഇടപെടുന്നു. Azure Kubernetes Service (AKS) APIകൾ ഉപയോഗിച്ച് AKS ക്ലസ്റ്ററിലേക്ക് പുതിയ GPU നോഡുകൾ ചേർക്കാൻ സഹായിക്കുന്നു. 
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ഒരു തുറന്ന സ്രോതസ്സ് ഘടകമാണ്. ഇത് [Karpenter-core](https://sigs.k8s.io/karpenter) APIകൾ പിന്തുണച്ചാൽ മറ്റ് കൺട്രോളറുകൾ ഉപയോഗിച്ച് മാറ്റിസ്ഥാപിക്കാനാകും.

## ഇൻസ്റ്റലേഷൻ

ഇൻസ്റ്റലേഷൻ മാർഗ്ഗനിർദ്ദേശം ഇവിടെ [check ചെയ്യുക](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## വേഗത്തിലുള്ള തുടക്കം - Inference Phi-3
[Sample Code Inference Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # ഔട്ട്‌പുട്ട് ACR പാത ട്യൂൺ ചെയ്യുന്നു
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

താഴെ കാണുന്ന കമാൻഡ് ഉപയോഗിച്ച് workspace നില നിരീക്ഷിക്കാം. WORKSPACEREADY കോളം `True` ആയാൽ, മോഡൽ വിജയകരമായി വിന്യസിച്ചിട്ടുണ്ട്.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

അടുത്തതായി, നിർണ്ണയ സേവനത്തിന്റെ ക്ലസ്റ്റർ IP കണ്ടെത്തി, ക്ലസ്റ്ററിൽ താൽക്കാലിക `curl` പോഡ് ഉപയോഗിച്ച് സേവനത്തിലേക്ക് പരീക്ഷണം നടത്താം.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## കൈറ്റോ ഉപയോഗിച്ച് Adapters-സഹിതം വേഗത്തിലുള്ള തുടക്കം - Inference Phi-3

Kaito ഇൻസ്റ്റാൾ ചെയ്തശേഷം, നിർണ്ണയ സേവനം ആരംഭിക്കുന്നതിന് താഴെ കാണുന്ന കമാൻഡുകൾ പരീക്ഷിക്കാം.

[Sample Code Inference Phi-3 with Adapters](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # ഔട്ട്‌പുട്ട് ACR പാത ട്യൂൺ ചെയ്യൽ
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

താഴെ കാണുന്ന കമാൻഡ് ഉപയോഗിച്ച് workspace നില നിരീക്ഷിക്കാം. WORKSPACEREADY കോളം `True` ആയാൽ, മോഡൽ വിജയകരമായി വിന്യസിച്ചിട്ടുണ്ട്.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

അടുത്തതായി, നിർണ്ണയ സേവനത്തിന്റെ ക്ലസ്റ്റർ IP കണ്ടെത്തി, ക്ലസ്റ്ററിൽ താൽക്കാലിക `curl` പോഡ് ഉപയോഗിച്ച് സേവനത്തിലേക്ക് പരീക്ഷണം നടത്താം.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസംബന്ധിക പ്രസ്താവന**:
ഈ രേഖ AI ഭാഷാന്തര സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതക്ക് ശ്രമിച്ചാൽ എങ്കിലും, സ്വയംകൃതമായ വിവർത്തനങ്ങളിൽ പിശകുകളും തെറ്റികളും ഉണ്ടായേക്കാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. സ്വതന്ത്ര ഭാഷയിലുള്ള મૂળ രേഖയാണ് പരമാധികാര ഉറവിടം എന്നത് പരിഗണിക്കേണ്ടതാണ്. പ്രധാന വിവരം ലഭിക്കുന്നതിനായി പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ആണ്. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതൊരു തെറ്റിദ്ധാരണയ്ക്കും ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->