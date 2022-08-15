import requests


def get_new_token():
    header_data = {"Content-Type": "application/json"}
    json_data = {"mobile": "13800000002", "password": "123456"}
    response1 = requests.post(url="http://ihrm2-test.itheima.net/api/sys/login",
                              headers=header_data,
                              json=json_data)

    token = response1.json().get("data")
    print(token)
    return token


if __name__ == '__main__':
    get_new_token()