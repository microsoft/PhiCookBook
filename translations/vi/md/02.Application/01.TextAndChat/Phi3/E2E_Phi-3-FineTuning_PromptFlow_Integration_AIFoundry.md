# Tinh chỉnh và Tích hợp mô hình Phi-3 tùy chỉnh với Prompt flow trong Microsoft Foundry

Mẫu toàn bộ quy trình (E2E) này dựa trên hướng dẫn "[Tinh chỉnh và Tích hợp các mô hình Phi-3 tùy chỉnh với Prompt Flow trong Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" từ Cộng đồng Kỹ thuật Microsoft. Nó giới thiệu các quy trình tinh chỉnh, triển khai và tích hợp các mô hình Phi-3 tùy chỉnh với Prompt flow trong Microsoft Foundry. Khác với mẫu E2E, "[Tinh chỉnh và Tích hợp các mô hình Phi-3 tùy chỉnh với Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", nơi chạy mã cục bộ, hướng dẫn này tập trung hoàn toàn vào tinh chỉnh và tích hợp mô hình của bạn bên trong Azure AI / ML Studio.

## Tổng quan

Trong mẫu E2E này, bạn sẽ học cách tinh chỉnh mô hình Phi-3 và tích hợp nó với Prompt flow trong Microsoft Foundry. Bằng cách tận dụng Azure AI / ML Studio, bạn sẽ thiết lập một quy trình làm việc để triển khai và sử dụng các mô hình AI tùy chỉnh. Mẫu E2E này được chia thành ba kịch bản:

**Kịch bản 1: Thiết lập tài nguyên Azure và Chuẩn bị tinh chỉnh**

**Kịch bản 2: Tinh chỉnh mô hình Phi-3 và Triển khai trong Azure Machine Learning Studio**

**Kịch bản 3: Tích hợp với Prompt flow và Trò chuyện với mô hình tùy chỉnh của bạn trong Microsoft Foundry**

Dưới đây là tổng quan về mẫu E2E này.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/vi/00-01-architecture.198ba0f1ae6d841a.webp)

### Mục lục

