URL = "http://challs.dvc.tf:6002/home?"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)

breakpoint()


driver.close()