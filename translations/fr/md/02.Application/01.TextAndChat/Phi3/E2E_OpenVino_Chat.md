<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-03-27T09:17:23+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\E2E_OpenVino_Chat.md",
  "language_code": "fr"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Ce code exporte un modèle au format OpenVINO, le charge et l'utilise pour générer une réponse à une invite donnée.

1. **Exporter le modèle** :
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Cette commande utilise `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **Importer les bibliothèques nécessaires** :
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Ces lignes importent des classes du module `transformers` library and the `optimum.intel.openvino`, nécessaires pour charger et utiliser le modèle.

3. **Configurer le répertoire et les paramètres du modèle** :
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` est un dictionnaire qui configure le modèle OpenVINO pour privilégier une faible latence, utiliser un seul flux d'inférence et ne pas utiliser de répertoire de cache.

4. **Charger le modèle** :
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Cette ligne charge le modèle à partir du répertoire spécifié, en utilisant les paramètres de configuration définis précédemment. Elle permet également l'exécution de code à distance si nécessaire.

5. **Charger le tokenizer** :
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Cette ligne charge le tokenizer, responsable de convertir le texte en tokens compréhensibles par le modèle.

6. **Configurer les arguments du tokenizer** :
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Ce dictionnaire spécifie que les tokens spéciaux ne doivent pas être ajoutés à la sortie tokenisée.

7. **Définir l'invite** :
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Cette chaîne de caractères configure une invite de conversation où l'utilisateur demande à l'assistant IA de se présenter.

8. **Tokeniser l'invite** :
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Cette ligne convertit l'invite en tokens que le modèle peut traiter, en retournant le résultat sous forme de tenseurs PyTorch.

9. **Générer une réponse** :
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Cette ligne utilise le modèle pour générer une réponse basée sur les tokens d'entrée, avec un maximum de 1024 nouveaux tokens.

10. **Décoder la réponse** :
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Cette ligne convertit les tokens générés en une chaîne lisible, en ignorant les tokens spéciaux, et récupère le premier résultat.

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous fassions de notre mieux pour garantir l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées découlant de l'utilisation de cette traduction.