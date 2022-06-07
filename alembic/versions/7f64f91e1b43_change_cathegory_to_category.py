"""change cathegory to category

Revision ID: 7f64f91e1b43
Revises: 0621998e91a6
Create Date: 2022-06-07 12:31:50.880408

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f64f91e1b43'
down_revision = '0621998e91a6'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('promo', 'cathegory', new_column_name='category')
    pass


def downgrade():
    op.alter_column('promo', 'category', new_column_name='cathegory')
    pass
