"""empty message

Revision ID: 0e9a23a6cbb4
Revises: cafd5f979022
Create Date: 2018-12-01 23:53:27.804359

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e9a23a6cbb4'
down_revision = 'cafd5f979022'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tag', sa.Column('tag_path', sa.String(length=500), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tag', 'tag_path')
    # ### end Alembic commands ###
