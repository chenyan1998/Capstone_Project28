import datetime
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
if __name__=='__main__':

    browser=webdriver.Chrome()
    web_link='https://forms.office.com/'
    browser.get(web_link)
    browser.maximize_window()
    WebDriverWait(browser,30,0.2).until(lambda x:x.find_element_by_xpath("/html/body/div[2]/div/div/header/div/div/div[2]/div[2]/div/div"))
    sleep(10)
    browser.switch_to.default_content()
    browser.find_element_by_xpath('/html/body/div[2]/div/div/header/div/div/div[2]/div[2]/div/div').click()
    sleep(10)
    browser.switch_to_frame('hrdIframe')
    browser.find_element_by_xpath('/html/body/div[2]/div/main/div[2]/div[2]/div/input').send_keys('qinruitang911@gmail.com')
    sleep(3)
    browser.find_element_by_xpath('/html/body/div[2]/div/main/div[2]/div[4]/input').click()
    sleep(10)
    browser.find_element_by_name('passwd').send_keys('Sutd0911')
    sleep(3)
    browser.find_element_by_xpath('/html/body/div/form[1]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div/div/input').click()
    sleep(3)
    browser.find_element_by_xpath('/html/body/div/form/div[1]/div/div[1]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div[1]/input').click()
    sleep(10)
    browser.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[1]/div/button/div[1]/i').click()
    sleep(3)
    browser.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div/div[1]/div[2]/div[2]/div[2]/button[1]/div/div[2]').click()
    sleep(3)
    browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div[4]/div/div/button/div').click()
    sleep(3)
    browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div[8]/div/div[2]/div').click()
    sleep(10)
    browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div[9]/div/div/div/div[3]/div[2]/div/button').click()
    sleep(20)
    print('finished')
    