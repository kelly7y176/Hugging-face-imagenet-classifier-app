import gradio as gr
from transformers import ViTForImageClassification, ViTImageProcessor, pipeline
from PIL import Image
import torch

# 1. Load the processor and model locally
# The Vision Transformer requires a processor (for resizing/normalization)
# and the model (for classification).
model_name = "google/vit-base-patch16-224"
processor = ViTImageProcessor.from_pretrained(model_name)
model = ViTForImageClassification.from_pretrained(model_name)

# 2. Define the prediction function using the transformers pipeline
# This pipeline handles all the pre/post-processing for you.
# Using device="cuda" if available, otherwise defaults to CPU.
device = "cuda" if torch.cuda.is_available() else "cpu"
image_classifier = pipeline(
    task="image-classification",
    model=model,
    feature_extractor=processor,
    device=device
)

def classify_image(image: Image.Image):
    """
    Classifies the PIL Image using the local transformers pipeline.
    """
    # The pipeline returns a list of dictionaries:
    # [{'score': 0.98, 'label': 'Labrador retriever'}, ...]
    results = image_classifier(image)
    
    # Format the output for Gradio's 'label' component:
    # {label: score, ...}
    formatted_output = {item['label']: item['score'] for item in results}
    return formatted_output

# 3. Create and Launch the Gradio Interface
iface = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type="pil"), # Use type="pil" to get a PIL Image object
    outputs="label",
    title="ImageNet Classification Website 🖼️",
    description="Upload an image to classify it into one of the 1000 ImageNet categories using a Google Vision Transformer (ViT) model, loaded directly into the Space.",
)

iface.launch(
    share=False,
    server_name="0.0.0.0"
)