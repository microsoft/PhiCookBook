<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-07-16T23:07:26+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "bg"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Този код експортира модел във формат OpenVINO, зарежда го и го използва за генериране на отговор на даден въпрос.

1. **Експортиране на модела**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Тази команда използва инструмента `optimum-cli` за експортиране на модел във формат OpenVINO, който е оптимизиран за ефективно извеждане.
   - Моделът, който се експортира, е `"microsoft/Phi-3-mini-4k-instruct"` и е настроен за задача за генериране на текст въз основа на предишен контекст.
   - Теглата на модела са квантизирани до 4-битови цели числа (`int4`), което помага за намаляване на размера на модела и ускоряване на обработката.
   - Други параметри като `group-size`, `ratio` и `sym` се използват за фина настройка на процеса на квантизация.
   - Експортираният модел се запазва в директорията `./model/phi3-instruct/int4`.

2. **Импортиране на необходими библиотеки**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Тези редове импортират класове от библиотеката `transformers` и модула `optimum.intel.openvino`, които са нужни за зареждане и използване на модела.

3. **Настройка на директорията на модела и конфигурацията**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` указва къде се съхраняват файловете на модела.
   - `ov_config` е речник, който конфигурира OpenVINO модела да приоритизира ниска латентност, да използва един inference поток и да не използва кеш директория.

4. **Зареждане на модела**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Този ред зарежда модела от посочената директория, използвайки предварително дефинираните настройки. Позволява се и изпълнение на отдалечен код, ако е необходимо.

5. **Зареждане на токенизатора**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Този ред зарежда токенизатора, който отговаря за преобразуването на текст в токени, които моделът може да разбере.

6. **Настройка на аргументите за токенизатора**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Този речник указва, че специални токени не трябва да се добавят към токенизирания изход.

7. **Дефиниране на подканата (prompt)**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Този низ задава разговорна подканa, в която потребителят моли AI асистента да се представи.

8. **Токенизиране на подканата**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Този ред преобразува подканата в токени, които моделът може да обработи, като връща резултата като PyTorch тензори.

9. **Генериране на отговор**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Този ред използва модела за генериране на отговор въз основа на входните токени, с максимум 1024 нови токена.

10. **Декодиране на отговора**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Този ред преобразува генерираните токени обратно в четим за човек низ, пропускайки специалните токени, и извлича първия резултат.

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.