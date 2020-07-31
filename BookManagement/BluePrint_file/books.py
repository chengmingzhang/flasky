from flask import Blueprint, render_template, session, redirect
from MongoData import MongoInfo

book_list = Blueprint('book_list', __name__)


@book_list.route('/xiuzhen')
def xiuzhen():
    if session.get('name') == 'jack':  # 设置需要登录才能访问
        book20 = MongoInfo().find()
        MongoInfo().close()
        return render_template('books.html', book20=book20)
    return redirect('/login')
