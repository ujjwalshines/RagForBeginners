import os

from chromadb import Documents
from langchain_chroma import Chroma

from EmbeddingEngines.openai_embeddings import OpenAIEmbeddingsInfo
from EmbeddingEngines.spacy_embeddings import SpacyEmbeddings


class VectorHelper:
    @staticmethod
    def get_vector_length(vector):
        """
        Get the length of a vector.

        Args:
            vector (list): The vector to calculate the length of.

        Returns:
            float: The length of the vector.
        """
        return sum(x ** 2 for x in vector) ** 0.5

    @staticmethod
    def store_vectors(chunks:list[Documents],embeddings:SpacyEmbeddings, persist_directory_path:str):
    # Persist the vector store to disk
     vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_directory_path or os.getenv("VECTOR_DB_PATH"),
        collection_metadata={"hnsw:space": "cosine"}
    
        )

    @staticmethod
    def retrieve_vectors(query:str, embedding_function:SpacyEmbeddings | OpenAIEmbeddingsInfo, persist_directory_path:str, k:int=5):
        vector_store = Chroma(persist_directory=persist_directory_path, embedding_function=embedding_function)
    
        # Perform a similarity search
        docs = vector_store.similarity_search(query, k=k)
        return docs

     