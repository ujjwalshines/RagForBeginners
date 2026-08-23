
import os

from httpx2 import query
from langchain_openai import OpenAIEmbeddings


class OpenAIEmbeddingsInfo(OpenAIEmbeddings):
    def __init__(self, model_name: str = "text-embedding-3-small"):
        self.model_name = model_name
        super().__init__(model_name=model_name)
    def embed_documents(self, documents: list[str]) -> list[list[float]]:
        # Use the OpenAI API to get embeddings for the documents
        openai_api_key = os.getenv("OPENAI_API_KEY") or "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"
        response = query(
            url="https://api.openai.com/v1/embeddings",
            method="POST",
            headers={"Authorization": f"Bearer {openai_api_key}"},
            json={"model": self.model_name, "input": documents},
        )
        response.raise_for_status()
        return [item["embedding"] for item in response.json()["data"]]

    def embed_query(self, query: str) -> list[float]:
        # Use the OpenAI API to get an embedding for the query
        openai_api_key = os.getenv("OPENAI_API_KEY") or "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"
        response = query(
            url="https://api.openai.com/v1/embeddings",
            method="POST",
            headers={"Authorization": f"Bearer {openai_api_key}"},
            json={"model": self.model_name, "input": query},
        )
        response.raise_for_status()
        return response.json()["data"][0]["embedding"]