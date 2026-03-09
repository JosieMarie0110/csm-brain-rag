import json
import os

import gradio as gr
from dotenv import load_dotenv

from ask_brain import generate_cs_brain_response

load_dotenv()


FORMATS_FILE = "formats.json"
IMAGE_PATH = "banner1.png"


def load_format_choices():
    if not os.path.exists(FORMATS_FILE):
        return [
            "CSM Analysis",
            "Executive Brief",
            "Action Plan",
            "QBR / EBR Support"
        ]

    with open(FORMATS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    return list(data.keys())


image_component_value = IMAGE_PATH if os.path.exists(IMAGE_PATH) else None
format_choices = load_format_choices()


custom_css = """
body, .gradio-container {
    background: #f6f9fd !important;
    font-family: Arial, sans-serif;
}

.gradio-container {
    max-width: 1600px !important;
    width: 95% !important;
    margin: 0 auto !important;
    padding: 18px 18px 24px 18px !important;
}

.topbar {
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 18px;
    padding: 14px 18px;
    background: #ffffff;
    border: 1px solid #dde8f5;
    border-radius: 18px;
    box-shadow: 0 2px 10px rgba(25, 60, 120, 0.04);
}

.brand-title {
    font-size: 28px;
    font-weight: 700;
    color: #173f7a;
    line-height: 1.1;
    margin: 0;
}

.brand-subtitle {
    font-size: 14px;
    color: #54719a;
    margin-top: 6px;
    line-height: 1.4;
}

.brand-image img {
    border-radius: 14px !important;
    border: 1px solid #d9e6f7 !important;
    object-fit: cover !important;
}

.panel-card {
    background: #edf5ff !important;
    border: 1px solid #d7e7fb !important;
    border-radius: 20px !important;
    padding: 20px !important;
    box-shadow: 0 2px 10px rgba(33, 84, 160, 0.05) !important;
}

.section-label {
    font-weight: 700;
    color: #244b86;
    font-size: 1.22rem;
    margin-bottom: 10px;
}

.gr-textbox textarea {
    border-radius: 16px !important;
    border: 1px solid #cfe0f6 !important;
    background: #ffffff !important;
    font-size: 1.02rem !important;
    line-height: 1.55 !important;
    padding: 14px !important;
}

.radio-group-wrap {
    background: #f8fbff !important;
    border: 1px solid #d7e7fb !important;
    border-radius: 16px !important;
    padding: 10px !important;
}

.output-shell {
    background: #edf5ff !important;
    border: 1px solid #d7e7fb !important;
    border-radius: 20px !important;
    padding: 16px !important;
    box-shadow: 0 2px 10px rgba(33, 84, 160, 0.05) !important;
}

.markdown-output {
    background: #ffffff !important;
    border: 1px solid #d7e7fb !important;
    border-radius: 16px !important;
    padding: 20px !important;
    min-height: 420px !important;
    overflow: auto !important;
}

.markdown-output h1,
.markdown-output h2,
.markdown-output h3 {
    color: #1f4f95 !important;
    margin-top: 0.55em !important;
    margin-bottom: 0.45em !important;
}

.markdown-output p,
.markdown-output li {
    color: #243b63 !important;
    line-height: 1.68 !important;
    font-size: 1rem !important;
}

.generate-btn {
    width: 100% !important;
    margin-top: 10px !important;
}

.generate-btn button {
    width: 100% !important;
    background: #3c6dc2 !important;
    color: white !important;
    border: none !important;
    border-radius: 18px !important;
    font-weight: 700 !important;
    font-size: 1.15rem !important;
    padding: 18px !important;
    min-height: 60px !important;
    box-shadow: 0 4px 14px rgba(60, 109, 194, 0.25) !important;
}

.generate-btn button:hover {
    background: #2f5bb0 !important;
}

footer {
    display: none !important;
}
"""


with gr.Blocks(title="CS Brain") as demo:
    with gr.Row(elem_classes=["topbar"]):
        if image_component_value:
            with gr.Column(scale=1, min_width=150, elem_classes=["brand-image"]):
                gr.Image(
                    value=image_component_value,
                    show_label=False,
                    interactive=False,
                    container=False,
                    height=95
                )

        with gr.Column(scale=8, min_width=400):
            gr.HTML("""
                <div class="brand-title">CS Brain</div>
                <div class="brand-subtitle">
                    Customer Success strategy assistant for risk analysis, executive messaging, and account planning.
                </div>
            """)

    with gr.Row():
        with gr.Column(scale=5):
            with gr.Column(elem_classes=["panel-card"]):
                gr.Markdown('<div class="section-label">Ask CS Brain</div>')

                user_query = gr.Textbox(
                    placeholder="Example: Summarize the renewal risk signals and provide an executive action plan.",
                    lines=10,
                    show_label=False
                )

                gr.Markdown('<div class="section-label">Output Format</div>')

                with gr.Column(elem_classes=["radio-group-wrap"]):
                    output_format = gr.Radio(
                        choices=format_choices,
                        value=format_choices[0] if format_choices else "CSM Analysis",
                        show_label=False
                    )

                submit_btn = gr.Button(
                    "Generate Response",
                    elem_classes=["generate-btn"]
                )

        with gr.Column(scale=7):
            with gr.Column(elem_classes=["output-shell"]):
                response_output = gr.Markdown(
                    value="Your response will appear here.",
                    elem_classes=["markdown-output"]
                )

    submit_btn.click(
        fn=generate_cs_brain_response,
        inputs=[user_query, output_format],
        outputs=response_output
    )

if __name__ == "__main__":
    demo.launch(css=custom_css)
