import gradio as gr
from transformers import pipeline
def summary(text):
# Load your fine-tuned model and tokenizer
    summarizer = pipeline("summarization", model="./t5-summarization", tokenizer="./t5-summarization", device=1)
    summary = summarizer(text, max_length=600, min_length=150, length_penalty=1.0, num_beams=5, do_sample=True, temperature=0.9)

    return summary[0]["summary_text"]

interface = gr.Interface(
    fn=summary, 
    inputs=gr.Textbox(lines=10, placeholder='Enter Text Here...', label='Input text'), 
    outputs=gr.Textbox(label='Summarized Text'),
    title='Text Summarizer using T5',
    flagging_options=["Incorrect Summary", "Offensive Output", "Other"]
)
interface.launch()