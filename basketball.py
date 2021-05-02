def checkInt(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.nba.com/players")

#select team name
#teamDD = Select(driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div[3]/section/div/div[2]/div[1]/div[2]/label/div/select'))
#teamDD.select_by_value('Cavaliers')

#all time
histDD = driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div[3]/section/div/div[2]/div[1]/div[6]/label/div/span')
histDD.click()

time.sleep(2)

#select All in page dropdown
pageDD = Select(driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div[3]/section/div/div[2]/div[1]/div[7]/div/div[3]/div/label/div/select'))
pageDD.select_by_value('-1')


r = driver.page_source

soup = BeautifulSoup(r, 'html.parser')

final = ''

#for each player
for i in soup.find_all('tr'):
    #get num
    for num in i.find_all('td'):
        if checkInt(num.text) or num.text == '':
            final += num.text
    #get name
    name = str(i.find(lambda tag: tag.name == 'p' and tag.get('class') == ['t6']))
    if name != 'None':
        final += name[14:-4]

print('Name' + final)

driver.quit()

