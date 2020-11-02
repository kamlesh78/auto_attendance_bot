from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

username = "your username here"
password = "your password here"

driver = webdriver.Firefox(executable_path=r'C:\driver\geckodriver.exe')
driver.get("http://45.116.207.86/moodle/login/index.php")
 
elem = driver.find_element_by_id("username").send_keys(username)
elem2 = driver.find_element_by_id("password").send_keys(password)
 

driver.find_element_by_id("loginbtn").click()

# TMC 101

def tmc101():
	try:
		driver.get("http://45.116.207.86/moodle/mod/attendance/view.php?id=473")
		d=driver.find_element_by_partial_link_text("Submit attendance")
		d.send_keys(Keys.DOWN)
		d.click()
		driver.find_element_by_id("id_status_149").click()
		driver.find_element_by_id("id_submitbutton").click()
	except NoSuchElementException:
		print("Attendance already marked")
		return
		
		
# TMC 102
def tmc102():
	try:
		driver.get("http://45.116.207.86/moodle/mod/attendance/view.php?id=645")
		d=driver.find_element_by_partial_link_text("Submit attendance")
		d.send_keys(Keys.DOWN)
		d.click()
		driver.find_element_by_id("id_status_353").click()
		driver.find_element_by_id("id_submitbutton").click()
	except NoSuchElementException:
		print("Attendance already marked")
		return
	
	
# TMC 103		
def tmc103():
	try:
		driver.get("http://45.116.207.86/moodle/mod/attendance/view.php?id=624")
		d=driver.find_element_by_partial_link_text("Submit attendance")
		d.send_keys(Keys.DOWN)
		d.click()
		driver.find_element_by_id("id_status_317").click()
		driver.find_element_by_id("id_submitbutton").click()
	except NoSuchElementException:
		print("Attendance already marked")
		return

	
def tmc104():
	try:
		driver.get("http://45.116.207.86/moodle/course/view.php?id=26")
		d = driver.find_elements_by_class_name("togglecompletion")
		for form in d:
			b = form.find_element_by_tag_name('button')
			b.send_keys(Keys.DOWN)
			value = b.find_element_by_tag_name('img').get_attribute('src')
			if value == "http://45.116.207.86/moodle/theme/image.php/boost/core/1602071174/i/completion-manual-n":
				b.click()
	except NoSuchElementException:
		print("Attendance already marked")
		return
	
# TMC 105
def tmc105():
	try:
		driver.get("http://45.116.207.86/moodle/mod/attendance/view.php?id=1184")
		d=driver.find_element_by_partial_link_text("Submit attendance")
		d.send_keys(Keys.DOWN)
		d.click()
		driver.find_element_by_id("id_status_845").click()
		driver.find_element_by_id("id_submitbutton").click()
	except NoSuchElementException:
		print("Attendance already marked")
		return	
# TMC 106		
def tmc106():
	try:
		driver.get("http://45.116.207.86/moodle/mod/attendance/view.php?id=525")
		d=driver.find_element_by_partial_link_text("Submit attendance")
		d.send_keys(Keys.DOWN)
		d.click()
		driver.find_element_by_id("id_status_193").click()
		driver.find_element_by_id("id_submitbutton").click()
	except NoSuchElementException:
		print("Attendance already marked")
		return	


 
	

tmc101()
tmc102()
tmc103()
tmc104()
tmc105()
tmc106()
 
