<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-07-09T20:07:20+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "uk"
}
-->
## Виведення з Kaito

[Kaito](https://github.com/Azure/kaito) — це оператор, який автоматизує розгортання моделей AI/ML для виведення в кластері Kubernetes.

Kaito має такі ключові відмінності порівняно з більшістю популярних методів розгортання моделей, побудованих на інфраструктурі віртуальних машин:

- Керує файлами моделей за допомогою контейнерних образів. HTTP-сервер надається для виконання викликів виведення через бібліотеку моделей.
- Уникає налаштування параметрів розгортання під конкретне GPU обладнання, пропонуючи готові конфігурації.
- Автоматично забезпечує GPU-вузли відповідно до вимог моделі.
- Розміщує великі образи моделей у публічному Microsoft Container Registry (MCR), якщо це дозволяє ліцензія.

Завдяки Kaito процес підключення великих AI моделей для виведення в Kubernetes значно спрощується.

## Архітектура

Kaito дотримується класичного патерну Kubernetes Custom Resource Definition (CRD)/controller. Користувач керує кастомним ресурсом `workspace`, який описує вимоги до GPU та специфікації виведення. Контролери Kaito автоматизують розгортання, узгоджуючи стан кастомного ресурсу `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Архітектура Kaito" alt="Архітектура Kaito">
</div>

На наведеній схемі показано огляд архітектури Kaito. Основні компоненти включають:

- **Workspace controller**: Узгоджує кастомний ресурс `workspace`, створює кастомні ресурси `machine` (описані нижче) для запуску автоматичного забезпечення вузлів, а також створює робоче навантаження для виведення (`deployment` або `statefulset`) на основі готових конфігурацій моделі.
- **Node provisioner controller**: Контролер з назвою *gpu-provisioner* у [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Використовує CRD `machine`, що походить від [Karpenter](https://sigs.k8s.io/karpenter), для взаємодії з workspace controller. Інтегрується з API Azure Kubernetes Service (AKS) для додавання нових GPU-вузлів до кластера AKS.
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) — це відкритий компонент. Його можна замінити іншими контролерами, якщо вони підтримують API [Karpenter-core](https://sigs.k8s.io/karpenter).

## Встановлення

Будь ласка, ознайомтеся з інструкцією з встановлення [тут](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Швидкий старт: Виведення Phi-3  
[Приклад коду для виведення Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

Статус workspace можна відстежувати за допомогою наступної команди. Коли у стовпці WORKSPACEREADY з’явиться `True`, модель успішно розгорнута.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Далі можна дізнатися IP-адресу сервісу виведення в кластері та використати тимчасовий pod з `curl` для тестування кінцевої точки сервісу в кластері.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Швидкий старт: Виведення Phi-3 з адаптерами

Після встановлення Kaito можна виконати наступні команди для запуску сервісу виведення.

[Приклад коду для виведення Phi-3 з адаптерами](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

Статус workspace можна відстежувати за допомогою наступної команди. Коли у стовпці WORKSPACEREADY з’явиться `True`, модель успішно розгорнута.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Далі можна дізнатися IP-адресу сервісу виведення в кластері та використати тимчасовий pod з `curl` для тестування кінцевої точки сервісу в кластері.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.