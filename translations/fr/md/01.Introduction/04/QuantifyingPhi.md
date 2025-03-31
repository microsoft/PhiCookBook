<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-03-27T08:16:45+00:00",
  "source_file": "md\\01.Introduction\\04\\QuantifyingPhi.md",
  "language_code": "fr"
}
-->
# **Quantification de la famille Phi**

La quantification de modèle fait référence au processus de réduction de la plage de valeurs des paramètres (comme les poids et les valeurs d'activation) d'un modèle de réseau neuronal, passant d'une plage étendue (généralement continue) à une plage de valeurs finie plus petite. Cette technologie permet de réduire la taille et la complexité computationnelle du modèle, tout en améliorant son efficacité dans des environnements contraints en ressources, tels que les appareils mobiles ou les systèmes embarqués. La quantification de modèle réalise une compression en diminuant la précision des paramètres, mais cela introduit également une certaine perte de précision. Il est donc nécessaire de trouver un équilibre entre la taille du modèle, sa complexité computationnelle et sa précision. Les méthodes de quantification courantes incluent la quantification à virgule fixe, la quantification à virgule flottante, etc. Vous pouvez choisir la stratégie de quantification adaptée en fonction des besoins et du contexte spécifique.

Nous souhaitons déployer le modèle GenAI sur des appareils en périphérie et permettre à davantage d'appareils d'accéder aux scénarios GenAI, comme les appareils mobiles, les PC équipés d'IA/Copilot+PC, et les dispositifs IoT traditionnels. Grâce à la quantification des modèles, nous pouvons les déployer sur différents appareils en périphérie selon leurs spécificités. Combinée aux cadres d'accélération de modèle et aux modèles quantifiés fournis par les fabricants de matériel, cette approche permet de créer de meilleurs scénarios d'application SLM.

Dans le contexte de la quantification, nous avons différentes précisions (INT4, INT8, FP16, FP32). Voici une explication des précisions de quantification couramment utilisées.

### **INT4**

La quantification INT4 est une méthode radicale qui réduit les poids et les valeurs d'activation du modèle à des entiers de 4 bits. Cette méthode entraîne généralement une perte de précision plus importante en raison de la plage de représentation réduite et de la précision inférieure. Cependant, comparée à la quantification INT8, la quantification INT4 permet de réduire encore davantage les besoins en stockage et la complexité computationnelle du modèle. Il convient de noter que la quantification INT4 est relativement rare dans les applications pratiques, car une précision trop faible peut entraîner une dégradation significative des performances du modèle. De plus, tous les matériels ne prennent pas en charge les opérations INT4, il est donc important de tenir compte de la compatibilité matérielle lors du choix de cette méthode.

### **INT8**

La quantification INT8 consiste à convertir les poids et les activations d’un modèle de nombres à virgule flottante en entiers de 8 bits. Bien que la plage de valeurs représentées par les entiers INT8 soit plus petite et moins précise, cette méthode permet de réduire significativement les besoins en stockage et en calcul. Dans la quantification INT8, les poids et les valeurs d'activation du modèle subissent un processus de quantification, incluant un échelonnage et un décalage, pour préserver autant que possible les informations d'origine en virgule flottante. Lors de l'inférence, ces valeurs quantifiées sont déquantifiées en nombres à virgule flottante pour le calcul, puis quantifiées à nouveau en INT8 pour l'étape suivante. Cette méthode offre une précision suffisante dans la plupart des applications tout en maintenant une efficacité computationnelle élevée.

### **FP16**

Le format FP16, soit des nombres à virgule flottante sur 16 bits (float16), réduit de moitié l'empreinte mémoire par rapport aux nombres à virgule flottante sur 32 bits (float32), ce qui représente un avantage significatif dans les applications de deep learning à grande échelle. Le format FP16 permet de charger des modèles plus volumineux ou de traiter davantage de données dans les limites de mémoire d'un GPU donné. Avec le support croissant des opérations FP16 par les matériels GPU modernes, l'utilisation du format FP16 peut également entraîner des améliorations en termes de vitesse de calcul. Cependant, le format FP16 présente également des inconvénients inhérents, notamment une précision moindre, ce qui peut entraîner une instabilité numérique ou une perte de précision dans certains cas.

### **FP32**

Le format FP32 offre une précision supérieure et peut représenter avec exactitude une large gamme de valeurs. Dans les scénarios nécessitant des opérations mathématiques complexes ou des résultats de haute précision, le format FP32 est privilégié. Cependant, cette précision accrue implique également une utilisation mémoire plus importante et des temps de calcul plus longs. Pour les modèles de deep learning à grande échelle, en particulier ceux avec de nombreux paramètres et des volumes de données massifs, le format FP32 peut entraîner une insuffisance de mémoire GPU ou une baisse de la vitesse d'inférence.

Sur les appareils mobiles ou les dispositifs IoT, nous pouvons convertir les modèles Phi-3.x en INT4, tandis que les PC équipés d'IA / Copilot PC peuvent utiliser des précisions plus élevées telles que INT8, FP16, FP32.

À l'heure actuelle, différents fabricants de matériel proposent des cadres variés pour supporter les modèles génératifs, tels qu'OpenVINO d'Intel, QNN de Qualcomm, MLX d'Apple, et CUDA de Nvidia, qui, combinés à la quantification de modèle, permettent une mise en œuvre locale.

Sur le plan technologique, nous avons différents formats pris en charge après quantification, comme les formats PyTorch / Tensorflow, GGUF, et ONNX. J'ai réalisé une comparaison des formats et des scénarios d'application entre GGUF et ONNX. Ici, je recommande le format de quantification ONNX, qui bénéficie d'un bon support allant du cadre de modèle au matériel. Dans ce chapitre, nous nous concentrerons sur ONNX Runtime pour GenAI, OpenVINO, et Apple MLX pour effectuer la quantification de modèle (si vous avez une meilleure méthode, vous pouvez également nous la soumettre via une PR).

**Ce chapitre inclut**

1. [Quantification de Phi-3.5 / 4 avec llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantification de Phi-3.5 / 4 avec les extensions Generative AI pour onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantification de Phi-3.5 / 4 avec Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantification de Phi-3.5 / 4 avec le cadre Apple MLX](./UsingAppleMLXQuantifyingPhi.md)

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions de garantir l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des imprécisions. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.