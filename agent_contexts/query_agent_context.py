from domain_models.criteria import Criteria
from models.rag_flow import RagFlows
from services.rag_service import RagService

def get_query_response(rag_flow: RagFlows, criteria: Criteria):
      _rag_service = RagService(criteria.embedding_type)
      __result=None
      try:
          match rag_flow:
              case RagFlows.OVERALL:
                  __result=_rag_service.overall_flow(criteria)
                  pass
              case RagFlows.CREATE_AND_SAVE:
                  __result=_rag_service.create_embeddings_flow(criteria)
              case RagFlows.SEARCH_INFO:
                  __result=_rag_service.search_info_flow(criteria)
              case _:
                 __result=f"Unsupported embedding type: {criteria.embedding_type}"
      except Exception as e:
          print(f"Error while processing the query:{e}") 
          raise e
      return __result


    