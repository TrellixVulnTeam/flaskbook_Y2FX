"""empty message

Revision ID: 0e53f70dc789
Revises: 
Create Date: 2019-07-13 08:35:33.286256

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e53f70dc789'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tbl_authors', sa.Column('email', sa.String(length=32), nullable=True))
    op.create_unique_constraint(None, 'tbl_authors', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tbl_authors', type_='unique')
    op.drop_column('tbl_authors', 'email')
    # ### end Alembic commands ###
