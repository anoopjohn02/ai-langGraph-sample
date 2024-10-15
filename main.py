"""
Main module
"""
from app.web.router import start
from app.web import register_app
from app.data import check_db
from app.ai import process_documents

if __name__ == "__main__":
    check_db()
    process_documents()
    #register_app()
    start()
