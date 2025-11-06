"""
Visual Question Answering App
A multimodal AI application that answers questions about images
"""

from transformers import ViltProcessor, ViltForQuestionAnswering
from PIL import Image
import gradio as gr
import torch

# Load the pre-trained model and processor
print("Loading model... This may take a moment on first run.")
processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
print("Model loaded successfully!")

def answer_question(image, question):
    """
    Process the image and question to generate an answer
    
    Args:
        image: PIL Image object
        question: String containing the question
    
    Returns:
        String containing the answer
    """
    if image is None:
        return "Please upload an image first!"
    
    if not question or question.strip() == "":
        return "Please enter a question about the image!"
    
    try:
        # Prepare inputs
        encoding = processor(image, question, return_tensors="pt")
        
        # Get model prediction
        with torch.no_grad():
            outputs = model(**encoding)
        
        # Get the predicted answer
        logits = outputs.logits
        idx = logits.argmax(-1).item()
        answer = model.config.id2label[idx]
        
        return f"Answer: {answer}"
    
    except Exception as e:
        return f"Error processing your request: {str(e)}"

# Example questions for users to try
example_questions = [
    ["What is in the image?"],
    ["What color is the object?"],
    ["How many people are there?"],
    ["What is the person doing?"],
    ["Is this indoors or outdoors?"],
]

# Create Gradio interface
with gr.Blocks(title="Visual Question Answering App", theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        # 🖼️ Visual Question Answering App
        
        Upload an image and ask questions about it! The AI will analyze the image and answer your questions.
        
        ### How to use:
        1. Upload an image using the image box
        2. Type your question in the text box
        3. Click Submit to get your answer
        """
    )
    
    with gr.Row():
        with gr.Column():
            image_input = gr.Image(type="pil", label="Upload Image")
            question_input = gr.Textbox(
                label="Ask a Question",
                placeholder="E.g., What color is the car? How many people are in the image?",
                lines=2
            )
            submit_btn = gr.Button("Submit", variant="primary")
        
        with gr.Column():
            answer_output = gr.Textbox(
                label="Answer",
                placeholder="The answer will appear here...",
                lines=3
            )
    
    gr.Markdown("### 💡 Example Questions")
    gr.Markdown("Try questions like: *What is in the image?*, *What color is it?*, *How many objects are there?*")
    
    # Connect the interface
    submit_btn.click(
        fn=answer_question,
        inputs=[image_input, question_input],
        outputs=answer_output
    )
    
    # Also allow pressing Enter to submit
    question_input.submit(
        fn=answer_question,
        inputs=[image_input, question_input],
        outputs=answer_output
    )

# Launch the app
if __name__ == "__main__":
    print("\n" + "="*50)
    print("Starting Visual Question Answering App...")
    print("="*50 + "\n")
    demo.launch(share=False)