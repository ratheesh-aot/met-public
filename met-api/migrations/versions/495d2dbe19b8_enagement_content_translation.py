"""Enagement Content Translation

Revision ID: 495d2dbe19b8
Revises: e4d15a1af865
Create Date: 2024-04-10 14:20:23.777834

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '495d2dbe19b8'
down_revision = 'e4d15a1af865'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('engagement_content_translation',
    sa.Column('created_date', sa.DateTime(), nullable=False),
    sa.Column('updated_date', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('language_id', sa.Integer(), nullable=False),
    sa.Column('engagement_content_id', sa.Integer(), nullable=False),
    sa.Column('content_title', sa.String(length=50), nullable=False),
    sa.Column('custom_text_content', sa.Text(), nullable=True),
    sa.Column('custom_json_content', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('created_by', sa.String(length=50), nullable=True),
    sa.Column('updated_by', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['engagement_content_id'], ['engagement_content.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['language_id'], ['language.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('engagement_content_id', 'language_id', name='_engagement_content_language_uc')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('engagement_content_translation')
    # ### end Alembic commands ###
