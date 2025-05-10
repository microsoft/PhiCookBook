<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-05-09T13:39:53+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "hr"
}
-->
# **Kvantificiranje Phi obitelji**

Kvantizacija modela odnosi se na proces mapiranja parametara (kao što su težine i vrijednosti aktivacije) u modelu neuronske mreže s velikog raspona vrijednosti (obično kontinuiranog) na manji konačni raspon vrijednosti. Ova tehnologija može smanjiti veličinu i računalnu složenost modela te poboljšati učinkovitost rada modela u okruženjima s ograničenim resursima poput mobilnih uređaja ili ugrađenih sustava. Kvantizacija modela postiže kompresiju smanjenjem preciznosti parametara, ali također uvodi određeni gubitak preciznosti. Stoga je tijekom procesa kvantizacije potrebno pronaći ravnotežu između veličine modela, računalne složenosti i preciznosti. Uobičajene metode kvantizacije uključuju kvantizaciju s fiksnom točkom, kvantizaciju s pomičnim zarezom i slično. Možete odabrati odgovarajuću strategiju kvantizacije prema specifičnom scenariju i potrebama.

Želimo implementirati GenAI model na edge uređaje i omogućiti većem broju uređaja ulazak u GenAI scenarije, poput mobilnih uređaja, AI PC/Copilot+PC i tradicionalnih IoT uređaja. Kroz kvantizirani model možemo ga rasporediti na različite edge uređaje ovisno o vrsti uređaja. U kombinaciji s okvirom za ubrzanje modela i kvantiziranim modelom koji pružaju proizvođači hardvera, možemo izgraditi bolje SLM aplikacijske scenarije.

U scenariju kvantizacije imamo različite preciznosti (INT4, INT8, FP16, FP32). Slijedi objašnjenje najčešće korištenih preciznosti kvantizacije.

### **INT4**

INT4 kvantizacija je radikalna metoda kvantizacije koja kvantizira težine i vrijednosti aktivacije modela u 4-bitne cijele brojeve. INT4 kvantizacija obično rezultira većim gubitkom preciznosti zbog manjeg raspona prikaza i niže preciznosti. Međutim, u usporedbi s INT8 kvantizacijom, INT4 može dodatno smanjiti zahtjeve za pohranom i računalnu složenost modela. Treba napomenuti da je INT4 kvantizacija relativno rijetka u praktičnim primjenama jer preniska preciznost može uzrokovati značajan pad performansi modela. Osim toga, ne sav hardver podržava INT4 operacije, pa treba uzeti u obzir kompatibilnost hardvera pri odabiru metode kvantizacije.

### **INT8**

INT8 kvantizacija je proces pretvaranja težina i aktivacija modela iz brojeva s pomičnim zarezom u 8-bitne cijele brojeve. Iako je numerički raspon koji predstavljaju INT8 cijeli brojevi manji i manje precizan, može značajno smanjiti zahtjeve za pohranom i izračunima. Tijekom INT8 kvantizacije, težine i vrijednosti aktivacije modela prolaze kroz proces kvantizacije koji uključuje skaliranje i pomak, kako bi se što bolje sačuvale informacije iz originalnih brojeva s pomičnim zarezom. Tijekom izvođenja, ove kvantizirane vrijednosti se dekvantiziraju natrag u brojeve s pomičnim zarezom za izračun, a zatim ponovno kvantiziraju u INT8 za sljedeći korak. Ova metoda može pružiti dovoljnu preciznost u većini primjena uz održavanje visoke računalne učinkovitosti.

### **FP16**

FP16 format, odnosno 16-bitni brojevi s pomičnim zarezom (float16), smanjuje zauzeće memorije za polovicu u odnosu na 32-bitne brojeve s pomičnim zarezom (float32), što ima značajne prednosti u velikim dubokim učenjima. FP16 format omogućuje učitavanje većih modela ili obradu većih količina podataka unutar istih ograničenja GPU memorije. Kako moderni GPU hardver sve više podržava FP16 operacije, korištenje FP16 formata može također donijeti poboljšanja u brzini izračuna. Međutim, FP16 format ima i svoje inherentne nedostatke, odnosno nižu preciznost, što može dovesti do numeričke nestabilnosti ili gubitka preciznosti u nekim slučajevima.

### **FP32**

FP32 format pruža veću preciznost i može točno predstaviti širok raspon vrijednosti. U scenarijima gdje se izvode složene matematičke operacije ili je potrebna visoka preciznost rezultata, FP32 format je poželjan. Međutim, visoka preciznost također znači veću potrošnju memorije i dulje vrijeme izračuna. Za velike modele dubokog učenja, posebno kada postoji mnogo parametara modela i ogromna količina podataka, FP32 format može uzrokovati nedostatak GPU memorije ili smanjenje brzine izvođenja.

Na mobilnim uređajima ili IoT uređajima možemo konvertirati Phi-3.x modele u INT4, dok AI PC / Copilot PC može koristiti veću preciznost poput INT8, FP16, FP32.

Trenutno različiti proizvođači hardvera imaju različite okvire za podršku generativnim modelima, poput Intelovog OpenVINO, Qualcommovog QNN, Appleovog MLX i Nvidijinog CUDA, u kombinaciji s kvantizacijom modela za lokalnu implementaciju.

S tehničke strane, nakon kvantizacije podržavamo različite formate, poput PyTorch / Tensorflow formata, GGUF i ONNX. Napravio sam usporedbu formata i primjenu između GGUF i ONNX. Ovdje preporučujem ONNX kvantizacijski format, koji ima dobru podršku od model frameworka do hardvera. U ovom poglavlju fokusirat ćemo se na ONNX Runtime za GenAI, OpenVINO i Apple MLX za izvođenje kvantizacije modela (ako imate bolji način, možete nam ga poslati putem PR-a).

**Ovo poglavlje uključuje**

1. [Quantizing Phi-3.5 / 4 using llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantizing Phi-3.5 / 4 using Generative AI extensions for onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantizing Phi-3.5 / 4 using Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantizing Phi-3.5 / 4 using Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Odricanje od odgovornosti**:  
Ovaj dokument preveden je korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba se smatrati službenim i autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja proizašla iz korištenja ovog prijevoda.