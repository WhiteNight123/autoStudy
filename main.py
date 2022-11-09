import requests
import time
import argparse


# 获取本期课程的id
def getId():
    param = {'time': time.time()}
    result = requests.get('http://stu.redrock.team/new_course.json', params=param)
    return result.json()['data'][0]['id']


# 开始学习
def study(openid, id):
    param = {'openid': openid, 'id': id}
    result = requests.get('http://stu.redrock.team/api/course/studyCourse', params=param)
    print(result.text.encode().decode("unicode_escape"))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='请输入openid')
    parser.add_argument('-openid', help='根据openid自动学习')
    openid = parser.parse_args().openid
    id = getId()
    study(openid, id)
