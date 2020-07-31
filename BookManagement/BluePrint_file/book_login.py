from flask import Blueprint, render_template, request, session

login = Blueprint('login', __name__)


@login.route('/login', methods=['GET', 'POST'])
def BookLogin():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.form.get('_username') if request.form.get('_username') else None
        password = request.form.get('_password') if request.form.get('_password') else None
        if name == 'jack' and password == '123456':
            session['name'] = 'jack'
            return 'login success'
        return '用户名或密码错误'
