import os

from models.embedding_type import EmbeddingTypes
from EmbeddingEngines.openai_embeddings import OpenAIEmbeddingsInfo
from EmbeddingEngines.spacy_embeddings import SpacyEmbeddings
from helpers.chunking_helper import ChunkingHelper
from helpers.vector_helper import VectorHelper
from utilities.rag_utilities import RagUtility


class EmbeddingHelpers:
    @staticmethod
    def get_embeddings(embedding_type: EmbeddingTypes, model_name: str):
        match embedding_type:
            case EmbeddingTypes.OPENAI:
                return OpenAIEmbeddingsInfo(model_name)
            case EmbeddingTypes.SPACY:
                return SpacyEmbeddings(model_name)
            case EmbeddingTypes.TFiDF:
                raise NotImplementedError("TFiDF embeddings are not implemented yet.")
            case _:
                raise ValueError(f"Unsupported embedding type: {embedding_type}")

    @staticmethod
    def create_embeddings(embedding_type: EmbeddingTypes, docs:str, model_name:str):
        # Load the medium English model containing 300-dim vectors
        print(f"chunking process started...")
        embedding_function = EmbeddingHelpers.get_embeddings(embedding_type,model_name)
        documents = RagUtility.load_documents_from_directory(docs)
        chunks=ChunkingHelper.character_chunk_splitter(documents, chunk_size=1000, chunk_overlap=20)
        # chunks=ChunkingHelper.semantic_chunk_splitter(documents, buffer_size=1000)
        print(f"Total Chunks created: {len(chunks)}")
        VectorHelper.store_vectors(chunks,embedding_function, persist_directory_path=os.getenv("VECTOR_DB_PATH"))

    @staticmethod
    def search_info(embedding_type: EmbeddingTypes, query:str, model_name:str=os.getenv("SPACY_MODEL_NAME_EN_CORE_WEB_MD")):
        embedding_function = EmbeddingHelpers.get_embeddings(embedding_type, model_name)
        docs = VectorHelper.retrieve_vectors(query, embedding_function, os.getenv("VECTOR_DB_PATH"), k=5)
        docs_with_similarity = []
        
        # print(f"\nquery: {query}")
        for i, doc in enumerate(docs):
             # print(f"\nresult {i + 1}:")
             docs_with_similarity.append(f"Context {i + 1}: {doc.page_content}")
             # print(f"content: {doc.page_content}")
             #print(f"metadata: {doc.metadata}")
        return docs_with_similarity