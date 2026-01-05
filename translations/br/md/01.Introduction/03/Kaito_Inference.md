<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aca91084bc440431571e00bf30d96ab8",
  "translation_date": "2026-01-05T14:14:02+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "br"
}
-->
## Inferência com Kaito 

[Kaito](https://github.com/Azure/kaito) é um operador que automatiza o deployment de modelos de inferência AI/ML em um cluster Kubernetes.

Kaito possui as seguintes diferenciações chave comparado à maioria das metodologias principais de deployment de modelos construídas sobre infraestruturas de máquinas virtuais:

- Gerencia arquivos do modelo usando imagens de container. Um servidor http é fornecido para realizar chamadas de inferência usando a biblioteca do modelo.
- Evita ajuste de parâmetros de deployment para se adequar ao hardware de GPU fornecendo configurações predefinidas.
- Auto-provisiona nós de GPU baseados nos requisitos do modelo.
- Hospeda grandes imagens de modelo no Registro Público de Contêineres da Microsoft (MCR) se a licença permitir.

Usando Kaito, o fluxo de trabalho para onboarding de grandes modelos de inferência AI no Kubernetes é amplamente simplificado.


## Arquitetura

Kaito segue o padrão clássico de design Kubernetes Custom Resource Definition(CRD)/controller. O usuário gerencia um recurso customizado `workspace` que descreve os requisitos da GPU e a especificação da inferência. Os controladores Kaito irão automatizar o deployment ao reconciliar o recurso customizado `workspace`.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architecture" alt="KAITO RAGEngine architecture">
</div>

A figura acima apresenta a visão geral da arquitetura do Kaito. Seus principais componentes consistem em:

- **Controlador Workspace**: Reconcilia o recurso customizado `workspace`, cria recursos customizados `machine` (explicados abaixo) para acionar o auto provisionamento de nós, e cria a carga de trabalho de inferência (`deployment` ou `statefulset`) baseado nas configurações predefinidas do modelo.
- **Controlador provisionador de nós**: O nome do controlador é *gpu-provisioner* no [chart helm gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Ele usa o CRD `machine` originado do [Karpenter](https://sigs.k8s.io/karpenter) para interagir com o controlador workspace. Ele integra-se com as APIs do Azure Kubernetes Service(AKS) para adicionar novos nós GPU ao cluster AKS. 
> Nota: O [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) é um componente open source. Ele pode ser substituído por outros controladores se eles suportarem as APIs [Karpenter-core](https://sigs.k8s.io/karpenter).

## Instalação

Por favor, verifique as orientações de instalação [aqui](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Início rápido Inferência Phi-3
[Código de Exemplo Inferência Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Ajustando o Caminho ACR de Saída
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

O status do workspace pode ser acompanhado executando o seguinte comando. Quando a coluna WORKSPACEREADY se tornar `True`, o modelo foi implantado com sucesso.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Em seguida, pode-se encontrar o IP do cluster do serviço de inferência e usar um pod temporário `curl` para testar o endpoint do serviço no cluster.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Início rápido Inferência Phi-3 com adaptadores

Após instalar o Kaito, pode-se tentar os comandos a seguir para iniciar um serviço de inferência.

[Código de Exemplo Inferência Phi-3 com Adaptadores](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Ajustando o Caminho de Saída ACR
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

O status do workspace pode ser acompanhado executando o seguinte comando. Quando a coluna WORKSPACEREADY se tornar `True`, o modelo foi implantado com sucesso.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Em seguida, pode-se encontrar o IP do cluster do serviço de inferência e usar um pod temporário `curl` para testar o endpoint do serviço no cluster.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional realizada por um tradutor humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->