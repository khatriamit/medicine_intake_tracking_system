"""create doctor info table

Revision ID: 40e419e5fe82
Revises: 726078c4fbe8
Create Date: 2021-11-23 14:15:08.258604

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '40e419e5fe82'
down_revision = '726078c4fbe8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "doctor_info",
        sa.Column("id", postgresql.UUID(as_uuid=False), primary_key=True),
        sa.Column("name", sa.String(55), nullable=False),
        sa.Column("phone", sa.String(55), nullable=False),
        sa.Column("address", sa.String(55), nullable=False),
    )


def downgrade():
    pass
