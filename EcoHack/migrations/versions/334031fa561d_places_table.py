"""places table

Revision ID: 334031fa561d
Revises: d3ac4635e5e0
Create Date: 2020-02-29 16:09:28.044419

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '334031fa561d'
down_revision = 'd3ac4635e5e0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('places',
    sa.Column('place_id', sa.Integer(), nullable=False),
    sa.Column('building_id', sa.Integer(), nullable=True),
    sa.Column('floor', sa.Integer(), nullable=True),
    sa.Column('otdel', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['building_id'], ['buildings.building_id'], ),
    sa.PrimaryKeyConstraint('place_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('places')
    # ### end Alembic commands ###
