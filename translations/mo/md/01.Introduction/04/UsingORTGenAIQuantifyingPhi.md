<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3bb9f5c926673593287eddc3741226cb",
  "translation_date": "2025-05-07T14:53:58+00:00",
  "source_file": "md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md",
  "language_code": "mo"
}
-->
## **Model Builder ໃຊ້ຢ່າງໃດເພື່ອ quantizing Phi-3.5**

Model Builder ຕອບຮັບການ quantization ໂປຣແມງ ONNX ສຳລັບ Phi-3.5 Instruct ແລະ Phi-3.5-Vision ແລ້ວ

### **Phi-3.5-Instruct**

**ການແປງດ້ວຍການເຊື່ອມຕໍ່ CPU ດ້ວຍ quantized INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**ການແປງດ້ວຍການເຊື່ອມຕໍ່ CUDA ດ້ວຍ quantized INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. ຕັ້ງຄ່າສິ່ງແວພາຍໃນ terminal

```bash

mkdir models

cd models 

```

2. ດາວໂຫຼດ microsoft/Phi-3.5-vision-instruct ໃນໂຟນເດີ models  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. ກະລຸນາດາວໂຫຼດໄຟລ໌ເຫຼົ່ານີ້ໄປທີ່ໂຟນເດີ Phi-3.5-vision-instruct ຂອງທ່ານ

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. ດາວໂຫຼດໄຟລ໌ນີ້ໄປທີ່ໂຟນເດີ models  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. ໄປທີ່ terminal

    ແປງ ONNX ໃຫ້ຮອງຮັບ FP32

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Note：**

1. Model Builder ປັດຈຸບັນສາມາດແປງ Phi-3.5-Instruct ແລະ Phi-3.5-Vision ໄດ້ ແຕ່ບໍ່ສາມາດແປງ Phi-3.5-MoE

2. ເພື່ອໃຊ້ໂປຣແມງ quantized ຂອງ ONNX ທ່ານສາມາດໃຊ້ຜ່ານ Generative AI extensions for onnxruntime SDK

3. ພວກເຮົາຈຳເປັນຕ້ອງພິຈາລະນາ AI ທີ່ຮັບຜິດຊອບຫຼາຍຂຶ້ນ, ຫຼັງຈາກການແປງ model ຄວນທົດສອບຜົນລັບຢ່າງມີປະສິດທິພາບ

4. ໂດຍການ quantize ໂປຣແມງ CPU INT4, ພວກເຮົາສາມາດນຳໄປ deploy ໃສ່ Edge Device ໄດ້, ມີສະພາບການນໍາໃຊ້ທີ່ດີກວ່າ, ດັ່ງນັ້ນພວກເຮົາໄດ້ສຳເລັດ Phi-3.5-Instruct ໃນຮູບແບບ INT 4 ແລ້ວ

## **ຊັບພະຍາກອນ**

1. ຮຽນຮູ້ເພີ່ມເຕີມເກັບ Generative AI extensions for onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime GitHub Repo [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Disclaimer**:  
This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.

---

(Note: "mo" is not a recognized language code or widely known language name. Could you please clarify which language "mo" refers to? This will help me provide an accurate translation.)