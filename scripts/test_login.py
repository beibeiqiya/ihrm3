import pytest

from api.login_api import LoginApi
from common.get_assert import get_assert
from common.get_jsondata import get_jsondata


class TestLogin:
    jsonpath = "D:\pyworkspace\ihrm3\data\login.json"
    @pytest.mark.parametrize("mobile,password,status_code,success,code,message",get_jsondata(jsonpath))
    def test_login(self,mobile,password, status_code, success, code, message):
        response1 = LoginApi.login_api(mobile,password)
        print(response1.json())
        get_assert(status_code, success, code, message, response1)


if __name__ == '__main__':
    TestLogin.test_login()

