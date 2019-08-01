import allure, pytest


class Test003:

    def test_001(self):
        with open("./123.png", "rb") as f:
            allure.attach("截图", f.read(), allure.attach_type.PNG)
        assert True

