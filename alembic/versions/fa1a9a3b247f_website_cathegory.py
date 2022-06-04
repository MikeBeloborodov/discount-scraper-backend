"""website cathegory

Revision ID: fa1a9a3b247f
Revises: 3e4f69040fad
Create Date: 2022-06-04 02:51:34.117220

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa1a9a3b247f'
down_revision = '3e4f69040fad'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_constraint(constraint_name='websites_link_key', table_name='websites', type_='unique')
    op.drop_constraint(constraint_name='websites_title_key', table_name='websites', type_='unique')
    op.drop_constraint(constraint_name='websites_phone_number_key', table_name='websites', type_='unique')
    pass


def downgrade():
    op.create_unique_constraint('link', 'websites', type_='unique')
    op.create_unique_constraint('title', 'websites', type_='unique')
    op.create_unique_constraint('phone_number', 'websites', type_='unique')
    pass
