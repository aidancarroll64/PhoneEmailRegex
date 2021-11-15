from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.python.org')
assert 'Python' in driver.title
elem = driver.find_element_by_name('q')
elem.clear()
elem.send_keys('aidn')
elem.send_keys(Keys.RETURN)
elem.find_element_by_css_selector('#content > div > section > form > ul > p')
assert 'No results found.' not in driver.page_source
drive.close()
