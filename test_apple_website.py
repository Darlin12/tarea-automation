import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from funciones.añadirIphoneSeACarrito import añadirIphoneSetoCart
from funciones.añadirAirpods3ToCart import añaddirAirpods3ToCart
from funciones.añadirIphone14proToCart import añadirIphone14ProToCart
from funciones.removerItemdelCart import removerItem
from funciones.checkOutApplePurchase import checkOutApplePurchase

def test_oderingAppleProducts():
    driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://www.apple.com/")

    time.sleep(5)

    #-------funcion para añadir airpod 3rd gen a carrito
    añaddirAirpods3ToCart(driver)

    # ------funcion para añadir iphone SE a carrito
    añadirIphoneSetoCart(driver)

    #-------funcion para añadir iphone 14 pro 128gb
    añadirIphone14ProToCart(driver)

    #-------funcion para remover iphone SE del carrito
    removerItem(driver)

    #funcion para proceder a check out
    checkOutApplePurchase(driver)

    time.sleep(10)