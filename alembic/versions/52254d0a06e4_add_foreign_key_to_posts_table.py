"""add foreign-key to posts table

Revision ID: 52254d0a06e4
Revises: ad2d347a2a55
Create Date: 2023-06-10 09:32:23.865131

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52254d0a06e4'
down_revision = 'ad2d347a2a55'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users',
                          local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
