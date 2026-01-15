<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7f72d7981ed3640865700f51ae407da4",
  "translation_date": "2026-01-14T15:52:22+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "vi"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot với Whisper

## Tổng quan

Interactive Phi 3 Mini 4K Instruct Chatbot là một công cụ cho phép người dùng tương tác với bản demo Microsoft Phi 3 Mini 4K instruct bằng cách nhập liệu văn bản hoặc âm thanh. Chatbot có thể được sử dụng cho nhiều tác vụ khác nhau, như dịch thuật, cập nhật thời tiết và thu thập thông tin chung.

### Bắt đầu

Để sử dụng chatbot này, chỉ cần làm theo các hướng dẫn sau:

1. Mở một [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) mới
2. Trong cửa sổ chính của notebook, bạn sẽ thấy giao diện hộp thoại trò chuyện với một hộp nhập văn bản và nút "Send".
3. Để sử dụng chatbot dựa trên văn bản, chỉ cần gõ tin nhắn của bạn vào hộp nhập văn bản và nhấn nút "Send". Chatbot sẽ phản hồi bằng một tệp âm thanh có thể phát trực tiếp ngay trong notebook.

**Lưu ý**: Công cụ này yêu cầu GPU và quyền truy cập vào các mô hình Microsoft Phi-3 và OpenAI Whisper, được dùng cho nhận dạng giọng nói và dịch thuật.

### Yêu cầu GPU

Để chạy bản demo này, bạn cần 12Gb bộ nhớ GPU.

Yêu cầu bộ nhớ để chạy bản demo **Microsoft-Phi-3-Mini-4K instruct** trên GPU sẽ phụ thuộc vào nhiều yếu tố, như kích thước dữ liệu đầu vào (âm thanh hoặc văn bản), ngôn ngữ được dùng để dịch, tốc độ mô hình, và bộ nhớ có sẵn trên GPU.

Nói chung, mô hình Whisper được thiết kế để chạy trên GPU. Dung lượng bộ nhớ GPU tối thiểu được khuyến nghị để chạy mô hình Whisper là 8 GB, nhưng nó có thể xử lý lượng bộ nhớ lớn hơn nếu cần.

Điều quan trọng là lưu ý rằng chạy một lượng lớn dữ liệu hoặc số lượng lớn các yêu cầu trên mô hình có thể yêu cầu nhiều bộ nhớ GPU hơn và/hoặc có thể gây ra các vấn đề về hiệu suất. Khuyến nghị bạn nên thử nghiệm trường hợp sử dụng của mình với các cấu hình khác nhau và theo dõi việc sử dụng bộ nhớ để xác định các cài đặt tối ưu cho nhu cầu cụ thể của bạn.

## Ví dụ E2E cho Interactive Phi 3 Mini 4K Instruct Chatbot với Whisper

Notebook jupyter có tên [Interactive Phi 3 Mini 4K Instruct Chatbot với Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) trình bày cách sử dụng Demo Microsoft Phi 3 Mini 4K instruct để tạo văn bản từ đầu vào âm thanh hoặc văn bản. Notebook định nghĩa một số hàm:

1. `tts_file_name(text)`: Hàm này tạo tên tệp dựa trên văn bản đầu vào để lưu tệp âm thanh được tạo.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Hàm này sử dụng API Edge TTS để tạo tệp âm thanh từ danh sách các đoạn văn bản đầu vào. Tham số đầu vào là danh sách đoạn, tốc độ lời nói, tên giọng nói, và đường dẫn lưu tệp âm thanh đầu ra.
1. `talk(input_text)`: Hàm này tạo tệp âm thanh bằng cách sử dụng API Edge TTS và lưu vào một tên tệp ngẫu nhiên trong thư mục /content/audio. Tham số đầu vào là văn bản cần chuyển đổi thành giọng nói.
1. `run_text_prompt(message, chat_history)`: Hàm này sử dụng bản demo Microsoft Phi 3 Mini 4K instruct tạo tệp âm thanh từ tin nhắn đầu vào và thêm nó vào lịch sử trò chuyện.
1. `run_audio_prompt(audio, chat_history)`: Hàm này chuyển đổi tệp âm thanh thành văn bản bằng API mô hình Whisper và truyền văn bản đó vào hàm `run_text_prompt()`.
1. Mã khởi chạy một ứng dụng Gradio cho phép người dùng tương tác với bản demo Phi 3 Mini 4K instruct bằng cách gõ tin nhắn hoặc tải lên tệp âm thanh. Kết quả đầu ra được hiển thị thành tin nhắn văn bản bên trong ứng dụng.

## Xử lý sự cố

Cài đặt driver Cuda GPU

1. Đảm bảo ứng dụng Linux của bạn được cập nhật

    ```bash
    sudo apt update
    ```

1. Cài đặt Driver Cuda

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Đăng ký vị trí driver cuda

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Kiểm tra kích thước bộ nhớ Nvidia GPU (Yêu cầu 12GB bộ nhớ GPU)

    ```bash
    nvidia-smi
    ```

1. Dọn Cache: Nếu bạn sử dụng PyTorch, bạn có thể gọi torch.cuda.empty_cache() để giải phóng tất cả bộ nhớ cache không sử dụng, giúp bộ nhớ đó có thể được các ứng dụng GPU khác sử dụng

    ```python
    torch.cuda.empty_cache() 
    ```

1. Kiểm tra Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Thực hiện các bước sau để tạo token Hugging Face.

    - Truy cập trang [Cài đặt Token Hugging Face](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Chọn **New token**.
    - Nhập **Name** dự án bạn muốn sử dụng.
    - Chọn **Type** thành **Write**.

> [!NOTE]
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

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ nguyên bản được coi là nguồn đáng tin cậy và chính thức. Đối với thông tin quan trọng, nên sử dụng dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc dịch sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->