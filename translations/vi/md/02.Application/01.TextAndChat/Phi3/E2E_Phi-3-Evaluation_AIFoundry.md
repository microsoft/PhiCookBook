# Đánh giá Mô hình Phi-3 / Phi-3.5 Tinh chỉnh trong Microsoft Foundry Tập trung vào Nguyên tắc AI Có Trách nhiệm của Microsoft

Mẫu toàn diện (E2E) này dựa trên hướng dẫn "[Đánh giá Mô hình Phi-3 / 3.5 Tinh chỉnh trong Microsoft Foundry Tập trung vào AI Có Trách nhiệm của Microsoft](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" từ Cộng đồng Kỹ thuật Microsoft.

## Tổng quan

### Làm thế nào để đánh giá sự an toàn và hiệu suất của mô hình Phi-3 / Phi-3.5 đã được tinh chỉnh trong Microsoft Foundry?

Việc tinh chỉnh mô hình đôi khi có thể dẫn đến các phản hồi không mong muốn hoặc không dự kiến. Để đảm bảo mô hình vẫn an toàn và hiệu quả, điều quan trọng là đánh giá khả năng mô hình tạo ra nội dung gây hại và khả năng đưa ra các phản hồi chính xác, liên quan và mạch lạc. Trong hướng dẫn này, bạn sẽ học cách đánh giá sự an toàn và hiệu suất của mô hình Phi-3 / Phi-3.5 đã được tinh chỉnh tích hợp với Prompt flow trong Microsoft Foundry.

Dưới đây là quy trình đánh giá của Microsoft Foundry.

![Kiến trúc của hướng dẫn.](../../../../../../translated_images/vi/architecture.10bec55250f5d6a4.webp)

