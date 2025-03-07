print("Hello World")


import pytest
from ..sum import add

# import selenium.webdriver
# from selenium.webdriver.common.by import Bom the root foldery
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import Select






def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

test_add()





# chrome_options = Options()
# chrome_options.add_argument("--headless=new")
# driver = selenium.webdriver.Chrome(options=chrome_options)

# print("aquiiiiiiiiiiiiiiiiiiiiiiiiiiiiii ------------------------------")
# start_url = "http://localhost:8000"
# driver.get(start_url)

# button = driver.find_element(By.ID, "name")
# button.click()

# dropdown = driver.find_element(By.TAG_NAME, "select")
# selection = Select(dropdown)

# selection.select_by_visible_text("English")

# selectelement = driver.find_element(By.ID, "first_name")
# selectelement.click()

# writeNumber = driver.find_element(By.ID, "number")
# writeNumber.send_keys(3)

# driver.find_element(By.ID, "generator").click()

# driver.implicitly_wait(10)

# listing=driver.find_elements(By.TAG_NAME, "thead")

# for name in range(len(listing)):
#     parent=listing[name].find_element(By.TAG_NAME, "tr")
#     child=parent.find_element(By.XPATH, ".//th")
#     print(child.get_attribute("innerHTML"))
