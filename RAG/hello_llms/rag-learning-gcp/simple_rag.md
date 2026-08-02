# RAG Diagram


                                    ┌──────────────────────────────────────────────────────────────┐
                                    │                 PHASE 1 : INDEXING (Offline)                │
                                    └──────────────────────────────────────────────────────────────┘


                    PDF / DOCX / TXT / HTML / Database / Website
                                      │
                                      │
                                      ▼
                            ┌──────────────────┐
                            │ Document Loader  │
                            └──────────────────┘
                                      │
                                      │
                                      ▼
                           Raw Text Extracted from Documents
                                      │
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │ Text Preprocessing      │
                         │ (optional)              │
                         │ • Remove headers        │
                         │ • Remove footers        │
                         │ • Clean whitespace      │
                         │ • OCR cleanup           │
                         └─────────────────────────┘
                                      │
                                      ▼
                            ┌────────────────────┐
                            │ Chunking           │
                            │                    │
                            │ Character Split    │
                            │ Token Split        │
                            │ Recursive Split    │
                            │ Semantic Split     │
                            └────────────────────┘
                                      │
                   ┌──────────────────┴──────────────────┐
                   │                                     │
                   ▼                                     ▼
              Chunk 1                              Chunk 2
                   │                                     │
                   └───────────────┬─────────────────────┘
                                   │
                                   ▼
                   ┌─────────────────────────────────────┐
                   │ Embedding Tokenizer                 │
                   │                                     │
                   │ Converts text into Token IDs        │
                   │                                     │
                   │ Example:                            │
                   │ "What is AI"                        │
                   │        ↓                            │
                   │ [154, 72, 811]                      │
                   └─────────────────────────────────────┘
                                   │
                                   ▼
                   ┌─────────────────────────────────────┐
                   │ Embedding Model                     │
                   │                                     │
                   │ (Sentence Transformer,              │
                   │ OpenAI Embeddings, BGE, E5...)      │
                   │                                     │
                   │ Token IDs → Dense Vector            │
                   └─────────────────────────────────────┘
                                   │
                                   ▼
                 Embedding Vector (Example: 768 / 1024 / 1536 dimensions)
                                   │
                                   ▼
                     ┌──────────────────────────────────┐
                     │ Vector Database                  │
                     │                                  │
                     │ Stores:                          │
                     │ Vector + Original Chunk + Metadata│
                     │                                  │
                     │ Metadata Example:                │
                     │ File Name                        │
                     │ Page Number                      │
                     │ Source                           │
                     │ Chunk ID                         │
                     └──────────────────────────────────┘



