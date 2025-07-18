<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-07-16T20:49:12+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "mr"
}
-->
## Kaito सह अनुमान

[Kaito](https://github.com/Azure/kaito) हा एक ऑपरेटर आहे जो Kubernetes क्लस्टरमध्ये AI/ML अनुमान मॉडेल तैनात करण्याचे स्वयंचलितीकरण करतो.

Kaito मध्ये बहुतेक मुख्य प्रवाहातील मॉडेल तैनाती पद्धतींपेक्षा खालील महत्त्वाचे फरक आहेत, जे वर्चुअल मशीन इन्फ्रास्ट्रक्चरवर आधारित आहेत:

- कंटेनर इमेजेस वापरून मॉडेल फाइल्स व्यवस्थापित करा. मॉडेल लायब्ररी वापरून अनुमान कॉल करण्यासाठी http सर्व्हर प्रदान केला जातो.
- GPU हार्डवेअरशी जुळवून घेण्यासाठी तैनातीचे पॅरामीटर्स ट्यून करण्याची गरज नाही, कारण पूर्वनिर्धारित कॉन्फिगरेशन दिलेले आहे.
- मॉडेलच्या गरजेनुसार GPU नोड्स आपोआप पुरवठा करा.
- परवानगी असल्यास मोठ्या मॉडेल इमेजेस सार्वजनिक Microsoft Container Registry (MCR) मध्ये होस्ट करा.

Kaito वापरून, Kubernetes मध्ये मोठ्या AI अनुमान मॉडेल्सचे ऑनबोर्डिंग कार्यप्रवाह मोठ्या प्रमाणात सुलभ होते.

## आर्किटेक्चर

Kaito पारंपरिक Kubernetes Custom Resource Definition(CRD)/controller डिझाइन पॅटर्नचे पालन करतो. वापरकर्ता `workspace` नावाचा कस्टम रिसोर्स व्यवस्थापित करतो जो GPU गरजा आणि अनुमान तपशील वर्णन करतो. Kaito कंट्रोलर्स `workspace` कस्टम रिसोर्सचे समन्वय करून तैनाती स्वयंचलित करतात.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

वरील आकृती Kaito आर्किटेक्चरचा आढावा दर्शवते. त्याचे मुख्य घटक खालीलप्रमाणे आहेत:

- **Workspace controller**: हा `workspace` कस्टम रिसोर्सचे समन्वय करतो, नोड ऑटो प्रोव्हिजनिंगसाठी `machine` (खाली समजावलेले) कस्टम रिसोर्स तयार करतो, आणि मॉडेलच्या पूर्वनिर्धारित कॉन्फिगरेशननुसार अनुमान वर्कलोड (`deployment` किंवा `statefulset`) तयार करतो.
- **Node provisioner controller**: या कंट्रोलरचे नाव [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) मध्ये *gpu-provisioner* आहे. हा `machine` CRD वापरतो जो [Karpenter](https://sigs.k8s.io/karpenter) कडून आला आहे आणि workspace controller शी संवाद साधतो. तो Azure Kubernetes Service(AKS) API सह एकत्रित होऊन AKS क्लस्टरमध्ये नवीन GPU नोड्स जोडतो.
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) हा एक मुक्त स्रोत घटक आहे. जर इतर कंट्रोलर्स [Karpenter-core](https://sigs.k8s.io/karpenter) API ला समर्थन देत असतील तर त्याने तो बदलता येऊ शकतो.

## स्थापना

कृपया स्थापना मार्गदर्शन [येथे](https://github.com/Azure/kaito/blob/main/docs/installation.md) तपासा.

## जलद प्रारंभ अनुमान Phi-3
[नमुना कोड अनुमान Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Tuning Output ACR Path
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

खालील कमांड चालवून workspace ची स्थिती तपासू शकता. जेव्हा WORKSPACEREADY कॉलम `True` होतो, तेव्हा मॉडेल यशस्वीपणे तैनात झालेले असते.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

यानंतर, अनुमान सेवेसाठी क्लस्टर आयपी शोधून क्लस्टरमधील सेवा एंडपॉइंट तपासण्यासाठी तात्पुरता `curl` pod वापरू शकता.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## जलद प्रारंभ अनुमान Phi-3 अ‍ॅडॉप्टर्ससह

Kaito स्थापित केल्यानंतर, खालील कमांड वापरून अनुमान सेवा सुरू करू शकता.

[नमुना कोड अनुमान Phi-3 अ‍ॅडॉप्टर्ससह](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Tuning Output ACR Path
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

खालील कमांड चालवून workspace ची स्थिती तपासू शकता. जेव्हा WORKSPACEREADY कॉलम `True` होतो, तेव्हा मॉडेल यशस्वीपणे तैनात झालेले असते.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

यानंतर, अनुमान सेवेसाठी क्लस्टर आयपी शोधून क्लस्टरमधील सेवा एंडपॉइंट तपासण्यासाठी तात्पुरता `curl` pod वापरू शकता.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.