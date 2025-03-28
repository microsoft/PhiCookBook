<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-03-27T08:25:57+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingAppleMLXQuantifyingPhi.md",
  "language_code": "ru"
}
-->
# **Квантование Phi-3.5 с использованием Apple MLX Framework**

MLX — это фреймворк для работы с массивами в исследованиях машинного обучения на устройствах с Apple Silicon, разработанный исследователями машинного обучения Apple.

MLX создан исследователями машинного обучения для исследователей машинного обучения. Этот фреймворк разработан таким образом, чтобы быть простым в использовании, но при этом эффективным для обучения и развертывания моделей. Концептуально дизайн фреймворка также предельно прост. Мы стремимся сделать его удобным для расширения и улучшения, чтобы исследователи могли быстро проверять новые идеи.

LLM-модели могут быть ускорены на устройствах с Apple Silicon с помощью MLX, а модели можно запускать локально с большим удобством.

Теперь Apple MLX Framework поддерживает квантованное преобразование Phi-3.5-Instruct (**поддержка Apple MLX Framework**), Phi-3.5-Vision (**поддержка MLX-VLM Framework**) и Phi-3.5-MoE (**поддержка Apple MLX Framework**). Давайте попробуем это:

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

### **🤖 Примеры для Phi-3.5 с Apple MLX**

| Лаборатории    | Описание | Перейти |
| -------------- | -------- | ------- |
| 🚀 Лаборатория: Введение в Phi-3.5 Instruct  | Узнайте, как использовать Phi-3.5 Instruct с Apple MLX Framework   |  [Перейти](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Лаборатория: Введение в Phi-3.5 Vision (анализ изображений) | Узнайте, как использовать Phi-3.5 Vision для анализа изображений с помощью Apple MLX Framework     |  [Перейти](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Лаборатория: Введение в Phi-3.5 MoE   | Узнайте, как использовать Phi-3.5 MoE с Apple MLX Framework  |  [Перейти](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Ресурсы**

1. Узнайте больше об Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Репозиторий Apple MLX на GitHub [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. Репозиторий MLX-VLM на GitHub [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, пожалуйста, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникающие в результате использования данного перевода.