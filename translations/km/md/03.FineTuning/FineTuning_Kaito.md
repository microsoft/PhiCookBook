## ការកែប្រែឲ្យសមរម្យជាមួយ Kaito

[Kaito](https://github.com/Azure/kaito) គឺជាអ្នកប្រតិបត្ដិការដែលស្វ័យប្រវត្តិក្នុងការចេញផ្សាយម៉ូដែលកំណត់អត្តសញ្ញាណ AI/ML ក្នុងក្លាស្តឺរ Kubernetes។

Kaito មានការផ្សេងគ្នាសំខាន់ៗដូចខាងក្រោមត្រូវធ្វើប្រៀបធៀបជាមួយវិធីសាស្រ្តចេញផ្សាយម៉ូដែលភាគច្រើនដែលបានបង្កើតលើហេដ្ឋារចនាសម្ព័ន្ធម៉ាស៊ីនមួយចំនួន៖

- គ្រប់គ្រងឯកសារម៉ូដែលដោយប្រើរូបភាព container។ មានម៉ាស៊ីនបម្រើ http ផ្តល់សេវាឲ្យហៅកំណត់អត្តសញ្ញាណដោយប្រើបណ្ណាល័យម៉ូដែល។
- ជៀសវាងការកំណត់ប៉ារ៉ាម៉ែត្រចេញផ្សាយសម្រាប់ផ្ទៀងផ្ទាត់ជាមួយសំភារៈ GPU ដោយផ្តល់ការកំណត់ជាមុន។
- ព្យួរបង្កើតជាមួយកូនខ្នាត GPU ដោយស្វ័យប្រវត្តិរួមបញ្ចូលតាមតម្រូវការម៉ូដែល។
- ផ្ទុករូបភាពម៉ូដែលធំៗនៅក្នុង Microsoft Container Registry (MCR) សាធារណៈ ប្រសិនបើមានការអនុញ្ញាតព័ត៌មានលិខិតអាជ្ញាបណ្ណ។

ដោយប្រើ Kaito ការប្រតិបត្ដិការចូលរួមម៉ូដែលកំណត់អត្តសញ្ញាណ AI ធំៗក្នុង Kubernetes កាន់តែងាយស្រួលខ្លាំង។

## សំណុំរចនាសម្ព័ន្ធ

Kaito អនុវត្តន៍បែបបទកំណត់ធនធានផ្ទាល់(Custom Resource Definition, CRD)/controller នៃ Kubernetes ដั้งដាល។ អ្នកប្រើគ្រប់គ្រងធនធានផ្ទាល់ `workspace` ដែលពិពណ៌នាវិញពីតម្រូវការកូនខ្នាត GPU និងបញ្ជាក់កំណត់អត្តសញ្ញាណ។ ម៉ាស៊ីនត្រួតពិនិត្យ Kaito នឹងស្វ័យប្រវត្តិក្នុងការចេញផ្សាយដោយការផ្គូផ្គងធនធានផ្ទាល់ `workspace`។

<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="រចនាសម្ព័ន្ធ Kaito" alt="រចនាសម្ព័ន្ធ Kaito">
</div>

រូបភាពខាងលើបង្ហាញទិដ្ឋភាពទូទៅនៃរចនាសម្ព័ន្ធ Kaito។ ធាតុសំខាន់ៗរបស់វារួមមាន៖

- **កុងត្រូលឡែរកន្លែងការ​ការងារ (Workspace controller)**៖ វាផ្គូផ្គងធនធានផ្ទាល់ `workspace` បង្កើតធនធានផ្ទាល់ `machine` (បានពិពណ៌នាខាងក្រោម) ដើម្បីបញ្ចេញបញ្ជា​ឲ្យបង្កើតកូនខ្នាតដោយស្វ័យប្រវត្តិ ហើយបង្កើតការងារកំណត់អត្តសញ្ញាណ (`deployment` ឬ `statefulset`) ដើម្បីផ្អែកលើការកំណត់ជាមុនរបស់ម៉ូដែល។
- **កុងត្រូលឡែរបង្កើតកូនខ្នាត (Node provisioner controller)**៖ ឈ្មោះកុងត្រូលនេះគឺ *gpu-provisioner* ក្នុង [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner)។ វាប្រើ CRD `machine` ដែលចាប់ផ្តើមពី [Karpenter](https://sigs.k8s.io/karpenter) ដើម្បីឆ្លើយតបទៅកាន់កុងត្រូល workspace។ វាភ្ជាប់ជាមួយ APIs របស់ Azure Kubernetes Service (AKS) ដើម្បីបន្ថែមកូនខ្នាត GPU ថ្មី ទៅក្នុងក្លាស្ទឺរ AKS។  
> សម្គាល់៖ [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) គឺជាធាតុដែលបើកកូដមួយ។ វាអាចជំនួសដោយកុងត្រូលផ្សេងៗ បើពួកវាគាំទ្រ APIs [Karpenter-core](https://sigs.k8s.io/karpenter)។

## វីដេអូទិដ្ឋភាពទូទៅ 
[មើលការបង្ហាញ Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## ការដំឡើង

សូមពិនិត្យមើលមគ្គុទេសក៍ដំឡើង [នៅទីនេះ](https://github.com/Azure/kaito/blob/main/docs/installation.md)។

## ចាប់ផ្តើមយ៉ាងរហ័ស

បន្ទាប់ពីបានដំឡើង Kaito អ្នកអាចព្យាយាមបញ្ជាការដូចខាងក្រោម ដើម្បីចាប់ផ្តើមសេវាកម្មកែប្រែឲ្យសមរម្យ។

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # ការតម្រង់ផ្លូវចេញ ACR
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/fine-tuning/kaito_workspace_tuning_phi_3.yaml
```

អាចតាមដានស្ថានភាព workspace ដោយរត់បញ្ជាការខាងក្រោម។ពេលផ្នែក WORKSPACEREADY ក្លាយជា `True` នេះមានន័យថា ម៉ូដែលបានចេញផ្សាយដោយជោគជ័យរួចហើយ។

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

បន្ទាប់មក អ្នកអាចស្វែងរកអាសយដ្ឋាន IP ក្រុមហ៊ុនសេវាកម្មកំណត់អត្តសញ្ញាណ ហើយប្រើ pod `curl` សម្រាប់ពេលខ្លី ដើម្បីសាកល្បងច្រកសេវាកម្មនៅក្នុងក្លាស្ទឺរ។

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ** ៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ក្នុងខណៈពេលដែលយើងខិតខំប្រឹងប្រែងឲ្យបានភាពត្រឹមត្រូវ សូមយល់ពីថា ការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬការមិនត្រឹមត្រូវខ្លះៗ។ ឯកសារដើមដោយភាសាមាតុភូមិគួរត្រូវបានពិចារណាថាជាផ្លូវការជាដើម។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមផ្តល់អាទិភាពដល់ការបកប្រែដោយអ្នកជំនាញមនុស្ស។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកប្រែខុសឆ្ងល់ណាមួយដែលកើតមានពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->