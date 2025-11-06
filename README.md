# Visual Question Answering App 

[![Open in Spaces](https://huggingface.co/datasets/huggingface/badges/raw/main/open-in-hf-spaces-lg.svg)](https://huggingface.co/spaces/Sakshi3027/vqa-app)

**🚀 [Try the Live Demo Here!](https://huggingface.co/spaces/Sakshi3027/vqa-app)**

A multimodal AI application that answers questions about images using Vision-and-Language Transformer (ViLT).

## Features

- Upload any image
- Ask questions in natural language
- Get AI-powered answers
- Fast and accurate responses
- Modern web interface

## Live Demo

Try it now: **[https://huggingface.co/spaces/Sakshi3027/vqa-app](https://huggingface.co/spaces/Sakshi3027/vqa-app)**

##  Technologies Used

- **Hugging Face Transformers** - Pre-trained VQA model
- **Gradio** - Interactive web interface
- **PyTorch** - Deep learning framework
- **Python** - Programming language

##  Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Steps

1. Clone the repository:
```bash
git clone https://github.com/Sakshi3027/vqa-app.git
cd vqa-app
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the app:
```bash
python app.py
```

5. Open your browser at `http://127.0.0.1:7860`

##  How It Works

This app uses **Vision-and-Language Transformer (ViLT)** - a multimodal model that processes images and text simultaneously to understand and answer questions about visual content.

### Example Questions:
- "What color is the car?"
- "How many people are in the image?"
- "What is the person doing?"
- "Is this indoors or outdoors?"
- "What objects can you see?"

## Project Structure
```
vqa-app/
├── app.py              # Main application
├── requirements.txt    # Dependencies
├── README.md          # Documentation
└── .gitignore         # Git ignore rules
```

##  Model Information

- **Model**: `dandelin/vilt-b32-finetuned-vqa`
- **Architecture**: Vision Transformer + BERT
- **Training Data**: VQA v2.0 dataset
- **Parameters**: ~113M

##  Use Cases

- Educational tools for learning AI
- Accessibility applications
- Image analysis and understanding
- Content moderation assistance
- Visual search and discovery

##  License

MIT License - feel free to use this project!

##  Acknowledgments

- [Hugging Face](https://huggingface.co/) for models and infrastructure
- [Gradio](https://gradio.app/) for the amazing UI framework
- ViLT paper: [arXiv:2102.03334](https://arxiv.org/abs/2102.03334)

##  Contact

**Sakshi3027** - [GitHub Profile](https://github.com/Sakshi3027)

**Live Demo**: [https://huggingface.co/spaces/Sakshi3027/vqa-app](https://huggingface.co/spaces/Sakshi3027/vqa-app)

---


