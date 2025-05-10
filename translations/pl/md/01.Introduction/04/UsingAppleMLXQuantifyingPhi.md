<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-05-09T13:43:46+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "pl"
}
-->
# **Kwantyzacja Phi-3.5 przy użyciu Apple MLX Framework**

MLX to framework tablicowy do badań nad uczeniem maszynowym na układach Apple Silicon, stworzony przez zespół Apple zajmujący się badaniami nad uczeniem maszynowym.

MLX został zaprojektowany przez badaczy uczenia maszynowego dla badaczy uczenia maszynowego. Framework ma być przyjazny dla użytkownika, a jednocześnie wydajny w trenowaniu i wdrażaniu modeli. Sama koncepcja frameworka jest również prosta. Chcemy, aby badacze mogli łatwo rozszerzać i ulepszać MLX, by szybko testować nowe pomysły.

Modele LLM można przyspieszać na urządzeniach Apple Silicon za pomocą MLX, a modele można wygodnie uruchamiać lokalnie.

Obecnie Apple MLX Framework wspiera konwersję kwantyzacji dla Phi-3.5-Instruct (**Apple MLX Framework support**), Phi-3.5-Vision (**MLX-VLM Framework support**), oraz Phi-3.5-MoE (**Apple MLX Framework support**). Wypróbujmy to teraz:

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

### **🤖 Przykłady dla Phi-3.5 z Apple MLX**

| Laboratorium    | Wprowadzenie | Przejdź |
| -------- | ------- |  ------- |
| 🚀 Lab-Wprowadzenie Phi-3.5 Instruct  | Naucz się korzystać z Phi-3.5 Instruct z frameworkiem Apple MLX   |  [Przejdź](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Wprowadzenie Phi-3.5 Vision (obraz) | Naucz się analizować obrazy za pomocą Phi-3.5 Vision i Apple MLX   |  [Przejdź](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Wprowadzenie Phi-3.5 Vision (moE)   | Naucz się korzystać z Phi-3.5 MoE z frameworkiem Apple MLX  |  [Przejdź](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Zasoby**

1. Dowiedz się więcej o Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Repozytorium Apple MLX na GitHub [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. Repozytorium MLX-VLM na GitHub [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uważany za źródło autorytatywne. W przypadku informacji o istotnym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.