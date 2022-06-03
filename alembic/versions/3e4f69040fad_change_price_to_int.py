"""change price to int

Revision ID: 3e4f69040fad
Revises: 0fdf6a86fed3
Create Date: 2022-06-04 01:18:04.127049

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e4f69040fad'
down_revision = '0fdf6a86fed3'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('promo', 'new_price', type_=sa.Integer(), postgresql_using='new_price::integer')
    op.alter_column('promo', 'old_price', type_=sa.Integer(), postgresql_using='old_price::integer')
    pass


def downgrade():
    op.alter_column('promo', 'new_price', type_=sa.String(), postgresql_using='new_price::varchar')
    op.alter_column('promo', 'old_price', type_=sa.String(), postgresql_using='old_price::varchar')
    pass
