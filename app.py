import gradio as gr

# Define the ImageNet-trained Vision Transformer model from the Hugging Face Hub
# This model is pre-trained on ImageNet-21k and fine-tuned on ImageNet-1k (1000 classes).
model_name = "google/vit-base-patch16-224"

# 1. Use gr.load() to fetch *only the core prediction function* from the Hub.
# This avoids the 'AttributeError: 'Dependency' object has no attribute 'launch''.
try:
    fn = gr.load(f"huggingface/{model_name}")
except Exception as e:
    # Print an error message if the model loading fails
    print(f"Error loading model {model_name}: {e}")
    # A placeholder function can be used to prevent a full crash
    def fn(image):
        return {"Error": "Model failed to load."}

# 2. Create the Gradio Interface explicitly.
# We define the inputs and outputs to ensure the interface is correctly built.
iface = gr.Interface(
    fn=fn,
    inputs="image",     # Input component: Allows user to upload an image.
    outputs="label",    # Output component: Displays the classification label and confidence score.
    title="ImageNet Classification Website 🖼️",
    description="Upload an image to classify it into one of the 1000 ImageNet categories using a Google Vision Transformer (ViT) model.",
    # Note: To include examples, you would add 'examples=[...]' here,
    # but only after uploading your example files to the Space.
)

# 3. Launch the Gradio application.
# The server_name="0.0.0.0" argument is absolutely essential for the app
# to be accessible within the container on Hugging Face Spaces.
iface.launch(
    share=False,
    server_name="0.0.0.0"
)