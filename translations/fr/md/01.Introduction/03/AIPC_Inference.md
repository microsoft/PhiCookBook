<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e08ce816e23ad813244a09ca34ebb8ac",
  "translation_date": "2025-03-27T06:51:50+00:00",
  "source_file": "md\\01.Introduction\\03\\AIPC_Inference.md",
  "language_code": "fr"
}
-->
# **Inference Phi-3 dans un PC AI**

Avec l'avancement de l'IA générative et l'amélioration des capacités matérielles des appareils en périphérie, un nombre croissant de modèles d'IA générative peuvent désormais être intégrés dans les appareils personnels des utilisateurs (BYOD). Les PC AI font partie de ces modèles. À partir de 2024, Intel, AMD et Qualcomm se sont associés à des fabricants de PC pour introduire des PC AI facilitant le déploiement de modèles d'IA générative localisés grâce à des modifications matérielles. Dans cette discussion, nous nous concentrerons sur les PC AI d'Intel et explorerons comment déployer Phi-3 sur un PC AI d'Intel.

### Qu'est-ce qu'un NPU

Un NPU (Neural Processing Unit) est un processeur ou une unité de traitement dédiée intégrée à un SoC plus large, conçue spécifiquement pour accélérer les opérations des réseaux neuronaux et les tâches d'IA. Contrairement aux CPU et GPU à usage général, les NPU sont optimisés pour un calcul parallèle axé sur les données, ce qui les rend extrêmement efficaces pour traiter d'énormes volumes de données multimédia comme des vidéos et des images, ainsi que pour traiter les données des réseaux neuronaux. Ils sont particulièrement adaptés aux tâches liées à l'IA, telles que la reconnaissance vocale, le floutage d'arrière-plan lors des appels vidéo et les processus d'édition photo ou vidéo comme la détection d'objets.

## NPU vs GPU

Bien que de nombreuses charges de travail d'IA et d'apprentissage automatique s'exécutent sur des GPU, il existe une distinction cruciale entre les GPU et les NPU.  
Les GPU sont connus pour leurs capacités de calcul parallèle, mais tous les GPU ne sont pas également efficaces au-delà du traitement graphique. Les NPU, en revanche, sont spécialement conçus pour les calculs complexes impliqués dans les opérations des réseaux neuronaux, ce qui les rend particulièrement performants pour les tâches d'IA.

En résumé, les NPU sont les experts en calcul qui accélèrent les opérations d'IA, et ils jouent un rôle clé dans l'ère émergente des PC AI !

***Cet exemple est basé sur le dernier processeur Intel Core Ultra d'Intel.***

## **1. Utiliser le NPU pour exécuter le modèle Phi-3**

Le périphérique Intel® NPU est un accélérateur d'inférence d'IA intégré aux CPU clients Intel, à partir de la génération de CPU Intel® Core™ Ultra (anciennement connue sous le nom de Meteor Lake). Il permet une exécution écoénergétique des tâches des réseaux neuronaux artificiels.

![Latency](../../../../../translated_images/aipcphitokenlatency.446d244d43a98a99f001e6eb55b421ab7ebc0b5d8f93fad8458da46cf263bfad.fr.png)

![Latency770](../../../../../translated_images/aipcphitokenlatency770.862269853961e495131e9465fdb06c2c7b94395b83729dc498cfc077e02caade.fr.png)

**Bibliothèque d'accélération Intel NPU**

La bibliothèque d'accélération Intel NPU [https://github.com/intel/intel-npu-acceleration-library](https://github.com/intel/intel-npu-acceleration-library) est une bibliothèque Python conçue pour améliorer l'efficacité de vos applications en exploitant la puissance de l'Intel Neural Processing Unit (NPU) pour effectuer des calculs rapides sur du matériel compatible.

Exemple de Phi-3-mini sur un PC AI équipé de processeurs Intel® Core™ Ultra.

