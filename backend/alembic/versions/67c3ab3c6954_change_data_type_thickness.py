"""change data type thickness

Revision ID: 67c3ab3c6954
Revises: 7dde8d5cdb1b
Create Date: 2023-09-01 23:32:20.487000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import text


# revision identifiers, used by Alembic.
revision: str = '67c3ab3c6954'
down_revision: Union[str, None] = '7dde8d5cdb1b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    conn = op.get_bind()
    conn.execute("ALTER TABLE thickness MODIFY COLUMN inspection_date DATE")


def downgrade() -> None:
    conn = op.get_bind()
    conn.execute("ALTER TABLE thickness MODIFY COLUMN inspection_date DATETIME")
