<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-07-16T21:52:26+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "ru"
}
-->
# **Квантование Phi-3.5 с использованием Apple MLX Framework**

MLX — это фреймворк для исследований в области машинного обучения на Apple Silicon, разработанный командой Apple по исследованию машинного обучения.

MLX создан исследователями машинного обучения для исследователей машинного обучения. Фреймворк ориентирован на удобство использования, при этом оставаясь эффективным для обучения и развертывания моделей. Концепция самого фреймворка также проста. Мы стремимся сделать MLX легко расширяемым и улучшаемым, чтобы исследователи могли быстро проверять новые идеи.

LLM можно ускорять на устройствах Apple Silicon с помощью MLX, а модели удобно запускать локально.

Сейчас Apple MLX Framework поддерживает конвертацию квантования для Phi-3.5-Instruct (**поддержка Apple MLX Framework**), Phi-3.5-Vision (**поддержка MLX-VLM Framework**), и Phi-3.5-MoE (**поддержка Apple MLX Framework**). Давайте попробуем:

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
| -------- | ------- |  ------- |
| 🚀 Лаборатория — Введение в Phi-3.5 Instruct  | Узнайте, как использовать Phi-3.5 Instruct с фреймворком Apple MLX   |  [Перейти](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Лаборатория — Введение в Phi-3.5 Vision (изображения) | Узнайте, как использовать Phi-3.5 Vision для анализа изображений с помощью Apple MLX   |  [Перейти](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Лаборатория — Введение в Phi-3.5 Vision (moE)   | Узнайте, как использовать Phi-3.5 MoE с фреймворком Apple MLX  |  [Перейти](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Ресурсы**

1. Узнайте больше об Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Репозиторий Apple MLX на GitHub [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. Репозиторий MLX-VLM на GitHub [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному переводу, выполненному человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.