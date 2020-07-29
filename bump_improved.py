from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver import ActionChains
import getpass
import random
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

def Bump():
	chrome_options = Options()
	chrome_options.add_argument("headless")
	chrome_options.add_argument("--no-sandbox")
	chrome_options.add_argument("--user-data-dir=C:\\Users\\Anas\\OneDrive\\Desktop\\Python Script\\chrome-data")
	driver = webdriver.Chrome(executable_path='./driver/chromedriver.exe',options=chrome_options)
	page_count=1
	url='https://backpack.tf/classifieds?page='+str(page_count)+'&steamid=76561198086548576'
	time.sleep(1)
	driver.get(url)
	while(True):
		url='https://backpack.tf/classifieds?page='+str(page_count)+"&steamid=76561198086548576"
		soup=BeautifulSoup(driver.page_source,'html.parser')
		buttons=soup.findAll('a',{"class":"btn btn-xs btn-bottom btn-default listing-relist listing-bump"})
		for button in buttons:
			text=".//a[@href=\'"+button["href"]+"\']"
			clickpath='//*[@id="page-content"]/div/div/div/div[2]/div/div[2]/div[2]/a[2]'
			time.sleep(1)
			click(driver, text)
		try:
			disabled=driver.find_elements_by_xpath("//main[@class='container']/child::nav/child::ul/child::li[@class='disabled']/child::a/child::i[@class='fa fa-angle-right']")
		except:
			pass
		if(len(disabled)>=1):
			break
		buttons.clear()
		page_count+=1
		try:
			next_arrow=driver.find_element_by_xpath("//i[@class='fa fa-angle-right']").click()	
		except:
			pass
	driver.quit()
	return

def click(driver,text):
	actionChains = ActionChains(driver)
	item=driver.find_element_by_xpath(text)
	try:
		actionChains.move_to_element(item).context_click(item).perform()
	except:
		time.sleep(1)
		buttons=soup.findAll('a',{"class":"btn btn-xs btn-bottom btn-default listing-relist listing-bump"})
		actionChains.move_to_element(item).context_click(item).perform()

url = 'https://backpack.tf/classifieds?page=1&steamid=76561198086548576'
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
Bump()
bump=0
bump+=1
print("Bumped")
while(True):
	delay=random.randint(1,5)
	TT=1800+(delay*60)
	print("Total delay time ",TT/60,'mins')
	time.sleep(TT)
	try:
		Bump()
		check=1
	except:
		Bump()
		pass
	bump+=1
	print("Bumped after ",TT/60,' Bump count: ',bump)
