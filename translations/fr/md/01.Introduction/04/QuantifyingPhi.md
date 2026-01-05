<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f4cbbe7bf3e764de52d64a96d97b3c35",
  "translation_date": "2026-01-05T08:11:02+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "fr"
}
-->
# **Quantification de la famille Phi**

La quantification de modèle désigne le processus de cartographie des paramètres (tels que les poids et les valeurs d'activation) dans un modèle de réseau neuronal d'une grande plage de valeurs (généralement une plage continue) vers une plage de valeurs finie plus petite. Cette technologie peut réduire la taille et la complexité computationnelle du modèle et améliorer l'efficacité opérationnelle du modèle dans des environnements à ressources limitées tels que les appareils mobiles ou les systèmes embarqués. La quantification du modèle réalise une compression en réduisant la précision des paramètres, mais elle introduit également une certaine perte de précision. Par conséquent, lors du processus de quantification, il est nécessaire de trouver un équilibre entre la taille du modèle, la complexité computationnelle et la précision. Les méthodes de quantification courantes comprennent la quantification en virgule fixe, la quantification en virgule flottante, etc. Vous pouvez choisir la stratégie de quantification appropriée selon le scénario spécifique et les besoins.

Nous espérons déployer le modèle GenAI sur des dispositifs edge et permettre à davantage d'appareils d'entrer dans les scénarios GenAI, tels que les appareils mobiles, les PC IA/Copilot+PC, et les dispositifs IoT traditionnels. Grâce au modèle quantifié, nous pouvons le déployer sur différents appareils edge en fonction des différents appareils. Associé au cadre d'accélération de modèle et au modèle quantifié fournis par les fabricants de matériel, nous pouvons construire de meilleurs scénarios d'application SLM.

Dans le scénario de quantification, nous disposons de différentes précisions (INT4, INT8, FP16, FP32). Voici une explication des précisions de quantification couramment utilisées.

### **INT4**

La quantification INT4 est une méthode de quantification radicale qui quantifie les poids et les valeurs d'activation du modèle en entiers sur 4 bits. La quantification INT4 entraîne généralement une plus grande perte de précision en raison de la plage de représentation plus petite et de la précision moindre. Cependant, comparée à la quantification INT8, la quantification INT4 peut réduire encore davantage les besoins de stockage et la complexité de calcul du modèle. Il convient de noter que la quantification INT4 est relativement rare dans les applications pratiques, car une précision trop faible peut entraîner une dégradation significative des performances du modèle. De plus, tous les matériels ne prennent pas en charge les opérations INT4, il faut donc considérer la compatibilité matérielle lors du choix d’une méthode de quantification.

### **INT8**

La quantification INT8 est le processus de conversion des poids et des activations d’un modèle de nombres à virgule flottante en entiers sur 8 bits. Bien que la plage numérique représentée par les entiers INT8 soit plus petite et moins précise, elle peut réduire de manière significative les exigences en stockage et calcul. Dans la quantification INT8, les poids et les valeurs d’activation du modèle passent par un processus de quantification, incluant mise à l’échelle et décalage, pour préserver autant que possible les informations d’origine à virgule flottante. Lors de l’inférence, ces valeurs quantifiées sont déquantifiées en nombres à virgule flottante pour le calcul, puis quantifiées de nouveau en INT8 pour l’étape suivante. Cette méthode peut offrir une précision suffisante dans la plupart des applications tout en maintenant une haute efficacité computationnelle.

### **FP16**

Le format FP16, c’est-à-dire les nombres en virgule flottante sur 16 bits (float16), réduit de moitié l’empreinte mémoire par rapport aux nombres en virgule flottante sur 32 bits (float32), ce qui présente des avantages importants dans les applications de deep learning à grande échelle. Le format FP16 permet de charger des modèles plus grands ou de traiter plus de données dans les mêmes limites de mémoire GPU. Alors que le matériel GPU moderne continue de supporter les opérations FP16, l’usage du format FP16 peut également entraîner des améliorations en vitesse de calcul. Cependant, le format FP16 a aussi ses inconvénients intrinsèques, à savoir une précision plus faible, qui peut occasionner une instabilité numérique ou une perte de précision dans certains cas.

### **FP32**

Le format FP32 offre une précision plus élevée et peut représenter avec exactitude une grande plage de valeurs. Dans les scénarios où des opérations mathématiques complexes sont effectuées ou des résultats très précis sont nécessaires, le format FP32 est privilégié. Cependant, une haute précision signifie aussi une utilisation mémoire plus importante et un temps de calcul plus long. Pour les modèles de deep learning à grande échelle, surtout lorsqu’il y a beaucoup de paramètres et une énorme quantité de données, le format FP32 peut provoquer une insuffisance de mémoire GPU ou une diminution de la vitesse d’inférence.

Sur les appareils mobiles ou les dispositifs IoT, nous pouvons convertir les modèles Phi-3.x en INT4, tandis que les PC IA / Copilot PC peuvent utiliser des précisions plus élevées telles que INT8, FP16, FP32.

Actuellement, différents fabricants de matériel disposent de cadres différents pour prendre en charge les modèles génératifs, tels que OpenVINO d’Intel, QNN de Qualcomm, MLX d’Apple, et CUDA de Nvidia, etc., combinés avec la quantification du modèle pour réaliser un déploiement local.

Sur le plan technologique, nous avons différents supports de format après quantification, tels que les formats PyTorch / TensorFlow, GGUF, et ONNX. J’ai réalisé une comparaison de formats et des scénarios d’application entre GGUF et ONNX. Ici, je recommande le format de quantification ONNX, qui bénéficie d’un bon support depuis le cadre de modèle jusqu’au matériel. Dans ce chapitre, nous nous concentrerons sur ONNX Runtime pour GenAI, OpenVINO et Apple MLX pour effectuer la quantification de modèle (si vous avez une meilleure méthode, vous pouvez aussi nous la proposer en soumettant un PR).

**Ce chapitre comprend**

1. [Quantifier Phi-3.5 / 4 avec llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantifier Phi-3.5 / 4 avec les extensions Generative AI pour onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantifier Phi-3.5 / 4 avec Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantifier Phi-3.5 / 4 avec le cadre Apple MLX](./UsingAppleMLXQuantifyingPhi.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’être précis, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour des informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou d’interprétations erronées résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->