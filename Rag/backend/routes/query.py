from fastapi import APIRouter
from google import genai
from langchain_qdrant import QdrantVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings

router = APIRouter(
    prefix="/query",
    tags=["query"],
)

embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-2",
    output_dimensionality=768
)

vector_db = QdrantVectorStore.from_existing_collection(
    embedding=embedding_model,
    collection_name="sample_collection",
    url="http://localhost:6333"
)

client = genai.Client()


@router.post("/")
async def query(question: str):

    search_results = vector_db.similarity_search(
        query=question,
        k=4
    )

    # Print retrieved chunks and their page numbers
    print("\n" + "=" * 60)
    print("RETRIEVED CHUNKS")
    print("=" * 60)

    for i, result in enumerate(search_results, start=1):
        page = result.metadata.get("page", "unknown")

        print(f"\nChunk {i}")
        print(f"Page: {page}")
        print(f"Content: {result.page_content[:500]}")
        print("-" * 60)

    context = "\n\n".join(
        [
            f"[Page {result.metadata.get('page', 'unknown')}] "
            f"{result.page_content}"
            for result in search_results
        ]
    )

    SYSTEM_PROMPT = f"""
You are a helpful assistant that answers questions based only on the
provided context.

If the context does not contain the answer, respond with "I don't know."

Always mention the page number when the answer comes from a specific page.

Context:
{context}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
{SYSTEM_PROMPT}

Question:
{question}
"""
    )

    return {
        "question": question,
        "answer": response.text
    }