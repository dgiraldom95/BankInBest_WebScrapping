from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import bs4


def obtenerCDT():
    url = 'https://www.bancofalabella.com.co/simulador-cdt'
    tasas = {}

    driver = webdriver.Chrome()

    # Los plazos con los cuales se van a calcular las tasas
    plazos = range(60, 540, 30)

    try:
        # Obtiene la tabla de tasas para cada plazo
        for i in plazos:
            driver.get(url)
            driver.switch_to.frame(
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "iframe"))))
            # Se selecciona el monto de la inversión como 1 millons
            ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "valor")))
            ele.send_keys('1000000')

            # Se selecciona el plazo
            ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "plazo")))
            ele.click()
            ele.send_keys(str(i))

            # Se selecciona tipo de CDT (solo hay uno)
            ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "TipoSelect")))
            select = Select(ele)
            select.select_by_visible_text('CDT tasa fija')

            # Se selecciona periocidad mensual
            ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "periodicidadSelect")))
            select = Select(ele)
            select.select_by_visible_text('Mensual')

            # Se hace click en el boton calcular
            ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "SimularCDT")))
            ele.click()

            # Espera a que se actualizen las tasas del cdt
            flagUpdate = False
            while not flagUpdate:
                # Elemento que tiene la tasa
                ele = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div[1]/div[1]/p[2]')))

                # String de la tasa, si no tiene '%' hay un error
                tasaString = ele.text.split()
                if tasaString[1] != '%':
                    raise Exception('Elemento no es la tasa')

                # Repite hasta que la tasa deje de ser 0
                if float(tasaString[0]) > 0:
                    flagUpdate = True
                    tasa = float(tasaString[0])
                    tasas[i] = tasa


    finally:
        # Cierra el webdriver
        driver.quit()

    return tasas
