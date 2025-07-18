<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-07-16T23:07:35+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "sr"
}
-->
[OpenVino Chat пример](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Овај код извози модел у OpenVINO формат, учитава га и користи за генерисање одговора на дати упит.

1. **Извоз модела**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Ова команда користи `optimum-cli` алат за извоз модела у OpenVINO формат, који је оптимизован за ефикасно извођење.
   - Модел који се извози је `"microsoft/Phi-3-mini-4k-instruct"`, и подешен је за задатак генерисања текста на основу претходног контекста.
   - Тежине модела су квантизоване у 4-битне целе бројеве (`int4`), што помаже у смањењу величине модела и убрзава обраду.
   - Остали параметри као што су `group-size`, `ratio` и `sym` користе се за прецизније подешавање процеса квантизације.
   - Извезени модел се чува у директоријуму `./model/phi3-instruct/int4`.

2. **Увоз потребних библиотека**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Ове линије увозе класе из `transformers` библиотеке и `optimum.intel.openvino` модула, које су потребне за учитавање и коришћење модела.

3. **Подешавање директоријума модела и конфигурације**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` одређује где се налазе фајлови модела.
   - `ov_config` је речник који конфигурише OpenVINO модел да приоритет даје ниској латенцији, користи један inference stream и да не користи кеш директоријум.

4. **Учитавање модела**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Ова линија учитава модел из назначеног директоријума, користећи претходно дефинисане конфигурационе параметре. Такође омогућава извршавање удаљеног кода ако је потребно.

5. **Учитавање токенизера**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Ова линија учитава токенизер, који је задужен за претварање текста у токене које модел може да разуме.

6. **Подешавање аргумената за токенизер**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Овај речник одређује да се специјални токени не додају у резултат токенизације.

7. **Дефинисање упита**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Овај низ поставља разговорни упит у коме корисник тражи од AI асистента да се представи.

8. **Токенизација упита**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Ова линија претвара упит у токене које модел може да обради, враћајући резултат као PyTorch тензоре.

9. **Генерисање одговора**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Ова линија користи модел за генерисање одговора на основу улазних токена, са максимално 1024 нова токена.

10. **Декодирање одговора**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Ова линија претвара генерисане токене назад у читљив текст, прескачући специјалне токене, и враћа први резултат.

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.