"""add last few columns to posts table

Revision ID: d3b558d8b1b5
Revises: 52254d0a06e4
Create Date: 2023-06-10 09:40:29.438641

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3b558d8b1b5'
down_revision = '52254d0a06e4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean, nullable=False, server_default='TRUE'))
    op.add_column("posts", sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
