"""Init

Revision ID: d121295f9114
Revises: 58cd14b3677e
Create Date: 2023-01-12 14:54:00.640374

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd121295f9114'
down_revision = '58cd14b3677e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students', sa.Column('name', sa.String(length=50), nullable=False))
    op.add_column('students', sa.Column('phone', sa.String(length=50), nullable=True))
    op.add_column('students', sa.Column('email', sa.String(length=150), nullable=True))
    op.drop_column('students', 'done')
    op.drop_column('students', 'description')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students', sa.Column('description', sa.VARCHAR(length=150), autoincrement=False, nullable=False))
    op.add_column('students', sa.Column('done', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('students', 'email')
    op.drop_column('students', 'phone')
    op.drop_column('students', 'name')
    # ### end Alembic commands ###
