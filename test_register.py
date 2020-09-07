import unittest
from register import register


class TestRegister(unittest.TestCase):
    """注册接口测试用例类"""

    def test_register_success(self):
        """注册成功"""
        data = ("zhangtest", "zhang123456", "zhang123456")  # 测试数据
        expected = {'code': 200, 'msg': '注册成功！'}  # 预期结果
        result = register(*data)  # 把测试数据传到被测试的代码，接收实际结果
        self.assertEqual(expected, result)  # 断言，预期结果与实际结果是否一致，一致即用例通过

    def test_username_isnull(self):
        """注册失败，用户名为空"""
        data = ("", "zhang123456", "zhang123456")  # 测试数据
        expected = {'code': 0, 'msg': '所有参数不能为空！'}  # 预期结果
        result = register(*data)  # 把测试数据传到被测试的代码，接收实际结果
        self.assertEqual(expected, result)  # 断言，预期结果与实际结果是否一致，一致即用例通过
