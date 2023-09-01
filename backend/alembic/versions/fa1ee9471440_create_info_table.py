"""create info table

Revision ID: fa1ee9471440
Revises: 
Create Date: 2023-08-29 19:46:50.487433

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fa1ee9471440'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'info',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('line_number', sa.String(255)),
        sa.Column('location', sa.String(255)),
        sa.Column('from_location', sa.String(255)),
        sa.Column('to_location', sa.String(255)),
        sa.Column('drawing_number', sa.String(255)),
        sa.Column('service', sa.String(255)),
        sa.Column('material', sa.String(255)),
        sa.Column('inservice_date', sa.Date),
        sa.Column('pipe_size', sa.Float),
        sa.Column('original_thickness', sa.Float),
        sa.Column('stress', sa.Float),
        sa.Column('joint_efficiency', sa.Float),
        sa.Column('ca', sa.Float),
        sa.Column('design_life', sa.Float),
        sa.Column('design_pressure', sa.Float),
        sa.Column('operating_pressure', sa.Float),
        sa.Column('design_temperature', sa.Float),
        sa.Column('operating_temperature', sa.Float)
    )


def downgrade() -> None:
    op.drop_table('info')
