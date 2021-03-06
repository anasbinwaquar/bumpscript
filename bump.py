from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver import ActionChains
import getpass
import random
from datetime import datetime

def Bump(driver):
	page_count=1
	url='https://backpack.tf/classifieds?page='+str(page_count)+'&steamid=76561198086548576'
	time.sleep(1)
	driver.get(url)
	while(True):
		url='https://backpack.tf/classifieds?page='+str(page_count)+"&steamid=76561198086548576"
		soup=BeautifulSoup(driver.page_source,'html.parser')
		buttons=soup.findAll('a',{"class":"btn btn-xs btn-bottom btn-default listing-relist listing-bump"})
		for button in buttons:
			# print(button["href"])
			# buttons=soup.findAll('a',{"class":"btn btn-xs btn-bottom btn-default listing-relist listing-bump"})
			text=".//a[@href=\'"+button["href"]+"\']"
			clickpath='//*[@id="page-content"]/div/div/div/div[2]/div/div[2]/div[2]/a[2]'
			time.sleep(1)
			if(page_count>1):
				driver.get(url)
			try:
				driver.find_element_by_xpath(text).click()
				try:
					driver.find_element_by_xpath(clickpath).click()
				except:
					time.sleep(1)
					driver.find_element_by_xpath('//*[@id="page-content"]/div/div/div/div[2]/div/div[2]/div[2]/a').click()
				time.sleep(random.randint(1,3))
			except Exception as e:
				print(e)
		disabled=driver.find_elements_by_xpath("//main[@class='container']/child::nav/child::ul/child::li[@class='disabled']/child::a/child::i[@class='fa fa-angle-right']")
		if(len(disabled)>=1):
			break
		buttons.clear()
		time.sleep(1)
		page_count+=1
		next_arrow=driver.find_element_by_xpath("//i[@class='fa fa-angle-right']").click()
		
	return

url = 'https://backpack.tf/classifieds?page=1&steamid=76561198086548576'
chrome_options = Options()
# chrome_options.add_argument("headless")
# chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--user-data-dir=C:\\Users\\Anas\\OneDrive\\Desktop\\Python Script\\chrome-data")
driver = webdriver.Chrome(executable_path='./driver/chromedriver.exe',options=chrome_options)
# driver.get(url)

# username=getpass.getpass("Enter username:")
# password=getpass.getpass("Enter pass:")
# # Find username textbox
# driver.get_screenshot_as_file("log.png")
# username_textbox = driver.find_element_by_id("steamAccountName")
# username_textbox.send_keys(username)

# # Find Password textbox
# password_textbox = driver.find_element_by_id("steamPassword")
# password_textbox.send_keys(password)

# # Hit login button
# login_button = driver.find_element_by_id("imageLogin")
# login_button.submit()

# time.sleep(1)

# # Input 2FA Code
# twofactor = getpass.getpass("Enter code: ")
# twofactor_textbox = driver.find_element_by_id("twofactorcode_entry")
# twofactor_textbox.send_keys(twofactor)

# twofactor_button = driver.find_element_by_xpath("//*[@id='login_twofactorauth_buttonset_entercode']/div[1]")
# twofactor_button.click()
# time.sleep(10)
# driver.get('https://backpack.tf/classifieds?steamid=76561198086548576')
# time.sleep(5)
Bump(driver)
bump=0
bump+=1
print("Bumped")
while(True):
	delay=random.randint(1,5)
	TT=1800+(delay*60)
	print("Total delay time ",TT/60,'mins')
	time.sleep(TT)
	Bump(driver)
	bump+=1
	print("Bumped after ",TT/60,' Bump count: ',bump)
