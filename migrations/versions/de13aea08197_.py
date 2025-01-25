"""empty message

Revision ID: de13aea08197
Revises: dd4657fe1324
Create Date: 2024-08-04 12:57:11.381837

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de13aea08197'
down_revision = 'dd4657fe1324'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('car_image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('car_id', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.String(length=200), nullable=False),
    sa.ForeignKeyConstraint(['car_id'], ['car.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('car_image')
    # ### end Alembic commands ###
