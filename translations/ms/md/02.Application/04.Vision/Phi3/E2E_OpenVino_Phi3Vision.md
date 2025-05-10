<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7d7afa242a4a041ff4193546d4baf16",
  "translation_date": "2025-05-09T20:01:32+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md",
  "language_code": "ms"
}
-->
This demo shows how to use a pretrained model to generate Python code based on an image and a text prompt.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Here's a step-by-step explanation:

1. **Imports and Setup**:
   - Import the necessary libraries and modules, including `requests`, `PIL` for image processing, and `transformers` for managing the model and processing.

2. **Loading and Displaying the Image**:
   - Open an image file (`demo.png`) using the `PIL` library and display it.

3. **Defining the Prompt**:
   - Create a message that includes the image and requests Python code to process the image and save it using `plt` (matplotlib).

4. **Loading the Processor**:
   - Load the `AutoProcessor` from a pretrained model located in the `out_dir` directory. This processor will handle both text and image inputs.

5. **Creating the Prompt**:
   - Use the `apply_chat_template` method to format the message into a prompt suitable for the model.

6. **Processing the Inputs**:
   - Convert the prompt and image into tensors that the model can process.

7. **Setting Generation Arguments**:
   - Define arguments for the model's generation, including the maximum number of new tokens and whether to sample the output.

8. **Generating the Code**:
   - Generate the Python code using the model based on the inputs and generation arguments. Use the `TextStreamer` to process the output, skipping the prompt and special tokens.

9. **Output**:
   - Print the generated code, which should include Python code to process and save the image as specified in the prompt.

This demo demonstrates how to utilize a pretrained model with OpenVino to dynamically generate code based on user input and images.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.