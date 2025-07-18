<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-07-16T20:53:42+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "sr"
}
-->
## Инференција са Kaitо

[Kaito](https://github.com/Azure/kaito) је оператор који аутоматизује распоређивање AI/ML инференцијских модела у Kubernetes кластеру.

Kaito има следеће кључне разлике у односу на већину уобичајених метода за распоређивање модела базираних на виртуелним машинама:

- Управљање фајловима модела помоћу контејнер слика. Пружа HTTP сервер за извођење инференцијских позива користећи библиотеку модела.
- Избегава подешавање параметара распоређивања у складу са GPU хардвером пружајући унапред дефинисане конфигурације.
- Аутоматско обезбеђивање GPU нодова у складу са захтевима модела.
- Хостовање великих слика модела у јавном Microsoft Container Registry (MCR) ако лиценца то дозвољава.

Коришћењем Kaitо-а, процес увођења великих AI инференцијских модела у Kubernetes је знатно поједностављен.

## Архитектура

Kaito прати класичан Kubernetes дизајн образац заснован на Custom Resource Definition (CRD)/контролеру. Корисник управља `workspace` прилагођеним ресурсом који описује захтеве за GPU и спецификацију инференције. Kaito контролери аутоматски распоређују ресурсе тако што усаглашавају `workspace` прилагођени ресурс.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Горња слика приказује преглед архитектуре Kaitо-а. Главне компоненте су:

- **Workspace контролер**: Усаглашава `workspace` прилагођени ресурс, креира `machine` (објашњено у наставку) прилагођене ресурсе како би покренуо аутоматско обезбеђивање нодова и креира инференцијски workload (`deployment` или `statefulset`) на основу унапред дефинисаних конфигурација модела.
- **Node provisioner контролер**: Контролер се зове *gpu-provisioner* у [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Користи `machine` CRD који потиче из [Karpenter](https://sigs.k8s.io/karpenter) за интеракцију са workspace контролером. Интегрише се са Azure Kubernetes Service (AKS) API-јима ради додавања нових GPU нодова у AKS кластер.
> Напомена: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) је отворени софтверски компонент. Може бити замењен другим контролерима ако подржавају [Karpenter-core](https://sigs.k8s.io/karpenter) API-је.

## Инсталација

Молимо проверите упутство за инсталацију [овде](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Брзи почетак инференције Phi-3
[Пример кода за инференцију Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

Статус workspace-а може се пратити покретањем следеће команде. Када колона WORKSPACEREADY постане `True`, модел је успешно распоређен.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Затим, може се пронаћи cluster IP инференцијске услуге и користити привремени `curl` под за тестирање крајње тачке услуге у кластеру.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Брзи почетак инференције Phi-3 са адаптерима

Након инсталације Kaitо-а, могу се покушати следеће команде за покретање инференцијске услуге.

[Пример кода за инференцију Phi-3 са адаптерима](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

Статус workspace-а може се пратити покретањем следеће команде. Када колона WORKSPACEREADY постане `True`, модел је успешно распоређен.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Затим, може се пронаћи cluster IP инференцијске услуге и користити привремени `curl` под за тестирање крајње тачке услуге у кластеру.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.