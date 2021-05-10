"""empty message

Revision ID: 8674bcb34006
Revises: 1e5532fa8540
Create Date: 2021-05-10 12:25:55.686541

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8674bcb34006'
down_revision = '1e5532fa8540'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('deliveries', 'created_at')
    op.add_column('orders', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.drop_column('test_deliveries', 'created_at')
    op.add_column('test_orders', sa.Column('created_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('test_orders', 'created_at')
    op.add_column('test_deliveries', sa.Column('created_at', mysql.DATETIME(), nullable=True))
    op.drop_column('orders', 'created_at')
    op.add_column('deliveries', sa.Column('created_at', mysql.DATETIME(), nullable=True))
    # ### end Alembic commands ###
