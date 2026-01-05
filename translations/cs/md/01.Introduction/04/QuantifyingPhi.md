<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f4cbbe7bf3e764de52d64a96d97b3c35",
  "translation_date": "2026-01-05T09:36:15+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "cs"
}
-->
# **Kvantisace rodiny Phi**

Kvantisace modelu označuje proces mapování parametrů (jako jsou váhy a hodnoty aktivace) v modelu neuronové sítě z velkého rozsahu hodnot (obvykle spojitého rozsahu hodnot) na menší konečný rozsah hodnot. Tato technologie může zmenšit velikost a výpočetně složitost modelu a zlepšit provozní efektivitu modelu v prostředích s omezenými zdroji, jako jsou mobilní zařízení nebo zabudované systémy. Kvantisace modelu dosahuje komprese snížením přesnosti parametrů, ale zároveň zavádí určitou ztrátu přesnosti. Proto je při procesu kvantisace nutné vyvážit velikost modelu, výpočetní složitost a přesnost. Běžné metody kvantisace zahrnují kvantisaci s pevnou čárkou, kvantisaci s pohyblivou desetinnou čárkou atd. Můžete si vybrat vhodnou kvantisovací strategii podle konkrétní situace a potřeb.

Doufáme, že nasadíme model GenAI na okrajová zařízení a umožníme více zařízením vstoupit do scénářů GenAI, jako jsou mobilní zařízení, AI PC/Copilot+PC a tradiční IoT zařízení. Prostřednictvím kvantizovaného modelu jej můžeme nasadit na různá okrajová zařízení na základě různých zařízení. V kombinaci s frameworkem pro akceleraci modelů a kvantizovaným modelem poskytovaným výrobci hardwaru můžeme vytvořit lepší scénáře aplikací SLM.

Ve scénáři kvantisace máme různé přesnosti (INT4, INT8, FP16, FP32). Následuje vysvětlení běžně používaných kvantisacích přesností

### **INT4**

Kvantisace INT4 je radikální kvantisovací metoda, která kvantizuje váhy a hodnoty aktivace modelu na 4-bitová celá čísla. Kvantisace INT4 obvykle vede k větší ztrátě přesnosti kvůli menšímu rozsahu reprezentace a nižší přesnosti. Nicméně ve srovnání s kvantisací INT8 může kvantisace INT4 dále snížit požadavky na úložiště a výpočetní složitost modelu. Je třeba poznamenat, že kvantisace INT4 je v praktických aplikacích poměrně vzácná, protože příliš nízká přesnost může způsobit významné zhoršení výkonu modelu. Navíc ne veškerý hardware podporuje operace INT4, proto je při výběru kvantisace třeba zvážit kompatibilitu hardwaru.

### **INT8**

Kvantisace INT8 je proces převodu vah a aktivací modelu z plovoucích desetinných čísel na 8-bitová celá čísla. Přestože číselný rozsah reprezentovaný celými čísly INT8 je menší a méně přesný, může výrazně snížit požadavky na úložiště a výpočty. Při kvantisaci INT8 procházejí váhy a hodnoty aktivací modelu kvantisovacím procesem, včetně škálování a posunu, aby byla zachována původní informace v plovoucí desetinné čárce co nejvíce. Během inference jsou tyto kvantizované hodnoty dequantizovány zpět na plovoucí desetinná čísla pro výpočty a poté kvantizovány zpět na INT8 pro další krok. Tato metoda může poskytnout dostatečnou přesnost ve většině aplikací při zachování vysoké výpočetní efektivity.

### **FP16**

Formát FP16, tedy 16-bitová plovoucí desetinná čísla (float16), snižuje paměťovou stopu na polovinu ve srovnání s 32-bitovými plovoucími desetinnými čísly (float32), což má významné výhody v rozsáhlých aplikacích hlubokého učení. Formát FP16 umožňuje načítání větších modelů nebo zpracování více dat v rámci stejných omezení paměti GPU. Vzhledem k tomu, že moderní hardwarové GPU stále více podporují operace FP16, použití formátu FP16 může také přinést zlepšení rychlosti výpočtů. Formát FP16 však má i své inherentní nevýhody, jmenovitě nižší přesnost, což může vést v některých případech k numerické nestabilitě nebo ztrátě přesnosti.

### **FP32**

Formát FP32 poskytuje vyšší přesnost a dokáže přesně reprezentovat širokou škálu hodnot. Ve scénářích, kde se provádějí složité matematické operace nebo je požadován výsledek s vysokou přesností, je formát FP32 preferován. Vyšší přesnost však znamená také větší využití paměti a delší dobu výpočtu. U rozsáhlých modelů hlubokého učení, zejména když je mnoho parametrů modelu a obrovské množství dat, může formát FP32 způsobovat nedostatek paměti GPU nebo pokles rychlosti inference.

Na mobilních zařízeních nebo IoT zařízeních můžeme převádět modely Phi-3.x na INT4, zatímco AI PC / Copilot PC mohou používat vyšší přesnosti jako INT8, FP16, FP 32.

V současnosti mají různí výrobci hardwaru různé frameworky na podporu generativních modelů, jako jsou Intel OpenVINO, Qualcomm QNN, Apple MLX a Nvidia CUDA atd., v kombinaci s kvantisací modelů pro lokální nasazení.

Z hlediska technologie máme po kvantisaci podporu různých formátů, například formáty PyTorch / TensorFlow, GGUF a ONNX. Provedl jsem srovnání formátů a aplikačních scénářů mezi GGUF a ONNX. Zde doporučuji kvantisovací formát ONNX, který má dobrou podporu jak od frameworku modelu, tak od hardwaru. V této kapitole se zaměříme na ONNX Runtime pro GenAI, OpenVINO a Apple MLX pro provádění kvantisace modelů (pokud máte lepší způsob, můžete nám jej také poskytnout zasláním PR).

**Tato kapitola obsahuje**

1. [Kvantisace Phi-3.5 / 4 pomocí llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Kvantisace Phi-3.5 / 4 pomocí Generative AI extensions for onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Kvantisace Phi-3.5 / 4 pomocí Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Kvantisace Phi-3.5 / 4 pomocí Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Upozornění**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli usilujeme o přesnost, vezměte prosím na vědomí, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace doporučujeme profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->