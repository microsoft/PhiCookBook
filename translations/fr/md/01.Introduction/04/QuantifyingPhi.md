<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-05-07T14:48:37+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "fr"
}
-->
# **Quantification de la famille Phi**

La quantification de modèle désigne le processus qui consiste à mapper les paramètres (tels que les poids et les valeurs d’activation) d’un modèle de réseau de neurones depuis une large plage de valeurs (généralement continue) vers une plage de valeurs finie plus restreinte. Cette technologie permet de réduire la taille et la complexité de calcul du modèle, tout en améliorant son efficacité d’exécution dans des environnements aux ressources limitées, comme les appareils mobiles ou les systèmes embarqués. La quantification compresse le modèle en réduisant la précision des paramètres, mais cela entraîne aussi une certaine perte de précision. Il est donc nécessaire de trouver un équilibre entre la taille du modèle, la complexité de calcul et la précision lors du processus de quantification. Les méthodes courantes incluent la quantification en point fixe, en virgule flottante, etc. Vous pouvez choisir la stratégie de quantification la mieux adaptée selon le contexte et les besoins spécifiques.

Nous souhaitons déployer les modèles GenAI sur des dispositifs en périphérie (edge devices) afin de permettre à davantage d’appareils d’intégrer des scénarios GenAI, tels que les appareils mobiles, les AI PC/Copilot+PC, et les dispositifs IoT traditionnels. Grâce à la quantification, nous pouvons déployer les modèles sur différents types d’appareils en périphérie, selon leurs caractéristiques. En combinant cela avec les frameworks d’accélération des modèles et les modèles quantifiés fournis par les fabricants de matériel, nous pouvons construire de meilleurs scénarios d’application SLM.

Dans le cadre de la quantification, différentes précisions sont disponibles (INT4, INT8, FP16, FP32). Voici une explication des précisions de quantification les plus couramment utilisées.

### **INT4**

La quantification INT4 est une méthode extrême qui quantifie les poids et les valeurs d’activation du modèle en entiers 4 bits. Elle entraîne généralement une perte de précision plus importante en raison de la plage de représentation plus réduite et de la précision moindre. Cependant, comparée à la quantification INT8, la quantification INT4 permet de diminuer encore davantage les besoins en stockage et la complexité de calcul du modèle. Il convient de noter que la quantification INT4 est relativement rare dans les applications pratiques, car une précision trop faible peut causer une dégradation significative des performances du modèle. De plus, tous les matériels ne supportent pas les opérations en INT4, il faut donc prendre en compte la compatibilité matérielle lors du choix de la méthode de quantification.

### **INT8**

La quantification INT8 consiste à convertir les poids et les activations d’un modèle de nombres à virgule flottante en entiers 8 bits. Bien que la plage numérique représentée par les entiers INT8 soit plus restreinte et moins précise, cette méthode permet de réduire considérablement les besoins en stockage et en calcul. Lors de la quantification INT8, les poids et les valeurs d’activation passent par un processus de quantification incluant une mise à l’échelle et un décalage, afin de préserver autant que possible l’information initiale en virgule flottante. Lors de l’inférence, ces valeurs quantifiées sont déquantifiées en nombres flottants pour les calculs, puis re-quantifiées en INT8 pour l’étape suivante. Cette méthode offre une précision suffisante dans la plupart des cas tout en maintenant une grande efficacité de calcul.

### **FP16**

Le format FP16, soit les nombres flottants 16 bits (float16), réduit de moitié l’empreinte mémoire comparé aux nombres flottants 32 bits (float32), ce qui présente un avantage significatif dans les applications de deep learning à grande échelle. Le format FP16 permet de charger des modèles plus volumineux ou de traiter plus de données dans les mêmes limites de mémoire GPU. Avec le support croissant des opérations FP16 par le matériel GPU moderne, l’utilisation du format FP16 peut aussi améliorer la vitesse de calcul. Cependant, le format FP16 a ses inconvénients intrinsèques, notamment une précision moindre qui peut entraîner une instabilité numérique ou une perte de précision dans certains cas.

### **FP32**

Le format FP32 offre une précision plus élevée et peut représenter avec exactitude une large gamme de valeurs. Dans les scénarios où des opérations mathématiques complexes sont effectuées ou lorsque des résultats très précis sont nécessaires, le format FP32 est préféré. Toutefois, cette haute précision implique une consommation mémoire plus importante et des temps de calcul plus longs. Pour les modèles de deep learning à grande échelle, en particulier ceux comportant un grand nombre de paramètres et un volume de données important, le format FP32 peut entraîner un manque de mémoire GPU ou une baisse de la vitesse d’inférence.

Sur les appareils mobiles ou les dispositifs IoT, nous pouvons convertir les modèles Phi-3.x en INT4, tandis que les AI PC / Copilot PC peuvent utiliser des précisions plus élevées comme INT8, FP16 ou FP32.

À l’heure actuelle, différents fabricants de matériel proposent des frameworks pour supporter les modèles génératifs, tels que OpenVINO d’Intel, QNN de Qualcomm, MLX d’Apple, et CUDA de Nvidia, qui combinés à la quantification des modèles permettent un déploiement local.

D’un point de vue technologique, différents formats sont pris en charge après quantification, tels que les formats PyTorch / Tensorflow, GGUF et ONNX. J’ai réalisé une comparaison des formats et des scénarios d’application entre GGUF et ONNX. Je recommande ici le format de quantification ONNX, qui bénéficie d’un bon support du framework de modèle jusqu’au matériel. Dans ce chapitre, nous nous concentrerons sur ONNX Runtime pour GenAI, OpenVINO et Apple MLX pour effectuer la quantification des modèles (si vous avez une meilleure méthode, vous pouvez aussi nous la proposer en soumettant un PR).

**Ce chapitre comprend**

1. [Quantification de Phi-3.5 / 4 avec llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantification de Phi-3.5 / 4 avec les extensions Generative AI pour onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantification de Phi-3.5 / 4 avec Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantification de Phi-3.5 / 4 avec le framework Apple MLX](./UsingAppleMLXQuantifyingPhi.md)

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant foi. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l'utilisation de cette traduction.