<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-05-09T05:12:45+00:00",
  "source_file": "code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md",
  "language_code": "th"
}
-->
## RAG กับ PromptFlow และ AISearch

ในตัวอย่างนี้ เราจะสร้างแอปพลิเคชัน Retrieval Augmented Generation (RAG) โดยใช้ Phi3 เป็น SLM, AI Search เป็น vectorDB และ Prompt Flow เป็นตัวจัดการแบบ low-code

## คุณสมบัติ

- ติดตั้งง่ายด้วย Docker
- สถาปัตยกรรมที่ปรับขนาดได้สำหรับจัดการเวิร์กโฟลว์ AI
- วิธีการเขียนโค้ดน้อยโดยใช้ Prompt Flow

## ข้อกำหนดเบื้องต้น

ก่อนเริ่มต้น ให้แน่ใจว่าคุณมีสิ่งต่อไปนี้:

- ติดตั้ง Docker บนเครื่องของคุณแล้ว
- บัญชี Azure ที่มีสิทธิ์สร้างและจัดการทรัพยากรคอนเทนเนอร์
- Azure AI Studio และ Azure AI Search
- โมเดล embedding สำหรับสร้างดัชนี (สามารถใช้ Azure OpenAI embedding หรือโมเดล OS จากแคตตาล็อก)
- ติดตั้ง Python 3.8 ขึ้นไปบนเครื่องของคุณ
- Azure Container Registry (หรือรีจิสทรีอื่นที่คุณเลือก)

## การติดตั้ง

1. สร้าง flow ใหม่ในโปรเจกต์ Azure AI Studio ของคุณโดยใช้ไฟล์ flow.yaml
2. ติดตั้ง Phi3 Model จากแคตตาล็อกโมเดล Azure AI และเชื่อมต่อกับโปรเจกต์ของคุณ [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. สร้างดัชนีเวกเตอร์บน Azure AI Search โดยใช้เอกสารที่คุณเลือก [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. ติดตั้ง flow บน managed endpoint และใช้งานในไฟล์ prompt-flow-frontend.py [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. โคลนรีโพสิทอรี:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. สร้าง Docker image:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. ดัน Docker image ไปยัง Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## การใช้งาน

1. รัน Docker container:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. เข้าใช้งานแอปพลิเคชันผ่านเบราว์เซอร์ที่ `http://localhost:8501`

## ติดต่อ

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

บทความเต็ม: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาด้วย AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นฉบับถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลสำคัญ แนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดใด ๆ ที่เกิดจากการใช้การแปลนี้