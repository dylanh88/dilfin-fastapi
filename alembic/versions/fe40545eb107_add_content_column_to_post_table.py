"""add content column to post table

Revision ID: fe40545eb107
Revises: 2dc9a7459c10
Create Date: 2023-02-06 15:39:27.009828

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe40545eb107'
down_revision = '2dc9a7459c10'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