![DemoPhiIntelAIPC](../../../../../imgs/01/03/AIPC/aipcphi3-mini.gif)

Installer la bibliothèque Python avec pip

```bash

   pip install intel-npu-acceleration-library

```

***Note*** Le projet est encore en cours de développement, mais le modèle de référence est déjà très complet.

### **Exécuter Phi-3 avec la bibliothèque d'accélération Intel NPU**

En utilisant l'accélération Intel NPU, cette bibliothèque n'affecte pas le processus de codage traditionnel. Vous devez simplement utiliser cette bibliothèque pour quantifier le modèle Phi-3 original, par exemple FP16, INT8, INT4, comme suit :

```python
from transformers import AutoTokenizer, pipeline,TextStreamer
from intel_npu_acceleration_library import NPUModelForCausalLM, int4
from intel_npu_acceleration_library.compiler import CompilerConfig
import warnings

model_id = "microsoft/Phi-3-mini-4k-instruct"

compiler_conf = CompilerConfig(dtype=int4)
model = NPUModelForCausalLM.from_pretrained(
    model_id, use_cache=True, config=compiler_conf, attn_implementation="sdpa"
).eval()

tokenizer = AutoTokenizer.from_pretrained(model_id)

text_streamer = TextStreamer(tokenizer, skip_prompt=True)
```

Une fois la quantification réussie, continuez l'exécution pour appeler le NPU afin d'exécuter le modèle Phi-3.

```python
generation_args = {
   "max_new_tokens": 1024,
   "return_full_text": False,
   "temperature": 0.3,
   "do_sample": False,
   "streamer": text_streamer,
}

pipe = pipeline(
   "text-generation",
   model=model,
   tokenizer=tokenizer,
)

query = "<|system|>You are a helpful AI assistant.<|end|><|user|>Can you introduce yourself?<|end|><|assistant|>"

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    pipe(query, **generation_args)
```

Lors de l'exécution du code, nous pouvons visualiser l'état de fonctionnement du NPU via le Gestionnaire des tâches.

![NPU](../../../../../translated_images/aipc_NPU.f047860f84f5bb5b183756f23b4b8506485e862ea34c6a53c58988707c23bc80.fr.png)

***Exemples*** : [AIPC_NPU_DEMO.ipynb](../../../../../code/03.Inference/AIPC/AIPC_NPU_DEMO.ipynb)

## **2. Utiliser DirectML + ONNX Runtime pour exécuter le modèle Phi-3**

### **Qu'est-ce que DirectML**

