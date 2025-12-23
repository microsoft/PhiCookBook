<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-12-22T01:15:35+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "ml"
}
-->
## Kaito ഉപയോഗിച്ച് ഇൻഫറൻസ്

[Kaito](https://github.com/Azure/kaito) ഒരു ഓപ്പറേറ്ററാണ്, ഇത് Kubernetes ക്ലസ്റ്ററിലെ AI/ML ഇൻഫറൻസ് മോഡൽ ഡിപ്ലോയ്‌മെന്റ് ഓട്ടോമേറ്റുചെയ്യുന്നു.

Kaito-ന് വെർച്വൽ മെഷീൻ അടിസ്ഥാനത്തിലുള്ള മെയിൻസ്റ്റ്രീം മോഡൽ ഡിപ്ലോയ്‌മെന്റ് രീതികളുമായി താരതമ്യം ചെയ്യുമ്പോൾ താഴെപ്പറയുന്ന പ്രധാന വ്യത്യാസങ്ങൾ ഉണ്ട്:

- മോഡൽ ഫയലുകൾ കണ്ടെയ്നർ ഇമേജുകൾ ഉപയോഗിച്ച് മാനേജ് ചെയ്യുന്നു. മോഡൽ ലൈബ്രറി ഉപയോഗിച്ച് ഇൻഫറൻസ് വിളിക്കാനുള്ള ഒരു http സെർവർ നൽകப்பட்டுள்ளது.
- പ്രസെറ്റ് കോൺഫിഗറേഷനുകൾ നൽകുന്നതിലൂടെ GPU ഹാർഡ്‌വെയറിനനുസരിച്ച് ഡിപ്ലോയ്‌മെന്റ് പാരാമീറ്ററുകൾ ട്യൂൺ ചെയ്യേണ്ടതിൽ നിന്ന് ഒഴിവാക്കുന്നു.
- മോഡൽ ആവശ്യകതകളുടെ അടിസ്ഥാനത്തിൽ GPU നോഡുകൾ സ്വയം പ്രൊവിഷൻ ചെയ്യുന്നു.
- ലൈസൻസ് അനുവദിക്കുകയാണെങ്കിൽ പൊതു Microsoft Container Registry (MCR)-ൽ വലിയ മോഡൽ ഇമേജുകൾ ഹോസ്റ്റ് ചെയ്യുന്നു.

Kaito ഉപയോഗിച്ച്, Kubernetes-ലിലുള്ള വലിയ AI ഇൻഫറൻസ് മോഡലുകൾ ഓൺബോർഡ് ചെയ്യാനുള്ള പ്രവൃത്തി പ്രവാഹം വലിയ തോതിൽ ലളിതമാക്കപ്പെടുന്നു.


## ആർക്കിടെക്ചർ

Kaito പരമ്പരാഗത Kubernetes Custom Resource Definition(CRD)/controller ഡിസൈൻ പാറ്റേൺ പിന്തുടരുന്നു. ഉപയോക്താവ് GPU ആവശ്യകതകളും ഇൻഫറൻസ് സ്പെസിഫിക്കേഷനും വിവരണം ചെയ്യുന്ന `workspace` കസ്റ്റം റിസോഴ്‌സ് കൈകാര്യം ചെയ്യുന്നു. Kaito കൺട്രോളറുകൾ `workspace` കസ്റ്റം റിസോഴ്സ് reconcile ചെയ്ത് ഡിപ്ലോയ്‌മെന്റ് ഓട്ടോമേറ്റുചെയ്യും.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito ആർക്കിടെക്ചർ" alt="Kaito ആർക്കിടെക്ചർ">
</div>

മുകളിൽ കാണിച്ചിരിക്കുന്ന ചിത്രം Kaito ആർക്കിടെക്ചറിന്റെ അവലോകനം അവതരിപ്പിക്കുന്നു. ഇതിന്റെ പ്രധാന ഘടകങ്ങൾ ഉൾപ്പെടുന്നത്:

- **Workspace controller**: ഇത് `workspace` കസ്റ്റം റിസോഴ്‌സ് reconcile ചെയ്യുന്നു, നോഡ് ഓട്ടോ പ്രൊവിഷനിംഗ് ട്രിഗർ ചെയ്യാൻ `machine` (താഴെ വിശദീകരിച്ചിരിക്കുന്നു) കസ്റ്റം റിസോഴ്‌സുകൾ സൃഷ്ടിക്കുന്നു, കൂടാതെ മോഡൽ പ്രിസെറ്റ് കോൺഫിഗറേഷനുകൾ അടിസ്ഥാനമാക്കി ഇൻഫറൻസ് വർക്ലോഡ് (`deployment` അല്ലെങ്കിൽ `statefulset`) സൃഷ്ടിക്കുന്നു.
- **Node provisioner controller**: കൺട്രോളറിന്റെ പേര് [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) ൽ *gpu-provisioner* ആണ്. അത് workspace controller-നുമായി ഇടപെടാൻ [Karpenter](https://sigs.k8s.io/karpenter)യിൽ നിന്നുള്ള `machine` CRD ഉപയോഗിക്കുന്നു. ഇത് Azure Kubernetes Service(AKS) APIs-നുമായി ഇന്റഗ്രേറ്റ് ചെയ്ത് AKS ക്ലസ്റ്ററിൽ പുതിയ GPU നോഡുകൾ ചേർക്കുന്നു. 
> കുറിപ്പ്: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ഒരു ഓപ്പൺ-സോഴ്‌സ് ഘടകമാണ്. ഇത് [Karpenter-core](https://sigs.k8s.io/karpenter) APIs പിന്തുണക്കുന്ന മറ്റ് കൺട്രോളറുകൾ ഉപയോഗിച്ച് മാറ്റാവുന്നതാണ്.

## ഇൻസ്റ്റലേഷൻ

ദയവായി ഇൻസ്റ്റലേഷൻ മാർഗനിർദ്ദേശം [ഇവിടെ](https://github.com/Azure/kaito/blob/main/docs/installation.md) പരിശോധിക്കുക.

## ക്വിക്ക് സ്റ്റാർട് ഇൻഫറൻസ് Phi-3
[സാമ്പിൾ കോഡ് ഇൻഫറൻസ് Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # ട്യൂണിംഗ് ഔട്ട്പുട്ട് ACR പാത
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

ചുവടെയുള്ള കമാൻഡ് اجرا ചെയ്ത് workspace സ്റ്റാറ്റസ് ട്രാക്ക് ചെയ്യാം. WORKSPACEREADY കോളം `True` ആയാൽ മോഡൽ വിജയകരമായി ഡിപ്ലോയ് ചെയ്തിരിക്കുന്നു.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

അടുത്തതായി, ഇൻഫറൻസ് സർവീസിന്റെ ക്ലസ്റ്റർ ip കണ്ടെത്തി ക്ലസ്റ്ററിലെ സർവീസ് എൻഡ്‌പോയിന്റ് ടെസ്റ്റ് ചെയ്യാൻ താത്കാലിക `curl` പോഡ് ഉപയോഗിക്കാം.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## ക്വിക്ക് സ്റ്റാർട്ട് ഇൻഫറൻസ് Phi-3 അഡാപ്റ്ററുകളോടൊപ്പം

Kaito ഇൻസ്റ്റാൾ ചെയ്തശേഷം, ഇൻഫറൻസ് സർവീസ് ആരംഭിക്കാനായി താഴെപ്പറയുന്ന കമാൻഡുകൾ പരീക്ഷിക്കാം.

[സാമ്പിൾ കോഡ് ഇൻഫറൻസ് Phi-3 അഡാപ്റ്ററുകളോടെ](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # ട്യൂണിംഗ് ഔട്ട്‌പുട്ട് ACR പാത
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

ചുവടെയുള്ള കമാൻഡ് 실행 ചെയ്ത് workspace സ്റ്റാറ്റസ് ട്രാക്ക് ചെയ്യാം. WORKSPACEREADY കോളം `True` ആയാൽ മോഡൽ വിജയകരമായി ഡിപ്ലോയ് ചെയ്തിരിക്കുന്നു.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

അടുത്തതായി, ഇൻഫറൻസ് സർവീസിന്റെ ക്ലസ്റ്റർ ip കണ്ടെത്തി ക്ലസ്റ്ററിലെ സർവീസ് എൻഡ്‌പോയിന്റ് ടെസ്റ്റ് ചെയ്യാൻ താത്കാലിക `curl` പോഡ് ഉപയോഗിക്കാം.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ഡിസ്‌ക്ലെയിമർ:
ഈ ഡോക്യുമെന്റ് AI പരിഭാഷാ സേവനമായ [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷചെയ്‍തതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി പരിശ്രമിച്ചിരുന്നാലും, സ്വയമത്തിലൂടെ്ഇടക്കുന്ന പരിഭാഷകളിൽ പിശകുകളും അസൂയതകളും ഉണ്ടാകാൻ സാധ്യതയുണ്ടെന്ന് ദയവായി ശ്രദ്ധിക്കുക. ഇതിന്റെ മാതൃഭാഷയിലുള്ള മൂല രേഖ പ്രാമാണിക സ്രോതസ്സായിരുന്നേക്കണം. നിർണായകമായ വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മാനവപരിഭാഷ നിർദേശിക്കുന്നു. ഈ പരിഭാഷയുടെ ഉപയോഗത്തിൽ നിന്നുണ്ടാകുന്ന任何 തെറ്റിദ്ധാരണങ്ങൾക്കോ വ്യാഖ്യാനഭ്രമങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->