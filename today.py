# -*- coding: UTF-8 -*-
import math
import function
import url
import browerConfig
from bs4 import BeautifulSoup
import timer
import time
import datetime
import userConfig

if __name__ == "__main__":
    print('''
        欢迎使用秒选座外挂2020.3.9版 ________ Powered By WZC
        ''')
    session = userConfig.userinfo()
    first_Time = math.floor(time.time())
    result = function.myWork(url.pageIndex, browerConfig.initPageIndex(first_Time, session))
    if "您好" in result:
        userConfig.succeed("成功进入选座系统")
        html = function.myWork(url.pageCenter, browerConfig.initPageIndex(first_Time, session))
        soup = BeautifulSoup(html, "html.parser")
        print("您的个人信息如下：")
        for k in soup.find_all('div', class_='nick'):
            print("您的系统昵称：" + k.string)
        url_t = url.pageIndex
        if timer.timer_today():
            print(datetime.datetime.now())
            top_time = math.floor(time.time() * 1000)
            print(top_time)
            print("抢座中....................................")
            result = function.start_today(url_t, top_time, session)
            # 此为本地验证码 result = function.start_tomorrow(url_t, top_time, session)
            # 不成功则一直请求，可手动ctal+z关闭
            while "成功" not in result:
                result = function.start_today(url_t, top_time, session)
                print(result)
            print(result + "\n成功")
    else:
        userConfig.failed("进入选座系统失败,请检查Session值")
