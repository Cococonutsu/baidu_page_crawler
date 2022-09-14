import requests
import json
import time
import re
import faker
faker = faker.Faker('zh_CN')

class GetPage():
    def __init__(self, url, path, circulate_time):
        headers = {
            'User-Agent' : str(faker.chrome())
        }
        self.headers = headers
        self.url = url
        self.path = path
        self.circulate_time = circulate_time

    def get_shufa(self):
        url = self.url
        # 预加载正则表达式
        obj_1 = re.compile(r'&pn=(?P<param>\d+)&',re.S)
        # 筛选出原来的pn参数
        old_param = int(obj_1.findall(url)[0])
        # 取一个完整的原来的pn参数,取这个整体用来做替换
        old_change_param = f'&pn={old_param}&'
        # 让pn参数变成0，从0开始
        start_param = f'&pn=0&'
        # 进行替换
        new_url = url.replace(old_change_param, start_param)
        param_num = 0
        url_list = []
        for i in range(self.circulate_time):
            try:
                resp_json = requests.get(url = new_url, headers = self.headers).json()
                for j in range(30):
                    url_list.append(resp_json['data'][j]['thumbURL'])
                # 循环对pn参数进行替换
                old_param = f'&pn={param_num}&'
                param_num += 30
                new_param = f'&pn={param_num}&'
                new_url = new_url.replace(old_param , new_param)
                print(f'已完成第【{i+1}】页的请求')
                time.sleep(1)
            except KeyError:
                print(f'至多只能获取【{i}】页')
                break

        page_num = 1
        url_list = list(set(url_list))
        for page_url in url_list:
            resp_content = requests.get(url = page_url, headers = self.headers).content
            with open(f'{self.path}/{page_num}.jpg','wb')as file:
                file.write(resp_content)
                print(f'下载图片 {page_num}/{len(url_list)} ')
                page_num += 1
                time.sleep(0.8)


if __name__ == '__main__':
    baidu_url = input('请输入需要爬取的百度图片的url: ')
    # save_path = r'D:\vs code\vs  code file\爬虫程序\baidu_page_crawler'
    save_path = input('请输入你要将这些图片保存的文件夹地址: ')
    circulate_time = int(input('请输入需要爬取的循环数量(一次循环30张图片):'))
    a = GetPage(url = baidu_url, path = save_path, circulate_time = circulate_time )
    a.get_shufa()


