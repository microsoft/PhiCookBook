<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-05-09T13:44:52+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "th"
}
-->
# **การควอนไทซ์ Phi-3.5 โดยใช้ Apple MLX Framework**

MLX คือเฟรมเวิร์กอาร์เรย์สำหรับการวิจัยด้านแมชชีนเลิร์นนิงบนชิป Apple silicon ซึ่งพัฒนาโดยทีมวิจัยแมชชีนเลิร์นนิงของ Apple

MLX ถูกออกแบบโดยนักวิจัยแมชชีนเลิร์นนิงสำหรับนักวิจัยแมชชีนเลิร์นนิง เฟรมเวิร์กนี้ตั้งใจให้ใช้งานง่าย แต่ยังคงประสิทธิภาพในการฝึกสอนและปรับใช้โมเดล การออกแบบของเฟรมเวิร์กเองก็เรียบง่ายในเชิงแนวคิด เราตั้งใจให้การขยายและปรับปรุง MLX เป็นเรื่องง่ายสำหรับนักวิจัย เพื่อให้สามารถสำรวจไอเดียใหม่ๆ ได้อย่างรวดเร็ว

โมเดล LLMs สามารถเร่งความเร็วบนอุปกรณ์ Apple Silicon ผ่าน MLX และโมเดลสามารถรันได้ในเครื่องอย่างสะดวกสบาย

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
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดขึ้นจากการใช้การแปลนี้