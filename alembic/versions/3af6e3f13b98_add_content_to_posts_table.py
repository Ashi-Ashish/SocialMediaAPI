"""add content to posts table

Revision ID: 3af6e3f13b98
Revises: 4ef4a895f8c4
Create Date: 2023-06-10 09:15:00.003915

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3af6e3f13b98'
down_revision = '4ef4a895f8c4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
