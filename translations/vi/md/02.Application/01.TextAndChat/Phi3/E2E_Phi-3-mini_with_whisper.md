<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-05-09T18:32:41+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "vi"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot với Whisper

## Tổng quan

Interactive Phi 3 Mini 4K Instruct Chatbot là một công cụ cho phép người dùng tương tác với bản demo Microsoft Phi 3 Mini 4K instruct thông qua đầu vào bằng văn bản hoặc âm thanh. Chatbot có thể được sử dụng cho nhiều nhiệm vụ khác nhau, như dịch thuật, cập nhật thời tiết và thu thập thông tin chung.

### Bắt đầu

Để sử dụng chatbot này, chỉ cần làm theo các hướng dẫn sau:

1. Mở file [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. Trong cửa sổ chính của notebook, bạn sẽ thấy giao diện hộp chat với ô nhập văn bản và nút "Send".
3. Để sử dụng chatbot dựa trên văn bản, chỉ cần nhập tin nhắn của bạn vào ô nhập văn bản và nhấn nút "Send". Chatbot sẽ phản hồi bằng một file âm thanh có thể phát trực tiếp ngay trong notebook.

**Note**: Công cụ này yêu cầu GPU và quyền truy cập vào các mô hình Microsoft Phi-3 và OpenAI Whisper, được sử dụng cho nhận dạng giọng nói và dịch thuật.

### Yêu cầu GPU

Để chạy demo này bạn cần 12GB bộ nhớ GPU.

Yêu cầu bộ nhớ để chạy demo **Microsoft-Phi-3-Mini-4K instruct** trên GPU sẽ phụ thuộc vào nhiều yếu tố, như kích thước dữ liệu đầu vào (âm thanh hoặc văn bản), ngôn ngữ dùng để dịch, tốc độ mô hình và bộ nhớ khả dụng trên GPU.

Thông thường, mô hình Whisper được thiết kế để chạy trên GPU. Dung lượng bộ nhớ GPU tối thiểu được khuyến nghị để chạy mô hình Whisper là 8 GB, nhưng nó có thể xử lý bộ nhớ lớn hơn nếu cần.

Cần lưu ý rằng khi chạy lượng dữ liệu lớn hoặc số lượng yêu cầu cao trên mô hình có thể cần nhiều bộ nhớ GPU hơn và/hoặc có thể gây ra vấn đề về hiệu suất. Khuyến khích bạn thử nghiệm trường hợp sử dụng với các cấu hình khác nhau và theo dõi việc sử dụng bộ nhớ để xác định cấu hình tối ưu cho nhu cầu cụ thể của bạn.

## Ví dụ E2E cho Interactive Phi 3 Mini 4K Instruct Chatbot với Whisper

Notebook jupyter có tên [Interactive Phi 3 Mini 4K Instruct Chatbot với Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) minh họa cách sử dụng Microsoft Phi 3 Mini 4K instruct Demo để tạo văn bản từ âm thanh hoặc đầu vào văn bản. Notebook định nghĩa một số hàm:

1. `tts_file_name(text)`: Hàm này tạo tên file dựa trên văn bản đầu vào để lưu file âm thanh đã tạo.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Hàm này sử dụng API Edge TTS để tạo file âm thanh từ danh sách các đoạn văn bản. Các tham số đầu vào là danh sách các đoạn, tốc độ nói, tên giọng nói và đường dẫn lưu file âm thanh tạo ra.
1. `talk(input_text)`: Hàm này tạo file âm thanh bằng cách sử dụng API Edge TTS và lưu vào tên file ngẫu nhiên trong thư mục /content/audio. Tham số đầu vào là văn bản sẽ được chuyển thành giọng nói.
1. `run_text_prompt(message, chat_history)`: Hàm này sử dụng demo Microsoft Phi 3 Mini 4K instruct để tạo file âm thanh từ tin nhắn đầu vào và thêm nó vào lịch sử trò chuyện.
1. `run_audio_prompt(audio, chat_history)`: Hàm này chuyển file âm thanh thành văn bản bằng API mô hình Whisper và truyền kết quả cho hàm `run_text_prompt()`.
1. Mã nguồn khởi chạy ứng dụng Gradio cho phép người dùng tương tác với demo Phi 3 Mini 4K instruct bằng cách nhập tin nhắn hoặc tải file âm thanh lên. Kết quả được hiển thị dưới dạng tin nhắn văn bản trong ứng dụng.

## Khắc phục sự cố

Cài đặt driver Cuda GPU

1. Đảm bảo hệ điều hành Linux của bạn được cập nhật

    ```bash
    sudo apt update
    ```

1. Cài đặt driver Cuda

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Đăng ký vị trí driver cuda

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Kiểm tra dung lượng bộ nhớ Nvidia GPU (Yêu cầu 12GB bộ nhớ GPU)

    ```bash
    nvidia-smi
    ```

1. Xóa bộ nhớ đệm: Nếu bạn dùng PyTorch, bạn có thể gọi torch.cuda.empty_cache() để giải phóng toàn bộ bộ nhớ đệm không sử dụng, giúp các ứng dụng GPU khác có thể dùng.

    ```python
    torch.cuda.empty_cache() 
    ```

1. Kiểm tra Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Thực hiện các bước sau để tạo token Hugging Face.

    - Truy cập [Trang cài đặt Token Hugging Face](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Chọn **New token**.
    - Nhập tên dự án bạn muốn sử dụng.
    - Chọn **Type** thành **Write**.

> **Note**
>
> Nếu bạn gặp lỗi sau:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Để khắc phục, hãy nhập lệnh sau trong terminal của bạn.
>
> ```bash
> sudo ldconfig
> ```

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc nên được xem là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hay giải thích sai nào phát sinh từ việc sử dụng bản dịch này.