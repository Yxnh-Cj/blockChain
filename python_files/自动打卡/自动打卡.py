# !/user/bin/env python3
# -*- coding: utf-8 -*-
# Author:Euler
import time
from lxml import etree
from selenium import webdriver
from chaojiying import Chaojiying_Client
from selenium.webdriver.chrome.options import Options


class auto_login_(object):
    def __init__(self):
        pass

    def auto_login(username1, password1):
        # 1.创建谷歌浏览器对象
        options_ = Options()
        options_.add_argument('--headless')
        chrome_obj = webdriver.Chrome(options=options_)
        # 2.给百度发送请求（访问百度）
        chrome_obj.get("http://202.203.16.42")
        chrome_obj.maximize_window()
        chrome_obj.find_element_by_id('username').send_keys(username1)
        chrome_obj.find_element_by_id('password').send_keys(password1)

        # 验证码
        # if etree.HTML(chrome_obj.page_source).xpath('/html/body/div[1]/div[2]/div/div/div[2]/div/form/ul/li[3]/div/input') != []:  # 无验证码
        #     img_src = chrome_obj.find_element_by_id('code')
        #     # print(img_src)
        #     # 获取图片位置 screenshot 指定位置截图
        #     img_src.screenshot('验证码.png')
        #     chaojiying = Chaojiying_Client('yxnh123', '111222', '922590')  # 用户中心>>软件ID 生成一个替换 96001
        #     im = open('验证码.png', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
        #     result = chaojiying.PostPic(im, 1902)['pic_str']  # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
        #     print(result)
        #     chrome_obj.find_element_by_id('verification').send_keys(result)
        chrome_obj.find_element_by_xpath('//*[@id="loginForm"]/div/a').click()
        time.sleep(5)

        name = chrome_obj.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div/span').text
        chrome_obj.find_element_by_class_name('fold').click()
        # time.sleep(2)
        chrome_obj.find_element_by_xpath('//*[@id="1$cell$1"]/div/div/span/span[2]').click()
        # time.sleep(5)
        chrome_obj.find_element_by_xpath('//*[@id="2$cell$1"]/div/div/span[3]/span[2]').click()
        time.sleep(2)

        chrome_obj.switch_to.frame(chrome_obj.find_element_by_xpath('/html/body/div[1]/div/div[7]/div['
                                                                    '2]/div/table/tbody/tr/td[2]/div[2]/div[2]/iframe'))
        js1 = 'document.getElementById("1$cell$6");'
        chrome_obj.execute_script(js1)
        js2 = 'document.getElementsByClassName("mini-grid-cell-inner  mini-grid-cell-nowrap ");'
        chrome_obj.execute_script(js2)
        time.sleep(3)
        # chrome_obj.find_element_by_link_text('填报').click()  # 搜索填报
        if time.mktime(time.strptime(
                f"{time.localtime().tm_year}-{time.localtime().tm_mon}-{time.localtime().tm_mday} 05:00:00",
                '%Y-%m-%d %H:%M:%S')) <= time.time() <= time.mktime(time.strptime(
                f"{time.localtime().tm_year}-{time.localtime().tm_mon}-{time.localtime().tm_mday} 11:59:59",
                '%Y-%m-%d %H:%M:%S')):
            chrome_obj.find_element_by_xpath(
                '/html/body/div[2]/div/div/div[2]/div[4]/div[2]/div/table/tbody/tr[3]/td[4]/div/a[1]').click()  # 搜索早上填报
        elif time.mktime(time.strptime(
                f"{time.localtime().tm_year}-{time.localtime().tm_mon}-{time.localtime().tm_mday} 12:00:00",
                '%Y-%m-%d %H:%M:%S')) <= time.time() <= time.mktime(time.strptime(
                f"{time.localtime().tm_year}-{time.localtime().tm_mon}-{time.localtime().tm_mday} 16:59:59",
                '%Y-%m-%d %H:%M:%S')):
            chrome_obj.find_element_by_xpath(
                '/html/body/div[2]/div/div/div[2]/div[4]/div[2]/div/table/tbody/tr[4]/td[4]/div/a[1]').click()  # 搜索中午填报
        else:
            chrome_obj.find_element_by_xpath(
                '/html/body/div[2]/div/div/div[2]/div[4]/div[2]/div/table/tbody/tr[5]/td[4]/div/a[1]').click()  # 搜索晚上填报
        time.sleep(2)

        # print(etree.HTML(chrome_obj.page_source).xpath('/html/body/div[5]')[0])  # []是未打卡，<Element div at
        # 0x248f8e47400>打卡框 print(chrome_obj.page_source) chrome_obj.quit() 已打卡
        if etree.HTML(chrome_obj.page_source).xpath('/html/body/div[5]') != []:
            chrome_obj.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/div[2]/a[1]/span')  # 定位到确定标签
            chrome_obj.quit()
            print(name + '已打卡！')

        else:
            chrome_obj.switch_to.default_content()  # 回到主界面
            chrome_obj.switch_to.frame(chrome_obj.find_element_by_xpath('/html/body/div[1]/div/div[7]/div['
                                                                        '2]/div/table/tbody/tr/td[2]/div[2]/div['
                                                                        '3]/iframe'))  # 切层进入填报界面
            # time.sleep(2)
            chrome_obj.find_element_by_xpath('//*[@id="c1"]/span/span/span[2]/span').click()
            chrome_obj.find_element_by_xpath('//*[@id="mini-6$0"]/td[2]').click()

            chrome_obj.find_element_by_xpath('//*[@id="c2"]/span/span/span[2]/span').click()
            chrome_obj.find_element_by_xpath('//*[@id="mini-9$0"]/td[2]').click()
            #
            chrome_obj.find_element_by_xpath('/html/body/div[1]/div[3]/a[2]/span').click()
            # chrome_obj.find_element_by_xpath('//*[@id="mini-18"]/span').click()
            chrome_obj.quit()
            print(name + '自动打卡成功！')


if __name__ == '__main__':
    try:
        l2 = ['2019109149', '2019109144', '2019109127']
        for i in l2:
            username = i.strip()
            password = '@c' + username
            auto_login_.auto_login(username, password)
    except Exception as e:
        print(e)
