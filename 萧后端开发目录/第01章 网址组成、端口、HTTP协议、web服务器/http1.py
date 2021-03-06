import socket


# 这个程序就是一个套路程序, 套路程序没必要思考为什么会是这样
# 记住套路, 能用, 就够了
# 运行这个程序后, 浏览器打开 localhost:2000 就能访问了
#
# 服务器的 host 为空字符串, 表示接受任意 ip 地址的连接
# post 是端口, 这里设置为 2000, 随便选的一个数字
host = ''          # 不同的系统定义不同的字符代表接受任意ip地址
port = 2000        # 定义的也是服务器端开放给外界的自身的端口

# s 是一个 socket 实例
s = socket.socket()
# s.bind 用于绑定
# 注意 bind 函数的参数是一个 tuple
s.bind((host, port))


# 用一个无限循环来处理请求
while True:
    # 套路, 先要 s.listen 开始监听
    # 注意 参数 5 的含义不必关心
    print('before listen')
    s.listen(5)
    # 当有客户端过来连接的时候, s.accept 函数就会返回 2 个值
    # 分别是 连接 和 客户端 ip 地址

    print('before accept')
    connection, address = s.accept()    # connection的type也是一个socket  address的type是一个tuple 内容是ip+端口
    print('after accept')

    # recv 可以接收客户端发送过来的数据
    # 参数是要接收的字节数
    # 返回值是一个 bytes 类型
    request = connection.recv(1024)

    '''这里只接受了1024字节 溢出怎么办 完整处理请求的数据是用一个循环
        buffer_size = 1024
        r = b''
        while True:
            request = connection.recv(buffer_size)
            r += request
            if len(request) < buffer_size:
                break
    '''

    # bytes 类型调用 decode('utf-8') 来转成一个字符串(str)
    print('ip and request, {}\n{}'.format(address, request.decode('utf-8')))

    # b'' 表示这是一个 bytes 对象
    response = b'HTTP/1.1 200 ok\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n<h1>Hello World!</h1>'
    # 用 sendall 发送给客户端
    connection.sendall(response)
    # 发送完毕后, 关闭本次连接
    connection.close()


