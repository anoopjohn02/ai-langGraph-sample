"""conversation history

Revision ID: 903e7e7f31ce
Revises: db24ffcf3023
Create Date: 2024-09-06 10:00:47.804168

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '903e7e7f31ce'
down_revision: Union[str, None] = 'db24ffcf3023'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(sa.DDL(
        """
        CREATE TABLE ai_assistant.conversation_history (
	        id uuid PRIMARY KEY,
	        retriever varchar NULL,
	        memory varchar NULL,
	        llm varchar NULL,
	        created_on timestamp NOT NULL,
	        user_id uuid NOT NULL
        );
        """
    ))


def downgrade() -> None:
    op.execute(sa.DDL(
        """
        DROP TABLE ai_assistant.conversation_history;
        """
    ))
