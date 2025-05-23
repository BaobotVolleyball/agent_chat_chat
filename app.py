import os

from theflow.settings import settings as flowsettings

KH_APP_DATA_DIR = getattr(flowsettings, "KH_APP_DATA_DIR", ".")
RUNNING_PORT = getattr(flowsettings, "RUNNING_PORT", 8222)

GRADIO_TEMP_DIR = os.getenv("GRADIO_TEMP_DIR", None)
# override GRADIO_TEMP_DIR if it's not set
if GRADIO_TEMP_DIR is None:
    GRADIO_TEMP_DIR = os.path.join(KH_APP_DATA_DIR, "gradio_tmp")
    os.environ["GRADIO_TEMP_DIR"] = GRADIO_TEMP_DIR


from qcom.main import App  # noqa

app = App()
demo = app.make()
demo.queue().launch(
    server_name="0.0.0.0", server_port=int(RUNNING_PORT),
    favicon_path=app._favicon,
    inbrowser=True,
    allowed_paths=[
        "libs/qcom/qcom/assets",
        GRADIO_TEMP_DIR,
    ],
    share=False,
)