import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def checkOutApplePurchase(driver):
    checkOut = driver.find_element(By.XPATH, '//button[@id="shoppingCart.actions.checkout"]')
    checkOut.click()

    time.sleep(3)

    continueAsGuest = driver.find_element(By.XPATH, "//button[@id='signIn.guestLogin.guestLogin']")
    continueAsGuest.click()

    time.sleep(3)

    inputLocation = driver.find_element(By.XPATH,
                                        '//input[@id="checkout.fulfillment.pickupTab.pickup.storeLocator.searchInput"]')
    inputLocation.send_keys("New York")
    time.sleep(3)
    inputLocation.send_keys(Keys.ENTER)

    selectStore = driver.find_element(By.XPATH,
                                      '//ul[@class="rt-storelocator-store-group form-selector-group"]//child::li[5]')
    selectStore.click()

    time.sleep(3)

    dateToPickUp = driver.find_element(By.XPATH, '//ul[@class="rs-pickup-slotgroup"]//child::li[2]')
    dateToPickUp.click()

    time.sleep(3)

    timeToPickUp = Select(driver.find_element(By.XPATH,
                                              '//select[@id="checkout.fulfillment.pickupTab.pickup.timeSlot.dateTimeSlots.timeSlotValue"]'))
    timeToPickUp.select_by_visible_text('8:45 a.m. – 9:00 a.m.')

    time.sleep(3)

    continuePickUpDetails = driver.find_element(By.XPATH, '//button[@id="rs-checkout-continue-button-bottom"]')
    continuePickUpDetails.click()

    time.sleep(3)

    firstName = driver.find_element(By.XPATH, "//input[@name='firstName']")
    firstName.send_keys('Darlin Manuel')
    lastName = driver.find_element(By.XPATH, "//input[@name='lastName']")
    lastName.send_keys('Casado Perez')
    emailAddress = driver.find_element(By.XPATH, "//input[@name='emailAddress']")
    emailAddress.send_keys('darlinmanuelcasdo@gmail.com')
    phoneNumber = driver.find_element(By.XPATH, "//input[@name='fullDaytimePhone']")
    phoneNumber.send_keys('8291546257')

    btnPayment = driver.find_element(By.XPATH, "//button[@id='rs-checkout-continue-button-bottom']")
    btnPayment.click()