===============================================================================================



                                    ┌──────────────────────────────────────────────────────────────┐
                                    │          PHASE 2 : RETRIEVAL + GENERATION (Online)          │
                                    └──────────────────────────────────────────────────────────────┘


                           User types a Question
                                      │
                                      ▼
                      "Explain LangChain RAG Pipeline"
                                      │
                                      ▼
                    ┌────────────────────────────────┐
                    │ Embedding Tokenizer            │
                    │                                │
                    │ Same tokenizer used during     │
                    │ indexing                       │
                    └────────────────────────────────┘
                                      │
                                      ▼
                              Query Token IDs
                                      │
                                      ▼
                    ┌────────────────────────────────┐
                    │ Embedding Model                │
                    │                                │
                    │ Converts query into vector     │
                    └────────────────────────────────┘
                                      │
                                      ▼
                               Query Vector
                                      │
                                      ▼
                    ┌────────────────────────────────┐
                    │ Retriever                      │
                    │                                │
                    │ Calls Vector DB                │
                    │ Requests Top-K Similar Chunks  │
                    └────────────────────────────────┘
                                      │
                                      ▼
                    ┌────────────────────────────────┐
                    │ Vector Database                │
                    │                                │
                    │ Similarity Search              │
                    │                                │
                    │ Cosine Similarity              │
                    │ Dot Product                    │
                    │ Euclidean Distance             │
                    │                                │
                    │ ANN Index                      │
                    │ (HNSW / IVF / PQ etc.)         │
                    └────────────────────────────────┘
                                      │
                                      ▼
                        Top K Matching Chunk IDs
                                      │
                                      ▼
                    Retrieve Original Text Chunks
                                      │
                                      ▼
              +-------------------------------------------+
              | Chunk 1                                   |
              | Chunk 2                                   |
              | Chunk 3                                   |
              +-------------------------------------------+
                                      │
                                      ▼
                    ┌────────────────────────────────┐
                    │ Prompt Builder                 │
                    │                                │
                    │ Builds Final Prompt            │
                    │                                │
                    │ System Prompt                  │
                    │ Retrieved Context              │
                    │ Conversation History           │
                    │ User Question                  │
                    └────────────────────────────────┘
                                      │
                                      ▼

          ---------------------------------------------------------
          SYSTEM:
          You are a helpful assistant.

          CONTEXT:
          Chunk 1...
          Chunk 2...
          Chunk 3...

          QUESTION:
          Explain LangChain RAG.
          ---------------------------------------------------------
                                      │
                                      ▼
                    ┌────────────────────────────────┐
                    │ LLM Tokenizer                  │
                    │                                │
                    │ Converts complete prompt       │
                    │ into Token IDs                 │
                    └────────────────────────────────┘
                                      │
                                      ▼
                               Prompt Token IDs
                                      │
                                      ▼
                    ┌────────────────────────────────┐
                    │ LLM (Transformer)              │
                    │                                │
                    │ Self Attention                 │
                    │ Feed Forward Network           │
                    │ Decoder Layers                 │
                    │                                │
                    │ Predict Next Token             │
                    └────────────────────────────────┘
                                      │
                                      ▼
                           Generated Token IDs
                                      │
                                      ▼
                    ┌────────────────────────────────┐
                    │ LLM Detokenizer                │
                    │                                │
                    │ Token IDs → Human Text         │
                    └────────────────────────────────┘
                                      │
                                      ▼
                            Final Answer to User



# End of Diagram

One Very Important Detail Most Tutorials Skip

Notice there are two completely separate tokenization processes:

Embedding Tokenizer
        │
        ▼
Embedding Model
        │
        ▼
Vector


LLM Tokenizer
        │
        ▼
LLM
        │
        ▼
Generated Answer

These are usually different tokenizers because the embedding model and the LLM are often different models.

For example:

Embedding model: text-embedding-3-small (uses its tokenizer)
LLM: Llama 3 (uses the Llama tokenizer)

They are independent.


##############################

What Actually Happens Internally in the Vector Database

Many people think the vector database loops through every vector one by one. For small datasets that can happen, but for real-world datasets with millions of vectors, that's too slow.

Instead, the vector database typically builds an Approximate Nearest Neighbor (ANN) index, such as:

HNSW (Hierarchical Navigable Small World) – very common in Qdrant, Weaviate, Chroma.
IVF (Inverted File Index) – common in FAISS.
PQ (Product Quantization) – compresses vectors for large-scale search.

When a query vector arrives, the database searches this index to quickly find the nearest vectors, then returns the associated text chunks.

Who Does What?
Component	Input	Output
Document Loader	Files	Raw text
Text Preprocessing	Raw text	Cleaned text
Chunker	Cleaned text	Chunks
Embedding Tokenizer	Chunk text / Query	Token IDs
Embedding Model	Token IDs	Dense vector
Vector Database	Vectors	Top-K similar vectors + metadata
Retriever	User query	Relevant text chunks
Prompt Builder	Context + Question	Final prompt
LLM Tokenizer	Prompt	Token IDs
LLM	Token IDs	Generated token IDs
Detokenizer	Generated token IDs	Human-readable answer

This is the complete low-level picture of a typical RAG system as used in frameworks like LangChain, LlamaIndex, Haystack, and many production AI applications. It includes all the major processing stages from raw documents to the final answer, without skipping the tokenization and embedding steps.