[DirectML](https://github.com/microsoft/DirectML) est une bibliothèque DirectX 12 haute performance et accélérée par le matériel pour l'apprentissage automatique. DirectML fournit une accélération GPU pour les tâches courantes d'apprentissage automatique sur une large gamme de matériels et de pilotes pris en charge, y compris tous les GPU compatibles DirectX 12 de fournisseurs tels qu'AMD, Intel, NVIDIA et Qualcomm.

Utilisé de manière autonome, l'API DirectML est une bibliothèque DirectX 12 bas niveau adaptée aux applications à haute performance et faible latence, comme les frameworks, les jeux et d'autres applications en temps réel. L'interopérabilité transparente de DirectML avec Direct3D 12 ainsi que sa faible surcharge et sa conformité sur différents matériels font de DirectML un choix idéal pour accélérer l'apprentissage automatique lorsque des performances élevées sont souhaitées, tout en garantissant la fiabilité et la prévisibilité des résultats sur différents matériels.

***Note*** : La dernière version de DirectML prend déjà en charge les NPU (https://devblogs.microsoft.com/directx/introducing-neural-processor-unit-npu-support-in-directml-developer-preview/).

### DirectML et CUDA en termes de capacités et de performances :

**DirectML** est une bibliothèque d'apprentissage automatique développée par Microsoft. Elle est conçue pour accélérer les charges de travail d'apprentissage automatique sur les appareils Windows, y compris les ordinateurs de bureau, les ordinateurs portables et les appareils en périphérie.
- Basé sur DX12 : DirectML est construit sur DirectX 12 (DX12), ce qui offre un large éventail de support matériel pour les GPU, y compris NVIDIA et AMD.
- Support étendu : En s'appuyant sur DX12, DirectML peut fonctionner avec tout GPU prenant en charge DX12, même les GPU intégrés.
- Traitement d'images : DirectML traite les images et d'autres données en utilisant des réseaux neuronaux, ce qui le rend adapté à des tâches telles que la reconnaissance d'images, la détection d'objets, etc.
- Facilité d'installation : La configuration de DirectML est simple et ne nécessite pas de SDK ou de bibliothèques spécifiques des fabricants de GPU.
- Performances : Dans certains cas, DirectML est performant et peut être plus rapide que CUDA, notamment pour certaines charges de travail.
- Limitations : Cependant, il existe des cas où DirectML peut être plus lent, en particulier pour des tailles de lots importantes en float16.

**CUDA** est la plateforme de calcul parallèle et le modèle de programmation de NVIDIA. Elle permet aux développeurs d'exploiter la puissance des GPU NVIDIA pour des calculs à usage général, y compris l'apprentissage automatique et les simulations scientifiques.
- Spécifique à NVIDIA : CUDA est étroitement intégré aux GPU NVIDIA et spécialement conçu pour eux.
- Hautement optimisé : Elle offre d'excellentes performances pour les tâches accélérées par GPU, en particulier avec les GPU NVIDIA.
- Largement utilisé : De nombreux frameworks et bibliothèques d'apprentissage automatique (comme TensorFlow et PyTorch) prennent en charge CUDA.
- Personnalisation : Les développeurs peuvent ajuster les paramètres de CUDA pour des tâches spécifiques, ce qui peut conduire à des performances optimales.
- Limitations : Cependant, la dépendance de CUDA au matériel NVIDIA peut être limitante si vous recherchez une compatibilité plus large avec différents GPU.

### Choisir entre DirectML et CUDA

Le choix entre DirectML et CUDA dépend de votre cas d'utilisation spécifique, de la disponibilité du matériel et de vos préférences.  
Si vous recherchez une compatibilité plus large et une installation facile, DirectML peut être un bon choix. Cependant, si vous disposez de GPU NVIDIA et avez besoin de performances hautement optimisées, CUDA reste une option solide. En résumé, DirectML et CUDA ont chacun leurs forces et leurs faiblesses, alors prenez en compte vos besoins et le matériel disponible avant de prendre une décision.

### **IA générative avec ONNX Runtime**

À l'ère de l'IA, la portabilité des modèles d'IA est très importante. ONNX Runtime permet de déployer facilement des modèles entraînés sur différents appareils. Les développeurs n'ont pas besoin de se préoccuper du framework d'inférence et peuvent utiliser une API unifiée pour effectuer l'inférence des modèles. À l'ère de l'IA générative, ONNX Runtime a également effectué des optimisations de code (https://onnxruntime.ai/docs/genai/). Grâce à ONNX Runtime optimisé, le modèle d'IA générative quantifié peut être inféré sur différents terminaux. Avec ONNX Runtime, vous pouvez utiliser les API de modèles d'IA via Python, C#, C/C++. Bien sûr, le déploiement sur iPhone peut tirer parti de l'API Generative AI avec ONNX Runtime en C++.

[Exemple de code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx)

***Compiler l'IA générative avec la bibliothèque ONNX Runtime***

```bash

winget install --id=Kitware.CMake  -e

git clone https://github.com/microsoft/onnxruntime.git

cd .\onnxruntime\

./build.bat --build_shared_lib --skip_tests --parallel --use_dml --config Release

cd ../

git clone https://github.com/microsoft/onnxruntime-genai.git

cd .\onnxruntime-genai\

mkdir ort

cd ort

mkdir include

mkdir lib

copy ..\onnxruntime\include\onnxruntime\core\providers\dml\dml_provider_factory.h ort\include

copy ..\onnxruntime\include\onnxruntime\core\session\onnxruntime_c_api.h ort\include

copy ..\onnxruntime\build\Windows\Release\Release\*.dll ort\lib

copy ..\onnxruntime\build\Windows\Release\Release\onnxruntime.lib ort\lib

python build.py --use_dml


```

**Installer la bibliothèque**

```bash

pip install .\onnxruntime_genai_directml-0.3.0.dev0-cp310-cp310-win_amd64.whl

```

Voici le résultat d'exécution 

![DML](../../../../../translated_images/aipc_DML.dd810ee1f3882323c131b39065ed0cf41bbe0aaa8d346a0d6d290c20f5c0bf75.fr.png)

***Exemples*** : [AIPC_DirectML_DEMO.ipynb](../../../../../code/03.Inference/AIPC/AIPC_DirectML_DEMO.ipynb)

## **3. Utiliser Intel OpenVino pour exécuter le modèle Phi-3**

### **Qu'est-ce qu'OpenVINO**

[OpenVINO](https://github.com/openvinotoolkit/openvino) est un kit d'outils open-source pour optimiser et déployer des modèles d'apprentissage profond. Il offre des performances améliorées pour les modèles de vision, d'audio et de langage issus de frameworks populaires comme TensorFlow, PyTorch, et plus encore. OpenVINO peut également être utilisé en combinaison avec des CPU et GPU pour exécuter le modèle Phi-3.

***Note*** : Actuellement, OpenVINO ne prend pas en charge les NPU.

### **Installer la bibliothèque OpenVINO**

```bash

 pip install git+https://github.com/huggingface/optimum-intel.git

 pip install git+https://github.com/openvinotoolkit/nncf.git

 pip install openvino-nightly

```

### **Exécuter Phi-3 avec OpenVINO**

Comme pour le NPU, OpenVINO permet d'exécuter les modèles d'IA générative en utilisant des modèles quantifiés. Nous devons d'abord quantifier le modèle Phi-3 et effectuer la quantification du modèle en ligne de commande via optimum-cli.

**INT4**

```bash

optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code ./openvinomodel/phi3/int4

```

**FP16**

```bash

optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format fp16 --trust-remote-code ./openvinomodel/phi3/fp16

```

Le format converti ressemble à ceci :

![openvino_convert](../../../../../translated_images/aipc_OpenVINO_convert.bd70cf3d87e65a923d2d663f559a03d86227ab71071802355a6cfeaf80eb7042.fr.png)

Charger les chemins des modèles (model_dir), les configurations associées (ov_config = {"PERFORMANCE_HINT": "LATENCY", "NUM_STREAMS": "1", "CACHE_DIR": ""}) et les périphériques accélérés par le matériel (GPU.0) via OVModelForCausalLM.

```python

ov_model = OVModelForCausalLM.from_pretrained(
     model_dir,
     device='GPU.0',
     ov_config=ov_config,
     config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
     trust_remote_code=True,
)

```

Lors de l'exécution du code, nous pouvons visualiser l'état de fonctionnement du GPU via le Gestionnaire des tâches.

![openvino_gpu](../../../../../translated_images/aipc_OpenVINO_GPU.142b31f25c5ffcf8802077629d11fbae275e53aeeb0752e0cdccf826feca6875.fr.png)

***Exemples*** : [AIPC_OpenVino_Demo.ipynb](../../../../../code/03.Inference/AIPC/AIPC_OpenVino_Demo.ipynb)

### ***Note*** : Les trois méthodes ci-dessus ont chacune leurs avantages, mais il est recommandé d'utiliser l'accélération NPU pour l'inférence sur PC AI.

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle effectuée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.