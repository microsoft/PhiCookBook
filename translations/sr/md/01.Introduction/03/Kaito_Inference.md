## Инференција са Kaitom

[Kaito](https://github.com/Azure/kaito) је оператор који аутоматизује деплојмент AI/ML инференс модела у Kubernetes кластери.

Kaito има следеће кључне разлике у односу на већину доминантних методологија за деплојмент модела изграђених на врху инфраструктура базираних на виртуелним машинама:

- Управља фајловима модела користећи контејнерске слике. Пружа се http сервер за извођење инференс позива користећи библиотеку модела.
- Избегава постављање параметара деплојмента у складу са GPU хардвером пружајући унапред подешене конфигурације.
- Ауто-провиђе GPU чворове на основу захтева модела.
- Држи велике слике модела у јавној Microsoft Container Registry (MCR) ако то лиценца дозвољава.

Коришћењем Kaitoa, радни ток увођења великих AI инференс модела у Kubernetes је знатно поједностављен.


## Архитектура

Kaito прати класичан дизајн образац Kubernetes Custom Resource Definition (CRD)/controller. Корисник управља `workspace` прилагођеним ресурсом који описује GPU захтеве и спецификацију инференс-а. Kaito контролери ће аутоматизовати деплојмент решавањем `workspace` прилагођеног ресурса.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine архитектура" alt="KAITO RAGEngine архитектура">
</div>

Горња слика представља преглед Kaitove архитектуре. Њене главне компоненте су:

- **Workspace controller**: Решава `workspace` прилагођени ресурс, креира `machine` (објашњено испод) прилагођене ресурсе да покрене ауто провизију чворова, и креира инференс радно оптерећење (`deployment` или `statefulset`) на основу унапред подешених конфигурација модела.
- **Node provisioner controller**: Назив контролера је *gpu-provisioner* у [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Користи `machine` CRD који потиче из [Karpenter](https://sigs.k8s.io/karpenter) да би комуницирао са workspace контролером. Интегрише се са Azure Kubernetes Service (AKS) API-јима да дода нове GPU чворове на AKS кластер.
> Напомена: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) је компонентa са отвореним кодом. Може бити замењена другим контролерима ако они подржавају [Karpenter-core](https://sigs.k8s.io/karpenter) API-је.

## Инсталација

Молимо проверите упутство за инсталацију [овде](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Брзи почетак Inference Phi-3
[Пример кода Inference Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Постављање путање излаза ACR
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

Статус workspace-а може се пратити покретањем следеће команде. Када колона WORKSPACEREADY постане `True`, модел је успешно деплојован.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Следеће, може се пронаћи cluster ip инференс сервиса и користити привремени `curl` под за тестирање сервисног енпојнта у кластери.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Брзи почетак Inference Phi-3 са адаптерима

Након инсталације Kaitoa, може се извршити следеће команде за покретање инференс сервиса.

[Пример кода Inference Phi-3 са адаптерима](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Подешавање излазног АЦР пута
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

Статус workspace-а може се пратити покретањем следеће команде. Када колона WORKSPACEREADY постане `True`, модел је успешно деплојован.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Следеће, може се пронаћи cluster ip инференс сервиса и користити привремени `curl` под за тестирање сервисног енпојнта у кластери.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Одрицање од одговорности**:
Овај документ је преведен уз помоћ AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се стручни људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->