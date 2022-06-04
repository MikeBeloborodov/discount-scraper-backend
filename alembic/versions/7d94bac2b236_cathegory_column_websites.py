"""cathegory column websites

Revision ID: 7d94bac2b236
Revises: fa1a9a3b247f
Create Date: 2022-06-04 03:05:18.682246

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d94bac2b236'
down_revision = 'fa1a9a3b247f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('websites', sa.Column('cathegory', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('websites', 'cathegory')
    pass
