# _*_coding:utf-8_*_
# Author:liu
from wxpy import Bot
from PIL import Image
import math
import os
import shutil
import sys

'''
下载微信好友的头像并拼接所有的图片
'''


def down_img(friends):
        '''下载头像'''
    if not os._exists('./头像'):
        shutil.rmtree('./头像')
    os.mkdir('./头像')

    # 首先下载大家的头像到本地
    num = 0
    for friend in friends:
        # 遍历好友分组得到每个好友
        # print(friend)
        # friend.get_avatar() 获取好友头像
        # print(friend.get_avatar())

        # 获取好友头像并保存到本地
        img = friend.get_avatar()
        fileImage = open('./头像/' + str(num) + '.jpg', 'wb')
        fileImage.write(img)
        fileImage.close()
        num += 1
        print('正在下载第：' + str(num) + '位好友头像')


def show_img():
    '''借助plt的Image库进行头像拼接'''
   


def main():
    # 登录微信
    # bot = Bot(cache_path=True)

    # 获取好友列表
    # friends = bot.friends()

    # 下载好友头像
    # down_img(friends)

    # 拼接好友头像
    # show_img()


if __name__ == '__main__':
    main()
