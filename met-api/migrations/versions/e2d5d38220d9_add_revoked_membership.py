""" Add revoked_date and revoked status for membership

Revision ID: e2d5d38220d9
Revises: db737a0db061
Create Date: 2023-08-09 07:21:47.043458

"""
from datetime import datetime
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'e2d5d38220d9'
down_revision = 'db737a0db061'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('membership', sa.Column('revoked_date', sa.DateTime(), nullable=True))

    membership_status_codes = sa.table(
        'membership_status_codes',
        sa.Column('id', sa.Integer),
        sa.Column('status_name', sa.String),
        sa.Column('description', sa.String),
        sa.Column('created_date', sa.DateTime),
        sa.Column('updated_date', sa.DateTime)
    )
    op.execute(
        membership_status_codes.insert().values(
            id=3,
            status_name='REVOKED',
            description='Revoked Membership',
            created_date=datetime.utcnow(),
            updated_date=datetime.utcnow()
        )
    )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('membership', 'revoked_date')
    # ### end Alembic commands ###