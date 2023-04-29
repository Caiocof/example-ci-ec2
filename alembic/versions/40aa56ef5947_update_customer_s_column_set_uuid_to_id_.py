"""update customer's column, set uuid to id because sqlalchemy compatibility

Revision ID: 40aa56ef5947
Revises: 59218c393467
Create Date: 2022-06-08 18:54:54.126575

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '40aa56ef5947'
down_revision = '59218c393467'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False))
    op.drop_index('ix_customer_uuid', table_name='customer')
    op.create_index(op.f('ix_customer_id'), 'customer', ['id'], unique=False)
    op.drop_column('customer', 'uuid')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('uuid', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_index(op.f('ix_customer_id'), table_name='customer')
    op.create_index('ix_customer_uuid', 'customer', ['uuid'], unique=False)
    op.drop_column('customer', 'id')
    # ### end Alembic commands ###