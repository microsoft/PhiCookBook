<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-07-16T21:51:11+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "sl"
}
-->
# **Kvantificiranje družine Phi**

Kvantizacija modela se nanaša na postopek preslikave parametrov (kot so uteži in vrednosti aktivacije) v nevronskem omrežju iz širokega območja vrednosti (običajno zveznega) v manjše končno območje vrednosti. Ta tehnologija lahko zmanjša velikost in računsko zahtevnost modela ter izboljša učinkovitost delovanja modela v okoljih z omejenimi viri, kot so mobilne naprave ali vgrajeni sistemi. Kvantizacija modela doseže stiskanje z zmanjšanjem natančnosti parametrov, vendar hkrati prinaša določeno izgubo natančnosti. Zato je pri kvantizacijskem postopku potrebno uravnotežiti velikost modela, računsko zahtevnost in natančnost. Pogoste metode kvantizacije vključujejo kvantizacijo s fiksno vejico, kvantizacijo s plavajočo vejico itd. Izbrati je treba ustrezno strategijo kvantizacije glede na specifičen scenarij in potrebe.

Želimo namestiti GenAI modele na robne naprave in omogočiti več napravam vstop v GenAI scenarije, kot so mobilne naprave, AI PC/Copilot+PC in tradicionalne IoT naprave. S pomočjo kvantiziranih modelov jih lahko namestimo na različne robne naprave glede na posamezno napravo. V kombinaciji z ogrodjem za pospeševanje modelov in kvantiziranimi modeli, ki jih zagotavljajo proizvajalci strojne opreme, lahko ustvarimo boljše aplikacijske scenarije SLM.

V kvantizacijskem scenariju imamo različne natančnosti (INT4, INT8, FP16, FP32). Spodaj je razlaga pogosto uporabljenih natančnosti kvantizacije.

### **INT4**

INT4 kvantizacija je radikalna metoda kvantizacije, ki uteži in vrednosti aktivacije modela pretvori v 4-bitne cele števke. INT4 kvantizacija običajno povzroči večjo izgubo natančnosti zaradi manjšega območja predstavitve in nižje natančnosti. Vendar pa v primerjavi z INT8 kvantizacijo INT4 še dodatno zmanjša zahteve po shranjevanju in računsko zahtevnost modela. Pomembno je opozoriti, da je INT4 kvantizacija v praksi razmeroma redka, saj lahko prenizka natančnost povzroči znatno poslabšanje zmogljivosti modela. Poleg tega ne podpirajo vse strojne opreme INT4 operacij, zato je pri izbiri metode kvantizacije treba upoštevati združljivost s strojno opremo.

### **INT8**

INT8 kvantizacija je postopek pretvorbe uteži in aktivacij modela iz plavajočih vejic v 8-bitne cele števke. Čeprav je numerično območje, ki ga predstavljajo INT8 števke, manjše in manj natančno, lahko znatno zmanjša zahteve po shranjevanju in izračunih. Pri INT8 kvantizaciji uteži in vrednosti aktivacije modela potekajo skozi kvantizacijski postopek, ki vključuje skaliranje in premik, da se ohrani čim več prvotnih informacij plavajoče vejice. Med inferenco se te kvantizirane vrednosti dekvantizirajo nazaj v plavajoče vejice za izračun, nato pa ponovno kvantizirajo v INT8 za naslednji korak. Ta metoda zagotavlja zadostno natančnost v večini aplikacij ob ohranjanju visoke računske učinkovitosti.

### **FP16**

FP16 format, torej 16-bitna plavajoča vejica (float16), zmanjša porabo pomnilnika za polovico v primerjavi z 32-bitno plavajočo vejico (float32), kar ima pomembne prednosti pri velikih aplikacijah globokega učenja. FP16 format omogoča nalaganje večjih modelov ali obdelavo več podatkov znotraj istih omejitev pomnilnika GPU. Ker sodobna GPU strojna oprema vse bolj podpira FP16 operacije, lahko uporaba FP16 formata prinese tudi izboljšave v hitrosti izračunov. Vendar ima FP16 format tudi svoje pomanjkljivosti, predvsem nižjo natančnost, kar lahko v nekaterih primerih vodi do numerične nestabilnosti ali izgube natančnosti.

### **FP32**

FP32 format zagotavlja višjo natančnost in lahko natančno predstavlja širok razpon vrednosti. V scenarijih, kjer se izvajajo kompleksne matematične operacije ali so potrebni rezultati z visoko natančnostjo, je FP32 format prednostna izbira. Vendar pa višja natančnost pomeni tudi večjo porabo pomnilnika in daljši čas izračuna. Pri velikih modelih globokega učenja, zlasti kadar je veliko parametrov modela in ogromno podatkov, lahko FP32 format povzroči pomanjkanje pomnilnika GPU ali upočasnitev inferenčne hitrosti.

Na mobilnih napravah ali IoT napravah lahko modele Phi-3.x pretvorimo v INT4, medtem ko AI PC / Copilot PC lahko uporabljajo višje natančnosti, kot so INT8, FP16, FP32.

Trenutno različni proizvajalci strojne opreme podpirajo generativne modele z različnimi ogrodji, kot so Intelov OpenVINO, Qualcommov QNN, Applov MLX in Nvidijin CUDA, ki jih kombiniramo s kvantizacijo modelov za lokalno namestitev.

Na tehnični ravni imamo po kvantizaciji podporo za različne formate, kot so PyTorch / Tensorflow format, GGUF in ONNX. Izvedel sem primerjavo formatov in aplikacijskih scenarijev med GGUF in ONNX. Tukaj priporočam ONNX kvantizacijski format, ki ima dobro podporo od ogrodja modela do strojne opreme. V tem poglavju se bomo osredotočili na ONNX Runtime za GenAI, OpenVINO in Apple MLX za izvedbo kvantizacije modelov (če imate boljši način, nam ga lahko posredujete z oddajo PR).

**To poglavje vključuje**

1. [Kvantizacija Phi-3.5 / 4 z uporabo llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Kvantizacija Phi-3.5 / 4 z uporabo Generative AI razširitev za onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Kvantizacija Phi-3.5 / 4 z uporabo Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Kvantizacija Phi-3.5 / 4 z uporabo Apple MLX ogrodja](./UsingAppleMLXQuantifyingPhi.md)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.