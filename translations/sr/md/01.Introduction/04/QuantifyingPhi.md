<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-05-09T13:39:07+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "sr"
}
-->
# **Kvantifikacija Phi porodice**

Kvantifikacija modela odnosi se na proces mapiranja parametara (kao što su težine i vrednosti aktivacije) u neuronskoj mreži sa širokog opsega vrednosti (obično kontinuirani opseg) na manji konačni opseg vrednosti. Ova tehnologija može smanjiti veličinu i računsku složenost modela, kao i poboljšati efikasnost rada modela u okruženjima sa ograničenim resursima, poput mobilnih uređaja ili ugrađenih sistema. Kvantifikacija modela postiže kompresiju smanjenjem preciznosti parametara, ali uvodi i određeni gubitak preciznosti. Zbog toga je u procesu kvantifikacije potrebno balansirati veličinu modela, računsku složenost i preciznost. Uobičajene metode kvantifikacije uključuju kvantifikaciju sa fiksnom tačkom, kvantifikaciju sa pokretnom tačkom i slično. Možete izabrati odgovarajuću strategiju kvantifikacije u zavisnosti od specifičnog scenarija i potreba.

Nadamo se da ćemo GenAI modele implementirati na edge uređaje i omogućiti većem broju uređaja da uđu u GenAI scenarije, kao što su mobilni uređaji, AI PC/Copilot+PC i tradicionalni IoT uređaji. Kroz kvantifikovane modele možemo ih rasporediti na različite edge uređaje u zavisnosti od vrste uređaja. U kombinaciji sa framework-om za ubrzanje modela i kvantifikacionim modelom koje obezbeđuju proizvođači hardvera, možemo izgraditi bolje SLM aplikacione scenarije.

U scenariju kvantifikacije imamo različite preciznosti (INT4, INT8, FP16, FP32). Sledeće je objašnjenje najčešće korišćenih preciznosti kvantifikacije.

### **INT4**

INT4 kvantifikacija je radikalna metoda kvantifikacije koja pretvara težine i vrednosti aktivacije modela u 4-bitne celine brojeve. INT4 kvantifikacija obično rezultira većim gubitkom preciznosti zbog manjeg opsega predstavljanja i niže preciznosti. Ipak, u poređenju sa INT8 kvantifikacijom, INT4 može dodatno smanjiti zahteve za skladištenjem i računsku složenost modela. Važno je napomenuti da se INT4 kvantifikacija retko koristi u praktičnim primenama, jer previše niska preciznost može značajno narušiti performanse modela. Takođe, nije sav hardver kompatibilan sa INT4 operacijama, pa treba uzeti u obzir kompatibilnost hardvera pri izboru metode kvantifikacije.

### **INT8**

INT8 kvantifikacija je proces pretvaranja težina i aktivacija modela iz brojeva sa pokretnom tačkom u 8-bitne celine brojeve. Iako je numerički opseg INT8 manji i manje precizan, ova metoda značajno smanjuje zahteve za skladištenjem i proračunima. Tokom INT8 kvantifikacije, težine i vrednosti aktivacije modela prolaze kroz proces kvantifikacije koji uključuje skaliranje i pomeranje, kako bi se sačuvale informacije iz originalnih brojeva sa pokretnom tačkom. Tokom inferencije, ovi kvantifikovani podaci se dekvantifikuju nazad u brojeve sa pokretnom tačkom za proračun, a zatim ponovo kvantifikuju u INT8 za sledeći korak. Ova metoda pruža dovoljnu preciznost u većini primena uz održavanje visoke računarske efikasnosti.

### **FP16**

FP16 format, odnosno 16-bitni brojevi sa pokretnom tačkom (float16), smanjuje zauzeće memorije za pola u poređenju sa 32-bitnim brojevima sa pokretnom tačkom (float32), što predstavlja značajnu prednost u velikim dubokim neuronskim mrežama. FP16 format omogućava učitavanje većih modela ili obradu većih količina podataka unutar istih memorijskih ograničenja GPU-a. Kako savremeni GPU hardver sve bolje podržava FP16 operacije, korišćenje FP16 formata može doneti i poboljšanja u brzini računanja. Ipak, FP16 ima i svoje mane, pre svega nižu preciznost, što može dovesti do numeričke nestabilnosti ili gubitka preciznosti u nekim slučajevima.

### **FP32**

FP32 format pruža veću preciznost i može tačno predstaviti širok spektar vrednosti. U scenarijima gde se izvode složene matematičke operacije ili je potrebna visoka preciznost rezultata, FP32 format je poželjan. Međutim, veća preciznost znači i veće korišćenje memorije i duže vreme računanja. Za velike duboke neuronske mreže, naročito kada postoji mnogo parametara modela i velika količina podataka, FP32 može dovesti do nedostatka memorije na GPU-u ili usporenja u brzini inferencije.

Na mobilnim ili IoT uređajima možemo konvertovati Phi-3.x modele u INT4, dok AI PC / Copilot PC mogu koristiti veće preciznosti kao što su INT8, FP16, FP32.

Trenutno različiti proizvođači hardvera imaju različite framework-e za podršku generativnim modelima, kao što su Intel OpenVINO, Qualcomm QNN, Apple MLX i Nvidia CUDA, koji se kombinuju sa kvantifikacijom modela za lokalnu implementaciju.

Sa tehničke strane, nakon kvantifikacije imamo podršku za različite formate, kao što su PyTorch / Tensorflow format, GGUF i ONNX. Napravio sam poređenje formata i aplikativnih scenarija između GGUF i ONNX. Ovde preporučujem ONNX format kvantifikacije, koji ima dobru podršku od framework-a modela do hardvera. U ovom poglavlju fokusiraćemo se na ONNX Runtime za GenAI, OpenVINO i Apple MLX za izvođenje kvantifikacije modela (ako imate bolji način, možete nam ga poslati putem PR-a).

**Ovo poglavlje uključuje**

1. [Kvantifikacija Phi-3.5 / 4 koristeći llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Kvantifikacija Phi-3.5 / 4 koristeći Generative AI ekstenzije za onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Kvantifikacija Phi-3.5 / 4 koristeći Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Kvantifikacija Phi-3.5 / 4 koristeći Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Ограничење одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо прецизности, имајте у виду да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални превод од стране људског преводиоца. Нисмо одговорни за било каква неспоразума или погрешна тумачења која могу настати коришћењем овог превода.