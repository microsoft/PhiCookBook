<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-05-09T15:57:39+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "vi"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Mã này xuất một mô hình sang định dạng OpenVINO, tải mô hình đó và sử dụng nó để tạo phản hồi cho một lời nhắc nhất định.

1. **Xuất Mô Hình**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Lệnh này sử dụng `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **Nhập Các Thư Viện Cần Thiết**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Các dòng này nhập các lớp từ module `transformers` library and the `optimum.intel.openvino`, cần thiết để tải và sử dụng mô hình.

3. **Thiết Lập Thư Mục Mô Hình và Cấu Hình**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` là một dictionary cấu hình mô hình OpenVINO ưu tiên độ trễ thấp, sử dụng một luồng suy luận, và không sử dụng thư mục cache.

4. **Tải Mô Hình**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Dòng này tải mô hình từ thư mục đã chỉ định, sử dụng các thiết lập cấu hình đã định nghĩa trước đó. Nó cũng cho phép thực thi mã từ xa nếu cần.

5. **Tải Bộ Mã Hóa (Tokenizer)**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Dòng này tải bộ mã hóa, chịu trách nhiệm chuyển đổi văn bản thành các token mà mô hình có thể hiểu.

6. **Thiết Lập Tham Số Cho Bộ Mã Hóa**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Dictionary này chỉ định không thêm các token đặc biệt vào kết quả đã được mã hóa.

7. **Định Nghĩa Lời Nhắc**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Chuỗi này thiết lập lời nhắc hội thoại, trong đó người dùng yêu cầu trợ lý AI tự giới thiệu về bản thân.

8. **Mã Hóa Lời Nhắc**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Dòng này chuyển lời nhắc thành các token để mô hình xử lý, trả về kết quả dưới dạng tensor PyTorch.

9. **Tạo Phản Hồi**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Dòng này sử dụng mô hình để tạo phản hồi dựa trên các token đầu vào, với tối đa 1024 token mới.

10. **Giải Mã Phản Hồi**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Dòng này chuyển các token đã tạo thành chuỗi có thể đọc được, bỏ qua các token đặc biệt, và lấy kết quả đầu tiên.

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc sự không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, khuyến nghị nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hay giải thích sai nào phát sinh từ việc sử dụng bản dịch này.