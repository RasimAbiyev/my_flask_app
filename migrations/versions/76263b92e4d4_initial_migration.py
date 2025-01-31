"""Initial migration.

Revision ID: 76263b92e4d4
Revises: 
Create Date: 2024-08-22 11:01:17.414532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76263b92e4d4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movie',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('year', sa.String(length=10), nullable=True),
    sa.Column('rated', sa.String(length=10), nullable=True),
    sa.Column('released', sa.String(length=20), nullable=True),
    sa.Column('runtime', sa.String(length=50), nullable=True),
    sa.Column('genre', sa.String(length=255), nullable=True),
    sa.Column('director', sa.String(length=255), nullable=True),
    sa.Column('writer', sa.String(length=255), nullable=True),
    sa.Column('actors', sa.Text(), nullable=True),
    sa.Column('plot', sa.Text(), nullable=True),
    sa.Column('language', sa.String(length=255), nullable=True),
    sa.Column('country', sa.String(length=100), nullable=True),
    sa.Column('awards', sa.String(length=255), nullable=True),
    sa.Column('poster', sa.Text(), nullable=True),
    sa.Column('metascore', sa.String(length=10), nullable=True),
    sa.Column('imdb_rating', sa.String(length=10), nullable=True),
    sa.Column('imdb_votes', sa.String(length=20), nullable=True),
    sa.Column('imdb_id', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movie')
    # ### end Alembic commands ###
