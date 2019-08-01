import allure

class Test001:

    @allure.step(title="打开首页")
    def test_001(self):
        allure.attach("输入url打开首页", " 进入网站首页")
        print("test_001")
        assert True

    @allure.step(title="进入个人中心")
    def test_002(self):
        allure.attach("点击我", " 进入个人中心")
        print("test_002")
        assert True

    @allure.step(title="查看订单历史")
    def test_003(self):
        allure.attach("点击我的订单", " 显示所有订单")
        print("test_003")
        assert True
