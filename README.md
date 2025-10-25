# 🖼️ Imagenet Classifier App

This repository houses the code for an image classification application deployed on the Hugging Face Hub. 
It uses a pre-trained model to classify images based on the Imagenet dataset. 
The interactive front-end is powered by Gradio.

# 🚀 Hugging Face Space Configuration

The following metadata, defined in the Space repository, controls the environment and appearance of the deployed application:

|Setting|Value|Description|
| --- | --- | --- |
| Title | Imagenet Classifier Project | Display name of the project. |
| Emoji | 👀 | The emoji used for the Space on the Hugging Face Hub. |
| Colors | green to indigo | Defines the gradient colors for the Space's UI. |
| SDK | gradio | The software development kit used to build the interface. |
| SDK Version | 5.49.1 | The specific version of Gradio used. |
| App File | app.py | The main Python script that runs the Gradio app. |
| License | apache-2.0 | The license under which the code is distributed. |

# 💻 Local Setup & Usage
To run this application locally, you'll need Python and the project dependencies.

1. Installation

  1. Clone the repository:Bash
```
git clone https://github.com/kelly7y176/Hugging-face-imagenet-classifier-app.git
cd Hugging-face-imagenet-classifier-app
```
  2. Install all required packages:Bash
```
pip install -r requirements.txt
```
2. Running the App
Execute the main application file (app.py) to launch the Gradio interface:
```
python app.py
```

The application will launch and provide a local URL (e.g., http://127.0.0.1:7860).

# 🌐 Deployment & Continuous Sync
The code in this GitHub repository is continuously synchronized with the Hugging Face Space.


### Space Link

The live, interactive version of the app is deployed here:

[tyuuu/imagenet-classifier-projectAutomated Workflow]( https://huggingface.co/spaces/tyuuu/imagenet-classifier-project)

### Automated Workflow
A GitHub Actions workflow (`.github/workflows/sync.yml`) is set up to automate deployment:

* Trigger: Any time a commit is pushed to the `main` branch of this repository.

* Action: The workflow automatically pushes those changes to the linked Hugging Face Space, ensuring the deployed app is always current with the GitHub code.


# 📂 Project Structure

|File / Folder |Description|
| --- | --- |
| app.py | Contains the core logic for the Gradio interface and the Imagenet model. |
| requirements.txt | Lists all necessary Python dependencies. |
| github/workflows/sync.yml | GitHub Actions configuration for automated deployment. |
| Configuration Files | (e.g., README.md on Hugging Face) Contains the metadata above. |

# 📜 License
This project is licensed under the **Apache-2.0 License**.

# Reference
Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

