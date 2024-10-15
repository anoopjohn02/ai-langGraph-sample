"""create schema

Revision ID: db24ffcf3023
Revises: 
Create Date: 2024-09-06 11:30:30.624786

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'db24ffcf3023'
down_revision: Union[str, None] = None #'d701eef05c35'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(sa.DDL(
        """
        create schema if not exists ai_assistant;
        """
    ))


def downgrade() -> None:
    pass
