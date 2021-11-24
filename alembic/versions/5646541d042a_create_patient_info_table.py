"""create patient info table

Revision ID: 5646541d042a
Revises: 40e419e5fe82
Create Date: 2021-11-23 14:16:26.019925

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql



# revision identifiers, used by Alembic.
revision = '5646541d042a'
down_revision = '40e419e5fe82'
branch_labels = None
depends_on = None


def upgrade():
     op.create_table(
        "patient_info",
        sa.Column("id", postgresql.UUID(as_uuid=False), primary_key=True),
        sa.Column("name", sa.String(55), nullable=False),
        sa.Column("phone", sa.String(55), nullable=False),
        sa.Column("address", sa.String(55), nullable=False),
    )


def downgrade():
    pass
