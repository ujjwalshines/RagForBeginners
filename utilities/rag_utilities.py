import os

from langchain_community.document_loaders import TextLoader,DirectoryLoader
from constants.rag_constant import constants
class RagUtility:
    @staticmethod
    def load_documents_from_directory(directory_path):
        __doc_type = os.getenv(constants['DOC_TYPE_KEY'])
        try:
            if not os.path.exists(directory_path):
                raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")
            if not os.path.isdir(directory_path):
                raise NotADirectoryError(f"The path '{directory_path}' is not a directory.")
            loader = DirectoryLoader(directory_path, glob=f'*.{__doc_type}', loader_cls=TextLoader)
            documents = loader.load()
            if(len(documents) == 0):
                    raise ValueError(f"No documents found in the directory '{directory_path}'.")
            return documents
        except Exception as e:
            print(f"Error loading documents: {e}")
            return []
