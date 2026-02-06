[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Цей код експортує модель у формат OpenVINO, завантажує її та використовує для генерації відповіді на заданий запит.

1. **Експорт моделі**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Ця команда використовує інструмент `optimum-cli` для експорту моделі у формат OpenVINO, оптимізований для ефективного виконання.
   - Експортується модель `"microsoft/Phi-3-mini-4k-instruct"`, налаштована для завдання генерації тексту на основі попереднього контексту.
   - Ваги моделі квантизовані до 4-бітних цілих чисел (`int4`), що допомагає зменшити розмір моделі та прискорити обробку.
   - Інші параметри, такі як `group-size`, `ratio` та `sym`, використовуються для тонкого налаштування процесу квантизації.
   - Експортована модель зберігається у директорії `./model/phi3-instruct/int4`.

2. **Імпорт необхідних бібліотек**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Ці рядки імпортують класи з бібліотеки `transformers` та модуля `optimum.intel.openvino`, які потрібні для завантаження та використання моделі.

3. **Налаштування директорії моделі та конфігурації**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` вказує, де зберігаються файли моделі.
   - `ov_config` — словник, який налаштовує модель OpenVINO для пріоритету низької затримки, використання одного потоку інференсу та відсутності кешування.

4. **Завантаження моделі**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Цей рядок завантажує модель із вказаної директорії, використовуючи раніше визначені налаштування. Також дозволяє виконання віддаленого коду за потреби.

5. **Завантаження токенізатора**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Цей рядок завантажує токенізатор, який відповідає за перетворення тексту у токени, зрозумілі моделі.

6. **Налаштування аргументів токенізатора**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Цей словник вказує, що спеціальні токени не повинні додаватися до токенізованого результату.

7. **Визначення запиту (prompt)**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Цей рядок задає текст запиту, де користувач просить AI-асистента представитися.

8. **Токенізація запиту**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Цей рядок перетворює запит у токени, які модель може обробити, повертаючи результат у вигляді тензорів PyTorch.

9. **Генерація відповіді**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Цей рядок використовує модель для генерації відповіді на основі вхідних токенів, з максимальною довжиною 1024 нових токенів.

10. **Декодування відповіді**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Цей рядок перетворює згенеровані токени назад у зрозумілий текст, пропускаючи спеціальні токени, і отримує перший результат.

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.