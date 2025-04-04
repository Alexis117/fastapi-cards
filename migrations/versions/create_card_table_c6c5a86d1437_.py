"""empty message

Revision ID: c6c5a86d1437
Revises: 
Create Date: 2025-04-03 16:43:22.623680

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import sqlite

# revision identifiers, used by Alembic.
revision = 'c6c5a86d1437'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('card',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('titulo', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('descripcion', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('img', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('tags', sqlite.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('card')
    # ### end Alembic commands ###
