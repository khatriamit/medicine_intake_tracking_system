"""create medical info table

Revision ID: 726078c4fbe8
Revises: 
Create Date: 2021-11-23 14:05:02.996162

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '726078c4fbe8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "medicine_info",
        sa.Column("id", postgresql.UUID(as_uuid=False), primary_key=True),
        sa.Column("name", sa.String(55), nullable=False),
        sa.Column("type", sa.String(55)),
        sa.Column("time", sa.String(55), nullable=False),
        sa.Column("start_date", sa.Date(), nullable=False),
        sa.Column("end_date", sa.Date(), nullable=False),
        sa.Column("quantity", sa.String(255), nullable=False),
        sa.Column("has_taken", sa.BOOLEAN), 
    )


def downgrade():
    pass
