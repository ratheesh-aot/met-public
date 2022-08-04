"""empty message

Revision ID: 8ca063aafc01
Revises: 6d3c33a79c5e
Create Date: 2022-07-28 15:13:35.368696

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime


# revision identifiers, used by Alembic.
revision = '8ca063aafc01'
down_revision = '6d3c33a79c5e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    comment_status_table = op.create_table('comment_status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status_name', sa.String(length=50), unique= True, nullable=False),
    sa.Column('description', sa.String(length=50), nullable=True),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('updated_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('submission_date', sa.DateTime(), nullable=True),
    sa.Column('reviewed_by', sa.String(length=50), nullable=True),
    sa.Column('review_date', sa.DateTime(), nullable=True),
    sa.Column('status_id', sa.Integer(), nullable=True),
    sa.Column('survey_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['status_id'], ['comment_status.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['survey_id'], ['survey.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.bulk_insert(comment_status_table, [
        {'id': 1, 'status_name': 'Pending', 'description': 'Comment is pending review', 'created_date': datetime.utcnow(), 'updated_date': datetime.utcnow()},
        {'id': 2, 'status_name': 'Accepted', 'description': 'Comment is accepted for public view', 'created_date': datetime.utcnow(), 'updated_date': datetime.utcnow()},
        {'id': 3, 'status_name': 'Rejected', 'description': 'Comment is rejected and not shown', 'created_date': datetime.utcnow(), 'updated_date': datetime.utcnow()},
    ])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment')
    op.drop_table('comment_status')
    # ### end Alembic commands ###