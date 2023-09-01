"""create info CML

Revision ID: 06a2546baa73
Revises: fa1ee9471440
Create Date: 2023-08-29 19:55:05.339347

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '06a2546baa73'
down_revision: Union[str, None] = 'fa1ee9471440'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'cml',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('cml_number', sa.Float),
        sa.Column('cml_description', sa.String(255)),
        sa.Column('actual_outside_diameter', sa.Float),
        sa.Column('design_thickness', sa.Float),
        sa.Column('structural_thickness', sa.Float),
        sa.Column('required_thickness', sa.Float),
        sa.Column('info_id', sa.Integer),
        sa.ForeignKeyConstraint(
            ["info_id"],
            ["info.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )

def downgrade():
    op.drop_table('cml')