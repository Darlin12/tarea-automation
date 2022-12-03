import time

from selenium.webdriver.common.by import By


def añaddirAirpods3ToCart(driver):
    clickOnAirpod = driver.find_element(By.XPATH, "//a[@class='ac-gn-link ac-gn-link-airpods']")
    clickOnAirpod.click()

    time.sleep(5)

    driver.execute_script("window.scrollTo(0,1250)")

    time.sleep(5)

    buyButtonAirpods = driver.find_element(By.XPATH, "//a[@aria-label='Buy AirPods (3rd generation)']//span[@class='icon-copy'][normalize-space()='Buy']")
    buyButtonAirpods.click()

    time.sleep(5)

    driver.execute_script("window.scrollTo(0,550)")
    magSafeOption = driver.find_element(By.XPATH, "//span[contains(text(), 'MagSafe Charging Case')]")
    magSafeOption.click()

    addToCart = driver.find_element(By.XPATH, "//button[@id='add-to-cart']")
    addToCart.click()

    driver.save_screenshot('./capturas/image1.png')

    time.sleep(5)