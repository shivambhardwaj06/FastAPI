from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
load_dotenv()


pdf_path = Path(__file__).parent / "data" / "sample.pdf"

loader = PyPDFLoader(str(pdf_path))
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(docs)

print("Pages:", len(docs))
print("Chunks:", len(chunks))

embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-2",
    output_dimensionality=768
)

vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    collection_name="sample_collection",
    url="http://localhost:6333"
)



print("Vector store created and data indexed successfully in QdrantDB.")