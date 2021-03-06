"""empty message

Revision ID: a7bc6eced4e2
Revises: 2d0ed130c7bb
Create Date: 2018-12-01 12:41:40.748854

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a7bc6eced4e2'
down_revision = '2d0ed130c7bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog_post', sa.Column('teaser', sa.String(length=512), nullable=True))
    op.drop_column('blog_post', 'path')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog_post', sa.Column('path', mysql.VARCHAR(length=512), nullable=True))
    op.drop_column('blog_post', 'teaser')
    # ### end Alembic commands ###
