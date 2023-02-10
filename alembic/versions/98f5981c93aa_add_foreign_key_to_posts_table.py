"""add foreign-key to posts table

Revision ID: 98f5981c93aa
Revises: d9203a327ae3
Create Date: 2023-02-06 15:57:48.668515

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98f5981c93aa'
down_revision = 'd9203a327ae3'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users", local_cols=[
        'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
