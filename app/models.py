from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


products_sold = db.Table('products_sold',
                         db.Column('product_id', db.Integer, db.ForeignKey(
                             'w3_db.Products.id', ondelete='CASCADE'), primary_key=True),
                         db.Column('sale_id', db.Integer, db.ForeignKey(
                             'w3_db.Sales.id', ondelete='CASCADE'), primary_key=True)
                         )


class User(UserMixin, db.Model):
    """
    Create an User table
    """
    __bind_key__ = 'w3_db'
    __table_args__ = {'schema': 'w3_db'}

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)


class Seller(UserMixin, db.Model):
    """
    Create an Seller table
    """
    __bind_key__ = 'w3_db'
    __table_args__ = {'schema': 'w3_db'}

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'Sellers'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    sale_id = db.Column(db.Integer, db.ForeignKey(
        'w3_db.Sales.id', ondelete='CASCADE'))
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Seller: {}>'.format(self.username)


@login_manager.user_loader
def load_user(user_id):
    return Seller.query.get(int(user_id))


class Product(db.Model):
    """
    Create an Product table
    """
    __bind_key__ = 'w3_db'
    __table_args__ = {'schema': 'w3_db'}

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'Products'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(60), index=True, unique=True)
    value = db.Column(db.Integer)
    volume_type = db.Column(db.String(10))
    supplier = db.relationship(
        'Supplier', backref='product', lazy=True, passive_deletes=True)
    sales = db.relationship(
        "Sale",
        secondary=products_sold,
        back_populates="Products",
        cascade="all, delete",
    )
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __repr__(self):
        return '<Product: {}>'.format(self.description)


class Supplier(db.Model):
    """
    Create an Supplier table
    """
    __bind_key__ = 'w3_db'
    __table_args__ = {'schema': 'w3_db'}

    __tablename__ = 'Suppliers'

    cnpj = db.Column(db.String(14), primary_key=True)
    nick = db.Column(db.String(60), index=True, unique=True)
    phone = db.Column(db.String(20), index=True, unique=True)
    product_id = db.Column(db.Integer, db.ForeignKey(
        'w3_db.Products.id', ondelete='CASCADE'))
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __repr__(self):
        return '<Supplier: {}>'.format(self.nick)


class Sale(db.Model):
    """
    Create an Sale table
    """
    __bind_key__ = 'w3_db'
    __table_args__ = {'schema': 'w3_db'}

    __tablename__ = 'Sales'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(60))
    seller = db.relationship(
        'Seller', backref='sale', lazy=True, passive_deletes=True, cascade="all, delete")
    products = db.relationship('Product', secondary=products_sold, lazy='subquery',
                               backref=db.backref('Sales', lazy=True), cascade="all, delete", passive_deletes=True,)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __repr__(self):
        return '<Sale: {}>'.format(self.id)
