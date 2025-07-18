<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-07-16T23:01:19+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "ru"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Этот код экспортирует модель в формат OpenVINO, загружает её и использует для генерации ответа на заданный запрос.

1. **Экспорт модели**:  
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```  
   - Эта команда использует инструмент `optimum-cli` для экспорта модели в формат OpenVINO, оптимизированный для эффективного вывода.  
   - Экспортируется модель `"microsoft/Phi-3-mini-4k-instruct"`, предназначенная для задачи генерации текста на основе предыдущего контекста.  
   - Веса модели квантизируются до 4-битных целых чисел (`int4`), что помогает уменьшить размер модели и ускорить обработку.  
   - Другие параметры, такие как `group-size`, `ratio` и `sym`, используются для тонкой настройки процесса квантизации.  
   - Экспортированная модель сохраняется в директории `./model/phi3-instruct/int4`.

2. **Импорт необходимых библиотек**:  
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```  
   - Эти строки импортируют классы из библиотеки `transformers` и модуля `optimum.intel.openvino`, которые нужны для загрузки и использования модели.

3. **Настройка директории модели и конфигурации**:  
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```  
   - `model_dir` указывает путь к файлам модели.  
   - `ov_config` — словарь с настройками модели OpenVINO, который приоритетно выбирает низкую задержку, использует один поток вывода и не применяет кэширование.

4. **Загрузка модели**:  
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```  
   - Эта строка загружает модель из указанной директории с использованием ранее заданных настроек. Также разрешается выполнение удалённого кода при необходимости.

5. **Загрузка токенизатора**:  
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```  
   - Эта строка загружает токенизатор, который отвечает за преобразование текста в токены, понятные модели.

6. **Настройка аргументов токенизатора**:  
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```  
   - Этот словарь указывает, что специальные токены не должны добавляться к токенизированному выводу.

7. **Определение запроса**:  
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```  
   - Эта строка задаёт текст запроса, в котором пользователь просит AI-ассистента представиться.

8. **Токенизация запроса**:  
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```  
   - Эта строка преобразует запрос в токены, которые модель может обработать, возвращая результат в виде тензоров PyTorch.

9. **Генерация ответа**:  
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```  
   - Эта строка использует модель для генерации ответа на основе входных токенов с максимальной длиной 1024 новых токенов.

10. **Декодирование ответа**:  
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```  
    - Эта строка преобразует сгенерированные токены обратно в читаемую строку, пропуская специальные токены, и возвращает первый результат.

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.