<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-07-16T21:57:30+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "sr"
}
-->
# **Квантизација Phi-3.5 уз помоћ Apple MLX Framework-а**

MLX је фрејмворк за машинско учење на Apple силицијуму, развијен од стране Apple истраживача машинског учења.

MLX је дизајниран од стране истраживача машинског учења за истраживаче машинског учења. Фрејмворк је намењен да буде једноставан за коришћење, али и ефикасан за тренирање и покретање модела. Сам дизајн фрејмворка је концептуално једноставан. Желимо да омогућимо истраживачима да лако проширују и унапређују MLX са циљем брзог испробавања нових идеја.

LLM модели могу бити убрзани на Apple Silicon уређајима преко MLX-а, а модели се могу покретати локално на веома згодан начин.

Сада Apple MLX Framework подржава конверзију квантизације за Phi-3.5-Instruct (**подршка Apple MLX Framework-а**), Phi-3.5-Vision (**подршка MLX-VLM Framework-а**) и Phi-3.5-MoE (**подршка Apple MLX Framework-а**). Хајде да пробамо следеће:

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

### **🤖 Примери за Phi-3.5 уз Apple MLX**

| Лабораторија | Увод | Иди |
| -------- | ------- | ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Научите како да користите Phi-3.5 Instruct уз Apple MLX framework   |  [Иди](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (слика) | Научите како да користите Phi-3.5 Vision за анализу слика уз Apple MLX framework     |  [Иди](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Научите како да користите Phi-3.5 MoE уз Apple MLX framework  |  [Иди](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Ресурси**

1. Сазнајте више о Apple MLX Framework-у [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub репозиторијум [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub репозиторијум [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.