from selenium import webdriver
browser = webdriver.Firefox()
browser.get('C:\\Users\\rwarth\Documents\\SBP-Biblio\\TestExports\\160204_Island-ShowAllFields.xml')
assert 'IIS Windows' in browser.title
print("Test comleted")
browser = quit()
