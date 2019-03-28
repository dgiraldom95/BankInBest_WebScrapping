from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import bs4


def obtenerCDT():
    url = 'https://www.grupobancolombia.com/wps/portal/personas/productos-servicios/inversiones/cdts/fisicos/simulador-cdt'
    tasas = {}

    driver = webdriver.Chrome('/Users/whatevercamps/PycharmProjects/BankInBest_WebScrapping/chromedriver')
   # driver = webdriver.Chrome(executable_path=r'C:/Users/Rouzajor/Desktop/Chrome Web Driver/chromedriver.exe')

    # Los plazos con los cuales se van a calcular las tasas
    plazos = range(60, 540, 30)

    try:
        # Obtiene la tabla de tasas para cada plazo
        for i in plazos:
            driver.get(url)

            # Se selecciona tipo de CDT como CDT Bancolombia
            ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "comboTipoCDT")))
            select = Select(ele)
            select.select_by_visible_text('CDT BANCOLOMBIA')

            # Se selecciona el monto de la inversión como 1 millon
            ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "textMontoInversion")))
            ele.click()
            ele.send_keys('1000000')

            # Se selecciona el plazo
            ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "textPlazoInversion")))
            ele.click()
            ele.send_keys(str(i))

            # Se selecciona periocidad de 1 mes
            ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "comboPeriodicidadInversion")))
            select = Select(ele)
            select.select_by_visible_text('Mensual')

            # Se hace click en el boton calcular
            ele = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="sim-detail"]/form/div[4]/button')))
            ele.click()

            # Espera a que aparezca la tabla de tasas
            ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'table-datos')))

            # Se obtiene el html de la pagina
            elem = driver.find_element_by_xpath("//*")
            html = elem.get_attribute("outerHTML")

            # Se instancia el BeautifulSoup a partir del html
            soup = BeautifulSoup(html, 'html.parser')

            # Se encuentra la tabla numero 2, que es la que contiene las tasas
            tabla = soup.find_all("table", {"class": "table-datos"})[1]
            # Se obtiene el tbody de la tabla
            tabla = tabla.find('tbody')

            filas = []  # Filas de la tabla
            # Convierte la tabla a una lista de listas (filas, columnas) con los contenidos de cada columna (solo texto
            for child in tabla.children:
                if type(child) is bs4.Tag:
                    cols = []  # Columnas en la fila de la tabla

                    for td in child.children:
                        if type(td) is bs4.Tag:
                            cols.append(td.string) #Se obtiene el texto del td

                    filas.append(cols)

            # La fila de los plazos es la segunda, la fila de las tasas es la tercera
            filaPlazo = filas[1]
            filaTasas = filas[2]

            # El plazo y la tasa estan de la segunda columna en adelante
            for plazoString, tasa in zip(filaPlazo[1:], filaTasas[1:]):
                # Se obtiene el primer numero en el string del plazo como entero
                plazo = [int(s) for s in plazoString.split() if s.isdigit()][0]
                # Se obtiene la tasa como float, sin espacios y sin '%'
                tasa = float(tasa.strip('% '))
                # Se agrega la tasa y el plazo al diccionario
                tasas[plazo] = tasa

    finally:
        # Cierra el webdriver
        driver.quit()

    return tasas