"""new column for conversation delete

Revision ID: 04459aa76cf6
Revises: d701eef05c35
Create Date: 2024-09-23 09:02:58.226952

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '04459aa76cf6'
down_revision: Union[str, None] = 'd701eef05c35'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(sa.DDL(
        """
        ALTER TABLE ai_assistant.conversation_history 
        ADD deleted boolean default false;
        """
    ))


def downgrade() -> None:
    op.execute(sa.DDL(
        """
        ALTER TABLE ai_assistant.conversation_history 
        DROP COLUMN deleted;
        """
    ))
