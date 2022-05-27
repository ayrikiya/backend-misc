var log = function() {
    console.log.apply(console, arguments)
}

var e = function(sel) {
    return document.querySelector(sel)
}

/*
 ajax 函数
*/
var ajax = function(method, path, data, responseCallback) {
    var r = new XMLHttpRequest()
    r.open(method, path, true)                               // 设置请求方法和请求地址
    r.setRequestHeader('Content-Type', 'application/json')  // 设置发送的数据的格式为 application/json 这个不是必须的
    r.onreadystatechange = function() {                      // 注册响应函数
        if(r.readyState === 4) {
            responseCallback(r.response)                     // r.response 存的就是服务器发过来的放在 HTTP BODY 中的数据
        }
    }
    data = JSON.stringify(data)                                // 把数据转换为 json 格式字符串
    r.send(data)                                               // 发送请求
}

// TODO API
// 获取所有 todo
var apiTodoAll = function(callback) {
    var path = '/api/todo/all'
    ajax('GET', path, '', callback)
}

// 增加一个 todo
var apiTodoAdd = function(form, callback) {
    var path = '/api/todo/add'
    ajax('POST', path, form, callback)
}

// 删除一个 todo
var apiTodoDelete = function(id, callback) {
    var path = '/api/todo/delete?id=' + id
    ajax('GET', path, '', callback)
    //    get(path, callback)
}

// 更新一个 todo
var apiTodoUpdate = function(form, callback) {
    var path = '/api/todo/update'
    ajax('POST', path, form, callback)
    //    post(path, form, callback)
}

// load weibo all
var apiWeiboAll = function(callback) {
    var path = '/api/weibo/all'
    ajax('GET', path, '', callback)
}

// 增加一个 todo
var apiWeiboAdd = function(form, callback) {
    var path = '/api/weibo/add'
    ajax('POST', path, form, callback)
}
