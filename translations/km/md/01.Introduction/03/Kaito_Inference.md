## ការសន្និដ្ឋាន ជាមួយ Kaito 

[Kaito](https://github.com/Azure/kaito) គឺជាអុបផេរ៉ែត័រមួយដែលធ្វើអូតូម៉េតិកក្នុងការចែកចាយម៉ូឌែល AI/ML សម្រាប់ការសន្និដ្ឋានក្នុងក្រុម Kubernetes ។

Kaito មានភាពខុសគ្នាសំខាន់ៗដូចខាងក្រោម ដោយប្រៀបធៀបនឹងវិធីសាស្ត្រចែកចាយម៉ូឌែលដ៏ធម្មតាច្រើនដែលបានសង់លើអគ្គិសនីកម្មវិធីម៉ាស៊ីនមេ (virtual machine)៖

- គ្រប់គ្រងឯកសារម៉ូឌែលដោយប្រើរូបភាព container។ មានម៉ាស៊ីនបម្រើ http ត្រូវបានផ្តល់សម្រាប់អនុវត្តការហៅសន្និដ្ឋានដោយប្រើបណ្ណាល័យម៉ូឌែល។
- ជៀសវាងការត្រួតពិនិត្យប៉ារ៉ាម៉ែត្រ deployment ដើម្បីឱ្យសមរម្យទៅនឹងឧបករណ៍ GPU ដោយផ្តល់ការកំណត់ជាមុន។
- រៀបចំកំណត់នូវកន្លែងGPU យ៉ាងស្វ័យប្រវត្តិដោយផ្អែកលើតម្រូវការម៉ូឌែល។
- បមត់រូបភាពម៉ូឌែលធំនៅក្នុង Public Microsoft Container Registry (MCR) ប្រសិនបើអាជ្ញាបណ្ណអនុញ្ញាត។

ដោយប្រើ Kaito ឈុតចរន្តការងារនៃការនាំចូលម៉ូឌែល AI សម្រាប់ការសន្និដ្ឋានធំៗក្នុង Kubernetes ត្រូវបានធ្វើឱ្យសាមញ្ញយ៉ាងច្រើន។

## ស្ថាបត្យកម្ម

Kaito អនុវត្តតាមលំនាំរចនាបែបប្រពៃណីនៃ Kubernetes Custom Resource Definition (CRD)/controller។ អ្នកប្រើគ្រប់គ្រង custom resource `workspace` ដែលពិពណ៌នាអំពីតម្រូវការជាចំពោះ GPU និងលក្ខណៈបញ្ជាក់សម្រាប់សន្និដ្ឋាន។ controllers របស់ Kaito នឹងធ្វើអូតូម៉ាទិចក្នុងការចែកចាយដោយធ្វើការ reconcile លើ custom resource `workspace` ។ 

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="រចនាសម្ព័ន្ធ KAITO RAGEngine" alt="រចនាសម្ព័ន្ធ KAITO RAGEngine">
</div>

រូបភាពខាងលើបង្ហាញទិដ្ឋភាពទូទៅនៃស្ថាបត្យកម្ម Kaito។ ធាតុលេខសំខាន់ៗរួមមាន:

- **Workspace controller**: វា reconcile លើ custom resource `workspace` បង្កើត custom resources `machine` (ពន្យល់ខាងក្រោម) ដើម្បីចាប់ផ្តើមការផ្តល់កន្លែង node យ៉ាងស្វ័យប្រវត្តិ ហើយបង្កើតកម្មការការងារសម្រាប់សន្និដ្ឋាន (`deployment` ឬ `statefulset`) ដោយផ្អែកលើការកំណត់ជាមុនសម្រាប់ម៉ូឌែល។
- **Node provisioner controller**: ឈ្មោះ controller នេះគឺ *gpu-provisioner* ក្នុង [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner)។ វាប្រើ `machine` CRD ដែលមានដើមកំណើតពី [Karpenter](https://sigs.k8s.io/karpenter) ដើម្បីអន្តរកម្មជាមួយ workspace controller។ វារួមបញ្ចូលជាមួយសេវាកម្ម Azure Kubernetes Service (AKS) APIs ដើម្បីបន្ថែមកន្លែង GPU ថ្មីទៅកាន់ក្រុម AKS ។
> បញ្ជាក់: The [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) គឺជាធាតុមួយដែលបានបើកប្រភព។ វាអាចជំនួសដោយ controllers ផ្សេងទៀត ប្រសិនបើពួកវាគាំទ្រ APIs [Karpenter-core](https://sigs.k8s.io/karpenter) ។

## Installation

សូមពិនិត្យមើលការណែនាំការដំឡើង [here](https://github.com/Azure/kaito/blob/main/docs/installation.md)។

## Quick start Inference Phi-3
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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # ផ្លូវ ACR សម្រាប់ការកែតម្រូវលទ្ធផលចេញ
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

អាចតាមដានស្ថានភាព workspace ដោយរត់ពាក្យបញ្ជាខាងក្រោម។ ពេលដែលជួរឈរដែលមានឈ្មោះ WORKSPACEREADY ក្លាយទៅជា `True` នោះម៉ូឌែលត្រូវបានចែកចាយដោយដោយជោគជ័យ។

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

បន្ទាប់មក អ្នកអាចស្វែងរក cluster ip របស់សេវាកម្មសន្និដ្ឋាន ហើយប្រើ pod `curl` តាមខណៈខ្លីសម្រាប់សាកល្បងចំណុចបញ្ចប់សេវាកម្មនៅក្នុងក្រុម។

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Quick start Inference Phi-3 with adapters

បន្ទាប់ពីដំឡើង Kaito អ្នកអាចសាកល្បងពាក្យបញ្ជាខាងក្រោមដើម្បីចាប់ផ្តើមសេវាកម្មសន្និដ្ឋាន។

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # ផ្លូវ ACR លទ្ធផលសម្រាប់ការកែតម្រូវ
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

អាចតាមដានស្ថានភាព workspace ដោយរត់ពាក្យបញ្ជាខាងក្រោម។ ពេលដែលជួរឈរដែលមានឈ្មោះ WORKSPACEREADY ក្លាយទៅជា `True` នោះម៉ូឌែលត្រូវបានចែកចាយដោយដោយជោគជ័យ។

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

បន្ទាប់មក អ្នកអាចស្វែងរក cluster ip របស់សេវាកម្មសន្និដ្ឋាន ហើយប្រើ pod `curl` តាមខណៈខ្លីសម្រាប់សាកល្បងចំណុចបញ្ចប់សេវាកម្មនៅក្នុងក្រុម។

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធការទទួលខុសត្រូវ**:
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែដោយ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលដែលយើងខំប្រឹងសម្រាប់ភាពត្រឹមត្រូវ សូមយកចិត្តទុកដាក់ថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមក្នុងភាសាមាតុភូមិគួរត្រូវបានចាត់ទុកថាជាប្រភពដែលទុកចិត្តបាន។ សម្រាប់ព័ត៌មានសំខាន់ៗ ការបកប្រែដោយអ្នកជំនាញមនុស្សត្រូវបានផ្តល់អនុសាសន៍។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកចេញខុសណាមួយដែលកើតមានពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->