1. **[Kịch bản 1: Thiết lập tài nguyên Azure và Chuẩn bị tinh chỉnh](#kịch-bản-1-thiết-lập-tài-nguyên-azure-và-chuẩn-bị-tinh-chỉnh)**
    - [Tạo không gian làm việc Azure Machine Learning](#tạo-không-gian-làm-việc-azure-machine-learning)
    - [Yêu cầu hạn ngạch GPU trong Subscription Azure](#yêu-cầu-hạn-ngạch-gpu-trong-subscription-azure)
    - [Thêm phân quyền vai trò](#thêm-phân-quyền-vai-trò)
    - [Thiết lập dự án](#thiết-lập-dự-án)
    - [Chuẩn bị bộ dữ liệu để tinh chỉnh](#chuẩn-bị-bộ-dữ-liệu-để-fine-tune)

1. **[Kịch bản 2: Tinh chỉnh mô hình Phi-3 và Triển khai trong Azure Machine Learning Studio](#kịch-bản-2-fine-tune-mô-hình-phi-3-và-triển-khai-trong-azure-machine-learning-studio)**
    - [Tinh chỉnh mô hình Phi-3](#fine-tune-mô-hình-phi-3)
    - [Triển khai mô hình Phi-3 đã tinh chỉnh](#triển-khai-mô-hình-phi-3-đã-fine-tune)

1. **[Kịch bản 3: Tích hợp với Prompt flow và Trò chuyện với mô hình tùy chỉnh của bạn trong Microsoft Foundry](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [Tích hợp mô hình Phi-3 tùy chỉnh với Prompt flow](#tích-hợp-mô-hình-phi-3-tùy-chỉnh-với-prompt-flow)
    - [Trò chuyện với mô hình Phi-3 tùy chỉnh của bạn](#chat-với-mô-hình-phi-3-tùy-chỉnh-của-bạn)

## Kịch bản 1: Thiết lập tài nguyên Azure và Chuẩn bị tinh chỉnh

### Tạo không gian làm việc Azure Machine Learning

1. Gõ *azure machine learning* vào **thanh tìm kiếm** ở đầu trang cổng và chọn **Azure Machine Learning** trong số các tùy chọn xuất hiện.

    ![Gõ azure machine learning.](../../../../../../translated_images/vi/01-01-type-azml.acae6c5455e67b4b.webp)

2. Chọn **+ Create** từ menu điều hướng.

3. Chọn **New workspace** từ menu điều hướng.

    ![Chọn new workspace.](../../../../../../translated_images/vi/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. Thực hiện các tác vụ sau:

    - Chọn **Subscription** Azure của bạn.
    - Chọn **Resource group** để sử dụng (tạo mới nếu cần).
    - Nhập **Workspace Name**. Nó phải là giá trị duy nhất.
    - Chọn **Region** mà bạn muốn sử dụng.
    - Chọn **Storage account** để sử dụng (tạo mới nếu cần).
    - Chọn **Key vault** để sử dụng (tạo mới nếu cần).
    - Chọn **Application insights** để sử dụng (tạo mới nếu cần).
    - Chọn **Container registry** để sử dụng (tạo mới nếu cần).

    ![Điền thông tin azure machine learning.](../../../../../../translated_images/vi/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. Chọn **Review + Create**.

6. Chọn **Create**.

### Yêu cầu hạn ngạch GPU trong Subscription Azure

Trong hướng dẫn này, bạn sẽ học cách tinh chỉnh và triển khai mô hình Phi-3 bằng GPU. Để tinh chỉnh, bạn sẽ sử dụng GPU *Standard_NC24ads_A100_v4*, điều này cần yêu cầu hạn ngạch. Để triển khai, bạn sẽ sử dụng GPU *Standard_NC6s_v3*, cũng cần yêu cầu hạn ngạch.

> [!NOTE]
>
> Chỉ các Subscription Pay-As-You-Go (loại subscription tiêu chuẩn) mới đủ điều kiện cấp phát GPU; các subscription ưu đãi hiện chưa được hỗ trợ.
>

1. Truy cập [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Thực hiện các tác vụ sau để yêu cầu hạn ngạch *Standard NCADSA100v4 Family*:

    - Chọn **Quota** từ tab bên trái.
    - Chọn **Virtual machine family** để sử dụng. Ví dụ, chọn **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, bao gồm GPU *Standard_NC24ads_A100_v4*.
    - Chọn **Request quota** từ menu điều hướng.

        ![Yêu cầu hạn ngạch.](../../../../../../translated_images/vi/02-02-request-quota.c0428239a63ffdd5.webp)

    - Trong trang Request quota, nhập **New cores limit** bạn muốn sử dụng. Ví dụ, 24.
    - Trong trang Request quota, chọn **Submit** để gửi yêu cầu hạn ngạch GPU.

1. Thực hiện các tác vụ sau để yêu cầu hạn ngạch *Standard NCSv3 Family*:

    - Chọn **Quota** từ tab bên trái.
    - Chọn **Virtual machine family** để sử dụng. Ví dụ, chọn **Standard NCSv3 Family Cluster Dedicated vCPUs**, bao gồm GPU *Standard_NC6s_v3*.
    - Chọn **Request quota** từ menu điều hướng.
    - Trong trang Request quota, nhập **New cores limit** bạn muốn sử dụng. Ví dụ, 24.
    - Trong trang Request quota, chọn **Submit** để gửi yêu cầu hạn ngạch GPU.

### Thêm phân quyền vai trò

Để tinh chỉnh và triển khai các mô hình, bạn phải tạo trước một User Assigned Managed Identity (UAI) và gán cho nó các quyền phù hợp. UAI này sẽ được dùng để xác thực khi triển khai.

#### Tạo User Assigned Managed Identity (UAI)

1. Gõ *managed identities* vào **thanh tìm kiếm** ở đầu trang cổng và chọn **Managed Identities** trong số các tùy chọn xuất hiện.

    ![Gõ managed identities.](../../../../../../translated_images/vi/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. Chọn **+ Create**.

    ![Chọn create.](../../../../../../translated_images/vi/03-02-select-create.92bf8989a5cd98f2.webp)

1. Thực hiện các tác vụ sau:

    - Chọn **Subscription** Azure của bạn.
    - Chọn **Resource group** để sử dụng (tạo mới nếu cần).
    - Chọn **Region** bạn muốn sử dụng.
    - Nhập **Name**. Nó phải là giá trị duy nhất.

    ![Điền thông tin.](../../../../../../translated_images/vi/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. Chọn **Review + create**.

1. Chọn **+ Create**.

#### Thêm phân quyền vai trò Contributor cho Managed Identity

1. Điều hướng đến tài nguyên Managed Identity mà bạn đã tạo.

1. Chọn **Azure role assignments** từ tab bên trái.

1. Chọn **+Add role assignment** từ menu điều hướng.

1. Trong trang Add role assignment, thực hiện các tác vụ sau:
    - Chọn **Scope** là **Resource group**.
    - Chọn **Subscription** Azure của bạn.
    - Chọn **Resource group** để sử dụng.
    - Chọn **Role** là **Contributor**.

    ![Điền thông tin vai trò contributor.](../../../../../../translated_images/vi/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. Chọn **Save**.

#### Thêm phân quyền vai trò Storage Blob Data Reader cho Managed Identity

1. Gõ *storage accounts* vào **thanh tìm kiếm** ở đầu trang cổng và chọn **Storage accounts** trong số các tùy chọn xuất hiện.

    ![Gõ storage accounts.](../../../../../../translated_images/vi/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. Chọn tài khoản lưu trữ liên kết với không gian làm việc Azure Machine Learning mà bạn đã tạo, ví dụ như *finetunephistorage*.

1. Thực hiện các tác vụ sau để điều hướng đến trang Add role assignment:

    - Điều hướng đến tài khoản lưu trữ Azure bạn đã tạo.
    - Chọn **Access Control (IAM)** từ tab bên trái.
    - Chọn **+ Add** từ menu điều hướng.
    - Chọn **Add role assignment** từ menu điều hướng.

    ![Thêm vai trò.](../../../../../../translated_images/vi/03-06-add-role.353ccbfdcf0789c2.webp)

1. Trong trang Add role assignment, thực hiện các tác vụ sau:

    - Trong trang Role, gõ *Storage Blob Data Reader* vào **thanh tìm kiếm** và chọn **Storage Blob Data Reader** trong số các tùy chọn xuất hiện.
    - Trong trang Role, chọn **Next**.
    - Trong trang Members, chọn **Assign access to** là **Managed identity**.
    - Trong trang Members, chọn **+ Select members**.
    - Trong trang Select managed identities, chọn **Subscription** Azure của bạn.
    - Trong trang Select managed identities, chọn **Managed identity** là **Manage Identity**.
    - Trong trang Select managed identities, chọn Manage Identity mà bạn đã tạo, ví dụ *finetunephi-managedidentity*.
    - Trong trang Select managed identities, chọn **Select**.

    ![Chọn managed identity.](../../../../../../translated_images/vi/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. Chọn **Review + assign**.

#### Thêm phân quyền vai trò AcrPull cho Managed Identity

1. Gõ *container registries* vào **thanh tìm kiếm** ở đầu trang cổng và chọn **Container registries** trong số các tùy chọn xuất hiện.

    ![Gõ container registries.](../../../../../../translated_images/vi/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. Chọn container registry liên kết với không gian làm việc Azure Machine Learning. Ví dụ, *finetunephicontainerregistry*.

1. Thực hiện các tác vụ sau để điều hướng đến trang Add role assignment:

    - Chọn **Access Control (IAM)** từ tab bên trái.
    - Chọn **+ Add** từ menu điều hướng.
    - Chọn **Add role assignment** từ menu điều hướng.

1. Trong trang Add role assignment, thực hiện các tác vụ sau:

    - Trong trang Role, Gõ *AcrPull* vào **thanh tìm kiếm** và chọn **AcrPull** trong số các tùy chọn xuất hiện.
    - Trong trang Role, chọn **Next**.
    - Trong trang Members, chọn **Assign access to** là **Managed identity**.
    - Trong trang Members, chọn **+ Select members**.
    - Trong trang Select managed identities, chọn **Subscription** Azure của bạn.
    - Trong trang Select managed identities, chọn **Managed identity** là **Manage Identity**.
    - Trong trang Select managed identities, chọn Manage Identity mà bạn đã tạo, ví dụ *finetunephi-managedidentity*.
    - Trong trang Select managed identities, chọn **Select**.
    - Chọn **Review + assign**.

### Thiết lập dự án

Để tải các bộ dữ liệu cần thiết cho việc tinh chỉnh, bạn sẽ thiết lập môi trường cục bộ.

Trong bài tập này, bạn sẽ

- Tạo một thư mục để làm việc bên trong đó.
- Tạo một môi trường ảo.
- Cài đặt các gói cần thiết.
- Tạo file *download_dataset.py* để tải bộ dữ liệu.

#### Tạo thư mục để làm việc bên trong

1. Mở cửa sổ terminal và gõ lệnh sau để tạo thư mục có tên *finetune-phi* ở đường dẫn mặc định.

    ```console
    mkdir finetune-phi
    ```

2. Gõ lệnh sau trong terminal để điều hướng vào thư mục *finetune-phi* bạn đã tạo.

    ```console
    cd finetune-phi
    ```

#### Tạo môi trường ảo

1. Gõ lệnh sau trong terminal để tạo môi trường ảo có tên *.venv*.
    ```console
    python -m venv .venv
    ```

2. Gõ lệnh sau vào terminal để kích hoạt môi trường ảo.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Nếu thành công, bạn sẽ thấy *(.venv)* trước dấu nhắc lệnh.

#### Cài đặt các gói cần thiết

1. Gõ lệnh sau vào terminal để cài đặt các gói cần thiết.

    ```console
    pip install datasets==2.19.1
    ```

#### Tạo file `donload_dataset.py`

> [!NOTE]
> Cấu trúc thư mục hoàn chỉnh:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Mở **Visual Studio Code**.

1. Chọn **File** từ thanh menu.

1. Chọn **Open Folder**.

1. Chọn thư mục *finetune-phi* mà bạn đã tạo, nằm tại *C:\Users\yourUserName\finetune-phi*.

    ![Chọn thư mục bạn đã tạo.](../../../../../../translated_images/vi/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. Ở khung bên trái của Visual Studio Code, nhấp chuột phải và chọn **New File** để tạo một file mới tên là *download_dataset.py*.

    ![Tạo file mới.](../../../../../../translated_images/vi/04-02-create-new-file.cf9a330a3a9cff92.webp)

### Chuẩn bị bộ dữ liệu để fine-tune

Trong bài tập này, bạn sẽ chạy file *download_dataset.py* để tải bộ dữ liệu *ultrachat_200k* về môi trường cục bộ của bạn. Sau đó, bạn sẽ dùng bộ dữ liệu này để fine-tune mô hình Phi-3 trong Azure Machine Learning.

Trong bài tập này, bạn sẽ:

- Thêm mã vào file *download_dataset.py* để tải bộ dữ liệu.
- Chạy file *download_dataset.py* để tải bộ dữ liệu về môi trường cục bộ.

#### Tải bộ dữ liệu của bạn bằng *download_dataset.py*

1. Mở file *download_dataset.py* trong Visual Studio Code.

1. Thêm mã sau vào file *download_dataset.py*.

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # Tải bộ dữ liệu với tên, cấu hình và tỷ lệ phân chia được chỉ định
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Chia bộ dữ liệu thành bộ huấn luyện và kiểm tra (80% huấn luyện, 20% kiểm tra)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Tạo thư mục nếu nó chưa tồn tại
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Mở file ở chế độ ghi
        with open(filepath, 'w', encoding='utf-8') as f:
            # Lặp qua từng bản ghi trong bộ dữ liệu
            for record in dataset:
                # Ghi bản ghi dưới dạng đối tượng JSON và ghi vào file
                json.dump(record, f)
                # Viết ký tự xuống dòng để phân tách các bản ghi
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Tải và chia bộ dữ liệu ULTRACHAT_200k với cấu hình và tỷ lệ phân chia cụ thể
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Trích xuất bộ dữ liệu huấn luyện và kiểm tra từ phần chia
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Lưu bộ dữ liệu huấn luyện vào file JSONL
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Lưu bộ dữ liệu kiểm tra vào một file JSONL riêng biệt
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. Gõ lệnh sau vào terminal để chạy script và tải bộ dữ liệu về môi trường cục bộ.

    ```console
    python download_dataset.py
    ```

1. Xác nhận bộ dữ liệu đã được lưu thành công vào thư mục *finetune-phi/data* trên máy cục bộ của bạn.

> [!NOTE]
>
> #### Lưu ý về kích thước bộ dữ liệu và thời gian fine-tune
>
> Trong hướng dẫn này, bạn chỉ sử dụng 1% của bộ dữ liệu (`split='train[:1%]'`). Điều này giảm đáng kể lượng dữ liệu, giúp tăng tốc cả quá trình tải lên và fine-tune. Bạn có thể điều chỉnh tỉ lệ phần trăm để tìm sự cân bằng phù hợp giữa thời gian huấn luyện và hiệu suất mô hình. Sử dụng tập con nhỏ hơn của bộ dữ liệu làm giảm thời gian cần thiết cho fine-tune, giúp quá trình dễ quản lý hơn cho một bài hướng dẫn.

## Kịch bản 2: Fine-tune mô hình Phi-3 và Triển khai trong Azure Machine Learning Studio

### Fine-tune mô hình Phi-3

Trong bài tập này, bạn sẽ fine-tune mô hình Phi-3 trong Azure Machine Learning Studio.

Trong bài tập này, bạn sẽ:

- Tạo cụm máy tính để fine-tune.
- Fine-tune mô hình Phi-3 trong Azure Machine Learning Studio.

#### Tạo cụm máy tính để fine-tune

1. Truy cập [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Chọn **Compute** từ tab bên trái.

1. Chọn **Compute clusters** từ menu điều hướng.

1. Chọn **+ New**.

    ![Chọn compute.](../../../../../../translated_images/vi/06-01-select-compute.a29cff290b480252.webp)

1. Thực hiện các bước sau:

    - Chọn **Region** bạn muốn sử dụng.
    - Chọn **Virtual machine tier** thành **Dedicated**.
    - Chọn **Virtual machine type** thành **GPU**.
    - Chọn bộ lọc **Virtual machine size** thành **Select from all options**.
    - Chọn **Virtual machine size** là **Standard_NC24ads_A100_v4**.

    ![Tạo cụm.](../../../../../../translated_images/vi/06-02-create-cluster.f221b65ae1221d4e.webp)

1. Chọn **Next**.

1. Thực hiện các bước sau:

    - Nhập **Compute name**. Giá trị này phải duy nhất.
    - Chọn **Minimum number of nodes** là **0**.
    - Chọn **Maximum number of nodes** là **1**.
    - Chọn **Idle seconds before scale down** là **120**.

    ![Tạo cụm.](../../../../../../translated_images/vi/06-03-create-cluster.4a54ba20914f3662.webp)

1. Chọn **Create**.

#### Fine-tune mô hình Phi-3

1. Truy cập [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Chọn workspace Azure Machine Learning mà bạn đã tạo.

    ![Chọn workspace bạn đã tạo.](../../../../../../translated_images/vi/06-04-select-workspace.a92934ac04f4f181.webp)

1. Thực hiện các bước sau:

    - Chọn **Model catalog** từ tab bên trái.
    - Gõ *phi-3-mini-4k* vào **thanh tìm kiếm** và chọn **Phi-3-mini-4k-instruct** từ các tùy chọn hiện ra.

    ![Gõ phi-3-mini-4k.](../../../../../../translated_images/vi/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. Chọn **Fine-tune** từ menu điều hướng.

    ![Chọn fine tune.](../../../../../../translated_images/vi/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. Thực hiện các bước sau:

    - Chọn **Select task type** là **Chat completion**.
    - Chọn **+ Select data** để tải lên **Dữ liệu huấn luyện**.
    - Chọn loại tải lên Dữ liệu kiểm tra (Validation data) là **Provide different validation data**.
    - Chọn **+ Select data** để tải lên **Dữ liệu kiểm tra**.

    ![Điền vào trang fine-tuning.](../../../../../../translated_images/vi/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> Bạn có thể chọn **Advanced settings** để tùy chỉnh các cấu hình như **learning_rate** và **lr_scheduler_type** nhằm tối ưu hóa quá trình fine-tune theo nhu cầu cụ thể của bạn.

1. Chọn **Finish**.

1. Trong bài tập này, bạn đã fine-tune thành công mô hình Phi-3 sử dụng Azure Machine Learning. Xin lưu ý quá trình fine-tune có thể mất khá nhiều thời gian. Sau khi chạy công việc fine-tune, bạn cần chờ cho đến khi nó hoàn thành. Bạn có thể theo dõi trạng thái công việc fine-tune bằng cách vào tab Jobs ở bên trái của Azure Machine Learning Workspace. Trong phần kế tiếp, bạn sẽ triển khai mô hình fine-tune và tích hợp nó với Prompt flow.

    ![Xem công việc finetuning.](../../../../../../translated_images/vi/06-08-output.2bd32e59930672b1.webp)

### Triển khai mô hình Phi-3 đã fine-tune

Để tích hợp mô hình Phi-3 đã fine-tune với Prompt flow, bạn cần triển khai mô hình để nó có thể được truy cập cho việc suy luận theo thời gian thực. Quá trình này bao gồm đăng ký mô hình, tạo endpoint trực tuyến, và triển khai mô hình.

Trong bài tập này, bạn sẽ:

- Đăng ký mô hình fine-tune trong workspace Azure Machine Learning.
- Tạo một endpoint trực tuyến.
- Triển khai mô hình Phi-3 fine-tune đã đăng ký.

#### Đăng ký mô hình fine-tune

1. Truy cập [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Chọn workspace Azure Machine Learning mà bạn đã tạo.

    ![Chọn workspace bạn đã tạo.](../../../../../../translated_images/vi/06-04-select-workspace.a92934ac04f4f181.webp)

1. Chọn **Models** từ tab bên trái.
1. Chọn **+ Register**.
1. Chọn **From a job output**.

    ![Đăng ký mô hình.](../../../../../../translated_images/vi/07-01-register-model.ad1e7cc05e4b2777.webp)

1. Chọn công việc mà bạn đã tạo.

    ![Chọn công việc.](../../../../../../translated_images/vi/07-02-select-job.3e2e1144cd6cd093.webp)

1. Chọn **Next**.

1. Chọn **Model type** là **MLflow**.

1. Đảm bảo **Job output** được chọn; nó sẽ được chọn tự động.

    ![Chọn output.](../../../../../../translated_images/vi/07-03-select-output.4cf1a0e645baea1f.webp)

2. Chọn **Next**.

3. Chọn **Register**.

    ![Chọn đăng ký.](../../../../../../translated_images/vi/07-04-register.fd82a3b293060bc7.webp)

4. Bạn có thể xem mô hình đã đăng ký bằng cách vào menu **Models** ở tab bên trái.

    ![Mô hình đã đăng ký.](../../../../../../translated_images/vi/07-05-registered-model.7db9775f58dfd591.webp)

#### Triển khai mô hình fine-tune

1. Truy cập workspace Azure Machine Learning mà bạn đã tạo.

1. Chọn **Endpoints** từ tab bên trái.

1. Chọn **Real-time endpoints** từ menu điều hướng.

    ![Tạo endpoint.](../../../../../../translated_images/vi/07-06-create-endpoint.1ba865c606551f09.webp)

1. Chọn **Create**.

1. Chọn mô hình đã đăng ký mà bạn đã tạo.

    ![Chọn mô hình đã đăng ký.](../../../../../../translated_images/vi/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. Chọn **Select**.

1. Thực hiện các bước sau:

    - Chọn **Virtual machine** là *Standard_NC6s_v3*.
    - Chọn **Instance count** bạn muốn sử dụng. Ví dụ, *1*.
    - Chọn **Endpoint** thành **New** để tạo một endpoint mới.
    - Nhập **Endpoint name**. Giá trị này phải duy nhất.
    - Nhập **Deployment name**. Giá trị này phải duy nhất.

    ![Điền cài đặt triển khai.](../../../../../../translated_images/vi/07-08-deployment-setting.43ddc4209e673784.webp)

1. Chọn **Deploy**.

> [!WARNING]
> Để tránh các phí bổ sung trên tài khoản của bạn, hãy nhớ xóa endpoint đã tạo trong workspace Azure Machine Learning khi không còn sử dụng nữa.
>

#### Kiểm tra trạng thái triển khai trong Azure Machine Learning Workspace

1. Truy cập workspace Azure Machine Learning mà bạn đã tạo.

1. Chọn **Endpoints** từ tab bên trái.

1. Chọn endpoint mà bạn đã tạo.

    ![Chọn endpoints](../../../../../../translated_images/vi/07-09-check-deployment.325d18cae8475ef4.webp)

1. Ở trang này, bạn có thể quản lý các endpoint trong quá trình triển khai.

> [!NOTE]
> Khi triển khai hoàn tất, hãy đảm bảo **Live traffic** được đặt là **100%**. Nếu không, hãy chọn **Update traffic** để điều chỉnh cài đặt lưu lượng. Lưu ý rằng bạn không thể thử nghiệm mô hình nếu lưu lượng được đặt bằng 0%.
>
> ![Đặt lưu lượng.](../../../../../../translated_images/vi/07-10-set-traffic.085b847e5751ff3d.webp)
>

## Kịch bản 3: Tích hợp với Prompt flow và chat với mô hình tùy chỉnh của bạn trong Microsoft Foundry

### Tích hợp mô hình Phi-3 tùy chỉnh với Prompt flow

Sau khi triển khai thành công mô hình bạn đã fine-tune, bạn có thể tích hợp nó với Prompt Flow để sử dụng mô hình trong các ứng dụng thời gian thực, cho phép thực hiện nhiều tác vụ tương tác với mô hình Phi-3 tùy chỉnh của bạn.

Trong bài tập này, bạn sẽ:

- Tạo Microsoft Foundry Hub.
- Tạo Microsoft Foundry Project.
- Tạo Prompt flow.
- Thêm kết nối tùy chỉnh cho mô hình Phi-3 đã fine-tune.
- Thiết lập Prompt flow để chat với mô hình Phi-3 tùy chỉnh của bạn

> [!NOTE]
> Bạn cũng có thể tích hợp với Promptflow bằng Azure ML Studio. Quy trình tích hợp tương tự có thể áp dụng cho Azure ML Studio.

#### Tạo Microsoft Foundry Hub

Bạn cần tạo một Hub trước khi tạo Project. Hub hoạt động giống như một Nhóm Tài nguyên, cho phép bạn tổ chức và quản lý nhiều Project trong Microsoft Foundry.
1. Truy cập [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Chọn **All hubs** từ tab bên trái.

1. Chọn **+ New hub** từ menu điều hướng.

    ![Create hub.](../../../../../../translated_images/vi/08-01-create-hub.8f7dd615bb8d9834.webp)

1. Thực hiện các tác vụ sau:

    - Nhập **Hub name**. Nó phải là một giá trị duy nhất.
    - Chọn **Subscription** Azure của bạn.
    - Chọn **Resource group** để sử dụng (tạo mới nếu cần).
    - Chọn **Location** bạn muốn sử dụng.
    - Chọn **Connect Azure AI Services** để sử dụng (tạo mới nếu cần).
    - Chọn **Connect Azure AI Search** để **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/vi/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. Chọn **Next**.

#### Tạo dự án Microsoft Foundry

1. Trong Hub mà bạn đã tạo, chọn **All projects** từ tab bên trái.

1. Chọn **+ New project** từ menu điều hướng.

    ![Select new project.](../../../../../../translated_images/vi/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. Nhập **Project name**. Nó phải là một giá trị duy nhất.

    ![Create project.](../../../../../../translated_images/vi/08-05-create-project.4d97f0372f03375a.webp)

1. Chọn **Create a project**.

#### Thêm kết nối tùy chỉnh cho mô hình Phi-3 được tinh chỉnh

Để tích hợp mô hình Phi-3 tùy chỉnh của bạn với Prompt flow, bạn cần lưu điểm cuối và khóa của mô hình trong một kết nối tùy chỉnh. Cấu hình này đảm bảo quyền truy cập vào mô hình Phi-3 tùy chỉnh của bạn trong Prompt flow.

#### Đặt khóa api và uri endpoint của mô hình Phi-3 được tinh chỉnh

1. Truy cập [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Điều hướng đến workspace Azure Machine learning mà bạn đã tạo.

1. Chọn **Endpoints** từ tab bên trái.

    ![Select endpoints.](../../../../../../translated_images/vi/08-06-select-endpoints.aff38d453bcf9605.webp)

1. Chọn endpoint mà bạn đã tạo.

    ![Select endpoints.](../../../../../../translated_images/vi/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. Chọn **Consume** từ menu điều hướng.

1. Sao chép **REST endpoint** và **Primary key** của bạn.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/vi/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### Thêm Kết nối Tùy chỉnh

1. Truy cập [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Điều hướng đến dự án Microsoft Foundry mà bạn đã tạo.

1. Trong dự án mà bạn đã tạo, chọn **Settings** từ tab bên trái.

1. Chọn **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/vi/08-09-select-new-connection.02eb45deadc401fc.webp)

1. Chọn **Custom keys** từ menu điều hướng.

    ![Select custom keys.](../../../../../../translated_images/vi/08-10-select-custom-keys.856f6b2966460551.webp)

1. Thực hiện các tác vụ sau:

    - Chọn **+ Add key value pairs**.
    - Với tên khóa, nhập **endpoint** và dán endpoint bạn đã sao chép từ Azure ML Studio vào trường giá trị.
    - Chọn **+ Add key value pairs** lần nữa.
    - Với tên khóa, nhập **key** và dán khóa bạn đã sao chép từ Azure ML Studio vào trường giá trị.
    - Sau khi thêm các khóa, chọn **is secret** để khóa không bị lộ.

    ![Add connection.](../../../../../../translated_images/vi/08-11-add-connection.785486badb4d2d26.webp)

1. Chọn **Add connection**.

#### Tạo Prompt flow

Bạn đã thêm một kết nối tùy chỉnh trong Microsoft Foundry. Bây giờ, hãy tạo một Prompt flow bằng các bước sau. Sau đó, bạn sẽ kết nối Prompt flow này với kết nối tùy chỉnh để có thể sử dụng mô hình được tinh chỉnh trong Prompt flow.

1. Điều hướng đến dự án Microsoft Foundry mà bạn đã tạo.

1. Chọn **Prompt flow** từ tab bên trái.

1. Chọn **+ Create** từ menu điều hướng.

    ![Select Promptflow.](../../../../../../translated_images/vi/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. Chọn **Chat flow** từ menu điều hướng.

    ![Select chat flow.](../../../../../../translated_images/vi/08-13-select-flow-type.2ec689b22da32591.webp)

1. Nhập **Folder name** để sử dụng.

    ![Enter name.](../../../../../../translated_images/vi/08-14-enter-name.ff9520fefd89f40d.webp)

2. Chọn **Create**.

#### Cấu hình Prompt flow để chat với mô hình Phi-3 tùy chỉnh của bạn

Bạn cần tích hợp mô hình Phi-3 được tinh chỉnh vào Prompt flow. Tuy nhiên, Prompt flow hiện tại được cung cấp không được thiết kế cho mục đích này. Vì vậy, bạn phải thiết kế lại Prompt flow để cho phép tích hợp mô hình tùy chỉnh.

1. Trong Prompt flow, thực hiện các tác vụ sau để xây dựng lại luồng hiện tại:

    - Chọn **Raw file mode**.
    - Xóa tất cả mã hiện có trong file *flow.dag.yml*.
    - Thêm đoạn mã sau vào file *flow.dag.yml*.

        ```yml
        inputs:
          input_data:
            type: string
            default: "Who founded Microsoft?"

        outputs:
          answer:
            type: string
            reference: ${integrate_with_promptflow.output}

        nodes:
        - name: integrate_with_promptflow
          type: python
          source:
            type: code
            path: integrate_with_promptflow.py
          inputs:
            input_data: ${inputs.input_data}
        ```

    - Chọn **Save**.

    ![Select raw file mode.](../../../../../../translated_images/vi/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. Thêm đoạn mã sau vào file *integrate_with_promptflow.py* để sử dụng mô hình Phi-3 tùy chỉnh trong Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Cài đặt ghi nhật ký
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 model endpoint with the given input data using Custom Connection.
        """

        # "connection" là tên của Kết nối Tùy chỉnh, "endpoint", "key" là các khóa trong Kết nối Tùy chỉnh
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "input_data": {
                "input_string": [
                    {"role": "user", "content": input_data}
                ],
                "parameters": {
                    "temperature": 0.7,
                    "max_new_tokens": 128
                }
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # Ghi nhật ký phản hồi JSON đầy đủ
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Paste prompt flow code.](../../../../../../translated_images/vi/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> Để biết thông tin chi tiết hơn về cách sử dụng Prompt flow trong Microsoft Foundry, bạn có thể tham khảo [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Chọn **Chat input**, **Chat output** để bật trò chuyện với mô hình của bạn.

    ![Input Output.](../../../../../../translated_images/vi/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. Bây giờ bạn đã sẵn sàng để chat với mô hình Phi-3 tùy chỉnh của bạn. Trong bài tập tiếp theo, bạn sẽ học cách khởi động Prompt flow và sử dụng nó để trò chuyện với mô hình Phi-3 được tinh chỉnh của mình.

> [!NOTE]
>
> Luồng được xây dựng lại sẽ trông như hình bên dưới:
>
> ![Flow example.](../../../../../../translated_images/vi/08-18-graph-example.d6457533952e690c.webp)
>

### Chat với mô hình Phi-3 tùy chỉnh của bạn

Bây giờ bạn đã tinh chỉnh và tích hợp mô hình Phi-3 tùy chỉnh với Prompt flow, bạn sẵn sàng bắt đầu tương tác với nó. Bài tập này sẽ hướng dẫn bạn quá trình thiết lập và bắt đầu trò chuyện với mô hình bằng cách sử dụng Prompt flow. Bằng cách làm theo các bước này, bạn sẽ có thể tận dụng tối đa khả năng của mô hình Phi-3 được tinh chỉnh cho các tác vụ và cuộc hội thoại khác nhau.

- Chat với mô hình Phi-3 tùy chỉnh của bạn bằng Prompt flow.

#### Bắt đầu Prompt flow

1. Chọn **Start compute sessions** để khởi động Prompt flow.

    ![Start compute session.](../../../../../../translated_images/vi/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. Chọn **Validate and parse input** để làm mới các tham số.

    ![Validate input.](../../../../../../translated_images/vi/09-02-validate-input.317c76ef766361e9.webp)

1. Chọn giá trị **Value** của **connection** tới kết nối tùy chỉnh bạn đã tạo. Ví dụ, *connection*.

    ![Connection.](../../../../../../translated_images/vi/09-03-select-connection.99bdddb4b1844023.webp)

#### Chat với mô hình tùy chỉnh của bạn

1. Chọn **Chat**.

    ![Select chat.](../../../../../../translated_images/vi/09-04-select-chat.61936dce6612a1e6.webp)

1. Đây là ví dụ về kết quả: Bây giờ bạn có thể chat với mô hình Phi-3 tùy chỉnh của mình. Nên đặt câu hỏi dựa trên dữ liệu đã sử dụng để tinh chỉnh.

    ![Chat with prompt flow.](../../../../../../translated_images/vi/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc sự không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn tham khảo chính xác. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm đối với bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->