<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f4cbbe7bf3e764de52d64a96d97b3c35",
  "translation_date": "2026-01-04T06:29:38+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "fr"
}
-->
# **Quantification de la famille Phi**

La quantification de modèle désigne le processus de mise en correspondance des paramètres (tels que les poids et les valeurs d'activation) d'un modèle de réseau neuronal d'une large plage de valeurs (généralement une plage continue) à une plage de valeurs finie plus petite. Cette technologie peut réduire la taille et la complexité computationnelle du modèle et améliorer l'efficacité de fonctionnement du modèle dans des environnements aux ressources limitées tels que les appareils mobiles ou les systèmes embarqués. La quantification du modèle permet une compression en réduisant la précision des paramètres, mais elle introduit également une certaine perte de précision. Par conséquent, lors du processus de quantification, il est nécessaire d'équilibrer la taille du modèle, la complexité calculatoire et la précision. Les méthodes de quantification courantes incluent la quantification en virgule fixe, la quantification en virgule flottante, etc. Vous pouvez choisir la stratégie de quantification appropriée en fonction du scénario et des besoins spécifiques.

Nous souhaitons déployer des modèles d'IA générative (GenAI) sur des appareils périphériques (edge) et permettre à davantage d'appareils d'entrer dans des scénarios GenAI, tels que les appareils mobiles, les PC IA / Copilot+PC et les appareils IoT traditionnels. Grâce aux modèles quantifiés, nous pouvons les déployer sur différents appareils edge en fonction des dispositifs. Associés au framework d'accélération de modèles et aux modèles quantifiés fournis par les fabricants de matériel, nous pouvons construire de meilleurs scénarios d'application SLM.

Dans le cadre de la quantification, nous disposons de différentes précisions (INT4, INT8, FP16, FP32). Ci-dessous une explication des précisions de quantification couramment utilisées

### **INT4**

La quantification INT4 est une méthode de quantification radicale qui quantifie les poids et les valeurs d'activation du modèle en entiers sur 4 bits. La quantification INT4 entraîne généralement une perte de précision plus importante en raison de la plage de représentation plus petite et de la précision réduite. Cependant, comparée à la quantification INT8, la quantification INT4 peut réduire encore davantage les besoins de stockage et la complexité de calcul du modèle. Il convient de noter que la quantification INT4 est relativement rare dans les applications pratiques, car une précision trop faible peut provoquer une dégradation significative des performances du modèle. De plus, tous les matériels ne prennent pas en charge les opérations INT4, il faut donc tenir compte de la compatibilité matérielle lors du choix d'une méthode de quantification.

### **INT8**

La quantification INT8 est le processus de conversion des poids et des activations d'un modèle de nombres à virgule flottante en entiers sur 8 bits. Bien que la plage numérique représentée par les entiers INT8 soit plus petite et moins précise, elle peut réduire considérablement les besoins en stockage et en calcul. Dans la quantification INT8, les poids et les valeurs d'activation du modèle subissent un processus de quantification, incluant la mise à l'échelle et le décalage, afin de préserver autant que possible les informations originales en virgule flottante. Lors de l'inférence, ces valeurs quantifiées sont désquantifiées en nombres à virgule flottante pour le calcul, puis re-quantifiées en INT8 pour l'étape suivante. Cette méthode peut offrir une précision suffisante dans la plupart des applications tout en maintenant une grande efficacité de calcul.

### **FP16**

Le format FP16, c'est-à-dire les nombres à virgule flottante 16 bits (float16), réduit de moitié l'empreinte mémoire par rapport aux nombres à virgule flottante 32 bits (float32), ce qui présente des avantages significatifs dans les applications d'apprentissage profond à grande échelle. Le format FP16 permet de charger des modèles plus grands ou de traiter davantage de données dans les mêmes limites de mémoire GPU. Au fur et à mesure que le matériel GPU moderne continue de prendre en charge les opérations FP16, l'utilisation du format FP16 peut également entraîner des améliorations de la vitesse de calcul. Cependant, le format FP16 présente aussi des inconvénients inhérents, à savoir une précision plus faible, ce qui peut conduire à une instabilité numérique ou à une perte de précision dans certains cas.

### **FP32**

Le format FP32 offre une précision plus élevée et peut représenter avec précision une large plage de valeurs. Dans les scénarios où des opérations mathématiques complexes sont effectuées ou des résultats à haute précision sont requis, le format FP32 est préféré. Cependant, une précision élevée implique aussi une utilisation mémoire plus importante et des temps de calcul plus longs. Pour les modèles d'apprentissage profond à grande échelle, en particulier lorsque le nombre de paramètres du modèle est important et que la quantité de données est énorme, le format FP32 peut entraîner une insuffisance de mémoire GPU ou une diminution de la vitesse d'inférence.

Sur les appareils mobiles ou les appareils IoT, nous pouvons convertir les modèles Phi-3.x en INT4, tandis que les PC IA / Copilot PC peuvent utiliser des précisions supérieures telles que INT8, FP16, FP 32.

Actuellement, différents fabricants de matériel disposent de frameworks différents pour prendre en charge les modèles génératifs, tels que OpenVINO d'Intel, QNN de Qualcomm, MLX d'Apple et CUDA de Nvidia, etc., combinés à la quantification de modèle pour réaliser un déploiement local.

D'un point de vue technologique, nous avons différents formats pris en charge après quantification, tels que les formats PyTorch / TensorFlow, GGUF et ONNX. J'ai réalisé une comparaison de formats et des scénarios d'application entre GGUF et ONNX. Ici, je recommande le format de quantification ONNX, qui bénéficie d'un bon support du framework de modèle au matériel. Dans ce chapitre, nous nous concentrerons sur ONNX Runtime for GenAI, OpenVINO et Apple MLX pour effectuer la quantification des modèles (si vous avez une meilleure méthode, vous pouvez aussi nous la proposer en soumettant une PR)

**Ce chapitre comprend**

1. [Quantification de Phi-3.5 / 4 avec llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantification de Phi-3.5 / 4 en utilisant les extensions Generative AI pour onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantification de Phi-3.5 / 4 avec Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantification de Phi-3.5 / 4 avec le framework Apple MLX](./UsingAppleMLXQuantifyingPhi.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Clause de non-responsabilité :
Ce document a été traduit à l'aide du service de traduction automatique Co-op Translator (https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original, dans sa langue d'origine, doit être considéré comme la source faisant foi. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un traducteur humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->