"""ingredients

Revision ID: 0621998e91a6
Revises: 7d94bac2b236
Create Date: 2022-06-04 12:11:59.849837

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0621998e91a6'
down_revision = '7d94bac2b236'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('promo', sa.Column('ingredients', sa.String(), nullable=True))
    pass


def downgrade():
    op.drop_column('promo', 'ingredients')
    pass
