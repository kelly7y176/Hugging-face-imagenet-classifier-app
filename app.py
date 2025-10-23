import gradio as gr

# The model 'google/vit-base-patch16-224' is a Vision Transformer (ViT)
# pre-trained on the massive ImageNet-21k dataset and fine-tuned on ImageNet-1k,
# making it an excellent choice for general-purpose image classification.
# Gradio's gr.Interface.load() handles everything, including:
# - Downloading the model.
# - Setting up the image-upload input component.
# - Processing the image (resizing, normalization).
# - Calling the model for inference.
# - Displaying the classification results (labels and probabilities).

model_name = "google/vit-base-patch16-224"

# Load the model directly from the Hugging Face Hub using Gradio's helper function.
# The `examples` argument provides sample images for the user to try out.
iface = gr.Interface.load(
    f"huggingface/{model_name}",
    title="ImageNet Classification Demo (Vision Transformer)",
    description="Upload an image to classify it into one of the 1000 ImageNet categories using a Google ViT model.",
    examples=[
        "path/to/example_image_1.jpg", # You'll replace these with actual paths later
        "path/to/example_image_2.jpg"
    ]
)

# Launch the Gradio interface
iface.launch()