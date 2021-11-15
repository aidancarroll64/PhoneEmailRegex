from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://www.bing.com')
search = browser.find_element_by_css_selector('#sb_form_q')
search.send.send_keys('Tommy Emmanuel')
search.submit()
search = browser.find_element_by_css_selector('#b_results > li:nth-child(1) > h2 > a')
search.click()

