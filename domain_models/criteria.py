from models.embedding_type import EmbeddingTypes


class Criteria:
    def __init__(self, embedding_type: EmbeddingTypes, query_text: str='', doc_path: str='docs', model_name:str='en_core_web_md',skip_embeddings:bool=True):
        self.embedding_type = embedding_type
        self.query_text = query_text or ''
        self.doc_path = doc_path or 'docs'
        self.model_name = model_name
        self.skip_embeddings = skip_embeddings or True