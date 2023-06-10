"""create post table

Revision ID: 4ef4a895f8c4
Revises: 
Create Date: 2023-06-07 13:47:17.572543

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ef4a895f8c4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False)) 
    pass


def downgrade():
    op.drop_table('posts')
    pass
