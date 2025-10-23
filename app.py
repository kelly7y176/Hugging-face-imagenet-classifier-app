import gradio as gr

# Define the ImageNet-trained model from the Hugging Face Hub
model_name = "google/vit-base-patch16-224"

# Load the model directly from the Hugging Face Hub.
# Gradio automatically infers the input (Image) and output (Label) components
# and handles all pre- and post-processing steps.
iface = gr.Interface.load(
    f"huggingface/{model_name}",
    # NOTE: You MUST create an 'examples' folder and place 'dog.jpg' and 'cat.jpg'
    # inside it for these paths to work. Remove this block if you don't have them yet.
    
)

# Launch the Gradio interface
# **KEY CHANGE:** setting share=False and server_name="0.0.0.0" is critical
# for the app to be accessible by the Hugging Face Space container.
iface.launch(
    share=False,
    server_name="0.0.0.0"
)