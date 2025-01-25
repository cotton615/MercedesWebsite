"""empty message

Revision ID: 5cb2447c9433
Revises: 90a0ae124323
Create Date: 2024-07-19 22:03:45.949739

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5cb2447c9433'
down_revision = '90a0ae124323'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_car')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('_alembic_tmp_car',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('model', sa.VARCHAR(length=50), nullable=False),
    sa.Column('img', sa.VARCHAR(length=200), nullable=False),
    sa.Column('carcass', sa.VARCHAR(length=20), nullable=False),
    sa.Column('transmission', sa.VARCHAR(length=20), nullable=False),
    sa.Column('volume', sa.FLOAT(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
