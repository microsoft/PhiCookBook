<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "74689a2b87f747d751edfec988ccb7fd",
  "translation_date": "2025-04-04T13:26:18+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Phi-3-visionWandB.md",
  "language_code": "mo"
}
-->
# Phi-3-Vision-128K-Instruct Project Overview

## The Model

Phi-3-Vision-128K-Instruct is a compact and cutting-edge multimodal model that serves as the foundation of this project. Part of the Phi-3 model series, it supports a context length of up to 128,000 tokens. The model was trained on a diverse dataset, including synthetic data and carefully curated publicly available websites, with a focus on high-quality, reasoning-heavy content. Training involved supervised fine-tuning and direct preference optimization to ensure precise instruction-following and robust safety protocols.

## Why Creating Sample Data Matters:

1. **Testing**: Sample data enables you to test your application across various scenarios without risking real data, which is especially useful during development and staging.

2. **Performance Tuning**: By using sample data that reflects the complexity and scale of real data, you can identify bottlenecks and optimize your application's performance.

3. **Prototyping**: Sample data helps create prototypes and mockups, aiding in understanding user needs and gathering feedback.

4. **Data Analysis**: In data science, sample data is often used for exploratory analysis, training models, and testing algorithms.

5. **Security**: Using sample data in development and testing minimizes the risk of exposing sensitive real data.

6. **Learning**: When learning a new tool or technology, sample data provides a hands-on way to practice and apply concepts.

Keep in mind that the quality of your sample data can significantly affect these activities. It should closely mimic real data in terms of structure and variability.

### Sample Data Creation
[Generate DataSet Script](./CreatingSampleData.md)

## Dataset

A great example of a sample dataset is [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (available on Huggingface). This dataset contains information about Burberry products, including metadata such as product category, price, and title. It includes 3,040 rows, each representing a unique product. This dataset allows testing the model's ability to interpret visual data and generate descriptive text that captures intricate visual details and brand-specific traits.

**Note:** Any dataset that includes images can be used.

## Complex Reasoning

The model must infer pricing and naming details based solely on the image. This demands the ability to not only recognize visual features but also interpret their significance in terms of product value and branding. By generating accurate textual descriptions from images, the project demonstrates the potential of leveraging visual data to improve model versatility and performance in practical applications.

## Phi-3 Vision Architecture

The model architecture is a multimodal adaptation of Phi-3. It processes text and image inputs, merging them into a unified sequence for comprehensive understanding and generation tasks. Separate embedding layers are used for text and images. Text tokens are transformed into dense vectors, while images are processed through a CLIP vision model to extract feature embeddings. These image embeddings are then projected to match the dimensions of text embeddings, ensuring seamless integration.

## Integration of Text and Image Embeddings

Special tokens within the text sequence indicate where image embeddings should be inserted. During processing, these special tokens are replaced with corresponding image embeddings, allowing the model to handle text and images as a unified sequence. The dataset prompt is formatted using the special <|image|> token, as shown below:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Sample Code
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Example walkthrough](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

It seems like you want the text translated into "mo," but could you clarify what "mo" refers to? Are you referring to a specific language or abbreviation? For example, it could be shorthand for Māori, Montenegrin, or another language. Let me know so I can assist you accurately!