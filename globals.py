# print(globals())
# # 用法
# globals()['a'] = '用例a返回的结果'
# # 用例b引用
# b = globals()['a']
# print(b)
import unittest
import requests


class TestA(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()
        self.g = globals()

    def test_a(self):
        """用例a"""
        result_a = 'aaaaa'  # 用例a的返回值

        # 返回值先给全部办理，存到字典对应的key
        self.g['a'] = result_a
        self.assertEqual(result_a, 'aaaaa')

    def test_b(self):
        '''用例b'''
        b = self.g['a']  # 引用用例a的返回值
        print("用例b引用用例a的返回值：%s" % b)
        result_b = b + '1111'
        self.g['b'] = result_b
        self.assertEqual(result_b, 'aaaaa1111')

    def test_c(self):
        '''用例c'''
        print("用例c依赖用例a和b")
        c_a = self.g['a']
        c_b = self.g['b']
        print("用例c的请求参数：%s" % c_a)
        print("用例c的请求参数：%s" % c_b)


if __name__ == '__main__':
    unittest.main()
