import requests


class LoginApi:
    @classmethod
    def login_api(self,mobile,password):
        header_data = {"Content-Type":"application/json"}
        json_data = {"mobile":mobile,"password":password}
        response1 = requests.post(url="http://ihrm2-test.itheima.net/api/sys/login",
                                  headers=header_data,
                                  json=json_data)
        print(response1.json())
        return response1


if __name__ == '__main__':
    LoginApi.login_api("13800000002","123456")