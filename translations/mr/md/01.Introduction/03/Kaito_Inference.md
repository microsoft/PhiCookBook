<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aca91084bc440431571e00bf30d96ab8",
  "translation_date": "2026-01-05T02:11:09+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "mr"
}
-->
## Kaito सह इन्फरन्स 

[Kaito](https://github.com/Azure/kaito) हा एक ऑपरेटर आहे जो Kubernetes क्लस्टरमध्ये AI/ML इन्फरन्स मॉडेल डिप्लॉयमेंट स्वयंचलित करतो.

Kaito मध्ये वर्चुअल मशीन इन्फ्रास्ट्रक्चरवर आधारित बहुसंख्य मुख्य प्रवाहातील मॉडेल डिप्लॉयमेंट पद्धतींपेक्षा खालील प्रमुख फरक आहेत:

- कंटेनर इमेजेस वापरून मॉडेल फाइल्स व्यवस्थापित करणे. मॉडेल लायब्ररी वापरून इन्फरन्स कॉल करण्यासाठी एक HTTP सर्व्हर प्रदान केला जातो.
- प्रिसेट कॉन्फिगरेशन्स देऊन GPU हार्डवेअरशी जुळवण्यासाठी डिप्लॉयमेंट पॅरामीटर्स ट्यून करण्याची आवश्यकता टाळणे.
- मॉडेलच्या आवश्यकता नुसार GPU नोड्स आपोआप प्रोव्हिजन करणे.
- परवाना परवानगी दिल्यास सार्वजनिक Microsoft Container Registry (MCR) मध्ये मोठ्या मॉडेल इमेजेस होस्ट केले जाऊ शकतात.

Kaito वापरून, Kubernetes मध्ये मोठ्या AI इन्फरन्स मॉडेल्सचे ऑनबोर्डिंग वर्कफ्लो प्रामुख्याने सुलभ होते.


## आर्किटेक्चर

Kaito पारंपरिक Kubernetes Custom Resource Definition(CRD)/controller डिझाइन पॅटर्नचे पालन करते. वापरकर्ता `workspace` कस्टम रिसोर्स व्यवस्थापित करतो जो GPU आवश्यकता आणि इन्फरन्स स्पेसिफिकेशन वर्णन करतो. Kaito कंट्रोलर `workspace` कस्टम रिसोर्सचे समायोजन करून डिप्लॉयमेंट स्वयंचलित करतील.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architecture" alt="KAITO RAGEngine architecture">
</div>

वरील आकृती Kaito आर्किटेक्चरचे सर्वसाधारण चित्र सादर करते. त्याचे मुख्य घटक खालीलप्रमाणे आहेत:

- **Workspace controller**: हे `workspace` कस्टम रिसोर्स समायोजित करते, नोड ऑटो-प्रोव्हिजनिंग सुरू करण्यासाठी `machine` (खाली स्पष्ट केले आहे) कस्टम रिसोर्स तयार करते, आणि मॉडेल प्रिसेट कॉन्फिगरेशन्सवर आधारित इन्फरन्स वर्कलोड (`deployment` किंवा `statefulset`) तयार करते.
- **Node provisioner controller**: या कंट्रोलरचे नाव [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) मध्ये *gpu-provisioner* आहे. हे workspace controller शी संवाद साधण्यासाठी [Karpenter](https://sigs.k8s.io/karpenter) कडून उत्पन्न झालेले `machine` CRD वापरते. ते Azure Kubernetes Service(AKS) APIs सह एकत्र काम करून AKS क्लस्टरमध्ये नवीन GPU नोड्स जोडते. 
> Note: The [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) is an open sourced component. It can be replaced by other controllers if they support [Karpenter-core](https://sigs.k8s.io/karpenter) APIs.

## इंस्टॉलेशन

कृपया इंस्टॉलेशन मार्गदर्शक [येथे](https://github.com/Azure/kaito/blob/main/docs/installation.md) तपासा.

## जलद प्रारंभ इन्फरन्स Phi-3
[नमुना कोड: इन्फरन्स Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # समायोजन आउटपुट ACR पथ
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

खालील कमांड चालवून workspace ची स्थिती ट्रॅक केली जाऊ शकते. जेव्हा WORKSPACEREADY स्तंभ `True` होतो, तेव्हा मॉडेल यशस्वीरित्या डिप्लॉय झालेले असते.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

नंतर, तुम्ही इन्फरन्स सेवाचा क्लस्टर आयपी शोधू शकता आणि क्लस्टरमधील सर्व्हिस एंडपॉईंट तपासण्यासाठी तात्पुरता `curl` पोड वापरू शकता.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## अॅडॅप्टरसह जलद प्रारंभ इन्फरन्स Phi-3

Kaito इन्स्टॉल केल्यानंतर, इन्फरन्स सेवा सुरू करण्यासाठी खालील कमांड्स वापरून पाहू शकता.

[नमुना कोड: इन्फरन्स Phi-3 अॅडॅप्टरसह](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # ट्यूनिंग आउटपुट ACR मार्ग
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

खालील कमांड चालवून workspace ची स्थिती ट्रॅक केली जाऊ शकते. जेव्हा WORKSPACEREADY स्तंभ `True` होतो, तेव्हा मॉडेल यशस्वीरित्या डिप्लॉय झालेले असते.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

नंतर, तुम्ही इन्फरन्स सेवाचा क्लस्टर आयपी शोधू शकता आणि क्लस्टरमधील सर्व्हिस एंडपॉईंट तपासण्यासाठी तात्पुरता `curl` पोड वापरू शकता.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI अनुवादन सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्न करत असलो तरी, कृपया लक्षात ठेवा की स्वयंचलित अनुवादांमध्ये चुका किंवा अपूर्णता असू शकते. मूळ भाषेतील दस्तऐवजाला अधिकृत स्रोत मानले पाहिजे. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याचा सल्ला दिला जातो. या अनुवादाच्या वापरामुळे उद्भवणार्‍या कोणत्याही गैरसमजुतींविषयी किंवा चुकीच्या अर्थनिर्वचनांबद्दल आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->