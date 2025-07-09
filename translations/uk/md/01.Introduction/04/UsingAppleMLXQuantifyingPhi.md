<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-07-09T19:45:56+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "uk"
}
-->
# **Квантизація Phi-3.5 за допомогою Apple MLX Framework**

MLX — це фреймворк для машинного навчання на Apple Silicon, розроблений дослідниками машинного навчання Apple.

MLX створений дослідниками машинного навчання для дослідників машинного навчання. Фреймворк має бути зручним у використанні, але водночас ефективним для навчання та розгортання моделей. Концепція самого фреймворку також досить проста. Ми прагнемо зробити його легким для розширення та вдосконалення дослідниками, щоб швидко експериментувати з новими ідеями.

Великі мовні моделі (LLM) можна прискорювати на пристроях Apple Silicon за допомогою MLX, а моделі можна запускати локально дуже зручно.

Зараз Apple MLX Framework підтримує конвертацію квантизації для Phi-3.5-Instruct (**підтримка Apple MLX Framework**), Phi-3.5-Vision (**підтримка MLX-VLM Framework**), та Phi-3.5-MoE (**підтримка Apple MLX Framework**). Спробуємо далі:

### **Phi-3.5-Instruct**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-mini-instruct -q

```

### **Phi-3.5-Vision**

```bash

python -m mlxv_lm.convert --hf-path microsoft/Phi-3.5-vision-instruct -q

```

### **Phi-3.5-MoE**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-MoE-instruct  -q

```

### **🤖 Приклади для Phi-3.5 з Apple MLX**

| Лабораторії    | Опис | Перейти |
| -------- | ------- |  ------- |
| 🚀 Лабораторія: Вступ до Phi-3.5 Instruct  | Дізнайтеся, як використовувати Phi-3.5 Instruct з Apple MLX framework   |  [Перейти](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Лабораторія: Вступ до Phi-3.5 Vision (зображення) | Дізнайтеся, як аналізувати зображення за допомогою Phi-3.5 Vision та Apple MLX framework     |  [Перейти](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Лабораторія: Вступ до Phi-3.5 Vision (moE)   | Дізнайтеся, як використовувати Phi-3.5 MoE з Apple MLX framework  |  [Перейти](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Ресурси**

1. Дізнайтеся про Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Репозиторій Apple MLX на GitHub [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. Репозиторій MLX-VLM на GitHub [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.