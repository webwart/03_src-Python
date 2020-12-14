from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.python.org/")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()


'''

from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://django.webwart.atria.uberspace.de/')
# assert 'Willkommen zu Django' in browser.title
assert 'Page not found at /' in browser.title
print("Test comleted")
browser = quit()

'''
