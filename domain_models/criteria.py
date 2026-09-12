import os

from models.embedding_type import EmbeddingTypes
from models.llm_type import InteractionLLMTypes


class Criteria:
    def __init__(self, embedding_type: EmbeddingTypes, query_text: str='', doc_path: str='docs', model_name:str=os.getenv("SPACY_MODEL_NAME_EN_CORE_WEB_MD"),skip_embeddings:bool=True):
        self.embedding_type = embedding_type
        self.query_text = query_text or ''
        self.doc_path = doc_path or 'docs'
        self.model_name = model_name or os.getenv("SPACY_MODEL_NAME_EN_CORE_WEB_MD") or 'en_core_web_md'
        self.skip_embeddings = skip_embeddings or True
class LLMCriteria:
    def __init__(self,LLMInteractionType:InteractionLLMTypes,model,model_name:str,retrieved_context,user_query:str):
        self.LLMInteractionType=LLMInteractionType
        self.model=model
        self.model_name=model_name
        self.retrieved_context=retrieved_context
        self.user_query=user_query