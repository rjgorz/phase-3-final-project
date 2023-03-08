"""updated content and viewer tabels

Revision ID: 8e35eaa92f24
Revises: 8d660fce0f8d
Create Date: 2023-03-08 11:08:17.535745

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e35eaa92f24'
down_revision = '8d660fce0f8d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('content',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('orig_title', sa.String(), nullable=True),
    sa.Column('orig_type', sa.String(), nullable=True),
    sa.Column('orig_release', sa.DateTime(), nullable=True),
    sa.Column('adapt_title', sa.String(), nullable=True),
    sa.Column('adapt_type', sa.String(), nullable=True),
    sa.Column('adapt_release', sa.DateTime(), nullable=True),
    sa.Column('genre', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('viewers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('viewer_id', sa.Integer(), nullable=True),
    sa.Column('content_id', sa.Integer(), nullable=True),
    sa.Column('orig_rating', sa.Integer(), nullable=True),
    sa.Column('adapt_rating', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['content_id'], ['content.id'], ),
    sa.ForeignKeyConstraint(['viewer_id'], ['viewers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    op.drop_table('viewers')
    op.drop_table('content')
    # ### end Alembic commands ###
