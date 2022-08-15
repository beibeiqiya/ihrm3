import json


def get_jsondata(jsonpath):
    with open(file=jsonpath,mode="r",encoding="utf8") as f:
        jsondata = json.load(f)
        jsonlist = []
        for i in jsondata:
            value = tuple(i.values())
            jsonlist.append(value)
        print(jsonlist)
        return jsonlist


if __name__ == '__main__':
    get_jsondata("D:\pyworkspace\ihrm3\data\login.json")
