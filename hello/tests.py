from django.test import TestCase

# Create your tests here.
class HelloTestCase(TestCase):
    def SetUp(self):
        # 环境构造
        pass
    def test_my_func(self):
        # 测试my_func方法
        print("[Test:] HelloTestCase")