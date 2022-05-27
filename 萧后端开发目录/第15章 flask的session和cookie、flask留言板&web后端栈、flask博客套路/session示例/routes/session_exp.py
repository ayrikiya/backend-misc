from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
    session,
)


main = Blueprint('session', __name__)

'''
1. 拆分有哪些页面， view 完成
2. 组织那些数据，把数据的操作实现 完成
3. 逻辑。
    3.1 没有登陆的时候，直接到登陆。没有登陆的情况下，session里面什么都没有
    3.2 登陆了以后，我们要展现出user_name页面
    3.3 当我退出了，我回到开始的页面，继续登陆
4. 开始实现代码，部分对，部分todo
5. 剩下的部分一点点补全
6. 美化页面
'''

@main.route('/')
def index():
    username = session.get("user_name", None)
    if username is None:
        return render_template("login.html")
    else:
        return render_template('session_index.html', username=username)

# @main.route('/')
# def index():
#     # username = session["user_name"]
#     username = session.get("user_name", None)
#     if username is None:
#         return render_template("session_index2.html")
#     else:
#         return render_template("session_index.html")


@main.route("/login", methods=['POST'])
def login():
    user_name = request.form.get("user_name", "")
    session["user_name"] = user_name
    return redirect(url_for(".index"))


@main.route("/logout", methods=['get'])
def log_out():
    session.pop("user_name")
    return redirect(url_for(".index"))