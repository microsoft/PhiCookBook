<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-07-17T06:20:42+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "mr"
}
-->
## Kaito सह फाइन-ट्यूनिंग

[Kaito](https://github.com/Azure/kaito) हा एक ऑपरेटर आहे जो Kubernetes क्लस्टरमध्ये AI/ML इन्फरन्स मॉडेल डिप्लॉयमेंट स्वयंचलित करतो.

Kaito मध्ये बहुतेक मुख्य प्रवाहातील मॉडेल डिप्लॉयमेंट पद्धतींपेक्षा खालील महत्त्वाचे फरक आहेत, जे वर्चुअल मशीन इन्फ्रास्ट्रक्चरवर आधारित आहेत:

- कंटेनर इमेजेस वापरून मॉडेल फाइल्स व्यवस्थापित करा. मॉडेल लायब्ररी वापरून इन्फरन्स कॉल करण्यासाठी http सर्व्हर दिला आहे.
- GPU हार्डवेअरशी जुळवून घेण्यासाठी डिप्लॉयमेंट पॅरामीटर्स ट्यून करण्याची गरज नाही, कारण प्रीसेट कॉन्फिगरेशन दिलेले आहेत.
- मॉडेलच्या गरजेनुसार GPU नोड्स आपोआप पुरवठा करा.
- परवानगी असल्यास मोठ्या मॉडेल इमेजेस सार्वजनिक Microsoft Container Registry (MCR) मध्ये होस्ट करा.

Kaito वापरून, Kubernetes मध्ये मोठ्या AI इन्फरन्स मॉडेल्सचे ऑनबोर्डिंगचे कार्यप्रवाह मोठ्या प्रमाणात सुलभ होते.

## आर्किटेक्चर

Kaito पारंपरिक Kubernetes Custom Resource Definition(CRD)/controller डिझाइन पॅटर्नचे पालन करतो. वापरकर्ता `workspace` कस्टम रिसोर्स व्यवस्थापित करतो, जो GPU गरजा आणि इन्फरन्स स्पेसिफिकेशन वर्णन करतो. Kaito कंट्रोलर्स `workspace` कस्टम रिसोर्सचे समन्वय करून डिप्लॉयमेंट स्वयंचलित करतात.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

वरील आकृती Kaito आर्किटेक्चरचा आढावा दर्शवते. त्याचे मुख्य घटक खालीलप्रमाणे आहेत:

- **Workspace controller**: हा `workspace` कस्टम रिसोर्सचे समन्वय करतो, नोड ऑटो प्रोव्हिजनिंगसाठी `machine` (खाली समजावलेले) कस्टम रिसोर्स तयार करतो, आणि मॉडेल प्रीसेट कॉन्फिगरेशननुसार इन्फरन्स वर्कलोड (`deployment` किंवा `statefulset`) तयार करतो.
- **Node provisioner controller**: या कंट्रोलरचे नाव [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) मध्ये *gpu-provisioner* आहे. हा `machine` CRD वापरतो जो [Karpenter](https://sigs.k8s.io/karpenter) कडून आला आहे आणि workspace controller शी संवाद साधतो. तो Azure Kubernetes Service(AKS) API सह एकत्र काम करून AKS क्लस्टरमध्ये नवीन GPU नोड्स जोडतो.
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) हा एक ओपन सोर्स घटक आहे. जर इतर कंट्रोलर्स [Karpenter-core](https://sigs.k8s.io/karpenter) API सपोर्ट करत असतील तर त्याने तो बदलता येऊ शकतो.

## आढावा व्हिडिओ  
[Kaito डेमो पाहा](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## इन्स्टॉलेशन

कृपया इन्स्टॉलेशन मार्गदर्शन [येथे](https://github.com/Azure/kaito/blob/main/docs/installation.md) तपासा.

## जलद प्रारंभ

Kaito इन्स्टॉल केल्यानंतर, फाइन-ट्यूनिंग सेवा सुरू करण्यासाठी खालील कमांड्स वापरून पाहू शकता.

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

workspace ची स्थिती खालील कमांड चालवून ट्रॅक करता येते. जेव्हा WORKSPACEREADY कॉलम `True` होतो, तेव्हा मॉडेल यशस्वीपणे डिप्लॉय झालेले असते.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

यानंतर, इन्फरन्स सेवेसाठी क्लस्टर IP शोधून क्लस्टरमधील सेवा एंडपॉइंट तपासण्यासाठी तात्पुरता `curl` पॉड वापरू शकता.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.