# RAG for Beginners

This project is a small, educational retrieval-augmented generation (RAG) foundation. It loads text documents, turns them into vector embeddings, stores those vectors locally in Chroma, and retrieves the most similar document chunks for a natural-language query.

The included example uses a text file about Google and asks questions such as:

- When was Google founded?
- Who founded Google?
- Where is Google's head office?

The project currently performs retrieval only. It prints the matching chunks and their metadata; it does not yet send those chunks to a generative language model to produce a final answer.

## How It Works

1. `RagUtility` loads all `.txt` files from the configured document directory.
2. `ChunkingHelper` splits each document into chunks of up to 1,000 characters with 20 characters of overlap.
3. An embedding engine converts the chunks into vectors.
4. `VectorHelper` persists the vectors in `embeddings/vector_store` using Chroma with cosine similarity.
5. A query is embedded using the same engine and Chroma returns the five most similar chunks.
6. `EmbeddingHelpers` prints each result's content and metadata.

## Project Layout

```text
app.py                         Example entry point
docs/                          Source .txt documents
domain_models/criteria.py      Runtime options for each flow
EmbeddingEngines/              Embedding implementations
helpers/                       Chunking, embedding, and vector-store helpers
models/                        Flow and embedding enums
services/rag_service.py        Orchestrates indexing and search
utilities/rag_utilities.py     Loads documents from disk
embeddings/vector_store/       Persisted Chroma database
```

## Requirements

- Python 3.10 or newer
- The dependencies imported by the project, including:
  - `spacy`
  - `langchain-community`
  - `langchain-text-splitters`
  - `langchain-chroma`
  - `chromadb`
  - `langchain-openai` for OpenAI embeddings
  - `httpx2` for the current OpenAI embedding implementation

Create and activate a virtual environment, then install the dependencies using your preferred package-management workflow. For the default spaCy example, also install the model:

```powershell
python -m venv .env
.\.env\Scripts\Activate.ps1
python -m pip install spacy langchain-community langchain-text-splitters langchain-chroma chromadb langchain-openai httpx2
python -m spacy download en_core_web_md
```

## Run the Example

From the repository root:

```powershell
python app.py
```

The script first creates or updates the local vector store, then runs the three sample searches in `app.py`.

To use different documents, place `.txt` files in `docs/` or pass another directory through a `Criteria` instance. The persisted store is located at `embeddings/vector_store` and can be rebuilt by running the create-and-save flow again.

## Embedding Engines

`EmbeddingTypes` defines these options:

- `SPACY`: Implemented locally through a spaCy model. The default example uses `en_core_web_md`.
- `OPENAI`: Implemented through the OpenAI embeddings API. Set `OPENAI_API_KEY` in the environment before using it.
- `TFiDF`: Declared in the enum but not implemented; selecting it raises `NotImplementedError`.

The embedding model used to build the store must be compatible with the model used during search. In practice, rebuild the store when changing embedding models or embedding providers.

## Flows

`RagFlows` exposes three operations:

- `CREATE_AND_SAVE`: Load documents, chunk them, embed them, and persist the vectors.
- `SEARCH_INFO`: Search the existing vector store and print the top five results.
- `OVERALL`: Intended to create embeddings when needed and then search.

The executable example in `app.py` uses `CREATE_AND_SAVE` followed by `SEARCH_INFO`.

## Current Limitations

- There is no answer-generation step or chat interface yet.
- Only `.txt` files are loaded from the document directory.
- The TF-IDF embedding option is not implemented.
- `Criteria.skip_embeddings` currently defaults to true and is forced true by its constructor expression, so the overall flow's skip behavior needs cleanup before it can be used as a reliable switch.
- The OpenAI integration should use an environment variable or a secret manager exclusively. Never commit API keys to source control.
