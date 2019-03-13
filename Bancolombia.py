from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import bs4

def obtenerCDT():
    url = 'https://www.grupobancolombia.com/wps/portal/personas/productos-servicios/inversiones/cdts/fisicos/simulador-cdt'

    driver = webdriver.Chrome()
    plazo = 60

    try:
        driver.get(url)

        ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "comboTipoCDT")))
        select = Select(ele)
        select.select_by_visible_text('CDT BANCOLOMBIA')

        ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "textMontoInversion")))
        ele.click()
        ele.send_keys('1000000')

        ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "textPlazoInversion")))
        ele.click()
        ele.send_keys(str(plazo))

        ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "comboPeriodicidadInversion")))
        select = Select(ele)
        select.select_by_visible_text('Mensual')

        ele = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="sim-detail"]/form/div[4]/button')))
        ele.click()

        ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'table-datos')))
        elem = driver.find_element_by_xpath("//*")
        html = elem.get_attribute("outerHTML")

    finally:
        driver.quit()

    soup = BeautifulSoup(html, 'html.parser')

    tabla = soup.find_all("table", {"class": "table-datos"})[1]
    tabla = tabla.find('tbody')

    filas = []  # Filas de la tabla
    for child in tabla.children:
        if type(child) is bs4.Tag:
            cols = []  # Columnas en la fila de la tabla

            for td in child.children:
                if type(td) is bs4.Tag:
                    cols.append(td.string)

            filas.append(cols)

    print(filas)