import os
from dotenv import load_dotenv
from agent_contexts.query_agent_context import get_query_response
from agents.query_agent import agent
from domain_models.criteria import Criteria
from models.embedding_type import EmbeddingTypes
from models.embedding_type import EmbeddingTypes
from domain_models.criteria import Criteria
from models.rag_flow import RagFlows
from constants.rag_constant import constants
load_dotenv()
# def main(rag_flow: RagFlows, criteria: Criteria):

#     _rag_service = RagService(criteria.embedding_type)
#     match rag_flow:
#                 case RagFlows.OVERALL:
#                     _rag_service.overall_flow(criteria)
#                     pass
#                 case RagFlows.CREATE_AND_SAVE:
#                     _rag_service.create_embeddings_flow(criteria)
#                 case RagFlows.SEARCH_INFO:
#                     _rag_service.search_info_flow(criteria)
#                 case _:
#                     raise ValueError(f"Unsupported embedding type: {embedding_type}")

if __name__ == "__main__":


    print(f"Plese enter your flow, type: \n1. CREATE_AND_SAVE, \n2. SEARCH_INFO")
    flow = input("Enter your flow: ")
    if flow not in ["1", "2"]:
        print(f"Invalid flow type. Please enter one of the following: OVERALL, CREATE_AND_SAVE, SEARCH_INFO")
        exit(1)
    while True:
        match flow:
            case "1":
                print(f"Creating and saving embeddings...")
                get_query_response(rag_flow=RagFlows.CREATE_AND_SAVE, criteria=Criteria(embedding_type=EmbeddingTypes.SPACY, doc_path="docs", model_name=os.getenv(constants["SPACY_MODEL_NAME_TOKEN"]), skip_embeddings=False))
            case "2":
                query = input("Enter your query: ")
                response = agent.invoke({"messages": [("user", query)]})
                print(f"\n\nAnswer:")
                print(response["messages"][-1].content[0]["text"])
        if flow=="1":
            print(f"Embeddings created and saved successfully.")
            break
        user_input = input("Do you wish to Continue? (type 'exit' to quit): ")
        print(f"==============================================================")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
#   main(rag_flow=RagFlows.CREATE_AND_SAVE, criteria=Criteria(embedding_type=EmbeddingTypes.SPACY, doc_path="docs", model_name=os.getenv(constants["SPACY_MODEL_NAME_TOKEN"]), skip_embeddings=False))
    # main(rag_flow=RagFlows.SEARCH_INFO, criteria=Criteria(embedding_type=EmbeddingTypes.SPACY, query_text="when google is founded?", doc_path="docs", model_name=os.getenv(constants["SPACY_MODEL_NAME_TOKEN"])))
    # main(rag_flow=RagFlows.SEARCH_INFO, criteria=Criteria(embedding_type=EmbeddingTypes.SPACY, query_text="who is the founder of google?", doc_path="docs", model_name=os.getenv(constants["SPACY_MODEL_NAME_TOKEN"])))
    # main(rag_flow=RagFlows.SEARCH_INFO, criteria=Criteria(embedding_type=EmbeddingTypes.SPACY, query_text="where the head office of google is situated?", doc_path="docs", model_name=os.getenv(constants["SPACY_MODEL_NAME_TOKEN"])))