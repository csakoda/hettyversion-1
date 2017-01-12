"""empty message

Revision ID: 7e5dddbb0d91
Revises: 127536b52f2d
Create Date: 2017-01-12 17:27:30.077290

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7e5dddbb0d91'
down_revision = '127536b52f2d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('band', 'slug')
    op.drop_column('song', 'slug')
    op.drop_column('version', 'slug')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('version', sa.Column('slug', mysql.VARCHAR(length=128), nullable=True))
    op.add_column('song', sa.Column('slug', mysql.VARCHAR(length=128), nullable=True))
    op.add_column('band', sa.Column('slug', mysql.VARCHAR(length=128), nullable=True))
    # ### end Alembic commands ###