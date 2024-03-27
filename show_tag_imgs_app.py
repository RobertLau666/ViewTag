import gradio as gr

from apps.show_image_app import show_image
from apps.show_result_app import show_result

from configs import config

with gr.Blocks() as demo:
    gr.Markdown("""
                <div style="display: inline">
                <strong><em>Image display and tag platform</em></strong>
                </div>
                """)

    with gr.Tabs():
        with gr.TabItem("show image") as tab_show_image:
            show_image()
        with gr.TabItem("show result") as tab_show_result:
            show_result()

demo.queue().launch(server_port=config.port, server_name="0.0.0.0", share=True)
