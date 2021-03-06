"""empty message

Revision ID: 1f758f99da0e
Revises: 
Create Date: 2020-11-26 11:55:30.187763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f758f99da0e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=60), nullable=True),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.Column('volume_type', sa.String(length=10), nullable=True),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='w3_db'
    )
    op.create_index(op.f('ix_w3_db_Products_description'), 'Products', ['description'], unique=True, schema='w3_db')
    op.create_table('Sales',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=60), nullable=True),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='w3_db'
    )
    op.create_table('Users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=60), nullable=True),
    sa.Column('first_name', sa.String(length=60), nullable=True),
    sa.Column('last_name', sa.String(length=60), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='w3_db'
    )
    op.create_index(op.f('ix_w3_db_Users_first_name'), 'Users', ['first_name'], unique=False, schema='w3_db')
    op.create_index(op.f('ix_w3_db_Users_last_name'), 'Users', ['last_name'], unique=False, schema='w3_db')
    op.create_index(op.f('ix_w3_db_Users_username'), 'Users', ['username'], unique=True, schema='w3_db')
    op.create_table('products',
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('sale_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['w3_db.Products.id'], ),
    sa.ForeignKeyConstraint(['sale_id'], ['w3_db.Sales.id'], ),
    sa.PrimaryKeyConstraint('product_id', 'sale_id')
    )
    op.create_table('Sellers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=60), nullable=True),
    sa.Column('first_name', sa.String(length=60), nullable=True),
    sa.Column('last_name', sa.String(length=60), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('sale_id', sa.Integer(), nullable=True),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['sale_id'], ['w3_db.Sales.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='w3_db'
    )
    op.create_index(op.f('ix_w3_db_Sellers_first_name'), 'Sellers', ['first_name'], unique=False, schema='w3_db')
    op.create_index(op.f('ix_w3_db_Sellers_last_name'), 'Sellers', ['last_name'], unique=False, schema='w3_db')
    op.create_index(op.f('ix_w3_db_Sellers_username'), 'Sellers', ['username'], unique=True, schema='w3_db')
    op.create_table('Suppliers',
    sa.Column('cnpj', sa.String(length=14), nullable=False),
    sa.Column('nick', sa.String(length=60), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['w3_db.Products.id'], ),
    sa.PrimaryKeyConstraint('cnpj'),
    schema='w3_db'
    )
    op.create_index(op.f('ix_w3_db_Suppliers_nick'), 'Suppliers', ['nick'], unique=True, schema='w3_db')
    op.create_index(op.f('ix_w3_db_Suppliers_phone'), 'Suppliers', ['phone'], unique=True, schema='w3_db')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_w3_db_Suppliers_phone'), table_name='Suppliers', schema='w3_db')
    op.drop_index(op.f('ix_w3_db_Suppliers_nick'), table_name='Suppliers', schema='w3_db')
    op.drop_table('Suppliers', schema='w3_db')
    op.drop_index(op.f('ix_w3_db_Sellers_username'), table_name='Sellers', schema='w3_db')
    op.drop_index(op.f('ix_w3_db_Sellers_last_name'), table_name='Sellers', schema='w3_db')
    op.drop_index(op.f('ix_w3_db_Sellers_first_name'), table_name='Sellers', schema='w3_db')
    op.drop_table('Sellers', schema='w3_db')
    op.drop_table('products')
    op.drop_index(op.f('ix_w3_db_Users_username'), table_name='Users', schema='w3_db')
    op.drop_index(op.f('ix_w3_db_Users_last_name'), table_name='Users', schema='w3_db')
    op.drop_index(op.f('ix_w3_db_Users_first_name'), table_name='Users', schema='w3_db')
    op.drop_table('Users', schema='w3_db')
    op.drop_table('Sales', schema='w3_db')
    op.drop_index(op.f('ix_w3_db_Products_description'), table_name='Products', schema='w3_db')
    op.drop_table('Products', schema='w3_db')
    # ### end Alembic commands ###
