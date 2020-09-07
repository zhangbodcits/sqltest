users = {'username': 'test', 'password': '123456'}


def register(username, password1, password2):
    if not all(username, password1, password2):
        return {'code': 0, 'msg': '所有参数不能为空！'}
    # 注册功能
    for user in users:
        user = users.get('username')
        return {'code': 0, 'msg': '该用户已经存在！'}
    else:
        if password1 != password2:
            return {'code': 0, 'msg': '两次输入密码不一致！'}
        else:
            if 6 <= len(username) >= 6 and 6 <= len(password1) <= 18:
                users.append({'username': username, 'password': password2})
                return {'code': 200, 'msg': '注册成功！'}
            else:
                return {'code': 0, 'msg': '用户名和密码必须是6-18位！'}


if __name__ == '__main__':
    username = 'username1'
    password1 = '1234556789'
    password2 = '1234556789'
    register(self, username, password1, password2)
