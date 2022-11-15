from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def connectToGiphy():
	options = webdriver.ChromeOptions()
	driver = webdriver.Chrome(executable_path="chromedriver")
	driver.maximize_window()
	driver.get("https://giphy.com/login")
	driver.implicitly_wait(0.5)
	username = driver.find_element(by=By.NAME, value="email")
	password = driver.find_element(by=By.NAME, value="password")
	username.send_keys("amitmenashe2@gmail.com")
	password.send_keys("seLenium1212")
	login_button = driver.find_element(By.XPATH, '//button[text()="Log in"]')
	login_button.click()
	sleep(2)
	driver.get("https://giphy.com/upload")
	sleep(2)
	gif = driver.find_element(By.XPATH, '//input[@type="file"]')
	gif.send_keys("C:\\Users\\Amit\\Desktop\\memcycoProj\\computerKid.gif")
	sleep(6)
	upload = driver.find_element(By.XPATH, '//div[@class="GradientBlock-sc-mtbfu0 GradientButton-sc-o939k5 enZVFv edtalM Button-sc-o4kshr djHNTu"]')
	sleep(10)
	upload.click()
	sleep(40)
	driver.get_screenshot_as_file('selenium_screenshot.jpeg')
	driver.quit()

connectToGiphy()
