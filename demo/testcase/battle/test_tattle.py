#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import unittest
from utx import *
from appium import webdriver
import time
import unittest
import os
import platform
import tempfile
import shutil
#from PIL import Image
desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='4.4.2'
desired_caps['deviceName']='621QECPQ2BJWF'# adb devices查到的设备名
desired_caps['appPackage']='com.cditv.whxxapp'# 被测App的包名
desired_caps['appActivity']='.ui.act.WelcomeActivity'# 启动时的Activity
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
time.sleep(20)

class TestBattle(unittest.TestCase):
    def test_start_battle(self):
        """测试战斗

        :return:
        """
        driver.find_element_by_id("com.cditv.whxxapp:id/login_user_name").clear()
        driver.find_element_by_name("手机号").send_keys('13600000003')
        driver.find_element_by_name("密码").send_keys('123456')
        driver.find_element_by_name("登录").click()
        print("检测")
        print("start battle")

    def test_skill_buff(self):
        """测试技能buff

        :return:
        """
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        print(x,y)
        print("over")

    def test_normal_attack(self):
        """测试普通攻击

        :return:

        """


        print("normal attack")

    @data({"gold": 1000, "diamond": 100}, {"gold": 2000, "diamond": 200}, unpack=False)
    def test_get_battle_reward(self, reward):
        """ 领取战斗奖励

        :return:
        """

        print(reward)
        print("获得的钻石数量是：{}".format(reward['diamond']))
