""" This are the handlers that respond to the web browsers"""

from functools import wraps
from flask import render_template, request, url_for, session, redirect, flash
from werkzeug.security import generate_password_hash
from app import app
from app.forms import RegisterForm, LoginForm, TextForm
from app.models.user import User
from app.models.data import Data


@app.route('/')
@app.route('/index/')
def index():
    """renders the homepage of the app"""
    page_title = "Home"
    return render_template('index.html', title=page_title)


@app.route('/register/', methods=['GET', 'POST'])
def register_user():
    """ The registration method"""
    page_title = "Register"
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        email = form.email.data
        password = generate_password_hash(form.password.data)

        if User.register(username, email, password) is True:
            user = User.current_user(email)
            session['logged_in'] = True
            session['username'] = username
            session['email'] = email
            session['password'] = password
            session['id'] = user['_id']
            flash('You have been registered!  {} '.format(username), 'success')
            print(session['id'])
            print(Data.users)
            return redirect(url_for('dashboard'))
        else:
            flash('Email exists!!! You can login instead!', 'error')
            return redirect(url_for('login_user'))
    return render_template('register.html',
                           form=form,
                           title=page_title)


@app.route('/login/', methods=['GET', 'POST'])
def login_user():
    """ The user login method"""
    page_title = "Login"
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data

        if User.user_exists(email) is True:
            if User.user_login_verify(email, password) is True:
                user = User.current_user(email)
                session['logged_in'] = True
                session['username'] = user['username']
                session['email'] = email
                session['password'] = user['password']
                session['id'] = user['_id']
                flash('You have successfully logged in!!', 'success')
                print(session['id'])
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid Login!! Password or Email incorrect', 'error')
                return redirect(url_for('login_user'))
        else:
            flash("Email do not exist!!  first register")
            return redirect(url_for('register_user'))
    return render_template('login.html',
                           form=form,
                           title=page_title)

def user_in_session(func):
    """function is decorated to verify user is in session
     before accessing various pages"""
    @wraps(func)
    def wrap(*arg, **kwargs):
        """the wrapper function"""
        if 'logged_in' in session:
            return func(*arg, **kwargs)
        else:
            flash('No Access, Please login first', 'danger')
            return redirect(url_for('login_user'))
    return wrap


  
@app.route('/logout/')
@user_in_session
def logout():
    """Method logs out user"""
    session.clear()
    flash('You have successfully logged out')
    return redirect(url_for('login_user'))


@app.route('/create_bucketlist/', methods=['GET', 'POST'])
@user_in_session
def create_bucketlist():
    """creates a bucketlist"""
    page_title = "Add"
    form = TextForm(request.form)
    user = User(session['username'],
                session['email'],
                session['password'],
                session['id'])
    if request.method == 'POST' and form.validate():
        title = form.title.data
        intro = form.body.data
        user.create_bucketlist(title, intro)
        flash(' You have created a bucketlist', 'success')
        return redirect(url_for('dashboard'))
    return render_template('create.html',
                           form=form,
                           title=page_title)

@app.route('/create_item/<string:_id>/', methods=['GET', 'POST'])
@user_in_session
def create_item(_id):
    """creates an item"""
    page_title = "Add"
    form = TextForm(request.form)
    if request.method == 'POST' and form.validate():
        item_name = form.title.data
        description = form.body.data
        User.create_item(_id, item_name, description)
        flash(' You have created a bucketlist item', 'success')
        return redirect(url_for('bucketlist_items', _id=_id))
    return render_template('add_item.html',
                           form=form,
                           title=page_title)

@app.route('/dashboard/')
@app.route('/bucketlists/')
@user_in_session
def dashboard():
    """method for displaying users bucketlists"""
    page_title = "Dashboard"
    bucketlists = Data.get_the_data(session['id'], Data.bucketlists)
    notify = 'You have no bucketlists yet'
    return render_template('dashboard.html',
                           bucketlists=bucketlists,
                           notify=notify,
                           username=session['username'],
                           title=page_title)


@app.route('/items/<string:_id>/')
@app.route('/items/')
@user_in_session
def bucketlist_items(_id):
    """method used for displaying a bucketlists items"""
    page_title = "Items"
    bucketlist_ = Data.get_the_data(_id, Data.bucketlists)
    items = Data.get_the_data(_id, Data.items)
    notify = 'You have no items in this bucketlist yet'
    return render_template('items.html',
                           items=items,
                           notify=notify,
                           bucketlist_=bucketlist_,
                           title=page_title)


@app.route('/edit_bucketlist/<string:_id>/', methods=['GET', 'POST'])
@user_in_session
def edit_bucketlist(_id):
    """method lets the user  edit existing buckelists"""
    page_title = "Edit"
    index_ = Data.get_index(_id, Data.bucketlists)
    form = TextForm(request.form)
    form.title.data = Data.bucketlists[index_]['title']
    form.body.data = Data.bucketlists[index_]['intro']

    if request.method == 'POST' and form.validate():
        title = request.form['title']
        intro = request.form['body']
        Data.bucketlists[index_]['title'] = title
        Data.bucketlists[index_]['intro'] = intro
        flash('Your Bucketlist has been updated', 'success')
        return redirect(url_for('dashboard'))
    return render_template('create.html', form=form, title=page_title)


@app.route('/edit_bucketlist_item/<string:_id>/', methods=['GET', 'POST'])
@user_in_session
def edit_bucketlist_item(_id):
    """method lets the user  edit existing buckelists"""
    page_title = "Edit"
    index_ = Data.get_index(_id, Data.items)
    form = TextForm(request.form)

#    ### populating the form for user to edit ###

    form.title.data = Data.items[index_]['item_name']
    form.body.data = Data.items[index_]['description']

    if request.method == 'POST' and form.validate():
        title = request.form['title']
        intro = request.form['body']
        Data.items[index_]['item_name'] = title
        Data.items[index_]['description'] = intro
        flash('Your Item has been updated', 'success')
        return redirect(url_for('bucketlist_items',
                                _id=Data.items[index_]['owner_id']))
    return render_template('add_item.html', form=form, title=page_title)


@app.route('/delete/<string:_id>/')
def delete_bucketlist(_id):
    """ deletes a bucketlist and its items"""
    Data.delete_dictionary(_id, Data.bucketlists)
    all_items = Data.get_the_data(_id, Data.items)
    if all_items is not None:
        for item in all_items:
            if item['_id'] in Data.items:
                Data.delete_dictionary(item['_id'], Data.items)
    flash('Bucketlist deleted', 'Danger')
    return redirect(url_for('dashboard'))

@app.route('/delete_item/<string:_id>/')
def delete_item(_id):
    """ deletes a bucketlist and its items"""
    index_ = Data.get_index(_id, Data.items)
    b_id = Data.items[index_]['owner_id']
    Data.delete_dictionary(_id, Data.items)
    flash('Item deleted', 'Danger')
    return redirect(url_for('bucketlist_items', _id=b_id))
