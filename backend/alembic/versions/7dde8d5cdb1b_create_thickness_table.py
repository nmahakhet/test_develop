"""create thickness table

Revision ID: 7dde8d5cdb1b
Revises: 157d67663d92
Create Date: 2023-08-29 22:19:15.938827

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7dde8d5cdb1b'
down_revision: Union[str, None] = '157d67663d92'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'thickness',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('inspection_date', sa.Date),
        sa.Column('actual_thickness', sa.Float),
        sa.Column('test_point_id', sa.Integer),
        sa.ForeignKeyConstraint(
            ["test_point_id"],
            ["test_point.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table('thickness')
