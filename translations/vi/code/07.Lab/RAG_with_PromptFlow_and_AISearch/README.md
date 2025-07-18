<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-07-16T17:09:37+00:00",
  "source_file": "code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md",
  "language_code": "vi"
}
-->
## RAG với PromptFlow và AISearch

Trong ví dụ này, chúng ta sẽ triển khai một ứng dụng Retrieval Augmented Generation (RAG) sử dụng Phi3 làm SLM, AI Search làm vectorDB và Prompt Flow làm công cụ điều phối low-code.

## Tính năng

- Triển khai dễ dàng bằng Docker.
- Kiến trúc có khả năng mở rộng để xử lý các luồng công việc AI.
- Phương pháp low-code sử dụng Prompt Flow.

## Yêu cầu trước

Trước khi bắt đầu, hãy đảm bảo bạn đã đáp ứng các yêu cầu sau:

- Đã cài đặt Docker trên máy tính cá nhân.
- Có tài khoản Azure với quyền tạo và quản lý tài nguyên container.
- Có các phiên bản Azure AI Studio và Azure AI Search.
- Một mô hình embedding để tạo chỉ mục (có thể là embedding của Azure OpenAI hoặc mô hình OS từ catalog).
- Đã cài đặt Python 3.8 trở lên trên máy tính cá nhân.
- Một Azure Container Registry (hoặc bất kỳ registry nào bạn chọn).

## Cài đặt

1. Tạo một flow mới trong dự án Azure AI Studio của bạn bằng file flow.yaml.
2. Triển khai một Phi3 Model từ catalog mô hình Azure AI và tạo kết nối đến dự án của bạn. [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Tạo chỉ mục vector trên Azure AI Search sử dụng bất kỳ tài liệu nào bạn chọn [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Triển khai flow trên một managed endpoint và sử dụng nó trong file prompt-flow-frontend.py. [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Clone repository:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Xây dựng Docker image:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Đẩy Docker image lên Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Cách sử dụng

1. Chạy container Docker:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Truy cập ứng dụng trên trình duyệt tại `http://localhost:8501`.

## Liên hệ

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Bài viết đầy đủ: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.