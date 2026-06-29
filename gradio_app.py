import gradio as gr
from app import summarize_website

with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.Markdown("# 🚀 AI Website Summarizer")

    gr.Markdown(
        """
Summarize any website using Llama 3.3 running on Groq.

Created by Karthik R
"""
    )

    url = gr.Textbox(
        label="Website URL",
        placeholder="https://openai.com"
    )

    summarize_button = gr.Button("🚀 Summarize Website")

    output = gr.Markdown()

    gr.Examples(
        examples=[
            ["https://openai.com"],
            ["https://www.nasa.gov"],
            ["https://www.microsoft.com"]
        ],
        inputs=url
    )

    summarize_button.click(
        fn=summarize_website,
        inputs=url,
        outputs=output
    )

demo.launch()