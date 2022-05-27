'''
0.web server app
1.web server framework
2.http server
3.tcp server

nginx : http server
gunicorn: http server
wsgi: 包装出来一个app

nginx gunicorn?
data -> nginx -> gunicorn -> wsgi -> app ?

1. 反向代理
    gunicorn 2000
    gunicorn 2002
    nginx 80
2. 负载均衡
    haproxy 去访问google.com
3. 静态文件托管
    send_by_directory 每次都send很不好
    配置了一个rule，保存在nginx的缓存，不会走到app这一层
4. 缓冲
    traffic busy
    缓冲负载
'''

'''
上传头像
1. form
2. post方法 对应一个路由 保存静态文件的功能
    1. 文件后缀要做过滤 img png gif
    2. 文件名也要小心
    /var/img
    ../../home/akirayu/.bash_rc -> xxxxxx
    ~/.bash_rc
    ~/.bash_profile
    pickle dump load
3. get方法，本地的静态文件转发给用户


发私信
数据结构
1. id
2. content
3. title
4. sender_id # 这个不应该是从表单里面拿的，hidden，伪造成任何人
5. receiver_id
6. read
'''