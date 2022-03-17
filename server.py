from flask import Flask, request, redirect, render_template
from model_user import User

app = Flask(__name__)
app.secret_key = "8d7198a6-2916-4de2-bde7-b871c53b6b31"

# DISPLAY: Displaying all users
@app.route('/users')
def read():
    all_users = User.get_all()
    return render_template('read.html', all_users=all_users)

# DISPLAY: Form for creating new user
@app.route('/users/new')
def new():
    return render_template('create.html')

# ACTION: Create new user
# Is it ok to use an f string in the redirect? I could see this being
# vulnerable to very indirect SQL injection via the read_user() route
@app.route('/users/create', methods=['POST'])
def create():
    form_data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
    }
    user_id = User.create(form_data)
    return redirect(f'/users/{str(user_id)}')

# DISPLAY: Show individual user
# could not get this to work trying to convert user_id to int directly in the
# route(), couldn't get it to work without creating that data dictionary to
# pass into the get_user() function to eventually be passed into the query_db
# function. I assume the mogrify from query_db needs a dictionary? How else
# can I do this?
# Syntax? Naming?
# Wtf is a decorator? What is actually happening with app.route()?
@app.route('/users/<user_id>')
def read_user(user_id):
    data = {
        'id': int(user_id)
    }
    this_user_instance = User.get_user(data)
    return render_template('user.html', user=this_user_instance)

# DISPLAY: Form for updating user
@app.route('/users/<user_id>/edit')
def edit(user_id):
    data = {
        'id': int(user_id)
    }
    this_user_instance = User.get_user(data)
    return render_template('edit.html', user=this_user_instance)

# ACTION: Update user. Redirect to read_user()
# Same thing here. f string?
@app.route('/users/<user_id>/update', methods=['POST'])
def update_user(user_id):
    data = {
        'id': int(user_id),
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.update_user(data)
    return redirect(f'/users/{user_id}')

# ACTION: Delete user. Redirect to show all users route
@app.route('/users/<user_id>/delete')
def delete_user(user_id):
    data = {
        'id': int(user_id)
    }
    User.delete_user(data)
    return redirect('/users')
    

if __name__ == '__main__':
    app.run(debug=True)