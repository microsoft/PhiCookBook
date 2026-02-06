## RAG กับ PromptFlow และ AISearch

ในตัวอย่างนี้ เราจะสร้างแอปพลิเคชัน Retrieval Augmented Generation (RAG) โดยใช้ Phi3 เป็น SLM, AI Search เป็น vectorDB และ Prompt Flow เป็นตัวจัดการแบบ low-code

## คุณสมบัติ

- ติดตั้งง่ายด้วย Docker
- สถาปัตยกรรมที่ปรับขนาดได้สำหรับจัดการเวิร์กโฟลว์ AI
- แนวทาง low code โดยใช้ Prompt Flow

## ข้อกำหนดเบื้องต้น

ก่อนเริ่มต้น โปรดตรวจสอบว่าคุณมีสิ่งต่อไปนี้ครบถ้วน:

- ติดตั้ง Docker บนเครื่องของคุณแล้ว
- บัญชี Azure ที่มีสิทธิ์สร้างและจัดการทรัพยากรคอนเทนเนอร์
- Azure AI Studio และ Azure AI Search
- โมเดล embedding สำหรับสร้างดัชนี (อาจเป็น Azure OpenAI embedding หรือโมเดล OS จากแคตตาล็อก)
- ติดตั้ง Python 3.8 ขึ้นไปบนเครื่องของคุณ
- Azure Container Registry (หรือรีจิสทรีที่คุณเลือกใช้)

## การติดตั้ง

1. สร้าง flow ใหม่ในโปรเจกต์ Azure AI Studio ของคุณโดยใช้ไฟล์ flow.yaml
2. นำ Phi3 Model จากแคตตาล็อกโมเดล Azure AI มาใช้งานและเชื่อมต่อกับโปรเจกต์ของคุณ [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. สร้าง vector index บน Azure AI Search โดยใช้เอกสารใดก็ได้ที่คุณเลือก [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. นำ flow ไป deploy บน managed endpoint และใช้งานในไฟล์ prompt-flow-frontend.py [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. โคลนรีโพซิทอรี:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. สร้าง Docker image:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. ส่ง Docker image ไปยัง Azure Container Registry:

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

2. เข้าถึงแอปพลิเคชันผ่านเบราว์เซอร์ที่ `http://localhost:8501`

## ติดต่อ

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

บทความเต็ม: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้