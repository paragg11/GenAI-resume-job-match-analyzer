
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import uuid


def semantic_search(resume_text, job_description):

    # Step 1: Load embedding model
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Step 2: Split resume into manageable chunks
    chunks = [
        chunk.strip()
        for chunk in resume_text.split("\n")
        if len(chunk.strip()) > 20
    ]

    if not chunks:
        chunks = [resume_text.strip()]

    # Step 3: Store resume chunks in ChromaDB
    vector_store = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        metadatas=[
            {"source": "resume", "chunk": i}
            for i in range(len(chunks))
        ],
        collection_name=f"resume_{uuid.uuid4().hex[:8]}"
    )

    # Step 4: Search resume using job description
    results = vector_store.similarity_search_with_score(
        job_description,
        k=min(3, len(chunks))
    )

    # Step 5: Return matching information
    return [
        {
            "content": document.page_content,
            "distance": round(float(score), 4)
        }
        for document, score in results
    ]
