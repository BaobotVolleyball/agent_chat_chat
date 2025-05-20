import os
from importlib.metadata import version
from inspect import currentframe, getframeinfo
from pathlib import Path

from decouple import config
from qcom.utils.lang import SUPPORTED_LANGUAGE_MAP # ok
from theflow.settings.default import *  # ok

cur_frame = currentframe()
if cur_frame is None:
    raise ValueError("Cannot get the current frame.")
this_file = getframeinfo(cur_frame).filename
this_dir = Path(this_file).parent

# PORT running this App
RUNNING_PORT = config("RUNNING_PORT", default=8333, cast=int)
# Config for OpenAI compatible API model from Cirrascale
KH_LLMS = {}
KH_EMBEDDINGS = {}
KH_RERANKINGS = {}

OPENAI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
OPENAI_CHAT_BASE = "https://aisuite.cirrascale.com/apis/v2"
OPENAI_EMBEDDINGS_BASE = "https://aisuite.cirrascale.com/apis/v2"
OPENAI_CHAT_MODEL = "Llama-3.1-8B"
OPENAI_EMBEDDINGS_MODEL = "BAAI/bge-large-en-v1.5"
if OPENAI_API_KEY:
    KH_LLMS["Llama-3.1-8B (Cirrascale)"] = {
        "spec": {
            "__type__": "kotaemon.llms.ChatOpenAI",
            "base_url": OPENAI_CHAT_BASE,
            "api_key": OPENAI_API_KEY,
            "model": OPENAI_CHAT_MODEL,
            "timeout": 200,
            "temperature": 0.7,
            "top_p": 0.95,
        },
        "default": True,
    }

    KH_LLMS["Llama-3.1-8B (Localhost)"] = {
        "spec": {
            "__type__": "kotaemon.llms.ChatOpenAI",
            "base_url": "http://z24:8000/v1",
            "api_key": OPENAI_API_KEY,
            "model": "meta-llama/Llama-3.1-8B-Instruct",
            "timeout": 20,
            "temperature": 0.7,
            "top_p": 0.95,
        },
        "default": False,
    }
    KH_EMBEDDINGS["BAAI/bge-large-en-v1.5(Cirrascale)"] = {
        "spec": {
            "__type__": "kotaemon.embeddings.OpenAIEmbeddings",
            "base_url": OPENAI_EMBEDDINGS_BASE,
            "api_key": OPENAI_API_KEY,
            "model": OPENAI_EMBEDDINGS_MODEL,
            "timeout": 200,
        },
        "default": True,
    }


# change this if your app use a different name
KH_PACKAGE_NAME = "demo_assistant_app"

KH_APP_VERSION = config("KH_APP_VERSION", None)
KH_APP_VERSION = "local"

KH_GRADIO_SHARE = config("KH_GRADIO_SHARE", default=False, cast=bool)
KH_ENABLE_FIRST_SETUP = config("KH_ENABLE_FIRST_SETUP", default=False, cast=bool)
KH_DEMO_MODE = config("KH_DEMO_MODE", default=False, cast=bool)

# App can be ran from anywhere and it's not trivial to decide where to store app data.
# So let's use the same directory as the flowsetting.py file.
KH_APP_DATA_DIR = this_dir / "qcom_app_data"
KH_APP_DATA_EXISTS = KH_APP_DATA_DIR.exists()
KH_APP_DATA_DIR.mkdir(parents=True, exist_ok=True)

# User data directory
KH_USER_DATA_DIR = KH_APP_DATA_DIR / "user_data"
KH_USER_DATA_DIR.mkdir(parents=True, exist_ok=True)

# markdown output directory
KH_MARKDOWN_OUTPUT_DIR = KH_APP_DATA_DIR / "markdown_cache_dir"
KH_MARKDOWN_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# chunks output directory
KH_CHUNKS_OUTPUT_DIR = KH_APP_DATA_DIR / "chunks_cache_dir"
KH_CHUNKS_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# zip output directory
KH_ZIP_OUTPUT_DIR = KH_APP_DATA_DIR / "zip_cache_dir"
KH_ZIP_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# zip input directory
KH_ZIP_INPUT_DIR = KH_APP_DATA_DIR / "zip_cache_dir_in"
KH_ZIP_INPUT_DIR.mkdir(parents=True, exist_ok=True)

