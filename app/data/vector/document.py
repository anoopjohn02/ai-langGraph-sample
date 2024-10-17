"""
Document module
"""
import logging
import os
import uuid
from datetime import datetime

import tiktoken
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

from app.config import OpenaiConfig as config
from app.config import OpenaiConfig
from app.config import PDF_DIRECTORY
from app.data.sql.entities import DocumentEmbedding, DocumentEmbeddingFiles
from app.data.sql.repo import DocumentEmbeddingRepo, DocumentEmbeddingFilesRepo
from . import build_vector_store

logging.basicConfig(level=logging.INFO)

embedding_repo = DocumentEmbeddingRepo()
embedding_file_repo = DocumentEmbeddingFilesRepo()

def calculate_tokens(texts):
    """
    Method to calculate token
    """
    encoding = tiktoken.encoding_for_model(config.EMBEDDING_MODEL)
    total_tokens = sum(len(encoding.encode(text.page_content))
                       for text in texts)
    return total_tokens


def process_documents(chunk_size = 1000, chunk_overlap = 200):
    """
    Method to process document
    """
    embeddings = embedding_repo.get_all()
    if len(embeddings) > 0:
        document_embeddings = embeddings[0]
    else:
        document_embeddings = DocumentEmbedding()
        document_embeddings.id = uuid.uuid1()
        document_embeddings.embedding_model = config.EMBEDDING_MODEL
        document_embeddings.chunk_size = chunk_size
        document_embeddings.chunk_overlap = chunk_overlap
        document_embeddings.token_encoding_model = OpenaiConfig.model
        document_embeddings.files = []

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    metadata = {getattr(file, "file_name"): file for file in document_embeddings.files}

    vectorstore = build_vector_store()
    for filename in os.listdir(PDF_DIRECTORY):
        if filename.endswith('.pdf'):
            file_path = os.path.join(PDF_DIRECTORY, filename)
            file_mtime = os.path.getmtime(file_path)

            # Check if file has been modified since last processing
            if filename in metadata and (file_mtime - metadata[filename].last_modified.timestamp() < 5):
                logging.info("Skipping %s - already processed", filename)
                continue

            logging.info("Processing file: %s", filename)
            loader = PyPDFLoader(file_path)
            pdf_documents = loader.load()
            texts = text_splitter.split_documents(pdf_documents)

            # Add or update embeddings for this file
            vectorstore.add_documents(texts)

            embedding_file = DocumentEmbeddingFiles()
            embedding_file.id = uuid.uuid1()
            embedding_file.file_name = filename
            embedding_file.num_chunks = len(texts)
            embedding_file.num_tokens = calculate_tokens(texts)
            embedding_file.processed_date = datetime.now()
            embedding_file.last_modified = datetime.fromtimestamp(file_mtime)
            document_embeddings.files.append(embedding_file)

    embedding_repo.save_embeddings(document_embeddings)
    logging.info("Embedding processing completed")
