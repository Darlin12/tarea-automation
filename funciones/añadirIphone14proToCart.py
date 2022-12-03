import time

from selenium.webdriver.common.by import By


def añadirIphone14ProToCart(driver):
    clickOnIphone = driver.find_element(By.XPATH, '//ul[@class="ac-gn-list"]//child::li[5]')
    clickOnIphone.click()

    time.sleep(3)

    driver.execute_script("window.scroll(0,1450)")

    buyButtonIphone14Pro = driver.find_element(By.XPATH, "//a[@data-analytics-title= 'buy - iphone 14 pro']")
    buyButtonIphone14Pro.click()

    time.sleep(3)

    selectIphone14Pro = driver.find_element(By.XPATH, '//span[@class = "form-selector-title"][contains(text(), "iPhone 14 Pro")]')
    selectIphone14Pro.click()

    time.sleep(3)

    selectIphoneColor = driver.find_element(By.XPATH, '//ul[@class="colornav-items"]//child::li[3]')
    selectIphoneColor.click()

    time.sleep(3)

    selectIphone14ProStorage = driver.find_element(By.XPATH, '//span[@class = "form-selector-title"][contains(text(), "128")]')
    selectIphone14ProStorage.click()

    time.sleep(3)

    noTradeInOption = driver.find_element(By.XPATH, "//*[contains(text(), 'No trade-in')]")
    noTradeInOption.click()

    time.sleep(3)

    payInFull = driver.find_element(By.XPATH, "//*[contains(text(), 'Pay the total amount today.')]")
    payInFull.click()

    time.sleep(3)

    selectCarrier = driver.find_element(By.XPATH, '//ul[@aria-labelledby="carrierModel"]//child::div[5]')
    selectCarrier.click()

    time.sleep(3)

    selectNoAppleCare = driver.find_element(By.XPATH, "//*[contains(text(), 'No AppleCare+ coverage')]")
    selectNoAppleCare.click()

    time.sleep(3)

    addToBag = driver.find_element(By.XPATH, '//button[@name = "add-to-cart"]')
    addToBag.click()

    driver.save_screenshot('./capturas/image3.png')

    time.sleep(10)