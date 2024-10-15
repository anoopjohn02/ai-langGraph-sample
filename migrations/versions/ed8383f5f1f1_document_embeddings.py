"""document embeddings

Revision ID: ed8383f5f1f1
Revises: dfa100ec9dd9
Create Date: 2024-09-25 15:45:49.001566

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ed8383f5f1f1'
down_revision: Union[str, None] = 'dfa100ec9dd9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(sa.DDL(
        """
        CREATE TABLE ai_assistant.document_embedding (
	        id uuid PRIMARY KEY,
	        embedding_model varchar NOT NULL,
	        chunk_size INTEGER NOT NULL,
            chunk_overlap INTEGER NOT NULL,
            token_encoding_model varchar NOT NULL
        );
        """
    ))
    op.execute(sa.DDL(
        """
        CREATE TABLE ai_assistant.document_embedding_files (
	        id uuid PRIMARY KEY,
            embedding_id uuid NOT NULL,
            file_name varchar NOT NULL,
	        num_chunks INTEGER NOT NULL,
            num_tokens INTEGER NOT NULL,
            processed_date timestamp NOT NULL,
            last_modified timestamp NOT NULL,
            CONSTRAINT document_embedding_files_fk FOREIGN KEY (embedding_id) REFERENCES ai_assistant.document_embedding(id) ON DELETE CASCADE
        );
        """
    ))


def downgrade() -> None:
    op.execute(sa.DDL(
        """
        DROP TABLE ai_assistant.document_embedding_files;
        """        
    ))
    op.execute(sa.DDL(
        """
        DROP TABLE ai_assistant.document_embedding;
        """        
    ))
