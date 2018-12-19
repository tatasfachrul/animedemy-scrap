from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = webdriver.ChromeOptions()
options.add_extension('./AdBlock_v3.36.0.crx')


driver = webdriver.Chrome(chrome_options=options)
driver.get("https://rainymood.com/")


driver.find_element_by_css_selector('.play').click()
