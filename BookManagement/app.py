from flask import Flask, render_template, url_for, request
from flask_script import Manager
from BluePrint_file.book_login import login
from BluePrint_file.book_delete import delete
from BluePrint_file.books import book_list

app = Flask(__name__)
app.secret_key = 'book'
app.register_blueprint(login)
app.register_blueprint(delete)
app.register_blueprint(book_list)
manager = Manager(app=app)


@app.route('/')
def index():
    return '<h2>Hello，欢迎使用图书系统</h2>'


if __name__ == '__main__':
    manager.run()
