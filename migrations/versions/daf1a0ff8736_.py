"""empty message

Revision ID: daf1a0ff8736
Revises: e673186292bc
Create Date: 2020-01-14 16:55:07.361995

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'daf1a0ff8736'
down_revision = 'e673186292bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pizza') as batch_op:
        batch_op.create_unique_constraint('unique_component_commit', ['name', 'company_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('unique_component_commit', 'pizza', type_='unique')
    # ### end Alembic commands ###
