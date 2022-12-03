import time

from selenium.webdriver.common.by import By


def añadirIphoneSetoCart(driver):
    clickOnIphone = driver.find_element(By.XPATH, '//ul[@class="ac-gn-list"]//child::li[5]')
    clickOnIphone.click()

    time.sleep(3)

    driver.execute_script("window.scroll(0, 2550)")

    time.sleep(3)

    buyButtonIphoneSE = driver.find_element(By.XPATH, "//li[@class='typography-hero-copy cta-link']//a[@aria-label='Buy iPhone SE'][normalize-space()='Buy']")
    buyButtonIphoneSE.click()

    time.sleep(3)

    iphoneColor = driver.find_element(By.XPATH,  '//ul[@class="colornav-items"]//child::li[2]')
    iphoneColor.click()

    time.sleep(5)

    iphoneStorage = driver.find_element(By.XPATH, "//span[contains(text(), '256')]")
    iphoneStorage.click()

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

    driver.save_screenshot('./capturas/image2.png')

    time.sleep(10)