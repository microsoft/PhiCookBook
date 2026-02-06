# Phi-3-Vision-128K-Instruct Project Overview

## The Model

The Phi-3-Vision-128K-Instruct, a lightweight, cutting-edge multimodal model, is the centerpiece of this project. It belongs to the Phi-3 model family and supports a context length of up to 128,000 tokens. The model was trained on a diverse dataset that includes synthetic data and carefully filtered publicly available websites, focusing on high-quality, reasoning-intensive content. The training process involved supervised fine-tuning and direct preference optimization to ensure precise compliance with instructions, along with strong safety measures.

## Creating sample data is essential for several reasons:

1. **Testing**: Sample data lets you test your application in different scenarios without affecting real data. This is especially important during development and staging.

2. **Performance Tuning**: Using sample data that reflects the scale and complexity of real data helps identify performance bottlenecks and optimize your application accordingly.

3. **Prototyping**: Sample data can be used to build prototypes and mockups, which aid in understanding user needs and gathering feedback.

4. **Data Analysis**: In data science, sample data is often used for exploratory analysis, model training, and algorithm testing.

5. **Security**: Using sample data in development and testing environments helps prevent accidental leaks of sensitive real data.

6. **Learning**: When learning a new technology or tool, working with sample data provides a practical way to apply what you’ve learned.

Keep in mind, the quality of your sample data can greatly affect these activities. It should closely resemble real data in terms of structure and variability.

### Sample Data Creation
[Generate DataSet Script](./CreatingSampleData.md)

## Dataset

A good example of a sample dataset is the [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (available on Huggingface).  
This sample dataset contains Burberry products along with metadata on product category, price, and title, totaling 3,040 rows, each representing a unique product. This dataset allows us to test the model’s ability to understand and interpret visual data, generating descriptive text that captures detailed visual features and brand-specific characteristics.

**Note:** You can use any dataset that includes images.

## Complex Reasoning

The model must reason about prices and product names based solely on the image. This requires the model not only to recognize visual features but also to understand their implications regarding product value and branding. By generating accurate textual descriptions from images, this project demonstrates the potential of combining visual data to improve model performance and versatility in real-world applications.

## Phi-3 Vision Architecture

The model architecture is a multimodal version of Phi-3. It processes both text and image data, integrating these inputs into a single sequence for comprehensive understanding and generation tasks. The model uses separate embedding layers for text and images. Text tokens are converted into dense vectors, while images are processed through a CLIP vision model to extract feature embeddings. These image embeddings are then projected to match the dimensions of the text embeddings, ensuring seamless integration.

## Integration of Text and Image Embeddings

Special tokens within the text sequence mark where the image embeddings should be inserted. During processing, these special tokens are replaced with the corresponding image embeddings, allowing the model to handle text and images as one sequence. The prompt for our dataset is formatted using the special <|image|> token as follows:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Sample Code
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Example walkthrough](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Disclaimer**:  
This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.