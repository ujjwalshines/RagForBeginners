from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain_core.tools import tool
from agent_contexts.query_agent_context import get_query_response
from domain_models.criteria import Criteria 
from constants.rag_constant import constants,models
from models.embedding_type import EmbeddingTypes
from models.rag_flow import RagFlows
import os
from dotenv import load_dotenv
load_dotenv()

@tool
def get_query_info(query:str):
    """Retrieves specific information related to the user's RAG query from the database."""
    return get_query_response(rag_flow=RagFlows.SEARCH_INFO, criteria=Criteria(embedding_type=EmbeddingTypes.SPACY, query_text=query, doc_path="docs", model_name=os.getenv(constants["SPACY_MODEL_NAME_TOKEN"])))

# query_tool = tool(
#     name="query_master",
#     func=get_query_info,
#     description="get information based on a query. input: query text (string)."
# )

llm = ChatGoogleGenerativeAI(
    model=models["GOOGLE_GEN_AI"]["GEMINI_FLASH_3_8"],  # or gemini-1.5-flash for faster responses
    temperature=0
)

# react_prompt = hub.pull("hwchase17/react")

agent = create_agent(llm, [get_query_info], system_prompt="You are a helpful assistant.")

#agent_executor = AgentExecutor(agent=agent, tools=[query_tool], verbose=True)
