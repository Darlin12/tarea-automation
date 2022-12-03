import time

from selenium.webdriver.common.by import By


def removerItem(driver):
    shoppingBagNavBar = driver.find_element(By.XPATH, '//ul[@class="ac-gn-list"]//child::li[13]')
    shoppingBagNavBar.click()

    time.sleep(9)

    bag = driver.find_element(By.XPATH, '//ul[@class = "ac-gn-bagview-nav-list "]//child::li[1]')
    bag.click()

    time.sleep(6)

    # to change the item to remove just change the index of bag-item, actual index is 2
    removeItem = driver.find_element(By.XPATH,
                                     '//li[@class= "rs-bag-item rs-iteminfo-wrap"][@data-autom="bag-item-2"]//child::button[@class="rs-iteminfo-remove as-buttonlink"] ')
    removeItem.click()

    time.sleep(8)