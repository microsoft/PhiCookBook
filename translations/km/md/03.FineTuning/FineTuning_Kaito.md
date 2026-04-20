## ការត្រួតពិនិត្យលម្អិតជាមួយ Kaito

[Kaito](https://github.com/Azure/kaito) គឺជាអ្នកប្រតិបត្តិការម្នាក់ដែលស្វ័យប្រវត្តិដាក់បំពង់ម៉ូឌែល AI/ML នៅក្នុងក្រុមបណ្តាញ Kubernetes។

Kaito មានចំណុចផ្តាច់មុខសំខាន់ៗដូចខាងក្រោម ដែលខុសពីវិធីសាស្ត្រដាក់បំពង់ម៉ូឌែលពេញនិយមភាគច្រើនដែលបង្កើតលើហេដ្ឋារចនាសម្ព័ន្ធម៉ាស៊ីនមួយវេគី:

- គ្រប់គ្រងគណនីម៉ូឌែលដោយប្រើរូបភាពខុនតឺន័រ។ មានម៉ាស៊ីនសេវា http ដែលបានផ្តល់ដោយសម្រាប់ការហៅការទាញយកតាមបណ្ដុំម៉ូឌែល។
- ចៀសវាងការតម្រូវប៉ារ៉ាម៉ែត្រដាក់ទិន្នន័យ ដើម្បីសម្រួលទៅកាន់ឧបករណ៍ GPU ដោយផ្តល់ការកំណត់បង្ហាញតំបន់ជាមុន។
- អូតូម៉ាទិចផ្តល់នូវកុំព្យូទ័រ GPU ដោយផ្អែកលើតម្រូវការម៉ូឌែល។
- ផ្ទុករូបភាពម៉ូឌែលធំៗនៅក្នុង Microsoft Container Registry ក្នុងសាធារណៈ (MCR) ប្រសិនបើអាជ្ញាបណ្ណអនុញ្ញាត។

ដោយប្រើ Kaito វិធីធ្វើការនាំចូលម៉ូឌែល AI ធំៗក្នុង Kubernetes ត្រូវបានធ្វើឱ្យសាមញ្ញយ៉ាងខ្លាំង។

## ស្ថាបត្យកម្ម

Kaito តាមដានការរចនាម៉ូដែល Kubernetes Custom Resource Definition (CRD)/controller ដែលមានស្ទីល។ អ្នកប្រើគ្រប់គ្រងធនធានបុគ្គលិក `workspace` ដែលពិពណ៌នាពីតម្រូវការពី GPU និងលក្ខណៈពិសេសនៃការទាញយក។ អ្នកគ្រប់គ្រង Kaito នឹងស្វ័យប្រវត្តិដាក់បំពង់ដោយបង្រួចធនធានបុគ្គល `workspace`។
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

គំនូសខាងលើបង្ហាញទិដ្ឋភាពទូទៅនៃស្ថាបត្យកម្ម Kaito។ ផ្នែកសំខាន់ៗរួមមានៈ

- **Workspace controller**: វាបង្រួចធនធានបុគ្គល `workspace` បង្កើតធនធានបុគ្គល `machine` (ពន្យល់ខាងក្រោម) ដើម្បីបង្កើតកូនកាំបិត node អូតូម៉ាទិច និងបង្កើតការទាញយកការងារ (`deployment` ឬ `statefulset`) ដោយផ្អែកលើការកំណត់ម៉ូឌែលជាមុន។
- **Node provisioner controller**: ឈ្មោះរបស់អ្នកគ្រប់គ្រងនេះគឺ *gpu-provisioner* ក្នុង [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner)។ វាប្រើ CRD `machine` ដែលមានដើមគឺពី [Karpenter](https://sigs.k8s.io/karpenter) ដើម្បីប្រតិបត្តិការជាមួយអ្នកគ្រប់គ្រង workspace។ វាអភិវឌ្ឍជាមួយ API របស់ Azure Kubernetes Service (AKS) ដើម្បីបន្ថែមកូន node GPU ទៅកាន់ក្រុម AKS។
> សម្គាល់៖ [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ជាផ្នែកទូរទស្សន៍បើកចំហរ។ វាអាចជំនួសដោយអ្នកគ្រប់គ្រងផ្សេងៗ ប្រសិនបើពួកគេគាំទ្រ API របស់ [Karpenter-core](https://sigs.k8s.io/karpenter)។

## វីដេអូទិដ្ឋភាពទូទៅ  
[មើលការបង្ហាញ Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)  
## ការដំឡើង

សូមពិនិត្យមើលការណែនាំការដំឡើង [នៅនេះ](https://github.com/Azure/kaito/blob/main/docs/installation.md)។

## ចាប់ផ្តើមរហ័ស

បន្ទាប់ពីដំឡើង Kaito អ្នកអាចសាកល្បងបញ្ជា ខាងក្រោមដើម្បីចាប់ផ្តើមសេវាកម្មត្រួតពិនិត្យលម្អិត។

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # ការតម្រុយផ្លូវ ACR ផលិតភាព
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/fine-tuning/kaito_workspace_tuning_phi_3.yaml
```

អាចតាមដានស្ថានភាព workspace ដោយរត់បញ្ជា ខាងក្រោម។ ប្រសិនបើជួរឈរដែលមានឈ្មោះ WORKSPACEREADY ជា `True` នោះម៉ូឌែលត្រូវបានដាក់បំពង់ដោយជោគជ័យ។

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

បន្ទាប់មក អ្នកអាចរកឃើញតាម IP cluster របស់សេវាកម្ម inference ហើយប្រើ `curl` pod យកឧបករណ៍ពេលខ្លីដើម្បីសាកល្បងកំពូលសេវាកម្មនៅក្នុង cluster។

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការ​មិនទទួលខុសត្រូវ**៖  
ឯកសារ​នេះត្រូវបាន​ប្រែសម្រួល​ដោយប្រើ​ប្រាស់​សេវាកម្ម​ប្រែសម្រួល AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេល​យើងខិតខំផ្តល់ភាពត្រឹមត្រូវ សូម​យល់ព្រោះថា ការប្រែសម្រួល​ដោយស្វ័យប្រវត្តិ​អាចមានកំហុស ឬខុសផ្សេងៗ។ ឯកសារ​ដើម​នៅភាសាទីមូលដ្ឋាន គួរត្រូវបានកត់សម្គាល់ថា​ជាប្រភព​ផ្លូវការ។ សម្រាប់​ព័ត៌មាន​សំខាន់ៗ យើងផ្តល់អនុសាសន៍ឱ្យប្រើការប្រែសម្រួល​ដោយមនុស្សដែលមានជំនាញ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការប្រែប្រួលដែលកើតមានពីការប្រើប្រាស់ការប្រែសម្រួល​នេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->