<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-07-17T06:22:25+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "th"
}
-->
## การปรับแต่งด้วย Kaito

[Kaito](https://github.com/Azure/kaito) คือ operator ที่ช่วยอัตโนมัติการติดตั้งโมเดล AI/ML สำหรับการทำ inference ในคลัสเตอร์ Kubernetes

Kaito มีความแตกต่างสำคัญเมื่อเทียบกับวิธีการติดตั้งโมเดลทั่วไปที่ใช้โครงสร้างพื้นฐานแบบเครื่องเสมือน (virtual machine) ดังนี้:

- จัดการไฟล์โมเดลโดยใช้ container images พร้อมให้บริการ http server สำหรับเรียกใช้งาน inference ผ่านไลบรารีโมเดล
- ไม่ต้องปรับแต่งพารามิเตอร์การติดตั้งให้เหมาะกับฮาร์ดแวร์ GPU โดยมีการตั้งค่าล่วงหน้าให้แล้ว
- จัดเตรียมโหนด GPU อัตโนมัติตามความต้องการของโมเดล
- โฮสต์ภาพโมเดลขนาดใหญ่ใน Microsoft Container Registry (MCR) สาธารณะ หากใบอนุญาตอนุญาตให้ทำได้

ด้วย Kaito กระบวนการนำโมเดล AI inference ขนาดใหญ่เข้าสู่ Kubernetes จะง่ายขึ้นมาก


## สถาปัตยกรรม

Kaito ใช้รูปแบบการออกแบบ Kubernetes Custom Resource Definition (CRD) และ controller แบบคลาสสิก ผู้ใช้จะจัดการ custom resource ชื่อ `workspace` ซึ่งระบุความต้องการ GPU และสเปคของการทำ inference ตัวควบคุมของ Kaito จะช่วยอัตโนมัติการติดตั้งโดยการประสานงานกับ custom resource `workspace`
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

ภาพด้านบนแสดงภาพรวมสถาปัตยกรรมของ Kaito ส่วนประกอบหลักประกอบด้วย:

- **Workspace controller**: ทำหน้าที่ประสานงานกับ custom resource `workspace` สร้าง custom resource `machine` (อธิบายด้านล่าง) เพื่อกระตุ้นการจัดเตรียมโหนดอัตโนมัติ และสร้างงาน inference (`deployment` หรือ `statefulset`) ตามการตั้งค่าล่วงหน้าของโมเดล
- **Node provisioner controller**: ตัวควบคุมนี้ชื่อ *gpu-provisioner* ใน [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) ใช้ `machine` CRD ที่มาจาก [Karpenter](https://sigs.k8s.io/karpenter) เพื่อสื่อสารกับ workspace controller และเชื่อมต่อกับ Azure Kubernetes Service (AKS) API เพื่อเพิ่มโหนด GPU ใหม่ในคลัสเตอร์ AKS
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) เป็นส่วนประกอบแบบโอเพนซอร์ส สามารถแทนที่ด้วยตัวควบคุมอื่นได้หากรองรับ [Karpenter-core](https://sigs.k8s.io/karpenter) API

## วิดีโอภาพรวม  
[ชมการสาธิต Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## การติดตั้ง

โปรดดูคำแนะนำการติดตั้งได้ที่ [นี่](https://github.com/Azure/kaito/blob/main/docs/installation.md)

## เริ่มต้นอย่างรวดเร็ว

หลังจากติดตั้ง Kaito แล้ว สามารถลองใช้คำสั่งต่อไปนี้เพื่อเริ่มบริการปรับแต่งโมเดล

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

สถานะของ workspace สามารถตรวจสอบได้โดยใช้คำสั่งด้านล่าง เมื่อคอลัมน์ WORKSPACEREADY แสดงค่า `True` หมายความว่าโมเดลถูกติดตั้งเรียบร้อยแล้ว

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

จากนั้น สามารถค้นหา cluster ip ของบริการ inference และใช้ pod ชั่วคราวที่ชื่อ `curl` เพื่อทดสอบ endpoint ของบริการในคลัสเตอร์ได้

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดขึ้นจากการใช้การแปลนี้