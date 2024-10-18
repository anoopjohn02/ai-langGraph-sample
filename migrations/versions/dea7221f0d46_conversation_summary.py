"""conversation summary

Revision ID: dea7221f0d46
Revises: 625d98f95683
Create Date: 2024-10-18 08:21:09.800178

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dea7221f0d46'
down_revision: Union[str, None] = '625d98f95683'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(sa.DDL(
        """
        CREATE TABLE ai_assistant.conversation_summary (
            id uuid PRIMARY KEY,
            conversation_id uuid NOT NULL,
            summary text NOT NULL,
            created_on timestamp NOT NULL,
            updated_on timestamp NOT NULL,
            CONSTRAINT conversation_messages_fk FOREIGN KEY (conversation_id) REFERENCES ai_assistant.conversation_history(id) ON DELETE CASCADE
        );
        """
    ))


def downgrade() -> None:
    op.execute(sa.DDL(
        """
        DROP TABLE ai_assistant.conversation_summary;
        """
    ))
