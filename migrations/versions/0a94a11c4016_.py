"""empty message

Revision ID: 0a94a11c4016
Revises: 
Create Date: 2018-10-18 14:25:53.112412

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a94a11c4016'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=60), nullable=True),
    sa.Column('desc', sa.Text(length=4294000000), nullable=True),
    sa.Column('author', sa.String(length=50), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('views', sa.Integer(), nullable=True),
    sa.Column('visibility', sa.String(length=8), server_default='public', nullable=True),
    sa.Column('sponsors', sa.String(length=500), nullable=True),
    sa.Column('locked', sa.Boolean(), server_default='0', nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_projects_author'), 'projects', ['author'], unique=False)
    op.create_index(op.f('ix_projects_date'), 'projects', ['date'], unique=False)
    op.create_index(op.f('ix_projects_title'), 'projects', ['title'], unique=True)
    op.create_index(op.f('ix_projects_views'), 'projects', ['views'], unique=False)
    op.create_table('proposals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=60), nullable=True),
    sa.Column('desc', sa.Text(length=4294000000), nullable=True),
    sa.Column('author', sa.String(length=50), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('views', sa.Integer(), nullable=True),
    sa.Column('sponsors', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_proposals_author'), 'proposals', ['author'], unique=False)
    op.create_index(op.f('ix_proposals_date'), 'proposals', ['date'], unique=False)
    op.create_index(op.f('ix_proposals_title'), 'proposals', ['title'], unique=True)
    op.create_index(op.f('ix_proposals_views'), 'proposals', ['views'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_proposals_views'), table_name='proposals')
    op.drop_index(op.f('ix_proposals_title'), table_name='proposals')
    op.drop_index(op.f('ix_proposals_date'), table_name='proposals')
    op.drop_index(op.f('ix_proposals_author'), table_name='proposals')
    op.drop_table('proposals')
    op.drop_index(op.f('ix_projects_views'), table_name='projects')
    op.drop_index(op.f('ix_projects_title'), table_name='projects')
    op.drop_index(op.f('ix_projects_date'), table_name='projects')
    op.drop_index(op.f('ix_projects_author'), table_name='projects')
    op.drop_table('projects')
    # ### end Alembic commands ###
