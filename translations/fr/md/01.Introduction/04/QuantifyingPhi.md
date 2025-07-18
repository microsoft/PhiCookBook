<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-07-16T21:41:08+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "fr"
}
-->
# **Quantification de la famille Phi**

La quantification de modèle désigne le processus qui consiste à mapper les paramètres (comme les poids et les valeurs d’activation) d’un modèle de réseau de neurones d’une large plage de valeurs (généralement continue) vers une plage de valeurs finie plus restreinte. Cette technologie permet de réduire la taille et la complexité de calcul du modèle, tout en améliorant son efficacité d’exécution dans des environnements aux ressources limitées, tels que les appareils mobiles ou les systèmes embarqués. La quantification compresse le modèle en réduisant la précision des paramètres, mais cela entraîne aussi une certaine perte de précision. Il est donc nécessaire, lors de la quantification, de trouver un équilibre entre la taille du modèle, la complexité de calcul et la précision. Les méthodes courantes de quantification incluent la quantification en nombres entiers fixes, la quantification en nombres flottants, etc. Vous pouvez choisir la stratégie de quantification adaptée selon le contexte et les besoins spécifiques.

Nous souhaitons déployer les modèles GenAI sur des appareils en périphérie et permettre à davantage d’appareils d’accéder aux scénarios GenAI, tels que les appareils mobiles, les PC AI/Copilot+PC, et les dispositifs IoT traditionnels. Grâce à la quantification, nous pouvons déployer le modèle sur différents appareils en périphérie selon leurs caractéristiques. En combinant cela avec les frameworks d’accélération et les modèles quantifiés fournis par les fabricants de matériel, nous pouvons construire de meilleurs scénarios d’application SLM.

Dans le cadre de la quantification, nous disposons de différentes précisions (INT4, INT8, FP16, FP32). Voici une explication des précisions de quantification les plus couramment utilisées.

### **INT4**

La quantification INT4 est une méthode très agressive qui convertit les poids et les valeurs d’activation du modèle en entiers sur 4 bits. La quantification INT4 entraîne généralement une perte de précision plus importante en raison de la plage de représentation plus restreinte et de la précision plus faible. Cependant, comparée à la quantification INT8, elle permet de réduire encore davantage les besoins en stockage et la complexité de calcul du modèle. Il est important de noter que la quantification INT4 est relativement rare en pratique, car une précision trop faible peut dégrader significativement les performances du modèle. De plus, tous les matériels ne supportent pas les opérations INT4, il faut donc prendre en compte la compatibilité matérielle lors du choix de la méthode de quantification.

### **INT8**

La quantification INT8 consiste à convertir les poids et les activations d’un modèle, initialement en nombres flottants, en entiers sur 8 bits. Bien que la plage numérique représentée par les entiers INT8 soit plus restreinte et moins précise, cette méthode permet de réduire considérablement les besoins en stockage et en calcul. Lors de la quantification INT8, les poids et les valeurs d’activation subissent un processus de quantification incluant mise à l’échelle et décalage, afin de préserver au mieux l’information flottante d’origine. Lors de l’inférence, ces valeurs quantifiées sont déquantifiées en nombres flottants pour les calculs, puis re-quantifiées en INT8 pour l’étape suivante. Cette méthode offre une précision suffisante dans la plupart des applications tout en maintenant une grande efficacité de calcul.

### **FP16**

Le format FP16, c’est-à-dire les nombres flottants sur 16 bits (float16), réduit de moitié la mémoire utilisée par rapport aux nombres flottants sur 32 bits (float32), ce qui présente un avantage significatif dans les applications d’apprentissage profond à grande échelle. Le format FP16 permet de charger des modèles plus volumineux ou de traiter plus de données dans les mêmes limites de mémoire GPU. Avec le support croissant des opérations FP16 par les GPU modernes, l’utilisation du format FP16 peut également améliorer la vitesse de calcul. Cependant, ce format présente aussi des inconvénients inhérents, notamment une précision moindre, qui peut entraîner une instabilité numérique ou une perte de précision dans certains cas.

### **FP32**

Le format FP32 offre une précision plus élevée et peut représenter avec exactitude une large gamme de valeurs. Dans les scénarios où des opérations mathématiques complexes sont effectuées ou lorsque des résultats très précis sont nécessaires, le format FP32 est privilégié. Toutefois, cette haute précision implique une consommation mémoire plus importante et des temps de calcul plus longs. Pour les modèles d’apprentissage profond à grande échelle, notamment lorsque le nombre de paramètres et la quantité de données sont très élevés, le format FP32 peut entraîner un manque de mémoire GPU ou une baisse de la vitesse d’inférence.

Sur les appareils mobiles ou IoT, nous pouvons convertir les modèles Phi-3.x en INT4, tandis que les PC AI / Copilot PC peuvent utiliser des précisions plus élevées comme INT8, FP16 ou FP32.

Actuellement, différents fabricants de matériel proposent des frameworks pour supporter les modèles génératifs, tels que OpenVINO d’Intel, QNN de Qualcomm, MLX d’Apple, et CUDA de Nvidia, combinés à la quantification pour permettre un déploiement local.

Sur le plan technique, nous disposons de différents formats supportés après quantification, comme les formats PyTorch / Tensorflow, GGUF, et ONNX. J’ai réalisé une comparaison des formats et des scénarios d’application entre GGUF et ONNX. Je recommande ici le format de quantification ONNX, qui bénéficie d’un bon support du framework modèle jusqu’au matériel. Dans ce chapitre, nous nous concentrerons sur ONNX Runtime pour GenAI, OpenVINO et Apple MLX pour effectuer la quantification des modèles (si vous avez une meilleure méthode, vous pouvez aussi nous la proposer via une PR).

**Ce chapitre comprend**

1. [Quantification de Phi-3.5 / 4 avec llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantification de Phi-3.5 / 4 avec les extensions Generative AI pour onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantification de Phi-3.5 / 4 avec Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantification de Phi-3.5 / 4 avec le framework Apple MLX](./UsingAppleMLXQuantifyingPhi.md)

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.