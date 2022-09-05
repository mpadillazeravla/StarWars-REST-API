"""empty message

Revision ID: 8d83aa2caab5
Revises: 7701603f316f
Create Date: 2022-09-05 19:19:49.650963

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8d83aa2caab5'
down_revision = '7701603f316f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('id_character', sa.Integer(), nullable=True),
    sa.Column('id_planet', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_character'], ['characters.id'], ),
    sa.ForeignKeyConstraint(['id_planet'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('user', 'is_active')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False))
    op.drop_table('favorites')
    # ### end Alembic commands ###
