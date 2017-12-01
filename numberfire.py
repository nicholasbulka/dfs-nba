username = "username-of-choice"
password = "password-of-choice"
location_to_chromedriver = "/Users/person/webdrivers/chromedriver"


import time
from selenium import webdriver
from lxml import html
import pandas

def number_fire_results():
    #log in to yahoo
    driver = webdriver.Chrome(location_to_chromedriver) 
    #driver = webdriver.PhantomJS('/usr/local/bin/phantomjs')
    url = 'http://www.yahoo.com';
    driver.get(url)
    time.sleep(1)
    link = driver.find_element_by_xpath('//*[@id="uh-signin"]')
    link.click()
    time.sleep(3)
    element = driver.find_element_by_xpath('//*[@id="login-username"]')
    element.send_keys(username)
    time.sleep(4.1)
    submit = driver.find_element_by_xpath('//*[@id="login-signin"]')
    submit.click()
    time.sleep(3.2)
    pw = driver.find_element_by_xpath('//*[@id="login-passwd"]')
    time.sleep(4.5)
    pw.send_keys(password)
    pwsubmit = driver.find_element_by_xpath('//*[@id="login-signin"]')
    time.sleep(4)
    pwsubmit.click()
    time.sleep(1)
    
    #go to numberfire
    numberfire = 'https://www.numberfire.com/account/login-yahoo'
    driver.get(numberfire)
    time.sleep(1)
    dk = 'http://www.numberfire.com/nba/daily-fantasy/daily-basketball-projections'
    driver.get(dk)
    dkclick = driver.find_element_by_xpath('//*[contains(concat(" ", normalize-space(@class), " "), "custom-drop__option-wrap")]/li[contains(text(), "DraftKings")]')
    driver.execute_script("$(arguments[0]).click();", dkclick)
    time.sleep(2)
    table = driver.find_element_by_xpath('//*[contains(concat(" ", normalize-space(@class), " "), "stat-table__body")]')
    htmlstring = table.get_attribute('innerHTML')
    root = html.fromstring(htmlstring)
    players = root.xpath('//*[@class="player-info"]/a[@class="full"]/text()')
    fpoints = root.xpath('//td[@class="fp active"]/text()')
    cost = root.xpath('//td[@class="cost"]/text()')
    value = root.xpath('//td[@class="value"]/text()')
    
    combined = zip(players,fpoints,cost,value)
    driver.close()
    driver.quit()
    
    
    nfdf = pandas.DataFrame(combined)
    nfdf[0] = nfdf[0].str.strip()
    nfdf[1] = nfdf[1].str.strip()
    nfdf[2] = nfdf[2].str.strip() 
    
    nfdf[3] = nfdf[3].str.strip()
     
     
    nfdf.to_csv("nf.csv")
    
    return

number_fire_results()