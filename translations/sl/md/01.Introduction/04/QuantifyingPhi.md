<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f4cbbe7bf3e764de52d64a96d97b3c35",
  "translation_date": "2026-01-05T15:42:19+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "sl"
}
-->
# **Kvantifikacija družine Phi**

Kvantizacija modela se nanaša na postopek preslikave parametrov (kot so uteži in vrednosti aktivacije) v nevronskem omrežju iz velikega razpona vrednosti (običajno zveznega vrednostnega razpona) v manjši končni razpon vrednosti. Ta tehnologija lahko zmanjša velikost in računsko zahtevnost modela ter izboljša učinkovitost delovanja modela v okoljih z omejenimi viri, kot so mobilne naprave ali vgrajeni sistemi. Kvantizacija modela doseže kompresijo z zmanjšanjem natančnosti parametrov, vendar pri tem pride tudi do določenih izgub natančnosti. Zato je pri procesu kvantizacije potrebno uravnotežiti velikost modela, računsko zahtevnost in natančnost. Pogoste metode kvantizacije vključujejo kvantizacijo s fiksno decimalno vejico, kvantizacijo s plavajočo vejico itd. Izbrati je mogoče ustrezno strategijo kvantizacije glede na specifičen scenarij in potrebe.

Upamo, da bomo lahko model GenAI postavili na robne naprave in omogočili več napravam vstop v scenarije GenAI, kot so mobilne naprave, AI PC/Copilot+PC in tradicionalne IoT naprave. S pomočjo kvantizacijskega modela ga lahko razporedimo na različne robne naprave, odvisno od različnih naprav. V kombinaciji z osnovnim ogrodjem za pospeševanje modela in kvantizacijskim modelom, ki ga zagotavljajo proizvajalci strojne opreme, lahko zgradimo boljše aplikacijske scenarije SLM.

V scenariju kvantizacije imamo različne natančnosti (INT4, INT8, FP16, FP32). Spodaj je pojasnilo o pogosto uporabljenih natančnostih kvantizacije.

### **INT4**

Kvantizacija INT4 je radikalna metoda kvantizacije, ki kvantizira uteži in vrednosti aktivacije modela v 4-bitne cela števila. Kvantizacija INT4 običajno povzroči večjo izgubo natančnosti zaradi manjše predstavitvene domene in nižje natančnosti. Vendar pa v primerjavi s kvantizacijo INT8 lahko kvantizacija INT4 še dodatno zmanjša potrebe po shrambi in računsko zahtevnost modela. Pomembno je omeniti, da je kvantizacija INT4 v praktični uporabi razmeroma redka, saj lahko prenizka natančnost povzroči znatno poslabšanje zmogljivosti modela. Poleg tega ne podpirajo vsi strojni opremi operacij INT4, zato je pri izbiri metode kvantizacije potrebno upoštevati združljivost s strojno opremo.

### **INT8**

Kvantizacija INT8 je postopek pretvorbe uteži in aktivacij modela iz plavajočih vejic v 8-bitna cela števila. Čeprav je numerični razpon, ki ga predstavljajo cela števila INT8, manjši in manj natančen, lahko znatno zmanjša potrebe po shrambi in izračunih. Pri kvantizaciji INT8 uteži in vrednosti aktivacije modela opravijo kvantizacijski postopek, vključno z ulomkom in premikom, da se ohranijo prvotne informacije plavajoče vejice čim bolj. V fazi sklepanja se te kvantizirane vrednosti odn kvantizirajo nazaj v plavajoče vejice za izračun, nato pa spet kvantizirajo v INT8 za naslednji korak. Ta metoda lahko zagotovi zadostno natančnost v večini aplikacij, hkrati pa ohranja visoko računsko učinkovitost.

### **FP16**

Format FP16, torej 16-bitna plavajoča vejica (float16), zmanjša porabo pomnilnika za polovico v primerjavi z 32-bitno plavajočo vejico (float32), kar ima pomembne prednosti pri velikih aplikacijah globokega učenja. Format FP16 omogoča nalaganje večjih modelov ali obdelavo več podatkov znotraj istih omejitev GPU pomnilnika. Ker sodobna GPU strojna oprema vse bolj podpira operacije FP16, lahko uporaba formata FP16 prinese tudi izboljšave v hitrosti izračuna. Vendar pa ima format FP16 tudi svoje inherentne pomanjkljivosti, in sicer nižjo natančnost, kar lahko v določenih primerih povzroči numerično nestabilnost ali izgubo natančnosti.

### **FP32**

Format FP32 nudi višjo natančnost in lahko natančno predstavi širok razpon vrednosti. V scenarijih, kjer se izvajajo zapletene matematične operacije ali so potrebni rezultati z visoko natančnostjo, je format FP32 začetna izbira. Vendar pa visoka natančnost pomeni tudi večjo porabo pomnilnika in daljši čas izračuna. Pri velikih modelih globokega učenja, zlasti kadar je veliko parametrov modela in ogromna količina podatkov, lahko format FP32 povzroči neustreznost pomnilnika GPU ali upad hitrosti sklepanja.

Na mobilnih napravah ali IoT napravah lahko modele Phi-3.x pretvorimo v INT4, medtem ko AI PC / Copilot PC lahko uporablja višjo natančnost, kot so INT8, FP16, FP32.

Trenutno različni proizvajalci strojne opreme uporabljajo različna ogrodja za podporo generativnim modelom, kot so Intelov OpenVINO, Qualcommov QNN, Applov MLX in Nvidia CUDA itd., v kombinaciji s kvantizacijo modela za izvedbo lokalne postavitve.

Na tehnični ravni imamo po kvantizaciji različne podpore formatov, kot so PyTorch/TensorFlow format, GGUF in ONNX. Pripravil sem primerjavo formatov in aplikacijskih scenarijev med GGUF in ONNX. Tukaj priporočam kvantizacijski format ONNX, ki ima dobro podporo od ogrodja modela do strojne opreme. V tem poglavju se bomo osredotočili na ONNX Runtime za GenAI, OpenVINO in Applov MLX za izvajanje kvantizacije modela (če imate boljšo metodo, nam jo lahko tudi posredujete s PR).

**To poglavje vključuje**

1. [Kvantifikacija Phi-3.5 / 4 z uporabo llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Kvantifikacija Phi-3.5 / 4 z uporabo razširitev Generative AI za onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Kvantifikacija Phi-3.5 / 4 z uporabo Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Kvantifikacija Phi-3.5 / 4 z uporabo Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo storitve za strojno prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->