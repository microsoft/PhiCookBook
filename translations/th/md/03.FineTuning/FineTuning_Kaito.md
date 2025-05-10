<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-05-09T20:40:49+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "th"
}
-->
## การปรับแต่งด้วย Kaito

[Kaito](https://github.com/Azure/kaito) คือ operator ที่ช่วยอัตโนมัติในการดีพลอยโมเดล AI/ML inference ใน Kubernetes cluster

Kaito มีความแตกต่างสำคัญเมื่อเทียบกับวิธีการดีพลอยโมเดลหลักๆ ที่สร้างบนโครงสร้างพื้นฐานของ virtual machine ดังนี้:

- จัดการไฟล์โมเดลโดยใช้ container images พร้อมเซิร์ฟเวอร์ http สำหรับเรียกใช้งาน inference ผ่านไลบรารีโมเดล
- ไม่ต้องปรับแต่งพารามิเตอร์การดีพลอยให้เข้ากับฮาร์ดแวร์ GPU ด้วยการตั้งค่าที่เตรียมไว้ล่วงหน้า
- จัดสรร GPU nodes อัตโนมัติตามความต้องการของโมเดล
- โฮสต์ภาพโมเดลขนาดใหญ่ใน Microsoft Container Registry (MCR) สาธารณะได้หากใบอนุญาตอนุญาต

ด้วย Kaito กระบวนการนำโมเดล AI inference ขนาดใหญ่เข้าสู่ Kubernetes จะง่ายขึ้นอย่างมาก

## สถาปัตยกรรม

Kaito ใช้รูปแบบการออกแบบ Kubernetes Custom Resource Definition (CRD)/controller แบบคลาสสิก ผู้ใช้จัดการกับ `workspace` custom resource ที่อธิบายความต้องการ GPU และสเปคของ inference โดย Kaito controllers จะทำการดีพลอยโดยอัตโนมัติผ่านการประสาน `workspace` custom resource
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

ภาพด้านบนแสดงภาพรวมสถาปัตยกรรมของ Kaito โดยส่วนประกอบหลักประกอบด้วย:

- **Workspace controller**: ทำการประสาน `workspace` custom resource สร้าง `machine` (อธิบายด้านล่าง) custom resources เพื่อเรียกใช้การจัดสรร node อัตโนมัติ และสร้าง inference workload (`deployment` หรือ `statefulset`) ตามการตั้งค่าโมเดลที่เตรียมไว้ล่วงหน้า
- **Node provisioner controller**: ชื่อ controller คือ *gpu-provisioner* ใน [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) ใช้ `machine` CRD ที่มาจาก [Karpenter](https://sigs.k8s.io/karpenter) เพื่อสื่อสารกับ workspace controller และเชื่อมต่อกับ Azure Kubernetes Service (AKS) APIs เพื่อเพิ่ม GPU nodes ใหม่ใน AKS cluster  
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) เป็นคอมโพเนนต์โอเพนซอร์ส สามารถแทนที่ด้วย controller อื่นได้ถ้ารองรับ [Karpenter-core](https://sigs.k8s.io/karpenter) APIs

## วิดีโอภาพรวม  
[ดู Kaito Demo](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## การติดตั้ง

โปรดดูคำแนะนำการติดตั้งได้ที่ [ที่นี่](https://github.com/Azure/kaito/blob/main/docs/installation.md)

## เริ่มต้นอย่างรวดเร็ว

หลังจากติดตั้ง Kaito แล้ว สามารถลองใช้คำสั่งต่อไปนี้เพื่อเริ่มบริการ fine-tuning

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

สถานะของ workspace สามารถติดตามได้โดยรันคำสั่งด้านล่าง เมื่อคอลัมน์ WORKSPACEREADY แสดงค่า `True` หมายความว่าโมเดลถูกดีพลอยเรียบร้อยแล้ว

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

ถัดไป สามารถหาคลัสเตอร์ IP ของบริการ inference และใช้ pod ชั่วคราวที่ชื่อ `curl` เพื่อทดสอบจุดเชื่อมต่อของบริการในคลัสเตอร์ได้

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความคลาดเคลื่อนได้ เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลสำคัญ ขอแนะนำให้ใช้บริการแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดขึ้นจากการใช้การแปลนี้