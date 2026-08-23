import spacy
from langchain_chroma import Chroma
from langchain_core.embeddings import Embeddings
from langchain_core.documents import Document

class SpacyEmbeddings(Embeddings):
    def __init__(self, model_name: str = "en_core_web_md"):
        self.nlp = spacy.load(model_name)

    def embed_documents(self, texts):
        return [self.nlp(text).vector for text in texts]

    def embed_query(self, text):
        return self.nlp(text).vector
