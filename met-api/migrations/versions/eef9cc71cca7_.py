"""empty message

Revision ID: eef9cc71cca7
Revises: 326419c08f59
Create Date: 2022-05-26 09:03:34.300400

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'eef9cc71cca7'
down_revision = '326419c08f59'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('engagement', sa.Column('rich_description', postgresql.JSON(astext_type=sa.Text()), nullable=False))
    op.alter_column('engagement', 'description',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('engagement', 'description',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.drop_column('engagement', 'rich_description')
    # ### end Alembic commands ###
