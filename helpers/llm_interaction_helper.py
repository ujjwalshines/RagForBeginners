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
        joined_context = "\n".join(LLMCriteria.retrieved_context)

        # 2. Safely inject the variable inside the f-string
        combined_input = f"""Use the following context to answer the question. If the answer cannot be found in the context, say "I don't know."Context:
                         \n{joined_context}
                         \nQuestion: {LLMCriteria.user_query}
                        """
        match LLMCriteria.LLMInteractionType:
            case InteractionLLMTypes.GOOGLE_GEN_AI:
                # Create context for Google Generative AI
                _client = genai.Client(api_key=os.getenv(constants["GOOGLE_GENAI_API_KEY"]))
                
                _interaction= _client.interactions.create(
                       model=LLMCriteria.model[LLMCriteria.model_name],
                       input=combined_input,
                       generation_config=LLMCriteria.model["CONFIG"],
                 )
                return _interaction.output_text
                pass
            case InteractionLLMTypes.OPEN_AI:
                # need to implement
                pass