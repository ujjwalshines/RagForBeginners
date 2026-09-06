from domain_models.criteria import Criteria, LLMCriteria
from helpers.llm_interaction_helper import LlmInteractionHelpers
from models.embedding_type import EmbeddingTypes
from helpers.embedding_helpers import EmbeddingHelpers
from constants.rag_constant import models
from models.llm_type import InteractionLLMTypes


class RagService:
    def __init__(self, embedding_type:EmbeddingTypes):
        self.embedding_type = embedding_type


    def overall_flow(self, criteria: Criteria):
        if not criteria.skip_embeddings:
            EmbeddingHelpers.create_embeddings(self.embedding_type, criteria.doc_path, criteria.model_name)
        retrieved_context=EmbeddingHelpers.search_info(self.embedding_type, criteria.query_text, criteria.model_name)
        return self.__generate_llm_response(criteria, retrieved_context)
    def create_embeddings_flow(self, criteria: Criteria):
        EmbeddingHelpers.create_embeddings(self.embedding_type, criteria.doc_path, criteria.model_name)

    def search_info_flow(self, criteria: Criteria):
        retrieved_context=EmbeddingHelpers.search_info(self.embedding_type, criteria.query_text, criteria.model_name)
        return self.__generate_llm_response(criteria, retrieved_context)

    def __generate_llm_response(self, criteria: Criteria,retrieved_context):
        _model=models["GOOGLE_GEN_AI"]
        llmCriteria=LLMCriteria(
                    LLMInteractionType=InteractionLLMTypes.GOOGLE_GEN_AI,
                    model=_model,
                    model_name=_model["GEMINI_FLASH_3_8"],
                    retrieved_context=retrieved_context,
                    user_query=criteria.query_text
                )
        print(f" sending data to LLM for response gen: {LLMCriteria}")
        _response=LlmInteractionHelpers.get_llm_response(llm=LlmInteractionHelpers.create_llm_context, LLMCriteria=llmCriteria)
        print(f" =====================================================================")
        print(f"response: {_response}")
        return _response
       