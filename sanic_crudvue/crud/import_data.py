"""
below to information is fake data or fiction data.Please don't take for reality.
"""

from .models import ShanghaiPersonInfo


# [{"id":1,"create_datetime":1495518486,"username":"baoer.gu","email":"gubaoer@hotmail.com","phone":"08613000001111","sex":"male","zone":"HongKou"}]

def generate_data():
    data_source = [
        {'username': 'baoer.gu', 'email': 'baoer.gu@hotmail.com', 'phone': '08613000001112', 'sex': 'male',
         "zone": "JingAn District"},
        {'username': 'yoyo.wu', 'email': 'yoyo.wu@gmail.com', 'phone': '08613000001113', 'sex': 'female',
         "zone": "JingAn District"},
        {'username': 'stacy.gao', 'email': 'stacy.gao@126.com', 'phone': '08613000001114', 'sex': 'female',
         "zone": "MinHang District"},
        {'username': 'yomiko.zhu', 'email': 'yomiko.zhu@qq.com', 'phone': '08613000001115', 'sex': 'female',
         "zone": "PuDong District"},
        {'username': 'hong.zhu', 'email': 'hong.zhu@163.com', 'phone': '08613000001116', 'sex': 'male',
         "zone": "YangPu District"},
        {'username': 'leon.lai', 'email': 'leon.lai@qq.com', 'phone': '08613000001117', 'sex': 'male',
         "zone": "JinShan District"},
        {'username': 'mark.lei', 'email': 'mark.lei@sohu.com', 'phone': '08613000001118', 'sex': 'male',
         "zone": "HuangPu District"},
        {'username': 'wen.liu', 'email': 'wen.liu@360.com', 'phone': '086130000011110', 'sex': 'male',
         "zone": "ChongMing District"},
        {'username': 'cai.lu', 'email': 'cai.lu@baidu.com', 'phone': '08613000001121', 'sex': 'female',
         "zone": "BaoShan District"},
        {'username': 'alex.li', 'email': 'alex.li@icee.com', 'phone': '08613000001122', 'sex': 'male',
         "zone": "ChangNing District"},
        {'username': 'sofia.xu', 'email': 'sofia.xu@qq.com', 'phone': '08613000001123', 'sex': 'female',
         "zone": "ZhaBei District"},
        {'username': 'cora.zhang', 'email': 'sofia.xu@gmail.com', 'phone': '08613000001124', 'sex': 'female',
         "zone": "XuHui District"},
        {'username': 'mark.gao', 'email': 'mark.gao@hotmail.com', 'phone': '08613000001125', 'sex': 'male',
         "zone": "HuangPu District"},
    ]

    for data_dict in data_source:
        ShanghaiPersonInfo.create(**data_dict)

    return 'ok'


if __name__ == '__main__':
    generate_data()