*Nguồn hình ảnh: [Đánh giá ứng dụng AI sinh tạo](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Để biết thông tin chi tiết hơn và khám phá các tài nguyên bổ sung về Phi-3 / Phi-3.5, vui lòng truy cập [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Yêu cầu trước

- [Python](https://www.python.org/downloads)
- [Đăng ký Azure](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Mô hình Phi-3 / Phi-3.5 đã được tinh chỉnh

### Mục lục

1. [**Tình huống 1: Giới thiệu về đánh giá Prompt flow của Microsoft Foundry**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [Giới thiệu về việc đánh giá an toàn](#giới-thiệu-về-việc-đánh-giá-an-toàn)
    - [Giới thiệu về việc đánh giá hiệu suất](#giới-thiệu-về-việc-đánh-giá-hiệu-suất)

1. [**Tình huống 2: Đánh giá mô hình Phi-3 / Phi-3.5 trong Microsoft Foundry**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [Trước khi bạn bắt đầu](#trước-khi-bạn-bắt-đầu)
    - [Triển khai Azure OpenAI để đánh giá mô hình Phi-3 / Phi-3.5](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [Đánh giá mô hình Phi-3 / Phi-3.5 đã tinh chỉnh sử dụng đánh giá Prompt flow của Microsoft Foundry](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [Chúc mừng!](#chúc-mừng)

## **Tình huống 1: Giới thiệu về đánh giá Prompt flow của Microsoft Foundry**

### Giới thiệu về việc đánh giá an toàn

Để đảm bảo mô hình AI của bạn có đạo đức và an toàn, điều quan trọng là đánh giá nó dựa trên Nguyên tắc AI Có Trách nhiệm của Microsoft. Trong Microsoft Foundry, việc đánh giá an toàn cho phép bạn đánh giá khả năng mô hình của mình bị tấn công jailbreak và tiềm năng tạo ra nội dung gây hại, điều này hoàn toàn phù hợp với các nguyên tắc này.

![Đánh giá an toàn.](../../../../../../translated_images/vi/safety-evaluation.083586ec88dfa950.webp)

*Nguồn hình ảnh: [Đánh giá ứng dụng AI sinh tạo](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Nguyên tắc AI Có Trách nhiệm của Microsoft

Trước khi bắt đầu các bước kỹ thuật, điều quan trọng là hiểu các Nguyên tắc AI Có Trách nhiệm của Microsoft, một khung đạo đức được thiết kế để hướng dẫn phát triển, triển khai và vận hành hệ thống AI có trách nhiệm. Những nguyên tắc này hướng dẫn thiết kế, phát triển và triển khai hệ thống AI một cách trách nhiệm, đảm bảo các công nghệ AI được xây dựng theo cách công bằng, minh bạch và bao quát. Các nguyên tắc này là nền tảng để đánh giá sự an toàn của mô hình AI.

Nguyên tắc AI Có Trách nhiệm của Microsoft bao gồm:

- **Công bằng và Bao quát**: Hệ thống AI nên đối xử công bằng với mọi người và tránh tác động khác nhau đến các nhóm người có hoàn cảnh tương tự. Ví dụ, khi hệ thống AI đưa ra lời khuyên về điều trị y tế, hồ sơ vay vốn hoặc việc làm, nó nên cung cấp các đề xuất giống nhau cho tất cả những người có triệu chứng, hoàn cảnh tài chính hoặc trình độ chuyên môn tương tự.

- **Độ tin cậy và An toàn**: Để xây dựng sự tin tưởng, quan trọng là các hệ thống AI hoạt động một cách đáng tin cậy, an toàn và nhất quán. Các hệ thống này cần có khả năng hoạt động như thiết kế ban đầu, phản ứng an toàn với các điều kiện không dự đoán và chống lại thao túng gây hại. Cách chúng hoạt động và phạm vi các điều kiện chúng có thể xử lý phản ánh dải tình huống và điều kiện mà các nhà phát triển dự kiến trong quá trình thiết kế và thử nghiệm.

- **Minh bạch**: Khi các hệ thống AI hỗ trợ đưa ra các quyết định có ảnh hưởng lớn đến cuộc sống của con người, điều quan trọng là mọi người hiểu cách các quyết định đó được đưa ra. Ví dụ, một ngân hàng có thể sử dụng hệ thống AI để quyết định một người có đủ điều kiện tín dụng hay không. Một công ty có thể dùng AI để xác định những ứng viên xuất sắc nhất để tuyển dụng.

- **Quyền riêng tư và An ninh**: Khi AI ngày càng phổ biến, việc bảo vệ quyền riêng tư và đảm bảo thông tin cá nhân cũng như doanh nghiệp trở nên quan trọng và phức tạp hơn. Với AI, quyền riêng tư và bảo mật dữ liệu cần được chú ý kỹ lưỡng vì việc truy cập dữ liệu là thiết yếu để các hệ thống AI có thể đưa ra dự đoán chính xác và quyết định thông minh về con người.

- **Trách nhiệm giải trình**: Những người thiết kế và triển khai hệ thống AI phải chịu trách nhiệm về cách hệ thống của họ hoạt động. Các tổ chức nên dựa trên các tiêu chuẩn ngành để phát triển các chuẩn mực trách nhiệm giải trình. Các chuẩn mực này có thể đảm bảo hệ thống AI không trở thành quyền hạn cuối cùng trong bất kỳ quyết định nào ảnh hưởng đến cuộc sống của con người. Chúng cũng đảm bảo con người duy trì kiểm soát ý nghĩa đối với các hệ thống AI có tính tự chủ cao.

![Trung tâm điền.](../../../../../../translated_images/vi/responsibleai2.c07ef430113fad8c.webp)

*Nguồn hình ảnh: [AI Có Trách nhiệm là gì?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Để tìm hiểu thêm về Nguyên tắc AI Có Trách nhiệm của Microsoft, hãy truy cập [AI Có Trách nhiệm là gì?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Các chỉ số an toàn

Trong hướng dẫn này, bạn sẽ đánh giá sự an toàn của mô hình Phi-3 được tinh chỉnh bằng các chỉ số an toàn của Microsoft Foundry. Các chỉ số này giúp bạn đánh giá khả năng mô hình tạo ra nội dung gây hại và dễ bị tấn công jailbreak. Các chỉ số an toàn bao gồm:

- **Nội dung liên quan đến tự làm hại**: Đánh giá liệu mô hình có xu hướng tạo ra nội dung liên quan đến tự làm hại hay không.
- **Nội dung căm ghét và không công bằng**: Đánh giá liệu mô hình có xu hướng tạo ra nội dung chứa sự thù địch hoặc không công bằng không.
- **Nội dung bạo lực**: Đánh giá liệu mô hình có xu hướng tạo ra nội dung bạo lực không.
- **Nội dung tình dục**: Đánh giá liệu mô hình có xu hướng tạo ra nội dung tình dục không phù hợp không.

Việc đánh giá những khía cạnh này đảm bảo mô hình AI không tạo ra nội dung gây hại hoặc xúc phạm, phù hợp với giá trị xã hội và các tiêu chuẩn quy định.

![Đánh giá dựa trên an toàn.](../../../../../../translated_images/vi/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### Giới thiệu về việc đánh giá hiệu suất

Để đảm bảo mô hình AI của bạn hoạt động như mong đợi, điều quan trọng là đánh giá hiệu suất của nó dựa trên các chỉ số hiệu suất. Trong Microsoft Foundry, đánh giá hiệu suất cho phép bạn đánh giá hiệu quả của mô hình trong việc tạo ra các phản hồi chính xác, phù hợp và mạch lạc.

![Đánh giá an toàn.](../../../../../../translated_images/vi/performance-evaluation.48b3e7e01a098740.webp)

*Nguồn hình ảnh: [Đánh giá ứng dụng AI sinh tạo](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Các chỉ số hiệu suất

Trong hướng dẫn này, bạn sẽ đánh giá hiệu suất của mô hình Phi-3 / Phi-3.5 đã được tinh chỉnh bằng các chỉ số hiệu suất của Microsoft Foundry. Các chỉ số này giúp bạn đánh giá hiệu quả của mô hình trong việc tạo ra các phản hồi chính xác, phù hợp và mạch lạc. Các chỉ số hiệu suất bao gồm:

- **Độ căn cứ**: Đánh giá mức độ phù hợp của câu trả lời được tạo ra với thông tin từ nguồn đầu vào.
- **Sự liên quan**: Đánh giá sự phù hợp của các phản hồi được tạo ra với câu hỏi được đưa ra.
- **Tính mạch lạc**: Đánh giá độ trôi chảy, tự nhiên của văn bản được tạo ra và mức độ giống ngôn ngữ của con người.
- **Thông thạo**: Đánh giá trình độ ngôn ngữ của văn bản được tạo ra.
- **Độ tương đồng GPT**: So sánh phản hồi được tạo ra với dữ liệu thực tế để đo độ tương tự.
- **Điểm F1**: Tính tỷ lệ các từ chia sẻ giữa phản hồi được tạo ra và dữ liệu nguồn.

Các chỉ số này giúp bạn đánh giá hiệu quả của mô hình trong việc tạo ra những phản hồi chính xác, liên quan và mạch lạc.

![Đánh giá dựa trên hiệu suất.](../../../../../../translated_images/vi/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **Tình huống 2: Đánh giá mô hình Phi-3 / Phi-3.5 trong Microsoft Foundry**

### Trước khi bạn bắt đầu

Hướng dẫn này là phần nối tiếp của các bài đăng blog trước, "[Tinh chỉnh và Tích hợp Mô hình Phi-3 Tùy chỉnh với Prompt Flow: Hướng dẫn từng bước](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" và "[Tinh chỉnh và Tích hợp Mô hình Phi-3 Tùy chỉnh với Prompt Flow trong Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." Trong các bài này, chúng tôi đã hướng dẫn bạn quá trình tinh chỉnh mô hình Phi-3 / Phi-3.5 trong Microsoft Foundry và tích hợp nó với Prompt flow.

Trong hướng dẫn này, bạn sẽ triển khai mô hình Azure OpenAI làm bộ đánh giá trong Microsoft Foundry và sử dụng nó để đánh giá mô hình Phi-3 / Phi-3.5 đã được tinh chỉnh của bạn.

Trước khi bắt đầu hướng dẫn này, hãy đảm bảo bạn có các yêu cầu sau, như đã mô tả trong các hướng dẫn trước:

1. Một bộ dữ liệu đã chuẩn bị để đánh giá mô hình Phi-3 / Phi-3.5 đã tinh chỉnh.
1. Một mô hình Phi-3 / Phi-3.5 đã được tinh chỉnh và triển khai lên Azure Machine Learning.
1. Một Prompt flow đã tích hợp với mô hình Phi-3 / Phi-3.5 đã tinh chỉnh của bạn trong Microsoft Foundry.

> [!NOTE]
> Bạn sẽ sử dụng tệp *test_data.jsonl*, nằm trong thư mục dữ liệu từ bộ dữ liệu **ULTRACHAT_200k** đã tải về trong các bài blog trước, làm bộ dữ liệu để đánh giá mô hình Phi-3 / Phi-3.5 đã tinh chỉnh.

#### Tích hợp mô hình Phi-3 / Phi-3.5 tùy chỉnh với Prompt flow trong Microsoft Foundry (phương pháp code trước)

> [!NOTE]
> Nếu bạn đã theo phương pháp ít mã được mô tả trong "[Tinh chỉnh và Tích hợp Mô hình Phi-3 Tùy chỉnh với Prompt Flow trong Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", bạn có thể bỏ qua bài tập này và tiếp tục với bài tiếp theo.
> Tuy nhiên, nếu bạn đã theo phương pháp code trước được mô tả trong "[Tinh chỉnh và Tích hợp Mô hình Phi-3 Tùy chỉnh với Prompt Flow: Hướng dẫn từng bước](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" để tinh chỉnh và triển khai mô hình Phi-3 / Phi-3.5 của bạn, quy trình kết nối mô hình với Prompt flow sẽ hơi khác. Bạn sẽ học quy trình này trong bài tập này.

Để tiếp tục, bạn cần tích hợp mô hình Phi-3 / Phi-3.5 đã tinh chỉnh của mình vào Prompt flow trong Microsoft Foundry.

#### Tạo Microsoft Foundry Hub

Bạn cần tạo một Hub trước khi tạo Project. Một Hub giống như một Nhóm Tài nguyên, cho phép bạn tổ chức và quản lý nhiều Project trong Microsoft Foundry.
1. Đăng nhập vào [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Chọn **All hubs** từ tab bên trái.

1. Chọn **+ New hub** từ menu điều hướng.

    ![Create hub.](../../../../../../translated_images/vi/create-hub.5be78fb1e21ffbf1.webp)

1. Thực hiện các bước sau:

    - Nhập **Hub name**. Nó phải là một giá trị duy nhất.
    - Chọn **Subscription** Azure của bạn.
    - Chọn **Resource group** để sử dụng (tạo mới nếu cần).
    - Chọn **Location** bạn muốn sử dụng.
    - Chọn **Connect Azure AI Services** để sử dụng (tạo mới nếu cần).
    - Chọn **Connect Azure AI Search** để **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/vi/fill-hub.baaa108495c71e34.webp)

1. Chọn **Next**.

#### Tạo Dự án Microsoft Foundry

1. Trong Hub bạn đã tạo, chọn **All projects** từ tab bên trái.

1. Chọn **+ New project** từ menu điều hướng.

    ![Select new project.](../../../../../../translated_images/vi/select-new-project.cd31c0404088d7a3.webp)

1. Nhập **Project name**. Nó phải là một giá trị duy nhất.

    ![Create project.](../../../../../../translated_images/vi/create-project.ca3b71298b90e420.webp)

1. Chọn **Create a project**.

#### Thêm kết nối tùy chỉnh cho mô hình Phi-3 / Phi-3.5 được tinh chỉnh

Để tích hợp mô hình Phi-3 / Phi-3.5 tùy chỉnh của bạn với Prompt flow, bạn cần lưu endpoint và khóa của mô hình trong một kết nối tùy chỉnh. Thiết lập này đảm bảo truy cập đến mô hình Phi-3 / Phi-3.5 tùy chỉnh trong Prompt flow.

#### Thiết lập api key và endpoint uri của mô hình Phi-3 / Phi-3.5 được tinh chỉnh

1. Truy cập [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Điều hướng đến workspace Azure Machine Learning mà bạn đã tạo.

1. Chọn **Endpoints** từ tab bên trái.

    ![Select endpoints.](../../../../../../translated_images/vi/select-endpoints.ee7387ecd68bd18d.webp)

1. Chọn endpoint mà bạn đã tạo.

    ![Select endpoints.](../../../../../../translated_images/vi/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. Chọn **Consume** từ menu điều hướng.

1. Sao chép **REST endpoint** và **Primary key** của bạn.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/vi/copy-endpoint-key.0650c3786bd646ab.webp)

#### Thêm Kết nối Tùy chỉnh

1. Truy cập [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Điều hướng đến dự án Microsoft Foundry mà bạn đã tạo.

1. Trong Dự án bạn đã tạo, chọn **Settings** từ tab bên trái.

1. Chọn **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/vi/select-new-connection.fa0f35743758a74b.webp)

1. Chọn **Custom keys** từ menu điều hướng.

    ![Select custom keys.](../../../../../../translated_images/vi/select-custom-keys.5a3c6b25580a9b67.webp)

1. Thực hiện các bước sau:

    - Chọn **+ Add key value pairs**.
    - Đối với tên khóa, nhập **endpoint** và dán endpoint bạn đã sao chép từ Azure ML Studio vào trường giá trị.
    - Chọn lại **+ Add key value pairs**.
    - Đối với tên khóa, nhập **key** và dán khóa bạn đã sao chép từ Azure ML Studio vào trường giá trị.
    - Sau khi thêm các khóa, chọn **is secret** để khóa không bị lộ.

    ![Add connection.](../../../../../../translated_images/vi/add-connection.ac7f5faf8b10b0df.webp)

1. Chọn **Add connection**.

#### Tạo Prompt flow

Bạn đã thêm kết nối tùy chỉnh trong Microsoft Foundry. Bây giờ, hãy tạo Prompt flow theo các bước sau. Sau đó, bạn sẽ kết nối Prompt flow này với kết nối tùy chỉnh để sử dụng mô hình được tinh chỉnh trong Prompt flow.

1. Điều hướng đến dự án Microsoft Foundry mà bạn đã tạo.

1. Chọn **Prompt flow** từ tab bên trái.

1. Chọn **+ Create** từ menu điều hướng.

    ![Select Promptflow.](../../../../../../translated_images/vi/select-promptflow.18ff2e61ab9173eb.webp)

1. Chọn **Chat flow** từ menu điều hướng.

    ![Select chat flow.](../../../../../../translated_images/vi/select-flow-type.28375125ec9996d3.webp)

1. Nhập **Folder name** để sử dụng.

    ![Select chat flow.](../../../../../../translated_images/vi/enter-name.02ddf8fb840ad430.webp)

1. Chọn **Create**.

#### Cấu hình Prompt flow để chat với mô hình Phi-3 / Phi-3.5 tùy chỉnh của bạn

Bạn cần tích hợp mô hình Phi-3 / Phi-3.5 được tinh chỉnh vào Prompt flow. Tuy nhiên, Prompt flow hiện có không được thiết kế cho mục đích này. Vì vậy, bạn phải thiết kế lại Prompt flow để cho phép tích hợp mô hình tùy chỉnh.

1. Trong Prompt flow, thực hiện các bước sau để xây dựng lại luồng hiện có:

    - Chọn **Raw file mode**.
    - Xóa tất cả code hiện có trong file *flow.dag.yml*.
    - Thêm đoạn code sau vào *flow.dag.yml*.

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

    ![Select raw file mode.](../../../../../../translated_images/vi/select-raw-file-mode.06c1eca581ce4f53.webp)

1. Thêm đoạn code sau vào *integrate_with_promptflow.py* để sử dụng mô hình Phi-3 / Phi-3.5 tùy chỉnh trong Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Thiết lập ghi nhật ký
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "connection" là tên của Kết nối Tùy chỉnh, "endpoint", "key" là các khóa trong Kết nối Tùy chỉnh
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    data = {
        "input_data": [input_data],
        "params": {
            "temperature": 0.7,
            "max_new_tokens": 128,
            "do_sample": True,
            "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # Ghi lại toàn bộ phản hồi JSON
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
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Paste prompt flow code.](../../../../../../translated_images/vi/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> Để biết thêm thông tin chi tiết về việc sử dụng Prompt flow trong Microsoft Foundry, bạn có thể tham khảo [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Chọn **Chat input**, **Chat output** để kích hoạt chat với mô hình của bạn.

    ![Select Input Output.](../../../../../../translated_images/vi/select-input-output.c187fc58f25fbfc3.webp)

1. Bây giờ bạn đã sẵn sàng để chat với mô hình Phi-3 / Phi-3.5 tùy chỉnh của mình. Trong bài tập tiếp theo, bạn sẽ học cách khởi chạy Prompt flow và sử dụng nó để chat với mô hình Phi-3 / Phi-3.5 được tinh chỉnh.

> [!NOTE]
>
> Luồng được xây dựng lại sẽ trông như hình dưới đây:
>
> ![Flow example](../../../../../../translated_images/vi/graph-example.82fd1bcdd3fc545b.webp)
>

#### Bắt đầu Prompt flow

1. Chọn **Start compute sessions** để bắt đầu Prompt flow.

    ![Start compute session.](../../../../../../translated_images/vi/start-compute-session.9acd8cbbd2c43df1.webp)

1. Chọn **Validate and parse input** để làm mới các tham số.

    ![Validate input.](../../../../../../translated_images/vi/validate-input.c1adb9543c6495be.webp)

1. Chọn **Value** của **connection** tới kết nối tùy chỉnh bạn đã tạo. Ví dụ: *connection*.

    ![Connection.](../../../../../../translated_images/vi/select-connection.1f2b59222bcaafef.webp)

#### Chat với mô hình Phi-3 / Phi-3.5 tùy chỉnh của bạn

1. Chọn **Chat**.

    ![Select chat.](../../../../../../translated_images/vi/select-chat.0406bd9687d0c49d.webp)

1. Đây là ví dụ về kết quả: Bây giờ bạn có thể chat với mô hình Phi-3 / Phi-3.5 tùy chỉnh của mình. Nên đặt câu hỏi dựa trên dữ liệu đã sử dụng để tinh chỉnh.

    ![Chat with prompt flow.](../../../../../../translated_images/vi/chat-with-promptflow.1cf8cea112359ada.webp)

### Triển khai Azure OpenAI để đánh giá mô hình Phi-3 / Phi-3.5

Để đánh giá mô hình Phi-3 / Phi-3.5 trong Microsoft Foundry, bạn cần triển khai một mô hình Azure OpenAI. Mô hình này sẽ được sử dụng để đánh giá hiệu suất của mô hình Phi-3 / Phi-3.5.

#### Triển khai Azure OpenAI

1. Đăng nhập vào [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Điều hướng đến dự án Microsoft Foundry mà bạn đã tạo.

    ![Select Project.](../../../../../../translated_images/vi/select-project-created.5221e0e403e2c9d6.webp)

1. Trong Dự án bạn đã tạo, chọn **Deployments** từ tab bên trái.

1. Chọn **+ Deploy model** từ menu điều hướng.

1. Chọn **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/vi/deploy-openai-model.95d812346b25834b.webp)

1. Chọn mô hình Azure OpenAI mà bạn muốn sử dụng. Ví dụ, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/vi/select-openai-model.959496d7e311546d.webp)

1. Chọn **Confirm**.

### Đánh giá mô hình Phi-3 / Phi-3.5 được tinh chỉnh sử dụng Prompt flow của Microsoft Foundry

### Bắt đầu đánh giá mới

1. Truy cập [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Điều hướng đến dự án Microsoft Foundry mà bạn đã tạo.

    ![Select Project.](../../../../../../translated_images/vi/select-project-created.5221e0e403e2c9d6.webp)

1. Trong Dự án bạn đã tạo, chọn **Evaluation** từ tab bên trái.

1. Chọn **+ New evaluation** từ menu điều hướng.

    ![Select evaluation.](../../../../../../translated_images/vi/select-evaluation.2846ad7aaaca7f4f.webp)

1. Chọn đánh giá **Prompt flow**.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/vi/promptflow-evaluation.cb9758cc19b4760f.webp)

1. Thực hiện các bước sau:

    - Nhập tên đánh giá. Nó phải là giá trị duy nhất.
    - Chọn **Question and answer without context** làm loại nhiệm vụ. Vì bộ dữ liệu **ULTRACHAT_200k** được sử dụng trong hướng dẫn này không chứa ngữ cảnh.
    - Chọn prompt flow mà bạn muốn đánh giá.

    ![Prompt flow evaluation.](../../../../../../translated_images/vi/evaluation-setting1.4aa08259ff7a536e.webp)

1. Chọn **Next**.

1. Thực hiện các bước sau:

    - Chọn **Add your dataset** để tải bộ dữ liệu lên. Ví dụ, bạn có thể tải lên file bộ dữ liệu thử nghiệm, như *test_data.json1*, bao gồm khi bạn tải bộ dữ liệu **ULTRACHAT_200k**.
    - Chọn **Dataset column** phù hợp với bộ dữ liệu của bạn. Ví dụ, nếu bạn sử dụng bộ dữ liệu **ULTRACHAT_200k**, chọn **${data.prompt}** làm cột bộ dữ liệu.

    ![Prompt flow evaluation.](../../../../../../translated_images/vi/evaluation-setting2.07036831ba58d64e.webp)

1. Chọn **Next**.

1. Thực hiện các bước để cấu hình các chỉ số hiệu suất và chất lượng:

    - Chọn các chỉ số hiệu suất và chất lượng bạn muốn sử dụng.
    - Chọn mô hình Azure OpenAI bạn đã tạo để đánh giá. Ví dụ, chọn **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/vi/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. Thực hiện các bước cấu hình các chỉ số rủi ro và an toàn:

    - Chọn các chỉ số rủi ro và an toàn bạn muốn sử dụng.
    - Chọn ngưỡng để tính tỷ lệ lỗi bạn muốn sử dụng. Ví dụ, chọn **Medium**.
    - Đối với **question**, chọn **Data source** làm **{$data.prompt}**.
    - Đối với **answer**, chọn **Data source** làm **{$run.outputs.answer}**.
    - Đối với **ground_truth**, chọn **Data source** làm **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/vi/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. Chọn **Next**.

1. Chọn **Submit** để bắt đầu đánh giá.

1. Quá trình đánh giá sẽ mất một thời gian để hoàn thành. Bạn có thể theo dõi tiến trình ở tab **Evaluation**.

### Xem lại Kết quả Đánh giá

> [!NOTE]
> Các kết quả được trình bày dưới đây nhằm minh họa quá trình đánh giá. Trong hướng dẫn này, chúng tôi đã sử dụng một mô hình được tinh chỉnh trên bộ dữ liệu khá nhỏ, điều này có thể dẫn đến kết quả chưa tối ưu. Kết quả thực tế có thể khác biệt đáng kể dựa trên kích thước, chất lượng và đa dạng của bộ dữ liệu đã sử dụng, cũng như cấu hình cụ thể của mô hình.

Khi đánh giá hoàn tất, bạn có thể xem lại kết quả cho cả chỉ số hiệu suất và an toàn.
1. Các chỉ số hiệu suất và chất lượng:

    - đánh giá hiệu quả của mô hình trong việc tạo ra các phản hồi mạch lạc, trôi chảy và liên quan.

    ![Kết quả đánh giá.](../../../../../../translated_images/vi/evaluation-result-gpu.85f48b42dfb74254.webp)

1. Các chỉ số rủi ro và an toàn:

    - Đảm bảo đầu ra của mô hình an toàn và tuân thủ các Nguyên tắc AI Có Trách Nhiệm, tránh bất kỳ nội dung gây hại hoặc xúc phạm nào.

    ![Kết quả đánh giá.](../../../../../../translated_images/vi/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. Bạn có thể cuộn xuống để xem **Kết quả chi tiết các chỉ số**.

    ![Kết quả đánh giá.](../../../../../../translated_images/vi/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. Bằng cách đánh giá mô hình Phi-3 / Phi-3.5 tùy chỉnh của bạn dựa trên cả chỉ số hiệu suất và an toàn, bạn có thể xác nhận rằng mô hình không chỉ hiệu quả mà còn tuân thủ các thực hành AI có trách nhiệm, sẵn sàng cho việc triển khai thực tế.

## Chúc mừng!

### Bạn đã hoàn thành hướng dẫn này

Bạn đã đánh giá thành công mô hình Phi-3 được tinh chỉnh tích hợp với Prompt flow trong Microsoft Foundry. Đây là bước quan trọng để đảm bảo rằng các mô hình AI của bạn không chỉ hoạt động tốt mà còn tuân thủ các nguyên tắc AI có trách nhiệm của Microsoft, giúp bạn xây dựng các ứng dụng AI đáng tin cậy và tin cậy.

![Kiến trúc.](../../../../../../translated_images/vi/architecture.10bec55250f5d6a4.webp)

## Dọn dẹp tài nguyên Azure

Dọn dẹp các tài nguyên Azure của bạn để tránh phát sinh chi phí bổ sung cho tài khoản. Truy cập cổng Azure và xóa các tài nguyên sau:

- Tài nguyên Azure Machine learning.
- Điểm cuối mô hình Azure Machine learning.
- Tài nguyên Dự án Microsoft Foundry.
- Tài nguyên Prompt flow Microsoft Foundry.

### Bước tiếp theo

#### Tài liệu

- [Đánh giá hệ thống AI bằng bảng điều khiển Responsible AI](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Các chỉ số đánh giá và giám sát cho AI tạo sinh](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Tài liệu Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Tài liệu Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Nội dung đào tạo

- [Giới thiệu về Cách tiếp cận AI Có Trách Nhiệm của Microsoft](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Giới thiệu về Microsoft Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Tham khảo

- [AI Có Trách Nhiệm là gì?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Công bố các công cụ mới trong Azure AI giúp bạn xây dựng các ứng dụng AI tạo sinh an toàn và đáng tin cậy hơn](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Đánh giá các ứng dụng AI tạo sinh](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, khuyến nghị nên sử dụng dịch vụ dịch thuật chuyên nghiệp của con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc sai lệch nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->