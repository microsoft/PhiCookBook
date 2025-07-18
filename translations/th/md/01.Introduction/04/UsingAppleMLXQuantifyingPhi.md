<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-07-16T21:55:16+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "th"
}
-->
# **การควอนไทซ์ Phi-3.5 ด้วย Apple MLX Framework**

MLX คือเฟรมเวิร์กอาร์เรย์สำหรับงานวิจัยด้านการเรียนรู้ของเครื่องบน Apple silicon พัฒนาโดยทีมวิจัยการเรียนรู้ของเครื่องของ Apple

MLX ถูกออกแบบโดยนักวิจัยการเรียนรู้ของเครื่องเพื่อให้นักวิจัยการเรียนรู้ของเครื่องใช้งานได้ง่าย เฟรมเวิร์กนี้เน้นความเป็นมิตรกับผู้ใช้ แต่ยังคงประสิทธิภาพสูงในการฝึกสอนและใช้งานโมเดล การออกแบบของเฟรมเวิร์กเองก็เรียบง่ายในเชิงแนวคิด เราตั้งใจให้เป็นเครื่องมือที่ช่วยให้นักวิจัยสามารถขยายและพัฒนา MLX ได้อย่างรวดเร็วเพื่อสำรวจไอเดียใหม่ๆ

โมเดล LLMs สามารถเร่งความเร็วบนอุปกรณ์ Apple Silicon ผ่าน MLX และสามารถรันโมเดลได้อย่างสะดวกสบายในเครื่องท้องถิ่น

ตอนนี้ Apple MLX Framework รองรับการแปลงควอนไทซ์ของ Phi-3.5-Instruct(**Apple MLX Framework support**), Phi-3.5-Vision(**MLX-VLM Framework support**), และ Phi-3.5-MoE(**Apple MLX Framework support**) ลองใช้งานกันเลย:

### **Phi-3.5-Instruct**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-mini-instruct -q

```

### **Phi-3.5-Vision**

```bash

python -m mlxv_lm.convert --hf-path microsoft/Phi-3.5-vision-instruct -q

```

### **Phi-3.5-MoE**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-MoE-instruct  -q

```

### **🤖 ตัวอย่างสำหรับ Phi-3.5 กับ Apple MLX**

| Labs    | แนะนำ | ไปที่ |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | เรียนรู้วิธีใช้ Phi-3.5 Instruct กับ Apple MLX framework   |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | เรียนรู้วิธีใช้ Phi-3.5 Vision วิเคราะห์ภาพด้วย Apple MLX framework     |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | เรียนรู้วิธีใช้ Phi-3.5 MoE กับ Apple MLX framework  |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **แหล่งข้อมูล**

1. เรียนรู้เกี่ยวกับ Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub Rep [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub Repo [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้