from flask import Blueprint, url_for, redirect
from MongoData import MongoInfo

delete = Blueprint('delete', __name__)


@delete.route('/delete/<bookname>')
def BookDelete(bookname):
    MongoInfo().remove({'name': bookname})
    MongoInfo().close()
    return redirect(url_for('book_list.xiuzhen'))  # url_for视图函数的反转，视图.函数名，book_list为蓝图注册的视图，xiuzhen为蓝图中的函数名
