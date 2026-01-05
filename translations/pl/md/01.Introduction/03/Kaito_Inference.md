<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aca91084bc440431571e00bf30d96ab8",
  "translation_date": "2026-01-05T03:30:43+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "pl"
}
-->
## Wnioskowanie z Kaito 

[Kaito](https://github.com/Azure/kaito) jest operatorem, który automatyzuje wdrażanie modeli inferencyjnych AI/ML w klastrze Kubernetes.

Kaito ma następujące kluczowe cechy odróżniające go od większości głównych metod wdrażania modeli opartych na infrastrukturze maszyn wirtualnych:

- Zarządzanie plikami modeli za pomocą obrazów kontenerów. Udostępniony jest serwer HTTP do wykonywania wywołań inferencji przy użyciu biblioteki modelu.
- Unika konieczności dostrajania parametrów wdrożenia do sprzętu GPU dzięki udostępnionym konfiguracjom wstępnym.
- Automatyczne tworzenie węzłów GPU na podstawie wymagań modelu.
- Hostowanie dużych obrazów modeli w publicznym Microsoft Container Registry (MCR), jeśli licencja na to pozwala.

Dzięki Kaito proces wprowadzania dużych modeli inferencyjnych AI do Kubernetes jest w dużym stopniu uproszczony.


## Architektura

Kaito stosuje klasyczny wzorzec projektowy Kubernetes Custom Resource Definition(CRD)/kontrolera. Użytkownik zarządza zasobem niestandardowym `workspace`, który opisuje wymagania dotyczące GPU oraz specyfikację inferencji. Kontrolery Kaito zautomatyzują wdrożenie, dokonując rekonsyliacji zasobu niestandardowego `workspace`.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="Architektura KAITO RAGEngine" alt="Architektura KAITO RAGEngine">
</div>

Powyższa ilustracja przedstawia przegląd architektury Kaito. Jej główne komponenty to:

- **Kontroler Workspace**: Dokonuje rekonsyliacji zasobu niestandardowego `workspace`, tworzy zasoby niestandardowe `machine` (opisane poniżej), aby uruchomić automatyczne tworzenie węzłów, oraz tworzy obciążenie inferencyjne (`deployment` lub `statefulset`) na podstawie wstępnych konfiguracji modelu.
- **Kontroler provisionowania węzłów**: Nazwa kontrolera to *gpu-provisioner* w [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Używa CRD `machine` pochodzącego z [Karpenter](https://sigs.k8s.io/karpenter), aby współdziałać z kontrolerem workspace. Integruje się z interfejsami API Azure Kubernetes Service(AKS), aby dodawać nowe węzły GPU do klastra AKS. 
> Uwaga: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) jest komponentem open source. Można go zastąpić innymi kontrolerami, jeśli obsługują API [Karpenter-core](https://sigs.k8s.io/karpenter).

## Instalacja

Proszę sprawdzić wskazówki instalacyjne [tutaj](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Szybki start inferencji Phi-3
[Przykładowy kod inferencji Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Ścieżka ACR wyjścia strojenia
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

Status zasobu `workspace` można śledzić, wykonując następujące polecenie. Gdy kolumna WORKSPACEREADY zmieni się na `True`, model został pomyślnie wdrożony.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Następnie można znaleźć adres IP klastra usługi inferencyjnej i użyć tymczasowego podu `curl`, aby przetestować punkt końcowy usługi w klastrze.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Szybki start inferencji Phi-3 z adapterami

Po zainstalowaniu Kaito można wypróbować poniższe polecenia, aby uruchomić usługę inferencyjną.

[Przykładowy kod inferencji Phi-3 z adapterami](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Ścieżka wyjściowa ACR dla strojenia
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

Status zasobu `workspace` można śledzić, wykonując następujące polecenie. Gdy kolumna WORKSPACEREADY zmieni się na `True`, model został pomyślnie wdrożony.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Następnie można znaleźć adres IP klastra usługi inferencyjnej i użyć tymczasowego podu `curl`, aby przetestować punkt końcowy usługi w klastrze.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Zastrzeżenie:
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczeń opartych na sztucznej inteligencji Co-op Translator (https://github.com/Azure/co-op-translator). Chociaż dokładamy starań, aby tłumaczenie było poprawne, prosimy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło wiążące. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->