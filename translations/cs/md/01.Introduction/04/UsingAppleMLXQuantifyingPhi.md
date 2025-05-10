<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-05-09T13:49:31+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "cs"
}
-->
# **Квантование Phi-3.5 с использованием Apple MLX Framework**

MLX — это фреймворк для машинного обучения на Apple silicon, разработанный исследователями машинного обучения Apple.

MLX создан исследователями машинного обучения для исследователей машинного обучения. Фреймворк ориентирован на удобство использования, но при этом эффективен для обучения и развертывания моделей. Его архитектура также концептуально проста. Мы стремимся сделать MLX легко расширяемым и улучшаемым, чтобы исследователи могли быстро экспериментировать с новыми идеями.

LLM можно ускорять на устройствах Apple Silicon с помощью MLX, а модели удобно запускать локально.

Сейчас Apple MLX Framework поддерживает преобразование квантования Phi-3.5-Instruct (**поддержка Apple MLX Framework**), Phi-3.5-Vision (**поддержка MLX-VLM Framework**), и Phi-3.5-MoE (**поддержка Apple MLX Framework**). Попробуем далее:

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

| Labs    | Описание | Перейти |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Узнайте, как использовать Phi-3.5 Instruct с Apple MLX framework   |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | Узнайте, как использовать Phi-3.5 Vision для анализа изображений с Apple MLX framework     |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Узнайте, как использовать Phi-3.5 MoE с Apple MLX framework  |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Ресурсы**

1. Узнайте об Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Репозиторий Apple MLX на GitHub [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. Репозиторий MLX-VLM на GitHub [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.