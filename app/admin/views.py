from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required
from wtforms import ValidationError

from . import admin
from .forms import FindSellerForm, AddSellerForm, EditSellerForm
from .. import db
from ..models import Seller

def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_admin:
        abort(403)

def define_seller(form):
    
    return Seller(email=form.email.data,
                        username=form.username.data,
                        first_name=form.first_name.data,
                        last_name=form.last_name.data,
                        is_admin=form.is_admin.data,
                        password=form.password.data)

def verify_seller(form):
    if(form.email.data != ''):
        return Seller.query.filter_by(email=form.email.data).first()
    if(form.username.data != ''):
        return Seller.query.filter_by(username=form.username.data).first()
    
    form.email.errors.append('Email não encontrado.')
    return form.username.errors.append('Username não encontrado.')

@admin.route('/home', methods=['GET','POST'])
@login_required
def home():
    check_admin()
    
    return render_template('admin/home.html', title="Home")

@admin.route('/sellers', methods=['GET', 'POST'])
@login_required
def list_sellers():
    check_admin()  
    
    sellers = Seller.query.all()
    
    return render_template('admin/sellers.html', sellers=sellers, title='Vendedores')


@admin.route('/sellers/new', methods=['GET', 'POST'])
@login_required
def add_seller():
    check_admin()
    
    add_seller = True
    
    form = AddSellerForm()
    if form.validate_on_submit():
        seller = define_seller(form)
        
        try:
            db.session.add(seller)
            db.session.commit()
            flash('Vendedor cadastrado com sucesso!')
        except:
            flash('Error: Vendedor ja existe!')
        
        return redirect(url_for('admin.list_sellers'))
    
    return render_template('admin/seller.html', action="Add",
                           add_seller=add_seller, form=form,
                           title="Registrar vendedor")

@admin.route('/sellers/update/<int:id>', methods=['GET','POST'])
@login_required
def edit_seller(id):
    check_admin()
    
    add_seller = False
    
    seller = Seller.query.get_or_404(id)
    form = EditSellerForm(obj=seller)
    if form.validate_on_submit():
        seller.email = form.email.data
        seller.username = form.username.data
        seller.first_name = form.first_name.data
        seller.last_name = form.last_name.data
        seller.is_admin = form.is_admin.data
        db.session.commit()
        flash('You have successfully edited the seller.')
        
        return redirect(url_for('admin.list_sellers'))
    
    form.email.data = seller.email
    form.username.data = seller.username
    form.first_name.data = seller.first_name
    form.last_name.data = seller.last_name
    form.is_admin.data = seller.is_admin
    return render_template('admin/seller.html', action="Edit", add_seller=add_seller, form=form, seller=seller, title="Edit Seller")


@admin.route('/sellers/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_seller(id):
    check_admin()

    seller = Seller.query.get_or_404(id)
    db.session.delete(seller)
    db.session.commit()
    flash('Vendedor deletado com sucesso!')

    # redirect to the departments page
    return redirect(url_for('admin.list_sellers'))

@admin.route('/sellers/find', methods=['GET', 'POST'])
@login_required
def find_seller():
    
    check_admin()
    
    form = FindSellerForm()
    if form.validate_on_submit():

        user = verify_seller(form)
        if user is not None:
            return render_template('admin/seller.html', seller=user, title=user.username)

        else:
            return render_template('admin/sellerForm.html', form=form, title='Login')


    return render_template('admin/sellerForm.html', form=form, title='Login')
