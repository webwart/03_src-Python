from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://localhost')
assert 'IIS Windows' in browser.title
print("Test comleted")
browser = quit()
