import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.zbj.com/search/service/?kw=saas&r=2')
page_source = driver.page_source
time.sleep(10)
print(page_source)
with open('acg.html',mode='w',encoding='utf-8') as f:
    f.write(page_source)
driver.quit()
