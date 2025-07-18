<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-07-16T21:49:49+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "cs"
}
-->
# **Kvantifikace rodiny Phi**

Kvantizace modelu označuje proces mapování parametrů (jako jsou váhy a aktivační hodnoty) v neuronové síti z rozsáhlého rozsahu hodnot (obvykle spojitého) na menší konečný rozsah hodnot. Tato technologie může snížit velikost a výpočetní náročnost modelu a zlepšit jeho provozní efektivitu v prostředích s omezenými zdroji, jako jsou mobilní zařízení nebo vestavěné systémy. Kvantizace modelu dosahuje komprese snížením přesnosti parametrů, ale zároveň přináší určitou ztrátu přesnosti. Proto je při kvantizaci nutné vyvážit velikost modelu, výpočetní náročnost a přesnost. Mezi běžné metody kvantizace patří kvantizace na pevný počet bitů, kvantizace s plovoucí desetinnou čárkou a další. Podle konkrétního scénáře a potřeb si můžete vybrat vhodnou kvantizační strategii.

Chceme nasadit GenAI modely na edge zařízení a umožnit tak více zařízením vstoupit do GenAI scénářů, jako jsou mobilní zařízení, AI PC/Copilot+PC a tradiční IoT zařízení. Díky kvantizovanému modelu je můžeme nasadit na různá edge zařízení podle jejich specifikací. Ve spojení s frameworkem pro akceleraci modelů a kvantizačními modely poskytovanými výrobci hardwaru můžeme vytvářet lepší aplikační scénáře SLM.

V kvantizačních scénářích používáme různé přesnosti (INT4, INT8, FP16, FP32). Níže je vysvětlení běžně používaných kvantizačních přesností.

### **INT4**

Kvantizace INT4 je radikální metoda, která kvantizuje váhy a aktivační hodnoty modelu na 4bitová celá čísla. Kvantizace INT4 obvykle vede k větší ztrátě přesnosti kvůli menšímu rozsahu reprezentace a nižší přesnosti. Na druhou stranu oproti INT8 kvantizaci může INT4 dále snížit požadavky na úložiště a výpočetní náročnost modelu. Je však třeba poznamenat, že kvantizace INT4 je v praxi poměrně vzácná, protože příliš nízká přesnost může výrazně zhoršit výkon modelu. Navíc ne všechny hardwarové platformy podporují operace s INT4, takže je třeba při výběru kvantizační metody zvážit kompatibilitu hardwaru.

### **INT8**

Kvantizace INT8 znamená převod vah a aktivačních hodnot modelu z čísel s plovoucí desetinnou čárkou na 8bitová celá čísla. Přestože je číselný rozsah INT8 menší a méně přesný, výrazně snižuje požadavky na úložiště a výpočty. Při kvantizaci INT8 procházejí váhy a aktivační hodnoty procesem kvantizace, který zahrnuje škálování a posun, aby se co nejvíce zachovala původní informace s plovoucí desetinnou čárkou. Při inferenci jsou tyto kvantizované hodnoty dekvantizovány zpět na čísla s plovoucí desetinnou čárkou pro výpočty a poté opět kvantizovány na INT8 pro další krok. Tato metoda poskytuje dostatečnou přesnost ve většině aplikací při zachování vysoké výpočetní efektivity.

### **FP16**

Formát FP16, tedy 16bitová čísla s plovoucí desetinnou čárkou (float16), snižuje paměťovou náročnost na polovinu oproti 32bitovým číslům s plovoucí desetinnou čárkou (float32), což má významné výhody v rozsáhlých aplikacích hlubokého učení. Formát FP16 umožňuje načítat větší modely nebo zpracovávat více dat v rámci stejné kapacity GPU paměti. Moderní GPU hardware stále více podporuje operace FP16, takže použití tohoto formátu může také zlepšit rychlost výpočtů. Na druhou stranu FP16 formát má inherentní nevýhodu nižší přesnosti, což může v některých případech vést k numerické nestabilitě nebo ztrátě přesnosti.

### **FP32**

Formát FP32 nabízí vyšší přesnost a dokáže přesně reprezentovat široký rozsah hodnot. V situacích, kdy se provádějí složité matematické operace nebo je potřeba vysoká přesnost výsledků, je preferován formát FP32. Vyšší přesnost však znamená větší nároky na paměť a delší dobu výpočtu. U rozsáhlých modelů hlubokého učení, zejména pokud obsahují mnoho parametrů a obrovské množství dat, může formát FP32 způsobit nedostatek paměti GPU nebo zpomalení inferenčního procesu.

Na mobilních zařízeních nebo IoT zařízeních můžeme převádět modely Phi-3.x na INT4, zatímco AI PC / Copilot PC mohou používat vyšší přesnosti jako INT8, FP16 nebo FP32.

V současnosti různí výrobci hardwaru nabízejí různé frameworky pro podporu generativních modelů, například Intel OpenVINO, Qualcomm QNN, Apple MLX a Nvidia CUDA, které v kombinaci s kvantizací modelu umožňují lokální nasazení.

Z technologického hlediska podporujeme po kvantizaci různé formáty, jako jsou PyTorch / Tensorflow, GGUF a ONNX. Provedl jsem srovnání formátů a aplikačních scénářů mezi GGUF a ONNX. Doporučuji kvantizační formát ONNX, který má dobrou podporu od frameworků až po hardware. V této kapitole se zaměříme na ONNX Runtime pro GenAI, OpenVINO a Apple MLX pro provádění kvantizace modelů (pokud máte lepší metodu, můžete nám ji také zaslat prostřednictvím PR).

**Tato kapitola obsahuje**

1. [Kvantizace Phi-3.5 / 4 pomocí llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Kvantizace Phi-3.5 / 4 pomocí rozšíření Generative AI pro onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Kvantizace Phi-3.5 / 4 pomocí Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Kvantizace Phi-3.5 / 4 pomocí Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.