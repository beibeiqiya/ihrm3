import requests

from common.get_department_id import deparment_add
from common.get_token import get_new_token
from config import token


class DeparmentManageApi:
    def setup_class(self):
        self.token = get_new_token()


    # 添加部门
    @classmethod
    def deparment_add(cls,d_name,d_code):
        header_json = {"Content-Type":"application/json","Authorization": token}
        json_data = {"name": d_name, "code": d_code}
        response1 = requests.post(url="http://ihrm2-test.itheima.net/api/company/department",
                                  headers=header_json,
                                  json=json_data)
        print(response1.json())
        deparment_id = response1.json().get("data").get("id")
        print(deparment_id)
        return response1,deparment_id

    # 查询部门
    @classmethod
    def deparment_query(cls):
        deparment_id = deparment_add()
        header_json = {"Content-Type":"application/json","Authorization": token}
        response1 = requests.get(url="http://ihrm2-test.itheima.net/api/company/department/"+deparment_id,
                                  headers=header_json)
        print(response1.json())
        return response1

    # 修改部门
    @classmethod
    def deparment_query(cls):
        deparment_id = deparment_add()
        header_json = {"Content-Type":"application/json","Authorization": token}
        response1 = requests.put(url="http://ihrm2-test.itheima.net/api/company/department/"+deparment_id,
                                  headers=header_json)
        print(response1.json())
        return response1

    # 删除部门
    @classmethod
    def deparment_query(cls):
        header_json = {"Content-Type":"application/json","Authorization": token}
        response1 = requests.delete(url="http://ihrm2-test.itheima.net/api/company/department/"+deparment_id,
                                  headers=header_json)
        print(response1.json())
        return response1

if __name__ == '__main__':
    resp = DeparmentManageApi.deparment_add("程少商部","12321")
    DeparmentManageApi.deparment_query()