<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-05-09T13:50:40+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "bg"
}
-->
# **Квантизиране на Phi-3.5 с помощта на Apple MLX Framework**

MLX е рамка за машинно обучение, създадена за изследвания върху Apple silicon, разработена от екипа за машинно обучение на Apple.

MLX е проектирана от изследователи в областта на машинното обучение за изследователи. Рамката е създадена да бъде лесна за използване, но същевременно ефективна за обучение и внедряване на модели. Концептуалният дизайн на рамката е опростен. Целта ни е да улесним изследователите в разширяването и подобряването на MLX, за да могат бързо да изследват нови идеи.

Големите езикови модели (LLMs) могат да се ускорят на устройства с Apple Silicon чрез MLX, а моделите могат да се изпълняват локално много удобно.

Сега Apple MLX Framework поддържа квантизационно преобразуване на Phi-3.5-Instruct (**поддръжка от Apple MLX Framework**), Phi-3.5-Vision (**поддръжка от MLX-VLM Framework**) и Phi-3.5-MoE (**поддръжка от Apple MLX Framework**). Нека да ги изпробваме:

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

| Лаборатории | Въведение | Отиди |
| -------- | ------- | ------- |
| 🚀 Лаборатория - Въведение в Phi-3.5 Instruct | Научете как да използвате Phi-3.5 Instruct с рамката Apple MLX | [Отиди](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb) |
| 🚀 Лаборатория - Въведение в Phi-3.5 Vision (изображение) | Научете как да използвате Phi-3.5 Vision за анализ на изображения с рамката Apple MLX | [Отиди](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb) |
| 🚀 Лаборатория - Въведение в Phi-3.5 Vision (moE) | Научете как да използвате Phi-3.5 MoE с рамката Apple MLX | [Отиди](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb) |

## **Ресурси**

1. Научете повече за Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub Репозитория [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub Репозитория [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или погрешни тълкувания, възникнали от използването на този превод.