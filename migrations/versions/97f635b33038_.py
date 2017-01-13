"""empty message

Revision ID: 97f635b33038
Revises: 7e5dddbb0d91
Create Date: 2017-01-12 22:45:46.673304

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97f635b33038'
down_revision = '7e5dddbb0d91'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'song', 'band', ['band_id'], ['band_id'])
    op.create_foreign_key(None, 'version', 'song', ['song_id'], ['song_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'version', type_='foreignkey')
    op.drop_constraint(None, 'song', type_='foreignkey')
    # ### end Alembic commands ###