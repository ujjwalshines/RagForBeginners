constants={
    "SPACY_MODEL_NAME_TOKEN":"SPACY_MODEL_NAME_EN_CORE_WEB_MD",
    "SPACY_MODEL_NAME_EN_CORE_WEB_MD": "en_core_web_md",
    "VECTOR_DB_PATH": "embeddings/vector_store",
    "GOOGLE_GENAI_API_KEY": "GOOGLE_API_KEY",
    "DOC_TYPE_KEY":"DOC_TYPE",
}

models={
    "GOOGLE_GEN_AI":{
        "GEMINI_FLASH_3_8B":"models/gemini-flash-3b",
        "GEMINI_1_5B":"models/gemini-1.5b",
        "GEMINI_FLASH_3_8":"models/gemini-3.8-flash",
        "TEXT_EMBEDDING_004":"models/text-embedding-004",
        "GEMINI_EMBEDDING_001":"gemini-embedding-001",
        "CONFIG" : {'max_output_tokens': 65536,'thinking_level': 'medium',}

    },
    "OPEN_AI":{
        "GPT_3_5_TURBO":"gpt-3.5-turbo",
        "GPT_4":"gpt-4"
    }
}