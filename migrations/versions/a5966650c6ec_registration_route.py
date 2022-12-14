"""registration route

Revision ID: a5966650c6ec
Revises: 2ebb78e9a3ea
Create Date: 2022-11-10 14:57:11.626814

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5966650c6ec'
down_revision = '2ebb78e9a3ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.String(length=255), nullable=False))
    op.add_column('users', sa.Column('admin', sa.Boolean(), nullable=False))
    op.add_column('users', sa.Column('active', sa.Boolean(), nullable=False))
    op.add_column('users', sa.Column('verified', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'verified')
    op.drop_column('users', 'active')
    op.drop_column('users', 'admin')
    op.drop_column('users', 'password')
    # ### end Alembic commands ###
