import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium import webdriver
from funciones.añadirIphoneSeACarrito import añadirIphoneSetoCart
from funciones.añadirAirpods3ToCart import añaddirAirpods3ToCart
from funciones.añadirIphone14proToCart import añadirIphone14ProToCart
from funciones.removerItemdelCart import removerItem
from funciones.checkOutApplePurchase import checkOutApplePurchase

def test_orderingAppleProducts():
    driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://www.apple.com/")

    time.sleep(5)

    #Escenario número 1
    #-------funcion para añadir airpod 3rd gen a carrito
    añaddirAirpods3ToCart(driver)

    # Escenario número 2
    # ------funcion para añadir iphone SE a carrito
    añadirIphoneSetoCart(driver)

    # Escenario número 3
    #-------funcion para añadir iphone 14 pro 128gb
    añadirIphone14ProToCart(driver)

    # Escenario número 4
    #-------funcion para remover iphone SE del carrito
    removerItem(driver)

    # Escenario número 5
    #funcion para proceder a check out
    checkOutApplePurchase(driver)

    time.sleep(10)