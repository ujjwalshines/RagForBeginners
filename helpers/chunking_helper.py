from langchain_text_splitters import CharacterTextSplitter
from langchain_experimental.text_splitter import SemanticChunker
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from constants.rag_constant import models
class ChunkingHelper:
    @staticmethod
    def chunk_text(text, chunk_size=1000):
        """
        Splits the input text into chunks of specified size.

        :param text: The input text to be chunked.
        :param chunk_size: The maximum size of each chunk.
        :return: A list of text chunks.
        """
        return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

    @staticmethod
    def character_chunk_splitter(documents, chunk_size=1000, chunk_overlap=20):
        text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        return text_splitter.split_documents(documents)

    @staticmethod
    def semantic_chunk_splitter(documents, buffer_size=1000):
        embeddings = GoogleGenerativeAIEmbeddings(model=models["GOOGLE_GEN_AI"]["GEMINI_EMBEDDING_001"])
        text_splitter = SemanticChunker(embeddings=embeddings, breakpoint_threshold_type="percentile",buffer_size=buffer_size)
        __raw_text:str=""
        for doc in documents:
            __raw_text+=str(doc.page_content)
        __docs=text_splitter.create_documents([__raw_text])
        print(f"Total Semantic Chunks created: {len(__docs)}")
        return __docs