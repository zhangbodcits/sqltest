import unittest
from register import register


class TestRegister(unittest.TestCase):
    """注册接口测试用例类"""

    def setUp(self):
        # 每条用例执行前都会被执行
        print('用例{}开始执行'.format(self))

    def tearDown(self):
        # 每条用例执行之后都会被执行
        print('用例{}执行结束'.format(self))

    @classmethod  # 指明这个类方法是以类为维度去执行的
    def setUpClass(cls):
        # 整个测试用例类执行之前，会先执行此方法
        print("-----setup-----class-----")

    @classmethod  # 指明这个类方法是以类为维度去执行的
    def tearDownClass(cls):
        # 整个测试用例类执行之前，会先执行此方法
        print("-----teardown-----class-----")

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

    def test_username_lt6(self):
        """注册失败，用户名大于18位"""
        data = ("zhangtestzhangtestzhangtest", "zhang123456", "zhang123456")  # 测试数据
        expected = {'code': 0, 'msg': '用户名和密码必须是6-18位！'}  # 预期结果
        result = register(*data)  # 把测试数据传到被测试的代码，接收实际结果
        self.assertEqual(expected, result)  # 断言，预期结果与实际结果是否一致，一致即用例通过

    def test_pwd1_not_pwd2(self):
        """注册失败，两次输入密码不一致"""
        data = ("zhangtest", "zhang123456", "zhang456456")  # 测试数据
        expected = {'code': 0, 'msg': '两次输入密码不一致！'}  # 预期结果
        result = register(*data)  # 把测试数据传到被测试的代码，接收实际结果
        self.assertEqual(expected, result)  # 断言，预期结果与实际结果是否一致，一致即用例通过


if __name__ == '__main__':
    unittest.main()
