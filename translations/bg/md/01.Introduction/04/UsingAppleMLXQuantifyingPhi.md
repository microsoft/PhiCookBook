<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-07-16T21:57:22+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "bg"
}
-->
# **Квантизиране на Phi-3.5 с помощта на Apple MLX Framework**

MLX е рамка за масиви, предназначена за изследвания в областта на машинното обучение на Apple silicon, разработена от екипа за машинно обучение на Apple.

MLX е създадена от изследователи в областта на машинното обучение за изследователи в същата област. Рамката е проектирана да бъде лесна за използване, но същевременно ефективна за обучение и внедряване на модели. Концептуалният дизайн на рамката също е опростен. Целта ни е да улесним изследователите да разширяват и подобряват MLX, за да могат бързо да изследват нови идеи.

Големите езикови модели (LLMs) могат да бъдат ускорени на устройства с Apple Silicon чрез MLX, а моделите могат да се изпълняват локално много удобно.

В момента Apple MLX Framework поддържа конверсия на квантизация за Phi-3.5-Instruct (**поддръжка от Apple MLX Framework**), Phi-3.5-Vision (**поддръжка от MLX-VLM Framework**) и Phi-3.5-MoE (**поддръжка от Apple MLX Framework**). Нека ги изпробваме:

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

### **🤖 Примери за Phi-3.5 с Apple MLX**

| Лаборатории    | Въведение | Отиди |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Научете как да използвате Phi-3.5 Instruct с Apple MLX framework   |  [Отиди](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | Научете как да използвате Phi-3.5 Vision за анализ на изображения с Apple MLX framework     |  [Отиди](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Научете как да използвате Phi-3.5 MoE с Apple MLX framework  |  [Отиди](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Ресурси**

1. Научете повече за Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub репозитория [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub репозитория [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.