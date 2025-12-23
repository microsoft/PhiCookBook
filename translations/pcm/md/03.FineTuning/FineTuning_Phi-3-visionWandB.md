<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-12-21T18:31:15+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "pcm"
}
-->
# Phi-3-Vision-128K-Instruct Project Overview

## The Model

The Phi-3-Vision-128K-Instruct, a lightweight, state-of-the-art multimodal model, dey at di core of this project. E be part of di Phi-3 model family and fit handle context length reach 128,000 tokens. Di model dem train on different kain dataset wey include synthetic data and public websites wey dem filter well, wey dey emphasize high-quality, reasoning-intensive content. Di training process include supervised fine-tuning and direct preference optimization to make sure e follow instructions correct, plus strong safety measures.

## Creating sample data is crucial for several reasons:

1. **Testing**: Sample data dey allow you test your application for different scenarios without affecting real data. Dis one dey especially important for development and staging phases.

2. **Performance Tuning**: If sample data mimic di scale and complexity of real data, you fit find performance bottlenecks and optimize your application accordingly.

3. **Prototyping**: Sample data fit help make prototypes and mockups, wey fit help you understand wetin users want and gather feedback.

4. **Data Analysis**: For data science, dem dey use sample data for exploratory data analysis, model training, and algorithm testing.

5. **Security**: To use sample data for development and testing environments fit help prevent accidental leak of sensitive real data.

6. **Learning**: If you dey learn new technology or tool, to work with sample data fit give you practical way to apply wetin you don learn.

Remember, di quality of your sample data fit seriously affect these activities. E suppose dey as close as possible to the real data for structure and variability.

### Sample Data Creation
[Script wey go generate DataSet](./CreatingSampleData.md)

## Dataset

A good example of sample dataset is [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (available on Huggingface). 
Di sample data set of Burberry products plus metadata on product category, price, and title get total of 3,040 rows, each one dey represent one unique product. Dis dataset let us test di model ability to understand and interpret visual data, and to generate descriptive text wey capture fine visual details and brand-specific characteristics.

**Note:** You fit use any dataset wey include images.

## Complex Reasoning

Di model need reason about prices and naming based on only di image. Dis one mean say di model no go just recognize visual features but go also understand wetin dem mean for product value and branding. By synthesizing accurate textual descriptions from images, di project dey show di potential of combining visual data to boost performance and versatility of models for real-world applications.

## Phi-3 Vision Architecture

Di model architecture na multimodal version of Phi-3. E dey process both text and image data, and e dey integrate these inputs into one unified sequence for thorough understanding and generation tasks. Di model dey use separate embedding layers for text and images. Text tokens dem convert into dense vectors, while images dem process through a CLIP vision model to extract feature embeddings. These image embeddings dem project to match di text embeddings dimensions, so dem fit integrate seamlessly.

## Integration of Text and Image Embeddings

Special tokens inside di text sequence dey show where di image embeddings suppose enter. During processing, these special tokens dem replace with di corresponding image embeddings, allowing di model to handle text and images as a single sequence. Di prompt for our dataset dey formatted using di special <|image|> token as follows:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Sample Code
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Example walkthrough](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dis document don translate wit AI translation service Co-op Translator (https://github.com/Azure/co-op-translator). Even though we try make am correct, automatic translation fit get mistakes or no too accurate. Di original document for im own language dey remain di authoritative source. For important or critical information, make you use professional human translator. We no go responsible or liable for any misunderstanding or wrong interpretation wey fit come from this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->