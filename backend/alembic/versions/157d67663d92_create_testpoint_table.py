"""create testpoint table

Revision ID: 157d67663d92
Revises: 06a2546baa73
Create Date: 2023-08-29 22:15:54.710766

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '157d67663d92'
down_revision: Union[str, None] = '06a2546baa73'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'test_point',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('tp_number', sa.Integer),
        sa.Column('tp_description', sa.Integer),
        sa.Column('note', sa.String(255)),
        sa.Column('cml_id', sa.Integer),
        sa.ForeignKeyConstraint(
            ["cml_id"],
            ["cml.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table('test_point')
