<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7d7afa242a4a041ff4193546d4baf16",
  "translation_date": "2025-07-17T05:00:12+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md",
  "language_code": "en"
}
-->
This demo showcases how to use a pretrained model to generate Python code based on an image and a text prompt. 

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Here's a step-by-step explanation:

1. **Imports and Setup**:
   - The necessary libraries and modules are imported, including `requests`, `PIL` for image processing, and `transformers` for handling the model and processing.

2. **Loading and Displaying the Image**:
   - An image file (`demo.png`) is opened using the `PIL` library and displayed.

3. **Defining the Prompt**:
   - A message is created that includes the image and a request to generate Python code to process the image and save it using `plt` (matplotlib).

4. **Loading the Processor**:
   - The `AutoProcessor` is loaded from a pretrained model specified by the `out_dir` directory. This processor will handle the text and image inputs.

5. **Creating the Prompt**:
   - The `apply_chat_template` method is used to format the message into a prompt suitable for the model.

6. **Processing the Inputs**:
   - The prompt and image are processed into tensors that the model can understand.

7. **Setting Generation Arguments**:
   - Arguments for the model's generation process are defined, including the maximum number of new tokens to generate and whether to sample the output.

8. **Generating the Code**:
   - The model generates the Python code based on the inputs and generation arguments. The `TextStreamer` is used to handle the output, skipping the prompt and special tokens.

9. **Output**:
   - The generated code is printed, which should include Python code to process the image and save it as specified in the prompt.

This demo illustrates how to leverage a pretrained model using OpenVino to generate code dynamically based on user input and images.

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.