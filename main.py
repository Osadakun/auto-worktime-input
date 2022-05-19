from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert

import config
import datetime
import random
import time

dt_now = datetime.datetime.now()
dt_now_date = dt_now.day

driver = webdriver.Chrome(ChromeDriverManager().install())                    # 毎回自動で最新のdriverに更新してくれる
driver.implicitly_wait(10)                                                    # 最大で10秒待ち
driver.maximize_window()                                                      # 画面サイズを最大に
driver.get(config.portal_url)                                                 # 学生ポータルを開く

driver.find_element_by_name("uid").send_keys(config.number)                   # 学籍番号入力
driver.find_element_by_name("pw").send_keys(config.password)                  # パスワード入力
driver.find_element_by_id("StudentLoginBtn").click()                          # ログインボタンクリック
driver.get(config.work_url)                                                   # 学生勤務管理を開く
driver.find_element_by_xpath("//*[@id=\"insertButton\"]").click()             # 勤務実績をクリック
driver.find_element_by_xpath("//*[@id=\"insKnm%d\"]" %dt_now_date).click()    # 今日の日付をクリック

driver.find_element_by_id("knmsbt").click()
driver.find_element_by_xpath("//*[@id=\"knmsbt\"]/option[2]").click()         # 該当授業をクリック
driver.find_element_by_id("timeDialog").click()                               # 授業時間選択をクリック
driver.find_element_by_xpath("//*[@id=\"timeId2\"]").click()                  # 3限をクリック
driver.find_element_by_xpath("//*[@id=\"timeId3\"]").click()                  # 4限をクリック
driver.find_element_by_xpath("//*[@id=\"confirmButton\"]/span").click()       # OKをクリック

driver.find_element_by_id("knmniySel").click()
driver.find_element_by_xpath("//*[@id=\"knmniySel\"]/option[2]").click()      # 授業時間の業務を選択
driver.find_element_by_id("knmniyText").send_keys(random.choice(config.item)) # ランダムにしたことを入力
driver.find_element_by_xpath("//*[@id=\"dialogButtonIDIns\"]/span").click()   # 登録をクリック
Alert(driver).accept()