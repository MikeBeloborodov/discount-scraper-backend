"""website cathegory to category

Revision ID: aa8c0d10cb90
Revises: 7f64f91e1b43
Create Date: 2022-06-07 12:47:04.888127

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa8c0d10cb90'
down_revision = '7f64f91e1b43'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('websites', 'cathegory', new_column_name='category')
    pass


def downgrade():
    op.alter_column('websites', 'category', new_column_name='cathegory')
    pass
