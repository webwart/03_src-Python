from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://django.webwart.atria.uberspace.de/admin')
# assert 'Willkommen zu Django' in browser.title
assert 'Anmelden | Django-Systemverwaltung' in browser.title
print("Test comleted")
browser = quit()
