## Kaito सह अनुमान

[Kaito](https://github.com/Azure/kaito) हा एक ऑपरेटर आहे जो Kubernetes क्लस्टरमध्ये AI/ML अनुमान मॉडेल तैनाती स्वयंचलित करतो.

Kaito मध्ये खालील मुख्य फरक आहेत जे बहुसंख्य प्रमुख मॉडेल तैनात करण्याच्या पद्धतींपेक्षा वेगळे आहेत जे आभासी मशीन इन्फ्रास्ट्रक्चरवर आधारित आहेत:

- कंटेनर इमेजेस वापरून मॉडेल फाईल्स व्यवस्थापित करा. मॉडेल लायब्ररी वापरून अनुमान कॉल करण्यासाठी एक http सर्व्हर दिला आहे.
- GPU हार्डवेअरशी जुळवण्यासाठी तैनात करण्याचे पॅरामीटर्स ट्यून करण्याचे टाळा, पूर्वनिर्धारित कॉन्फिगरेशन प्रदान करून.
- मॉडेल आवश्यकतांनुसार GPU नोड्स आपोआप उपलब्ध करा.
- परवानगी असल्यास मोठ्या मॉडेल इमेजेस Microsoft Container Registry (MCR) मध्ये होस्ट करा.

Kaito वापरून, Kubernetes मध्ये मोठ्या AI अनुमान मॉडेल्सचे ऑनबोर्डिंग कार्यप्रवाह मोठ्या प्रमाणात सुलभ होते.


## आर्किटेक्चर

Kaito पारंपरिक Kubernetes कस्टम रिसोर्स डिफिनिशन(CRD)/कंट्रोलर डिझाइन पॅटर्नचे पालन करते. वापरकर्ता GPU आवश्यकतांचे आणि अनुमान तपशीलांचे वर्णन करणारा `workspace` कस्टम रिसोर्स व्यवस्थापित करतो. Kaito कंट्रोलर्स `workspace` कस्टम रिसोर्सची एकत्रित तपासणी करून तैनात करण्याचे स्वयंचलन करेल.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architecture" alt="KAITO RAGEngine architecture">
</div>

वरील आकृती Kaito आर्किटेक्चरचे सारांश दर्शवते. त्याचे प्रमुख घटक पुढीलप्रमाणे आहेत:

- **Workspace कंट्रोलर**: तो `workspace` कस्टम रिसोर्सची एकत्रित तपासणी करतो, नोड आपोआप पुरवठा सुरू करण्यासाठी `machine` (खाली समजावलेले) कस्टम रिसोर्स तयार करतो, आणि मॉडेलच्या पूर्वनिर्धारित कॉन्फिगरेशन नुसार अनुमान वर्कलोड (`deployment` किंवा `statefulset`) तयार करतो.
- **Node provisioner कंट्रोलर**: कंट्रोलरचे नाव [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) मध्ये *gpu-provisioner* आहे. तो Karpenter कडून घेतलेला `machine` CRD वापरून workspace कंट्रोलरशी संवाद साधतो. तो Azure Kubernetes Service(AKS) APIs सोबत एकत्र होऊन AKS क्लस्टरमध्ये नवीन GPU नोड्स जोडतो.
> नोंद: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) हा एक मुक्त स्त्रोत घटक आहे. तो अन्य कंट्रोलर्सने बदला जाऊ शकतो, जे [Karpenter-core](https://sigs.k8s.io/karpenter) APIsना सपोर्ट करतात.

## स्थापना

कृपया स्थापना मार्गदर्शन [येथे](https://github.com/Azure/kaito/blob/main/docs/installation.md) तपासा.

## जलद सुरुवात Inference Phi-3
[नमुना कोड Inference Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # आउटपुट ACR मार्ग ट्यून करत आहे
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

खालील कमांड चालवून workspace स्थिती ट्रॅक करता येते. जेव्हा WORKSPACEREADY कॉलम `True` होतो, तेव्हा मॉडेल यशस्वीरित्या तैनात झालेले असते.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

यानंतर, अनुमान सेव्हिसचा क्लस्टर ip शोधून क्लस्टरमधील सेव्हिस एंडपॉइंटची चाचणी करण्यासाठी तात्पुरता `curl` पॉड वापरता येतो.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## जलद सुरुवात Inference Phi-3 अ‍ॅडॉप्टर्ससह

Kaito स्थापित केल्यानंतर, खालील कमांड वापरून अनुमान सेवा सुरु करू शकतो.

[नमुना कोड Inference Phi-3 अ‍ॅडॉप्टर्ससह](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # आउटपुट ACR पथ ट्यून करणे
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

खालील कमांड चालवून workspace स्थिती ट्रॅक करता येते. जेव्हा WORKSPACEREADY कॉलम `True` होतो, तेव्हा मॉडेल यशस्वीरित्या तैनात झालेले असते.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

यानंतर, अनुमान सेव्हिसचा क्लस्टर ip शोधून क्लस्टरमधील सेव्हिस एंडपॉइंटची चाचणी करण्यासाठी तात्पुरता `curl` पॉड वापरता येतो.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**सरणीपत्रक**:
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील आहोत, तरी कृपया लक्षात ठेवा की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेतील त्रुटी असू शकतात. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत म्हणून मानले जावे. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद केलेला असल्यास उत्तम. या अनुवादाच्या वापरामुळे उद्भवणार्‍या कोणत्याही गैरसमजुतीसाठी किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->