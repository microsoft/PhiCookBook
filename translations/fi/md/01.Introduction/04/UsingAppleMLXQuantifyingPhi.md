<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-07-16T21:55:47+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "fi"
}
-->
# **Phi-3.5:n kvantisointi Apple MLX -kehyksellä**

MLX on taulukkoalusta koneoppimustutkimukseen Apple-sirulla, jonka on kehittänyt Apple koneoppimustutkimus.

MLX on suunniteltu koneoppimustutkijoiden toimesta koneoppimustutkijoille. Kehys on tarkoitettu käyttäjäystävälliseksi, mutta silti tehokkaaksi mallien kouluttamiseen ja käyttöönottoon. Myös kehyksen rakenne on konseptuaalisesti yksinkertainen. Tavoitteenamme on tehdä MLX:n laajentamisesta ja parantamisesta helppoa tutkijoille, jotta uusia ideoita voidaan nopeasti kokeilla.

LLM-malleja voidaan nopeuttaa Apple Silicon -laitteilla MLX:n avulla, ja malleja voi ajaa paikallisesti erittäin kätevästi.

Nyt Apple MLX -kehys tukee Phi-3.5-Instructin kvantisointimuunnosta (**Apple MLX Framework support**), Phi-3.5-Visionin (**MLX-VLM Framework support**) tukea sekä Phi-3.5-MoE:n (**Apple MLX Framework support**). Kokeillaanpa seuraavaksi:

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

### **🤖 Esimerkkejä Phi-3.5:stä Apple MLX:n kanssa**

| Labrat   | Esittely | Siirry |
| -------- | -------- | ------ |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Opi käyttämään Phi-3.5 Instructia Apple MLX -kehyksen kanssa | [Siirry](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb) |
| 🚀 Lab-Introduce Phi-3.5 Vision (kuva) | Opi käyttämään Phi-3.5 Visionia kuvan analysointiin Apple MLX -kehyksen avulla | [Siirry](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb) |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE) | Opi käyttämään Phi-3.5 MoE:ta Apple MLX -kehyksen kanssa | [Siirry](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb) |

## **Resurssit**

1. Tutustu Apple MLX -kehykseen [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub -repositorio [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub -repositorio [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.