## ការសន្និដ្ឋានជាមួយ Kaito

[Kaito](https://github.com/Azure/kaito) គឺជាម៉ាស៊ីនប្រតិបត្តិការ ព្រមទាំងស្វ័យប្រតិបត្តិការការផ្ទុកបង្ហោះម៉ូឌែល AI/ML សម្រាប់ការសន្និដ្ឋានក្នុងក្លាស៊ែរ Kubernetes។

Kaito មានការផ្លាស់ប្តូរសំខាន់ៗបញ្ចាក់ខុសពីវិធីសាស្រ្តផ្ទុកម៉ូឌែលដែលមានប្រជាប្រិយភាពបំផុតច្រើន ដែលបានសង់លើហេដ្ឋារចនាសម្ព័ន្ធម៉ាស៊ីនវីរុអាល់ (virtual machine):

- គ្រប់គ្រងឯកសារម៉ូឌែលដោយប្រើរូបភាពឃុងតឺន័រ។ មានមួយម៉ាស៊ីនបម្រើ http ដែលផ្តល់សេវាកម្មសម្រាប់ហៅសន្និដ្ឋានដោយប្រើបណ្ណាល័យម៉ូឌែល។
- ដាក់ចៀសវាងការតំឡើងប៉ារ៉ាម៉ែត្រផ្ទុកដើម្បីសម្រួលគាំទ្រដើម្បីផ្គូផ្គងបន្ទះ GPU តាមការផ្តល់ការកំណត់ជាមុន។
- បង្កើត núod GPU ដោយស្វ័យប្រវត្តិឡើងវិញដោយផ្អែកលើតំរូវការម៉ូឌែល។
- ផ្ទុករូបភាពម៉ូឌែលធំនៅក្នុង Microsoft Container Registry (MCR) ការបើកផ្សព្វផ្សាយបើអនុញ្ញាតឲ្យមានអាជ្ញាប័ណ្ណ។

ដោយប្រើ Kaito ខ្សែការងារនៃការបញ្ចូលម៉ូឌែល AI សន្និដ្ឋានធំនៅ Kubernetes ត្រូវបានសាមញ្ញយ៉ាងខ្លាំង។

## ស្ថាបត្យកម្ម

Kaito អនុវត្តតាមគំរូបែបផែន Custom Resource Definition(CRD)/controller ចាស់ទាស់របស់ Kubernetes។ អ្នកប្រើគ្រប់គ្រងធនធានបណ្តាញផ្ទាល់ខ្លួន `workspace` ដែលពិពណ៌នាអំពីតម្រូវការចំពោះ GPU និងការបញ្ជាក់សន្និដ្ឋាន។ ឃោសនាកម្ម Kaito នឹងស្វ័យប្រវត្តិក្នុងការផ្ទុកដោយធ្វើការបង្រួមបង្រួមមធ្យោបាយ `workspace` custom resource ។

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architecture" alt="KAITO RAGEngine architecture">
</div>

រូបភាពខាងលើបង្ហាញទិដ្ឋភាពទូទៅនៃស្ថាបត្យកម្ម Kaito។ ធាតុសំខាន់ៗរបស់វា រួមមាន៖

- **Workspace controller**: វាបង្រួមបង្រួមមធ្យោបាយ `workspace` custom resource, បង្កើត `machine` (បានពន្យល់ខាងក្រោម) custom resources ដើម្បីចាប់ផ្តើមការបង្កើត núod ដោយស្វ័យប្រវត្តិ, និងបង្កើតភារកិច្ចសន្និដ្ឋាន (`deployment` ឬ `statefulset`) ដោយផ្អែកលើការកំណត់ជាមុនរបស់ម៉ូឌែល។
- **Node provisioner controller**: ឈ្មោះឃោសនា *gpu-provisioner* ក្នុង [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner)។ វា ប្រើ `machine` CRD ដែលមានដើមកំណើតពី [Karpenter](https://sigs.k8s.io/karpenter) ដើម្បីធ្វើការប្រាស្រ័យទាក់ទងជាមួយ workspace controller។ វាបញ្ចូលជាមួយ API របស់ Azure Kubernetes Service(AKS) ដើម្បីបន្ថែម núod GPU ថ្មីៗ ទៅក្នុងក្លាស៊ែរ AKS។  
> Note: The [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) គឺជាគ្រឿងចង្កេះបើកប្រភព។ វាអាចត្រូវបានជំនួសដោយឃោសនាផ្សេងទៀត បើសិនជាពួកគេគាំទ្រអំពី API [Karpenter-core](https://sigs.k8s.io/karpenter)។

## ការតម្លើង

សូមពិនិត្យមើលការណែនាំការតម្លើង [នៅទីនេះ](https://github.com/Azure/kaito/blob/main/docs/installation.md)។

## ចាប់ផ្តើមលឿន ជាមួយសន្និដ្ឋាន Phi-3  
[Code ឧទាហរណ៍សន្និដ្ឋាន Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # កំណត់បច្ចេកទេសផ្លូវចេញ ACR
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```
  
អាចតាមដានស្ថានភាព workspace ដោយការបញ្ជាទាត់បន្ទាត់បញ្ជាខាងក្រោម។ នៅពេលដែលជួរឈរ WORKSPACEREADY បង្ហាញជា `True` នោះម៉ូឌែលត្រូវបានផ្ទុកជាស្ថាពរហើយ។

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```
  
បន្ទាប់មក អ្នកអាចស្វែងរក cluster ip របស់សេវាសន្និដ្ឋាន ហើយប្រើ pod `curl` ជាបណ្តោះអាសន្ន ដើម្បីសាកល្បងច្រកសេវាកម្មនៅក្នុងក្លាស៊ែរ។

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```
  
## ចាប់ផ្តើមលឿនជាមួយសន្និដ្ឋាន Phi-3 មាន adapters

បន្ទាប់ពីបានតម្លើង Kaito អ្នកអាចសាកល្បងបញ្ជារបញ្ជាខាងក្រោម ដើម្បីចាប់ផ្តើមសេវាសន្និដ្ឋាន។

[Code ឧទាហរណ៍សន្និដ្ឋាន Phi-3 ជាមួយ Adapters](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # ការតម្រឹមផ្លូវ ACR ចេញ
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```
  
អាចតាមដានស្ថានភាព workspace ដោយការបញ្ជាទាត់បន្ទាត់បញ្ជាខាងក្រោម។ នៅពេលដែលជួរឈរ WORKSPACEREADY បង្ហាញជា `True` នោះម៉ូឌែលត្រូវបានផ្ទុកជាស្ថាពរហើយ។

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```
  
បន្ទាប់មក អ្នកអាចស្វែងរក cluster ip របស់សេវាសន្និដ្ឋាន ហើយប្រើ pod `curl` ជាបណ្តោះអាសន្ន ដើម្បីសាកល្បងច្រកសេវាកម្មនៅក្នុងក្លាស៊ែរ។

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំខិតខំក្នុងការធានាភាពត្រឹមត្រូវ ក៏សូមយល់ដឹងថាការបកប្រែដោយស្វ័យប្រវត្តិកើតមានកំហុសឬអច្បាប់ខុសខាតបាន។ ឯកសារដើមជាភាសាដើមគួរត្រូវបានយកសម្រាប់ជាអ្នកផ្ដល់ព័ត៌មានដែលមានសុពលភាព។ សម្រាប់ព័ត៌មានសំខាន់ យើងណែនាំឲ្យមានការបកប្រែដោយអ្នកជំនាញមនុស្ស។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំឬការបកស្រាយខុសដែលមានហេតុចេញពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->