"""init

Revision ID: a5f50af8d088
Revises: 
Create Date: 2025-04-17 14:04:45.605879

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a5f50af8d088'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'table',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('seats', sa.Integer),
        sa.Column('location', sa.String(100))
    )
    op.create_table(
        'reservation',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('table_id', sa.Integer, sa.ForeignKey('table.id'), nullable=False),
        sa.Column('customer_name', sa.String(100), nullable=False),
        sa.Column('reservation_time', sa.DateTime, nullable=False)
    )


def downgrade() -> None:
    op.drop_table('reservation')
    op.drop_table('table')
