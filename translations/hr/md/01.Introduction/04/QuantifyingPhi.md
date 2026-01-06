<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f4cbbe7bf3e764de52d64a96d97b3c35",
  "translation_date": "2026-01-05T15:35:43+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "hr"
}
-->
# **Kvantificiranje obitelji Phi**

Kvantizacija modela odnosi se na proces mapiranja parametara (kao što su težine i aktivacijske vrijednosti) u modelu neuronske mreže s velikog raspona vrijednosti (obično kontinuirani raspon vrijednosti) na manji konačni raspon vrijednosti. Ova tehnologija može smanjiti veličinu i računalnu složenost modela te poboljšati operativnu učinkovitost modela u okruženjima s ograničenim resursima kao što su mobilni uređaji ili ugrađeni sustavi. Kvantizacija modela postiže kompresiju smanjenjem preciznosti parametara, ali također uvodi određeni gubitak preciznosti. Stoga je u procesu kvantizacije potrebno uravnotežiti veličinu modela, računalnu složenost i preciznost. Uobičajene metode kvantizacije uključuju kvantizaciju fiksne točke, kvantizaciju s pomičnim zarezom itd. Možete odabrati odgovarajuću strategiju kvantizacije prema specifičnom scenariju i potrebama.

Nadamo se implementirati GenAI model na edge uređaje i omogućiti većem broju uređaja ulazak u GenAI scenarije, kao što su mobilni uređaji, AI PC/Copilot+PC i tradicionalni IoT uređaji. Kroz kvantizirani model možemo ga rasporediti na različite edge uređaje ovisno o različitim uređajima. U kombinaciji s okvirom za ubrzanje modela i kvantiziranim modelom koji pružaju proizvođači hardvera, možemo izgraditi bolje SLM aplikacijske scenarije.

U scenariju kvantizacije imamo različite preciznosti (INT4, INT8, FP16, FP32). Slijedi objašnjenje često korištenih preciznosti kvantizacije.

### **INT4**

INT4 kvantizacija je radikalna metoda kvantizacije koja kvantizira težine i aktivacijske vrijednosti modela u 4-bitne cijele brojeve. INT4 kvantizacija obično rezultira većim gubitkom preciznosti zbog manjeg raspona prikaza i niže preciznosti. Međutim, u usporedbi s INT8 kvantizacijom, INT4 kvantizacija može dodatno smanjiti zahtjeve za pohranom i računalnu složenost modela. Treba napomenuti da je INT4 kvantizacija relativno rijetka u praktičnim primjenama jer preniska preciznost može uzrokovati značajno pogoršanje performansi modela. Osim toga, ne podržava sav hardver operacije INT4, stoga je kompatibilnost s hardverom potrebno uzeti u obzir pri odabiru metode kvantizacije.

### **INT8**

INT8 kvantizacija je proces pretvaranja težina i aktivacija modela iz brojeva s pokretnim zarezom u 8-bitne cijele brojeve. Iako je numerički raspon predstavljen INT8 cijelim brojevima manji i manje precizan, može značajno smanjiti zahtjeve za pohranom i izračunima. U INT8 kvantizaciji, težine i aktivacijske vrijednosti modela prolaze kroz proces kvantizacije koji uključuje skaliranje i pomak kako bi se očuvale informacije izvornih brojeva s pomičnim zarezom koliko je moguće. Tijekom izvođenja, te kvantizirane vrijednosti će se dekvantizirati natrag u brojeve s pomičnim zarezom za izračun, a zatim ponovno kvantizirati u INT8 za sljedeći korak. Ova metoda može pružiti dovoljan stupanj preciznosti u većini primjena uz održavanje visoke računalne učinkovitosti.

### **FP16**

FP16 format, odnosno 16-bitni brojevi s pomičnim zarezom (float16), smanjuju memorijski otisak na pola u usporedbi s 32-bitnim brojevima s pomičnim zarezom (float32), što ima značajne prednosti u velikim primjenama dubokog učenja. FP16 format omogućuje učitavanje većih modela ili obradu većih količina podataka unutar istih ograničenja memorije GPU-a. Kako moderni GPU hardver sve više podržava FP16 operacije, korištenje FP16 formata može također donijeti poboljšanja u brzini računanja. Međutim, FP16 format ima i svoje inherentne nedostatke, naime nižu preciznost, što može uzrokovati numeričku nestabilnost ili gubitak preciznosti u nekim slučajevima.

### **FP32**

FP32 format pruža veću preciznost i može točno predstaviti širok raspon vrijednosti. U scenarijima gdje se obavljaju složene matematičke operacije ili su potrebni rezultati visoke preciznosti, FP32 format je poželjniji. Međutim, visoka preciznost također znači veću potrošnju memorije i duže vrijeme izračuna. Za velike modele dubokog učenja, posebno kada postoji mnogo parametara modela i ogromna količina podataka, FP32 format može uzrokovati nedostatak memorije na GPU-u ili smanjenje brzine izvođenja.

Na mobilnim uređajima ili IoT uređajima možemo pretvoriti Phi-3.x modele u INT4, dok AI PC / Copilot PC može koristiti veću preciznost kao što su INT8, FP16, FP32.

Trenutno različiti proizvođači hardvera imaju različite okvire za podršku generativnim modelima, poput Intelovog OpenVINO, Qualcommovog QNN, Appleovog MLX i Nvidijinega CUDA-e, itd., u kombinaciji s kvantizacijom modela za lokalnu implementaciju.

Što se tiče tehnologije, imamo različite podržane formate nakon kvantizacije, kao što su PyTorch / TensorFlow format, GGUF i ONNX. Napravio sam usporedbu formata i scenarija primjene između GGUF i ONNX. Ovdje preporučujem ONNX format kvantizacije, koji ima dobru podršku od okvira modela do hardvera. U ovom poglavlju fokusirat ćemo se na ONNX Runtime za GenAI, OpenVINO i Apple MLX za izvođenje kvantizacije modela (ako imate bolji način, također ga možete predati putem PR-a).

**Ovo poglavlje uključuje**

1. [Kvantiziranje Phi-3.5 / 4 pomoću llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Kvantiziranje Phi-3.5 / 4 pomoću generativnih AI ekstenzija za onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Kvantiziranje Phi-3.5 / 4 pomoću Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Kvantiziranje Phi-3.5 / 4 pomoću Apple MLX okvira](./UsingAppleMLXQuantifyingPhi.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj je dokument preveden pomoću AI usluge prevođenja [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, molimo imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili kriva tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->