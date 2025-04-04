<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "82289836c6113c9df7544eec1fc54802",
  "translation_date": "2025-04-04T07:15:38+00:00",
  "source_file": "md\\03.FineTuning\\Finetuning_VSCodeaitoolkit.md",
  "language_code": "ko"
}
-->
## VS Code용 AI Toolkit에 오신 것을 환영합니다

[VS Code용 AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit/tree/main)은 Azure AI Studio Catalog 및 Hugging Face와 같은 기타 카탈로그의 다양한 모델을 하나로 통합합니다. 이 툴킷은 생성형 AI 도구 및 모델을 활용한 AI 앱 개발의 일반적인 작업을 간소화합니다:
- 모델 탐색 및 플레이그라운드로 시작하기
- 로컬 컴퓨팅 자원을 활용한 모델 세부 조정 및 추론
- Azure 자원을 활용한 원격 세부 조정 및 추론

[VS Code용 AI Toolkit 설치하기](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

![AIToolkit FineTuning](../../../../translated_images/Aitoolkit.fc953930f4b4027110910d62005d87c6ac76941120d31139a2d9b0de2d4b64b8.ko.png)

**[Private Preview]** 클라우드에서 모델 세부 조정 및 추론을 실행하기 위한 Azure Container Apps의 원클릭 프로비저닝.

이제 AI 앱 개발을 시작해 봅시다:

- [VS Code용 AI Toolkit에 오신 것을 환영합니다](../../../../md/03.FineTuning)
- [로컬 개발](../../../../md/03.FineTuning)
  - [준비](../../../../md/03.FineTuning)
  - [Conda 활성화](../../../../md/03.FineTuning)
  - [기본 모델 세부 조정만 수행](../../../../md/03.FineTuning)
  - [모델 세부 조정 및 추론](../../../../md/03.FineTuning)
  - [모델 세부 조정](../../../../md/03.FineTuning)
  - [Microsoft Olive](../../../../md/03.FineTuning)
  - [세부 조정 샘플 및 리소스](../../../../md/03.FineTuning)
- [**\[Private Preview\]** 원격 개발](../../../../md/03.FineTuning)
  - [사전 요구 사항](../../../../md/03.FineTuning)
  - [원격 개발 프로젝트 설정](../../../../md/03.FineTuning)
  - [Azure 자원 프로비저닝](../../../../md/03.FineTuning)
  - [\[선택 사항\] Huggingface 토큰을 Azure Container App 비밀에 추가](../../../../md/03.FineTuning)
  - [세부 조정 실행](../../../../md/03.FineTuning)
  - [추론 엔드포인트 프로비저닝](../../../../md/03.FineTuning)
  - [추론 엔드포인트 배포](../../../../md/03.FineTuning)
  - [고급 사용법](../../../../md/03.FineTuning)

## 로컬 개발
### 준비

1. 호스트에 NVIDIA 드라이버가 설치되어 있는지 확인하세요.
2. 데이터셋 활용을 위해 HF를 사용하는 경우 `huggingface-cli login`을 실행하세요.
3. 메모리 사용량을 수정하는 모든 설정에 대한 `Olive` 키 설명.

### Conda 활성화
WSL 환경을 사용 중이며 공유되므로 Conda 환경을 수동으로 활성화해야 합니다. 이 단계 후 세부 조정 또는 추론을 실행할 수 있습니다.

```bash
conda activate [conda-env-name] 
```

### 기본 모델 세부 조정만 수행
세부 조정 없이 기본 모델만 시도하려면 Conda를 활성화한 후 아래 명령을 실행하세요.

```bash
cd inference

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://0.0.0.0:7860) in a browser after gradio initiates the connections.
python gradio_chat.py --baseonly
```

### 모델 세부 조정 및 추론

워크스페이스가 개발 컨테이너에서 열리면 터미널을 열고(기본 경로는 프로젝트 루트) 아래 명령을 실행하여 선택한 데이터셋에서 LLM을 세부 조정합니다.

```bash
python finetuning/invoke_olive.py 
```

체크포인트와 최종 모델은 `models` folder.

Next run inferencing with the fune-tuned model through chats in a `console`, `web browser` or `prompt flow`에 저장됩니다.

```bash
cd inference

# Console interface.
python console_chat.py

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://127.0.0.1:7860) in a browser after gradio initiates the connections.
python gradio_chat.py
```

`prompt flow` in VS Code, please refer to this [Quick Start](https://microsoft.github.io/promptflow/how-to-guides/quick-start.html).

### Model Fine-tuning

Next, download the following model depending on the availability of a GPU on your device.

To initiate the local fine-tuning session using QLoRA, select a model you want to fine-tune from our catalog.
| Platform(s) | GPU available | Model name | Size (GB) |
|---------|---------|--------|--------|
| Windows | Yes | Phi-3-mini-4k-**directml**-int4-awq-block-128-onnx | 2.13GB |
| Linux | Yes | Phi-3-mini-4k-**cuda**-int4-onnx | 2.30GB |
| Windows<br>Linux | No | Phi-3-mini-4k-**cpu**-int4-rtn-block-32-acc-level-4-onnx | 2.72GB |

**_Note_** You do not need an Azure Account to download the models

The Phi3-mini (int4) model is approximately 2GB-3GB in size. Depending on your network speed, it could take a few minutes to download.

Start by selecting a project name and location.
Next, select a model from the model catalog. You will be prompted to download the project template. You can then click "Configure Project" to adjust various settings.

### Microsoft Olive 

We use [Olive](https://microsoft.github.io/Olive/why-olive.html) to run QLoRA fine-tuning on a PyTorch model from our catalog. All of the settings are preset with the default values to optimize to run the fine-tuning process locally with optimized use of memory, but it can be adjusted for your scenario.

### Fine Tuning Samples and Resoures

- [Fine tuning Getting Started Guide](https://learn.microsoft.com/windows/ai/toolkit/toolkit-fine-tune)
- [Fine tuning with a HuggingFace Dataset](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-hf-dataset.md)
- [Fine tuning with Simple DataSet](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-simple-dataset.md)

## **[Private Preview]** Remote Development

### Prerequisites

1. To run the model fine-tuning in your remote Azure Container App Environment, make sure your subscription has enough GPU capacity. Submit a [support ticket](https://azure.microsoft.com/support/create-ticket/) to request the required capacity for your application. [Get More Info about GPU capacity](https://learn.microsoft.com/azure/container-apps/workload-profiles-overview)
2. If you are using private dataset on HuggingFace, make sure you have a [HuggingFace account](https://huggingface.co/?WT.mc_id=aiml-137032-kinfeylo) and [generate an access token](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=aiml-137032-kinfeylo)
3. Enable Remote Fine-tuning and Inference feature flag in the AI Toolkit for VS Code
   1. Open the VS Code Settings by selecting *File -> Preferences -> Settings*.
   2. Navigate to *Extensions* and select *AI Toolkit*.
   3. Select the *"Enable Remote Fine-tuning And Inference"* option.
   4. Reload VS Code to take effect.

- [Remote Fine tuning](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/remote-finetuning.md)

### Setting Up a Remote Development Project
1. Execute the command palette `AI Toolkit: Focus on Resource View`.
2. Navigate to *Model Fine-tuning* to access the model catalog. Assign a name to your project and select its location on your machine. Then, hit the *"Configure Project"* button.
3. Project Configuration
    1. Avoid enabling the *"Fine-tune locally"* option.
    2. The Olive configuration settings will appear with pre-set default values. Please adjust and fill in these configurations as required.
    3. Move on to *Generate Project*. This stage leverages WSL and involves setting up a new Conda environment, preparing for future updates that include Dev Containers.
4. Click on *"Relaunch Window In Workspace"* to open your remote development project.

> **Note:** The project currently works either locally or remotely within the AI Toolkit for VS Code. If you choose *"Fine-tune locally"* during project creation, it will operate exclusively in WSL without remote development capabilities. On the other hand, if you forego enabling *"Fine-tune locally"*, the project will be restricted to the remote Azure Container App environment.

### Provision Azure Resources
To get started, you need to provision the Azure Resource for remote fine-tuning. Do this by running the `AI Toolkit: Provision Azure Container Apps job for fine-tuning` from the command palette.

Monitor the progress of the provision through the link displayed in the output channel.

### [Optional] Add Huggingface Token to the Azure Container App Secret
If you're using private HuggingFace dataset, set your HuggingFace token as an environment variable to avoid the need for manual login on the Hugging Face Hub.
You can do this using the `AI Toolkit: Add Azure Container Apps Job secret for fine-tuning command`. With this command, you can set the secret name as [`HF_TOKEN`](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables#hftoken) and use your Hugging Face token as the secret value.

### Run Fine-tuning
To start the remote fine-tuning job, execute the `AI Toolkit: Run fine-tuning` command.

To view the system and console logs, you can visit the Azure portal using the link in the output panel (more steps at [View and Query Logs on Azure](https://aka.ms/ai-toolkit/remote-provision#view-and-query-logs-on-azure)). Or, you can view the console logs directly in the VSCode output panel by running the command `AI Toolkit: Show the running fine-tuning job streaming logs`. 
> **Note:** The job might be queued due to insufficient resources. If the log is not displayed, execute the `AI Toolkit: Show the running fine-tuning job streaming logs` command, wait for a while and then execute the command again to re-connect to the streaming log.

During this process, QLoRA will be used for fine-tuning, and will create LoRA adapters for the model to use during inference.
The results of the fine-tuning will be stored in the Azure Files.

### Provision Inference Endpoint
After the adapters are trained in the remote environment, use a simple Gradio application to interact with the model.
Similar to the fine-tuning process, you need to set up the Azure Resources for remote inference by executing the `AI Toolkit: Provision Azure Container Apps for inference` from the command palette.

By default, the subscription and the resource group for inference should match those used for fine-tuning. The inference will use the same Azure Container App Environment and access the model and model adapter stored in Azure Files, which were generated during the fine-tuning step. 


### Deploy the Inference Endpoint
If you wish to revise the inference code or reload the inference model, please execute the `AI Toolkit: Deploy for inference` command. This will synchronize your latest code with Azure Container App and restart the replica.  

Once deployment is successfully completed, you can access the inference API by clicking on the "*Go to Inference Endpoint*" button displayed in the VSCode notification. Or, the web API endpoint can be found under `ACA_APP_ENDPOINT` in `./infra/inference.config.json`을 사용하고 출력 패널에서 모델을 평가할 준비가 되었습니다.

### 고급 사용법
AI Toolkit을 활용한 원격 개발에 대한 추가 정보는 [원격으로 모델 세부 조정](https://aka.ms/ai-toolkit/remote-provision) 및 [세부 조정된 모델로 추론](https://aka.ms/ai-toolkit/remote-inference) 문서를 참조하세요.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역은 오류나 부정확성을 포함할 수 있습니다. 원본 문서를 해당 언어로 작성된 상태로 권위 있는 자료로 간주해야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역을 사용하는 과정에서 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.