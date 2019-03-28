from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import bs4

def obtenerCDT():
    url = 'https://www.bbva.com.co/personas/productos/inversion/cdt/tradicional/simulador.html'
    tasas = {}

    driver = webdriver.Chrome()

    # Los plazos con los cuales se van a calcular las tasas
    plazos = range(2, 16)

    try:
        driver.get(url)
        for i in plazos:
            # Se selecciona el plazo de CDT
            elem = driver.find_element_by_xpath("//*")
            html = elem.get_attribute("outerHTML")

            # Se instancia el BeautifulSoup a partir del html
            soup = BeautifulSoup(html, 'html.parser')
            print(soup.prettify())

            ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'headerTitle')))
            select = Select(ele)
            select.select_by_visible_text(str(i) + ' meses')

             # Se selecciona el monto de la inversión como 1 millon
            ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "resultSimulator\:j_idt6_input")))
            ele.click()
            ele.send_keys('1000000')

    finally:
        # Cierra el webdriver
        driver.quit()

    return tasas

