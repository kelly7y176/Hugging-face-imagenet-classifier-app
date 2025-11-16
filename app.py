import gradio as gr
from transformers import ViTForImageClassification, ViTImageProcessor, pipeline
from PIL import Image
import torch
# --- NEW FIREBASE IMPORTS ---
import firebase_admin
from firebase_admin import credentials, firestore
import json
import os
import datetime
# ----------------------------

# --- FIREBASE INITIALIZATION ---
# The Firebase JSON key must be set as a Secret named FIREBASE_CREDENTIALS_JSON
db = None
if "FIREBASE_CREDENTIALS_JSON" in os.environ:
    try:
        # Load the JSON content from the environment variable (Hugging Face Secret)
        cred_json = json.loads(os.environ["FIREBASE_CREDENTIALS_JSON"])
        cred = credentials.Certificate(cred_json)
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        print("✅ Firestore Client Initialized. Logging enabled.")
    except Exception as e:
        print(f"❌ Failed to initialize Firebase client from secret: {e}")
else:
    print("⚠️ FIREBASE_CREDENTIALS_JSON secret not found. Logging is disabled.")
# -------------------------------

# 1. Load the processor and model locally
model_name = "google/vit-base-patch16-224"
processor = ViTImageProcessor.from_pretrained(model_name)
model = ViTForImageClassification.from_pretrained(model_name)

# 2. Define the prediction pipeline
device = "cuda" if torch.cuda.is_available() else "cpu"
image_classifier = pipeline(
    task="image-classification",
    model=model,
    feature_extractor=processor,
    device=device
)

# --- NEW LOGGING FUNCTION ---
def log_classification(results, timestamp, model_name):
    """Logs the top classification result to Firestore."""
    if db is None or not results:
        return

    # Log only the top result (the first item in the results list)
    top_result = results[0]
    
    log_entry = {
        "timestamp": timestamp,
        "label": top_result['label'],
        "confidence": top_result['score'],
        "model": model_name,
    }
    
    try:
        # Write the entry to a collection named 'classification_logs'
        db.collection("classification_logs").add(log_entry)
        # Optional: Print statement for successful logging (will appear in the HF Space logs)
        # print("Log entry added to Firestore.")
    except Exception as e:
        print(f"❌ Failed to write log to Firestore: {e}")
# ----------------------------


def classify_image(image: Image.Image):
    """
    Classifies the image and logs the result before returning output for Gradio.
    """
    if image is None:
        return {"Please upload, capture, or paste an image to classify.": 0.0}

    results = image_classifier(image)
    
    # --- LOGGING CALL ---
    log_classification(results, datetime.datetime.now(), model_name)
    # --------------------

    # Format the output for Gradio's 'label' component: {label: score, ...}
    formatted_output = {item['label']: item['score'] for item in results}
    
    return formatted_output

# 3. Create and Launch the Gradio Interface
iface = gr.Interface(
    fn=classify_image,
    # sources=['upload', 'webcam', 'clipboard'] enables all desired inputs
    inputs=gr.Image(type="pil", sources=["upload", "webcam", "clipboard"]),
    
    # outputs="label" maintains the original bar chart design
    outputs="label",
    
    title="ImageNet Classification Website 🖼️",
    description="Upload, capture, or paste an image to classify it into one of the 1000 ImageNet categories using a Google Vision Transformer (ViT) model.",
)

iface.launch(
    share=False,
    server_name="0.0.0.0"
)
