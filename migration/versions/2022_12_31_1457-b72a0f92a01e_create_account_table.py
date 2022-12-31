"""create account table

Revision ID: b72a0f92a01e
Revises: 
Create Date: 2022-12-31 14:57:35.625284

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = 'b72a0f92a01e'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('uuid', UUID(as_uuid=True), unique=True, nullable=False),
        sa.Column('name', sa.String),
        sa.Column('email', sa.String, unique=True),
        sa.Column('password', sa.String)
    )


def downgrade() -> None:
    op.drop_table('users')
