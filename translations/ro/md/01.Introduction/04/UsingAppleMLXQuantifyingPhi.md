# **Cuantificarea Phi-3.5 folosind Apple MLX Framework**

MLX este un framework pentru array-uri destinat cercetării în învățarea automată pe siliciu Apple, dezvoltat de echipa de cercetare Apple în domeniul învățării automate.

MLX este creat de cercetători în învățarea automată pentru cercetători în același domeniu. Framework-ul este conceput să fie prietenos cu utilizatorul, dar în același timp eficient pentru antrenarea și implementarea modelelor. Designul framework-ului este, de asemenea, simplu din punct de vedere conceptual. Ne propunem să facilităm extinderea și îmbunătățirea MLX de către cercetători, cu scopul de a explora rapid idei noi.

Modelele LLM pot fi accelerate pe dispozitivele Apple Silicon prin MLX, iar modelele pot fi rulate local foarte convenabil.

Acum, Apple MLX Framework suportă conversia prin cuantificare pentru Phi-3.5-Instruct (**suport Apple MLX Framework**), Phi-3.5-Vision (**suport MLX-VLM Framework**), și Phi-3.5-MoE (**suport Apple MLX Framework**). Să încercăm acum:

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

### **🤖 Exemple pentru Phi-3.5 cu Apple MLX**

| Laboratoare    | Introducere | Acces |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Învață cum să folosești Phi-3.5 Instruct cu framework-ul Apple MLX   |  [Acces](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (imagine) | Învață cum să folosești Phi-3.5 Vision pentru analiza imaginilor cu framework-ul Apple MLX     |  [Acces](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Învață cum să folosești Phi-3.5 MoE cu framework-ul Apple MLX  |  [Acces](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Resurse**

1. Află mai multe despre Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Repozitoriu Apple MLX pe GitHub [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. Repozitoriu MLX-VLM pe GitHub [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.