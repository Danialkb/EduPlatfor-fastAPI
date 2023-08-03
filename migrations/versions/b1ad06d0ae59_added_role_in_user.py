"""added role in user

Revision ID: b1ad06d0ae59
Revises: f9a6e42963e2
Create Date: 2023-08-02 16:58:50.570982

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1ad06d0ae59'
down_revision = 'f9a6e42963e2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('role', sa.Enum('TUTOR', 'STUDENT', name='roleenum'), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'role')
    # ### end Alembic commands ###