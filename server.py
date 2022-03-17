from flask import Flask, request, redirect, render_template
from model_user import User

app = Flask(__name__)
app.secret_key = "8d7198a6-2916-4de2-bde7-b871c53b6b31"

@app.route('/users')
def index():
    all_users = User.get_all()
    return render_template('read.html', all_users=all_users)

@app.route('/users/new')
def new():
    return render_template('create.html')

@app.route('/users/create', methods=['POST'])
def create():
    form_data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
    }
    User.create(form_data)
    return redirect('/users')
    


if __name__ == '__main__':
    app.run(debug=True)