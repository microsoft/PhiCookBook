<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7d7afa242a4a041ff4193546d4baf16",
  "translation_date": "2025-12-21T21:55:12+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md",
  "language_code": "pcm"
}
-->
Dis demo dey show how to use one pretrained model to generate Python code based on an image and a text prompt. 

[Sample Code](../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Below na step-by-step explanation:

1. **Imports and Setup**:
   - Di necessary libraries and modules dem don import, including `requests`, `PIL` for image processing, and `transformers` for handling di model and processing.

2. **Loading and Displaying the Image**:
   - One image file (`demo.png`) dem open with di `PIL` library and display am.

3. **Defining the Prompt**:
   - Dem create one message wey include the image and request make e generate Python code to process the image and save am using `plt` (matplotlib).

4. **Loading the Processor**:
   - Di `AutoProcessor` dem load am from a pretrained model wey di `out_dir` directory specify. Dis processor go handle di text and image inputs.

5. **Creating the Prompt**:
   - Di `apply_chat_template` method na wetin dem use format di message into one prompt wey correct for di model.

6. **Processing the Inputs**:
   - Di prompt and image dem process into tensors wey di model fit understand.

7. **Setting Generation Arguments**:
   - Dem define arguments for di model generation process, like di maximum number of new tokens wey e go generate and whether dem go sample di output.

8. **Generating the Code**:
   - Di model go generate di Python code based on di inputs and generation arguments. Dem use `TextStreamer` to handle di output, e go skip di prompt and special tokens.

9. **Output**:
   - Di generated code dem print am, e suppose include Python code wey go process di image and save am like di prompt talk.

Dis demo dey show how to use one pretrained model with OpenVino to generate code on the fly based on user input and images.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dis dokument don translate wit AI translator wey dem dey call [Co-op Translator](https://github.com/Azure/co-op-translator). Even as we dey try make everything correct, abeg sabi say automatic translation fit get mistakes or no too accurate. The original dokument for im own language na im be final authority. If na important or critical information, make you use professional human translator. We no dey responsible for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->