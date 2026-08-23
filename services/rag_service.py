from domain_models.criteria import Criteria
from models.embedding_type import EmbeddingTypes
from helpers.embedding_helpers import EmbeddingHelpers


class RagService:
    def __init__(self, embedding_type:EmbeddingTypes):
        self.embedding_type = embedding_type


    def overall_flow(self, criteria: Criteria):
        if not criteria.skip_embeddings:
            EmbeddingHelpers.create_embeddings(self.embedding_type, criteria.doc_path, criteria.model_name)
        EmbeddingHelpers.search_info(self.embedding_type, criteria.query_text, criteria.model_name)

    def create_embeddings_flow(self, criteria: Criteria):
        EmbeddingHelpers.create_embeddings(self.embedding_type, criteria.doc_path, criteria.model_name)

    def search_info_flow(self, criteria: Criteria):
        EmbeddingHelpers.search_info(self.embedding_type, criteria.query_text, criteria.model_name)
       