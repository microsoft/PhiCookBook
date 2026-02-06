## Kaito ഉപയോഗിച്ച് ഫൈൻ-ട്യൂണിംഗ് 

[Kaito](https://github.com/Azure/kaito) Kubernetes ക്ലസ്റ്ററിലുള്ള AI/ML ഇൻഫറൻസ് മോഡൽ ഡിപ്ലോയ്മെന്റ് ഓട്ടോമേറ്റുചെയ്യുന്ന ഒരു ഓപ്പറേറ്ററാണ്.

Kaito-ക്ക് വെർച്ച്വൽ മെഷീൻ അടിസ്ഥാനത്തിലുള്ള ഇൻഫ്രാസ്ട്രക്ചറുകളിലേക്ക് നിർമിച്ച മെയിൻസ്റ്റ്രീം മോഡൽ ഡിപ്ലോയ്മെന്റ് രീതികളുമായി താരതമ്യപ്പെടുത്തുമ്പോൾ താഴെപ്പറയുന്ന പ്രധാന വ്യത്യാസങ്ങൾ ഉണ്ട്:

- മോഡൽ ഫയലുകൾ container images ഉപയോഗിച്ച് മാനേജ് ചെയ്യുക. മോഡൽ ലൈബ്രറി ഉപയോഗിച്ച് ഇൻഫറൻസ് കോൾകൾ നടത്താൻ ഒരു http സെർവർ നൽകിയിരിക്കുന്നു.
- പ്രിസെറ്റ് കോൺഫിഗറേഷനുകൾ നൽകി GPU ഹാർഡ്വെയറിനൊത്തുനേരമായി ഡിപ്ലോയ്മെന്റ് പാരാമീറ്ററുകൾ ട്യൂൺ ചെയ്യേണ്ട ആവശ്യം ഒഴിവാക്കുന്നു.
- മോഡൽ ആവശ്യകതകൾ അടിസ്ഥാനമാക്കി GPU നോഡുകൾ സ്വയമേവ പ്രൊവിഷൻ ചെയ്യുക.
- ലൈസൻസ് അനുവദിച്ചാൽ വലിയ മോഡൽ ഇമേജുകൾ public Microsoft Container Registry (MCR)-ൽ ഹോസ്റ്റ് ചെയ്യുക.

Kaito ഉപയോഗിച്ച് Kubernetes-ൽ വലിയ AI ഇൻഫറൻസ് മോഡലുകൾ ഓൺബോർഡ് ചെയ്യാനുള്ള വർക്‌ഫ്ലോ വളരെ ലളിതമാക്കപ്പെടുന്നു.


## ആർക്കിടെക്ചർ

Kaito പരമ്പരാഗതമായ Kubernetes Custom Resource Definition(CRD)/controller ഡിസൈൻ പാറ്റേൺ പിന്തുടരുന്നു. ഉപയോക്താവ് GPU ആവശ്യകതകളും ഇൻഫറൻസ് സ്പെസിഫിക്കേഷനും വിശദീകരിക്കുന്ന ഒരു `workspace` custom resource മാനേജ് ചെയ്യുന്നു. Kaito controllers `workspace` custom resource reconcile ചെയ്ത് ഡിപ്ലോയ്മെന്റ് ഓട്ടോമേറ്റുചെയ്യും.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito ആർക്കിടെക്ചർ" alt="Kaito ആർക്കിടെക്ചർ">
</div>

മുകളിലുള്ള ചിത്രത്തിൽ Kaito ആർക്കിടെക്ചറിന്റെ അവലോകനമാണ് പ്രത്യക്ഷം. അതിന്റെ പ്രധാന ഘടകങ്ങൾ താഴെക്കാണുന്നതാണ്:

- **വർക്ക്സ്പേസ് കൺട്രോളർ**: ഇത് `workspace` custom resource reconcile ചെയ്യുന്നു, നോഡ് ഓട്ടോ-പ്രൊവിഷനിംഗ് ട്രിഗർ ചെയ്യാൻ `machine` (താഴെ വിശദീകരിച്ചിരിക്കുന്നു) custom resources സൃഷ്ടിക്കുന്നു, കൂടാതെ മോഡൽ പ്രിസെറ്റ് കോൺഫിഗറേഷനുകൾ അടിസ്ഥാനമാക്കി ഇൻഫറൻസ് വർക്ക്ലോഡ് (`deployment` അല്ലെങ്കിൽ `statefulset`) സൃഷ്ടിക്കുന്നു.
- **Node provisioner controller**: കണ്ട്രോളറിന്റെ പേര് [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) ൽ *gpu-provisioner* ആണ്. ഇത് workspace controller-നുമായി ഇന്ററാക്ട് ചെയ്യാൻ [Karpenter](https://sigs.k8s.io/karpenter) നിന്നുണ്ടായ `machine` CRD ഉപയോഗിക്കുന്നു. ഇത് Azure Kubernetes Service(AKS) APIs-നുമായി സംയോജിച്ച് AKS ക്ലസ്റ്ററിലേക്ക് പുതിയ GPU നോഡുകൾ ചേർക്കുന്നു. 
> കുറിപ്പ്: The [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ഒരു open sourced component ആണ്. ഇത് [Karpenter-core](https://sigs.k8s.io/karpenter) APIs പിന്തുണക്കുന്ന മറ്റു കണ്ട്രോളറുകൾ ഉപയോഗിച്ച് മാറ്റിസ്ഥാപിക്കാവുന്നതാണ്.

## അവലോകന വീഡിയോ 
[Kaito ഡെമോ കാണുക](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)
## ഇൻസ്റ്റലേഷൻ

ഇൻസ്റ്റലേഷൻ മാർഗനിർദ്ദേശങ്ങൾക്കായി ദയവായി [ഇവിടെ](https://github.com/Azure/kaito/blob/main/docs/installation.md) പരിശോധിക്കുക.

## ക്വിക്ക് സ്റ്റാർട്ട്

Kaito ഇൻസ്റ്റാൾ ചെയ്തതിനുശേഷം, ഫൈൻ-ട്യൂണിംഗ് സർവീസ് ആരംഭിക്കാൻ താഴെയുള്ള കമാൻഡുകൾ പരീക്ഷിക്കാവുന്നതാണ്.

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # ട്യൂണിംഗ് ഔട്ട്പുട്ട് ACR പാത
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/fine-tuning/kaito_workspace_tuning_phi_3.yaml
```

താഴെക്കാണുന്ന കമാൻഡ് റൺ ചെയ്താൽ workspace നില ട്രാക്ക് ചെയ്യാൻ കഴിയും. WORKSPACEREADY കോളം `True` ആയിച്ചാൽ മോഡൽ വിജയകരമായി ഡിപ്ലോയ് ചെയ്തിട്ടുണ്ട്.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

അടുത്തതായി, ഇൻഫറൻസ് സർവീസിന്റെ ക്ലസ്റ്റർ ip കണ്ടെത്തി ക്ലസ്റ്ററിനുള്ളിൽ സർവിസ് എൻഡ്‌പോയിന്റ് ടെസ്റ്റ് ചെയ്യാൻ ഒരു താൽക്കാലിക `curl` പോഡ് ഉപയോഗിക്കാവുന്നു.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ഡിസ്‌ക്ലെയിമർ:
ഈ ഡോക്യുമെന്റ് AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്ക് ശ്രമിച്ചാലും, ഓട്ടോമേറ്റഡ് വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാവാൻ സാധ്യതയുണ്ടെന്ന് ദയവായി ശ്രദ്ധിക്കുക. യഥാർത്ഥ ഭാഷയിലുള്ള ഒറിജിനൽ ഡോക്യുമെന്റ് ആണ് അദ്ധീകാര്യമായ ഉറവിടം എന്ന് കരുതണമെന്ന് നിർദേശിക്കുന്നു. നിർണ്ണായകമായ വിവരങ്ങൾക്കായി പ്രൊഫഷണൽ മനുഷ്യപരിഭാഷ ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിച്ചതിനെത്തുടർന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കും വ്യാഖ്യാനപിഴവുകൾക്കും ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->