# HF models cache
os.environ["HF_HOME"] = str(KH_APP_DATA_DIR / "huggingface")
os.environ["HF_HUB_CACHE"] = str(KH_APP_DATA_DIR / "huggingface")

# doc directory
KH_DOC_DIR = this_dir / "docs"

KH_MODE = "dev"

KH_SSO_ENABLED = config("KH_SSO_ENABLED", default=False, cast=bool)

KH_FEATURE_CHAT_SUGGESTION = config(
    "KH_FEATURE_CHAT_SUGGESTION", default=False, cast=bool
)

KH_FEATURE_USER_MANAGEMENT = config(
    "KH_FEATURE_USER_MANAGEMENT", default=False, cast=bool
)

KH_USER_CAN_SEE_PUBLIC = None
KH_FEATURE_USER_MANAGEMENT_ADMIN = str(
    config("KH_FEATURE_USER_MANAGEMENT_ADMIN", default="admin")
)
KH_FEATURE_USER_MANAGEMENT_PASSWORD = str(
    config("KH_FEATURE_USER_MANAGEMENT_PASSWORD", default="admin")
)

KH_ENABLE_ALEMBIC = False

KH_DATABASE = f"sqlite:///{KH_USER_DATA_DIR / 'sql.db'}"
KH_FILESTORAGE_PATH = str(KH_USER_DATA_DIR / "files")
KH_WEB_SEARCH_BACKEND = (
    # "kotaemon.indices.retrievers.tavily_web_search.WebSearch"
    # "kotaemon.indices.retrievers.jina_web_search.WebSearch"
)

KH_DOCSTORE = {
    # "__type__": "kotaemon.storages.ElasticsearchDocumentStore",
    # "__type__": "kotaemon.storages.SimpleFileDocumentStore",
    "__type__": "kotaemon.storages.LanceDBDocumentStore",
    "path": str(KH_USER_DATA_DIR / "docstore"),
}
KH_VECTORSTORE = {
    # "__type__": "kotaemon.storages.LanceDBVectorStore",
    "__type__": "kotaemon.storages.ChromaVectorStore",
    # "__type__": "kotaemon.storages.MilvusVectorStore",
    # "__type__": "kotaemon.storages.QdrantVectorStore",
    "path": str(KH_USER_DATA_DIR / "vectorstore"),
}


KH_REASONINGS = [
    "qcom.reasoning.docs_assistant.FullQAPipeline",
]

KH_REASONINGS_USE_MULTIMODAL = config("USE_MULTIMODAL", default=False, cast=bool)
KH_VLM_ENDPOINT = ""

SETTINGS_APP: dict[str, dict] = {}


SETTINGS_REASONING = {
    "use": {
        "name": "Reasoning options",
        "value": None,
        "choices": [],
        "component": "radio",
    },
    "lang": {
        "name": "Language",
        "value": "vi",
        "choices": [(lang, code) for code, lang in SUPPORTED_LANGUAGE_MAP.items()],
        "component": "dropdown",
    },
    "max_context_length": {
        "name": "Max context length (LLM)",
        "value": 4096,
        "component": "number",
    },
}

USE_GLOBAL_GRAPHRAG = config("USE_GLOBAL_GRAPHRAG", default=False, cast=bool)
USE_NANO_GRAPHRAG = config("USE_NANO_GRAPHRAG", default=False, cast=bool)
USE_LIGHTRAG = config("USE_LIGHTRAG", default=False, cast=bool)
USE_MS_GRAPHRAG = config("USE_MS_GRAPHRAG", default=True, cast=bool)

GRAPHRAG_INDEX_TYPES = []

KH_INDEX_TYPES = [
    "qcom.index.file.FileIndex",
    *GRAPHRAG_INDEX_TYPES,
]

GRAPHRAG_INDICES = [
    {
        "name": graph_type.split(".")[-1].replace("Index", "")
        + " Collection",  # get last name
        "config": {
            "supported_file_types": (
                ".pdf"
            ),
            "private": True,
        },
        "index_type": graph_type,
    }
    for graph_type in GRAPHRAG_INDEX_TYPES
]

KH_INDICES = [
    {
        "name": "File Collection",
        "config": {
            "supported_file_types": (
                ".pdf"
            ),
            "private": True,
        },
        "index_type": "qcom.index.file.FileIndex",
    },
    *GRAPHRAG_INDICES,
]
