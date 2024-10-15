"""store token usage

Revision ID: dfa100ec9dd9
Revises: 04459aa76cf6
Create Date: 2024-09-23 09:03:57.013228

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dfa100ec9dd9'
down_revision: Union[str, None] = '04459aa76cf6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(sa.DDL(
        """
        ALTER TABLE ai_assistant.conversation_messages ADD transaction_id uuid NULL;
        CREATE TABLE ai_assistant.messages_token_usage (
	        id uuid PRIMARY KEY,
            conversation_id uuid NOT NULL,
	        transaction_id uuid NOT NULL,
	        prompt_tokens INTEGER NOT NULL,
	        output_tokens INTEGER NOT NULL,
            prompt_cost NUMERIC NOT NULL,
            output_cost NUMERIC NOT NULL,
            embedding_cost NUMERIC NOT NULL,
            llm_model varchar NULL,
	        embedding_model varchar NULL,
            start_time timestamp NOT NULL,
            end_time timestamp NOT NULL,
	        created_on timestamp NOT NULL,
            CONSTRAINT conversation_messages_token_usage_fk FOREIGN KEY (conversation_id) REFERENCES ai_assistant.conversation_history(id) ON DELETE CASCADE
        );
        """
    ))


def downgrade() -> None:
    op.execute(sa.DDL(
        """
        ALTER TABLE ai_assistant.conversation_messages DROP COLUMN transaction_id;
        DROP TABLE ai_assistant.messages_token_usage;
        """
    ))
