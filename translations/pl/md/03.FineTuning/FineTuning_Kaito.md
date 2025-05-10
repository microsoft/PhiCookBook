<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-05-09T20:40:16+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "pl"
}
-->
## Fine-Tuning z Kaito

[Kaito](https://github.com/Azure/kaito) to operator, który automatyzuje wdrażanie modeli AI/ML do inferencji w klastrze Kubernetes.

Kaito wyróżnia się na tle większości popularnych metod wdrażania modeli opartych na infrastrukturze maszyn wirtualnych dzięki następującym cechom:

- Zarządzanie plikami modeli za pomocą obrazów kontenerów. Udostępniany jest serwer http do wykonywania wywołań inferencyjnych z wykorzystaniem biblioteki modeli.
- Unikanie dostrajania parametrów wdrożenia pod sprzęt GPU dzięki gotowym konfiguracjom.
- Automatyczne przydzielanie węzłów GPU na podstawie wymagań modelu.
- Hostowanie dużych obrazów modeli w publicznym Microsoft Container Registry (MCR), jeśli pozwala na to licencja.

Dzięki Kaito proces wdrażania dużych modeli AI do inferencji w Kubernetes jest znacznie uproszczony.

## Architektura

Kaito opiera się na klasycznym wzorcu projektowym Kubernetes Custom Resource Definition (CRD)/kontroler. Użytkownik zarządza zasobem niestandardowym `workspace`, który opisuje wymagania dotyczące GPU oraz specyfikację inferencji. Kontrolery Kaito automatyzują wdrożenie poprzez uzgadnianie zasobu niestandardowego `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Architektura Kaito" alt="Architektura Kaito">
</div>

Powyższy rysunek przedstawia przegląd architektury Kaito. Główne jej elementy to:

- **Kontroler Workspace**: Uzgadnia zasób niestandardowy `workspace`, tworzy zasoby niestandardowe `machine` (opisane poniżej) w celu wywołania automatycznego przydzielania węzłów oraz tworzy obciążenie inferencyjne (`deployment` lub `statefulset`) na podstawie gotowych konfiguracji modelu.
- **Kontroler przydzielania węzłów**: Kontroler nazywa się *gpu-provisioner* w [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Wykorzystuje CRD `machine` pochodzący z [Karpenter](https://sigs.k8s.io/karpenter) do komunikacji z kontrolerem workspace. Integruje się z API Azure Kubernetes Service (AKS), aby dodawać nowe węzły GPU do klastra AKS.
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) jest komponentem open source. Może zostać zastąpiony przez inne kontrolery, jeśli obsługują API [Karpenter-core](https://sigs.k8s.io/karpenter).

## Film przeglądowy  
[Obejrzyj demo Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Instalacja

Proszę sprawdzić instrukcję instalacji [tutaj](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Szybki start

Po zainstalowaniu Kaito można wypróbować poniższe polecenia, aby uruchomić usługę fine-tuningu.

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

Status workspace można śledzić za pomocą następującego polecenia. Gdy kolumna WORKSPACEREADY stanie się `True`, model został pomyślnie wdrożony.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Następnie można znaleźć adres IP klastra usługi inferencyjnej i użyć tymczasowego poda `curl`, aby przetestować punkt końcowy usługi w klastrze.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą automatycznej usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku źródłowym powinien być traktowany jako źródło wiążące. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.