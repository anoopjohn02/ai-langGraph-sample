"""iot devices

Revision ID: 625d98f95683
Revises: ed8383f5f1f1
Create Date: 2024-10-06 21:23:50.407469

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '625d98f95683'
down_revision: Union[str, None] = 'ed8383f5f1f1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(sa.DDL(
        """
        CREATE TABLE ai_assistant.devices (
            id uuid PRIMARY KEY,
            name varchar NULL,
            description varchar NULL,
            type varchar NULL,
            created_on timestamp NOT NULL,
            user_id uuid NOT NULL
        );
        """
    ))


def downgrade() -> None:
    op.execute(sa.DDL(
        """
        DROP TABLE ai_assistant.devices;
        """
    ))
