"""empty message

Revision ID: df2170431f54
Revises: 1d43054f0676
Create Date: 2023-06-16 22:39:58.869663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df2170431f54'
down_revision = '1d43054f0676'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('muestra',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_name', sa.String(length=150), nullable=False),
    sa.Column('ubication', sa.String(length=120), nullable=False),
    sa.Column('ubication_image', sa.String(length=120), nullable=False),
    sa.Column('area', sa.String(length=80), nullable=False),
    sa.Column('specimen', sa.String(length=80), nullable=False),
    sa.Column('quality_specimen', sa.String(length=80), nullable=False),
    sa.Column('image_specimen', sa.String(length=80), nullable=False),
    sa.Column('aditional_coments', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('last_name', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('rut', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('rol', sa.String(length=20), nullable=False))
        batch_op.create_unique_constraint(None, ['rut'])
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('rol')
        batch_op.drop_column('rut')
        batch_op.drop_column('last_name')
        batch_op.drop_column('name')

    op.drop_table('muestra')
    # ### end Alembic commands ###
