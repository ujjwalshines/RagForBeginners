import os

from domain_models.criteria import Criteria
from models.embedding_type import EmbeddingTypes
from models.rag_flow import RagFlows
from services import rag_service
from services.rag_service import RagService
from constants.rag_constant import constants


from dotenv import load_dotenv
load_dotenv()
def main(rag_flow: RagFlows, criteria: Criteria):

    _rag_service = RagService(criteria.embedding_type)
    match rag_flow:
                case RagFlows.OVERALL:
                    _rag_service.overall_flow(criteria)
                    pass
                case RagFlows.CREATE_AND_SAVE:
                    _rag_service.create_embeddings_flow(criteria)
                case RagFlows.SEARCH_INFO:
                    _rag_service.search_info_flow(criteria)
                case _:
                    raise ValueError(f"Unsupported embedding type: {embedding_type}")

if __name__ == "__main__":
   main(rag_flow=RagFlows.CREATE_AND_SAVE, criteria=Criteria(embedding_type=EmbeddingTypes.SPACY, doc_path="docs", model_name=os.getenv(constants["SPACY_MODEL_NAME_TOKEN"]), skip_embeddings=False))
   main(rag_flow=RagFlows.SEARCH_INFO, criteria=Criteria(embedding_type=EmbeddingTypes.SPACY, query_text="when google is founded?", doc_path="docs", model_name=os.getenv(constants["SPACY_MODEL_NAME_TOKEN"])))
   main(rag_flow=RagFlows.SEARCH_INFO, criteria=Criteria(embedding_type=EmbeddingTypes.SPACY, query_text="who is the founder of google?", doc_path="docs", model_name=os.getenv(constants["SPACY_MODEL_NAME_TOKEN"])))
   main(rag_flow=RagFlows.SEARCH_INFO, criteria=Criteria(embedding_type=EmbeddingTypes.SPACY, query_text="where the head office of google is situated?", doc_path="docs", model_name=os.getenv(constants["SPACY_MODEL_NAME_TOKEN"])))