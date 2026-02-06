## Виведення з Kaito

[Kaito](https://github.com/Azure/kaito) — це оператор, який автоматизує розгортання моделей AI/ML для виведення в кластері Kubernetes.

Kaito має такі ключові відмінності в порівнянні з більшістю основних методологій розгортання моделей, побудованих на основі інфраструктури віртуальних машин:

- Керує файлами моделей за допомогою образів контейнерів. Надається HTTP-сервер для виконання викликів виведення з використанням бібліотеки моделей.
- Уникає налаштувань параметрів розгортання для підгонки під апаратне забезпечення GPU, надаючи попередньо встановлені конфігурації.
- Автоматично забезпечує GPU-вузли на основі вимог моделі.
- Розміщує великі образи моделей у публічному Microsoft Container Registry (MCR), якщо це дозволяє ліцензія.

Використовуючи Kaito, робочий процес підключення великих AI моделей для виведення в Kubernetes значно спрощується.

## Архітектура

Kaito дотримується класичного шаблону проектування Kubernetes Custom Resource Definition (CRD)/controller. Користувач керує користувацьким ресурсом `workspace`, який описує вимоги до GPU та специфікацію виведення. Контролери Kaito автоматизують розгортання шляхом узгодження користувацького ресурсу `workspace`.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architecture" alt="KAITO RAGEngine architecture">
</div>

На наведеному малюнку зображено огляд архітектури Kaito. Її основні компоненти складаються з:

- **Контролер workspace**: він узгоджує користувацький ресурс `workspace`, створює користувацькі ресурси `machine` (пояснено нижче) для ініціювання автоматичного забезпечення вузлів та створює робоче навантаження для виведення (`deployment` або `statefulset`) на основі попередньо встановлених конфігурацій моделі.
- **Контролер забезпечення вузлів**: ім'я контролера — *gpu-provisioner* у [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Він використовує CRD `machine`, що походить від [Karpenter](https://sigs.k8s.io/karpenter), для взаємодії з контролером workspace. Інтегрується з Azure Kubernetes Service (AKS) API для додавання нових GPU-вузлів до кластера AKS.
> Примітка: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) — це компонент з відкритим вихідним кодом. Його можна замінити іншими контролерами, якщо вони підтримують API [Karpenter-core](https://sigs.k8s.io/karpenter).

## Встановлення

Будь ласка, перегляньте інструкції з встановлення [тут](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Швидкий початок: виведення Phi-3  
[Приклад коду виведення Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Налаштування шляху вихідного ACR
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

Статус workspace можна відстежувати, виконавши таку команду. Коли стовпець WORKSPACEREADY стане `True`, модель успішно розгорнута.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Далі можна знайти IP-адресу служби виведення в кластері та за допомогою тимчасового `curl` pod протестувати кінцеву точку сервісу в кластері.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Швидкий початок: виведення Phi-3 з адаптерами

Після встановлення Kaito можна спробувати виконати такі команди, щоб запустити сервіс виведення.

[Приклад коду виведення Phi-3 з адаптерами](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Налаштування вихідного шляху ACR
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

Статус workspace можна відстежувати, виконавши таку команду. Коли стовпець WORKSPACEREADY стане `True`, модель успішно розгорнута.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Далі можна знайти IP-адресу служби виведення в кластері та за допомогою тимчасового `curl` pod протестувати кінцеву точку сервісу в кластері.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено з використанням сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, зверніть увагу, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом інформації. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->