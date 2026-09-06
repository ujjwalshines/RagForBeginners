import os

from domain_models.criteria import LLMCriteria
from models.llm_type import InteractionLLMTypes
from google import genai
from constants.rag_constant import constants
class LlmInteractionHelpers:
    @staticmethod
    def get_llm_response(llm,LLMCriteria:LLMCriteria):
        """
        Get the response from the LLM based on the provided prompt.

        Args:
            llm: The LLM instance to interact with.
            prompt: The prompt to send to the LLM.

        Returns:
            The response from the LLM.
        """
        try:
            response = llm(LLMCriteria)
            return response
        except Exception as e:
            print(f"Error while getting response from LLM: {e}")
            return None
    @staticmethod
    def create_llm_context(LLMCriteria:LLMCriteria):
        # 1. Join the list into a single string outside the f-string
        joined_context = "\n\n\n".join(LLMCriteria.retrieved_context)
        # 2. Safely inject the variable inside the f-string
        _combined_input = f"""I am a helpful assistant. I am trying to find the answer from the best suitable contexts.
                         \nUse the following contexts to answer the question. If the answer cannot be found in the context, say "I don't know."Context:
                         \n\n{joined_context}
                         \n\nQuestion: {LLMCriteria.user_query}
                        """
       
        match LLMCriteria.LLMInteractionType:
            case InteractionLLMTypes.GOOGLE_GEN_AI:
                # Create context for Google Generative AI
                # print(f"api key: {os.getenv(constants['GOOGLE_GENAI_API_KEY'])}")
                _client = genai.Client(api_key=os.getenv(constants['GOOGLE_GENAI_API_KEY']))
                # for m in _client.models.list():
                #   if "generateContent" in (m.supported_actions or []):
                #     print(f" • {m.name}")

                # print(f"model:{LLMCriteria.model}, model_name:{LLMCriteria.model_name}")
                _chat = _client.chats.create(model=LLMCriteria.model[LLMCriteria.model_name])
                _response= _chat.send_message(
                          _combined_input
                       # model=LLMCriteria.model[LLMCriteria.model_name],
                       # contents=combined_input,
                       # generation_config=LLMCriteria.model["CONFIG"],
                 )
                print(f"response: {_response.text}")
                return _response.text
                pass
            case InteractionLLMTypes.OPEN_AI:
                # need to implement
                pass