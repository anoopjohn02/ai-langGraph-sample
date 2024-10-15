"""conversation messages

Revision ID: d701eef05c35
Revises: 903e7e7f31ce
Create Date: 2024-09-06 10:40:52.146795

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import app.config as config


# revision identifiers, used by Alembic.
revision: str = 'd701eef05c35'
down_revision: Union[str, None] = '903e7e7f31ce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(sa.DDL(
        """
        CREATE TABLE ai_assistant.conversation_messages (
	        id uuid PRIMARY KEY,
	        conversation_id uuid NOT NULL,
	        "role" varchar NOT NULL,
	        "content" text NOT NULL,
	        created_on timestamp NOT NULL,
	        CONSTRAINT conversation_messages_fk FOREIGN KEY (conversation_id) REFERENCES ai_assistant.conversation_history(id) ON DELETE CASCADE
        );
        """
    ))


def downgrade() -> None:
    op.execute(sa.DDL(
        """
        DROP TABLE ai_assistant.conversation_messages;
        """
    ))
