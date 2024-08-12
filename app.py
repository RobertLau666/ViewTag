import gradio as gr
from configs import config
if config.view_mode == 2:
    from apps.show_image_app_2 import show_image
elif config.view_mode == 1:
    from apps.show_image_app_1 import show_image
from apps.show_result_app import show_result


with gr.Blocks() as demo:
    gr.Markdown("""
                <div style="view: inline">
                <strong><em>ViewTag: Image viewing and tagging platform</em></strong>
                </div>
                """)

    with gr.Tabs():
        with gr.TabItem("show image") as tab_show_image:
            show_image()
        with gr.TabItem("show result") as tab_show_result:
            show_result()

demo.queue().launch(server_port=config.port, server_name="0.0.0.0", share=True)
