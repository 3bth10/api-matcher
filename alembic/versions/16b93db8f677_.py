"""empty message

Revision ID: 16b93db8f677
Revises: e3b8f3e96da1
Create Date: 2026-06-07 23:51:12.548492

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '16b93db8f677'
down_revision: Union[str, Sequence[str], None] = 'e3b8f3e96da1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
