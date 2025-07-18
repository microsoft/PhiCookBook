<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-07-16T20:50:18+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "pl"
}
-->
## Inference z Kaito

[Kaito](https://github.com/Azure/kaito) to operator, który automatyzuje wdrażanie modeli AI/ML do inferencji w klastrze Kubernetes.

Kaito wyróżnia się na tle większości popularnych metod wdrażania modeli opartych na infrastrukturze maszyn wirtualnych dzięki następującym cechom:

- Zarządzanie plikami modeli za pomocą obrazów kontenerów. Udostępniany jest serwer http do wykonywania wywołań inferencji z wykorzystaniem biblioteki modelu.
- Unikanie dostrajania parametrów wdrożenia pod sprzęt GPU dzięki gotowym konfiguracjom.
- Automatyczne przydzielanie węzłów GPU na podstawie wymagań modelu.
- Przechowywanie dużych obrazów modeli w publicznym Microsoft Container Registry (MCR), jeśli pozwala na to licencja.

Dzięki Kaito proces wdrażania dużych modeli AI do inferencji w Kubernetes jest znacznie uproszczony.

## Architektura

Kaito opiera się na klasycznym wzorcu projektowym Kubernetes Custom Resource Definition (CRD)/kontroler. Użytkownik zarządza niestandardowym zasobem `workspace`, który opisuje wymagania dotyczące GPU oraz specyfikację inferencji. Kontrolery Kaito automatyzują wdrożenie, synchronizując stan zasobu `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Architektura Kaito" alt="Architektura Kaito">
</div>

Powyższy rysunek przedstawia ogólny przegląd architektury Kaito. Główne jej komponenty to:

- **Kontroler workspace**: Synchronizuje niestandardowy zasób `workspace`, tworzy niestandardowe zasoby `machine` (opisane poniżej) w celu wywołania automatycznego przydzielania węzłów oraz tworzy obciążenie inferencyjne (`deployment` lub `statefulset`) na podstawie gotowych konfiguracji modelu.
- **Kontroler przydzielania węzłów**: Kontroler o nazwie *gpu-provisioner* w [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Wykorzystuje CRD `machine` pochodzący z [Karpenter](https://sigs.k8s.io/karpenter) do współpracy z kontrolerem workspace. Integruje się z API Azure Kubernetes Service (AKS), aby dodawać nowe węzły GPU do klastra AKS.
> Uwaga: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) to komponent open source. Może zostać zastąpiony innymi kontrolerami, jeśli obsługują API [Karpenter-core](https://sigs.k8s.io/karpenter).

## Instalacja

Proszę zapoznać się z instrukcją instalacji [tutaj](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Szybki start Inference Phi-3
[Przykładowy kod Inference Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

Status workspace można śledzić, wykonując poniższe polecenie. Gdy kolumna WORKSPACEREADY zmieni się na `True`, model został pomyślnie wdrożony.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Następnie można znaleźć adres IP usługi inferencyjnej w klastrze i użyć tymczasowego poda `curl`, aby przetestować punkt końcowy usługi w klastrze.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Szybki start Inference Phi-3 z adapterami

Po zainstalowaniu Kaito można wypróbować poniższe polecenia, aby uruchomić usługę inferencyjną.

[Przykładowy kod Inference Phi-3 z adapterami](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

Status workspace można śledzić, wykonując poniższe polecenie. Gdy kolumna WORKSPACEREADY zmieni się na `True`, model został pomyślnie wdrożony.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Następnie można znaleźć adres IP usługi inferencyjnej w klastrze i użyć tymczasowego poda `curl`, aby przetestować punkt końcowy usługi w klastrze.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do jak największej dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.