Šis demonstracinis pavyzdys parodo, kaip naudoti iš anksto apmokytą modelį Python kodui generuoti pagal vaizdą ir tekstinį užklausą.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Štai žingsnis po žingsnio paaiškinimas:

1. **Importavimas ir paruošimas**:
   - Importuojamos reikalingos bibliotekos ir moduliai, įskaitant `requests`, `PIL` vaizdų apdorojimui ir `transformers` modelio valdymui bei apdorojimui.

2. **Vaizdo įkėlimas ir rodymas**:
   - Vaizdo failas (`demo.png`) atidaromas naudojant `PIL` biblioteką ir parodomas.

3. **Užklausos apibrėžimas**:
   - Sukuriama žinutė, kurioje yra vaizdas ir prašymas sugeneruoti Python kodą, kuris apdorotų vaizdą ir išsaugotų jį naudojant `plt` (matplotlib).

4. **Procesoriaus įkėlimas**:
   - `AutoProcessor` įkeltas iš iš anksto apmokyto modelio, nurodyto `out_dir` kataloge. Šis procesorius apdoros tekstinius ir vaizdinius įvesties duomenis.

5. **Užklausos sukūrimas**:
   - Naudojamas `apply_chat_template` metodas, kad žinutė būtų suformatuota į užklausą, tinkamą modeliui.

6. **Įvesties apdorojimas**:
   - Užklausa ir vaizdas apdorojami į tensorius, kuriuos modelis gali suprasti.

7. **Generavimo parametrų nustatymas**:
   - Apibrėžiami modelio generavimo proceso parametrai, įskaitant maksimalų naujų generuojamų žetonų skaičių ir ar naudoti atsitiktinį generavimą.

8. **Kodo generavimas**:
   - Modelis generuoja Python kodą pagal įvesties duomenis ir generavimo parametrus. `TextStreamer` naudojamas rezultatų valdymui, praleidžiant užklausą ir specialius žetonus.

9. **Rezultatas**:
   - Sugeneruotas kodas atspausdinamas, kuris turėtų apimti Python kodą vaizdo apdorojimui ir išsaugojimui, kaip nurodyta užklausoje.

Šis demonstracinis pavyzdys parodo, kaip pasinaudoti iš anksto apmokytu modeliu naudojant OpenVino, kad dinamiškai generuotumėte kodą pagal vartotojo įvestį ir vaizdus.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.