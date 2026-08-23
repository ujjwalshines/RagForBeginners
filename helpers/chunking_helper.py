from langchain_text_splitters import CharacterTextSplitter


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
    def chunk_splitter(documents, chunk_size=1000, chunk_overlap=20):
        text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        return text_splitter.split_documents(documents)