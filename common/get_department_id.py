import requests

from config import token


def deparment_add(d_name, d_code):
    header_json = {"Content-Type": "application/json", "Authorization": token}
    json_data = {"name": d_name, "code": d_code}
    response1 = requests.post(url="http://ihrm2-test.itheima.net/api/company/department",
                              headers=header_json,
                              json=json_data)

    deparment_id = response1.json().get("data").get("id")

    return deparment_id