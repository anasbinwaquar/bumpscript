from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver import ActionChains
import getpass
import random

def Bump(driver):
	page_count=1
	url='https://backpack.tf/classifieds?page='+str(page_count)+"&steamid=76561198086548576"
	driver.get_screenshot_as_file("gg.png")
	while(True):
		url='https://backpack.tf/classifieds?page='+str(page_count)+"&steamid=76561198086548576"
		driver.get(url)
		time.sleep(1)
		soup=BeautifulSoup(driver.page_source,'html.parser')
		buttons=soup.findAll('a',{"class":"btn btn-xs btn-bottom btn-default listing-relist listing-bump"})
		if(len(buttons)>0):
			action=ActionChains(driver)
			for button in buttons:
				# print(button["href"])
				time.sleep(1)
				# buttons=soup.findAll('a',{"class":"btn btn-xs btn-bottom btn-default listing-relist listing-bump"})
				bplink='https://backpack.tf'+button["href"]
				text=".//a[@href=\'"+button["href"]+"\']"
				clickpath='//*[@id="page-content"]/div/div/div/div[2]/div/div[2]/div[2]/a[2]'
				driver.find_element_by_xpath(text).click()
				try:
					driver.find_element_by_xpath(clickpath).click()
				except:
					time.sleep(1)
					driver.find_element_by_xpath('//*[@id="page-content"]/div/div/div/div[2]/div/div[2]/div[2]/a').click()
				time.sleep(random.randint(1,3))
			page_count+=1
		else:
			break
	return

url = "https://steamcommunity.com/openid/login?openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.mode=checkid_setup&openid.return_to=http%3A%2F%2Fbackpack.tf%2Flogin&openid.realm=http%3A%2F%2Fbackpack.tf&openid.ns.sreg=http%3A%2F%2Fopenid.net%2Fextensions%2Fsreg%2F1.1&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select"
chrome_options = Options()
# chrome_options.add_argument("headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--user-data-dir=./chrome-data")
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

username=getpass.getpass("Enter username:")
password=getpass.getpass("Enter pass:")
# Find username textbox
driver.get_screenshot_as_file("log.png")
username_textbox = driver.find_element_by_id("steamAccountName")
username_textbox.send_keys(username)

# Find Password textbox
password_textbox = driver.find_element_by_id("steamPassword")
password_textbox.send_keys(password)

# Hit login button
login_button = driver.find_element_by_id("imageLogin")
login_button.submit()

time.sleep(1)

# Input 2FA Code
twofactor = getpass.getpass("Enter code: ")
twofactor_textbox = driver.find_element_by_id("twofactorcode_entry")
twofactor_textbox.send_keys(twofactor)

twofactor_button = driver.find_element_by_xpath("//*[@id='login_twofactorauth_buttonset_entercode']/div[1]")
twofactor_button.click()
time.sleep(10)
driver.get('https://backpack.tf/classifieds?steamid=76561198086548576')
time.sleep(5)
Bump(driver)
print("Bumped")
while(True):
	delay=random.randint(4,15)
	TT=1800+(delay*60)
	print("Total time ",TT/60)
	time.sleep(TT)
	Bump(driver)
	print("Bumped after ",TT/60)