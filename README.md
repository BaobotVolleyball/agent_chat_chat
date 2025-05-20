## System and OS Requirements:
    
    Disk: 16GB
    RAM: 16GB
    CPU: Common CPU (better CPU for faster Docs processing, only affect to Docs processing speed at first time when newly uploading)
    OS: Ubuntu-22

## Environments:

    $conda create --name demo_rag_llm_env python=3.10
    $conda activate demo_rag_llm_env
    $pip install -r requirements.txt

## Config App:

    Change essential Env Variables in flowsettings.py

    - PORT running this App: RUNNING_PORT
    - Default LLM Endpoints (OpenAI): OPENAI_API_KEY, OPENAI_CHAT_BASE, OPENAI_CHAT_MODEL
    - Default Embeddings Endpoints (OpenAI): OPENAI_API_KEY, OPENAI_EMBEDDINGS_BASE, OPENAI_EMBEDDINGS_MODEL

## Start App:

    bash run.sh

## UI Description:

    Web browser address: http://IP_or_hostname:RUNNING_PORT

    - Tab "Chat":(for Users) chat UI including: Chat Sessions, Select files for reference, Information Panel for detailing related Docs for each chatbot answer, Chat settings: choosing LLM model Endpoints available on Resources.
    - Tab "File Collection":(for Admin) Database managementincluding: Upload PDF file process and add to docs/embedding database. Interact with existing Docs in database (download, delete). Grouping Docs into different group name to query (simulate for Docs access control).
    - Tab "Resources":(for Admin) File Processing Config/LLM Endpoints/Embeddings Enpoinds
    - Tab "Settings":(for Admin) Retrieval setting: Set number of doc chunks for retrieve, Reasoning settings: System prompt
