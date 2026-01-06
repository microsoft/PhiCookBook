<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aca91084bc440431571e00bf30d96ab8",
  "translation_date": "2026-01-05T12:19:40+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "th"
}
-->
## การอนุมานด้วย Kaito

[Kaito](https://github.com/Azure/kaito) เป็นโอเปอเรเตอร์ที่ช่วยอัตโนมัติการปรับใช้งานโมเดล AI/ML สำหรับการอนุมานในคลัสเตอร์ Kubernetes

Kaito มีความแตกต่างสำคัญดังต่อไปนี้เมื่อเทียบกับวิธีการปรับใช้โมเดลที่เป็นกระแสหลักส่วนใหญ่ซึ่งสร้างมาบนโครงสร้างพื้นฐานของเครื่องเสมือน:

- จัดการไฟล์โมเดลโดยใช้ภาพคอนเทนเนอร์ เซิร์ฟเวอร์ http ถูกจัดเตรียมเพื่อดำเนินการเรียกอนุมานโดยใช้ไลบรารีโมเดล
- หลีกเลี่ยงการปรับแต่งพารามิเตอร์การปรับใช้ให้เหมาะสมกับฮาร์ดแวร์ GPU โดยให้การกำหนดค่าล่วงหน้า
- จัดเตรียมโหนด GPU อัตโนมัติตามความต้องการของโมเดล
- โฮสต์ภาพโมเดลขนาดใหญ่ใน Microsoft Container Registry (MCR) สาธารณะ หากใบอนุญาตอนุญาต

ด้วย Kaito เวิร์กโฟลว์ของการนำโมเดล AI สำหรับอนุมานขนาดใหญ่มาใช้ใน Kubernetes จะง่ายขึ้นอย่างมาก


## สถาปัตยกรรม

Kaito ปฏิบัติตามรูปแบบการออกแบบคลาสสิกของ Kubernetes Custom Resource Definition(CRD)/controller ผู้ใช้จัดการทรัพยากรแบบกำหนดเอง `workspace` ซึ่งอธิบายความต้องการ GPU และข้อกำหนดการอนุมาน ตัวควบคุม Kaito จะดำเนินการปรับใช้โดยการกระทบยอดทรัพยากรแบบกำหนดเอง `workspace`

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architecture" alt="KAITO RAGEngine architecture">
</div>

รูปภาพข้างต้นนำเสนอภาพรวมสถาปัตยกรรมของ Kaito ส่วนประกอบหลักประกอบด้วย:

- **ตัวควบคุม Workspace**: กระทบยอดทรัพยากรแบบกำหนดเอง `workspace` สร้างทรัพยากรแบบกำหนดเอง `machine` (อธิบายด้านล่าง) เพื่อกระตุ้นการจัดเตรียมโหนดอัตโนมัติ และสร้างงานอนุมาน (`deployment` หรือ `statefulset`) ตามการกำหนดค่าล่วงหน้าของโมเดล
- **ตัวควบคุมตัวจัดหาโหนด**: ตัวควบคุมนี้มีชื่อว่า *gpu-provisioner* ใน [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) ใช้ CRD `machine` ที่มาจาก [Karpenter](https://sigs.k8s.io/karpenter) เพื่อติดต่อกับตัวควบคุม workspace มันรวมกับ Azure Kubernetes Service(AKS) APIs เพื่อเพิ่มโหนด GPU ใหม่ไปยังคลัสเตอร์ AKS 
> หมายเหตุ: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) เป็นคอมโพเนนต์แบบโอเพนซอร์ส สามารถแทนที่ด้วยตัวควบคุมอื่นถ้ารองรับ APIs ของ [Karpenter-core](https://sigs.k8s.io/karpenter)

## การติดตั้ง

โปรดตรวจสอบคำแนะนำการติดตั้งได้ที่ [นี่](https://github.com/Azure/kaito/blob/main/docs/installation.md)

## เริ่มต้นอย่างรวดเร็วกับ Inference Phi-3
[ตัวอย่างโค้ด Inference Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # ปรับแต่งเส้นทางเอาต์พุต ACR
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

สถานะของ workspace สามารถติดตามได้โดยรันคำสั่งดังต่อไปนี้ เมื่อคอลัมน์ WORKSPACEREADY เป็น `True` แสดงว่าโมเดลถูกปรับใช้เรียบร้อยแล้ว

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

ถัดไป สามารถค้นหาไอพีคลัสเตอร์ของบริการอนุมานและใช้ pod `curl` ชั่วคราวเพื่อทดสอบ endpoint ของบริการภายในคลัสเตอร์ได้

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## เริ่มต้นอย่างรวดเร็วกับ Inference Phi-3 พร้อมอะแดปเตอร์

หลังจากติดตั้ง Kaito แล้ว สามารถลองใช้คำสั่งต่อไปนี้เพื่อเริ่มบริการอนุมาน

[ตัวอย่างโค้ด Inference Phi-3 พร้อมอะแดปเตอร์](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # ปรับแต่งเส้นทาง ACR เอาต์พุต
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

สถานะของ workspace สามารถติดตามได้โดยรันคำสั่งดังต่อไปนี้ เมื่อคอลัมน์ WORKSPACEREADY เป็น `True` แสดงว่าโมเดลถูกปรับใช้เรียบร้อยแล้ว

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

ถัดไป สามารถค้นหาไอพีคลัสเตอร์ของบริการอนุมานและใช้ pod `curl` ชั่วคราวเพื่อทดสอบ endpoint ของบริการภายในคลัสเตอร์ได้

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:
เอกสารฉบับนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้ความแม่นยำสูงสุด โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความคลาดเคลื่อน เอกสารต้นฉบับในภาษาต้นฉบับถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลสำคัญแนะนำให้ใช้บริการแปลโดยมนุษย์มืออาชีพ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดใด ๆ ที่เกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->